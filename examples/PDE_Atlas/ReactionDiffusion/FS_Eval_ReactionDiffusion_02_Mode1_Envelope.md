# AD Evaluation: Reaction–Diffusion Systems — Mode 1: Axiom → Envelope

Allen Proxmire

April 2026

---

## Overview

Mode 1 traces the path from the RD axioms (RD-1 through RD-8) to the architectural envelope. The RD envelope is qualitatively different from every previously evaluated architecture. The NS envelope is closed in 2D but open in 3D. The CH and AC envelopes are fully closed in all dimensions. The RD envelope is *constitutively dependent* — its closure, tightness, and structural properties depend on the specific reaction kinetics and diffusion coefficients chosen under RD-8. The RD architecture, as a class, has the *loosest* envelope in the PDE Atlas: it permits the widest range of dynamical behaviors, including phenomena (oscillations, chaos, Turing patterns) that are axiomatically forbidden in gradient-flow architectures.

Throughout, we work with the canonical RD system:

    partial_t **u** = **D** Delta **u** + **R**(**u**)

on Omega subset R^d (d = 1, 2, 3), with **u** = (u_1, ..., u_n), **D** positive definite (or semi-definite), and **R** : R^n → R^n smooth.

---

## 1. Forbidden Configurations

### F1. Nonlocal Reaction Terms

**Axiom source:** RD-2 (Locality).

The reaction terms R_i(**u**) depend only on **u**(x, t) at each point — not on **u** at distant points, not on integrals of **u** over the domain, and not on nonlocal functionals. The following are forbidden:

- Integral reaction terms: R_i = integral K(x, y) u_j(y) dy.
- Mean-field coupling: R_i depends on the spatial average of u_j.
- Nonlocal competition kernels (common in ecology but outside the standard RD architecture).

The RD architecture is *fully local*: every interaction is mediated by pointwise values and local derivatives. This is the same locality as AC and CH, and stronger than NS (which has the nonlocal pressure channel).

### F2. Non-Elliptic Diffusion

**Axiom source:** RD-3 (Diffusion Structure), RD-7 (Forward Parabolicity).

The diffusion matrix **D** must be positive semi-definite (and, for uniformly parabolic systems, positive definite). Non-elliptic diffusion — with negative eigenvalues of **D** — is forbidden because it produces a backward-heat-type equation that is catastrophically ill-posed:

- **D** with a negative eigenvalue → some modes grow at rate |D| k^2, faster at smaller scales → instantaneous blowup of high-frequency modes.
- Cross-diffusion matrices with det(**D**) < 0 can produce similar ill-posedness.

The ellipticity condition is not a physical law but a *well-posedness requirement*: it is the structural condition under which the PDE has solutions in the forward direction.

### F3. Backward Parabolicity

**Axiom source:** RD-7 (Time Orientation).

The RD architecture evolves forward in time. Backward evolution (partial_t **u** = -**D** Delta **u** - **R**(**u**)) is forbidden: it reverses the sign of the diffusion operator, making the equation ill-posed. The past cannot be recovered from the present — the diffusion channel destroys information irreversibly.

This is a structural irreversibility: the RD architecture distinguishes past from future through the sign of the diffusion operator. Time-reversal symmetry is broken by construction.

### F4. Infinite-Speed Propagation (for Nonlinear/Degenerate Diffusion)

**Axiom source:** RD-3 (Diffusion Structure).

For *linear* diffusion (constant **D**), the heat kernel has infinite speed of propagation: a point perturbation is felt everywhere instantaneously (though with exponentially small amplitude at large distances). This is a structural feature, not a bug — linear parabolic equations propagate information at infinite speed.

For *nonlinear/degenerate* diffusion (e.g., porous medium equation with D(u) = m u^{m-1}, m > 1), the propagation speed is finite. The diffuse interface has a sharp front that moves at a well-defined speed. Infinite-speed propagation is forbidden in this sub-class.

The distinction is constitutive (RD-8): linear diffusion allows infinite speed; degenerate diffusion forbids it. The RD architectural class contains both behaviors.

### F5. Conservation Laws (Unless Explicitly Imposed)

**Axiom source:** RD-4 (Reaction Terms), RD-8 (Constitutive Choices).

A generic RD system does *not* conserve total mass:

    d/dt integral u_i dx = integral R_i(**u**) dx + boundary terms

The integral of R_i is nonzero in general. Conservation of integral u_i requires the specific structural condition integral R_i(**u**) dx = 0 for all admissible **u**, which holds only for special reaction kinetics (e.g., R_1 + R_2 = 0 in a two-species conversion reaction).

Conservation is *not* an architectural property of the RD class — it is a constitutive specialization. When present, it adds structure analogous to CH-3 (conserved order parameter). When absent (the generic case), the architecture is free to create and destroy species locally.

### F6. Variational / Gradient-Flow Structure (Generically)

**Axiom source:** RD-4 (Reaction Terms), RD-8 (Constitutive Choices).

A generic RD system is *not* a gradient flow of any functional. The gradient-flow condition requires:

    R_i(**u**) = -partial F / partial u_i

for some functional F[**u**]. For multi-species systems (n >= 2), this is a severe restriction: it requires the Jacobian matrix partial R_i / partial u_j to be symmetric. Most reaction kinetics of physical interest (predator-prey, activator-inhibitor, chemical oscillators) have *asymmetric* Jacobians and are not gradient flows.

Consequences of non-gradient structure:
- No Lyapunov functional is guaranteed (F8 below).
- Limit cycles, oscillations, and chaos are *permitted* (not forbidden by monotone energy descent).
- Traveling waves with non-trivial phase dynamics are permitted.
- The dynamics are not confined to monotone descent through an energy landscape.

The gradient-flow property is a *constitutive specialization* (realized by AC, not by general RD). Its absence is the structural reason that the RD class permits oscillatory and chaotic dynamics.

### F7. Maximum Principle for Multi-Species Systems (n >= 2)

**Axiom source:** RD-3 (Diffusion Structure), RD-4 (Reaction Terms).

The classical maximum principle holds for *scalar* second-order parabolic equations (n = 1) with appropriate reaction terms (R inward-pointing at the boundary of an invariant set). For *systems* (n >= 2), the component-wise maximum principle generally fails:

- The coupling between species (through R and cross-diffusion) can drive individual concentrations outside their natural range.
- There is no general mechanism preventing u_i from becoming negative in a system where all u_j start positive, unless the reaction kinetics satisfy specific *quasi-positivity* conditions: R_i(**u**) >= 0 whenever u_i = 0 and u_j >= 0 for j ≠ i.

The scalar maximum principle is a *structural gift* of scalar second-order parabolic equations. Multi-species RD systems do not receive this gift. Invariant-region theory (Chueh–Conley–Smoller) provides partial substitutes — *bounded invariant regions* that the dynamics cannot escape — but these require specific structural conditions on **R** and **D** that are not generically satisfied.

### F8. Global Lyapunov Functional (Generically)

**Axiom source:** RD-4, RD-8.

A generic multi-species RD system has no known Lyapunov functional — no scalar quantity V[**u**] that decreases monotonically along all trajectories. Without a Lyapunov functional:

- The dynamics are not guaranteed to converge to equilibrium.
- Limit cycles (periodic orbits) are permitted.
- Strange attractors and spatiotemporal chaos are permitted.
- The long-time behavior can be qualitatively unpredictable.

Specific RD systems *do* have Lyapunov functionals:
- AC has F[phi] = integral [f(phi) + (epsilon^2/2)|nabla phi|^2] dx.
- Gradient systems (symmetric Jacobian) have F[**u**] = integral [V(**u**) + (1/2) sum D_i |nabla u_i|^2] dx where R = -grad V.
- Some cooperative systems have entropy-type Lyapunov functionals.

But these are constitutive specializations, not architectural properties.

### F9. Fourth-Order Smoothing

**Axiom source:** RD-3 (Diffusion Structure).

The RD diffusion channel is second-order: **D** Delta **u**, involving the Laplacian (two spatial derivatives). Fourth-order operators (bilaplacian Delta^2, as in CH) are outside the standard RD architecture. This means:

- The smoothing rate is k^2 (not k^4 as in CH).
- The smoothing is *weaker* than CH's: the Laplacian may not control certain nonlinearities that the bilaplacian would tame.
- The maximum principle is *available* (for scalar equations), compensating for the weaker smoothing.

The RD architecture is the *second-order parabolic* class. Fourth-order parabolic equations (CH, Kuramoto–Sivashinsky, Swift–Hohenberg) are outside this class.

### F10. Nonlocal Constraints (No Pressure-Type Channel)

**Axiom source:** RD-2 (Locality).

The RD architecture has no analogue of the NS pressure Poisson equation — no elliptic constraint that couples all points in the domain instantaneously. There is:

- No divergence-free condition.
- No incompressibility constraint.
- No Lagrange multiplier field.
- No global enforcement mechanism.

All constraints in the RD architecture are local (pointwise or differential). The absence of nonlocal constraints is the structural basis for RD's full locality.

### Summary of Forbidden Configurations

| Label | Forbidden Configuration                   | Excluding Axiom(s)     |
|-------|-------------------------------------------|------------------------|
| F1    | Nonlocal reaction terms                   | RD-2                   |
| F2    | Non-elliptic diffusion                    | RD-3, RD-7             |
| F3    | Backward parabolicity                     | RD-7                   |
| F4    | Infinite-speed propagation (degenerate D) | RD-3 (sub-class)       |
| F5    | Conservation laws (generic)               | RD-4, RD-8             |
| F6    | Gradient-flow structure (generic)         | RD-4, RD-8             |
| F7    | Maximum principle for n >= 2              | RD-3, RD-4             |
| F8    | Global Lyapunov functional (generic)      | RD-4, RD-8             |
| F9    | Fourth-order smoothing                    | RD-3                   |
| F10   | Nonlocal constraints                      | RD-2                   |

---

## 2. Necessary Configurations

### N1. Local Parabolic Smoothing at Small Scales

**Source:** RD-3, RD-7.

The diffusion channel **D** Delta **u** provides second-order parabolic smoothing. In Fourier space, mode k is damped at rate D_min k^2, where D_min is the smallest eigenvalue of **D**. At small scales (large k), the diffusion channel dominates the reaction channel:

    |diffusion rate| / |reaction rate| = D k^2 / ||R'|| → infinity as k → infinity

This means: *at sufficiently small scales, the RD architecture is always diffusion-dominated*. High-frequency oscillations, sharp jumps, and sub-diffusion-scale features are smoothed by the Laplacian. The RD architecture has a *built-in ultraviolet cutoff* provided by the diffusion channel.

### N2. Finite-Speed Interface Propagation

**Source:** RD-3, RD-4 (for degenerate diffusion or bistable reactions).

For scalar RD with bistable reaction and constant diffusion (e.g., Nagumo equation), traveling fronts propagate at a unique selected speed c* determined by the reaction kinetics:

    c* = integral_{u_-}^{u_+} R(u) du / integral |phi'|^2 dz    [variational characterization]

For Fisher–KPP-type reactions (R(0) = R(1) = 0, R'(0) > 0, R(u) > 0 for 0 < u < 1), the minimum wave speed is:

    c_min = 2 sqrt(D R'(0))

Traveling fronts and interfaces propagate at finite, architecturally determined speeds. This is a *necessary consequence* of the reaction-diffusion balance.

### N3. Reaction-Dominated Bulk Dynamics

**Source:** RD-4.

In regions where **u** is spatially uniform (or slowly varying), the PDE reduces to the ODE system:

    d**u**/dt = **R**(**u**)

The bulk dynamics are governed by the reaction kinetics alone. The ODE system determines the fixed points, their stability, limit cycles, and bifurcation structure. All qualitative bulk behaviors (monostability, bistability, excitability, oscillation, chaos) are inherited from the ODE.

### N4. Diffusion-Dominated Small-Scale Dynamics

**Source:** RD-3.

At scales L << L_D = sqrt(D / ||R'||) (the reaction-diffusion length), the dynamics are governed by the diffusion operator alone:

    partial_t **u** ≈ **D** Delta **u**

This is the linear heat equation for each species (decoupled if **D** is diagonal). Solutions decay exponentially toward spatial uniformity on time scale L^2 / D.

### N5. Existence of Multiple Dynamical Regimes

**Source:** RD-4, RD-8.

The reaction kinetics can support qualitatively different dynamical regimes depending on the constitutive parameters. For a single RD system, different parameter ranges can produce:

- **Monostable:** Single stable fixed point. All solutions converge.
- **Bistable:** Two stable fixed points, one unstable. Traveling fronts connect them.
- **Excitable:** Single stable fixed point, but large perturbations trigger a long excursion before returning. Traveling pulses.
- **Oscillatory:** Unstable fixed point surrounded by a stable limit cycle. Sustained oscillations.
- **Chaotic:** Strange attractor in the ODE. Spatiotemporal chaos in the PDE.

The *existence* of multiple regimes is architecturally necessary: the RD framework, being unconstrained by gradient-flow or Lyapunov requirements, necessarily admits reaction kinetics in all of these classes. The specific regime is selected by the constitutive parameters (RD-8).

### N6. Possibility of Turing Instability (Multi-Species)

**Source:** RD-3, RD-4 (for n >= 2 with appropriate kinetics).

For a two-species system with a stable homogeneous steady state **u**_0 (stable in the absence of diffusion), the Turing instability occurs when diffusion *destabilizes* the steady state. The necessary conditions are:

    (i)   tr(**J**) < 0 and det(**J**) > 0    [**u**_0 stable for the ODE]
    (ii)  D_v J_{11} + D_u J_{22} > 0         [diffusion-induced instability]
    (iii) (D_v J_{11} + D_u J_{22})^2 > 4 D_u D_v det(**J**)    [unstable modes exist]

where **J** is the Jacobian of **R** at **u**_0. These conditions require D_v ≠ D_u (differential diffusion) and specific sign structure in **J** (typically activator-inhibitor: J_{11} > 0, J_{22} < 0, J_{12} and J_{21} of appropriate signs).

The Turing instability is a *necessary architectural possibility* for the multi-species RD class: the axioms permit reaction kinetics and diffusion ratios that satisfy conditions (i)–(iii). The instability is absent for single-species systems (n = 1) and for equal-diffusion systems (D_u = D_v).

### N7. Possibility of Traveling Waves and Fronts

**Source:** RD-3, RD-4.

The RD architecture necessarily admits traveling-wave solutions **u**(x, t) = **U**(x - ct) for appropriate kinetics:

- **Bistable fronts:** Monotone fronts connecting two stable fixed points. Speed uniquely selected.
- **Fisher–KPP fronts:** Fronts with minimum speed c_min = 2 sqrt(D R'(0)).
- **Pulses:** Localized traveling structures in excitable media (FitzHugh–Nagumo type).
- **Wave trains:** Periodic traveling waves in oscillatory media.
- **Spiral waves:** Rotating spiral patterns in 2D excitable media.

Traveling waves are a *necessary consequence* of the reaction-diffusion architecture: the interplay of local reaction and spatial diffusion produces propagating structures whenever the reaction kinetics have appropriate fixed-point topology.

### N8. Possibility of Spatiotemporal Chaos

**Source:** RD-4, RD-8 (for n >= 2 or n = 1 with appropriate kinetics).

For multi-species systems with oscillatory kinetics, the RD architecture admits spatiotemporal chaos — irregular, aperiodic spatiotemporal dynamics with sensitive dependence on initial conditions. This occurs when:

- The ODE kinetics have a chaotic attractor (n >= 3), or
- The PDE dynamics destabilize uniform oscillations through spatial coupling (n >= 2), or
- Spiral waves break up into spatiotemporal turbulence (n >= 2 in d >= 2).

Spatiotemporal chaos is a *necessary architectural possibility* — the axioms do not exclude it, and specific constitutive choices realize it. Gradient-flow architectures (AC, CH) exclude chaos by Lyapunov monotonicity; the RD class, lacking this constraint, admits it.

### N9. No Global Conservation Law (Generic)

**Source:** F5 above.

The generic RD system has d/dt integral u_i dx = integral R_i(**u**) dx ≠ 0. Total mass is not conserved. The architecture can create and destroy species locally. Conservation must be *imposed* as an additional structural constraint (by requiring specific relations among the R_i); it is not generated by the axioms.

### N10. No Global Lyapunov Structure (Generic)

**Source:** F8 above.

The generic multi-species RD system has no Lyapunov functional. The dynamics are not confined to monotone descent. The long-time behavior can include limit cycles, quasi-periodic orbits, and strange attractors — none of which are accessible to gradient-flow architectures.

### Summary of Necessary Configurations

| Label | Necessary Configuration                     | Source              |
|-------|---------------------------------------------|---------------------|
| N1    | Parabolic smoothing at small scales         | RD-3, RD-7          |
| N2    | Finite-speed front propagation              | RD-3, RD-4          |
| N3    | Reaction-dominated bulk dynamics            | RD-4                |
| N4    | Diffusion-dominated small-scale dynamics    | RD-3                |
| N5    | Multiple dynamical regimes possible         | RD-4, RD-8          |
| N6    | Turing instability possible (n >= 2)        | RD-3, RD-4          |
| N7    | Traveling waves possible                    | RD-3, RD-4          |
| N8    | Spatiotemporal chaos possible               | RD-4, RD-8          |
| N9    | No global conservation (generic)            | RD-4, RD-8          |
| N10   | No global Lyapunov (generic)                | RD-4, RD-8          |

---

## 3. Envelope Inequalities (E1–E12)

---

**E1. Parabolic Smoothing Inequality**

For the linear part of the RD system:

    ||**u**(t)||_{H^s} <= C(s, t_0) ||**u**_0||_{L^2}    for all t >= t_0 > 0,    s >= 0

The diffusion channel provides instantaneous regularization: L^2 initial data becomes C^{infinity} for t > 0 (in the absence of nonlinear blowup). The smoothing estimate is:

    ||nabla^k **u**(t)||_{L^2} <= C_k t^{-k/2} ||**u**_0||_{L^2}    for the linear heat equation

This is second-order smoothing — weaker than CH's fourth-order smoothing but architecturally sufficient for many regularity arguments.

---

**E2. Reaction–Diffusion Balance Inequality**

The competition between diffusion and reaction defines a characteristic length scale:

    L_RD = sqrt(D / ||**R**'||)

At scales L >> L_RD: reaction dominates (bulk dynamics ≈ ODE system).
At scales L << L_RD: diffusion dominates (dynamics ≈ heat equation).
At scales L ~ L_RD: balance (interfaces, fronts, patterns).

This balance inequality is the *architectural resolution scale* of the RD class, analogous to epsilon in AC/CH and to the Kolmogorov scale eta in NS.

---

**E3. Diffusion-Dominated Small-Scale Bound**

At high wavenumbers (k >> 1/L_RD):

    sigma(k) ≈ -D_min k^2 + O(1)

All sufficiently high-frequency modes decay. The diffusion channel dominates the reaction at small scales, providing an ultraviolet cutoff. No RD system (with positive definite **D**) can generate structure at arbitrarily small scales.

---

**E4. Reaction-Dominated Large-Scale Bound**

At zero wavenumber (k = 0, spatially uniform dynamics):

    d**u**/dt = **R**(**u**)

The spatially uniform dynamics are governed by the ODE system. All large-scale (long-wavelength) behavior is determined by the reaction kinetics. The RD architecture's large-scale behavior is an *ODE property*, not a PDE property.

---

**E5. Turing Instability Condition**

For a two-species system (u, v) with diffusion coefficients D_u, D_v and Jacobian **J** = (partial R_i / partial u_j) at a stable steady state:

    Turing instability iff:
    (i)   tr(**J**) < 0, det(**J**) > 0
    (ii)  D_v J_{11} + D_u J_{22} > 0
    (iii) (D_v J_{11} + D_u J_{22})^2 > 4 D_u D_v det(**J**)

The unstable wavenumber band is:

    k_-^2 < k^2 < k_+^2

where k_±^2 = [D_v J_{11} + D_u J_{22} ± sqrt(discriminant)] / (2 D_u D_v).

The most unstable mode k_max and its growth rate sigma_max are determined by the Jacobian and diffusion coefficients. This is the *pattern-selection mechanism* of the RD architecture: the wavelength of Turing patterns is architecturally determined by E5.

---

**E6. Wave-Speed Inequality for Bistable Fronts**

For scalar RD with bistable reaction (R(u_-) = R(u_+) = 0, R has three zeros):

    c* = integral_{u_-}^{u_+} R(u) du / integral_{-infinity}^{infinity} (phi')^2 dz

where phi(z) is the front profile. The wave speed is *uniquely selected* by the reaction kinetics:

- If integral R(u) du > 0: the front propagates in the direction that expands the more energetically favorable phase.
- If integral R(u) du = 0: the front is stationary (balanced bistability, as in AC with symmetric wells).

For Fisher–KPP type (monostable, R(0) = 0, R'(0) > 0):

    c >= c_min = 2 sqrt(D R'(0))

The minimum wave speed is set by the linearized growth rate at the unstable fixed point.

---

**E7. Excitability Threshold Inequality**

For excitable RD systems (e.g., FitzHugh–Nagumo near the rest state), there exists a threshold perturbation amplitude delta_* such that:

    |**u** - **u**_0| < delta_*    =>    solution returns to rest (sub-threshold)
    |**u** - **u**_0| > delta_*    =>    solution fires a pulse (super-threshold)

The threshold delta_* is determined by the geometry of the nullclines in the (**u**, **v**) phase plane and the time-scale separation epsilon between the fast (u) and slow (v) dynamics.

---

**E8. Oscillation Criterion (Hopf Bifurcation)**

A homogeneous steady state **u**_0 undergoes a Hopf bifurcation (onset of oscillations) when:

    tr(**J**) = 0    and    det(**J**) > 0    [for n = 2]

More generally, when a pair of complex eigenvalues of **J** crosses the imaginary axis. The Hopf condition determines the *onset of sustained oscillations* in the bulk kinetics. When combined with diffusion, the Hopf instability can produce:

- Uniform oscillations (all points oscillating in phase).
- Traveling waves (oscillations propagating through space).
- Spiral waves (rotating patterns in 2D).
- Spatiotemporal chaos (irregular, aperiodic oscillations).

---

**E9. No Maximum Principle for n >= 2 (Negative Envelope Bound)**

For multi-species RD systems, the component-wise maximum principle does *not* hold generically:

    sup_{x,t} u_i(x,t)    is NOT bounded by    sup_x u_{i,0}(x)    in general

The coupling between species (through **R** and cross-diffusion) can amplify individual concentrations beyond their initial range. This is a *negative envelope bound* — a statement about what the architecture does NOT guarantee.

**Exception:** If the reaction kinetics satisfy quasi-positivity (R_i >= 0 when u_i = 0 and u_j >= 0 for j ≠ i), then positivity is preserved: u_i(0) >= 0 implies u_i(t) >= 0. This is a constitutive specialization (common in chemical and biological models) but not an architectural property.

---

**E10. No Lyapunov Identity (Negative Envelope Bound)**

For generic multi-species RD systems:

    There exists no functional V[**u**] such that dV/dt <= 0 along all trajectories

The dynamics are not constrained to monotone descent. The long-time behavior can include periodic orbits, quasi-periodic tori, and chaotic attractors. This is the *fundamental negative envelope bound* of the RD class — the architectural reason why RD permits oscillations and chaos.

**Exception:** Gradient systems (R = -grad V) have the Lyapunov functional F[**u**] = integral [V(**u**) + (1/2) sum D_i |nabla u_i|^2] dx. But these are a constitutive specialization (the AC sub-class), not the generic case.

---

**E11. No Blowup for Scalar RD with Bounded Kinetics**

For scalar RD (n = 1) with reaction R(u) bounded (|R(u)| <= C for all u in an invariant interval):

    ||u(t)||_{L^infinity} <= C    for all t >= 0

The maximum principle + bounded reaction → global regularity. This is the AC envelope bound (E5 in the AC evaluation), specialized to the scalar case.

---

**E12. Possible Blowup for Super-Linear Kinetics**

For scalar RD with super-linear reaction (e.g., R(u) = u^p with p > 1):

    partial_t u = D Delta u + u^p

solutions can blow up in finite time:

    ||u(t)||_{L^infinity} → infinity    as t → T* < infinity

The blowup is *constitutively permitted* by the RD architecture whenever the reaction kinetics grow super-linearly. The Fujita exponent p_F = 1 + 2/d is the critical threshold: for 1 < p <= p_F, *all* positive solutions blow up; for p > p_F, small solutions exist globally while large solutions blow up.

The blowup channel in RD is *constitutive*: it opens or closes depending on the reaction kinetics (RD-8). This contrasts with NS, where the blowup channel is *architectural* (present for all NS solutions in 3D, independent of constitutive choices).

---

### Envelope Summary

The RD envelope is defined by twelve constraints (E1–E12) organized into four tiers:

**Tier 1 — Architectural Constraints (hold for all RD systems):**
- E1: Parabolic smoothing (second-order, unconditional).
- E2: Reaction-diffusion balance (sets characteristic length L_RD).
- E3: Diffusion dominance at small scales (ultraviolet cutoff).
- E4: Reaction dominance at large scales (ODE reduction).

**Tier 2 — Pattern-Formation Bounds (hold for specific sub-classes):**
- E5: Turing instability condition (n >= 2, differential diffusion).
- E6: Wave-speed selection (bistable or monostable reactions).
- E7: Excitability threshold (excitable kinetics with time-scale separation).
- E8: Hopf oscillation criterion (complex eigenvalues crossing imaginary axis).

**Tier 3 — Negative Bounds (what the architecture does NOT guarantee):**
- E9: No maximum principle for n >= 2.
- E10: No Lyapunov identity (generically).

**Tier 4 — Regularity Bounds (constitutive-dependent):**
- E11: No blowup for scalar RD with bounded kinetics.
- E12: Possible blowup for super-linear kinetics (Fujita exponent).

---

## 4. Central Architectural Finding

The RD Mode 1 envelope is the *loosest* of any PDE architecture in the PDE Atlas.

### 4.1 Comparison of Envelope Openness

| Architecture | Envelope Status                  | Open Faces        | Blowup Channel           |
|--------------|----------------------------------|--------------------|--------------------------|
| ED           | Fully closed (static)            | None               | None                     |
| AC           | Fully closed (all d <= 3)        | None               | None                     |
| CH           | Fully closed (all d <= 3)        | None               | None                     |
| NS           | Closed in 2D; open in 3D        | 1 (enstrophy, 3D)  | Vortex stretching (arch.)|
| **RD**       | **Constitutively dependent**     | **Multiple**       | **Constitutive (E12)**   |

The RD envelope does not have a fixed closure status — its openness depends on the constitutive choices (RD-8):

- **Scalar RD with bounded kinetics (AC-type):** Fully closed. Maximum principle + Lyapunov (if gradient) seals all faces.
- **Multi-species RD with bounded kinetics:** Partially closed. Global existence likely but regularity may require specific structural conditions.
- **RD with super-linear kinetics:** Open. Finite-time blowup is possible (E12).
- **RD with oscillatory kinetics:** Open in a different sense — no blowup, but no convergence to equilibrium either. The dynamics can be permanently non-stationary.

### 4.2 What RD Permits That AC/CH Forbid

| Phenomenon                 | AC    | CH    | RD (generic)  |
|----------------------------|-------|-------|---------------|
| Limit cycles               | No    | No    | Yes           |
| Sustained oscillations     | No    | No    | Yes           |
| Traveling pulses           | No*   | No    | Yes           |
| Spiral waves               | No    | No    | Yes           |
| Turing patterns            | No    | No    | Yes (n >= 2)  |
| Spatiotemporal chaos       | No    | No    | Yes           |
| Finite-time blowup         | No    | No    | Yes (E12)     |
| Non-convergent dynamics    | No    | No    | Yes           |

*AC permits traveling *fronts* (monotone) but not traveling *pulses* (localized excitations).

### 4.3 Structural Assessment

The RD architecture is the *universal class for spatially extended nonlinear dynamics*. It achieves this universality by *omitting* the structural constraints that make AC and CH well-behaved:

- **No Lyapunov functional** → permits oscillations and chaos.
- **No conservation law** → permits creation and destruction of species.
- **No maximum principle (n >= 2)** → permits unbounded concentration amplification.
- **No gradient-flow structure** → permits non-monotone, non-convergent dynamics.

The omission of these constraints is not a defect — it is the *architectural price of universality*. The RD class must be loose enough to contain all pattern-forming, oscillatory, and excitable dynamics observed in nature. A tighter envelope (like AC's or CH's) would exclude too many phenomena.

The AD evaluation of RD therefore has a fundamentally different character from the evaluations of AC, CH, and NS. Those evaluations asked whether a *specific* architecture is structurally sound. The RD evaluation asks whether a *class* of architectures has a well-defined structural boundary. The answer is: the boundary exists (Tier 1 constraints hold for all members) but its tightness varies across the class (Tiers 2–4 are constitutive-dependent).

---

*End of Mode 1: Axiom → Envelope. Mode 2 (PDE → Extremal Dynamics) will follow in a subsequent file.*
