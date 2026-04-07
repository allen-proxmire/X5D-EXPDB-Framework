"""
Succession plot: what happens as you shave the cusp.

Shows the current A(sigma) envelope and three hypothetical improvements,
each lowering the peak further. The new bottleneck migrates rightward
through Ivic (2003), Ivic (1980), TTY (2024), etc.
"""

import sys, os, io
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'vendor', 'expdb', 'blueprint', 'src', 'python'))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
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


# Canonical label for coloring
def canonical_label(raw):
    if raw is None:
        return ''
    r = raw.lower()
    if 'ingham' in r: return 'Ingham'
    if 'guth' in r: return 'GM'
    if 'ivic' in r or 'ivi' in r:
        if '2003' in raw or '2002' in raw: return 'Ivic03'
        if '1980' in raw or '1979' in raw: return 'Ivic80'
        return 'Ivic'
    if 'tao' in r or 'trudgian' in r: return 'TTY'
    if 'bourgain' in r: return 'Bourg'
    if 'pintz' in r: return 'Pintz'
    if 'heath' in r: return 'HB'
    if 'chen' in r: return 'CDV'
    if 'derived' in r: return 'Derived'
    return 'Other'


def main():
    print("Building hypothesis set...")
    hs = build_hs()
    best_zd = zd.best_zero_density_estimate(hs, verbose=False)
    x_sym = sympy.Symbol('x')

    def eval_A(sigma):
        for h in best_zd:
            if h.data.interval.contains(sigma):
                try:
                    return float(h.data.at(sigma)), h.name
                except:
                    return float(h.data.bound.subs(x_sym, sigma)), h.name
        return None, None

    # ---- Sample the envelope ----
    sigmas = np.linspace(0.501, 0.995, 2000)
    A_vals = np.zeros_like(sigmas)
    srcs = []
    for i, s in enumerate(sigmas):
        a, src = eval_A(s)
        A_vals[i] = a if a else 0
        srcs.append(canonical_label(src))

    A_inf = np.max(A_vals)
    sigma_star = sigmas[np.argmax(A_vals)]

    # ---- Build hypothetical shaved envelopes ----
    # For each epsilon, create a new envelope where A is capped at (A_inf - eps)
    # This simulates "someone proved a bound that beats everything near the cusp"
    epsilons = [0.0, 0.10, 0.22, 0.43]
    labels_eps = [
        f'Current ($\\|\\!A\\!\\|_\\infty = {A_inf:.3f}$)',
        f'After 1st shave ($\\varepsilon = 0.10$)',
        f'After 2nd shave ($\\varepsilon = 0.22$)',
        f'After 3rd shave ($\\varepsilon = 0.43$)',
    ]
    colors_eps = ['#333333', '#E41A1C', '#FF7F00', '#984EA3']
    lw_eps = [2.5, 2.0, 2.0, 2.0]
    ls_eps = ['-', '-', '--', ':']

    # For each epsilon, find the new peak and its location
    peaks = []
    for eps in epsilons:
        capped = np.minimum(A_vals, A_inf - eps)
        new_peak = np.max(capped)
        new_sigma = sigmas[np.argmax(capped)]
        new_src = srcs[np.argmax(capped)]
        peaks.append((new_peak, new_sigma, new_src))

    # ---- Plot ----
    fig, ax = plt.subplots(figsize=(10, 6))

    # Faint background: original envelope in light gray
    ax.fill_between(sigmas, 0, A_vals, color='#f0f0f0', zorder=0)

    # Plot each shaved envelope
    for j, eps in enumerate(epsilons):
        capped = np.minimum(A_vals, A_inf - eps)
        ax.plot(sigmas, capped, ls_eps[j], color=colors_eps[j],
                linewidth=lw_eps[j], label=labels_eps[j], zorder=3 - j*0.1)

    # Horizontal lines at each new peak
    peak_labels = [
        ('Ingham / GM cusp', '#333333'),
        ('Ivi\u0107 (2003)', '#1B7837'),
        ('Ivi\u0107 (1979) / TTY', '#F46D43'),
        ('Ivi\u0107 (1980)', '#41AB5D'),
    ]
    for j, (peak_val, peak_sig, peak_src) in enumerate(peaks):
        ax.axhline(y=peak_val, color=colors_eps[j], linewidth=0.6,
                   linestyle=':', alpha=0.5, zorder=1)

    # Mark each new peak with a dot and annotation
    # Offset annotations to avoid overlap
    offsets = [
        (0.03, 0.06),    # current peak
        (0.04, 0.04),    # 1st shave
        (0.05, 0.04),    # 2nd shave
        (0.05, 0.04),    # 3rd shave
    ]
    for j, (peak_val, peak_sig, peak_src) in enumerate(peaks):
        ax.plot(peak_sig, peak_val, 'o', color=colors_eps[j],
                markersize=7, markeredgecolor='black', markeredgewidth=0.8, zorder=5)

        label_text = f'{peak_labels[j][0]}\n$A = {peak_val:.3f}$, $\\sigma = {peak_sig:.3f}$'
        theta_val = 1 - 1/peak_val if peak_val > 1 else 0
        label_text += f'\n$\\theta = {theta_val:.4f}$'

        ox, oy = offsets[j]
        ax.annotate(label_text,
                    xy=(peak_sig, peak_val),
                    xytext=(peak_sig + ox, peak_val + oy),
                    fontsize=8, ha='left', va='bottom',
                    color=colors_eps[j],
                    arrowprops=dict(arrowstyle='->', color=colors_eps[j], lw=1.0),
                    bbox=dict(boxstyle='round,pad=0.3', fc='white',
                              ec=colors_eps[j], alpha=0.85))

    # Draw the "march to the right" arrow
    arrow_y = 1.72
    ax.annotate('', xy=(0.82, arrow_y), xytext=(0.68, arrow_y),
                arrowprops=dict(arrowstyle='->', color='#333333', lw=2.0,
                                connectionstyle='arc3,rad=0.15'))
    ax.text(0.75, arrow_y + 0.05, 'bottleneck migrates $\\longrightarrow$',
            fontsize=10, ha='center', va='bottom', color='#333333', fontstyle='italic')

    # Density Hypothesis reference line
    ax.axhline(y=2.0, color='#999999', linewidth=0.8, linestyle='--', alpha=0.4, zorder=1)
    ax.text(0.505, 2.02, 'Density Hypothesis ($A = 2$)',
            fontsize=8, color='#999999', va='bottom')

    # Vertical dashed line at original sigma*
    ax.axvline(x=0.70, color='#aaaaaa', linewidth=0.7, linestyle=':', alpha=0.5, zorder=1)

    # Formatting
    ax.set_xlabel(r'$\sigma$', fontsize=13)
    ax.set_ylabel(r'$A(\sigma)$', fontsize=13)
    ax.set_title('Succession of Bottlenecks: Shaving the Cusp', fontsize=14, pad=10)

    ax.set_xlim(0.50, 1.00)
    ax.set_ylim(0, 2.55)
    ax.set_xticks(np.arange(0.50, 1.01, 0.05))
    ax.set_yticks(np.arange(0, 2.6, 0.5))
    ax.tick_params(labelsize=10)
    ax.grid(True, alpha=0.15, linewidth=0.5)

    ax.legend(loc='upper right', fontsize=8.5, framealpha=0.9, edgecolor='#cccccc')

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__), '..', '..', 'examples', 'expdb', 'analysis', 'figures', 'succession_bottlenecks.png')
    fig.savefig(out_path, dpi=200, bbox_inches='tight', facecolor='white')
    print(f"Saved to {os.path.abspath(out_path)}")
    plt.close()


if __name__ == '__main__':
    main()
