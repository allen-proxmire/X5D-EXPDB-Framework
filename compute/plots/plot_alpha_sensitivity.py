"""
Plot dα/dA and dα/dB as functions of σ for the GAPSQUARE α formula.

α(σ) = 4σ - 2 + 2(B(1-σ) - 1) / (B - A)

The partial derivatives measure the leverage of improving A vs B
at each σ. The crossover determines which lever matters where.
"""

import sys, os, io
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'vendor', 'expdb', 'blueprint', 'src', 'python'))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
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
    best_ze = ze.compute_best_energy_bound(hs)
    x_sym = sympy.Symbol('x')

    def eval_A(sigma):
        for h in best_zd:
            if h.data.interval.contains(sigma):
                try:
                    return float(h.data.at(sigma))
                except:
                    return float(h.data.bound.subs(x_sym, sigma))
        return None

    def eval_B(sigma):
        for h in best_ze:
            if h.data.interval.contains(sigma):
                try:
                    return float(h.data.at(sigma))
                except:
                    return float(h.data.bound.subs(x_sym, sigma))
        return None

    # ---- Compute dα/dA and dα/dB numerically ----
    sigmas = np.linspace(0.505, 0.995, 1500)
    da_dA = np.full_like(sigmas, np.nan)
    da_dB = np.full_like(sigmas, np.nan)
    eps = 1e-6

    for i, s in enumerate(sigmas):
        A = eval_A(s)
        B = eval_B(s)
        if A is None or B is None or A <= 0 or B <= 0 or B <= A:
            continue

        alpha_0 = 4*s - 2 + 2*(B*(1-s) - 1) / (B - A)

        # dα/dA: perturb A downward (improvement direction)
        A2 = A - eps
        if B > A2:
            alpha_A = 4*s - 2 + 2*(B*(1-s) - 1) / (B - A2)
            da_dA[i] = (alpha_A - alpha_0) / (-eps)

        # dα/dB: perturb B downward
        B2 = B - eps
        if B2 > A:
            alpha_B = 4*s - 2 + 2*(B2*(1-s) - 1) / (B2 - A)
            da_dB[i] = (alpha_B - alpha_0) / (-eps)

    # ---- Find the crossover (where |dα/dA| = |dα/dB|) ----
    # Look for where the two absolute values cross
    valid = np.isfinite(da_dA) & np.isfinite(da_dB)
    diff = np.abs(da_dA) - np.abs(da_dB)
    crossover_sigma = None
    for i in range(1, len(sigmas)):
        if valid[i-1] and valid[i] and diff[i-1] * diff[i] < 0:
            # Linear interpolation
            t = diff[i-1] / (diff[i-1] - diff[i])
            crossover_sigma = sigmas[i-1] + t * (sigmas[i] - sigmas[i-1])
            break

    # Also find the zero crossing of dα/dA
    zero_crossing_sigma = None
    for i in range(1, len(sigmas)):
        if valid[i-1] and valid[i] and da_dA[i-1] * da_dA[i] < 0:
            t = da_dA[i-1] / (da_dA[i-1] - da_dA[i])
            zero_crossing_sigma = sigmas[i-1] + t * (sigmas[i] - sigmas[i-1])
            break

    print(f"  Crossover |dα/dA| = |dα/dB| at σ ≈ {crossover_sigma:.4f}")
    print(f"  Zero crossing dα/dA = 0 at σ ≈ {zero_crossing_sigma:.4f}")

    # ---- Plot ----
    fig, ax = plt.subplots(figsize=(10, 5.5))

    # Background shading for regimes
    ax.axvspan(0.50, 0.72, alpha=0.06, color='#2166AC', zorder=0)   # A-dominant
    ax.axvspan(0.72, 0.82, alpha=0.06, color='#4DAF4A', zorder=0)   # balanced
    ax.axvspan(0.82, 1.00, alpha=0.06, color='#E41A1C', zorder=0)   # B-dominant

    # The two sensitivity curves
    ax.plot(sigmas[valid], da_dA[valid], '-', color='#2166AC', linewidth=2.2,
            label=r'$\partial\alpha / \partial A$ (tightening $A$)', zorder=3)
    ax.plot(sigmas[valid], da_dB[valid], '-', color='#E41A1C', linewidth=2.2,
            label=r'$\partial\alpha / \partial B$ (tightening $A^*$)', zorder=3)

    # Zero line
    ax.axhline(y=0, color='#888888', linewidth=0.8, linestyle='-', zorder=1)

    # Crossover marker
    if crossover_sigma:
        # Evaluate dα/dA at crossover by interpolation
        idx = np.searchsorted(sigmas, crossover_sigma)
        val = 0.5 * (np.abs(da_dA[idx]) + np.abs(da_dB[idx])) if valid[idx] else 0
        # Use the actual value from one of the curves
        crossover_val = np.interp(crossover_sigma, sigmas[valid], da_dB[valid])
        ax.plot(crossover_sigma, crossover_val, 'o', color='#4DAF4A',
                markersize=9, markeredgecolor='black', markeredgewidth=1.2, zorder=5)
        ax.annotate(f'crossover\n$\\sigma \\approx {crossover_sigma:.3f}$',
                    xy=(crossover_sigma, crossover_val),
                    xytext=(crossover_sigma + 0.05, crossover_val + 0.04),
                    fontsize=9, ha='left', va='bottom',
                    arrowprops=dict(arrowstyle='->', color='#333333', lw=1.0),
                    bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#4DAF4A', alpha=0.9))

    # Zero crossing marker for dα/dA
    if zero_crossing_sigma:
        ax.plot(zero_crossing_sigma, 0, 's', color='#2166AC',
                markersize=7, markeredgecolor='black', markeredgewidth=1.0, zorder=5)
        ax.annotate(f'$\\partial\\alpha/\\partial A = 0$\n$\\sigma \\approx {zero_crossing_sigma:.3f}$',
                    xy=(zero_crossing_sigma, 0),
                    xytext=(zero_crossing_sigma + 0.04, -0.05),
                    fontsize=9, ha='left', va='top',
                    arrowprops=dict(arrowstyle='->', color='#2166AC', lw=1.0),
                    bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#2166AC', alpha=0.9))

    # Regime labels
    ax.text(0.60, 0.205, '$A$-dominant', fontsize=11, ha='center', va='center',
            color='#2166AC', fontstyle='italic', alpha=0.7)
    ax.text(0.77, 0.205, 'balanced', fontsize=11, ha='center', va='center',
            color='#4DAF4A', fontstyle='italic', alpha=0.7)
    ax.text(0.91, 0.205, '$B$-dominant', fontsize=11, ha='center', va='center',
            color='#E41A1C', fontstyle='italic', alpha=0.7)

    # Explanatory annotations
    ax.annotate('improving $A$ here\nworsens $\\alpha$',
                xy=(0.88, -0.07), xytext=(0.88, -0.13),
                fontsize=8, ha='center', va='top', color='#555555',
                arrowprops=dict(arrowstyle='->', color='#999999', lw=0.8))

    # Formatting
    ax.set_xlabel(r'$\sigma$', fontsize=13)
    ax.set_ylabel(r'Sensitivity (per unit decrease)', fontsize=12)
    ax.set_title(r'Sensitivity of $\alpha(\sigma)$ to $A(\sigma)$ and $B(\sigma) = A^*(\sigma)$',
                 fontsize=13, pad=10)

    ax.set_xlim(0.50, 1.00)
    ax.set_ylim(-0.20, 0.25)
    ax.set_xticks(np.arange(0.50, 1.01, 0.05))
    ax.set_yticks(np.arange(-0.20, 0.26, 0.05))
    ax.tick_params(labelsize=10)
    ax.grid(True, alpha=0.15, linewidth=0.5)

    ax.legend(loc='upper left', fontsize=10, framealpha=0.9, edgecolor='#cccccc')

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(__file__), '..', '..', 'examples', 'expdb', 'analysis', 'figures', 'alpha_sensitivity.png')
    fig.savefig(out_path, dpi=200, bbox_inches='tight', facecolor='white')
    print(f"Saved to {os.path.abspath(out_path)}")
    plt.close()


if __name__ == '__main__':
    main()
