# AD Evaluation: Reaction–Diffusion Systems — Mode 2: PDE → Extremal Dynamics

Allen Proxmire

April 2026

---

## Overview

Mode 2 moves from the static envelope to the dynamics. The RD Mode 2 analysis is qualitatively different from any previous evaluation: where AC has a single dynamical pathway (relaxation → extinction → equilibrium) and CH has a single pathway (spinodal → coarsening → equilibrium), the RD class contains an *entire zoo* of dynamical behaviors — fronts, pulses, spirals, Turing patterns, chaos — with no single pathway dominating. The RD architecture is the universal class for spatially extended nonlinear dynamics, and its Mode 2 analysis is correspondingly the richest in the PDE Atlas.

Throughout:

    partial_t **u** = **D** Delta **u** + **R**(**u**)

on Omega subset R^d (d = 1, 2, 3), with **u** in R^n, **D** positive definite, **R** smooth.

---

## 1. Diffusion–Reaction Competition

### 1.1 The Two Fundamental Time Scales

Every RD system is governed by the competition between two processes operating at characteristic rates:

**Diffusion time scale:** The time for diffusion to homogenize a perturbation of spatial scale L:

    t_D = L^2 / D

where D is the diffusion coefficient (or the smallest eigenvalue of **D** for systems). Diffusion is *slower* at large scales and *faster* at small scales — it takes time proportional to L^2.

**Reaction time scale:** The time for the local reaction kinetics to produce significant change:

    t_R = 1 / ||**R**'(**u**_0)||

where ||**R**'|| is the spectral radius of the Jacobian of **R** at the operating point **u**_0. The reaction rate is *scale-independent* — it operates at the same rate regardless of the spatial wavelength.

The ratio of these time scales — the *Damkohler number*:

    Da = t_D / t_R = L^2 ||**R**'|| / D

determines which channel dominates at each spatial scale.

### 1.2 Three Dynamical Regimes

**Regime I: Diffusion-Dominated (Da << 1, small L or large D)**

At scales L << L_RD = sqrt(D / ||**R**'||), diffusion overwhelms reaction:

    partial_t **u** ≈ **D** Delta **u**

The dynamics are approximately the heat equation. Solutions are smooth, exponentially decaying toward spatial uniformity. No pattern formation, no oscillation, no structure. The diffusion channel enforces spatial homogeneity.

**Regime II: Reaction-Dominated (Da >> 1, large L or small D)**

At scales L >> L_RD, reaction overwhelms diffusion:

    partial_t **u** ≈ **R**(**u**)

The dynamics are approximately the ODE system at each point independently. Spatial structure is frozen — each point evolves according to its local reaction kinetics. The qualitative behavior (fixed points, limit cycles, chaos) is determined by the ODE phase portrait.

**Regime III: Mixed Regime (Da ~ 1, L ~ L_RD)**

At the characteristic scale L_RD, diffusion and reaction are commensurate. This is the *pattern formation window* — the range of scales where the two channels interact nontrivially, producing:

- Interfaces and fronts (AC-type behavior at the level of individual interfaces).
- Turing patterns (stationary spatial structures selected by the instability band).
- Traveling waves (propagating structures with speed set by the reaction-diffusion balance).
- Spiral waves (rotating patterns at the intersection of reaction oscillation and spatial diffusion).

The mixed regime is the *architecturally rich* regime: all interesting RD dynamics occur at scales where Da ~ 1.

### 1.3 No Single Universal Scaling Law

AC has a single scaling: interface motion by mean curvature, with speed V ~ epsilon / L. CH has a single coarsening law: L(t) ~ t^{1/3} or t^{1/4}. RD has *no single universal scaling law* because:

- Different constitutive choices (RD-8) produce different dynamics (fronts, patterns, waves, chaos).
- The characteristic scale L_RD itself depends on the constitutive parameters.
- The long-time behavior depends on the ODE phase portrait (fixed point, limit cycle, chaos), which varies across the class.
- Multiple time scales (fast reaction, slow diffusion, or vice versa) can coexist, producing multi-scale dynamics with no single power law.

The absence of a universal scaling law is the architectural signature of the RD class's breadth: it contains too many qualitatively different sub-architectures to be characterized by a single exponent.

---

## 2. Extremal Behaviors

### E1. Turing Instability (Multi-Species, n >= 2)

**Regime:** Mixed regime, n >= 2, differential diffusion (D_v >> D_u).

A homogeneous steady state **u**_0 that is *stable* for the ODE (d**u**/dt = **R**(**u**)) becomes *unstable* for the PDE when the diffusion of the inhibitor is sufficiently faster than the diffusion of the activator. The instability produces stationary periodic patterns (spots, stripes, labyrinths) with wavelength set by the most unstable mode:

    lambda_Turing ~ 2 pi L_RD = 2 pi sqrt(D_u / ||**R**'||)

The Turing instability is the RD architecture's *signature pattern-forming mechanism*. It requires:
- At least two species (n >= 2).
- Differential diffusion (D_v / D_u > threshold).
- Activator-inhibitor reaction topology (J_{11} > 0, J_{22} < 0).

It is absent in scalar RD (n = 1) and in equal-diffusion systems (D_u = D_v). The Turing instability is the *extremal pattern* of the RD class: the most spatially organized structure that the architecture can produce autonomously.

### E2. Traveling Fronts (Bistable or Monostable Kinetics)

**Regime:** Scalar or multi-species, bistable or monostable reaction.

**Bistable fronts:** For scalar RD with three zeros of R (two stable, one unstable), there exists a unique traveling front **u**(x, t) = phi(x - c*t) connecting the two stable states, with uniquely selected speed:

    c* = integral_{u_-}^{u_+} R(u) du / integral (phi')^2 dz

The front is a *heteroclinic connection* in the traveling-wave ODE. Its speed is determined by the energetic asymmetry between the two wells.

**Monostable (Fisher–KPP) fronts:** For R(0) = 0, R'(0) > 0, R(1) = 0, R(u) > 0 on (0,1), fronts exist for all speeds c >= c_min with:

    c_min = 2 sqrt(D R'(0))

The minimum-speed front is *pulled* — its speed is determined by the linearized dynamics at the leading edge. Steeper fronts (c > c_min) exist but are typically not selected by generic initial data.

**Extremal speed:** The Fisher–KPP minimum speed c_min = 2 sqrt(D R'(0)) is the *extremal propagation rate* for monostable RD: no invasion can proceed faster than this without super-linear diffusion or anomalous kinetics.

### E3. Pulses and Excitability (FitzHugh–Nagumo Type)

**Regime:** Two-species, excitable kinetics, time-scale separation.

In excitable RD systems (e.g., FitzHugh–Nagumo: partial_t u = D_u Delta u + u - u^3 - v, partial_t v = epsilon(u - gamma v)), a localized super-threshold perturbation triggers a *traveling pulse*: a localized excitation that propagates through the medium at constant speed, leaving a refractory region behind it.

**Pulse structure:**
- Leading front: rapid excitation (u jumps from rest to excited state).
- Plateau: excited state maintained by the slow variable v.
- Trailing front: recovery (u returns to rest as v catches up).
- Refractory tail: the medium is temporarily unresponsive to further stimulation.

**Extremal pulse speed:** The pulse speed is determined by the fast-variable diffusion and the excitation threshold:

    c_pulse ~ 2 sqrt(D_u / t_fast) ~ sqrt(D_u ||R'_fast||)

The pulse speed is comparable to the Fisher–KPP speed for the fast variable alone. The slow variable v modulates the pulse shape but not its leading-order speed.

**Extremal excitability:** The threshold perturbation delta_* separating sub-threshold (return to rest) from super-threshold (pulse firing) is determined by the nullcline geometry and the time-scale separation epsilon. As epsilon → 0, delta_* becomes sharp — the excitable system approaches a *threshold automaton*.

### E4. Spiral Waves (Oscillatory Kinetics, d >= 2)

**Regime:** Two-species, oscillatory or excitable kinetics, d = 2 or 3.

In two-dimensional excitable or oscillatory media, broken wave fronts curl into *spiral waves* — rotating patterns that persist indefinitely and organize the spatiotemporal dynamics of the entire domain.

**Spiral structure:**
- A spiral tip (phase singularity) around which the wave rotates.
- Curved wave fronts emanating from the tip, forming an Archimedean spiral.
- The rotation period T_spiral and wavelength lambda_spiral are determined by the reaction kinetics and diffusion.

**Spiral selection:** The spiral frequency omega_spiral is *intrinsically selected* by the medium — it depends on the reaction kinetics and diffusion coefficients but not on the domain size or boundary conditions (for sufficiently large domains). The spiral is a *self-organized* rotating pattern.

**Three-dimensional spirals:** In d = 3, the spiral tip becomes a *filament* — a one-dimensional curve around which the scroll wave rotates. Filaments can be straight, curved, knotted, or linked, and their dynamics are governed by a curvature-driven evolution law.

### E5. Spatiotemporal Chaos (Multi-Species, Oscillatory)

**Regime:** Multi-species, oscillatory kinetics, large domain.

When spiral waves become unstable (through spiral breakup, Doppler instability, or meander instability), the spatiotemporal dynamics become *chaotic*: irregular, aperiodic patterns with sensitive dependence on initial conditions.

**Mechanisms of spatiotemporal chaos:**
- **Spiral breakup:** A single spiral becomes unstable and fragments into multiple spirals, which themselves break up, producing a turbulent sea of spiral fragments.
- **Defect-mediated turbulence:** Spiral tips (topological defects) are created and annihilated in pairs, with the defect density fluctuating chaotically.
- **Phase turbulence:** For weakly nonlinear oscillations, the phase of the oscillation becomes spatiotemporally chaotic (described by the Kuramoto–Sivashinsky equation in appropriate limits).

Spatiotemporal chaos is the *extremal complexity* of the RD architecture: the most dynamically complex behavior that the PDE can produce. It requires:
- At least two species (n >= 2) with oscillatory kinetics.
- Sufficiently large domain (L >> L_RD).
- Sufficiently strong nonlinearity (beyond the weakly nonlinear regime).

### E6. Wave–Pattern Interactions

**Regime:** Multi-species, mixed Turing-Hopf dynamics.

When the RD kinetics are near the intersection of a Turing bifurcation and a Hopf bifurcation, the system can exhibit *mixed-mode dynamics*:

- **Oscillating Turing patterns:** Stationary spatial patterns whose amplitude oscillates in time.
- **Traveling Turing patterns:** Spatial patterns that drift through the domain.
- **Turing-Hopf competition:** Alternation between patterned and oscillatory states.

These mixed-mode dynamics are the extremal *multi-instability* behaviors of the RD architecture: they occur where two distinct instability mechanisms (spatial patterning and temporal oscillation) compete for dominance.

### E7. Finite-Speed Propagation (Nonlinear/Degenerate Diffusion)

**Regime:** Scalar, degenerate diffusion D(u) = m u^{m-1} (porous medium).

For degenerate diffusion (D(u) → 0 as u → 0), perturbations propagate at *finite speed*: there exists a sharp front separating the region where u > 0 from the region where u = 0. The front speed is determined by the diffusion exponent m and the reaction kinetics.

This contrasts with linear diffusion, where perturbations propagate at infinite speed (though with exponentially small amplitude). Finite-speed propagation is a constitutive specialization (degenerate diffusion) within the RD class.

### E8. Possible Blowup for Super-Linear Kinetics

**Regime:** Scalar, R(u) = u^p with p > 1.

For the equation partial_t u = D Delta u + u^p on R^d:

- **p <= 1 + 2/d (Fujita exponent):** *All* positive solutions blow up in finite time. No global solution exists.
- **p > 1 + 2/d:** *Small* solutions exist globally; *large* solutions blow up.
- **Blowup rate:** ||u(t)||_{L^infinity} ~ (T* - t)^{-1/(p-1)} as t → T*.
- **Blowup set:** The set of points where u → infinity. Can be a single point, a finite set, or the entire domain, depending on the initial data and the spatial dimension.

Blowup is the *extremal destabilization* of the RD architecture: the most dramatic failure of regularity permitted by the axioms. It occurs when the reaction channel overwhelms the diffusion channel at all scales simultaneously — the reaction grows super-linearly, producing more of itself faster than diffusion can spread it.

---

## 3. Universal Inequalities

---

**U1. Parabolic Smoothing Inequality**

For the linear part **D** Delta **u**:

    ||nabla^k **u**(t)||_{L^2} <= C_k t^{-k/2} ||**u**_0||_{L^2}    for t > 0,  k >= 0

Instantaneous regularization: L^2 data becomes C^{infinity} for t > 0. The smoothing rate is t^{-k/2} — second-order, weaker than CH's fourth-order smoothing but architecturally present in all RD systems.

**Structural role:** Ensures that the diffusion channel provides a minimum level of regularity. At sufficiently small scales, diffusion always dominates reaction.

---

**U2. Reaction–Diffusion Balance Inequality**

    L_RD = sqrt(D_min / ||**R**'||_max)

The characteristic length scale separating diffusion-dominated (L < L_RD) from reaction-dominated (L > L_RD) dynamics. All RD pattern formation occurs at scales L ~ L_RD.

**Structural role:** Sets the architectural resolution scale. Analogous to epsilon in AC/CH and the Kolmogorov scale eta in NS. But unlike those scales, L_RD is *constitutive-dependent* (it varies with D and R).

---

**U3. Turing Instability Condition**

For n = 2 with Jacobian **J** and diffusion D_u, D_v at a stable steady state:

    Turing instability iff:
    (i)   tr(**J**) < 0,  det(**J**) > 0
    (ii)  D_v J_{11} + D_u J_{22} > 0
    (iii) (D_v J_{11} + D_u J_{22})^2 > 4 D_u D_v det(**J**)

The critical diffusion ratio for Turing instability is:

    (D_v / D_u)_crit = [J_{11} J_{22} - 2 det(**J**) + 2 sqrt(det(**J**)(det(**J**) - J_{11} J_{22}))] / J_{22}^2

**Structural role:** Determines whether spatial patterning is possible. The condition is *algebraic* — it can be checked from the Jacobian and diffusion matrix alone.

---

**U4. Wave-Speed Inequality for Bistable Fronts**

For scalar RD with R(u_-) = R(u_+) = 0, R having one unstable zero between u_- and u_+:

    c* = integral_{u_-}^{u_+} R(u) du / integral (phi')^2 dz

For Fisher–KPP-type reactions:

    c >= c_min = 2 sqrt(D R'(0))

**Structural role:** Determines propagation speeds. The wave speed is *uniquely selected* (bistable) or *bounded from below* (monostable).

---

**U5. Excitability Threshold Inequality**

For excitable systems (e.g., FitzHugh–Nagumo) with rest state **u**_0:

    There exists delta_* > 0 such that:
    ||**u**(0) - **u**_0|| < delta_*  =>  ||**u**(t) - **u**_0|| → 0
    ||**u**(0) - **u**_0|| > delta_*  =>  **u** fires a pulse before returning

The threshold delta_* is determined by the nullcline geometry and is sharp in the singular limit (epsilon → 0).

**Structural role:** Defines the boundary between sub-threshold and super-threshold response. The excitability threshold is the RD analogue of a phase transition.

---

**U6. Hopf Oscillation Criterion**

A homogeneous steady state **u**_0 undergoes a Hopf bifurcation when:

    **J** has eigenvalues lambda = alpha(mu) ± i omega(mu) with alpha(mu_c) = 0, alpha'(mu_c) ≠ 0

The oscillation frequency at onset is omega(mu_c). The bifurcation can be:
- Supercritical: stable limit cycle born at the bifurcation. Amplitude grows as sqrt(mu - mu_c).
- Subcritical: unstable limit cycle shrinks onto the steady state. Hysteresis and hard onset.

**Structural role:** Determines the onset of sustained oscillations. Combined with diffusion, the Hopf instability can produce traveling waves, spiral waves, or spatiotemporal chaos.

---

**U7. No Maximum Principle for n >= 2 (Negative Universal Inequality)**

    For n >= 2: sup_{x,t} u_i(x,t) is NOT bounded by sup_x u_{i,0}(x)    generically

The component-wise maximum principle fails for multi-species systems. Individual concentrations can be amplified beyond their initial range by cross-species coupling.

**Structural role:** Negative bound — a statement about what is NOT guaranteed. The absence of the maximum principle is the structural reason that multi-species RD can exhibit phenomena (Turing instability, oscillations) that scalar RD cannot.

---

**U8. No Global Lyapunov Functional (Negative Universal Inequality)**

    For generic multi-species RD: no V[**u**] exists with dV/dt <= 0 along all solutions

The dynamics are not confined to monotone descent. Limit cycles, quasi-periodic orbits, and strange attractors are permitted.

**Structural role:** The fundamental negative inequality of the RD class. Its absence is what separates RD from AC/CH and permits the full range of nonlinear dynamics.

---

**U9. No Conservation Law (Negative Universal Inequality)**

    d/dt integral u_i dx = integral R_i(**u**) dx ≠ 0    generically

Total mass is not conserved. The architecture can create and destroy species.

**Structural role:** Permits source/sink dynamics, population growth/decay, and chemical production/consumption — none of which are accessible to conserved architectures (CH).

---

**U10. Blowup Criterion (Fujita Exponent)**

For partial_t u = D Delta u + u^p on R^d:

    p_F = 1 + 2/d    (Fujita exponent)

    1 < p <= p_F:  All positive solutions blow up in finite time.
    p > p_F:       Small-data global existence; large-data blowup.

Blowup rate: ||u(t)||_{L^infinity} ~ C(T* - t)^{-1/(p-1)}.

**Structural role:** Determines the boundary between global existence and finite-time blowup within the scalar RD class. The Fujita exponent is the *dimensional signature* of the diffusion-reaction competition: it expresses the precise threshold where the reaction's super-linear growth overwhelms the diffusion's quadratic spreading.

---

### Universal Inequality Summary

| Label | Inequality                          | Type            | Status              | Role                        |
|-------|--------------------------------------|-----------------|---------------------|-----------------------------|
| U1    | Parabolic smoothing                  | Positive        | All RD              | Regularity baseline         |
| U2    | Reaction-diffusion balance           | Scale relation  | All RD              | Sets L_RD                   |
| U3    | Turing instability condition         | Algebraic       | n >= 2              | Pattern formation gate      |
| U4    | Wave-speed inequality                | Bound           | Scalar bistable/mono| Propagation rate             |
| U5    | Excitability threshold               | Threshold       | Excitable kinetics  | Pulse firing gate            |
| U6    | Hopf oscillation criterion           | Bifurcation     | n >= 2              | Oscillation onset            |
| U7    | No maximum principle (n >= 2)        | Negative        | n >= 2              | Permits amplification        |
| U8    | No Lyapunov functional               | Negative        | Generic             | Permits oscillation/chaos    |
| U9    | No conservation law                  | Negative        | Generic             | Permits source/sink          |
| U10   | Blowup criterion (Fujita)            | Threshold       | Scalar, u^p kinetics| Regularity boundary          |

**Structural note:** Three of the ten universal inequalities (U7, U8, U9) are *negative* — they state what the architecture does NOT guarantee. This is unique in the PDE Atlas: AC has zero negative universal inequalities, CH has one (no maximum principle, E6), NS has one (maximum principle failure, E9 in Mode 1). The RD class has *three* — reflecting its status as the loosest architecture.

---

## 4. Attractors and Long-Time Behavior

### 4.1 Scalar RD with Bounded Kinetics (AC-Type)

For scalar RD (n = 1) with R bounded on an invariant interval [a, b]:

**Global attractor:** Exists. Compact, finite-dimensional, connected subset of H^1(Omega).

**Structure:** The attractor contains:
- All stable steady states.
- All unstable/saddle steady states.
- All heteroclinic connections (monotone fronts connecting different steady states).
- Traveling wave profiles (if the domain is unbounded or periodic).

**Long-time behavior:** Every solution converges to a steady state (on bounded domains) or to a traveling wave (on unbounded domains or large periodic domains). The convergence is monotone if a Lyapunov functional exists (gradient systems) or possibly non-monotone otherwise.

**Attractor dimension:** Bounded by C(D, ||R'||, |Omega|). The attractor is *finite-dimensional* — the PDE reduces to finite-dimensional dynamics on the attractor.

### 4.2 Multi-Species RD with Oscillatory Kinetics

For n >= 2 with oscillatory ODE kinetics (stable limit cycle):

**Global attractor:** Exists (under appropriate dissipativity conditions — R must not allow unbounded growth). May be *infinite-dimensional* in the spatiotemporal chaos regime, or finite-dimensional for simple oscillations.

**Structure — the attractor zoo:**

- **Uniform oscillation:** All points oscillate in phase. The attractor is a single limit cycle in the spatially uniform subspace. Dimension = 1 (the phase of the oscillation).

- **Traveling waves:** Plane-wave solutions u(x, t) = U(x - ct) that are periodic in the comoving frame. Attractor dimension = 2 (phase + translation).

- **Spiral waves (d = 2):** Rotating spirals with a phase singularity at the tip. Attractor dimension depends on the number of spirals and their interactions. For a single spiral on a large domain: dimension ~ 3 (tip position + rotation phase).

- **Multi-spiral states:** Multiple interacting spirals. The dynamics on the attractor include spiral drift, pair annihilation, and spiral-tip meandering. Attractor dimension scales with the number of spirals.

- **Spatiotemporal chaos:** Irregular, aperiodic dynamics with positive Lyapunov exponents. The attractor is *high-dimensional* (possibly with fractal dimension growing with domain size). This is the most complex attractor in the PDE Atlas.

### 4.3 The Richest Attractor Zoo

The RD class has the *richest attractor zoo* of any architecture in the PDE Atlas:

| Attractor Type              | AC  | CH  | NS (2D) | NS (3D) | RD          |
|-----------------------------|-----|-----|---------|---------|-------------|
| Stable fixed points         | Yes | Yes | Yes     | Yes     | Yes         |
| Traveling fronts             | Yes | No  | No      | No      | Yes         |
| Traveling pulses             | No  | No  | No      | No      | Yes         |
| Limit cycles                 | No  | No  | Yes*    | Yes*    | Yes         |
| Traveling waves              | No  | No  | No      | No      | Yes         |
| Spiral waves                 | No  | No  | Yes**   | Yes**   | Yes         |
| Turing patterns              | No  | No  | No      | No      | Yes (n>=2)  |
| Quasi-periodic tori          | No  | No  | Yes*    | Yes*    | Yes         |
| Strange attractors           | No  | No  | Yes*    | Open    | Yes         |
| Spatiotemporal chaos         | No  | No  | Yes*    | Open    | Yes         |

*NS when forced. **NS vortices are not spiral waves in the RD sense but share rotational structure.

The gradient-flow architectures (AC, CH) are confined to fixed points and connecting orbits — monotone descent forbids everything else. NS (when forced) can exhibit complex attractors, but the analysis is complicated by the nonlocal pressure channel and the open regularity problem in 3D. The RD class admits the full range of attractor types *structurally*, without requiring forcing and without nonlocal complications.

### 4.4 Attractor Dimension Scaling

For the RD class, the attractor dimension depends on the constitutive parameters:

**Scalar RD:** dim(A) ~ |Omega| / L_RD^d. Proportional to the number of reaction-diffusion "cells" fitting in the domain.

**Multi-species oscillatory RD:** dim(A) can scale as |Omega| / L_RD^d (extensive — proportional to domain volume) in the spatiotemporal chaos regime. This is the *most complex* attractor scaling in the PDE Atlas: the number of effective degrees of freedom grows linearly with the domain size.

**Comparison:**
- AC: dim(A) ~ number of metastable interfaces ~ |Omega| / (L * epsilon). Finite and decreasing over time.
- CH: dim(A) ~ G^{2/3} (Grashof number in the forced case). Finite.
- NS (2D): dim(A) ~ G^{2/3}. Finite (forced).
- RD (chaotic): dim(A) ~ |Omega| / L_RD^d. Can be *arbitrarily large* for large domains.

---

## 5. Comparison with AC and CH

### 5.1 Allen–Cahn

**AC dynamics:** Monotone descent of a Lyapunov functional. Phase selection → interface formation → mean-curvature shrinkage → extinction → uniform equilibrium. Every trajectory converges to a steady state. No oscillations, no patterns, no chaos, no sustained dynamics.

**RD dynamics:** No Lyapunov constraint (generically). Oscillations, patterns, waves, chaos, excitability — the full range of nonlinear dynamics. Trajectories may converge to steady states, limit cycles, quasi-periodic orbits, or strange attractors.

**Structural difference:** AC is a *gradient-flow specialization* of scalar RD. The gradient-flow structure (AC-4) eliminates all non-monotone dynamics. Removing the gradient-flow constraint (passing from AC to general scalar RD) immediately permits traveling waves, excitability, and bistable switching. Passing to multi-species RD further permits Turing patterns, spiral waves, and spatiotemporal chaos.

### 5.2 Cahn–Hilliard

**CH dynamics:** Monotone descent of a Lyapunov functional (same as AC). Spinodal decomposition → interface formation → coarsening → equilibrium. Mass conservation forces coarsening instead of extinction. No oscillations, no patterns, no chaos.

**RD dynamics:** No conservation constraint (generically). Species can be created and destroyed locally. No coarsening (which requires conservation). Instead, the RD class has Turing patterns (stationary structures maintained by reaction-diffusion balance, not by conservation) and traveling waves (propagating structures that AC's gradient flow forbids).

**Structural difference:** CH is a fourth-order conserved gradient flow, outside the RD class. The conservation axiom (CH-3) and the fourth-order structure (from the conserving Laplacian) produce phenomena (coarsening, Ostwald ripening) that RD cannot generate. Conversely, RD produces phenomena (oscillations, spirals, chaos) that CH cannot generate. The two architectures have *disjoint* dynamical repertoires beyond their shared fixed-point convergence.

### 5.3 Positioning Summary

| Feature                    | AC                  | CH                  | RD (generic)         |
|----------------------------|---------------------|---------------------|----------------------|
| Lyapunov functional        | Yes (F)             | Yes (F)             | Generically no       |
| Maximum principle          | Yes                 | No                  | Scalar only          |
| Conservation               | No                  | Yes                 | Generically no       |
| Gradient-flow structure    | Yes (L^2)           | Yes (H^{-1})        | Generically no       |
| Long-time behavior         | Convergence to ±1   | Convergence to phases| Constitutive-dependent|
| Oscillations permitted     | No                  | No                  | Yes                  |
| Patterns permitted         | No                  | No (coarsening only)| Yes (Turing, spirals)|
| Chaos permitted            | No                  | No                  | Yes                  |
| Traveling waves            | Fronts only         | Not standard        | Fronts, pulses, waves|
| Blowup possible            | No                  | No                  | Yes (constitutive)   |
| Attractor complexity       | Fixed points        | Fixed points        | Full zoo             |

The RD class is the *universal architecture* for spatially extended nonlinear dynamics — the broadest second-order parabolic class, containing AC as a gradient-flow specialization and generating the full range of pattern-forming, oscillatory, excitable, and chaotic behaviors that gradient-flow architectures cannot access.

---

*End of Mode 2: PDE → Extremal Dynamics. Mode 3 (Channels → Constraint Surface) will follow in a subsequent file.*
