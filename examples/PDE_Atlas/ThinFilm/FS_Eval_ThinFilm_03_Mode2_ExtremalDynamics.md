# AD Evaluation: Thin-Film Equation — Mode 2: PDE → Extremal Dynamics

Allen Proxmire

April 2026

---

## Overview

Mode 2 moves from the static envelope to the dynamics. The TFE's dynamical landscape is a *hybrid* of the CH and PME landscapes: it has the fourth-order smoothing character of CH (k^4 damping, monotone energy decay, gradient-flow structure) combined with the degenerate free-boundary geometry of PME (contact line, finite-speed propagation, compact support). The resulting dynamics are structurally simple — one channel driving one geometric feature toward one universal attractor — but technically richer than either ancestor because the fourth-order degeneracy introduces phenomena (waiting times, contact-angle selection, positivity questions) that neither second-order degeneracy nor fourth-order non-degeneracy produces alone.

Throughout:

    partial_t h = -div(h^n nabla Delta h),    n > 0,    h >= 0

on Omega subset R^d (d = 1, 2) with no-flux boundary conditions.

---

## 1. Fundamental Time and Length Scales

### 1.1 The State-Dependent Fourth-Order Diffusion Time

The TFE diffusion coefficient is D(h) = h^n, applied to a fourth-order operator. The local diffusion time scale at height H and spatial scale L is:

    t_D(H, L) = L^4 / H^n

This differs from the PME time scale (L^2 / H^{m-1}) in two ways:
- The spatial-scale dependence is L^4 (not L^2) — fourth-order diffusion is *quadratically slower* at large scales than second-order.
- The height dependence is H^n (analogous to PME's H^{m-1}) — diffusion shuts off at H = 0.

The L^4 scaling has profound dynamical consequences:
- Large-scale rearrangements are *extremely slow*: doubling the spatial scale increases the diffusion time by a factor of 16 (compared to 4 for the PME).
- Small-scale smoothing is *extremely fast*: halving the spatial scale decreases the diffusion time by a factor of 16.
- The separation between large-scale and small-scale dynamics is *more extreme* in the TFE than in any second-order architecture.

### 1.2 Three Geometric Regimes

**Regime (A): Interior (h > 0, away from the contact line)**

Inside the support, h is bounded away from zero: h >= delta > 0. The effective diffusion coefficient H^n >= delta^n > 0, and the equation is *uniformly fourth-order parabolic*. The dynamics are:

- C^{infinity} smooth (instantaneous regularization by the fourth-order operator).
- Governed by capillary-pressure equilibration: flow from regions of high -Delta h to regions of low -Delta h.
- Monotone: the surface energy E = (1/2)||nabla h||^2 decreases.
- The L^4 time scale controls: large-scale features evolve slowly; small-scale features are smoothed instantly.

**Regime (B): Contact Line (h = 0 at the boundary of the support)**

At the contact line Gamma(t), the film height approaches zero: h → 0. The mobility degenerates: h^n → 0. The dynamics slow down and the regularity drops:

- h is Holder continuous across the contact line (typically C^{alpha} for some alpha < 1, depending on n).
- The contact-line velocity V_n is determined by the local height profile near Gamma(t).
- The fourth-order structure produces a *capillary-pressure singularity* at the contact line that is regularized by the degeneracy h^n.
- For n = 3 (Navier-Stokes lubrication): the classical *contact-line singularity* of viscous flow theory is resolved by the mobility degeneracy.

**Regime (C): Dry Region (h = 0 identically)**

Outside the support, h = 0. No dynamics, no diffusion, no flow. The dry region is perfectly static until the contact line reaches it. This is identical to the PME's vacuum regime.

### 1.3 Comparison with CH and PME

| Feature                    | TFE                            | CH                           | PME                          |
|----------------------------|--------------------------------|------------------------------|------------------------------|
| Diffusion time scale       | L^4 / H^n                    | L^4 / (M eps^2)             | L^2 / H^{m-1}              |
| Spatial-scale dependence   | L^4 (fourth-order)            | L^4 (fourth-order)           | L^2 (second-order)          |
| State dependence           | H^n (degenerate)              | None (non-degenerate)        | H^{m-1} (degenerate)       |
| Interior regularity        | C^{infinity}                  | C^{infinity}                 | C^{infinity}                |
| Contact-line regularity    | Holder (C^{alpha})            | N/A (no contact line)        | Holder (C^{alpha})          |
| Vacuum/dry region          | Frozen (h = 0)                | N/A (phi defined everywhere) | Frozen (u = 0)              |
| Large-scale separation     | Extreme (L^4)                 | Extreme (L^4)                | Moderate (L^2)              |

The TFE combines CH's L^4 time-scale separation with PME's degenerate contact-line geometry. This produces a system with *both* the extreme scale separation of fourth-order diffusion *and* the sharp geometric interface of degenerate diffusion ��� a combination absent in any other FS-evaluated architecture.

---

## 2. Extremal Behaviors

### E1. Finite-Speed Propagation of the Contact Line (n >= 1)

For n >= 1 with compactly supported initial data:

    supp(h(t)) subset B(0, R(t)),    R(t) <= C t^{beta}

with beta = 1/(n + 2d) (general) or beta = 1/(n + 4) for d = 1 source-type solutions. The contact line advances at finite, decelerating speed:

    dR/dt ~ t^{beta - 1} → 0    as t → infinity

The finite-speed propagation is the geometric consequence of the degeneracy h^n: the mobility vanishes at the contact line, throttling the flux. The fourth-order character makes the spreading *slower* than the PME's: beta_TFE = 1/(n+4) < beta_PME = 1/(m+1) for comparable degeneracy parameters, because the fourth-order operator requires pressure gradients (fourth derivatives) rather than density gradients (second derivatives) to drive the flow.

**Extremal speed:** The self-similar source-type solution saturates the propagation bound: it spreads at exactly R(t) = C t^{beta}. No other solution with the same mass spreads faster.

### E2. Contact-Line Velocity Law

At smooth points of the contact line, the normal velocity is:

    V_n = lim_{x→Gamma^+} [-h^n nabla(Delta h) . n / h]

For the self-similar solution, this simplifies to a power-law dependence on time. The contact-line velocity is *slaved* to the capillary-pressure gradient at the interface, modulated by the mobility degeneracy.

**Contact-angle structure:** Near the contact line, the film profile has the asymptotic form:

    h(x) ~ C |x - x_0|^{alpha}    as x → x_0 in Gamma

where the exponent alpha depends on n and the local dynamics. For n = 3, the profile approaches the contact line with a *finite contact angle* (Tanner's law regime), and the velocity satisfies a relation of the form:

    V_n ~ theta^3 ~ h_x^3    (Tanner's law for thin films)

where theta is the apparent contact angle. The third-power dependence is a structural consequence of the n = 3 mobility combined with the fourth-order capillary driving.

### E3. Self-Similar Spreading

The TFE admits source-type self-similar solutions:

    h(x, t) = t^{-alpha} H(x / t^{beta})

For d = 1:
- alpha = 1/(n + 4) (height decay exponent).
- beta = 1/(n + 4) (spreading exponent).
- The profile H(eta) is compactly supported and determined by a fourth-order ODE.

For general d:
- alpha = d/(n + 2d) (height decay).
- beta = 1/(n + 2d) (spreading).
- alpha = d beta (mass conservation coupling).

**Comparison of spreading rates:**

| Architecture | Spreading exponent beta     | Order | Degeneracy     |
|-------------|----------------------------|-------|----------------|
| PME          | 1/(d(m-1) + 2)            | 2nd   | u^{m-1}       |
| TFE          | 1/(n + 2d)                 | 4th   | h^n            |
| Heat (m=1)   | 1/2 (Gaussian)             | 2nd   | None           |
| Biharmonic   | 1/4 (d=1)                  | 4th   | None           |

The TFE spreading is slower than the PME's for comparable parameters because the fourth-order operator introduces an additional L^2 factor in the time scale.

**Attractor property:** Generic finite-mass solutions converge to the self-similar source-type profile as t → infinity. The convergence is universal — all initial-data dependence beyond total mass M is forgotten in the long-time limit. This is the TFE's version of the PME's Barenblatt attractor theorem.

### E4. Fourth-Order Smoothing

Inside the support {h > 0}, the fourth-order operator provides:

    Damping rate of mode k: sigma(k) ~ -h^n k^4

The k^4 dependence means:
- High-frequency modes are damped *quadratically faster* than in PME (k^4 vs. k^2).
- The interior of the support becomes C^{infinity} instantaneously (for t > 0), regardless of initial regularity.
- The smoothing is *stronger* than any second-order architecture can provide.

At the contact line, the smoothing degenerates (h^n → 0), and the regularity drops to Holder. This two-tier regularity (C^{infinity} interior, Holder boundary) mirrors the PME's structure but occurs at one higher order of differentiability.

### E5. Exact Energy Dissipation

    dE/dt = -integral h^n |nabla Delta h|^2 dx

This is the TFE's Lyapunov identity — exact for smooth solutions. The dissipation rate D(t) = integral h^n |nabla Delta h|^2 dx is:

- Strictly positive for non-flat h (D(t) > 0 unless nabla Delta h = 0 in {h > 0}).
- Degenerate at the contact line (h^n → 0 suppresses the dissipation density near Gamma).
- Integrable over all time: integral_0^{infinity} D(t) dt = E[h_0] < infinity.

The finite total dissipation budget forces the system to approach equilibrium. The dissipation rate D(t) itself decays to zero as t → infinity — the dynamics slow down monotonically.

### E6. Waiting-Time Phenomena

Like the PME, the TFE can exhibit *waiting times*: for certain initial data, the contact line remains stationary for a positive time t_w > 0 before beginning to move.

Waiting times occur when the initial height profile approaches zero slowly enough near the contact line that the capillary-pressure gradient is initially too small to overcome the mobility degeneracy. The contact line remains pinned until the interior fourth-order diffusion steepens the profile sufficiently.

**Structural mechanism:** The waiting time is a consequence of the *competition between the degeneracy* (which freezes the contact line when h is small) and the *fourth-order smoothing* (which eventually steepens the profile and drives the contact line forward). In the PME, the analogous competition is between degeneracy and second-order smoothing — the mechanism is the same but the time scales differ (L^4 vs. L^2).

**Comparison with PME:** TFE waiting times are expected to be *longer* than PME waiting times for comparable initial profiles, because the fourth-order operator is slower at large scales. The profile must steepen through a fourth-order mechanism (capillary-pressure equilibration) rather than a second-order mechanism (direct density diffusion).

### E7. Instantaneous Regularization Inside the Support

For t > 0, the TFE solution is C^{infinity} in the interior of {h > 0}:

    h in C^{infinity}({h > 0} cap (Omega x (0, T)))

The fourth-order smoothing provides two extra derivatives of regularity compared to the PME's second-order smoothing. Inside the support, the TFE behaves like a (nonlinear) biharmonic equation with smooth coefficients — all standard fourth-order parabolic regularity theory applies.

At the contact line, the regularity drops to Holder: h is continuous but nabla h may be discontinuous, and higher derivatives of h may blow up as h → 0. This is the *degenerate boundary layer* of the TFE — a thin region near the contact line where the fourth-order smoothing battles the mobility degeneracy.

### E8. No Oscillations, No Chaos

The gradient-flow structure (E5) combined with the absence of a reaction channel (TFE-7) forbids:

- Limit cycles (E decreasing → no periodic orbits).
- Sustained oscillations (E monotone → no recurrence).
- Chaos (gradient flows are monotone systems → no sensitive dependence in the long-time limit).
- Pattern formation (n = 1 species, no reaction → no Turing instability).

The TFE dynamics are *monotonically simplifying*: the surface flattens, the contact line expands, and the film approaches a uniform-height configuration (h = M/|support|). The dynamics are as predictable as the PME's — one channel, one attractor, no surprises.

---

## 3. Universal Inequalities

---

**U1. Energy Dissipation Identity**

    E[h(t)] + integral_0^t integral h^n |nabla Delta h|^2 dx ds = E[h_0]

Exact identity. Closed energy accounting with no gap.

---

**U2. Mass Conservation Identity**

    integral h(x, t) dx = M    for all t >= 0

Exact conservation of total film volume.

---

**U3. Fourth-Order Smoothing Estimate**

For the linearized equation (constant mobility h_0 > 0):

    ||nabla^k h(t)||_{L^2} <= C_k t^{-k/4} ||h_0||_{L^2}    for t > 0, k >= 0

Each derivative costs t^{-1/4} — slower per derivative than second-order (t^{-1/2}) but applicable to higher total order.

---

**U4. Finite-Speed Propagation Bound (n >= 1)**

    R(t) <= C(n, d, M) t^{beta},    beta = 1/(n + 2d)

Contact line cannot advance faster than the self-similar rate. Saturated by the source-type solution.

---

**U5. Self-Similar Scaling Laws**

    alpha = d/(n + 2d),    beta = 1/(n + 2d),    alpha = d beta

Height decays as t^{-alpha}; radius grows as t^{beta}. Exponents uniquely determined by n and d.

---

**U6. Entropy/Energy Functional Inequalities**

    ||nabla h(t)||_{L^2}^2 = 2 E[h(t)] <= 2 E[h_0]    for all t >= 0

The surface energy provides uniform-in-time H^1 control. Additional entropy functionals (integral h^{alpha} dx for appropriate alpha) may also be dissipated under specific conditions on n.

---

**U7. Curvature Bounds from Energy**

    ||Delta h||_{L^2}^2 is controlled by E and boundary terms

Through the energy dissipation and interpolation:

    integral_0^T ||Delta h||_{L^2}^2 dt <= C(E[h_0], T)

providing time-integrated curvature control.

---

**U8. No-Blowup Inequality (Physical Regime, n >= 1)**

    ||h(t)||_{L^{infinity}} <= C(n, d, M, E[h_0])    for all t > 0

Follows from mass conservation + energy bounds + Sobolev/interpolation. The maximum film height is uniformly bounded and decaying.

---

**U9. Monotone Decay of Surface Energy**

    E[h(t_2)] <= E[h(t_1)]    for all t_2 >= t_1 >= 0

Strict Lyapunov property. The film surface becomes monotonically flatter.

---

**U10. Positivity-Preservation Conditions**

    n >= 1:  h_0 >= 0 => h(t) >= 0    (positivity preserved)
    0 < n < 1:  positivity may fail    (open structural question)

The n-dependent positivity condition. For the physical case n = 3, positivity is preserved — the envelope is sealed. For 0 < n < 1, the positivity face may be open.

---

### Universal Inequality Summary

| Label | Inequality                        | Type            | Status              | Role                        |
|-------|-----------------------------------|-----------------|---------------------|-----------------------------|
| U1    | Energy dissipation identity       | Exact equality  | Unconditional       | Primary accounting          |
| U2    | Mass conservation                 | Exact equality  | Unconditional       | Fundamental invariant       |
| U3    | Fourth-order smoothing            | Estimate        | Interior, t > 0     | High-k damping              |
| U4    | Finite-speed bound                | Upper bound     | n >= 1              | Contact-line speed limit    |
| U5    | Self-similar scaling              | Exact exponents | All n > 0           | Architectural constants     |
| U6    | Energy functionals                | Bound           | Unconditional       | H^1 control                 |
| U7    | Curvature bounds                  | Integrated      | Unconditional       | Delta h control             |
| U8    | No blowup                         | Decay bound     | n >= 1              | Envelope sealed             |
| U9    | Energy monotonicity               | Lyapunov        | Unconditional       | Gradient-flow structure     |
| U10   | Positivity                        | n-dependent     | n >= 1: unconditional| Positivity face             |

---

## 4. Attractors and Long-Time Behavior

### 4.1 The Self-Similar Source-Type Attractor

For finite-mass initial data h_0 on R^d, the TFE solution converges to the self-similar source-type profile:

    h(x, t) → H_*(x / t^{beta}) t^{-alpha}    as t → infinity

where H_* is the unique compactly supported similarity profile with mass M. The convergence is:

- **In L^1:** ||h(t) - h_{ss}(t)||_{L^1} → 0.
- **In rescaled variables:** t^{alpha} h(t^{beta} x, t) → H_*(x).
- **Universal:** Independent of the shape of h_0 (depends only on M).

This is the TFE's version of the PME's Barenblatt theorem: nonlinear degenerate diffusion (whether second-order or fourth-order) drives all finite-mass data toward a unique self-similar profile parameterized by mass alone.

### 4.2 Spreading Rate Dependence on n

The spreading exponent beta = 1/(n + 2d) decreases as n increases:

| n    | beta (d=1) | beta (d=2) | Physical interpretation                |
|------|-----------|-----------|----------------------------------------|
| 1    | 1/5       | 1/5       | Linear mobility                        |
| 2    | 1/6       | 1/6       | Intermediate                           |
| 3    | 1/7       | 1/7       | Navier–Stokes thin film (no-slip)     |
| 4    | 1/8       | 1/8       | Strong degeneracy                      |

Larger n → slower spreading. The contact line advances more sluggishly as the mobility vanishes more strongly at h = 0. For n = 3 (the physical case), the spreading is slow: R(t) ~ t^{1/7} in d = 1. A film that doubles its radius takes 2^7 = 128 times as long ��� the spreading decelerates dramatically over time.

### 4.3 Comparison with Other Architectures

| Architecture | Attractor                    | Spreading       | Conservation | Order |
|-------------|------------------------------|-----------------|-------------|-------|
| PME         | Barenblatt (explicit)        | R ~ t^{1/(m+1)} | Yes         | 2nd   |
| **TFE**     | **Self-similar (4th-order)** | **R ~ t^{1/(n+4)}** | **Yes** | **4th** |
| CH          | Phase-separated domains      | Coarsening L~t^{1/3}| Yes      | 4th   |
| AC          | phi = ±1 (uniform)           | Extinction       | No          | 2nd   |
| RD          | Constitutive                 | Constitutive     | Constitutive| 2nd   |

The TFE attractor is structurally closest to the PME's Barenblatt attractor: both are self-similar spreading profiles, explicit (determined by an ODE), universal (parameterized by mass alone), and algebraically decaying. The key difference is the spreading rate: TFE spreads as t^{1/(n+2d)} while PME spreads as t^{1/(d(m-1)+2)} — the fourth-order TFE is slower at large scales.

CH's attractor is qualitatively different: it consists of *phase-separated configurations* (two domains with phi = ±1) rather than *spreading profiles*. CH coarsens (domains merge) while TFE spreads (a single film expands). The two architectures share fourth-order structure but model fundamentally different physics (phase separation vs. film spreading).

### 4.4 The Hybrid Nature: CH Smoothing + PME Geometry

The TFE's long-time behavior combines features of both ancestors:

**From CH:** Fourth-order smoothing dominates the interior dynamics. The surface energy E = (1/2)||nabla h||^2 is the Lyapunov functional. High-frequency modes are damped at rate k^4. The interior is C^{infinity} for t > 0.

**From PME:** Degenerate mobility dominates the contact-line dynamics. The free boundary propagates at finite speed. The support is compact. The long-time behavior is self-similar spreading to an explicit profile.

**Unique to TFE:** The interplay of fourth-order smoothing with degenerate free-boundary motion produces phenomena absent in both ancestors:
- Contact-angle selection (Tanner's law for n = 3).
- Fourth-order waiting times (longer than PME waiting times).
- The positivity question (fourth-order operator + degeneracy = can h go negative?).
- Capillary-pressure singularity resolution at the contact line.

---

## 5. Comparison with AC, CH, PME, and RD

### 5.1 The 2×2 Gradient-Flow Hierarchy

The four gradient-flow architectures form a 2×2 grid:

|                    | Non-conserved       | Conserved             |
|--------------------|--------------------|-----------------------|
| **Non-degenerate** | AC (2nd, L^2 flow) | CH (4th, H^{-1} flow)|
| **Degenerate**     | PME (2nd, Wass.)   | TFE (4th, weighted H^{-1}) |

Each step in the grid changes one structural feature:
- Horizontal (→): add conservation. Raises PDE order by 2.
- Vertical (↓): add degeneracy. Introduces free boundary and finite speed.

The TFE occupies the bottom-right corner: *maximum structural complexity* within the gradient-flow class. It inherits features from all three other corners and adds its own unique phenomena.

### 5.2 Feature-by-Feature Comparison

| Feature                    | AC           | CH           | PME          | TFE               |
|----------------------------|--------------|--------------|--------------|--------------------|
| PDE order                  | 2nd          | 4th          | 2nd          | 4th                |
| Diffusion type             | Linear       | Non-degen.   | Degenerate   | Degenerate         |
| Conservation               | No           | Yes          | Yes          | Yes                |
| Gradient-flow metric       | L^2          | H^{-1}      | Wasserstein  | Weighted H^{-1}    |
| Propagation speed          | Infinite     | Infinite     | Finite       | Finite (n >= 1)    |
| Interface type             | Diffuse      | Diffuse      | Sharp        | Sharp              |
| Free boundary              | No           | No           | Yes          | Yes (contact line) |
| Max. principle              | Yes          | No           | Yes (comparison)| n-dependent     |
| Smoothing rate             | k^2          | k^4          | h^{m-1} k^2 | h^n k^4            |
| Attractor                  | phi = ±1     | Phase-sep.   | Barenblatt   | Self-similar       |
| Spreading law              | Extinction   | Coarsening   | R ~ t^{1/(m+1)}| R ~ t^{1/(n+4)} |
| Oscillations               | No           | No           | No           | No                 |
| Blowup                     | No           | No           | No           | No (n >= 1)        |
| Positivity                 | Yes (\|phi\|<=1)| N/A       | Yes          | n-dependent        |
| Waiting time               | No           | No           | Yes          | Yes                |

### 5.3 Structural Assessment

The TFE is the *most structurally complex gradient-flow architecture* in the PDE Atlas: it has fourth-order smoothing (from CH), degenerate mobility (from PME), conservation (from both), a free boundary (from PME), and a gradient-flow Lyapunov functional (from all four corners). It is the *intersection point* of all four structural features that the gradient-flow hierarchy can provide.

Despite this complexity, the TFE remains anomaly-free in the physical regime (n >= 1): the gradient-flow structure seals the oscillation/chaos faces, the fourth-order smoothing + conservation + degeneracy seals the blowup face, and the n >= 1 condition seals the positivity face. The architecture achieves closure through the *cooperation* of its four inherited mechanisms — each inherited feature contributes to the closure of a specific face.

The TFE's single structural vulnerability is the positivity question for 0 < n < 1: the fourth-order character prevents the maximum principle from operating, and the weak degeneracy may be insufficient to keep h >= 0. This is the *cost* of combining fourth-order smoothing with degeneracy — a structural tension absent in the PME (which has second-order + degeneracy + comparison) and in CH (which has fourth-order + non-degeneracy + no free boundary).

---

*End of Mode 2: PDE → Extremal Dynamics. Mode 3 (Channels → Constraint Surface) will follow in a subsequent file.*
