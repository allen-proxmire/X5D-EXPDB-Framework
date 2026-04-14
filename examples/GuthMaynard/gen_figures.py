"""Generate the four figures for GuthMaynard_BindingConstraints_v2.md.

Outputs PNGs only into ./figures/.
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.colors import LinearSegmentedColormap

OUTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(OUTDIR, exist_ok=True)

DPI = 160

# ---------------------------------------------------------------------
# Closed-form A(sigma) curves used throughout
# ---------------------------------------------------------------------
def A_ingham(s):    return 3.0 / (2.0 - s)              # rising limb on [1/2, 7/10]
def A_gm(s):        return 15.0 / (5.0*s + 3.0)         # GM on [7/10, 19/25]
def A_huxley(s):    return 12.0*(1.0 - s) / 5.0          # now-superseded

# Energy estimate B(sigma) = A^*(sigma) (Heath-Brown 1979 on [5/6, 1))
def B_hb(s):        return 12.0 / (4.0*s - 1.0)

SIGMA_STAR = 7.0/10.0
A_PEAK = 30.0/13.0

# Falling-limb anchors (sigma, A) drawn straight from the binding tables in
# §4 and §9 of the paper.  Curves between Ivić/TTY/.../Pintz are approximated
# by linear interpolation between adjacent anchors -- close enough at this
# resolution and faithful to the values quoted in the manuscript.
FALLING_ANCHORS = [
    (0.76, 30.0/13.0 - 0.10),   # Ivić (2003) start ~ 2.21
    (0.78, 2.10),
    (0.86, 1.88),
    (0.92, 1.50),
    (0.96, 1.09),
    (0.98, 0.85),
    (0.999, 0.55),
]

def A_falling(s):
    xs = np.array([a[0] for a in FALLING_ANCHORS])
    ys = np.array([a[1] for a in FALLING_ANCHORS])
    return np.interp(s, xs, ys)

# Piecewise envelope (sigma intervals + the active formula on each piece)
PIECES = [
    (0.50, 0.70, A_ingham,    "Ingham (1940)",         "#1f77b4"),
    (0.70, 0.76, A_gm,        "Guth--Maynard (2024)",  "#d62728"),
    (0.76, 0.78, A_falling,   r"Ivić (2003)",          "#2ca02c"),
    (0.78, 0.86, A_falling,   "TTY (2025)",            "#9467bd"),
    (0.86, 0.92, A_falling,   r"Ivić (1980)",          "#8c564b"),
    (0.92, 0.96, A_falling,   "Bourgain EP",           "#e377c2"),
    (0.96, 0.999, A_falling,  "Pintz (2023)",          "#7f7f7f"),
]

def envelope(sigma_array):
    """Pointwise envelope (lower hull) over the active pieces."""
    out = np.full_like(sigma_array, np.inf)
    for lo, hi, f, _, _ in PIECES:
        mask = (sigma_array >= lo) & (sigma_array <= hi + 1e-9)
        out[mask] = np.minimum(out[mask], f(sigma_array[mask]))
    return out

# =====================================================================
# Figure 1.  A(sigma) envelope
# =====================================================================
def fig_envelope():
    fig, ax = plt.subplots(figsize=(8.0, 5.2), dpi=DPI)

    # extended dashed Ingham + GM
    s_ext = np.linspace(0.5, 0.999, 800)
    ax.plot(s_ext, A_ingham(s_ext), color="#1f77b4", linewidth=1.0,
            linestyle=(0, (4, 3)), alpha=0.55, label="Ingham (extended)")
    s_gmx = np.linspace(0.55, 0.95, 600)
    ax.plot(s_gmx, A_gm(s_gmx), color="#d62728", linewidth=1.0,
            linestyle=(0, (4, 3)), alpha=0.55, label="GM (extended)")

    # Solid binding pieces
    for lo, hi, f, label, color in PIECES:
        s = np.linspace(lo, hi, 200)
        ax.plot(s, f(s), color=color, linewidth=2.6, label=label, solid_capstyle="round")

    # Cusp marker
    ax.plot([SIGMA_STAR], [A_PEAK], "o", markersize=8,
            markerfacecolor="black", markeredgecolor="white", zorder=10)
    ax.annotate(r"cusp $\sigma^{*}=7/10$" + "\n" + r"$\|A\|_{\infty}=30/13\approx 2.308$",
                xy=(SIGMA_STAR, A_PEAK),
                xytext=(0.78, 2.55),
                fontsize=9.5,
                arrowprops=dict(arrowstyle="->", color="black", lw=0.9))

    # Density Hypothesis line
    ax.axhline(2.0, color="grey", linestyle=":", linewidth=0.9)
    ax.text(0.51, 2.04, "Density Hypothesis $A=2$", fontsize=8.5, color="grey")

    ax.set_xlabel(r"$\sigma$", fontsize=12)
    ax.set_ylabel(r"$A(\sigma)$", fontsize=12)
    ax.set_xlim(0.5, 1.0)
    ax.set_ylim(0.0, 3.1)
    ax.set_title(r"Zero-density envelope $A(\sigma)$ after Guth--Maynard",
                 fontsize=12, pad=10)
    ax.grid(True, linestyle=":", alpha=0.4)
    leg = ax.legend(loc="upper right", fontsize=8, ncol=2, framealpha=0.92)
    leg.get_frame().set_edgecolor("#cccccc")

    plt.tight_layout()
    out = os.path.join(OUTDIR, "A_sigma_envelope.png")
    plt.savefig(out, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", out)

# =====================================================================
# Figure 2.  Sensitivity heat map for theta_PNTALL
# =====================================================================
def fig_sensitivity_heatmap():
    fig, ax = plt.subplots(figsize=(8.0, 5.0), dpi=DPI)

    sigmas = np.linspace(0.55, 0.85, 400)
    eps    = np.linspace(0.0, 0.18, 300)
    S, E = np.meshgrid(sigmas, eps)

    A_env = envelope(sigmas)[None, :]
    headroom = A_PEAK - A_env  # >= 0
    # sensitivity nonzero only where epsilon > headroom
    active = np.maximum(E - headroom, 0.0)  # 0 outside the cone, magnitude inside
    # weight by 1/||A||^2 (the dtheta/dA at the cusp)
    sens = active * (13.0**2 / 30.0**2)

    pcm = ax.pcolormesh(sigmas, eps, sens, cmap="magma_r",
                        vmin=0, vmax=sens.max() * 0.95, shading="auto")
    cb = fig.colorbar(pcm, ax=ax, pad=0.015)
    cb.set_label(r"effective $|d\theta_{\mathrm{PNTALL}}/dA|$", fontsize=10)

    # White V boundary lines (slope ±300/169)
    slope = 300.0 / 169.0
    eps_line = np.linspace(0.0, 0.18, 200)
    ax.plot(SIGMA_STAR + eps_line / slope, eps_line,
            color="white", linewidth=1.6, linestyle="-")
    ax.plot(SIGMA_STAR - eps_line / slope, eps_line,
            color="white", linewidth=1.6, linestyle="-")

    ax.axvline(SIGMA_STAR, color="white", linewidth=0.7, linestyle=":")
    ax.text(SIGMA_STAR + 0.005, 0.005, r"$\sigma^{*}=7/10$",
            color="white", fontsize=9)

    ax.set_xlabel(r"$\sigma$", fontsize=12)
    ax.set_ylabel(r"improvement $\varepsilon$ in $A(\sigma)$", fontsize=11)
    ax.set_title(r"Sensitivity cone for $\theta_{\mathrm{PNTALL}}$ at the cusp",
                 fontsize=12, pad=10)
    ax.set_xlim(0.55, 0.85)
    ax.set_ylim(0.0, 0.18)

    plt.tight_layout()
    out = os.path.join(OUTDIR, "sensitivity_heatmap.png")
    plt.savefig(out, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", out)

# =====================================================================
# Figure 3.  Partial derivatives d alpha / dA  and  d alpha / dB
# =====================================================================
def fig_alpha_sensitivity():
    """alpha = 4*sigma - 2 + 2*(B*(1-sigma) - 1)/(B - A)."""
    fig, ax = plt.subplots(figsize=(8.0, 5.0), dpi=DPI)

    sigmas = np.linspace(0.55, 0.99, 500)
    A = envelope(sigmas)
    # Build B from a few literature pieces; the numbers in the paper's table use
    # the post-GM B that is dominated by Heath-Brown on [5/6, 1) and by an
    # extension at lower sigma.  For visualization we use HB everywhere with
    # a soft cap matching the table values (B \in [4.3, 6.1]).
    B = np.maximum(B_hb(sigmas), 4.0 + 2.0 * (1.0 - sigmas))

    # partial derivatives of alpha
    denom = (B - A)
    dalpha_dA = 2.0 * (B * (1.0 - sigmas) - 1.0) / denom**2
    dalpha_dB = 2.0 * ((1.0 - sigmas) * (B - A) - (B * (1.0 - sigmas) - 1.0)) / denom**2

    ax.axhline(0.0, color="black", linewidth=0.6)
    ax.plot(sigmas, dalpha_dA, color="#1f77b4", linewidth=2.4,
            label=r"$\partial\alpha/\partial A$")
    ax.plot(sigmas, dalpha_dB, color="#d62728", linewidth=2.4,
            label=r"$\partial\alpha/\partial B$")

    # Crossover & sign change
    cross_idx = np.where(np.diff(np.sign(dalpha_dB - dalpha_dA)))[0]
    if len(cross_idx):
        sx = sigmas[cross_idx[0]]
        ax.axvline(sx, color="grey", linestyle="--", linewidth=0.8)
        ax.text(sx + 0.005, 0.20, f"crossover\n$\\sigma\\approx{sx:.3f}$",
                fontsize=8.5, color="grey")
    sign_idx = np.where(np.diff(np.sign(dalpha_dA)))[0]
    if len(sign_idx):
        sz = sigmas[sign_idx[0]]
        ax.plot([sz], [0.0], "o", markersize=6,
                markerfacecolor="#1f77b4", markeredgecolor="white", zorder=10)
        ax.annotate(rf"$\partial\alpha/\partial A=0$ at $\sigma\approx{sz:.3f}$",
                    xy=(sz, 0.0), xytext=(sz + 0.02, -0.06),
                    fontsize=8.5, color="#1f77b4",
                    arrowprops=dict(arrowstyle="->", color="#1f77b4", lw=0.7))

    ax.set_xlabel(r"$\sigma$", fontsize=12)
    ax.set_ylabel(r"partial derivative", fontsize=11)
    ax.set_xlim(0.55, 0.99)
    ax.set_title(r"Sensitivity of $\alpha(\sigma)$ to $A$ and $B$",
                 fontsize=12, pad=10)
    ax.grid(True, linestyle=":", alpha=0.45)
    leg = ax.legend(loc="upper right", fontsize=10, framealpha=0.92)
    leg.get_frame().set_edgecolor("#cccccc")

    plt.tight_layout()
    out = os.path.join(OUTDIR, "alpha_sensitivity.png")
    plt.savefig(out, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", out)

# =====================================================================
# Figure 4.  Succession of bottlenecks
# =====================================================================
def fig_succession():
    fig, ax = plt.subplots(figsize=(8.0, 5.2), dpi=DPI)
    sigmas = np.linspace(0.50, 0.999, 1200)
    A0 = envelope(sigmas)

    ax.plot(sigmas, A0, color="black", linewidth=2.4, label="Current envelope")

    cuts = [(0.10, "#d62728", r"$\varepsilon=0.10$:  next peak Ivić (2003) $\sim 0.76$"),
            (0.22, "#ff7f0e", r"$\varepsilon=0.22$:  next peak Ivić/TTY  $\sim 0.77$"),
            (0.43, "#9467bd", r"$\varepsilon=0.43$:  next peak Ivić (1980) $\sim 0.80$")]
    for eps, color, label in cuts:
        cap = A_PEAK - eps
        cut_curve = np.minimum(A0, cap)
        ax.plot(sigmas, cut_curve, color=color, linewidth=1.7,
                linestyle=(0, (5, 2)), label=label)

    # Density Hypothesis floor
    ax.axhline(2.0, color="grey", linestyle=":", linewidth=0.9)
    ax.text(0.505, 2.04, "Density Hypothesis $A=2$", fontsize=8.5, color="grey")

    # Mark current peak
    ax.plot([SIGMA_STAR], [A_PEAK], "o", markersize=7,
            markerfacecolor="black", markeredgecolor="white", zorder=10)
    ax.annotate(r"current peak $30/13$",
                xy=(SIGMA_STAR, A_PEAK),
                xytext=(0.80, 2.6), fontsize=9,
                arrowprops=dict(arrowstyle="->", color="black", lw=0.8))

    ax.set_xlabel(r"$\sigma$", fontsize=12)
    ax.set_ylabel(r"$A(\sigma)$", fontsize=12)
    ax.set_xlim(0.5, 1.0)
    ax.set_ylim(0.5, 3.0)
    ax.set_title(r"Succession of bottlenecks under hypothetical improvements",
                 fontsize=12, pad=10)
    ax.grid(True, linestyle=":", alpha=0.4)
    leg = ax.legend(loc="lower left", fontsize=8.5, framealpha=0.92)
    leg.get_frame().set_edgecolor("#cccccc")

    plt.tight_layout()
    out = os.path.join(OUTDIR, "succession_bottlenecks.png")
    plt.savefig(out, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", out)

if __name__ == "__main__":
    fig_envelope()
    fig_sensitivity_heatmap()
    fig_alpha_sensitivity()
    fig_succession()
    print("done")
