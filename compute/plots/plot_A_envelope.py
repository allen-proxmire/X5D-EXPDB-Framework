"""
Plot the full zero-density envelope A(sigma) from the EXPDB pipeline.
Each binding interval is colored by its source constraint.
"""

import sys, os, io
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'vendor', 'expdb', 'blueprint', 'src', 'python'))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
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


# Canonical label mapping: raw EXPDB source name -> clean display label
def canonical_label(raw):
    raw_lower = raw.lower()
    if 'ingham' in raw_lower:
        return 'Ingham (1940)'
    if 'guth' in raw_lower and 'maynard' in raw_lower:
        return 'Guth\u2013Maynard (2024)'
    if 'ivic' in raw_lower or 'ivi' in raw_lower:
        # Distinguish by year if possible
        if '2003' in raw or '2002' in raw:
            return 'Ivi\u0107 (2003)'
        if '1980' in raw or '1979' in raw:
            return 'Ivi\u0107 (1980)'
        if '1984' in raw:
            return 'Ivi\u0107 (1984)'
        return 'Ivi\u0107'
    if 'tao' in raw_lower or 'trudgian' in raw_lower:
        return 'Tao\u2013Trudgian\u2013Yang (2024)'
    if 'bourgain' in raw_lower:
        return 'Bourgain (2000)'
    if 'pintz' in raw_lower:
        return 'Pintz (2023)'
    if 'heath' in raw_lower and 'brown' in raw_lower:
        return 'Heath-Brown (1979)'
    if 'chen' in raw_lower:
        return 'Chen\u2013Debruyne\u2013Vindas (2024)'
    if 'derived' in raw_lower:
        return 'Bourgain-derived'
    return raw[:30]


# Color palette for each canonical source
COLORS = {
    'Ingham (1940)':                   '#2166AC',  # deep blue
    'Guth\u2013Maynard (2024)':        '#B2182B',  # deep red
    'Ivi\u0107 (2003)':                '#1B7837',  # forest green
    'Ivi\u0107 (1980)':                '#41AB5D',  # medium green
    'Ivi\u0107 (1984)':                '#74C476',  # light green
    'Ivi\u0107':                       '#74C476',
    'Tao\u2013Trudgian\u2013Yang (2024)': '#F46D43', # orange
    'Bourgain (2000)':                 '#9970AB',  # purple
    'Bourgain-derived':                '#762A83',  # dark purple
    'Pintz (2023)':                    '#D6604D',  # salmon
    'Heath-Brown (1979)':              '#878787',  # gray
    'Chen\u2013Debruyne\u2013Vindas (2024)': '#FDB863', # gold
}
DEFAULT_COLOR = '#333333'


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

    # ---- Sample A(sigma) at high resolution ----
    sigmas = np.linspace(0.501, 0.998, 2000)
    A_vals = np.zeros_like(sigmas)
    labels = []
    for i, s in enumerate(sigmas):
        a, src = eval_A(s)
        A_vals[i] = a if a else np.nan
        labels.append(canonical_label(src) if src else '')

    # ---- Build per-source segments for colored plotting ----
    # Each segment: (sigma_array, A_array, canonical_label)
    segments = []
    seg_start = 0
    for i in range(1, len(sigmas)):
        if labels[i] != labels[seg_start]:
            segments.append((sigmas[seg_start:i+1].copy(),
                             A_vals[seg_start:i+1].copy(),
                             labels[seg_start]))
            seg_start = i
    segments.append((sigmas[seg_start:].copy(), A_vals[seg_start:].copy(), labels[seg_start]))

    # ---- Also compute the "ghost" curves for Ingham and GM across full range ----
    sigma_full = np.linspace(0.501, 0.998, 500)
    A_ingham = 3.0 / (2.0 - sigma_full)
    A_gm = 15.0 / (5.0 * sigma_full + 3.0)

    # ---- Plot ----
    fig, ax = plt.subplots(figsize=(10, 5.5))

    # Ghost curves (dashed, faint)
    ax.plot(sigma_full, A_ingham, '--', color='#2166AC', alpha=0.25, linewidth=1.0, zorder=1)
    ax.plot(sigma_full, A_gm, '--', color='#B2182B', alpha=0.25, linewidth=1.0, zorder=1)

    # Colored segments (binding envelope)
    plotted_labels = set()
    for (ss, aa, lab) in segments:
        color = COLORS.get(lab, DEFAULT_COLOR)
        lw = 2.5 if lab in ('Ingham (1940)', 'Guth\u2013Maynard (2024)') else 2.0
        ax.plot(ss, aa, '-', color=color, linewidth=lw, zorder=3,
                label=lab if lab not in plotted_labels else None)
        plotted_labels.add(lab)

    # Vertical dashed line at sigma = 0.70
    ax.axvline(x=0.70, color='#444444', linestyle=':', linewidth=1.0, alpha=0.6, zorder=2)

    # Mark the cusp
    cusp_A = 30.0 / 13.0
    ax.plot(0.70, cusp_A, 'o', color='black', markersize=6, zorder=5)
    ax.annotate(r'$\frac{30}{13}$',
                xy=(0.70, cusp_A),
                xytext=(0.715, cusp_A + 0.06),
                fontsize=12,
                ha='left', va='bottom',
                arrowprops=dict(arrowstyle='->', color='black', lw=1.0),
                zorder=5)

    # Annotate sigma*
    ax.annotate(r'$\sigma^* = \frac{7}{10}$',
                xy=(0.70, 0),
                xytext=(0.70, -0.08),
                fontsize=10,
                ha='center', va='top',
                color='#444444',
                annotation_clip=False)

    # Horizontal reference: Density Hypothesis A = 2
    ax.axhline(y=2.0, color='#999999', linestyle='--', linewidth=0.8, alpha=0.5, zorder=1)
    ax.text(0.505, 2.02, 'Density Hypothesis ($A = 2$)', fontsize=8, color='#999999', va='bottom')

    # Labels and formatting
    ax.set_xlabel(r'$\sigma$', fontsize=13)
    ax.set_ylabel(r'$A(\sigma)$', fontsize=13)
    ax.set_title(r'Zero-Density Envelope $A(\sigma)$ After Guth–Maynard (2024)', fontsize=14, pad=12)

    ax.set_xlim(0.50, 1.00)
    ax.set_ylim(0, 2.55)
    ax.set_xticks(np.arange(0.50, 1.01, 0.05))
    ax.set_yticks(np.arange(0, 2.6, 0.5))
    ax.tick_params(labelsize=10)
    ax.grid(True, alpha=0.2, linewidth=0.5)

    # Legend — deduplicate and order
    legend_order = [
        'Ingham (1940)',
        'Guth\u2013Maynard (2024)',
        'Ivi\u0107 (2003)',
        'Ivi\u0107 (1980)',
        'Tao\u2013Trudgian\u2013Yang (2024)',
        'Bourgain-derived',
        'Bourgain (2000)',
        'Heath-Brown (1979)',
        'Chen\u2013Debruyne\u2013Vindas (2024)',
        'Pintz (2023)',
    ]
    handles = []
    for lab in legend_order:
        if lab in plotted_labels:
            color = COLORS.get(lab, DEFAULT_COLOR)
            lw = 2.5 if 'Ingham' in lab or 'Guth' in lab else 2.0
            handles.append(Line2D([0], [0], color=color, linewidth=lw, label=lab))

    ax.legend(handles=handles, loc='upper right', fontsize=8, framealpha=0.9,
              edgecolor='#cccccc')

    plt.tight_layout()

    out_path = os.path.join(os.path.dirname(__file__), '..', '..', 'examples', 'expdb', 'analysis', 'figures', 'A_sigma_envelope.png')
    fig.savefig(out_path, dpi=200, bbox_inches='tight', facecolor='white')
    print(f"Saved to {os.path.abspath(out_path)}")
    plt.close()


if __name__ == '__main__':
    main()
