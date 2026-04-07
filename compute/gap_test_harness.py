"""
Gap Test Harness: Systematically check whether EXPDB has fully exploited Guth-Maynard.

Runs the EXPDB pipeline under different configurations and compares the
resulting A(sigma), A*(sigma), and theta values.
"""

import sys, os, io, json, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'vendor', 'expdb', 'blueprint', 'src', 'python'))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import numpy as np
from fractions import Fraction as frac
import sympy

# Probe points for comparing A(sigma) across runs
PROBE_SIGMAS = [0.52, 0.55, 0.60, 0.65, 0.68, 0.695, 0.70, 0.705, 0.71,
                0.72, 0.74, 0.76, 0.78, 0.80, 0.85, 0.90, 0.95, 0.98, 0.99]


def extract_profile(hs, label=""):
    """
    Given a hypothesis set, compute A(sigma) and A*(sigma) at probe points.
    Returns a dict with all results.
    """
    import zero_density_estimate as zd
    import zero_density_energy_estimate as ze

    x_sym = sympy.Symbol('x')

    best_zd = zd.best_zero_density_estimate(hs, verbose=False)
    best_ze = ze.compute_best_energy_bound(hs)

    def eval_at(bound_list, sigma):
        for h in bound_list:
            d = h.data
            if d.interval.contains(sigma):
                try:
                    return float(d.at(sigma)), h.name
                except:
                    return float(d.bound.subs(x_sym, sigma)), h.name
        return None, None

    # Compute profiles
    A_profile = {}
    B_profile = {}
    for sigma in PROBE_SIGMAS:
        A_val, A_src = eval_at(best_zd, sigma)
        B_val, B_src = eval_at(best_ze, sigma)
        A_profile[str(sigma)] = {"value": A_val, "source": A_src}
        B_profile[str(sigma)] = {"value": B_val, "source": B_src}

    # Compute ||A||_inf
    sigmas_fine = np.linspace(0.501, 0.999, 5000)
    best_A = -1
    best_sigma = None
    best_src = None
    for sigma in sigmas_fine:
        A_val, A_src = eval_at(best_zd, sigma)
        if A_val is not None and A_val > best_A:
            best_A = A_val
            best_sigma = sigma
            best_src = A_src

    theta_PNTALL = 1 - 1/best_A if best_A > 1 else None

    return {
        "label": label,
        "A_profile": A_profile,
        "B_profile": B_profile,
        "A_inf": best_A,
        "sigma_star": best_sigma,
        "A_inf_source": best_src,
        "theta_PNTALL": theta_PNTALL,
        "num_zd": len(best_zd),
        "num_ze": len(best_ze),
    }


def compare_profiles(baseline, test, label=""):
    """Print a comparison of two profiles."""
    print(f"\n{'='*72}")
    print(f"COMPARISON: {label}")
    print(f"{'='*72}")

    print(f"\n  ||A||_inf:  baseline = {baseline['A_inf']:.8f},  test = {test['A_inf']:.8f}")
    delta_A = test['A_inf'] - baseline['A_inf']
    print(f"  Delta ||A||_inf = {delta_A:+.10f}")

    if baseline['theta_PNTALL'] and test['theta_PNTALL']:
        delta_theta = test['theta_PNTALL'] - baseline['theta_PNTALL']
        print(f"  theta_PNTALL:  baseline = {baseline['theta_PNTALL']:.8f},  test = {test['theta_PNTALL']:.8f}")
        print(f"  Delta theta = {delta_theta:+.10f}")

    if abs(delta_A) < 1e-8:
        print(f"\n  RESULT: NO CHANGE to ||A||_inf")
    elif delta_A < 0:
        print(f"\n  *** IMPROVEMENT FOUND: ||A||_inf decreased by {abs(delta_A):.10f} ***")
    else:
        print(f"\n  RESULT: ||A||_inf INCREASED (unexpected)")

    # Check A(sigma) at each probe point
    print(f"\n  {'sigma':>8s}  {'A_base':>10s}  {'A_test':>10s}  {'Delta':>12s}  {'Note'}")
    print(f"  {'-'*8}  {'-'*10}  {'-'*10}  {'-'*12}  {'-'*20}")
    any_change = False
    for sigma_str in [str(s) for s in PROBE_SIGMAS]:
        A_base = baseline['A_profile'].get(sigma_str, {}).get('value')
        A_test = test['A_profile'].get(sigma_str, {}).get('value')
        if A_base is not None and A_test is not None:
            delta = A_test - A_base
            note = ""
            if abs(delta) > 1e-8:
                note = "CHANGED" if delta < 0 else "worse"
                any_change = True
            print(f"  {sigma_str:>8s}  {A_base:10.6f}  {A_test:10.6f}  {delta:+12.8f}  {note}")

    # Check A*(sigma) at probe points
    print(f"\n  {'sigma':>8s}  {'B_base':>10s}  {'B_test':>10s}  {'Delta':>12s}  {'Note'}")
    print(f"  {'-'*8}  {'-'*10}  {'-'*10}  {'-'*12}  {'-'*20}")
    any_B_change = False
    for sigma_str in [str(s) for s in PROBE_SIGMAS]:
        B_base = baseline['B_profile'].get(sigma_str, {}).get('value')
        B_test = test['B_profile'].get(sigma_str, {}).get('value')
        if B_base is not None and B_test is not None:
            delta = B_test - B_base
            note = ""
            if abs(delta) > 1e-8:
                note = "CHANGED" if delta < 0 else "worse"
                any_B_change = True
            print(f"  {sigma_str:>8s}  {B_base:10.6f}  {B_test:10.6f}  {delta:+12.8f}  {note}")

    if not any_change and not any_B_change:
        print(f"\n  SUMMARY: No changes detected in A(sigma) or A*(sigma)")
    elif any_change:
        print(f"\n  SUMMARY: A(sigma) CHANGED at some probe points")
    elif any_B_change:
        print(f"\n  SUMMARY: A*(sigma) CHANGED at some probe points (A unchanged)")

    return delta_A


def build_baseline_hs():
    """Build the standard hypothesis set (same as prove_prime_gap2)."""
    from literature import literature
    import zero_density_estimate as zd
    import zero_density_energy_estimate as ze
    from functions import Interval
    from reference import Reference
    from hypotheses import Hypothesis_Set

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


# ====================================================================
# MAIN: Run all gap tests
# ====================================================================

if __name__ == "__main__":
    print("=" * 72)
    print("EXPDB GAP TEST HARNESS")
    print("Checking whether GM interactions are fully exploited")
    print("=" * 72)

    # ------------------------------------------------------------------
    # STEP 1: BASELINE
    # ------------------------------------------------------------------
    print("\n[STEP 1] Computing baseline...")
    t0 = time.time()
    baseline_hs = build_baseline_hs()
    baseline = extract_profile(baseline_hs, "BASELINE (K=4, standard)")
    t1 = time.time()
    print(f"  Baseline computed in {t1-t0:.1f}s")
    print(f"  ||A||_inf = {baseline['A_inf']:.8f}")
    print(f"  theta_PNTALL = {baseline['theta_PNTALL']:.8f}")
    print(f"  sigma* = {baseline['sigma_star']:.6f}")
    print(f"  Binding: {baseline['A_inf_source']}")

    # ------------------------------------------------------------------
    # STEP 2: GAP 1 — Increase K
    # ------------------------------------------------------------------
    print("\n[STEP 2] Testing Gap 1: LVER parameter K...")

    # We need to reload literature with different K
    # The cleanest way: modify the call and reimport
    # Since Python caches imports, we need to be careful

    # Read current literature.py to find the K=4 line
    lit_path = os.path.join(os.path.dirname(__file__),
                            'expdb', 'blueprint', 'src', 'python', 'literature.py')

    with open(lit_path, 'r', encoding='utf-8') as f:
        lit_original = f.read()

    for K_test in [10, 20]:
        print(f"\n  Testing K = {K_test}...")
        # Modify literature.py
        lit_modified = lit_original.replace(
            'add_lver_guth_maynard_2024a(4)',
            f'add_lver_guth_maynard_2024a({K_test})')

        with open(lit_path, 'w', encoding='utf-8') as f:
            f.write(lit_modified)

        # Force reimport
        mods_to_remove = [k for k in sys.modules if k in
                          ('literature', 'additive_energy', 'large_values',
                           'zero_density_estimate', 'zero_density_energy_estimate',
                           'derived', 'hypotheses', 'functions', 'region',
                           'polytope', 'zeta_large_values', 'bound_beta',
                           'bound_mu', 'exponent_pair', 'reference', 'constants',
                           'transform', 'prime_gap')]
        for m in mods_to_remove:
            del sys.modules[m]

        try:
            t0 = time.time()
            test_hs = build_baseline_hs()
            test_profile = extract_profile(test_hs, f"K={K_test}")
            t1 = time.time()
            print(f"  Computed in {t1-t0:.1f}s")
            compare_profiles(baseline, test_profile, f"Gap 1: K=4 vs K={K_test}")
        except Exception as e:
            print(f"  ERROR with K={K_test}: {e}")

    # Restore original
    with open(lit_path, 'w', encoding='utf-8') as f:
        f.write(lit_original)

    # Force reimport back to original
    mods_to_remove = [k for k in sys.modules if k in
                      ('literature', 'additive_energy', 'large_values',
                       'zero_density_estimate', 'zero_density_energy_estimate',
                       'derived', 'hypotheses', 'functions', 'region',
                       'polytope', 'zeta_large_values', 'bound_beta',
                       'bound_mu', 'exponent_pair', 'reference', 'constants',
                       'transform', 'prime_gap')]
    for m in mods_to_remove:
        del sys.modules[m]

    # ------------------------------------------------------------------
    # STEP 3: GAP 2 — Check EP hull vs hardcoded pairs
    # ------------------------------------------------------------------
    print("\n[STEP 3] Testing Gap 2: EP hull vs hardcoded pairs...")

    try:
        from literature import literature
        import exponent_pair as ep
        import zero_density_estimate as zd

        # Get the hardcoded pairs from bourgain_ep_to_zd
        # These are at zero_density_estimate.py lines 633-644
        print("  Reading hardcoded exponent pairs from bourgain_ep_to_zd...")

        zd_path = os.path.join(os.path.dirname(__file__),
                               'expdb', 'blueprint', 'src', 'python', 'zero_density_estimate.py')
        with open(zd_path, 'r', encoding='utf-8') as f:
            zd_content = f.read()

        # Extract the hardcoded pairs by looking for the function
        # We'll just report what we find
        import re
        pairs_match = re.findall(r'frac\((\d+),\s*(\d+)\),\s*frac\((\d+),\s*(\d+)\)', zd_content)
        print(f"  Found {len(pairs_match)} hardcoded (k, l) pairs")
        for i, (k_n, k_d, l_n, l_d) in enumerate(pairs_match[:20]):
            k = frac(int(k_n), int(k_d))
            l = frac(int(l_n), int(l_d))
            # Check Bourgain constraints
            valid = (k < frac(11,85) or (frac(11,85) < k < frac(1,5))) and l >= frac(3,5) and 15*l + 20*k >= 13
            if valid:
                print(f"    Pair {i}: k={k} ({float(k):.6f}), l={l} ({float(l):.6f})  [Bourgain-valid]")

        # Try to compute the EP hull
        print("\n  Computing exponent pair hull from literature...")
        ep_hypotheses = literature.list_hypotheses(hypothesis_type="Exponent pair")
        print(f"  Found {len(ep_hypotheses)} exponent pair hypotheses in literature")
        for h in ep_hypotheses[:10]:
            print(f"    {h.name}: ({h.data.k}, {h.data.l}) = ({float(h.data.k):.6f}, {float(h.data.l):.6f})")
        if len(ep_hypotheses) > 10:
            print(f"    ... and {len(ep_hypotheses)-10} more")

    except Exception as e:
        print(f"  ERROR in Gap 2 test: {e}")
        import traceback
        traceback.print_exc()

    # ------------------------------------------------------------------
    # STEP 5: GAP 5 — Check A* <= 3A propagation
    # ------------------------------------------------------------------
    print("\n[STEP 5] Testing Gap 5: A* <= 3A propagation...")

    try:
        import zero_density_energy_estimate as ze

        # Check if the trivial bounds are in the hypothesis set
        ze_hypotheses = baseline_hs.list_hypotheses(
            hypothesis_type="Zero density energy estimate")
        print(f"  ZDE hypotheses in baseline set: {len(ze_hypotheses)}")

        # Check for trivial bounds
        trivial_count = 0
        for h in ze_hypotheses:
            if 'trivial' in h.name.lower() or '3' in str(h.data):
                trivial_count += 1
                print(f"    Trivial-type: {h.name}")

        if trivial_count == 0:
            print("  NO trivial A* <= 3A bounds found in hypothesis set!")
            print("  This means the pipeline may NOT be using the post-GM trivial bound.")
            print("  Adding trivial bounds and recomputing...")

            # Add trivial bounds
            ze.add_trivial_zero_density_energy_estimates(baseline_hs)
            test_gap5 = extract_profile(baseline_hs, "With trivial A* bounds")
            compare_profiles(baseline, test_gap5, "Gap 5: Adding trivial A* <= 3A")
        else:
            print(f"  Found {trivial_count} trivial-type bounds. Pipeline appears to include them.")

    except Exception as e:
        print(f"  ERROR in Gap 5 test: {e}")
        import traceback
        traceback.print_exc()

    # ------------------------------------------------------------------
    # FINAL SUMMARY
    # ------------------------------------------------------------------
    print("\n" + "=" * 72)
    print("GAP TEST HARNESS: COMPLETE")
    print("=" * 72)
