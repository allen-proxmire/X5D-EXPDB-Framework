# AD Evaluation: Allen–Cahn Equation — Mode 2: PDE → Extremal Dynamics

Allen Proxmire

April 2026

---

## Overview

Mode 2 moves from the static envelope (Mode 1) to the dynamics — the time-evolution behavior that the AC PDE forces, permits, or forbids. The AC dynamical landscape is *simpler* than CH's and vastly simpler than NS's. Where CH dynamics proceed through a rich sequence (spinodal decomposition → interface formation → coarsening → metastability → equilibrium), AC dynamics proceed through a shorter sequence (phase selection → interface formation → interface shrinkage → extinction → uniform equilibrium). The shorter sequence reflects the absence of mass conservation: without the constraint of preserving total phi, the system takes the fastest path down the energy landscape, annihilating interfaces rather than rearranging them.

Throughout:

    partial_t phi = M epsilon^2 Delta phi + M(phi - phi^3)
    F[phi] = integral [f(phi) + (epsilon^2/2)|nabla phi|^2] dx,    f(phi) = (1/4)(phi^2 - 1)^2

on Omega subset R^d (d = 1, 2, 3) with constant M > 0 and Neumann boundary conditions.

---

## 1. Gradient-Flow Structure and Free-Energy Dissipation

### 1.1 Derivation of the Lyapunov Identity

Compute the time derivative of F:

    dF/dt = integral [f'(phi) partial_t phi + epsilon^2 nabla phi . nabla(partial_t phi)] dx

Integrate by parts on the second term (using nabla phi . n = 0 on partial Omega):

    dF/dt = integral [f'(phi) - epsilon^2 Delta phi] partial_t phi dx = integral mu partial_t phi dx

Substitute partial_t phi = -M mu:

    dF/dt = -M integral |mu|^2 dx = -M ||mu||_{L^2}^2            ... (AC Lyapunov Identity)

### 1.2 Properties of the Dissipation Channel

**Strict monotonicity:** D(t) = M ||mu(t)||_{L^2}^2 >= 0, with D(t) = 0 if and only if mu(x, t) = 0 for (almost) all x. The only states with zero dissipation are equilibria satisfying f'(phi) = epsilon^2 Delta phi pointwise.

**Finite total budget:**

    M integral_0^{infinity} ||mu(s)||^2 ds = F[phi_0] - lim_{t→∞} F[phi(t)] <= F[phi_0]

The total dissipation over all time is bounded by the initial free energy. The budget is fixed at initialization and spent irreversibly.

**Non-monotonicity of the rate:** The dissipation rate D(t) itself is not monotone. During the early phase-selection stage, D(t) may increase as phi departs from the unstable hilltop and mu grows. During the late extinction stage, D(t) decreases toward zero as phi approaches a uniform equilibrium.

### 1.3 Contrast with CH

| Feature                    | Allen–Cahn                  | Cahn–Hilliard                 |
|----------------------------|-----------------------------|------------------------------ |
| Dissipation identity       | dF/dt = -M \|\|mu\|\|^2    | dF/dt = -M \|\|nabla mu\|\|^2|
| Gradient-flow metric       | L^2                         | H^{-1}                       |
| Equilibrium condition      | mu = 0 (pointwise)         | mu = const (spatially uniform)|
| What is dissipated         | Chemical potential itself   | Chemical potential *gradient* |
| Large-scale cost           | O(1) per unit volume       | O(L^2) per unit volume       |

The L^2 metric makes AC dynamics *cheap at large scales*: converting a large domain from phi = 0 to phi = 1 costs O(|Omega|) in the L^2 metric (proportional to the volume of the change), regardless of the domain size. The H^{-1} metric makes the same conversion cost O(|Omega| L^2) in CH, because the mass must be *transported* across distance L. This is why AC is fast (t ~ L^2 relaxation) and CH is slow (t ~ L^4 diffusion-limited coarsening).

The equilibrium conditions also differ qualitatively. AC equilibrium requires mu = 0 *everywhere* — the chemical potential must vanish pointwise. CH equilibrium requires only mu = const — the chemical potential can be nonzero as long as it is spatially uniform. This means CH admits phase-separated equilibria (two phases coexisting with equal chemical potential), while AC equilibria are either uniform states (phi = ±1) or special interface configurations where the mean-curvature flow happens to produce a stationary surface (e.g., minimal surfaces in certain geometries).

---

## 2. Reaction–Diffusion Dynamics

### 2.1 Decomposition of the Chemical Potential

    mu = phi^3 - phi - epsilon^2 Delta phi = mu_R + mu_S

where:
- mu_R = f'(phi) = phi^3 - phi is the *reaction* (double-well) contribution.
- mu_S = -epsilon^2 Delta phi is the *surface-tension* (Laplacian) contribution.

The AC evolution is partial_t phi = -M mu = -M mu_R - M mu_S, which gives:

    partial_t phi = M(phi - phi^3) + M epsilon^2 Delta phi
                  = -M mu_R        +   M mu_S   [with sign convention]

### 2.2 Destabilizing Contribution (Reaction)

The reaction term R(phi) = M(phi - phi^3) = -M f'(phi):

- **At the hilltop** (phi = 0): f'(0) = 0, f''(0) = -1. The hilltop is an *unstable* equilibrium of the ODE dphi/dt = M(phi - phi^3). Small perturbations grow exponentially at rate M.

- **In the spinodal region** (|phi| < 1/sqrt(3)): f''(phi) < 0. The reaction amplifies deviations from the hilltop, driving phase separation.

- **Near the wells** (|phi| close to 1): f''(±1) = 2 > 0. The reaction acts as a *restoring force*, pulling phi back toward ±1 at rate 2M.

- **Beyond the wells** (|phi| > 1): The reaction is inward-pointing, pulling phi back into [-1, 1].

The reaction term is *spatially homogeneous* — it acts identically at every point, independently of neighboring values of phi. It is the ODE part of the PDE: if the Laplacian were absent, every point would evolve independently as dphi/dt = M(phi - phi^3), converging to ±1 depending on the sign of the initial datum.

### 2.3 Stabilizing Contribution (Laplacian)

The smoothing term S(phi) = M epsilon^2 Delta phi:

- Damps mode k at rate M epsilon^2 k^2 (Fourier space).
- Penalizes spatial gradients, favoring smooth configurations.
- Sets the interface width at O(epsilon) by balancing the reaction's tendency to create sharp fronts.

### 2.4 Scale-Dependent Dominance

The competition between R and S determines which channel controls the dynamics at each spatial scale:

**Large scales (L >> epsilon):** The smoothing rate S ~ M epsilon^2 / L^2 is small compared to the reaction rate R ~ M. The reaction channel dominates: phi is driven toward ±1 at each point independently. This is the *bulk relaxation* regime — fast, local, and independent of spatial structure.

**Interface scale (L ~ epsilon):** R ~ S ~ M. The two channels are commensurate, producing the equilibrium interface profile phi = tanh(z/(epsilon sqrt(2))). The interface is the *balanced* state where reaction and diffusion exactly counteract.

**Small scales (L << epsilon):** S ~ M epsilon^2 / L^2 >> M ~ R. The smoothing channel dominates, suppressing sub-interface structure. Features smaller than epsilon are rapidly smoothed out.

This scale separation produces the characteristic AC dynamics: fast bulk selection (on time scale 1/M), followed by slow interface motion (on time scale L^2 / (M epsilon)), with sub-interface details smoothed instantaneously.

---

## 3. Extremal Behaviors

### 3.1 Mean-Curvature Motion of Interfaces

In the sharp-interface limit epsilon → 0, the interface Gamma(t) separating {phi ≈ +1} from {phi ≈ -1} evolves by *mean curvature flow*:

    V_n = M sigma kappa

where V_n is the normal velocity (positive for inward motion of a convex surface), sigma = (2 sqrt(2)/3) epsilon is the surface tension, and kappa is the mean curvature.

Properties of mean curvature flow:
- Convex surfaces remain convex and shrink monotonically.
- The enclosed area/volume decreases: d|enclosed|/dt = -integral_Gamma V_n dS = -M sigma integral_Gamma kappa dS.
- In 2D, a convex curve shrinks to a point in finite time (Gage–Hamilton theorem, Grayson theorem).
- In 3D, convex surfaces shrink to a point in finite time.
- Non-convex surfaces can develop singularities (self-intersections, pinch-offs) before vanishing.

Mean curvature flow is the *extremal interface dynamics* of the AC architecture: the fastest rate at which interfaces can move under the gradient-flow constraint.

### 3.2 Finite-Time Extinction of Droplets

A spherical droplet of radius R in d dimensions shrinks as:

    dR/dt = -(d-1) M sigma / R

Integrating:

    R(t)^2 = R_0^2 - 2(d-1) M sigma t

The droplet vanishes at the *extinction time*:

    T* = R_0^2 / (2(d-1) M sigma) = R_0^2 / (2(d-1) M (2 sqrt(2)/3) epsilon)

For a circle (d = 2): T* = R_0^2 / (2 M sigma).
For a sphere (d = 3): T* = R_0^2 / (4 M sigma).

**Extremal extinction:** The fastest-vanishing droplet is the smallest: T* ~ R_0^2, so small droplets vanish first. Finite-time extinction is architecturally necessary for all closed interfaces — there is no mechanism to sustain a curved interface against mean-curvature shrinkage.

**Comparison with CH:** In CH, a droplet of radius R does *not* vanish. Mass conservation prevents it: the enclosed phase must be transferred elsewhere. Instead, the droplet exchanges material with other droplets (Ostwald ripening), and large droplets grow at the expense of small ones. The CH droplet lifetime is controlled by *inter-droplet diffusion*, not by *curvature-driven shrinkage*.

### 3.3 Exponential Relaxation in Bulk

In regions where phi is close to a well (phi ≈ ±1):

    partial_t phi ≈ -M f''(±1)(phi ∓ 1) + M epsilon^2 Delta(phi ∓ 1)

The leading-order behavior (ignoring the Laplacian for L >> epsilon) is:

    partial_t delta ≈ -2M delta    =>    delta(t) ~ delta(0) exp(-2M t)

where delta = phi ∓ 1. The relaxation rate is 2M = M f''(±1), independent of epsilon, the domain size, and the spatial dimension.

**Extremal relaxation:** The fastest relaxation occurs at the hilltop phi = 0, where the linearized rate is M |f''(0)| = M. Near the wells, the rate is 2M (twice as fast because f''(±1) = 2). The slowest relaxation is at the inflection points phi = ±1/sqrt(3), where f'' changes sign — but these are transient states, not persistent ones.

### 3.4 Metastability of Well-Separated Droplets

A configuration with N well-separated droplets of radii R_1, ..., R_N is *metastable*: each droplet shrinks independently by mean curvature (N3 from Mode 1), and the inter-droplet interactions are exponentially weak:

    |interaction between droplets at distance L| ~ exp(-C L / epsilon)

The metastable lifetime of the configuration is determined by the *smallest* droplet: T_meta ~ R_min^2 / (M sigma). After the smallest droplet vanishes, the configuration has N-1 droplets, and the process repeats.

The *slow manifold* of the AC dynamics is the set of configurations with well-separated interfaces. This manifold can be parameterized by the interface positions and (for droplets) radii. The AC dynamics on the slow manifold are an ODE system:

    dR_i/dt = -(d-1) M sigma / R_i + exponentially small corrections

The leading-order dynamics are *independent* for each droplet — each shrinks at its own rate, determined only by its own curvature. This is fundamentally different from CH coarsening, where the droplets interact through bulk diffusion and the dynamics are *coupled*.

### 3.5 Absence of Coarsening

The AC architecture does *not* coarsen. Coarsening — the growth of larger domains at the expense of smaller ones, preserving total phase volume — is a consequence of mass conservation, which AC does not possess.

In AC:
- Small interfaces shrink and vanish (by mean curvature).
- Large interfaces also shrink (more slowly, because curvature is smaller).
- No interface grows (mean curvature is always positive for closed curves/surfaces in Euclidean space).
- The total interface area is strictly decreasing.
- The number of phase domains is non-increasing (domains can only disappear, not split or grow).

The long-time behavior is *extinction*, not coarsening: all interfaces eventually vanish, and the solution converges to a uniform state phi = +1 or phi = -1 (or a non-trivial stationary solution on certain domain geometries).

### 3.6 Absence of Finite-Time Blowup

The AC architecture has no blowup channel. The structural proof:

1. Maximum principle: ||phi(t)||_{L^infinity} <= max(||phi_0||_{L^infinity}, 1).
2. Bounded nonlinearity: |phi - phi^3| <= C for |phi| bounded.
3. Linear PDE with bounded forcing: partial_t phi = M epsilon^2 Delta phi + g(x,t), ||g||_{L^infinity} <= C.
4. Parabolic regularity: phi in C^{infinity} for t > 0.

No conditional hypothesis is needed. The maximum principle provides L^{infinity} control at step 1, and the rest follows by standard theory.

---

## 4. Universal Inequalities

---

**U1. Free-Energy Dissipation Identity**

    F[phi(t)] + M integral_0^t ||mu(s)||^2 ds = F[phi_0]    for all t >= 0

Exact identity. Primary accounting.

**Structural role:** Determines the total dissipation budget. Guarantees convergence to equilibrium (mu → 0).

---

**U2. Maximum Principle (L^{infinity} Bound)**

    ||phi(t)||_{L^infinity} <= max(||phi_0||_{L^infinity}, 1)    for all t >= 0

For |phi_0| <= 1: -1 <= phi(x,t) <= 1 for all x, t.

**Structural role:** The strongest a priori estimate in the AC architecture. Provides L^{infinity} control without energy estimates, Sobolev embedding, or bootstrapping. This is the key advantage of second-order over fourth-order parabolic equations.

---

**U3. H^1 Control from Free Energy**

    ||nabla phi(t)||_{L^2}^2 <= 2 F[phi_0] / epsilon^2    for all t >= 0

**Structural role:** Uniform-in-time gradient control. Combined with U2, gives uniform H^1 bounds.

---

**U4. Interface Width Lower Bound**

    (Interface width) >= C epsilon

No structure finer than O(epsilon) persists. The equilibrium tanh profile saturates this bound.

**Structural role:** Sets the architectural resolution scale.

---

**U5. Mean-Curvature Motion Law**

    V_n = M sigma kappa + O(epsilon)    as epsilon → 0

Interface velocity is proportional to mean curvature. Closed interfaces shrink and vanish.

**Structural role:** Governs the extremal (large-scale) interface dynamics. Determines extinction times.

---

**U6. Exponential Bulk Relaxation**

    |phi(x,t) - phi_*| <= C exp(-lambda t)    in bulk regions, lambda = M f''(phi_*) = 2M

The approach to the well values ±1 is exponential in bulk regions, with rate independent of epsilon.

**Structural role:** Separates time scales — bulk relaxation (fast, rate 2M) is decoupled from interface motion (slow, rate ~ M epsilon / L).

---

**U7. No Blowup Channel**

    phi(t) in C^{infinity}(Omega)    for all t > 0,    d = 1, 2, 3

Unconditional global regularity. No conditional hypothesis, no dimensional restriction (within d <= 3).

**Structural role:** Seals the envelope. The AC architecture is unconditionally self-consistent.

---

### Universal Inequality Summary

| Label | Inequality                          | Type            | Status        | Role                        |
|-------|--------------------------------------|-----------------|---------------|-----------------------------|
| U1    | Free-energy dissipation identity     | Exact equality  | Unconditional | Primary accounting          |
| U2    | Maximum principle                    | Sharp bound     | Unconditional | L^{infinity} control        |
| U3    | H^1 control from energy             | Inequality      | Unconditional | Gradient control            |
| U4    | Interface width >= O(epsilon)        | Lower bound     | Unconditional | Resolution scale            |
| U5    | Mean-curvature motion                | Asymptotic law  | epsilon → 0   | Interface dynamics          |
| U6    | Exponential bulk relaxation          | Decay estimate  | Unconditional | Time-scale separation       |
| U7    | No blowup                           | Regularity      | Unconditional | Envelope closure            |

**All seven inequalities are unconditional.** No dimensional restrictions, no conditional hypotheses, no open faces.

---

## 5. Attractors and Long-Time Behavior

### 5.1 Global Attractor

The AC equation on a bounded domain with Neumann boundary conditions possesses a *global attractor* A: a compact, connected, finite-dimensional invariant set in H^1(Omega) that attracts all trajectories.

**Existence:** The absorbing ball (from the energy bound and the maximum principle) and the compactness of the solution operator (parabolic smoothing maps H^1 to H^2, and H^2 hookrightarrow H^1 is compact on bounded domains) provide the ingredients for the standard Ladyzhenskaya–Temam attractor existence theorem.

**Structure:** The attractor contains:
- The two uniform equilibria phi = +1 and phi = -1.
- All non-trivial stationary solutions (if any exist for the given domain).
- All heteroclinic connections between equilibria.
- The unstable manifolds of unstable/saddle equilibria.

**Dimension:** The attractor dimension is bounded by C(epsilon, M, |Omega|, d). As epsilon → 0, the attractor dimension grows — reflecting the increasing number of metastable interface configurations.

### 5.2 Equilibrium States

The stationary solutions of AC satisfy:

    mu = f'(phi) - epsilon^2 Delta phi = 0    on Omega
    nabla phi . n = 0    on partial Omega

This is the Euler–Lagrange equation for the free energy F, *without* a Lagrange multiplier for mass conservation (contrast with CH, where the stationary condition is mu = const, not mu = 0).

**Stable equilibria:**
- phi = +1 (uniform, corresponding to the global minimum of F on the component with positive average phi — but only for appropriate domains).
- phi = -1 (uniform, global minimum on the negative-average component).

**Unstable equilibria:**
- phi = 0 (uniform, saddle point of F — unstable to all perturbations).
- Non-trivial stationary solutions with interfaces: these exist for certain domain geometries (e.g., planar interfaces in rectangular domains, radial solutions in spherical domains) but are *unstable* — perturbations cause the interfaces to drift by mean curvature until they reach a boundary or annihilate.

**Generic long-time behavior:** For generic initial data on a bounded domain, the solution converges to one of the two uniform equilibria phi = ±1. The selection depends on the initial data: roughly, if the average of phi_0 is positive, the solution converges to phi = +1; if negative, to phi = -1. The convergence is through the sequence: bulk relaxation → interface formation → interface shrinkage → extinction → uniform state.

### 5.3 The Metastable Manifold

Before reaching the final uniform equilibrium, the AC dynamics spend extended time on *metastable manifolds* — the slow manifolds of configurations with well-separated interfaces.

**One-dimensional case:** On an interval [0, L] with Neumann boundary conditions, a configuration with N transition layers at positions x_1 < x_2 < ... < x_N forms an approximately invariant manifold M_N. The dynamics on M_N are governed by an ODE:

    dx_i/dt = C(epsilon) [exp(-(x_{i+1} - x_i) / epsilon) - exp(-(x_i - x_{i-1}) / epsilon)]

where C(epsilon) is a constant of order M/epsilon. Adjacent layers interact attractively and *annihilate in pairs*: the two closest layers merge and disappear, reducing N by 2. The annihilation time for layers separated by distance L is:

    T_annihilation ~ (epsilon / M) exp(C L / epsilon)

This is exponentially long in L/epsilon — the hallmark of metastability. The system spends most of its time near the metastable manifolds, with rapid transitions between them.

**Higher-dimensional case:** The metastable manifold is parameterized by the positions and shapes of the interfaces. The slow dynamics are given by mean-curvature flow (N3 from Mode 1), and the metastable lifetimes scale as R^2 / (M sigma) for droplets of radius R.

### 5.4 Extinction Dynamics

The terminal phase of AC dynamics is *extinction*: the last remaining interfaces shrink to zero size and vanish, leaving a uniform state.

**Extinction cascade:** In a configuration with multiple droplets of different sizes, the smallest droplet vanishes first (T* ~ R^2), then the next smallest, and so on. The extinction cascade proceeds from small to large, with each event reducing the number of droplets by one (or two, for layer annihilation in 1D).

**Extinction rate:** The total number of phase domains N(t) decreases stepwise, with each step separated by an interval of order R_min(t)^2 / (M sigma), where R_min(t) is the radius of the smallest remaining droplet. Since R_min increases as small droplets vanish, the intervals between extinction events grow longer over time. The dynamics decelerate as the configuration simplifies.

**Final convergence:** After the last interface vanishes, the solution is close to a uniform state phi ≈ ±1 with small perturbations. The final approach to exact uniformity is governed by the linearized dynamics (U6): exponential convergence at rate 2M (independent of the domain size).

### 5.5 Exponential Convergence to Equilibrium

Near a stable uniform equilibrium phi_* = ±1, the linearized AC operator is:

    L_* phi = M epsilon^2 Delta phi - M f''(phi_*) phi = M epsilon^2 Delta phi - 2M phi

This is a self-adjoint operator on L^2(Omega) (with Neumann boundary conditions) with eigenvalues:

    lambda_k = -M epsilon^2 mu_k - 2M

where mu_k >= 0 are the eigenvalues of -Delta on Omega. The largest eigenvalue is lambda_0 = -2M (corresponding to the constant eigenfunction), and all eigenvalues are strictly negative. The spectral gap is:

    gap = |lambda_0| = 2M

Solutions near phi_* converge at rate:

    ||phi(t) - phi_*||_{L^2} <= C exp(-2M t)

The final convergence is *fast* (rate 2M, independent of epsilon and |Omega|) — much faster than the slow metastable dynamics that precede it.

---

## 6. Comparison with CH Mode 2

### 6.1 Interface Fate

**AC:** Interfaces *shrink and vanish*. Mean curvature flow drives every closed interface inward until it collapses to a point in finite time. The total interface area is strictly decreasing. The long-time state is uniform (phi = ±1).

**CH:** Interfaces *merge and coarsen*. Mass conservation prevents interfaces from vanishing (the enclosed phase must go somewhere). Instead, smaller domains transfer material to larger domains through bulk diffusion (Ostwald ripening), and the characteristic domain size grows as t^{1/3} or t^{1/4}. The long-time state is a small number of large domains (or a single domain filling half the volume, depending on the mass constraint).

This is the most consequential dynamical difference between AC and CH: extinction vs. coarsening. It is a direct consequence of the conservation axiom (CH-3 present, AC-3 absent).

### 6.2 Maximum Principle

**AC:** Satisfies the maximum principle. |phi(t)| <= max(|phi_0|, 1). The invariant set [-1, 1] is preserved. L^{infinity} control is *free*.

**CH:** Does *not* satisfy the maximum principle. Fourth-order parabolic equations permit overshoot. L^{infinity} control requires H^2 estimates + Sobolev embedding — it is *earned*, not given.

The maximum principle is the structural gift of second-order parabolic character. AC receives it; CH, being fourth-order, does not.

### 6.3 Gradient-Flow Metric

**AC:** L^2 gradient flow. Dissipation rate = M ||mu||^2. Equilibrium: mu = 0 (pointwise).

**CH:** H^{-1} gradient flow. Dissipation rate = M ||nabla mu||^2. Equilibrium: mu = const (spatially uniform).

The L^2 metric makes large-scale rearrangements cheap — moving phi from 0 to 1 across a large domain costs O(volume) regardless of scale. The H^{-1} metric makes large-scale rearrangements expensive — cost O(volume x L^2). This is why AC relaxes at rate t ~ L^2 while CH coarsens at rate t ~ L^4.

### 6.4 Time-Scale Separation

**AC:** Two time scales.
- Fast: bulk relaxation (rate 2M, independent of spatial scale).
- Slow: interface motion by mean curvature (rate ~ M epsilon / L).

**CH:** Three time scales.
- Fast: interface profile relaxation (rate ~ M/epsilon^2).
- Intermediate: coarsening (rate ~ M epsilon / L^3 for constant mobility).
- Slow: metastable transitions (rate ~ exp(-CL/epsilon)).

CH has a richer time-scale hierarchy because the conservation constraint forces the dynamics through an additional stage (coarsening) that AC skips entirely.

### 6.5 Attractor Structure

**AC:** Global attractor exists unconditionally. Generic trajectories converge to uniform equilibria phi = ±1. Non-trivial stationary solutions (with interfaces) are generically unstable.

**CH:** Global attractor exists unconditionally. Generic trajectories converge to phase-separated equilibria (two domains with phi = ±1 separated by interfaces of constant mean curvature). The equilibrium states have nontrivial structure because mass conservation constrains the final volume fractions.

### 6.6 Summary Table

| Feature                    | Allen–Cahn                  | Cahn–Hilliard               |
|----------------------------|-----------------------------|------------------------------|
| Interface fate             | Shrink and vanish           | Merge and coarsen            |
| Maximum principle          | Yes                         | No                           |
| Gradient-flow metric       | L^2                         | H^{-1}                      |
| Dissipation rate           | M \|\|mu\|\|^2             | M \|\|nabla mu\|\|^2        |
| Equilibrium                | mu = 0 (uniform states)    | mu = const (phase coexistence)|
| Coarsening                 | None                        | L ~ t^{1/3} or t^{1/4}      |
| Time scales                | 2 (bulk + interface)       | 3 (interface + coarsen + meta)|
| Long-time state            | Uniform phi = ±1           | Phase-separated domains      |
| Blowup channel             | None                        | None                         |
| Lyapunov structure         | Exact identity              | Exact identity               |
| Locality                   | Fully local                 | Fully local                  |
| Envelope closure           | All d <= 3                  | All d <= 3                   |

---

*End of Mode 2: PDE → Extremal Dynamics. Mode 3 (Channels → Constraint Surface) will follow in a subsequent file.*
