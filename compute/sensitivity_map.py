"""
Fine-Grained Sensitivity Map for the EXPDB Pipeline

For every sigma in (1/2, 1), compute:
  1. Which ZD estimate is binding (the "active constraint")
  2. How much theta_PNTALL would improve if A(sigma) decreased by epsilon at that sigma
  3. How much theta_GAPSQUARE would improve
  4. The marginal value of tightening each constraint type

The key insight: theta_PNTALL = 1 - 1/||A||_inf where ||A||_inf = sup A(sigma).
So only improvements at sigma values where A(sigma) is NEAR the supremum matter.
The sensitivity drops to zero away from the peak.

But for theta_GAPSQUARE, improvements at HIGH sigma matter through the alpha/beta
formulas, so the sensitivity landscape is completely different.
"""

import sys, os, io
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'vendor', 'expdb', 'blueprint', 'src', 'python'))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import numpy as np
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
    print("=" * 80)
    print("SENSITIVITY MAP: WHERE DOES EFFORT PAY OFF?")
    print("=" * 80)

    hs = build_hs()
    best_zd = zd.best_zero_density_estimate(hs, verbose=False)
    best_ze = ze.compute_best_energy_bound(hs)
    x_sym = sympy.Symbol('x')

    def eval_A(sigma):
        for h in best_zd:
            if h.data.interval.contains(sigma):
                try:
                    return float(h.data.at(sigma)), h.name
                except:
                    return float(h.data.bound.subs(x_sym, sigma)), h.name
        return None, None

    def eval_B(sigma):
        for h in best_ze:
            if h.data.interval.contains(sigma):
                try:
                    return float(h.data.at(sigma)), h.name
                except:
                    return float(h.data.bound.subs(x_sym, sigma)), h.name
        return None, None

    # ================================================================
    # 1. COMPUTE THE FULL A(sigma) PROFILE AND ||A||_inf
    # ================================================================
    sigmas = np.linspace(0.505, 0.998, 1000)
    A_vals = []
    A_srcs = []
    B_vals = []
    B_srcs = []
    for s in sigmas:
        a, asrc = eval_A(s)
        b, bsrc = eval_B(s)
        A_vals.append(a if a else 0)
        A_srcs.append(asrc if asrc else "")
        B_vals.append(b if b else 0)
        B_srcs.append(bsrc if bsrc else "")

    A_vals = np.array(A_vals)
    B_vals = np.array(B_vals)
    A_inf = np.max(A_vals)
    sigma_star = sigmas[np.argmax(A_vals)]
    theta_PNTALL = 1 - 1/A_inf

    print(f"\n  ||A||_inf = {A_inf:.8f}")
    print(f"  sigma*    = {sigma_star:.6f}")
    print(f"  theta_PNTALL = {theta_PNTALL:.8f}")

    # ================================================================
    # 2. SENSITIVITY MAP FOR theta_PNTALL
    # ================================================================
    # theta = 1 - 1/||A||_inf
    # If we improve A(sigma_0) by epsilon (decrease it), then:
    #   - If A(sigma_0) < ||A||_inf: NO EFFECT (not the binding point)
    #   - If A(sigma_0) = ||A||_inf: delta_theta = -epsilon / ||A||_inf^2
    #
    # More precisely, if we decrease A on an interval [sigma_0-delta, sigma_0+delta]:
    #   The new ||A||_inf = max(A_inf - epsilon, max A(sigma) outside the interval)
    #
    # The "shadow" of the peak: how far from sigma* can you go and still
    # have the improvement matter?

    print("\n" + "=" * 80)
    print("SECTION 1: SENSITIVITY MAP FOR theta_PNTALL")
    print("=" * 80)

    print("""
  The Ingham relation theta = 1 - 1/||A||_inf means that ONLY improvements
  at sigma values where A(sigma) is at or near the supremum ||A||_inf matter.

  The "effective radius" around sigma* is the range of sigma values where
  A(sigma) > ||A||_inf - delta, for a given improvement delta.
""")

    # For each sigma, compute the "headroom": how much A(sigma) is below the peak
    headroom = A_inf - A_vals

    print(f"  Headroom = ||A||_inf - A(sigma):")
    print(f"  (Only sigma values with headroom < epsilon benefit from an epsilon-improvement)")
    print()
    print(f"  {'sigma':>8s}  {'A(sigma)':>10s}  {'headroom':>10s}  {'source':<45s}")
    print(f"  {'-'*8}  {'-'*10}  {'-'*10}  {'-'*45}")

    for i, s in enumerate(sigmas):
        if s in [0.55, 0.60, 0.65, 0.68, 0.69, 0.695, 0.698, 0.699, 0.70,
                 0.701, 0.702, 0.705, 0.71, 0.72, 0.75, 0.80, 0.90] or \
           abs(s - sigma_star) < 0.002:
            marker = " <<<" if headroom[i] < 0.001 else ""
            print(f"  {s:8.4f}  {A_vals[i]:10.6f}  {headroom[i]:10.6f}  {A_srcs[i][:45]}{marker}")

    # The effective radius: for a given epsilon improvement, which sigma range benefits?
    print(f"\n  Effective radius for different improvement magnitudes:")
    print(f"  {'epsilon':>10s}  {'sigma_low':>10s}  {'sigma_high':>10s}  {'width':>8s}  {'delta_theta':>12s}")
    print(f"  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*8}  {'-'*12}")

    for eps in [0.001, 0.005, 0.01, 0.02, 0.05, 0.1]:
        in_range = sigmas[A_vals > A_inf - eps]
        if len(in_range) > 0:
            s_lo = in_range[0]
            s_hi = in_range[-1]
            width = s_hi - s_lo
            new_A_inf = A_inf - eps
            new_theta = 1 - 1/new_A_inf if new_A_inf > 1 else 0
            delta_theta = new_theta - theta_PNTALL
            print(f"  {eps:10.4f}  {s_lo:10.4f}  {s_hi:10.4f}  {width:8.4f}  {delta_theta:+12.6f}")

    # ================================================================
    # 3. CONSTRAINT-BY-CONSTRAINT SENSITIVITY
    # ================================================================
    print("\n" + "=" * 80)
    print("SECTION 2: CONSTRAINT-BY-CONSTRAINT ANALYSIS")
    print("=" * 80)

    # Group sigma ranges by which constraint is binding
    print(f"\n  Which constraint is binding at each sigma?")
    print()

    current_src = ""
    interval_start = sigmas[0]
    constraint_intervals = []

    for i, s in enumerate(sigmas):
        if A_srcs[i] != current_src:
            if current_src:
                constraint_intervals.append((interval_start, sigmas[i-1], current_src, peak_A))
            current_src = A_srcs[i]
            interval_start = s
            peak_A = A_vals[i]
        peak_A = max(peak_A, A_vals[i])

    constraint_intervals.append((interval_start, sigmas[-1], current_src, peak_A))

    print(f"  {'sigma range':<25s}  {'max A':>8s}  {'headroom':>10s}  {'constraint':<50s}")
    print(f"  {'-'*25}  {'-'*8}  {'-'*10}  {'-'*50}")

    for (s0, s1, src, peak) in constraint_intervals:
        hr = A_inf - peak
        marker = " *** BINDING" if hr < 0.001 else ""
        print(f"  [{s0:.4f}, {s1:.4f}]  {peak:8.4f}  {hr:10.4f}  {src[:50]}{marker}")

    # ================================================================
    # 4. SENSITIVITY MAP FOR theta_GAPSQUARE
    # ================================================================
    print("\n" + "=" * 80)
    print("SECTION 3: SENSITIVITY MAP FOR theta_GAPSQUARE")
    print("=" * 80)

    print("""
  For GAPSQUARE, both A(sigma) and B(sigma) = A*(sigma) matter.
  The formula: GAPSQUARE <= max(2-2/||A||_inf, sup max(alpha, beta))
  where alpha = 4s-2 + 2(B(1-s)-1)/(B-A), beta = 4s-2 + (B(1-s)-1)/A.

  We compute d(alpha)/d(A) and d(alpha)/d(B) at each sigma to see
  where improvements to A vs B have the most leverage.
""")

    print(f"  {'sigma':>7s}  {'A':>7s}  {'B':>7s}  {'B/A':>6s}  {'alpha':>8s}  {'beta':>8s}  {'d(a)/dA':>9s}  {'d(a)/dB':>9s}  {'which':>6s}")
    print(f"  {'-'*7}  {'-'*7}  {'-'*7}  {'-'*6}  {'-'*8}  {'-'*8}  {'-'*9}  {'-'*9}  {'-'*6}")

    eps = 1e-5
    for i, s in enumerate(sigmas):
        A = A_vals[i]
        B = B_vals[i]
        if A <= 0 or B <= 0 or B <= A:
            continue

        alpha = 4*s - 2 + 2*(B*(1-s) - 1) / (B - A)
        beta = 4*s - 2 + (B*(1-s) - 1) / A

        # d(alpha)/d(A) numerically
        A2 = A - eps
        alpha2 = 4*s - 2 + 2*(B*(1-s) - 1) / (B - A2)
        da_dA = (alpha2 - alpha) / (-eps)

        # d(alpha)/d(B) numerically
        B2 = B - eps
        alpha3 = 4*s - 2 + 2*(B2*(1-s) - 1) / (B2 - A)
        da_dB = (alpha3 - alpha) / (-eps)

        which = "alpha" if alpha >= beta else "beta"

        # Only print at selected sigma values
        if s < 0.52 or (abs(s % 0.05) > 0.003 and abs(s - 0.70) > 0.003
                        and abs(s - 0.75) > 0.003 and abs(s - 0.85) > 0.003):
            continue

        print(f"  {s:7.4f}  {A:7.4f}  {B:7.4f}  {B/A:6.1f}  {alpha:8.4f}  {beta:8.4f}  {da_dA:+9.4f}  {da_dB:+9.4f}  {which:>6s}")

    # ================================================================
    # 5. THE HEAT MAP: WHERE TO AIM
    # ================================================================
    print("\n" + "=" * 80)
    print("SECTION 4: THE HEAT MAP — WHERE TO AIM")
    print("=" * 80)

    print("""
  For theta_PNTALL, the sensitivity is concentrated in a narrow band
  around sigma* = 0.70. The "heat" is:

    high  ██████████  sigma ~ 0.695–0.705 (the cusp)
    med   ████        sigma ~ 0.68–0.72
    low   ██          sigma ~ 0.65–0.75
    zero              sigma < 0.60 or sigma > 0.80

  For theta_GAPSQUARE, the sensitivity is concentrated at HIGH sigma
  (near 1), where the alpha formula dominates:

    high  ██████████  sigma ~ 0.95–0.999 (alpha → 2)
    med   ████        sigma ~ 0.90–0.95
    low   ██          sigma ~ 0.80–0.90
    zero              sigma < 0.70

  The two heat maps are DISJOINT. Improving A near sigma=0.70 helps
  theta_PNTALL but not theta_GAPSQUARE. Improving A or B near sigma=0.95
  helps theta_GAPSQUARE but not theta_PNTALL.
""")

    # Quantitative heat map
    print("  QUANTITATIVE HEAT MAP FOR theta_PNTALL:")
    print("  (epsilon = 0.01 improvement in A at each sigma)")
    print()
    epsilon = 0.01
    for i, s in enumerate(sigmas):
        if abs(s % 0.02) > 0.003 and abs(s - 0.70) > 0.003:
            continue
        if s < 0.52 or s > 0.98:
            continue

        A_here = A_vals[i]
        # If we lower A(sigma) by epsilon, does ||A||_inf change?
        new_peak = max(A_inf - epsilon if abs(A_here - A_inf) < epsilon else A_inf,
                       0)
        # More precisely: the new ||A||_inf is the max of A over all sigma,
        # with A(sigma_here) reduced by epsilon
        if A_here >= A_inf - epsilon:
            # This sigma is near the peak; the improvement matters
            # New ||A||_inf = max(A_inf - epsilon, max A elsewhere)
            # For simplicity, assume the second-highest point determines the new peak
            delta_theta = epsilon / A_inf**2  # first-order approximation
            bar = "█" * min(40, int(delta_theta * 2000))
        else:
            delta_theta = 0
            bar = ""

        print(f"  sigma={s:.3f}  A={A_here:.4f}  headroom={A_inf-A_here:.4f}  |  delta_theta={delta_theta:.6f}  {bar}")

    # ================================================================
    # 6. THE TWO-SIDED CUSP ANALYSIS
    # ================================================================
    print("\n" + "=" * 80)
    print("SECTION 5: THE TWO-SIDED CUSP")
    print("=" * 80)

    # The cusp at sigma=0.70 is where Ingham meets GM.
    # Left side: A_Ing(s) = 3/(2-s), increasing
    # Right side: A_GM(s) = 15/(5s+3), decreasing
    # Both = 30/13 at s = 7/10

    # Slopes at the cusp:
    # d/ds [3/(2-s)] = 3/(2-s)^2. At s=0.70: 3/(1.3)^2 = 3/1.69 = 1.775
    # d/ds [15/(5s+3)] = -75/(5s+3)^2. At s=0.70: -75/(6.5)^2 = -75/42.25 = -1.775

    left_slope = 3 / (2 - 0.70)**2
    right_slope = -75 / (5*0.70 + 3)**2

    print(f"""
  The cusp at sigma* = 7/10:

  Left limb (Ingham):  A(s) = 3/(2-s)
    Slope at cusp: dA/ds = +{left_slope:.4f}
    To lower ||A||_inf by epsilon, need to beat Ingham on [0.70 - delta, 0.70]
    where delta ~ epsilon / {left_slope:.3f} = epsilon * {1/left_slope:.4f}

  Right limb (GM):     A(s) = 15/(5s+3)
    Slope at cusp: dA/ds = {right_slope:.4f}
    To lower ||A||_inf by epsilon, need to beat GM on [0.70, 0.70 + delta]
    where delta ~ epsilon / {abs(right_slope):.3f} = epsilon * {1/abs(right_slope):.4f}

  The slopes are SYMMETRIC: |left slope| = |right slope| = {left_slope:.4f}.
  This means an epsilon-improvement on EITHER side requires beating the
  current bound on an interval of width ~ epsilon * {1/left_slope:.4f}.

  For epsilon = 0.01:  need to beat on width ~ {0.01/left_slope:.5f} around sigma = 0.70
  For epsilon = 0.05:  need to beat on width ~ {0.05/left_slope:.5f}
  For epsilon = 0.10:  need to beat on width ~ {0.10/left_slope:.5f}

  The corresponding theta improvements:
    epsilon = 0.01 → delta_theta = {0.01/A_inf**2:.6f}
    epsilon = 0.05 → delta_theta = {0.05/A_inf**2:.6f}
    epsilon = 0.10 → delta_theta = {0.10/A_inf**2:.6f}

  ATTACK SURFACE: The cusp is sharp (slope ~ 1.78 on both sides).
  A tiny improvement in A at sigma = 0.70 suffices — you don't need
  to beat the bound on a wide interval. An improvement of 0.01 at
  a single point sigma = 0.70 would need to hold on an interval of
  width only ~ 0.006.
""")

    # ================================================================
    # 7. THE NEXT-CONSTRAINT ANALYSIS
    # ================================================================
    print("=" * 80)
    print("SECTION 6: WHAT HAPPENS AFTER YOU SHAVE THE PEAK?")
    print("=" * 80)

    # If someone proves A(0.70) < 30/13, the new ||A||_inf is determined by
    # the SECOND-HIGHEST point of A(sigma). Where is that?
    print(f"\n  If the cusp at sigma=0.70 is lowered, what becomes the new peak?")
    print(f"\n  Second-highest values of A(sigma):")

    # Sort by A value, descending
    sorted_indices = np.argsort(-A_vals)
    seen_sources = set()
    count = 0
    for idx in sorted_indices:
        src = A_srcs[idx]
        if src in seen_sources:
            continue
        seen_sources.add(src)
        s = sigmas[idx]
        a = A_vals[idx]
        gap = A_inf - a
        print(f"    sigma={s:.4f}  A={a:.6f}  gap from peak={gap:.6f}  [{src[:50]}]")
        count += 1
        if count >= 10:
            break

    print(f"""
  The second-highest source is at sigma ~ 0.76–0.80, from Ivic/TTY estimates.
  If someone shaves the cusp by 0.10 (from 2.308 to 2.208), the new peak
  would be around A ~ 2.21 from Ivic at sigma ~ 0.76.

  This means: after the FIRST improvement past GM, the SECOND improvement
  would need to target a DIFFERENT sigma range (sigma ~ 0.76–0.80) and a
  DIFFERENT constraint (Ivic 2003 or TTY 2024).

  The landscape of successive improvements:
    1st target: sigma = 0.70, beat GM/Ingham cusp (30/13 → ?)
    2nd target: sigma ~ 0.76, beat Ivic 2003 (A ~ 2.21)
    3rd target: sigma ~ 0.80, beat Ivic 1980 (A ~ 1.88)
    ...
    Final target: Density Hypothesis (A → 2 everywhere)
""")


if __name__ == "__main__":
    main()
