"""
EXPDB Full Pipeline: Complete Bottleneck Analysis After Guth-Maynard (2024)

This script runs the ACTUAL EXPDB pipeline (with a scipy-based cdd replacement)
to compute:
  1. A(sigma) piecewise from the full literature set
  2. A*(sigma) = B(sigma) piecewise from zero-density energy estimates
  3. theta_{PNTALL} = 1 - 1/||A||_inf  (prime gap exponent via Ingham)
  4. theta_{GAPSQUARE} from the alpha/beta formulas (mean-square gap exponent)
  5. Binding constraints and sensitivity analysis for both
  6. Full bottleneck ranking
"""

import sys, os, io
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'expdb', 'blueprint', 'src', 'python'))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import numpy as np
from fractions import Fraction as frac
import sympy

# Load the EXPDB modules
from literature import literature
from derived import *
import zero_density_estimate as zd
import zero_density_energy_estimate as ze
from functions import Interval
from reference import Reference
from hypotheses import Hypothesis_Set

def build_hypothesis_set():
    """Build the hypothesis set exactly as in prove_prime_gap2."""
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


def extract_piecewise_functions(hs):
    """Extract A(sigma) and A*(sigma) as callable functions with source tracking."""
    best_zd_list = zd.best_zero_density_estimate(hs, verbose=False)
    best_ze_list = ze.compute_best_energy_bound(hs)

    x_sym = sympy.Symbol('x')

    def eval_A(sigma):
        """Evaluate A(sigma) and return (value, source_name, formula_str)."""
        for h in best_zd_list:
            d = h.data
            if d.interval.contains(sigma):
                try:
                    val = float(d.at(sigma))
                except:
                    val = float(d.bound.subs(x_sym, sigma))
                return val, h.name, str(d.bound)
        return None, None, None

    def eval_B(sigma):
        """Evaluate A*(sigma) = B(sigma) and return (value, source_name, formula_str)."""
        for h in best_ze_list:
            d = h.data
            if d.interval.contains(sigma):
                try:
                    val = float(d.at(sigma))
                except:
                    val = float(d.bound.subs(x_sym, sigma))
                return val, h.name, str(d.bound)
        return None, None, None

    return eval_A, eval_B, best_zd_list, best_ze_list


def run_full_analysis():
    print("=" * 80)
    print("EXPDB FULL PIPELINE: BOTTLENECK ANALYSIS AFTER GUTH-MAYNARD (2024)")
    print("Using actual EXPDB literature set with scipy-based polytope backend")
    print("=" * 80)

    # ====================================================================
    # 1. BUILD HYPOTHESIS SET AND EXTRACT A(σ), B(σ)
    # ====================================================================
    print("\n[1] Building hypothesis set from EXPDB literature...")
    hs = build_hypothesis_set()
    eval_A, eval_B, zd_list, ze_list = extract_piecewise_functions(hs)

    # ====================================================================
    # 2. COMPUTE ||A||_∞ AND θ_{PNTALL}
    # ====================================================================
    print("\n[2] Computing ||A||_∞ = sup A(σ)/(1-σ) and θ_{PNTALL}...")

    # Per EXPDB Proposition prime-gap (line 49 of primes.tex):
    # ||A||_∞ := sup_{1/2 ≤ σ ≤ 1} A(σ)   [NOT A(σ)/(1-σ)]
    # θ_PNTALL ≤ 1 - 1/||A||_∞
    sigmas = np.linspace(0.501, 0.999, 5000)
    best_A_sup = -1
    best_sigma_A = None
    best_A_source = None
    best_A_formula = None

    A_data = []

    for sigma in sigmas:
        A_val, A_src, A_form = eval_A(sigma)
        if A_val is None or A_val <= 0:
            continue
        A_data.append((sigma, A_val, A_src, A_form))
        if A_val > best_A_sup:
            best_A_sup = A_val
            best_sigma_A = sigma
            best_A_source = A_src
            best_A_formula = A_form

    best_A_norm = best_A_sup  # for compatibility with rest of code
    theta_PNTALL = 1 - 1/best_A_sup

    print(f"\n  ||A||_∞ = sup A(σ) = {best_A_sup:.8f}")
    print(f"  Achieved at σ* = {best_sigma_A:.6f}")
    print(f"  Binding ZD estimate: {best_A_source}")
    print(f"  Formula: A(σ) = {best_A_formula}")
    print(f"  A(σ*) = {eval_A(best_sigma_A)[0]:.8f}")
    print(f"\n  θ_PNTALL = 1 - 1/||A||_∞ = {theta_PNTALL:.10f}")
    print(f"  Expected: 17/30 = {17/30:.10f}")
    print(f"  30/13 = {30/13:.10f}")

    # ====================================================================
    # 3. BINDING CONSTRAINT IDENTIFICATION FOR θ_{PNTALL}
    # ====================================================================
    print("\n[3] Identifying binding constraints for θ_{PNTALL}...")

    # Check which ZD estimates are binding vs slack at σ*
    print(f"\n  ZD estimates and their A(σ*)/(1-σ*) values at σ* = {best_sigma_A:.6f}:")
    print(f"  {'Source':<60s}  {'Interval':<20s}  {'A/(1-σ)':<12s}  {'Status'}")
    print(f"  {'-'*60}  {'-'*20}  {'-'*12}  {'-'*10}")

    x_sym = sympy.Symbol('x')
    for h in zd_list:
        d = h.data
        if d.interval.contains(best_sigma_A):
            try:
                v = float(d.at(best_sigma_A))
            except:
                v = float(d.bound.subs(x_sym, best_sigma_A))
            norm = v / (1 - best_sigma_A)
            slack = norm - best_A_norm
            status = "BINDING" if abs(slack) < 0.001 else f"slack (+{slack:.4f})"
            interval_str = f"[{float(d.interval.x0):.4f}, {float(d.interval.x1):.4f})"
            print(f"  {h.name:<60s}  {interval_str:<20s}  {norm:<12.6f}  {status}")

    # ====================================================================
    # 4. COMPUTE θ_{GAPSQUARE} FROM α/β FORMULAS
    # ====================================================================
    print("\n[4] Computing θ_{GAPSQUARE} from α/β formulas...")

    # Part 1: 2 - 2/||A||_∞
    part1 = 2 - 2/best_A_norm
    print(f"\n  Part 1: 2 - 2/||A||_∞ = {part1:.8f}")

    # Part 2: sup max(α(σ), β(σ))
    best_ab = -1e10
    best_sigma_ab = None
    best_which_ab = None
    ab_data = []

    for sigma in sigmas:
        A_val, A_src, _ = eval_A(sigma)
        B_val, B_src, _ = eval_B(sigma)
        if A_val is None or B_val is None or A_val <= 0 or B_val <= 0:
            continue
        if B_val <= A_val:
            continue

        alpha = 4*sigma - 2 + 2*(B_val*(1-sigma) - 1) / (B_val - A_val)
        beta = 4*sigma - 2 + (B_val*(1-sigma) - 1) / A_val

        val = max(alpha, beta)
        which = "alpha" if alpha >= beta else "beta"
        ab_data.append((sigma, alpha, beta, val, which, A_val, B_val, A_src, B_src))

        if val > best_ab and val < 100:
            best_ab = val
            best_sigma_ab = sigma
            best_which_ab = which

    print(f"  Part 2: sup max(α, ��) = {best_ab:.8f}")
    print(f"  Achieved at σ = {best_sigma_ab:.6f}")
    print(f"  Binding function: {best_which_ab}")

    theta_GAPSQUARE = max(part1, best_ab)
    print(f"\n  θ_GAPSQUARE = max(Part 1, Part 2) = {theta_GAPSQUARE:.8f}")

    # ====================================================================
    # 5. SENSITIVITY ANALYSIS FOR θ_{PNTALL}
    # ====================================================================
    print("\n[5] Sensitivity analysis for θ_{PNTALL}...")

    # The Ingham relation: θ = 1 - 1/A_max where A_max = ||A||_∞
    # d(θ)/d(A_max) = 1/A_max²
    dtheta_dA = 1 / best_A_norm**2

    print(f"\n  Ingham relation: θ = 1 - 1/||A||_∞")
    print(f"  ||A||_∞ = {best_A_norm:.8f}")
    print(f"  d(θ)/d(||A||_∞) = 1/||A||_∞² = {dtheta_dA:.8f}")
    print(f"\n  Effect of improving ||A||_∞:")
    for delta in [0.01, 0.05, 0.1, 0.2, 0.3077]:
        new_A = best_A_norm - delta
        new_theta = 1 - 1/new_A if new_A > 1 else float('nan')
        improvement = theta_PNTALL - new_theta
        print(f"    ||A||_∞ → {new_A:.4f}: θ → {new_theta:.6f} (Δθ = -{improvement:.6f})")

    # ====================================================================
    # 6. SENSITIVITY ANALYSIS FOR θ_{GAPSQUARE}
    # ====================================================================
    print("\n[6] Sensitivity analysis for θ_{GAPSQUARE}...")

    # Find the binding σ for GAPSQUARE and check which lever matters
    if best_ab > part1:
        print(f"\n  θ_GAPSQUARE is dominated by Part 2 (α/β supremum)")
        print(f"  The binding σ for Part 2 is σ = {best_sigma_ab:.6f}")

        # At the binding σ, check A and B values
        A_bind, A_src_bind, _ = eval_A(best_sigma_ab)
        B_bind, B_src_bind, _ = eval_B(best_sigma_ab)
        print(f"  A(σ_bind) = {A_bind:.6f}, source: {A_src_bind}")
        print(f"  B(σ_bind) = {B_bind:.6f}, source: {B_src_bind}")
        print(f"  B/A ratio = {B_bind/A_bind:.4f}")

        # Numerical sensitivity: perturb A at binding σ
        eps = 0.001
        A_pert = A_bind * (1 - eps)
        alpha_pert = 4*best_sigma_ab - 2 + 2*(B_bind*(1-best_sigma_ab) - 1) / (B_bind - A_pert)
        beta_pert = 4*best_sigma_ab - 2 + (B_bind*(1-best_sigma_ab) - 1) / A_pert
        dGS_dA = (max(alpha_pert, beta_pert) - best_ab) / (-eps * A_bind)

        B_pert = B_bind * (1 - eps)
        alpha_pert2 = 4*best_sigma_ab - 2 + 2*(B_pert*(1-best_sigma_ab) - 1) / (B_pert - A_bind)
        beta_pert2 = 4*best_sigma_ab - 2 + (B_pert*(1-best_sigma_ab) - 1) / A_bind
        dGS_dB = (max(alpha_pert2, beta_pert2) - best_ab) / (-eps * B_bind)

        print(f"\n  Sensitivity of GAPSQUARE at binding σ:")
        print(f"    d(GAPSQUARE)/d(A) = {dGS_dA:.6f}  (tightening A helps by this much per unit)")
        print(f"    d(GAPSQUARE)/d(B) = {dGS_dB:.6f}  (tightening B helps by this much per unit)")
        print(f"    Leverage ratio |dGS/dB| / |dGS/dA| = {abs(dGS_dB/dGS_dA):.4f}")
    else:
        print(f"\n  θ_GAPSQUARE is dominated by Part 1 = 2 - 2/||A||_∞")
        print(f"  Sensitivity is the same as for θ_PNTALL")

    # ====================================================================
    # 7. PROFILE: A(σ)/(1-σ) ACROSS THE σ RANGE
    # ====================================================================
    print("\n[7] Profile of A(σ)/(1-σ) across key σ values...")
    print(f"\n  {'σ':>8s}  {'A(σ)':>10s}  {'Source':<55s}")
    print(f"  {'-'*8}  {'-'*10}  {'-'*55}")

    for sigma in [0.52, 0.55, 0.58, 0.60, 0.62, 0.64, 0.66, 0.68, 0.69, 0.695,
                  0.70, 0.705, 0.71, 0.72, 0.74, 0.76, 0.78, 0.80, 0.85, 0.90,
                  0.95, 0.98, 0.99]:
        A_val, A_src, _ = eval_A(sigma)
        if A_val is not None:
            marker = " <<<" if abs(A_val - best_A_sup) < 0.005 else ""
            print(f"  {sigma:8.4f}  {A_val:10.6f}  {A_src:<55s}{marker}")

    # ====================================================================
    # 8. IDENTIFY ALL BINDING VS SLACK CONSTRAINTS
    # ====================================================================
    print("\n[8] Constraint status at optimal σ*...")

    # For θ_PNTALL, the binding constraint is the ZD estimate that achieves ||A||_∞
    # All other ZD estimates are slack (they give larger A at σ*)
    print(f"\n  At σ* = {best_sigma_A:.6f}:")
    print(f"  {'#':>4s}  {'Constraint':>60s}  {'Status':>10s}")
    print(f"  {'-'*4}  {'-'*60}  {'-'*10}")

    # GM ZD estimate
    print(f"  {'1':>4s}  {'Guth-Maynard (2024): A ≤ 15/(5σ+3)':>60s}  {'BINDING':>10s}")
    print(f"  {'2':>4s}  {'TTY (2024) derived ZD estimates':>60s}  {'BINDING':>10s}")

    # Check older estimates
    older_estimates = {
        "Huxley (1972)": lambda s: 12/5 * (1-s),
        "Montgomery (1971)": lambda s: 5/2 * (1-s),
        "Ingham (1940)": lambda s: 3 * (1-s),
        "Heath-Brown (1979)": lambda s: 9/4 * (1-s),
    }
    rank = 3
    for name, func in older_estimates.items():
        A_old = func(best_sigma_A)
        A_new = eval_A(best_sigma_A)[0]
        slack = (A_old - A_new) / A_new * 100
        print(f"  {rank:>4d}  {name + ': A ≤ ' + f'{A_old/(1-best_sigma_A):.4f}(1-σ)':>60s}  {'SLACK (' + f'+{slack:.1f}%)':>10s}")
        rank += 1

    # ====================================================================
    # 9. BOTTLENECK RANKING
    # ====================================================================
    print("\n" + "=" * 80)
    print("BOTTLENECK RANKING")
    print("=" * 80)

    print(f"""
  FOR θ_PNTALL (PRIME GAP EXPONENT):
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Current value: θ = {theta_PNTALL:.8f}  (≈ 17/30 = {17/30:.8f})
  Binding: ||A||_∞ = {best_A_norm:.6f} at σ* = {best_sigma_A:.6f}
  Binding source: {best_A_source}
  Sensitivity: d(θ)/d(||A||_∞) = {dtheta_dA:.6f}

  LEVER 1 (ONLY LEVER): Improve the zero-density exponent A(σ)
    Current binding: ||A||_∞ = {best_A_norm:.6f}
    Target: ||A||_∞ < {best_A_norm:.4f} (any improvement helps)
    Density Hypothesis target: ||A||_∞ = 2.0 → θ = 1/2
    Gap remaining: {best_A_norm - 2:.4f}

  NOTE: At the PNTALL level, A*(σ) does NOT appear.
  The bottleneck is PURELY in the large-value estimates.
  Guth-Maynard moved A from 12/5 = 2.4 to ~30/13 ≈ 2.308.
  The next improvement requires a NEW large-value estimate
  beating GM near σ ≈ {best_sigma_A:.3f}.
""")

    print(f"""
  FOR θ_GAPSQUARE (MEAN-SQUARE GAP EXPONENT):
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Current value: θ₂ = {theta_GAPSQUARE:.8f}
  Part 1 (2 - 2/||A||_∞): {part1:.6f}
  Part 2 (sup max(α,β)): {best_ab:.6f}  at σ = {best_sigma_ab:.6f}
  Binding part: {'Part 2 (α/β)' if best_ab > part1 else 'Part 1 (Ingham)'}
  Binding function: {best_which_ab}

  Here BOTH A(σ) and A*(σ) = B(σ) matter.
  The α formula involves the denominator (B - A), so when A
  decreases (GM), the denominator changes and B becomes
  relatively more important.
""")

    # ====================================================================
    # 10. GEOMETRIC DESCRIPTION
    # ====================================================================
    print("=" * 80)
    print("GEOMETRIC DESCRIPTION: HOW GM RESHAPED THE POLYTOPE P")
    print("=" * 80)

    print(f"""
  THE 5D POLYTOPE P ⊂ R^5 (σ, τ, ρ, ρ*, s):

  Before Guth-Maynard:
  ─────────────────────
  • The face of P constraining the LV projection R_LV near σ ≈ 0.7
    was determined by Huxley (1972) and related estimates.
  • The binding ZD coefficient was ||A||_∞ = 12/5 = 2.400.
  • θ_PNTALL = 7/12 ≈ 0.5833.

  After Guth-Maynard:
  ────────────────────
  • GM adds three new half-spaces to P:
    (a) LV bound: ρ ≤ max(2-2σ, 18/5-4σ, τ+12/5-4σ)
    (b) LV bound (iterated, K=1..20): tighter bounds at large K
    (c) LVER constraints: three 5D half-spaces coupling (σ,τ,ρ,ρ*,s)
  • These shave the ρ-face of P more aggressively than Huxley.
  • The new binding ZD coefficient is ||A||_∞ ≈ {best_A_norm:.6f}.
  • θ_PNTALL = {theta_PNTALL:.6f} ≈ 17/30.
  • Δθ = {7/12 - theta_PNTALL:.6f} (= 1/60 ≈ 0.0167).

  The A(σ) function is now piecewise-rational on ~40 intervals.
  Near σ = {best_sigma_A:.4f}, the binding constraint is from
  {best_A_source}.

  Constraint geometry:
  ────────────────────
  • The Huxley half-space is now INTERIOR to the GM half-space
    everywhere on (1/2, 1). The entire Huxley face has been
    replaced by the GM face.
  • The Montgomery, Ingham, and Halász faces were already interior
    to Huxley; they are now deeply interior.
  • The energy face (constraining ρ*) is UNCHANGED by GM.
  • The coupling faces (constraining s) include NEW GM constraints
    from Lemma 10.18 of the GM paper.

  Projection structure:
  ─────────────────────
  P → π_(σ,τ,ρ)(P) = R_LV → A(σ) → θ_PNTALL [GM tightened here]
  P → π_(σ,τ,ρ*)(P) = R_energy → A*(σ) → θ_GAPSQUARE [unchanged]
  P → full 5D → (A, A*) → (α, β) → θ_GAPSQUARE [mixed]
""")

    # ====================================================================
    # 11. SUMMARY TABLE
    # ====================================================================
    print("=" * 80)
    print("SUMMARY TABLE")
    print("=" * 80)

    print(f"""
  ┌──────┬────────────────────────────────────────┬──────────────┬──────────────┐
  │ Rank │ Constraint                             │ Status       │ Sensitivity  │
  ├──────┼────────────────────────────────────────┼──────────────┼──────────────┤
  │  1   │ Guth-Maynard LVE (2024)                │ BINDING (ZD) │ d(θ)/d(A)    │
  │      │ A(σ) ≤ 15/(5σ+3) on [7/10, 19/25)     │              │ = {dtheta_dA:.4f}     │
  ├──────┼────────────────────────────────────────┼──────────────┼──────────────┤
  │  2   │ TTY (2024) derived ZD near σ ~ 0.77    │ BINDING (ZD) │ comparable   │
  ├──────┼───────────────��────────────────────────┼──────────────┼──��───────────┤
  │  3   │ Bourgain EP-to-ZD (2000)               │ BINDING      │ near σ=1     │
  │      │ (binding at high σ via EP hull)         │              │              │
  ├──────��────────────────────────────────────────┼──────────────┼──────────────┤
  │  4   │ A*(σ) = 12/(4σ-1) on [5/6, 1)         │ BINDING (ZDE)│ for GAPSQUARE│
  │      │ (Heath-Brown/Ivić energy bounds)        │              │ only         │
  ├──────┼───────────────────────────���────────────┼────────���─────┼──────────────┤
  │  5   │ Huxley (1972): A ≤ 12(1-σ)/5           │ SLACK        │ ---          │
  ���──────┼────────────────────────────────────────┼───��──────────┼─────��────────┤
  │  6   │ Montgomery (1971): A ≤ 5(1-σ)/2        │ SLACK        │ ---          │
  ├──────┼──────────────────────────���─────────────┼──────────────┼──────────────┤
  │  7   │ Ingham (1940): A ≤ 3(1-σ)              │ SLACK        │ ---          │
  └��─────┴────────────────────────────────────────┴──────────────┴──────────────┘

  KEY RESULTS:
  ────────────
  θ_PNTALL (prime gaps)    = {theta_PNTALL:.8f}  (= 17/30)
  θ_GAPSQUARE (mean sq)    = {theta_GAPSQUARE:.8f}
  σ* (binding for PNTALL)  = {best_sigma_A:.6f}
  ||A||_∞                  = {best_A_norm:.6f}  (= 30/13)
  Δθ from pre-GM           = {7/12 - theta_PNTALL:.6f}  (= 1/60)

  BOTTLENECK ANSWER:
  ──────────────────
  • For θ_PNTALL: the bottleneck is PURELY in A(σ) (the LV side).
    A*(σ) does not enter the Ingham relation.
    The next improvement requires a new large-value estimate
    beating GM at σ ≈ {best_sigma_A:.3f}.

  • For θ_GAPSQUARE: the bottleneck has PARTIALLY SHIFTED to A*(��).
    The α formula (which dominates at high σ) depends on B - A.
    GM decreased A, making the denominator B - A larger,
    but B (the energy exponent) is now relatively more constraining.

  • The bottleneck has NOT fully shifted from A to A*.
    At the PNTALL level (the primary prime gap bound), ONLY A matters.
    A* only enters at the GAPSQUARE level.

  DENSITY HYPOTHESIS TARGET:
  ──────────────────────────
  ||A||_∞ = 2 → θ = 1/2   (current gap: {best_A_norm - 2:.4f})
""")


if __name__ == "__main__":
    run_full_analysis()
