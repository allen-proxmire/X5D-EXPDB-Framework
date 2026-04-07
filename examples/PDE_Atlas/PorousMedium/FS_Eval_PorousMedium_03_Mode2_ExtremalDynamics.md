# AD Evaluation: Porous Medium Equation — Mode 2: PDE → Extremal Dynamics

Allen Proxmire

April 2026

---

## Overview

Mode 2 moves from the static envelope to the dynamics. The PME Mode 2 analysis is the *simplest* in the PDE Atlas: one dynamical channel (nonlinear diffusion), one geometric feature (free boundary), one universal attractor (Barenblatt), and one asymptotic regime (self-similar spreading). There are no competing channels, no bifurcations, no parameter-dependent regimes, and no qualitative transitions. The entire dynamical program is: spread, smooth, decay, converge to Barenblatt. The drama of the PME is not *what* happens (that is completely determined) but *how fast* — the quantitative rates of spreading, decay, and convergence.

Throughout:

    partial_t u = Delta(u^m),    m > 1,    u >= 0

on R^d (or bounded domains with no-flux boundary conditions).

---

## 1. Fundamental Time and Length Scales

### 1.1 The State-Dependent Diffusion Time Scale

The PME diffusion coefficient D(u) = m u^{m-1} depends on the density itself. The local diffusion time scale at a point with density U and spatial scale L is:

    t_D(U, L) = L^2 / D(U) = L^2 / (m U^{m-1})

This time scale is *state-dependent*: diffusion is fast where u is large and slow (infinitely slow) where u is zero. Contrast with the linear heat equation (m = 1), where t_D = L^2 / D is uniform — the same everywhere, independent of the solution value.

The state-dependence of t_D is the structural origin of all PME phenomenology:

- **Dense regions** (U >> 0): t_D is short. Diffusion acts quickly, smoothing concentration gradients on a fast time scale. The interior of the support behaves like a nonlinear but non-degenerate parabolic equation.
- **Near-vacuum regions** (U → 0): t_D → infinity. Diffusion grinds to a halt. The density cannot spread into the vacuum — the free boundary advances only as fast as the density gradient can push it.
- **Vacuum** (U = 0): t_D = infinity. No diffusion at all. The vacuum is frozen.

### 1.2 Three Geometric Regimes

The PME dynamics partition the spatial domain into three regions with qualitatively different behavior:

**Regime (i): Interior Smoothing (u > 0, away from the free boundary)**

Inside the support, u is bounded away from zero: u >= delta > 0. The diffusion coefficient D(u) >= m delta^{m-1} > 0 is uniformly positive, and the equation is *uniformly parabolic*. The dynamics are:

- Smooth: u in C^{infinity}(interior of support x (0, T)) for smooth initial data.
- Regularizing: rough initial data is instantaneously smoothed.
- Decaying: ||u||_{L^{infinity}} decreases as t^{-alpha}.
- Non-degenerate: all estimates for uniformly parabolic equations apply.

The interior regime is the *well-behaved* part of the PME — structurally similar to the linear heat equation, with the nonlinearity D(u) = m u^{m-1} providing quantitative but not qualitative differences.

**Regime (ii): Free-Boundary Motion (u = 0 at the boundary of the support)**

At the free boundary Gamma(t) = partial {u > 0}, the density approaches zero from the positive side. The diffusion coefficient degenerates, and the regularity drops: u is typically only Holder continuous (not C^1) at Gamma(t). The dynamics are governed by the *Darcy law*:

    V_n = -partial_n(u^{m-1}) / (m-1)    (generalized)

or equivalently, the free boundary moves at a speed determined by the pressure gradient at the interface (where the "pressure" is p = m u^{m-1} / (m-1)).

The free-boundary regime is the *architecturally distinctive* part of the PME — it has no counterpart in AC, CH, or the linear heat equation. The free boundary is a *moving singular surface* where the equation degenerates.

**Regime (iii): Far-Field Vacuum (u = 0)**

Outside the support, u = 0 identically. There is no dynamics, no diffusion, no evolution. The vacuum is perfectly static until the free boundary reaches it.

### 1.3 Contrast with Other Architectures

| Feature                    | PME                         | AC                  | CH                  | RD                   |
|----------------------------|-----------------------------|---------------------|---------------------|----------------------|
| Propagation speed          | Finite (degenerate)         | Infinite (linear D) | Infinite (linear D) | Constitutive         |
| Interface type             | Sharp (free boundary)       | Diffuse (tanh)      | Diffuse (tanh)      | Constitutive         |
| Interior regularity        | C^{infinity}               | C^{infinity}        | C^{infinity}        | C^{infinity}         |
| Interface regularity       | Holder (C^{alpha})          | C^{infinity}        | C^{infinity}        | Constitutive         |
| Diffusion time scale       | State-dependent (u^{m-1}/L^2)| Fixed (eps^2/L^2) | Fixed (eps^2/L^4)  | Fixed (D/L^2)        |
| Vacuum dynamics            | Frozen                      | N/A (no vacuum)     | N/A (no vacuum)     | Constitutive         |

The PME is the only architecture in the Atlas with a *state-dependent* diffusion time scale, *finite-speed propagation*, and a *free boundary*. These three features are structurally coupled: they all arise from the single feature of degenerate diffusion at u = 0.

---

## 2. Extremal Behaviors

### E1. Finite-Speed Propagation (Compact Support Preserved)

If supp(u_0) subset B(0, R_0), then supp(u(t)) subset B(0, R(t)) with:

    R(t) <= C(m, d, M) (t + t_0)^{beta},    beta = 1/(d(m-1) + 2)

The support expands at algebraic rate t^{beta} — decelerating over time (beta < 1). No information escapes the support faster than this rate.

**Extremal propagation:** The Barenblatt solution saturates this bound: its free boundary expands at exactly R(t) = C t^{beta}. This is the *fastest possible* spreading for a given total mass M — any other initial datum with the same mass spreads no faster.

**Waiting-time connection:** For certain initial data (flat-topped, with u_0(x) ~ |x - x_0|^{alpha} near the boundary), the free boundary can remain *stationary* for a positive waiting time t_w > 0 before beginning to move. The waiting time is a *structural feature* of degenerate diffusion: the interface does not move until the density gradient at the boundary becomes sufficiently steep to overcome the degeneracy. See E7 below.

### E2. Free-Boundary Motion Law

The free boundary Gamma(t) moves with normal velocity:

    V_n = lim_{x → Gamma(t)^+} [-nabla(u^m) . n / u]

For smooth free boundaries, this simplifies to the *Darcy velocity*:

    V_n = -(m/(m-1)) partial_n(u^{m-1})

where the limit is taken from the positive side. The velocity depends on the *pressure gradient* p = m u^{m-1}/(m-1) at the interface.

**Extremal velocity:** For the Barenblatt solution on R^d:

    V_n(t) = dR/dt = C beta t^{beta-1}

This velocity is *decelerating* (beta - 1 < 0): the free boundary slows down as it expands. The deceleration is a consequence of mass conservation: as the support expands, the mass spreads over a larger volume, the density near the boundary decreases, and the density gradient driving the boundary weakens.

**Geometric law:** For general (non-spherical) free boundaries, the motion depends on the *local curvature* and the *local density gradient*. Convex free boundaries tend to become more spherical over time — the curvature-dependent corrections to the Darcy velocity are regularizing. This is the PME analogue of mean-curvature regularization in AC, but operating through the density gradient rather than through surface tension.

### E3. Barenblatt Self-Similar Spreading (Universal Attractor)

The Barenblatt profile:

    B(x, t; M) = t^{-alpha} [C_0 - k |x|^2 / t^{2beta}]_+^{1/(m-1)}

with alpha = d/(d(m-1)+2), beta = 1/(d(m-1)+2), and C_0, k determined by m, d, M.

**Universality:** For *any* non-negative u_0 in L^1(R^d) with integral u_0 = M:

    lim_{t→infinity} t^{alpha} ||u(t) - B(t; M)||_{L^{infinity}} = 0

The convergence is universal — it holds for all initial data, regardless of shape, symmetry, or regularity. The Barenblatt profile is the unique attractor of the PME dynamics, parameterized solely by the total mass M.

**Rate of convergence:** Under moment conditions on u_0 (e.g., integral |x|^2 u_0 dx < infinity), the convergence rate is:

    ||u(t) - B(t; M)||_{L^1} <= C t^{-gamma}

where gamma > 0 depends on the initial data's moments. The sharper the initial data concentrates near the Barenblatt profile, the faster the convergence.

### E4. Algebraic Decay of Height and Expansion of Radius

The PME solution has two coupled power-law behaviors:

**Height decay:**
    ||u(t)||_{L^{infinity}} ~ M^{2beta} t^{-alpha}    as t → infinity

**Radius expansion:**
    R(t) ~ M^{(m-1)beta} t^{beta}    as t → infinity

**Mass conservation links them:**
    ||u||_{L^{infinity}} * R(t)^d ~ M    (the mass is spread over volume R^d at height ~ ||u||_{L^{infinity}})

The two power laws are not independent — they are coupled through the conservation constraint alpha = d beta. As the height decreases, the radius must increase to preserve mass, and the rates are locked together by the self-similar scaling.

### E5. L^1 Contraction (Strongest Stability in the Atlas)

For any two PME solutions u, v:

    ||u(t) - v(t)||_{L^1} <= ||u_0 - v_0||_{L^1}    for all t >= 0

This is the *strongest stability property* in the entire PDE Atlas:

- **Stronger than energy stability** (NS: ||**u** - **v**||_{L^2} bounded but possibly growing in 3D).
- **Stronger than Lyapunov decay** (AC/CH: F[phi(t)] decreases but doesn't directly bound ||phi(t) - psi(t)||).
- **Stronger than comparison** (E6: ordering is preserved but distance is not controlled).

The L^1 contraction implies:
- **Uniqueness:** If u_0 = v_0 a.e., then u(t) = v(t) for all t.
- **Continuous dependence:** Small changes in initial data produce small changes in the solution for all time.
- **Asymptotic convergence:** All solutions with the same mass converge to the same Barenblatt profile (since ||u(t) - B(t;M)||_{L^1} is non-increasing and the Barenblatt profile is the unique steady state in rescaled variables).

### E6. Instantaneous Regularization Inside the Support

For t > 0, the PME solution is smooth in the interior of its support:

    u in C^{infinity}({u > 0} ∩ (Omega x (0, T)))

The regularization is *instantaneous*: even if u_0 is merely in L^1, the solution becomes smooth inside {u > 0} for any t > 0. The smoothing is provided by the *non-degenerate* diffusion in the interior (where u > 0 implies D(u) > 0).

**At the free boundary:** The regularity is *limited*. The density u is Holder continuous (C^{alpha} for some alpha depending on m) across the free boundary, but typically *not* C^1. The pressure p = m u^{m-1}/(m-1) may be Lipschitz continuous across Gamma(t) but the density gradient nabla u may be discontinuous.

This two-tier regularity (C^{infinity} interior, Holder boundary) is unique to the PME among FS-evaluated architectures. AC and CH have C^{infinity} regularity everywhere; NS has C^{infinity} in 2D and open regularity in 3D; the PME has *position-dependent regularity*, with the degeneracy at the free boundary limiting the smoothness.

### E7. Waiting-Time Phenomena

For certain initial data, the free boundary can remain *stationary* for a positive time before beginning to move. The waiting time t_w satisfies:

    t_w > 0    if u_0(x) ~ |x - x_0|^{alpha} with alpha >= 2/(m-1) near a boundary point x_0

**Physical mechanism:** If the initial density approaches zero sufficiently slowly near the boundary (with a shallow enough profile), the density gradient at the boundary is too small to drive the interface forward. The boundary waits until the interior diffusion steepens the gradient sufficiently.

**Waiting-time bound:**

    t_w <= C ||u_0||_{L^{infinity}}^{1-m} R_0^2

where R_0 is the initial support radius. After the waiting time, the free boundary begins to move and never stops again.

**Structural role:** The waiting time is a *structural consequence* of the degeneracy: only degenerate diffusion can produce a free boundary that sits still for positive time. Non-degenerate diffusion (m = 1) has infinite propagation speed and no waiting time. The waiting time is the most delicate dynamical feature of the PME — it depends on the local geometry of the initial data near the free boundary.

### E8. No Oscillations, No Patterns, No Chaos

The PME dynamics are *unconditionally monotone*:

- All convex entropies decrease (E4 from Mode 1).
- L^1 distances between solutions are non-increasing (E5).
- The ordering of solutions is preserved (E6 from Mode 1).
- The free boundary only advances (E1 from Mode 1).

These properties collectively forbid:
- Oscillations (the distance between any two solutions is non-increasing — no recurring behavior).
- Patterns (one species, no reaction — no mechanism for spatial structure beyond the free boundary).
- Chaos (L^1 contraction implies Lipschitz stability — no sensitive dependence on initial conditions).
- Non-convergent dynamics (the entropy dissipation forces convergence to Barenblatt).

The PME is the *most dynamically predictable* PDE in the PDE Atlas: given the total mass M, the complete long-time dynamics are determined up to a universal profile.

---

## 3. Universal Inequalities

---

**U1. Degenerate Parabolic Inequality**

    partial_t u >= 0    on Gamma(t) (from the positive side)

The free boundary can only advance. Support expansion is irreversible.

---

**U2. Finite-Speed Propagation Bound**

    R(t) <= C(m, d, M) (t + t_0)^{beta},    beta = 1/(d(m-1) + 2)

Saturated by the Barenblatt solution. This is the PME speed limit.

---

**U3. Barenblatt Scaling Laws**

    alpha = d/(d(m-1) + 2),    beta = 1/(d(m-1) + 2),    alpha = d beta

The exponents are uniquely determined by m and d. They are *architectural constants*.

---

**U4. Entropy Dissipation Inequality**

    d/dt integral Phi(u) dx <= 0    for all convex Phi with Phi(0) = 0

In particular, for H(u) = integral u^m/(m-1) dx:

    dH/dt = -(4m/(m-1)) integral |nabla(u^{(m+1)/2})|^2 dx <= 0

---

**U5. L^1 Contraction Inequality**

    ||u(t) - v(t)||_{L^1} <= ||u_0 - v_0||_{L^1}    for all t >= 0

The strongest stability estimate in the PDE Atlas.

---

**U6. Comparison Principle**

    u_0 <= v_0  =>  u(t) <= v(t)    for all t >= 0

Order-preserving dynamics.

---

**U7. Free-Boundary Velocity Inequality**

    V_n = -(m/(m-1)) partial_n(u^{m-1})    at smooth points of Gamma(t)

The velocity is slaved to the pressure gradient.

---

**U8. Mass Conservation Identity**

    integral u(x, t) dx = M    for all t >= 0

Exact conservation.

---

**U9. No Blowup Inequality**

    ||u(t)||_{L^{infinity}} <= C(m, d) M^{2beta} t^{-alpha}

The L^{infinity} norm *decays* algebraically. Blowup is structurally impossible.

---

**U10. No Oscillation Inequality (Monotone Smoothing)**

    For all convex Phi: integral Phi(u(t_2)) dx <= integral Phi(u(t_1)) dx    whenever t_2 >= t_1

Combined with U5, this ensures that the dynamics are monotonically smoothing: every measure of complexity decreases over time.

---

### Universal Inequality Summary

| Label | Inequality                     | Type            | Status        | Role                      |
|-------|--------------------------------|-----------------|---------------|---------------------------|
| U1    | Free boundary advances only    | One-sided       | Unconditional | Irreversible expansion    |
| U2    | Finite-speed bound             | Upper bound     | Unconditional | Speed limit               |
| U3    | Barenblatt scaling laws        | Exact           | Unconditional | Architectural constants   |
| U4    | Entropy dissipation            | Exact identity  | Unconditional | Monotone smoothing        |
| U5    | L^1 contraction                | Sharp           | Unconditional | Strongest stability       |
| U6    | Comparison principle           | Order           | Unconditional | Ordering preserved        |
| U7    | Free-boundary velocity         | Slaved          | Smooth Gamma  | Interface motion law      |
| U8    | Mass conservation              | Exact equality  | Unconditional | Fundamental invariant     |
| U9    | No blowup                     | Decay bound     | Unconditional | Envelope sealed           |
| U10   | Monotone smoothing             | Entropy monotone| Unconditional | No oscillation/chaos      |

**All ten inequalities are unconditional.** No dimensional restrictions, no conditional hypotheses, no constitutive dependencies. This is the most uniform set of universal inequalities in the PDE Atlas.

---

## 4. Attractors and Long-Time Behavior

### 4.1 The Universal Attractor: Barenblatt Profile

The PME has a *single* universal attractor — the Barenblatt family {B(x, t; M) : M > 0}, parameterized by total mass.

**Universality theorem (Friedman–Kamin, Vazquez, Carrillo–Toscani):** For any u_0 in L^1(R^d), u_0 >= 0, integral u_0 = M > 0:

    u(t) → B(t; M)    as t → infinity

in L^1, L^{infinity} (rescaled), and intermediate L^p norms. The convergence is *universal*: it depends on u_0 only through the total mass M. All other features of the initial data (shape, symmetry, support geometry, regularity) are *forgotten* in the long-time limit.

This universality is the PME analogue of the central limit theorem:

- **CLT (m = 1):** All finite-variance distributions converge to the Gaussian under iterated convolution.
- **PME attractor (m > 1):** All finite-mass densities converge to the Barenblatt profile under nonlinear diffusion.

The Barenblatt profile plays the role of the Gaussian in the nonlinear theory — it is the *unique fixed point of the rescaled dynamics*.

### 4.2 Why PME Has a Single Asymptotic Regime

The PME's single-attractor structure arises from the combination of three properties:

1. **Mass conservation** fixes the attractor parameter (M).
2. **L^1 contraction** ensures that all solutions with the same mass converge to the same limit.
3. **Entropy dissipation** drives the convergence and provides a rate.

No other structural feature is needed. The PME does not require:
- A Lyapunov functional in the AC/CH sense (entropy dissipation is stronger).
- A maximum principle in the AC sense (comparison principle suffices).
- A spectral gap (the convergence is algebraic, not exponential).

The single-attractor structure is *architecturally forced*: the three properties above are *necessary consequences* of the axioms (PME-3, PME-4, PME-7, PME-8), and they uniquely determine the long-time behavior.

### 4.3 Contrast with Other Architectures

| Architecture | Attractor Structure                          | Parameterization    | Convergence Rate |
|-------------|----------------------------------------------|---------------------|------------------|
| PME         | Single family (Barenblatt)                   | Total mass M        | Algebraic (t^{-gamma}) |
| AC          | Finite set (phi = ±1, unstable interfaces)   | Domain topology     | Exponential (2M rate)  |
| CH          | Manifold (phase-separated configurations)    | Mass + topology     | Algebraic (coarsening) |
| NS (2D)    | Compact finite-dimensional set               | Grashof number      | Dissipation-dependent  |
| RD          | Constitutive-dependent (fixed pts to chaos)  | Kinetics            | Constitutive           |

The PME attractor is the *simplest* in the Atlas: a one-parameter family of explicit profiles. AC's attractor contains multiple equilibria and their connecting orbits. CH's attractor is a manifold of phase-separated states with complex topology. NS's attractor (2D, forced) can be high-dimensional. RD's attractors range from fixed points to strange attractors.

The PME's simplicity is a consequence of its channel structure: one channel (nonlinear diffusion) with one conserved quantity (mass) produces one attractor family (Barenblatt). Every additional channel (reaction in RD, double-well in AC, bilaplacian in CH, advection in NS) enriches the attractor structure.

### 4.4 One Channel → One Geometry → One Attractor

The PME's architectural simplicity produces a uniquely clean dynamical structure:

**One channel:** Nonlinear diffusion Delta(u^m). No reaction, no forcing, no coupling.

**One geometry:** The free boundary Gamma(t) = partial{u > 0}. No diffuse interfaces, no patterns, no waves, no vortices.

**One attractor:** The Barenblatt profile B(x,t;M). Universal, explicit, unique for each mass.

This "1-1-1 structure" is without parallel in the PDE Atlas. Every other evaluated PDE has multiple channels, multiple geometric features, or multiple attractors (or all three). The PME demonstrates the *minimum dynamical complexity* that a nontrivial PDE can achieve.

---

## 5. Comparison with AC, CH, and RD

### 5.1 PME vs. Allen–Cahn

| Feature                    | PME                          | Allen–Cahn                  |
|----------------------------|------------------------------|-----------------------------|
| Propagation speed          | Finite                       | Infinite                    |
| Interface type             | Sharp (free boundary)        | Diffuse (tanh, width eps)   |
| Interface motion           | Darcy velocity (V ~ grad p)  | Mean curvature (V ~ kappa)  |
| Diffusion type             | Degenerate (D ~ u^{m-1})    | Constant (D = M eps^2)      |
| Reaction                   | None                         | phi - phi^3 (double-well)   |
| Conservation               | Yes (mass)                   | No                          |
| Attractor                  | Barenblatt (spreading)       | phi = ±1 (extinction)       |
| Convergence rate           | Algebraic (t^{-gamma})      | Exponential (exp(-2Mt))     |
| Waiting time               | Possible                     | No                          |
| Regularity at interface    | Holder                       | C^{infinity}                |

The deepest difference: PME interfaces are *sharp* and move by pressure gradients; AC interfaces are *diffuse* and move by mean curvature. PME conserves mass; AC does not. PME solutions spread forever; AC solutions converge to uniform states in finite time (via interface extinction).

### 5.2 PME vs. Cahn–Hilliard

| Feature                    | PME                          | Cahn–Hilliard               |
|----------------------------|------------------------------|-----------------------------|
| PDE order                  | 2nd (nonlinear)              | 4th (biharmonic)            |
| Conservation               | Yes (mass)                   | Yes (mass)                  |
| Gradient-flow              | Yes (Wasserstein)            | Yes (H^{-1})                |
| Phase separation           | No (single phase)            | Yes (two phases ±1)         |
| Coarsening                 | No (spreading only)          | Yes (L ~ t^{1/3})           |
| Free boundary              | Yes                          | No (diffuse interfaces)     |
| Attractor                  | Barenblatt (explicit)        | Phase-separated (implicit)  |
| Number of phases           | 1 (density into vacuum)      | 2 (phi = +1, phi = -1)      |

Both PME and CH conserve mass and have gradient-flow structure, but they model fundamentally different physics: PME models *spreading of a single phase into vacuum*; CH models *separation of a mixture into two phases*. The PME free boundary is a matter-vacuum interface; the CH interface is a matter-matter interface.

### 5.3 PME vs. Reaction–Diffusion

| Feature                    | PME                          | RD (generic)                |
|----------------------------|------------------------------|-----------------------------|
| Reaction                   | None                         | R(u) (arbitrary)            |
| Diffusion                  | Nonlinear, degenerate        | Linear or weakly nonlinear  |
| Species                    | 1                            | n >= 1                      |
| Oscillations               | Forbidden                    | Permitted                   |
| Patterns                   | Forbidden                    | Permitted (Turing, spirals) |
| Chaos                      | Forbidden                    | Permitted                   |
| Blowup                     | Forbidden                    | Constitutive                |
| Attractor                  | Barenblatt (unique)          | Constitutive (full zoo)     |
| Free boundary              | Yes                          | Constitutive                |

PME is the *most constrained* member of the broader parabolic PDE family: no reaction, no coupling, no forcing. RD is the *least constrained*. The PME sits at the opposite extreme from RD on the constraint-universality axis:

    PME ←— most constrained ————— least constrained ——→ RD

- PME: one channel, one attractor, no oscillations, no patterns, no chaos.
- RD: multiple channels, many attractors, oscillations, patterns, chaos permitted.

### 5.4 Summary Table

| Feature                    | PME          | AC            | CH            | RD            | NS            |
|----------------------------|-------------|---------------|---------------|---------------|---------------|
| Propagation speed          | Finite      | Infinite      | Infinite      | Constitutive  | Infinite      |
| Interface type             | Sharp       | Diffuse       | Diffuse       | Constitutive  | N/A           |
| Conservation               | Yes         | No            | Yes           | Constitutive  | Yes (mass+mom)|
| Gradient flow              | Yes (Wass.) | Yes (L^2)     | Yes (H^{-1})  | Generically no| No            |
| Reaction                   | None        | phi-phi^3     | via mu        | Generic R(u)  | Advection     |
| Attractor                  | Barenblatt  | ±1            | Phase-sep.    | Constitutive  | 2D: exists    |
| Oscillations               | No          | No            | No            | Permitted     | When forced   |
| Blowup                     | No          | No            | No            | Constitutive  | 3D: open      |
| Envelope                   | Closed      | Closed        | Closed        | Constitutive  | 3D: open      |
| Structural complexity      | Lowest      | Low           | Moderate      | Highest       | High          |

The PME is the *structural minimum* of the PDE Atlas: the least complex architecture that produces nontrivial dynamics. Every other architecture adds channels, adds complexity, and enriches the dynamical repertoire — at the cost of structural looseness. The PME demonstrates what nonlinear diffusion alone, without any enrichment, can achieve.

---

*End of Mode 2: PDE → Extremal Dynamics. Mode 3 (Channels → Constraint Surface) will follow in a subsequent file.*
