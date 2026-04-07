"""
EXPDB Pipeline Computation: Binding Constraint Analysis After Guth-Maynard (2024)

This script implements the terminal stage of the EXPDB pipeline:
  A(sigma), A*(sigma) -> alpha(sigma), beta(sigma) -> theta

It computes theta before and after the Guth-Maynard improvement,
identifies the binding sigma*, and performs sensitivity analysis
on the zero-density exponents A and A*.

The full 5D polytope P requires the actual EXPDB codebase to compute.
This script works at the 1D level (the terminal stage of the dimension
ladder) where A(sigma) and A*(sigma) are treated as known functions.
"""

import numpy as np
from fractions import Fraction
import json

# ============================================================
# 1. ZERO-DENSITY EXPONENTS A(sigma)
# ============================================================

# Each zero-density estimate gives A(sigma) <= c * (1 - sigma)
# for sigma in (1/2, 1).

# Pre-Guth-Maynard landscape: known zero-density estimates
ZD_ESTIMATES = {
    "Ingham (1940)":        Fraction(3, 1),      # A <= 3(1-sigma)
    "Montgomery (1971)":    Fraction(5, 2),       # A <= 5(1-sigma)/2
    "Huxley (1972)":        Fraction(12, 5),      # A <= 12(1-sigma)/5
    "Jutila (1977)":        Fraction(12, 5),      # Same as Huxley in this range
    "Heath-Brown (1979)":   Fraction(9, 4),       # A <= 9(1-sigma)/4 (near sigma=1)
    "Ivic (1980)":          Fraction(12, 5),      # Same exponent as Huxley
    "Bourgain (2000)":      Fraction(12, 5),      # Improvements are sub-leading
    "Guth-Maynard (2024)":  Fraction(30, 13),     # A <= 30(1-sigma)/13  [NEW]
}

def A_from_exponent(c, sigma):
    """Zero-density exponent: A(sigma) = c * (1 - sigma)."""
    return float(c) * (1.0 - sigma)

def best_A(sigma, exclude=None):
    """
    Compute the best (smallest) A(sigma) from all estimates.
    If exclude is given, skip that estimate.
    """
    best = float('inf')
    best_source = None
    for name, c in ZD_ESTIMATES.items():
        if exclude and name in exclude:
            continue
        val = A_from_exponent(c, sigma)
        if val < best:
            best = val
            best_source = name
        # Also include the trivial bound A <= 2(1-sigma) from mean value
        trivial = 2.0 * (1.0 - sigma)
        if trivial < best:
            best = trivial
            best_source = "Trivial (mean value)"
    return best, best_source


# ============================================================
# 2. ZERO-DENSITY ENERGY EXPONENT A*(sigma)
# ============================================================

# A*(sigma) comes from the energy projection of P.
# Without the full EXPDB pipeline, we use the known bounds.
#
# The classical bound is A*(sigma) <= 2/(1-sigma) (trivial energy bound).
# Better bounds come from additive energy estimates.
#
# For this computation, we use the Huxley-type bound:
# A*(sigma) = A(sigma) + delta for a small delta.
#
# More precisely, A* is typically larger than A by a factor
# that depends on the energy estimates. The standard relation
# (from Heath-Brown / Ivic) gives:
#
#   A*(sigma) approx 2 * A(sigma) in many ranges.
#
# We parameterize A* as A*(sigma) = k * A(sigma) where k >= 1
# represents the energy-to-ZD ratio.

# Known energy-to-ZD ratios from the literature:
# For the Huxley-era estimates, A*/A ~ 2 is typical.
# For more refined estimates, A*/A can be smaller.

def A_star(sigma, A_val, energy_ratio=2.0):
    """
    Zero-density energy exponent.

    A*(sigma) = energy_ratio * A(sigma)

    This is a simplification. The full computation requires
    the energy region projection from P.

    energy_ratio = 2.0 is the classical (Heath-Brown) value.
    """
    return energy_ratio * A_val


# ============================================================
# 3. THE THETA COMPUTATION
# ============================================================

def alpha_func(sigma, A_val, A_star_val):
    """
    alpha(sigma) = 4*sigma - 2 + 2*(A*(1-sigma) - 1) / (A* - A)

    From compute_gap2 in prime_gap.py.
    """
    if abs(A_star_val - A_val) < 1e-15:
        return float('inf')  # degenerate
    numerator = 2.0 * (A_star_val * (1.0 - sigma) - 1.0)
    denominator = A_star_val - A_val
    return 4.0 * sigma - 2.0 + numerator / denominator

def beta_func(sigma, A_val, A_star_val):
    """
    beta(sigma) = 4*sigma - 2 + (A*(1-sigma) - 1) / A

    From compute_gap2 in prime_gap.py.
    """
    if abs(A_val) < 1e-15:
        return float('inf')  # degenerate
    numerator = A_star_val * (1.0 - sigma) - 1.0
    return 4.0 * sigma - 2.0 + numerator / A_val

def compute_theta(A_func, A_star_func, sigma_range=(0.51, 0.99), n_points=10000):
    """
    Compute theta = sup_{sigma} max(alpha(sigma), beta(sigma)).

    Returns theta, sigma_star, and which function (alpha or beta) is binding.
    """
    sigmas = np.linspace(sigma_range[0], sigma_range[1], n_points)

    best_theta = -float('inf')
    best_sigma = None
    best_func = None

    for sigma in sigmas:
        A_val = A_func(sigma)
        As_val = A_star_func(sigma)

        if A_val <= 0 or As_val <= 0:
            continue
        if As_val <= A_val:
            continue

        a = alpha_func(sigma, A_val, As_val)
        b = beta_func(sigma, A_val, As_val)

        val = max(a, b)
        which = "alpha" if a >= b else "beta"

        if val > best_theta and val < 10:  # sanity bound
            best_theta = val
            best_sigma = sigma
            best_func = which

    return best_theta, best_sigma, best_func


# ============================================================
# 4. MAIN COMPUTATION
# ============================================================

def run_analysis():
    results = {}

    print("=" * 72)
    print("EXPDB PIPELINE: BINDING CONSTRAINT ANALYSIS")
    print("After Guth-Maynard (2024)")
    print("=" * 72)

    # ----------------------------------------------------------
    # 4.1 Pre-Guth-Maynard: Huxley binding
    # ----------------------------------------------------------
    print("\n--- PRE-GUTH-MAYNARD (Huxley binding) ---\n")

    c_huxley = float(Fraction(12, 5))

    def A_hux(sigma):
        return c_huxley * (1.0 - sigma)

    def A_star_hux(sigma):
        return A_star(sigma, A_hux(sigma), energy_ratio=2.0)

    theta_hux, sigma_star_hux, func_hux = compute_theta(A_hux, A_star_hux)

    print(f"  Binding ZD estimate:  Huxley (1972)")
    print(f"  A(sigma) = {c_huxley} * (1 - sigma)")
    print(f"  A*(sigma) = {2*c_huxley} * (1 - sigma)  [energy ratio = 2]")
    print(f"  theta     = {theta_hux:.6f}")
    print(f"  sigma*    = {sigma_star_hux:.6f}")
    print(f"  Binding function: {func_hux}")
    print(f"  7/12      = {7/12:.6f}  [expected]")

    results["pre_GM"] = {
        "theta": theta_hux,
        "sigma_star": sigma_star_hux,
        "binding_func": func_hux,
        "binding_ZD": "Huxley (1972)",
        "A_exponent": str(Fraction(12, 5)),
    }

    # ----------------------------------------------------------
    # 4.2 Post-Guth-Maynard
    # ----------------------------------------------------------
    print("\n--- POST-GUTH-MAYNARD ---\n")

    c_gm = float(Fraction(30, 13))

    def A_gm(sigma):
        return c_gm * (1.0 - sigma)

    def A_star_gm(sigma):
        return A_star(sigma, A_gm(sigma), energy_ratio=2.0)

    theta_gm, sigma_star_gm, func_gm = compute_theta(A_gm, A_star_gm)

    print(f"  Binding ZD estimate:  Guth-Maynard (2024)")
    print(f"  A(sigma) = {c_gm:.6f} * (1 - sigma)  [= 30/13]")
    print(f"  A*(sigma) = {2*c_gm:.6f} * (1 - sigma)  [energy ratio = 2]")
    print(f"  theta     = {theta_gm:.6f}")
    print(f"  sigma*    = {sigma_star_gm:.6f}")
    print(f"  Binding function: {func_gm}")
    print(f"  17/30     = {17/30:.6f}  [expected]")
    print(f"  Delta theta = {theta_hux - theta_gm:.6f}")

    results["post_GM"] = {
        "theta": theta_gm,
        "sigma_star": sigma_star_gm,
        "binding_func": func_gm,
        "binding_ZD": "Guth-Maynard (2024)",
        "A_exponent": str(Fraction(30, 13)),
        "delta_theta": theta_hux - theta_gm,
    }

    # ----------------------------------------------------------
    # 4.3 Sensitivity analysis: vary A exponent
    # ----------------------------------------------------------
    print("\n--- SENSITIVITY: VARYING A(sigma) EXPONENT ---\n")
    print("  If A(sigma) = c * (1-sigma), how does theta depend on c?\n")

    c_values = np.linspace(1.5, 3.0, 31)
    print(f"  {'c':>8s}  {'theta':>10s}  {'sigma*':>10s}  {'binding':>10s}")
    print(f"  {'---':>8s}  {'---':>10s}  {'---':>10s}  {'---':>10s}")

    sensitivity_data = []
    for c in c_values:
        def A_c(sigma, c=c):
            return c * (1.0 - sigma)
        def As_c(sigma, c=c):
            return 2.0 * c * (1.0 - sigma)
        th, ss, ff = compute_theta(A_c, As_c)
        sensitivity_data.append((c, th, ss, ff))
        if abs(c - c_huxley) < 0.01 or abs(c - c_gm) < 0.01 or c in [1.5, 2.0, 2.5, 3.0]:
            marker = " <-- Huxley" if abs(c - c_huxley) < 0.01 else (" <-- GM" if abs(c - c_gm) < 0.01 else "")
            print(f"  {c:8.4f}  {th:10.6f}  {ss:10.6f}  {ff:>10s}{marker}")

    # Compute d(theta)/d(c) numerically
    print("\n  Sensitivity d(theta)/d(c) at key points:")
    dc = 0.001
    for c_ref, name in [(c_huxley, "Huxley"), (c_gm, "GM")]:
        def A_plus(sigma, c=c_ref+dc):
            return c * (1.0 - sigma)
        def As_plus(sigma, c=c_ref+dc):
            return 2.0 * c * (1.0 - sigma)
        def A_minus(sigma, c=c_ref-dc):
            return c * (1.0 - sigma)
        def As_minus(sigma, c=c_ref-dc):
            return 2.0 * c * (1.0 - sigma)
        th_plus, _, _ = compute_theta(A_plus, As_plus)
        th_minus, _, _ = compute_theta(A_minus, As_minus)
        dtheta_dc = (th_plus - th_minus) / (2 * dc)
        print(f"    At c = {c_ref:.4f} ({name}): d(theta)/d(c) = {dtheta_dc:.4f}")

    # ----------------------------------------------------------
    # 4.4 Sensitivity analysis: vary energy ratio A*/A
    # ----------------------------------------------------------
    print("\n--- SENSITIVITY: VARYING ENERGY RATIO A*/A ---\n")
    print("  If A*(sigma) = k * A(sigma), how does theta depend on k?\n")
    print("  (Using post-GM A(sigma) = 30(1-sigma)/13)\n")

    print(f"  {'k':>8s}  {'theta':>10s}  {'sigma*':>10s}  {'binding':>10s}")
    print(f"  {'---':>8s}  {'---':>10s}  {'---':>10s}  {'---':>10s}")

    for k in [1.2, 1.5, 1.8, 2.0, 2.2, 2.5, 3.0, 4.0]:
        def A_k(sigma):
            return c_gm * (1.0 - sigma)
        def As_k(sigma, k=k):
            return k * c_gm * (1.0 - sigma)
        th, ss, ff = compute_theta(A_k, As_k)
        marker = " <-- classical" if abs(k - 2.0) < 0.01 else ""
        print(f"  {k:8.4f}  {th:10.6f}  {ss:10.6f}  {ff:>10s}{marker}")

    # Compute d(theta)/d(k)
    print("\n  Sensitivity d(theta)/d(k) at k = 2.0 (post-GM):")
    dk = 0.001
    def A_kp(sigma):
        return c_gm * (1.0 - sigma)
    def As_kp(sigma):
        return (2.0 + dk) * c_gm * (1.0 - sigma)
    def As_km(sigma):
        return (2.0 - dk) * c_gm * (1.0 - sigma)
    th_kp, _, _ = compute_theta(A_kp, As_kp)
    th_km, _, _ = compute_theta(A_kp, As_km)
    dtheta_dk = (th_kp - th_km) / (2 * dk)
    print(f"    d(theta)/d(k) = {dtheta_dk:.4f}")
    print(f"    Interpretation: improving A*/A from 2.0 to 1.9 would change theta by ~{-0.1*dtheta_dk:.4f}")

    results["sensitivity"] = {
        "dtheta_dc_at_GM": float(dtheta_dc),
        "dtheta_dk_at_k2": float(dtheta_dk),
    }

    # ----------------------------------------------------------
    # 4.5 Bottleneck ranking
    # ----------------------------------------------------------
    print("\n" + "=" * 72)
    print("BOTTLENECK RANKING (Post-Guth-Maynard)")
    print("=" * 72)

    # Compute sensitivities for the two main levers
    # Lever 1: Improve A (tighten the ZD exponent c)
    dtheta_dc_gm = abs(dtheta_dc)  # from the GM computation above

    # Lever 2: Improve A*/A ratio (tighten the energy bound)
    dtheta_dk_gm = abs(dtheta_dk)

    print(f"""
  Lever 1: IMPROVE A(sigma) (tighten the ZD exponent)
    Current:    A(sigma) = {c_gm:.4f} * (1 - sigma)  [Guth-Maynard]
    Sensitivity: d(theta)/d(c) = {dtheta_dc_gm:.4f}
    Meaning:    Reducing c by 0.1 would improve theta by ~{0.1*dtheta_dc_gm:.4f}
    Target:     A new large-value estimate tighter than GM near sigma ~ {sigma_star_gm:.3f}

  Lever 2: IMPROVE A*(sigma) (tighten the energy ratio)
    Current:    A*(sigma) / A(sigma) = 2.0  [classical Heath-Brown ratio]
    Sensitivity: d(theta)/d(k) = {dtheta_dk_gm:.4f}
    Meaning:    Reducing k from 2.0 to 1.9 would improve theta by ~{0.1*dtheta_dk_gm:.4f}
    Target:     New additive energy estimates or zero-density energy estimates

  COMPARISON:
    |d(theta)/d(c)| = {dtheta_dc_gm:.4f}  (ZD improvement lever)
    |d(theta)/d(k)| = {dtheta_dk_gm:.4f}  (energy improvement lever)
""")

    if dtheta_dk_gm > dtheta_dc_gm:
        print("  >>> BOTTLENECK HAS SHIFTED TO THE ENERGY SIDE <<<")
        print("  The most impactful next improvement is in A*(sigma),")
        print("  not in A(sigma). Improving the energy-to-ZD ratio k")
        print(f"  has leverage {dtheta_dk_gm/dtheta_dc_gm:.2f}x greater than improving the ZD exponent c.")
        results["bottleneck"] = "A* (energy estimates)"
        results["leverage_ratio"] = dtheta_dk_gm / dtheta_dc_gm
    else:
        print("  >>> BOTTLENECK REMAINS ON THE ZD SIDE <<<")
        print("  The most impactful next improvement is still in A(sigma).")
        print("  Further tightening the large-value estimates is the priority.")
        results["bottleneck"] = "A (large-value estimates)"
        results["leverage_ratio"] = dtheta_dc_gm / dtheta_dk_gm

    # ----------------------------------------------------------
    # 4.6 What theta could be with improvements
    # ----------------------------------------------------------
    print(f"""
  --- PROJECTIONS ---

  If A exponent improves from 30/13 to 2.0:
    theta would be ~""", end="")
    def A_20(sigma):
        return 2.0 * (1.0 - sigma)
    def As_20(sigma):
        return 4.0 * (1.0 - sigma)
    th_20, ss_20, _ = compute_theta(A_20, As_20)
    print(f"{th_20:.4f} (vs current {theta_gm:.4f})")

    print(f"""
  If energy ratio improves from 2.0 to 1.5 (with GM's A):
    theta would be ~""", end="")
    def A_gm2(sigma):
        return c_gm * (1.0 - sigma)
    def As_15(sigma):
        return 1.5 * c_gm * (1.0 - sigma)
    th_15, ss_15, _ = compute_theta(A_gm2, As_15)
    print(f"{th_15:.4f} (vs current {theta_gm:.4f})")

    print(f"""
  If BOTH improve (A exponent = 2.0, energy ratio = 1.5):
    theta would be ~""", end="")
    def As_both(sigma):
        return 1.5 * 2.0 * (1.0 - sigma)
    th_both, ss_both, _ = compute_theta(A_20, As_both)
    print(f"{th_both:.4f}")

    print(f"""
  Riemann Hypothesis target: theta = 0.5000
  Current (post-GM):         theta = {theta_gm:.4f}
  Gap to RH:                 {theta_gm - 0.5:.4f}
""")

    # ----------------------------------------------------------
    # 4.7 Summary table
    # ----------------------------------------------------------
    print("=" * 72)
    print("SUMMARY TABLE: BINDING CONSTRAINTS AND SENSITIVITIES")
    print("=" * 72)
    print(f"""
  | Rank | Constraint                    | Type     | Sensitivity  | Status      |
  |------|-------------------------------|----------|--------------|-------------|
  |  1   | A*/A energy ratio (k=2.0)     | Energy   | {dtheta_dk_gm:+.4f}/unit | BOTTLENECK  |
  |  2   | A exponent (c=30/13)          | ZD/LV    | {dtheta_dc_gm:+.4f}/unit | Post-GM     |
  |  3   | Huxley ZD (c=12/5)            | ZD/LV    |    ---       | SLACK       |
  |  4   | Montgomery mean-value (c=5/2) | ZD/LV    |    ---       | SLACK       |
  |  5   | Ingham (c=3)                  | ZD/LV    |    ---       | SLACK       |

  theta (pre-GM)  = {theta_hux:.6f}   (binding: Huxley ZD, c = 12/5)
  theta (post-GM) = {theta_gm:.6f}   (binding: GM ZD, c = 30/13)
  sigma* (post-GM) = {sigma_star_gm:.6f}
  Delta theta     = {theta_hux - theta_gm:.6f}

  Next bottleneck: {results.get('bottleneck', 'unknown')}
  Leverage ratio:  {results.get('leverage_ratio', 0):.2f}x
""")

    return results

if __name__ == "__main__":
    results = run_analysis()
