# AD Evaluation: Cahn–Hilliard Equation — Mode 1: Axiom → Envelope

Allen Proxmire

April 2026

---

## Overview

Mode 1 traces the path from the Cahn–Hilliard axioms (CH-1 through CH-8) to the architectural envelope — the maximal set of constraints that the architecture imposes on all admissible states and evolutions. For CH, this envelope is qualitatively different from the Navier–Stokes envelope: it is *closed* in every dimension, with no open face and no regularity gap. The gradient-flow structure (CH-4) provides a Lyapunov functional that the NS architecture lacks, and the fourth-order parabolic character provides smoothing that exceeds what the NS second-order viscous channel can achieve.

Throughout, we work with the Cahn–Hilliard equation on a bounded domain Omega subset R^d (d = 1, 2, 3) with constant mobility M > 0:

    partial_t phi = M Delta mu,    mu = phi^3 - phi - epsilon^2 Delta phi
    nabla phi . n = nabla mu . n = 0  on partial Omega
    phi(x, 0) = phi_0(x)

The free energy is F[phi] = integral [f(phi) + (epsilon^2/2)|nabla phi|^2] dx with f(phi) = (1/4)(phi^2 - 1)^2.

---

## 1. Forbidden Configurations

A forbidden configuration is a state, operator, or evolution that is axiomatically excluded by the CH architecture.

### F1. Non-Conserved Order Parameter Evolution

**Axiom source:** CH-3 (Conservation).

Any evolution for which d/dt integral phi dx ≠ 0 is forbidden. The total order parameter is exactly conserved. The architecture cannot create, destroy, or leak phi — it can only redistribute it spatially through a divergence-form flux. In particular:

- Source/sink terms (partial_t phi = ... + g(phi)) that do not integrate to zero are forbidden.
- Allen–Cahn dynamics (partial_t phi = -mu, without the conserving Laplacian) are forbidden — they relax phi locally without conserving mass.
- Boundary conditions that permit net flux through partial Omega (nabla mu . n ≠ 0 with nonzero integral) are forbidden under the standard architecture.

Conservation is the single most constraining axiom: it forces the dynamics into the narrow class of divergence-form evolutions.

### F2. Free-Energy Increasing Dynamics

**Axiom source:** CH-4 (Gradient-Flow Structure).

Any evolution along which the free energy F[phi(t)] increases is forbidden. The gradient-flow structure guarantees:

    dF/dt = -integral M |nabla mu|^2 dx <= 0

This is an *exact identity*, not an inequality derived from estimates. The free energy is a strict Lyapunov functional: it decreases along every non-stationary trajectory and is constant only at equilibrium (mu = const). There is no mechanism in the architecture for energy to increase — no forcing channel, no external input, no stochastic perturbation. The CH architecture is *autonomously dissipative*.

Consequences:
- Oscillatory dynamics are forbidden: the system cannot revisit a state with higher free energy.
- Limit cycles are forbidden: periodic orbits would require dF/dt = 0 at all times, which implies mu = const, which is a fixed point.
- Chaos (in the sense of sensitive dependence on initial conditions with recurrence) is forbidden for the same reason.

The CH architecture is a *monotone* system in the free-energy sense: every trajectory descends through the energy landscape toward a local minimum.

### F3. Chemical Potentials Not Derived from F

**Axiom source:** CH-6 (Chemical Potential Definition).

The chemical potential must be the variational derivative of the free energy:

    mu = delta F / delta phi = f'(phi) - epsilon^2 Delta phi

Any chemical potential that is not expressible in this form — for instance, a prescribed function mu(x, t) independent of phi, or a nonlocal functional of phi — is forbidden. The chemical potential is a *slave variable* with no independent degrees of freedom, entirely determined by phi and its local derivatives.

### F4. Interfaces Thinner Than O(epsilon)

**Axiom source:** CH-5 (Free-Energy Functional).

The gradient-penalty term (epsilon^2/2)|nabla phi|^2 in the free energy penalizes spatial gradients with a characteristic cost proportional to epsilon^2 / (interface width)^2. The balance between the double-well bulk energy and the gradient penalty sets the equilibrium interface width at O(epsilon). Interfaces thinner than O(epsilon) carry prohibitively large gradient energy and are dynamically unstable — the fourth-order diffusion channel smooths them to the equilibrium width.

The architecture has a *built-in minimum length scale*: epsilon. No structure finer than O(epsilon) can persist. This is in stark contrast to Navier–Stokes, where the minimum length scale (the Kolmogorov scale eta) depends on the flow state and is not set by any architectural parameter.

### F5. Nonlocal Coupling

**Axiom source:** CH-2 (Locality).

All channel interactions are local: the evolution of phi at x depends only on phi and its derivatives at x (up to fourth order). The following are forbidden:

- Integral operators on phi (convolution kernels, fractional Laplacians, nonlocal free energies of the form integral integral J(x-y) phi(x) phi(y) dx dy with non-delta-function kernels).
- Long-range interactions that couple phi at distant points without passing through local derivatives.
- Pressure-type nonlocal constraints (there is no incompressibility condition in CH, so no Poisson equation).

The CH architecture is *fully local* at both the formulation and solution levels — a stronger locality than NS achieves.

### F6. Non-Newtonian Mobility Coupling

**Axiom source:** CH-7 (Mobility).

The flux is **J** = -M nabla mu, with M a scalar (or at most tensor-valued) function of phi. The following are forbidden:

- History-dependent mobility: M depending on the time history of phi (viscoelastic or memory effects).
- Velocity-coupled mobility: M depending on an external flow field (this would require coupling to a momentum equation, extending beyond the CH architecture).
- Negative mobility: M < 0 at any point, which would reverse the gradient flow and produce energy-increasing dynamics (contradicting F2).

### F7. Anisotropic Gradient Penalty (Under Standard Axioms)

**Axiom source:** CH-5 + CH-8 (Free Energy + Euclidean Geometry).

The gradient penalty (epsilon^2/2)|nabla phi|^2 is isotropic — it penalizes gradients equally in all directions. Under the standard axioms, anisotropic gradient penalties of the form (1/2) epsilon_ij^2 (partial_i phi)(partial_j phi) with epsilon_ij ≠ epsilon delta_ij are forbidden. Anisotropic phase-field models exist (for crystal growth, etc.) but extend beyond the standard CH architecture.

### F8. Multi-Component or Vector Order Parameters

**Axiom source:** CH-3, CH-5, CH-6 (Conservation + Free Energy + Chemical Potential).

The architecture is built for a *scalar* order parameter phi. Vector-valued order parameters (phi_1, ..., phi_n) or multi-component systems (Cahn–Hilliard systems with multiple conserved fields) are outside the single-component CH architecture. Extensions to multi-component systems (multicomponent CH, Cahn–Hilliard–Cook) exist but require additional axioms.

### Summary of Forbidden Configurations

| Label | Forbidden Configuration                  | Excluding Axiom(s)    |
|-------|------------------------------------------|-----------------------|
| F1    | Non-conserved evolution                  | CH-3                  |
| F2    | Free-energy increase                     | CH-4                  |
| F3    | Non-variational chemical potential       | CH-6                  |
| F4    | Sub-epsilon interface structure          | CH-5                  |
| F5    | Nonlocal coupling                        | CH-2                  |
| F6    | Non-Newtonian / history-dependent mobility | CH-7                |
| F7    | Anisotropic gradient penalty             | CH-5, CH-8            |
| F8    | Multi-component order parameter          | CH-3, CH-5, CH-6      |

---

## 2. Necessary Configurations

A necessary configuration is a structure that every admissible CH system *must* exhibit.

### N1. Mass Conservation (Exact, Permanent)

**Source:** CH-3.

    integral_Omega phi(x, t) dx = integral_Omega phi_0(x) dx    for all t >= 0

The total order parameter is an exact invariant of the dynamics. This follows from the divergence form of the PDE and the no-flux boundary conditions:

    d/dt integral phi dx = integral partial_t phi dx = integral M Delta mu dx = M integral nabla mu . n dS = 0

Mass conservation is not a tendency or an approximation — it is an algebraic identity of the architecture.

### N2. Monotone Free-Energy Dissipation (Exact Identity)

**Source:** CH-4, CH-5, CH-6, CH-7.

    dF/dt = integral [f'(phi) partial_t phi + epsilon^2 nabla phi . nabla(partial_t phi)] dx

Integrating by parts and using mu = f'(phi) - epsilon^2 Delta phi:

    dF/dt = integral mu partial_t phi dx = integral mu M Delta mu dx = -M integral |nabla mu|^2 dx

Therefore:

    dF/dt = -M ||nabla mu||_{L^2}^2 <= 0                       ... (Dissipation Identity)

This is an *exact identity* for all solutions — not an inequality derived from estimates, but an algebraic consequence of the gradient-flow structure. The dissipation rate is M ||nabla mu||^2, which vanishes if and only if mu = const (thermodynamic equilibrium).

**Comparison with NS:** The NS energy identity dE/dt = -epsilon + P_f is also exact for smooth solutions, but NS has a forcing channel that can inject energy. CH has no forcing channel — the dissipation identity is one-sided and permanent. The CH Lyapunov structure is *stronger* than the NS energy structure.

### N3. Fourth-Order Parabolic Character

**Source:** CH-2, CH-4, CH-5, CH-6.

The combined equation partial_t phi = -M epsilon^2 Delta^2 phi + M Delta(phi^3 - phi) has its highest-order term as -M epsilon^2 Delta^2 phi, the *biharmonic* operator. This makes CH a fourth-order parabolic PDE. The fourth-order character is structurally necessary — it arises from the gradient penalty in F (which contributes a Laplacian to mu, and a second Laplacian from the divergence-form flux).

Consequences of fourth-order parabolic character:
- Stronger smoothing than second-order diffusion. The biharmonic operator smooths at rate k^4 in Fourier space (vs. k^2 for the Laplacian).
- The fundamental solution decays faster at high wavenumbers.
- The scaling is t ~ L^4 (not L^2), so dynamics are slower at large scales.
- *No maximum principle.* Fourth-order parabolic equations do not satisfy a maximum principle — phi can exceed its initial bounds. This is a structural property, not a defect.

### N4. Chemical Potential as Slave Variable

**Source:** CH-6.

    mu(x, t) = f'(phi(x, t)) - epsilon^2 Delta phi(x, t)

The chemical potential is uniquely determined at every point by the order parameter and its second spatial derivatives. It carries no independent degrees of freedom, has no separate evolution equation, and has no independent initial condition. This is analogous to the NS pressure being slaved to velocity, but with the crucial difference that the CH chemical potential is determined *locally* (no Poisson equation, no Green's function, no nonlocal coupling).

### N5. Spinodal Decomposition

**Source:** CH-3, CH-4, CH-5.

For initial data near the unstable state phi ≈ 0 (the hilltop of the double-well), linearization of the CH equation gives:

    partial_t phi ≈ M Delta [f''(0) phi - epsilon^2 Delta phi] = -M Delta [(1 - f''(0)) phi + epsilon^2 Delta phi]

For the standard double-well, f''(0) = -1 (the hilltop is concave), so:

    partial_t phi ≈ M Delta [-phi - epsilon^2 Delta phi] = -M [Delta phi + epsilon^2 Delta^2 phi]

In Fourier space, mode k grows at rate sigma(k) = M k^2 (1 - epsilon^2 k^2). Modes with k < 1/epsilon are *unstable* (sigma > 0); modes with k > 1/epsilon are *stable* (sigma < 0). The most unstable mode has wavenumber k_max = 1/(epsilon sqrt(2)) and growth rate sigma_max = M / (4 epsilon^2).

Spinodal decomposition — the spontaneous amplification of concentration fluctuations at intermediate wavelengths — is an *architecturally necessary* consequence of the axioms whenever the initial data lies in the spinodal region (f''(phi_0) < 0). The characteristic wavelength of the initial phase separation pattern is O(epsilon), set by the competition between the reaction channel (destabilizing at large scales) and the surface-tension channel (stabilizing at small scales).

### N6. Interface Formation

**Source:** CH-3, CH-4, CH-5.

After spinodal decomposition, the solution develops regions where phi ≈ +1 and phi ≈ -1, separated by *diffuse interfaces* of width O(epsilon). The equilibrium interface profile (in one dimension, for a planar interface centered at x = 0) is:

    phi_eq(x) = tanh(x / (epsilon sqrt(2)))

This profile is the unique (up to translation) minimizer of F subject to the boundary conditions phi → ±1 as x → ±infinity. The interface profile is *architecturally determined* — the axioms force its existence and its specific shape.

The interfacial energy per unit area (surface tension) is:

    sigma = integral_{-infty}^{infty} [f(phi_eq) + (epsilon^2/2)(phi_eq')^2] dx = (2 sqrt(2) / 3) epsilon

Surface tension is proportional to epsilon — another architecturally determined quantity.

### N7. Coarsening

**Source:** CH-3, CH-4, CH-5.

After interface formation, the system enters a *coarsening* regime: larger phase domains grow at the expense of smaller ones, driven by the reduction of total interfacial energy. Coarsening is architecturally necessary because:

- The free energy F is approximately proportional to the total interface area (for well-separated phases).
- The gradient-flow structure (N2) forces F to decrease monotonically.
- The only mechanism to decrease total interface area, given mass conservation (N1), is for smaller domains to shrink and disappear while larger domains grow.

Coarsening is a *topological* process: it changes the number and connectivity of phase domains. It is driven entirely by the thermodynamic preference for fewer, larger domains (lower surface-area-to-volume ratio) and is constrained by mass conservation.

### N8. Equilibrium States

**Source:** CH-4, CH-5.

Stationary solutions satisfy mu = const throughout Omega. For the standard double-well on a bounded domain, the equilibrium states include:

- **Homogeneous states:** phi = const, with mu = f'(phi). Stable if f''(phi) > 0 (phi near ±1); unstable if f''(phi) < 0 (phi near 0).
- **Phase-separated states:** Two domains with phi ≈ +1 and phi ≈ -1, separated by interfaces of width O(epsilon), with the volume fractions determined by mass conservation and the interface geometry determined by the condition of constant mean curvature (Gibbs–Thomson relation).

The equilibrium states are *architecturally determined* by the axioms. The number, location, and shape of equilibrium interfaces are determined by the variational principle delta F = 0 subject to the mass constraint.

### Summary of Necessary Configurations

| Label | Necessary Configuration              | Forcing Axiom(s)        |
|-------|--------------------------------------|-------------------------|
| N1    | Mass conservation                    | CH-3                    |
| N2    | Monotone free-energy dissipation     | CH-4, CH-5, CH-6, CH-7 |
| N3    | Fourth-order parabolic character     | CH-2, CH-4, CH-5, CH-6 |
| N4    | Chemical potential as slave variable | CH-6                    |
| N5    | Spinodal decomposition               | CH-3, CH-4, CH-5       |
| N6    | Interface formation (tanh profile)   | CH-3, CH-4, CH-5       |
| N7    | Coarsening                           | CH-3, CH-4, CH-5       |
| N8    | Equilibrium states (mu = const)      | CH-4, CH-5              |

---

## 3. Extremal Bounds

The extremal bounds sharpen the qualitative envelope into quantitative inequalities.

### E-Bound 1: Lyapunov Dissipation Identity

    dF/dt = -M ||nabla mu||_{L^2}^2                              ... (exact)

This is the *primary envelope identity* of the CH architecture. It is stronger than any inequality because it holds with equality for all solutions at all times. The dissipation rate is exactly M ||nabla mu||^2 — no more, no less.

**Integrated form:**

    F[phi(t)] + M integral_0^t ||nabla mu(s)||^2 ds = F[phi_0]

Total free energy at time t plus total energy dissipated over [0, t] equals initial free energy. There is no gap, no anomalous dissipation, no inequality. The CH energy accounting is *exact and closed*.

### E-Bound 2: Free-Energy Lower Bound

The free energy is bounded below:

    F[phi] >= -C |Omega|

for a constant C depending only on f and epsilon. For the standard double-well, f(phi) = (1/4)(phi^2 - 1)^2 >= 0, so the bulk energy contribution is non-negative, and:

    F[phi] >= 0    for all phi

Combined with the dissipation identity (E-Bound 1), this gives:

    M integral_0^{infinity} ||nabla mu(s)||^2 ds <= F[phi_0] < infinity

The total dissipation over all time is *finite* — the system has a finite "dissipation budget" set by the initial free energy. This forces the system to approach equilibrium: ||nabla mu(t)|| → 0 as t → infinity (along subsequences, and in a time-averaged sense).

### E-Bound 3: L^2 Bound on phi (Mass + Energy Control)

By mass conservation and the Poincare inequality, the mean value phi-bar = (1/|Omega|) integral phi dx is constant. The free energy controls the fluctuations:

    (epsilon^2 / 2) ||nabla phi||_{L^2}^2 <= F[phi] <= F[phi_0]

so:

    ||nabla phi(t)||_{L^2}^2 <= 2 F[phi_0] / epsilon^2    for all t >= 0

By the Poincare–Wirtinger inequality:

    ||phi(t) - phi-bar||_{L^2}^2 <= C_P ||nabla phi(t)||_{L^2}^2 <= 2 C_P F[phi_0] / epsilon^2

Therefore:

    ||phi(t)||_{L^2}^2 <= |phi-bar|^2 |Omega| + 2 C_P F[phi_0] / epsilon^2

The L^2 norm of phi is *uniformly bounded for all time*, with a bound depending only on the initial data, epsilon, and the domain. This is an unconditional a priori estimate — it holds in every dimension.

### E-Bound 4: H^2 Bound (Uniform-in-Time Regularity)

The fourth-order structure provides higher regularity. Testing the PDE against -Delta phi and using the dissipation structure, one obtains (on bounded domains with appropriate boundary conditions):

    ||phi(t)||_{H^2}^2 <= C(F[phi_0], epsilon, M, Omega)    for all t >= delta > 0

where delta > 0 is an arbitrarily small waiting time (instantaneous regularization from the biharmonic term). The H^2 norm is *uniformly bounded* for all positive times, regardless of initial regularity.

**Comparison with NS:** In NS, the analogous H^1 bound (controlling nabla **u**) is available only in 2D (via enstrophy closure). In CH, the H^2 bound is available in *every* dimension (1D, 2D, 3D). This is the structural consequence of fourth-order vs. second-order parabolic character.

### E-Bound 5: Global Regularity (All Dimensions)

The a priori bounds (E-Bounds 3 and 4) are sufficient to prove:

**Theorem (Global Regularity).** For any phi_0 in H^1(Omega) (or even L^2(Omega)), the Cahn–Hilliard equation with constant positive mobility has a unique global smooth solution phi in C^{infinity}(Omega x (0, infinity)) for all d = 1, 2, 3.

The proof follows a standard bootstrap: the energy bound gives H^1 control; the fourth-order smoothing of the biharmonic term gives H^2 control; the nonlinearity phi^3 is subcritical relative to H^2 in dimensions d <= 3; and the bootstrap closes without a gap.

**There is no regularity problem for Cahn–Hilliard.** The fourth-order diffusion channel is strong enough to control the cubic nonlinearity in all physically relevant dimensions. The CH envelope is *closed* — it has no open face.

### E-Bound 6: Maximum Principle Failure

Fourth-order parabolic equations do not satisfy the maximum principle. The order parameter phi can exceed the well values ±1:

    sup_{x, t} |phi(x, t)| is NOT bounded by sup_x |phi_0(x)| in general
    sup_{x, t} phi(x, t) > 1 is possible even if phi_0 <= 1

This is a *structural feature* of the fourth-order architecture, not a pathology. The double-well drives phi toward ±1, but the biharmonic diffusion can overshoot. The overshoot is bounded: the energy bound ensures that the L^infinity norm of phi remains finite, even if it exceeds the equilibrium values.

**Logarithmic potential variant:** If f(phi) is replaced by a logarithmic potential (Flory–Huggins: f(phi) = (1/2)[(1+phi)log(1+phi) + (1-phi)log(1-phi)] - theta phi^2 / 2), then |phi| < 1 is enforced by the singularity of f at phi = ±1. This maximum principle is a consequence of the *potential*, not the PDE structure.

### E-Bound 7: Coarsening Rate Bounds

During the coarsening regime (after initial spinodal decomposition), the characteristic domain size L(t) grows in time. The coarsening rate depends on the dominant coarsening mechanism:

**Diffusion-limited coarsening (Lifshitz–Slyozov–Wagner, constant mobility):**

    L(t) ~ t^{1/3}    as t → infinity

This scaling arises from the balance between the driving force (curvature-driven chemical potential gradients, which scale as 1/L^2) and the diffusive flux (which introduces a factor of L in the flux timescale), giving dL/dt ~ 1/L^2, hence L^3 ~ t.

**Surface-diffusion-limited coarsening (degenerate mobility M = 1 - phi^2):**

    L(t) ~ t^{1/4}    as t → infinity

This slower scaling arises because the degenerate mobility restricts diffusion to the interfacial region, introducing an additional factor of epsilon/L in the effective flux.

These coarsening rates are *not rigorous theorems* for the CH PDE — they are scaling predictions supported by formal asymptotics, matched asymptotic expansions, and extensive numerical evidence. Rigorous upper bounds on the coarsening rate have been established:

    F[phi(t)] >= C t^{-1/3}    (Kohn–Otto, for constant mobility)
    F[phi(t)] >= C t^{-1/4}    (for degenerate mobility)

These bounds confirm that coarsening cannot be *faster* than the predicted rates but do not prove that it is exactly at those rates for generic initial data.

### E-Bound 8: Interfacial Energy Scaling

For solutions in the coarsening regime with well-separated phases (phi ≈ ±1 away from interfaces of width O(epsilon)):

    F[phi(t)] ≈ sigma * (total interface area at time t)

where sigma = (2 sqrt(2)/3) epsilon is the surface tension. The coarsening bound (E-Bound 7) then translates into a bound on the decay of total interface area:

    (Total interface area)(t) >= C / (sigma t^{1/3})

The interface area decreases, but not faster than t^{-1/3}. This is an *architectural bound* on the rate of topological simplification.

### E-Bound 9: Spectral Gap and Exponential Approach to Equilibrium

Near a non-degenerate local minimum phi_* of F (subject to mass conservation), the linearized CH operator has a spectral gap lambda_1 > 0. Solutions sufficiently close to phi_* converge exponentially:

    ||phi(t) - phi_*||_{H^1} <= C exp(-lambda_1 t / 2)

The spectral gap is architecturally determined by the curvature of F at phi_* and the domain geometry. Near equilibrium, the system behaves like a linear gradient flow with exponential decay — all transients die out at rate lambda_1.

---

## 4. Structural Invariants

### I1. Mass Conservation

    integral_Omega phi(x, t) dx = integral_Omega phi_0(x) dx    for all t >= 0

The total order parameter is exactly conserved. This is the most fundamental structural invariant.

### I2. Free-Energy Monotonicity

    F[phi(t_2)] <= F[phi(t_1)]    for all t_2 >= t_1 >= 0

The free energy is monotone non-increasing. This is an *exact* invariant (not a statistical or approximate statement).

### I3. Dissipation Budget

    M integral_0^{infinity} ||nabla mu(s)||^2 ds = F[phi_0] - F[phi_*] <= F[phi_0]

The total dissipation over the infinite time horizon is bounded by the initial free energy (minus the equilibrium energy). The system has a finite dissipation budget.

### I4. Interface Width Scaling

In the sharp-interface limit epsilon → 0, the equilibrium interface profile has width O(epsilon) and the surface tension is sigma = O(epsilon). These scaling relations are exact consequences of the free-energy functional (CH-5) and hold for all admissible equilibrium configurations.

### I5. Absence of Finite-Time Blowup

The global regularity theorem (E-Bound 5) is itself a structural invariant: for all admissible initial data, the solution exists globally in time and remains smooth. There are no finite-time singularities in the CH architecture, in any spatial dimension d = 1, 2, 3.

### I6. Equilibrium Characterization

Every omega-limit set of the dynamics is contained in the set of stationary solutions:

    { phi : mu = delta F / delta phi = const on Omega }

The dynamics converge (along subsequences) to states of uniform chemical potential. This is a structural invariant of the gradient-flow architecture.

### I7. Scaling Symmetry (Partial)

The CH equation with constant mobility has the scaling:

    phi_lambda(x, t) = phi(lambda x, lambda^4 t),   epsilon → lambda^{-1} epsilon

Under this scaling, the free energy transforms as F → lambda^{d-1} F and the surface tension as sigma → lambda^{-1} sigma. The scaling symmetry is *partial* — it requires simultaneous rescaling of epsilon, unlike the NS scaling which is exact for fixed nu.

---

## 5. Minimal Inequality Set (The CH Envelope)

The CH architectural envelope is defined by the following irreducible constraints, labeled E1–E9.

---

**E1. Mass Conservation (Exact Equality)**

    integral_Omega phi(x, t) dx = integral_Omega phi_0(x) dx    for all t >= 0

Hard constraint. Defines the admissible state space for given initial data.

---

**E2. Free-Energy Dissipation Identity (Exact Equality)**

    dF/dt = -M ||nabla mu||_{L^2}^2

Not an inequality — an exact identity. F is a strict Lyapunov functional. This is the strongest envelope constraint: it completely determines the energy budget with no gap.

---

**E3. Free-Energy Lower Bound**

    F[phi(t)] >= 0    for all t >= 0    [standard double-well]

Combined with E2, this ensures finite total dissipation:

    M integral_0^{infinity} ||nabla mu||^2 ds <= F[phi_0]

---

**E4. Gradient Bound (H^1 Control)**

    ||nabla phi(t)||_{L^2}^2 <= 2 F[phi_0] / epsilon^2    for all t >= 0

The free energy controls the H^1 seminorm of phi uniformly in time. This is an unconditional a priori estimate.

---

**E5. Global Regularity (All Dimensions)**

    phi(t) in C^{infinity}(Omega)    for all t > 0,    d = 1, 2, 3

The CH envelope is *closed in every dimension*. There is no regularity gap, no blowup channel, and no open face. The fourth-order biharmonic smoothing controls the cubic nonlinearity in all physically relevant dimensions.

---

**E6. Maximum Principle Failure**

    sup_{x,t} |phi(x,t)| is NOT bounded by max(|phi_0|, 1) in general

The fourth-order character permits overshoot beyond the well values ±1. The overshoot is bounded (by the energy bound) but not prevented.

---

**E7. Coarsening Rate Upper Bound**

    F[phi(t)] >= C t^{-alpha}    as t → infinity

with alpha = 1/3 for constant mobility and alpha = 1/4 for degenerate mobility. Coarsening cannot be faster than these rates.

---

**E8. Spinodal Instability Band**

    Modes with 0 < |k| < 1/epsilon are linearly unstable near phi = 0
    Modes with |k| > 1/epsilon are linearly stable
    Most unstable mode: |k_max| = 1/(epsilon sqrt(2))

The spinodal band is architecturally determined by epsilon. The architecture generates its own instability — the double-well drives phase separation at a wavelength set by the gradient penalty.

---

**E9. Exponential Convergence Near Equilibrium**

    ||phi(t) - phi_*||_{H^1} <= C exp(-lambda_1 t / 2)    near non-degenerate equilibria

The spectral gap lambda_1 > 0 of the linearized operator at a local minimum of F determines the rate of final approach to equilibrium.

---

### Envelope Summary

The CH architectural envelope is defined by nine constraints (E1–E9) organized into three tiers:

**Tier 1 — Hard Constraints (exact identities, always hold):**
- E1: Mass conservation (exact equality).
- E2: Free-energy dissipation identity (exact, Lyapunov).
- E3: Free-energy lower bound (non-negative).
- E4: Gradient bound (H^1 control from energy).

**Tier 2 — Global Structure (unconditional, all dimensions):**
- E5: Global regularity (smooth for all t > 0, d = 1, 2, 3). **Closed envelope — no open face.**
- E6: Maximum principle failure (structural feature of fourth-order PDEs).
- E8: Spinodal instability band (architecturally determined by epsilon).

**Tier 3 — Asymptotic Behavior:**
- E7: Coarsening rate bound (algebraic decay of free energy).
- E9: Exponential convergence near equilibrium.

**The defining architectural feature of the CH envelope, in contrast to NS, is its complete closure.** The NS envelope has an open face in 3D (the enstrophy gap, E4 in the NS evaluation). The CH envelope is closed in *every* dimension: the fourth-order smoothing, combined with the Lyapunov structure, controls the nonlinearity unconditionally. There is no CH regularity problem, no Millennium-type question, and no architectural self-consistency gap.

The CH architecture achieves what the NS architecture achieves only in 2D: a fully closed envelope with unconditional regularity, a finite-dimensional attractor, and guaranteed convergence to equilibrium. The structural mechanism is different — NS uses enstrophy closure (absence of vortex stretching); CH uses fourth-order smoothing and the Lyapunov functional — but the architectural outcome is the same: complete self-consistency.

---

*End of Mode 1: Axiom → Envelope. Mode 2 (PDE → Extremal Dynamics) will follow in a subsequent file.*
