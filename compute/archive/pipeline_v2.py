"""
EXPDB Pipeline v2: Direct theta computation from zero-density estimates.

The prime gap bound theta is related to zero-density estimates by the
Ingham-Huxley method. The key relation (simplified) is:

  theta = 1 - 1/(A_max)

where A_max = sup_{sigma in (1/2, 1)} A(sigma)/(1 - sigma) is the
zero-density exponent coefficient.

More precisely, the Ingham (1940) approach gives:
  Primes exist in [x, x + x^theta] for theta > 1 - 1/A_max
  where A_max is the sup of A(sigma)/(2(1-sigma)) over sigma in (1/2, 1).

The standard result:
  If N(sigma, T) <= T^{A * (1-sigma) + o(1)}, then
  primes in short intervals of length x^{theta} for
  theta = 1 - 1/A  (the Ingham exponent).

Let's verify:
  Huxley: A = 12/5 -> theta = 1 - 5/12 = 7/12 = 0.5833  [correct!]
  GM:     A = 30/13 -> theta = 1 - 13/30 = 17/30 = 0.5667  [correct!]

This is the correct formula.
"""

from fractions import Fraction
import numpy as np

print("=" * 72)
print("EXPDB PIPELINE v2: INGHAM EXPONENT COMPUTATION")
print("Binding Constraint Analysis After Guth-Maynard (2024)")
print("=" * 72)

# ============================================================
# The Ingham relation: theta = 1 - 1/A
# where A is the zero-density exponent coefficient
# ============================================================

# Known zero-density estimates: N(sigma, T) <= T^{A * (1-sigma) + o(1)}
estimates = {
    "Ingham (1940)":         Fraction(3, 1),
    "Montgomery (1971)":     Fraction(5, 2),
    "Huxley (1972)":         Fraction(12, 5),
    "Heath-Brown (1979)":    Fraction(9, 4),   # Near sigma=1 only
    "Guth-Maynard (2024)":   Fraction(30, 13),
}

print("\n--- ZERO-DENSITY ESTIMATES AND THEIR INGHAM EXPONENTS ---\n")
print(f"  {'Source':<25s}  {'A':>8s}  {'A (dec)':>8s}  {'theta = 1-1/A':>14s}  {'theta (dec)':>11s}")
print(f"  {'---':<25s}  {'---':>8s}  {'---':>8s}  {'---':>14s}  {'---':>11s}")

for name, A in sorted(estimates.items(), key=lambda x: x[1], reverse=True):
    theta = 1 - Fraction(1, 1) / A
    print(f"  {name:<25s}  {str(A):>8s}  {float(A):8.4f}  {str(theta):>14s}  {float(theta):11.6f}")

print(f"\n  The binding estimate is the one with the SMALLEST A")
print(f"  (which gives the smallest theta = best prime gap bound).\n")

# ============================================================
# Sensitivity analysis
# ============================================================

print("=" * 72)
print("SENSITIVITY ANALYSIS")
print("=" * 72)

A_gm = Fraction(30, 13)
theta_gm = 1 - Fraction(1, 1) / A_gm
A_hux = Fraction(12, 5)
theta_hux = 1 - Fraction(1, 1) / A_hux

print(f"""
  Pre-GM:   A = {A_hux} = {float(A_hux):.4f},  theta = {theta_hux} = {float(theta_hux):.6f}
  Post-GM:  A = {A_gm} = {float(A_gm):.4f},  theta = {theta_gm} = {float(theta_gm):.6f}
  Improvement: Delta(theta) = {float(theta_hux - theta_gm):.6f}
""")

# d(theta)/d(A) = 1/A^2
print("  The Ingham relation theta = 1 - 1/A gives:")
print(f"    d(theta)/d(A) = 1/A^2\n")
print(f"  At A = {A_gm} (GM):  d(theta)/d(A) = 1/{A_gm}^2 = {float(1/A_gm**2):.6f}")
print(f"  At A = {A_hux} (Hux): d(theta)/d(A) = 1/{A_hux}^2 = {float(1/A_hux**2):.6f}")
print()
print(f"  Interpretation:")
print(f"    Reducing A by 0.1 (from {float(A_gm):.4f} to {float(A_gm)-0.1:.4f})")
print(f"    would improve theta by approximately {0.1 * float(1/A_gm**2):.6f}")
print()

# ============================================================
# What determines A? The large value estimate landscape
# ============================================================

print("=" * 72)
print("THE LARGE VALUE ESTIMATE LANDSCAPE")
print("=" * 72)

print("""
  The zero-density exponent A comes from large value estimates (LVE).

  An LVE bounds how often a Dirichlet polynomial F(s) = sum a_n n^{-s}
  of length N can have |F(s)| >= N^sigma on a set of T^tau well-spaced
  points, with the set having "size" N^rho.

  In the EXPDB (sigma, tau, rho) coordinates, each LVE constrains the
  large value region R_LV subset R^3.

  The zero-density exponent A(sigma) is computed from R_LV by:
    A(sigma) = sup { rho/tau : (sigma, tau, rho) in R_LV, tau > 0 }

  The key LVEs and their bounds on A:

  | Source                | Bound on A                        | Range        |
  |-----------------------|-----------------------------------|--------------|
  | Mean value theorem    | A <= 2(1-sigma)/(sigma - 1/2)     | sigma > 1/2  |
  | Halasz (1968)         | A <= 3(1-sigma)                   | All sigma    |
  | Montgomery (1971)     | A <= 5(1-sigma)/2                 | All sigma    |
  | Huxley (1972)         | A <= 12(1-sigma)/5                | All sigma    |
  | Guth-Maynard (2024)   | A <= 30(1-sigma)/13               | All sigma    |

  The binding LVE is the one giving the smallest A coefficient.
  Post-GM: the binding coefficient is 30/13 = 2.3077 (from GM).
  All older estimates (Huxley 12/5 = 2.4, Montgomery 5/2 = 2.5,
  Halasz 3.0) are now SLACK.
""")

# ============================================================
# The energy side: A*(sigma) and its role
# ============================================================

print("=" * 72)
print("THE ENERGY SIDE: A*(sigma) AND THE BOTTLENECK QUESTION")
print("=" * 72)

print("""
  The full EXPDB pipeline computes theta from BOTH A(sigma) and A*(sigma):

    alpha(sigma) = 4*sigma - 2 + 2*(A*(1-sigma) - 1) / (A* - A)
    beta(sigma)  = 4*sigma - 2 + (A*(1-sigma) - 1) / A
    theta = sup_sigma max(alpha, beta)

  The simplified Ingham relation theta = 1 - 1/A assumes A* is not
  the binding constraint. This is valid when A*/A is large (the energy
  bound is much weaker than the ZD bound).

  But as A decreases (GM tightens it), A* becomes relatively more
  important. The question: has the bottleneck shifted from A to A*?

  To answer this precisely requires knowing A*(sigma), which comes from
  the energy projection of the 5D polytope P — not computable without
  the full EXPDB pipeline.

  However, we can identify the STRUCTURAL question:

  BEFORE GM:
    A was the bottleneck. Improving A (from Huxley to something better)
    would improve theta. A* was slack.

  AFTER GM:
    A has been improved. Two scenarios:

    (a) If A* >> A (energy bound much weaker):
        A is still the bottleneck. Further LVE improvements help.
        theta = 1 - 1/A, and d(theta)/d(A) = 1/A^2 ~ 0.188.

    (b) If A* is comparable to A (energy bound nearly as tight):
        A* becomes the bottleneck. The alpha formula dominates,
        and improving A further has diminishing returns.
        The next improvement requires tightening A*.

  THE KEY QUESTION FOR THE EXPDB COMPUTATION:
    What is A*(sigma*) / A(sigma*) at the optimal sigma*?
    If this ratio is >> 1: scenario (a), A still bottleneck.
    If this ratio is close to 1: scenario (b), A* is bottleneck.
""")

# ============================================================
# Binding constraint table
# ============================================================

print("=" * 72)
print("BINDING CONSTRAINT TABLE (Post-Guth-Maynard)")
print("=" * 72)

print(f"""
  | Rank | Constraint                     | Source              | Status    | Sensitivity      |
  |------|--------------------------------|---------------------|-----------|------------------|
  |  1   | A <= 30(1-sigma)/13            | Guth-Maynard (2024) | BINDING   | d(theta)/d(A)={float(1/A_gm**2):.4f} |
  |  2   | A*(sigma) from energy region   | Heath-Brown / Ivic  | UNKNOWN*  | Requires EXPDB   |
  |  3   | EP hull constraints            | Various             | UNKNOWN*  | Requires EXPDB   |
  |  4   | LVER coupling (s-coordinate)   | Heath-Brown (1979)  | UNKNOWN*  | Requires EXPDB   |
  |  5   | A <= 12(1-sigma)/5             | Huxley (1972)       | SLACK     | ---              |
  |  6   | A <= 5(1-sigma)/2              | Montgomery (1971)   | SLACK     | ---              |
  |  7   | A <= 3(1-sigma)                | Ingham (1940)       | SLACK     | ---              |

  * These constraints require the full EXPDB polytope computation to evaluate.
    The simplified Ingham relation theta = 1 - 1/A does not see them.

  DEFINITE CONCLUSIONS:
    - GM is the binding ZD estimate (all older estimates are slack).
    - theta = 17/30 = 0.56667 (confirmed by the Ingham relation).
    - d(theta)/d(A) = 1/A^2 = 13^2/30^2 = 169/900 ~ 0.1878
    - Further LVE improvement: reducing A by delta improves theta by delta/A^2.

  OPEN QUESTION (requires EXPDB computation):
    - Is A*(sigma*) binding in the full alpha/beta formulas?
    - What is the A*/A ratio at the optimal sigma*?
    - Has the bottleneck shifted from the LV side to the energy side?
""")

# ============================================================
# Projections toward RH
# ============================================================

print("=" * 72)
print("PROJECTIONS TOWARD theta = 1/2 (Riemann Hypothesis target)")
print("=" * 72)

print(f"""
  Riemann Hypothesis implies: theta = 1/2 + epsilon for all epsilon > 0.
  This corresponds to: A = 2 (the "density hypothesis").

  Current state (post-GM):
    A = 30/13 ~ 2.308
    theta = 17/30 ~ 0.567
    Gap to density hypothesis: A - 2 = {float(A_gm - 2):.4f}
    Gap to RH target: theta - 1/2 = {float(theta_gm) - 0.5:.4f}

  Improvements needed:
    To reach theta = 0.55:  need A <= {1/(1-0.55):.4f}  (currently {float(A_gm):.4f})
    To reach theta = 0.54:  need A <= {1/(1-0.54):.4f}
    To reach theta = 0.53:  need A <= {1/(1-0.53):.4f}
    To reach theta = 0.52:  need A <= {1/(1-0.52):.4f}
    To reach theta = 0.51:  need A <= {1/(1-0.51):.4f}
    To reach theta = 0.50:  need A <= {1/(1-0.50):.4f}  (density hypothesis)

  Each step requires a NEW large-value estimate or a completely new
  method for bounding zero-density regions.

  The Guth-Maynard improvement (12/5 -> 30/13, i.e. 2.400 -> 2.308)
  took 52 years (Huxley 1972 -> GM 2024). At this rate, reaching
  A = 2 would take... a long time. But the history of analytic number
  theory shows that breakthroughs come in bursts, not linearly.
""")

# ============================================================
# Summary
# ============================================================

print("=" * 72)
print("EXECUTIVE SUMMARY")
print("=" * 72)

print(f"""
  1. GUTH-MAYNARD RESULT:
     Replaces Huxley's A = 12/5 with A = 30/13 as the binding
     zero-density exponent. All older estimates become slack.
     theta improves from 7/12 to 17/30 (a gain of 1/60).

  2. BINDING CONSTRAINT:
     At the simplified (Ingham) level: GM is the sole binding constraint.
     At the full EXPDB level: the energy estimates (A*) and the LVER
     coupling constraints may also be binding. This requires computation.

  3. SENSITIVITY:
     d(theta)/d(A) = 1/A^2 = 169/900 ~ 0.188 at the GM value.
     Each 0.01 reduction in A improves theta by ~0.002.

  4. NEXT BOTTLENECK:
     UNKNOWN without the full EXPDB computation.
     If A*/A >> 1: still on the LV side (need better LVE).
     If A*/A ~ 1: shifted to energy side (need better energy estimates).

  5. ACTIONABLE NEXT STEP:
     Fork github.com/teorth/expdb, add the GM hypothesis,
     run the full pipeline, extract the binding constraints and
     dual variables at the optimal sigma*.

  6. PATH TO DENSITY HYPOTHESIS (A = 2, theta = 1/2):
     Current gap: A - 2 = 0.308. Need ~13% reduction in A.
     This is a major open problem in analytic number theory.
""")
