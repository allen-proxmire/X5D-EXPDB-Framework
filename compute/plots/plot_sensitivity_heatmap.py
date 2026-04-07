"""
Heat map of dθ/dA(σ) for θ_PNTALL.

The Ingham relation θ = 1 - 1/||A||_∞ means that only improvements
at σ values where A(σ) is near the supremum ||A||_∞ affect θ.

For a hypothetical improvement of magnitude ε applied at a single σ₀:
  - If A(σ₀) ≥ ||A||_∞ - ε:  the new ||A||_∞ drops, and Δθ ≈ -ε/||A||_∞²
  - If A(σ₀) < ||A||_∞ - ε:  no effect (the peak is elsewhere)

We visualize this as a continuous sensitivity field by defining:
  S(σ, ε) = max(0, 1 - headroom(σ)/ε) × (1/||A||_∞²)
where headroom(σ) = ||A||_∞ - A(σ).

For small ε, this concentrates sharply around σ* = 0.70.
"""

import sys, os, io
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'vendor', 'expdb', 'blueprint', 'src', 'python'))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import FancyArrowPatch
from fractions import Fraction as frac
import sympy

from literature import literature
import zero_density_estimate as zd
import zero_density_energy_estimate as ze
from functions import Interval
from reference import Reference
from hypotheses import Hypothesis_Set


def build_hs():
    hs = Hypothesis_Set()
    hs.add_hypotheses(literature.list_hypotheses(hypothesis_type="Zero density estimate"))
    hs.add_hypotheses(literature.list_hypotheses(hypothesis_type="Zero density energy estimate"))
    ref = Reference.make("Tao--Trudgian--Yang", 2024)
    zd.add_zero_density(hs, "2/(9*x - 6)", Interval("[17/22, 38/49]"), ref)
    zd.add_zero_density(hs, "9/(8*(2*x - 1))", Interval("[38/49, 4/5]"), ref)
    zd.add_zero_density(hs, "3/(10 * x - 7)", Interval("[701/1000, 1]"), ref)
    hs.add_hypotheses(zd.bourgain_ep_to_zd())
    zd.add_zero_density(hs, "3/(40 * x - 35)", Interval("[39/40, 40/41)"), ref)
    zd.add_zero_density(hs, "2/(13 * x - 10)", Interval("[40/41, 41/42)"), ref)
    hs.add_hypotheses([
        ze.literature_zero_density_energy_estimate(
            "5 * (18 - 19 * x) / ((2 * (5 * x + 3)) * (1 - x))",
            Interval(frac(7,10), 0.7255782330963900973348270455), ref),
        ze.literature_zero_density_energy_estimate(
            "2 * (45 - 44 * x) / ((2 * x + 15) * (1 - x))",
            Interval(0.7255782330963900973348270455, frac(3,4)), ref),
        ze.literature_zero_density_energy_estimate(
            "(197 - 220 * x) / (8 * (5 * x - 1) * (1 - x))",
            Interval(frac(3,4), frac(289,380)), ref),
        ze.literature_zero_density_energy_estimate(
            "3 * (29 - 30 * x) / (5 * (5 * x - 1) * (1 - x))",
            Interval(frac(289,380), 0.7929182893891673924914902646), ref),
        ze.literature_zero_density_energy_estimate(
            "(40 - 36 * x) / ((20 * x - 5) * (1 - x))",
            Interval(0.7929182893891673924914902646, frac(5,6)), ref),
    ])
    return hs


def main():
    print("Building hypothesis set...")
    hs = build_hs()
    best_zd = zd.best_zero_density_estimate(hs, verbose=False)
    x_sym = sympy.Symbol('x')

    def eval_A(sigma):
        for h in best_zd:
            if h.data.interval.contains(sigma):
                try:
                    return float(h.data.at(sigma))
                except:
                    return float(h.data.bound.subs(x_sym, sigma))
        return None

    # ---- Sample A(sigma) ----
    sigmas = np.linspace(0.501, 0.998, 2000)
    A_vals = np.array([eval_A(s) or 0.0 for s in sigmas])
    A_inf = np.max(A_vals)
    idx_star = np.argmax(A_vals)
    sigma_star = sigmas[idx_star]
    headroom = A_inf - A_vals

    # ---- Build the 2D sensitivity field ----
    # x-axis: sigma (0.50 to 1.00)
    # y-axis: epsilon (improvement magnitude), from 0.001 to 0.15
    # value:  S(sigma, eps) = max(0, 1 - headroom/eps) / A_inf^2

    eps_values = np.linspace(0.001, 0.15, 300)
    S = np.zeros((len(eps_values), len(sigmas)))

    base_sensitivity = 1.0 / A_inf**2  # = 169/900

    for j, eps in enumerate(eps_values):
        # fraction of improvement that "reaches" the peak from this sigma
        reach = np.clip(1.0 - headroom / eps, 0, 1)
        S[j, :] = reach * base_sensitivity

    # ---- Plot ----
    fig = plt.figure(figsize=(11, 6.5))

    # Use gridspec for the main plot + inset arrangement
    gs = fig.add_gridspec(1, 2, width_ratios=[1, 0.02], wspace=0.03)
    ax = fig.add_subplot(gs[0, 0])
    cax = fig.add_subplot(gs[0, 1])

    # Custom colormap: deep blue -> cyan -> yellow -> white at peak
    cmap = mcolors.LinearSegmentedColormap.from_list(
        'sensitivity',
        [(0.0,  '#0D1B2A'),   # near-black blue
         (0.01, '#1B3A5C'),   # dark blue
         (0.05, '#2166AC'),   # medium blue
         (0.15, '#4393C3'),   # blue
         (0.30, '#66C2A5'),   # teal
         (0.50, '#D9EF8B'),   # yellow-green
         (0.70, '#FEE08B'),   # yellow
         (0.85, '#FDAE61'),   # orange
         (0.95, '#F46D43'),   # red-orange
         (1.0,  '#D73027')],  # red
        N=256
    )

    im = ax.pcolormesh(sigmas, eps_values, S, cmap=cmap, shading='gouraud',
                       vmin=0, vmax=base_sensitivity, rasterized=True)

    # Color bar
    cb = fig.colorbar(im, cax=cax)
    cb.set_label(r'$d\theta / dA(\sigma)$', fontsize=12, labelpad=8)
    cb.ax.tick_params(labelsize=9)
    # Add the key value on the colorbar
    cb.ax.axhline(y=base_sensitivity, color='white', linewidth=0.8, linestyle='--')
    cb.ax.text(0.5, base_sensitivity, f' {base_sensitivity:.4f}',
               transform=cb.ax.get_yaxis_transform(),
               fontsize=8, color='white', va='center', ha='left')

    # Vertical dashed line at sigma*
    ax.axvline(x=0.70, color='white', linestyle='--', linewidth=1.0, alpha=0.7)

    # Mark the cusp
    ax.plot(0.70, 0.001, '*', color='white', markersize=12, zorder=5,
            markeredgecolor='black', markeredgewidth=0.5)

    # Annotate sigma*
    ax.annotate(r'$\sigma^* = 0.70$',
                xy=(0.70, 0.145), xytext=(0.76, 0.14),
                fontsize=10, color='white',
                arrowprops=dict(arrowstyle='->', color='white', lw=1.2),
                va='center')

    # Draw the effective-radius contours (where S > 0 boundary)
    # The boundary is where headroom = eps, i.e., A(sigma) = A_inf - eps
    # On the left limb: A = 3/(2-s), so s = 2 - 3/(A_inf - eps)
    # On the right limb: A = 15/(5s+3), so s = (15/(A_inf - eps) - 3)/5
    eps_contour = np.linspace(0.002, 0.148, 200)
    left_boundary = np.array([2.0 - 3.0 / (A_inf - e) for e in eps_contour])
    right_boundary = np.array([(15.0 / (A_inf - e) - 3.0) / 5.0 for e in eps_contour])

    # Clip to valid range
    mask_l = (left_boundary >= 0.50) & (left_boundary <= 0.70)
    mask_r = (right_boundary >= 0.70) & (right_boundary <= 1.00)

    ax.plot(left_boundary[mask_l], eps_contour[mask_l], '-', color='white',
            linewidth=1.5, alpha=0.8, zorder=4)
    ax.plot(right_boundary[mask_r], eps_contour[mask_r], '-', color='white',
            linewidth=1.5, alpha=0.8, zorder=4)

    # Annotate the slopes
    # Left slope annotation at eps ~ 0.07
    eps_annot = 0.07
    s_left = 2.0 - 3.0 / (A_inf - eps_annot)
    ax.annotate(r'slope $= +\frac{300}{169} \approx +1.775$',
                xy=(s_left, eps_annot),
                xytext=(0.54, 0.095),
                fontsize=9, color='white',
                arrowprops=dict(arrowstyle='->', color='white', lw=1.0),
                va='center', ha='center',
                bbox=dict(boxstyle='round,pad=0.3', fc='#333333', ec='white', alpha=0.7))

    # Right slope annotation
    s_right = (15.0 / (A_inf - eps_annot) - 3.0) / 5.0
    ax.annotate(r'slope $= -\frac{300}{169} \approx -1.775$',
                xy=(s_right, eps_annot),
                xytext=(0.86, 0.095),
                fontsize=9, color='white',
                arrowprops=dict(arrowstyle='->', color='white', lw=1.0),
                va='center', ha='center',
                bbox=dict(boxstyle='round,pad=0.3', fc='#333333', ec='white', alpha=0.7))

    # Mark the narrow band [0.695, 0.705] at small epsilon
    ax.annotate('',
                xy=(0.695, 0.012), xytext=(0.705, 0.012),
                arrowprops=dict(arrowstyle='<->', color='white', lw=1.5))
    ax.text(0.70, 0.016, r'$\Delta\sigma \approx 0.01$',
            fontsize=8, color='white', ha='center', va='bottom')

    # Labels
    ax.set_xlabel(r'$\sigma$', fontsize=13)
    ax.set_ylabel(r'Improvement magnitude $\varepsilon$', fontsize=12)
    ax.set_title(r'Sensitivity $\,d\theta_{\mathrm{PNTALL}}\!/\,dA(\sigma)$: '
                 r'where does effort pay off?', fontsize=13, pad=10)
    ax.set_xlim(0.50, 1.00)
    ax.set_ylim(0.001, 0.15)
    ax.set_xticks(np.arange(0.50, 1.01, 0.05))
    ax.tick_params(labelsize=10)

    # Add text box summarizing key facts
    textstr = (r'$\|\!A\!\|_\infty = \frac{30}{13}$' + '\n'
               r'$\theta = \frac{17}{30}$' + '\n'
               r'$\frac{d\theta}{d\|\!A\!\|_\infty} = \frac{169}{900}$')
    ax.text(0.92, 0.035, textstr, fontsize=9, color='white',
            ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.5', fc='#222222', ec='#888888', alpha=0.85))

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__), '..', '..', 'examples', 'expdb', 'analysis', 'figures', 'sensitivity_heatmap.png')
    fig.savefig(out_path, dpi=200, bbox_inches='tight', facecolor='#0D1B2A')
    print(f"Saved to {os.path.abspath(out_path)}")
    plt.close()


if __name__ == '__main__':
    main()
