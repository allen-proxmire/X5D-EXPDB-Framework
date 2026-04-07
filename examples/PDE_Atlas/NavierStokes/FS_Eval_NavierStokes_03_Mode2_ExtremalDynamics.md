# AD Evaluation: Navier–Stokes Equations — Mode 2: PDE → Extremal Dynamics

Allen Proxmire

April 2026

---

## Overview

Mode 2 of the AD evaluation moves from the static envelope (Mode 1) to the *dynamics* — the time-evolution behavior that the PDE forces, permits, or forbids. Where Mode 1 asked "what does the architecture allow?", Mode 2 asks "what does the architecture *do*?"

The analysis proceeds through six stages: energy balance and dissipation (the primary dynamical accounting), enstrophy and vorticity dynamics (the secondary accounting that reveals the 2D/3D split), extremal behaviors (the dynamical frontier), universal inequalities (the quantitative skeleton), attractors and long-time behavior (the asymptotic fate), and a comparison with ED's Mode 2.

Throughout, we work with the incompressible NS equations as specified in the Architectural Specification:

    partial_t **u** + (**u** . nabla)**u** = -nabla p + nu Delta **u** + **f**
    div(**u**) = 0

on a domain Omega subset R^d (d = 2, 3) with nu > 0. All inner products are L^2(Omega) and integration is over Omega unless otherwise stated. We write E(t) = (1/2)||**u**(t)||^2 for kinetic energy, epsilon(t) = nu ||nabla **u**(t)||^2 for the dissipation rate, and Omega(t) = (1/2)||omega(t)||^2 for enstrophy (where omega = curl **u**).

---

## 1. Energy Balance and Dissipation

### 1.1 Derivation of the Kinetic Energy Identity

Take the L^2 inner product of the momentum equation with **u**:

    (partial_t **u**, **u**) + ((**u** . nabla)**u**, **u**) = -(nabla p, **u**) + nu(Delta **u**, **u**) + (**f**, **u**)

Each term resolves as follows.

**Time derivative term:**

    (partial_t **u**, **u**) = d/dt (1/2)||**u**||^2 = dE/dt

**Advection term:** For divergence-free **u** with vanishing boundary conditions (no-slip or periodic):

    ((**u** . nabla)**u**, **u**) = integral u_j (partial_j u_i) u_i dx
                                  = (1/2) integral u_j partial_j |**u**|^2 dx
                                  = -(1/2) integral (div **u**) |**u**|^2 dx = 0

The advection term vanishes *identically* from the energy equation. This is a structural identity, not an approximation: incompressible self-advection redistributes kinetic energy across space and across scales, but creates and destroys none. The advection channel is *energy-invisible* — it does all of its work (cascade, mixing, stretching) without appearing in the energy budget.

**Pressure term:** For divergence-free **u**:

    (nabla p, **u**) = -integral p (div **u**) dx = 0

The pressure term also vanishes identically. Pressure does no work on an incompressible field. This is the kinematic consequence of NS-6: the Lagrange multiplier enforcing the constraint performs no net work on the constrained submanifold.

**Viscous term:** Integration by parts (with vanishing boundary terms):

    nu(Delta **u**, **u**) = -nu ||nabla **u**||^2 = -epsilon(t)

The viscous term is strictly non-positive. It removes kinetic energy at a rate proportional to the L^2 norm of the velocity gradient — the *enstrophy* (up to a factor of nu). High-gradient regions dissipate faster. The viscous channel is the architecture's sole energy sink.

**Forcing term:**

    (**f**, **u**) = P_f(t)

This is the instantaneous power input from external forcing.

### 1.2 The Energy Identity (Smooth Solutions)

Assembling:

    dE/dt = -epsilon(t) + P_f(t)

or equivalently:

    d/dt (1/2)||**u**||^2 = -nu ||nabla **u**||^2 + (**f**, **u**)         ... (Energy-I)

This is an *exact identity* for smooth solutions. It states that kinetic energy changes at a rate equal to the power input minus the viscous dissipation. The advection and pressure channels are structurally silent in the energy budget.

**Integrated form:**

    E(t) + nu integral_0^t ||nabla **u**(s)||^2 ds = E(0) + integral_0^t P_f(s) ds     ... (Energy-II)

Total kinetic energy at time t, plus total energy dissipated over [0, t], equals initial energy plus total work done by forcing.

### 1.3 The Energy Inequality (Weak Solutions)

For Leray–Hopf weak solutions, the identity (Energy-II) weakens to an inequality:

    E(t) + nu integral_0^t ||nabla **u**(s)||^2 ds <= E(0) + integral_0^t P_f(s) ds     ... (Energy-III)

The inequality is one-sided: energy may be *lost* (anomalous dissipation) but never spontaneously *gained*. If equality fails, the gap measures energy that has been dissipated through a mechanism not captured by the classical viscous term — a structural signal that the solution has left the smooth regime.

### 1.4 The Unforced Dissipation Pathway

For **f** = 0:

    dE/dt = -epsilon(t) <= 0

Kinetic energy is strictly monotone decreasing (unless **u** = 0). Every unforced NS flow dissipates to rest. The dissipation rate epsilon(t) = nu ||nabla **u**||^2 is controlled from below by the Poincare inequality (on bounded domains):

    epsilon(t) = nu ||nabla **u**||^2 >= nu lambda_1 ||**u**||^2 = 2 nu lambda_1 E(t)

where lambda_1 is the first eigenvalue of -Delta on Omega. This yields exponential decay:

    E(t) <= E(0) exp(-2 nu lambda_1 t)

On the whole space R^d, the Poincare inequality fails and the decay is algebraic (see E-Bound 8 in Mode 1): E(t) = O(t^{-d/2}).

### 1.5 Role of the Leray Projection

The energy identity can be written in Leray-projected form:

    dE/dt = -(nu A **u**, **u**) + (P **f**, **u**)

where A = -P Delta is the Stokes operator and P is the Leray projector. The Stokes operator is a *positive, self-adjoint* operator on the space of divergence-free fields. Its eigenvalues {lambda_k} form a discrete increasing sequence tending to infinity (on bounded domains). The energy dissipation is:

    epsilon(t) = nu (A **u**, **u**) = nu sum_k lambda_k |hat{u}_k|^2

where hat{u}_k are the Fourier–Stokes coefficients. Dissipation is *weighted toward high modes*: modes with large lambda_k (small spatial scales) are dissipated faster. This is the spectral signature of the viscous channel — it acts as a low-pass filter, preferentially removing small-scale structure.

The Leray projection's role in the energy pathway is *structural*: it confines the dynamics to the divergence-free subspace, ensures that pressure does no work, and reduces the energy budget to a competition between the Stokes operator (dissipation) and the projected forcing (injection). The nonlinear advection term, after projection, affects the *distribution* of energy across modes but not the *total* energy.

---

## 2. Enstrophy and Vorticity Dynamics

### 2.1 Derivation of the Vorticity Equation

Apply the curl operator to the momentum equation. Using the vector identity

    curl[(**u** . nabla)**u**] = (**u** . nabla)omega - (omega . nabla)**u** + omega(div **u**) - **u**(div omega)

and noting div **u** = 0 (incompressibility) and div omega = div(curl **u**) = 0 (identically), we obtain:

**3D Vorticity Equation:**

    partial_t omega + (**u** . nabla)omega = (omega . nabla)**u** + nu Delta omega + curl **f**     ... (Vort-3D)

**2D Vorticity Equation** (omega is a scalar, omega = partial_1 u_2 - partial_2 u_1):

    partial_t omega + (**u** . nabla)omega = nu Delta omega + (curl **f**)_3                        ... (Vort-2D)

The *vortex stretching term* (omega . nabla)**u** is present in 3D and *identically absent* in 2D. This is not a simplification or an approximation — it is a structural consequence of dimension: in 2D, vorticity is a scalar and cannot be stretched by the velocity gradient. The 2D/3D asymmetry in the vorticity equation is architecturally forced.

### 2.2 Physical Content of Vortex Stretching

The term (omega . nabla)**u** represents the stretching and tilting of vortex lines by the velocity gradient. Decompose the velocity gradient into strain rate S and rotation R:

    partial_j u_i = S_ij + R_ij

The stretching term becomes:

    [(omega . nabla)**u**]_i = omega_j S_ji + omega_j R_ji = (S . omega)_i

(The antisymmetric part R produces only rotation of omega, not amplification.) The rate of change of vorticity magnitude along a material element is governed by the *eigenvalues of the strain rate tensor*:

    d/dt |omega| = (omega-hat . S . omega-hat) |omega| + diffusion + forcing

where omega-hat = omega / |omega|. If omega is aligned with the direction of maximum strain (eigenvalue lambda_1 > 0), vorticity is amplified exponentially:

    |omega(t)| ~ |omega(0)| exp(integral_0^t lambda_1(s) ds)

This exponential amplification is the destabilizing mechanism unique to 3D. It has no 2D counterpart and no architectural bound: the axioms do not constrain the time-integrated strain rate *a priori*.

### 2.3 Enstrophy Balance

Take the L^2 inner product of the vorticity equation with omega:

**3D Enstrophy Equation:**

    d/dt Omega(t) = integral (omega . nabla)**u** . omega dx - nu ||nabla omega||^2 + integral (curl **f**) . omega dx     ... (Enst-3D)

              =          S(t)                    -     D_omega(t)     +         F_omega(t)

where:
- S(t) = integral omega_i S_ij omega_j dx is the *stretching production* of enstrophy
- D_omega(t) = nu ||nabla omega||^2 is the *enstrophy dissipation* (palinstrophy)
- F_omega(t) = integral (curl **f**) . omega dx is the *enstrophy forcing*

**2D Enstrophy Equation:**

    d/dt Omega(t) = -nu ||nabla omega||^2 + integral (curl **f**) omega dx                         ... (Enst-2D)

### 2.4 The 2D Closure

In 2D, the enstrophy equation (Enst-2D) has no production term. Therefore:

    d/dt Omega(t) <= -nu ||nabla omega||^2 + ||curl **f**||_{L^2} ||omega||_{L^2}

By Young's inequality:

    d/dt Omega(t) <= -(nu/2) ||nabla omega||^2 + (1/(2nu)) ||curl **f**||_{L^2}^2

Dropping the palinstrophy term:

    d/dt Omega(t) <= (1/(2nu)) ||curl **f**||_{L^2}^2

Integrating:

    Omega(t) <= Omega(0) + (1/(2nu)) integral_0^t ||curl **f**(s)||^2 ds       ... (Enst-2D-Bound)

This bound is *finite for all time* if the forcing is square-integrable. Enstrophy control implies:

    ||nabla **u**(t)||_{L^2} = ||omega(t)||_{L^2} <= C(t)    [finite for all t]

which, via Sobolev embedding in 2D, gives L^infinity control of **u**. The regularity bootstrap closes: bounded velocity gradients prevent singularity formation. **The 2D NS architecture is globally regular.** The closure is achieved entirely by the *absence* of vortex stretching.

### 2.5 The 3D Gap

In 3D, the stretching term S(t) must be estimated. Using the Cauchy–Schwarz and Sobolev inequalities:

    |S(t)| = |integral omega_i S_ij omega_j dx| <= ||omega||_{L^3}^2 ||nabla **u**||_{L^3}

By Sobolev embedding and interpolation in 3D:

    |S(t)| <= C ||omega||_{L^2} ||nabla omega||_{L^2}^2

Substituting into (Enst-3D):

    d/dt Omega <= C ||omega||_{L^2} ||nabla omega||^2 - nu ||nabla omega||^2 + F_omega

    = ||nabla omega||^2 (C ||omega||_{L^2} - nu) + F_omega

If ||omega||_{L^2} exceeds nu / C, the effective coefficient of ||nabla omega||^2 becomes *positive* — dissipation is overwhelmed by production. The enstrophy equation becomes a differential inequality of the form:

    d/dt Omega <= C' Omega^3 / nu^2 + F_omega         ... (Enst-3D-Open)

(after using the Poincare or interpolation inequality to bound ||nabla omega||^2 from below by Omega). The cubic nonlinearity in Omega admits finite-time blowup: the ODE dy/dt = C y^3 blows up in time T* = 1/(2C y(0)^2). The PDE inequality (Enst-3D-Open) does not force blowup — but it does not prevent it either. **The 3D enstrophy inequality is open.**

---

## 3. Extremal Behaviors

The extremal behaviors are the dynamical configurations at the *boundary* of what the PDE permits — the most extreme states that the architecture can reach (or approach) under its own evolution.

### 3.1 Finite-Time Blowup Channels (3D)

The architecture permits — but does not require — the following blowup scenarios in 3D:

**Channel B1: Vorticity Blowup.** The Beale–Kato–Majda theorem (see U3 below) states that a smooth solution loses regularity at time T* if and only if:

    integral_0^{T*} ||omega(t)||_{L^infinity} dt = +infinity

If blowup occurs, the L^infinity norm of vorticity must diverge. The architectural mechanism is vortex stretching: local alignment of omega with the direction of maximum strain produces exponential amplification of |omega|, which steepens gradients, which enhances strain, in a self-reinforcing loop.

**Channel B2: Strain Concentration.** Equivalently, blowup requires the strain rate tensor to develop a sufficiently strong and persistent singularity. The strain eigenvalue lambda_max must grow fast enough that its time integral diverges.

**Channel B3: Energy Cascade to Zero Scale.** In Fourier space, blowup corresponds to kinetic energy cascading to arbitrarily small scales in finite time — the spectral support of **u** reaching wavenumber k = infinity at t = T*. The viscous dissipation nu k^2 at wavenumber k grows with k^2, but if the cascade is faster than quadratic, dissipation cannot keep pace.

**Structural constraint on blowup:** Even if blowup occurs, the energy inequality (Energy-III) must hold throughout. Kinetic energy remains bounded up to and through any potential blowup time. A 3D NS singularity, if it exists, would be a *regularity failure at bounded energy* — the velocity concentrates at a point (or on a set of measure zero) without the total energy diverging. This is the architectural signature: blowup is a breakdown of *smoothness*, not of *energy*.

### 3.2 Global Regularity Channels

**Channel R1: 2D — Unconditional.** In 2D, global regularity follows from the enstrophy closure (Section 2.4). No additional conditions are needed. Every smooth initial datum with finite energy produces a global smooth solution.

**Channel R2: 3D — Small Data.** If ||**u**_0||_{L^3(R^3)} (or an equivalent critical norm) is sufficiently small relative to nu, the solution remains smooth globally. The viscous channel dominates the advection channel at all scales when the Reynolds number is small enough. The precise threshold is:

    ||**u**_0||_{L^3} < c nu    (for an absolute constant c)

**Channel R3: 3D — Conditional (Serrin).** If the solution *happens* to satisfy a Serrin-class bound (U4 below), regularity is guaranteed. The architecture is self-consistent whenever the velocity field remains in a scaling-critical space-time class.

**Channel R4: 3D — Eventual Regularity (Unforced).** Even if a solution develops a singularity at finite time T*, the energy inequality guarantees that E(t) -> 0 as t -> infinity. Eventually, the solution enters the small-data regime (R2) and becomes smooth for all sufficiently large t. Singularities, if they occur, are *transient*.

### 3.3 Scaling-Critical Behavior

The NS scaling symmetry **u** -> lambda **u**(lambda x, lambda^2 t) leaves the equations invariant and identifies the *critical* quantities:

| Quantity             | Scaling dimension | Critical? |
|----------------------|-------------------|-----------|
| ||u||_{L^2}          | lambda^{d/2 - 1}  | d=2 only  |
| ||u||_{L^3}          | lambda^0           | Yes (3D)  |
| ||u||_{L^d}          | lambda^0           | Yes       |
| ||omega||_{L^1}      | lambda^{d-2}       | d=2 only  |
| ||omega||_{L^{3/2}}  | lambda^0           | Yes (3D)  |
| ||nabla u||_{L^{d/2}}| lambda^0           | Yes       |
| E = ||u||_{L^2}^2    | lambda^{d-2}       | d=2 only  |

In 3D, the energy E scales as lambda^1 — it is *supercritical*. A rescaling that concentrates the solution to smaller scales *increases* the critical norm while leaving the energy fixed. The architecture's primary conservation law (energy) is therefore *blind* to the scaling that drives potential blowup. This is the dimensional root of the 3D open problem.

### 3.4 Energy Cascade Pathways

The nonlinear advection term, while energy-neutral in total, redistributes energy across spatial scales. In Fourier space:

    partial_t hat{u}(k) = T(k) - nu |k|^2 hat{u}(k) + hat{f}(k)

where T(k) is the triadic transfer term arising from the quadratic nonlinearity. The transfer T conserves total energy: sum_k T(k) = 0.

**Forward cascade (3D):** Energy is transferred from large scales (small |k|) to small scales (large |k|), where viscous dissipation nu |k|^2 absorbs it. This is the *Kolmogorov cascade* — a statistical consequence of the architecture in 3D turbulence. The cascade proceeds until reaching the *dissipation scale* eta ~ (nu^3 / epsilon)^{1/4}, where viscous damping balances nonlinear transfer.

**Inverse cascade (2D):** In 2D, energy is transferred preferentially from small scales to large scales (inverse cascade), while enstrophy cascades forward. This dual cascade is an architectural consequence of the simultaneous conservation of energy and enstrophy by the 2D advection term.

**Extremal cascade rate:** The most extreme dynamical behavior occurs when the forward cascade in 3D is maximally efficient — when all of the energy injected at large scales is transferred without loss to arbitrarily small scales in finite time. This is the cascade pathway to the blowup channel B3.

### 3.5 Vortex Stretching Amplification

The extremal vortex stretching scenario is a *self-similar* blowup:

    **u**(x, t) ~ (T* - t)^{-1/2} **U**((x - x_0) / (T* - t)^{1/2})

where **U** is a self-similar profile. Under this ansatz, vorticity grows as:

    |omega(x_0, t)| ~ (T* - t)^{-1}

and the BKM integral diverges logarithmically:

    integral_0^{T*} ||omega||_{L^infinity} dt ~ integral_0^{T*} (T* - t)^{-1} dt = +infinity

The architecture *admits* this self-similar scaling (it is consistent with the PDE), but no proof exists that the PDE dynamics actually produce it. The question is whether the strain field can maintain sufficient alignment with vorticity, against the competing effects of viscous diffusion and geometric depletion, for long enough to drive the singularity to completion.

**Geometric depletion:** There are known structural mechanisms by which the geometry of the vorticity field resists blowup. The most important is the *depletion of nonlinearity*: in regions of high vorticity, the vorticity direction omega-hat tends to become locally parallel, which suppresses the stretching term (stretching requires spatial variation of omega-hat). This depletion is an architectural feature — it is a consequence of the advection and incompressibility channels working together — but its quantitative sufficiency is not established.

---

## 4. Universal Inequalities

The following inequalities hold for *every* admissible NS evolution. They are the quantitative backbone of the Mode 2 analysis, labeled U1–U9 for reference.

---

**U1. Energy Inequality**

    E(t) + nu integral_0^t ||nabla **u**||^2 ds <= E(0) + integral_0^t (**f**, **u**) ds

Holds for all Leray–Hopf weak solutions. Equality for smooth solutions. This is the primary accounting identity of the architecture.

**Structural role:** Ensures that kinetic energy is bounded for all time (given bounded forcing and initial data). Does not control derivatives of **u** in 3D.

---

**U2. Enstrophy Inequality (2D, Closed)**

    Omega(t) <= Omega(0) + (1/(2nu)) integral_0^t ||curl **f**||^2 ds       [d = 2]

Holds unconditionally in 2D. Provides global-in-time control of ||nabla **u**||_{L^2}, which closes the regularity bootstrap.

**Structural role:** The inequality that separates 2D from 3D. Its validity rests entirely on the absence of vortex stretching in 2D.

---

**U3. Beale–Kato–Majda (BKM) Criterion**

A smooth solution on [0, T) extends to [0, T] if and only if:

    integral_0^T ||omega(t)||_{L^infinity} dt < +infinity

Equivalently: *blowup occurs at time T if and only if the L^infinity norm of vorticity has a non-integrable singularity at T.*

**Structural role:** Localizes the blowup mechanism to vorticity concentration. If blowup occurs, it must be accompanied by ||omega||_{L^infinity} -> infinity. This is the architecture's diagnostic: the single quantity whose integrability controls global regularity.

---

**U4. Serrin Conditional Regularity**

If a weak solution satisfies:

    **u** in L^q(0, T; L^p(R^3))    with   2/q + 3/p <= 1,   3 < p <= infinity

then **u** is smooth on (0, T].

**Endpoint cases:**
- p = infinity, q = 2: **u** in L^2(0,T; L^infinity) — the Serrin endpoint.
- p = 3, q = infinity: **u** in L^infinity(0,T; L^3) — the Escauriaza–Seregin–Sverak critical case (regularity holds here too, by their celebrated theorem).

**Structural role:** Defines the *conditional interior* of the envelope. Any solution satisfying a Serrin-class bound is guaranteed smooth. The open question is whether the PDE dynamics can push a solution outside every Serrin class.

---

**U5. Ladyzhenskaya Inequality**

In 2D:

    ||**u**||_{L^4}^2 <= C ||**u**||_{L^2} ||nabla **u**||_{L^2}

In 3D:

    ||**u**||_{L^4}^{4/3} <= C ||**u**||_{L^2}^{2/3} ||nabla **u**||_{L^2}^{2/3}
    ||**u**||_{L^3}^3 <= C ||**u**||_{L^2}^{3/2} ||nabla **u**||_{L^2}^{3/2}

These are *interpolation inequalities* between the energy norm and the dissipation norm. They are the bridge between U1 (energy control) and higher-integrability estimates.

**Structural role:** In 2D, the Ladyzhenskaya inequality is the key tool that converts energy + enstrophy control into L^infinity control, closing the bootstrap. In 3D, the exponents are unfavorable — the interpolation does not close without an independent bound on higher norms.

---

**U6. Poincare Inequality (Bounded Domains)**

On a bounded domain Omega with no-slip or periodic boundary conditions:

    ||**u**||_{L^2}^2 <= (1/lambda_1) ||nabla **u**||_{L^2}^2

where lambda_1 > 0 is the first eigenvalue of the Stokes operator on Omega.

**Structural role:** Converts dissipation control (||nabla **u**||^2) into energy control (||**u**||^2), yielding exponential energy decay in the unforced case:

    E(t) <= E(0) exp(-2 nu lambda_1 t)

This inequality is *domain-dependent* — lambda_1 depends on the size and shape of Omega. On R^d, lambda_1 = 0 and the inequality fails; decay is algebraic instead.

---

**U7. Grashof / Absorbing Ball Bound (Forced, Bounded Domain)**

For time-independent forcing **f** on a bounded domain, the long-time energy satisfies:

    limsup_{t -> infinity} ||**u**(t)||_{L^2}^2 <= ||**f**||_{H^{-1}}^2 / (nu^2 lambda_1)

The system is *ultimately bounded*: regardless of initial data, the energy is eventually confined to a ball of radius determined by nu, lambda_1, and the forcing strength. The dimensionless ratio

    G = ||**f**||_{H^{-1}} / (nu^2 lambda_1)

is the *Grashof number* — the architecture's intrinsic measure of the forcing-to-dissipation ratio. It controls the size of the absorbing ball and, in 2D, the dimension of the global attractor.

**Structural role:** Guarantees that the dynamics are ultimately confined to a bounded region of phase space, regardless of initial data. This is the architectural basis for the existence of attractors.

---

**U8. Pressure–Enstrophy Coupling**

    ||p||_{L^{d/2}} <= C ||**u**||_{L^d}^2

and via the Poisson equation:

    ||nabla p||_{L^{d/(d-1)}} <= C ||**u** otimes **u**||_{L^{d/(d-1)}}

The pressure is slaved to the velocity field at every instant. This coupling is not an inequality to be optimized — it is a *structural identity* degraded into an inequality by the Sobolev and Calderon–Zygmund estimates. The pressure carries no independent degrees of freedom.

**Structural role:** Ensures that pressure does not introduce new dynamical freedom. Every pressure estimate is reducible to a velocity estimate. The loss (quadratic dependence on **u**) is architecturally fixed by the nonlinearity of the Poisson source term.

---

**U9. Vortex Stretching / Strain-Enstrophy Inequality (3D)**

    |d/dt Omega| <= C ||S||_{L^infinity} Omega + nu ||nabla omega||^2 + forcing

where S is the strain rate tensor. The enstrophy growth rate is bounded by the *maximum strain rate* times the current enstrophy.

More precisely, using the eigenvalue decomposition of S with eigenvalues lambda_1 >= lambda_2 >= lambda_3 and the incompressibility constraint lambda_1 + lambda_2 + lambda_3 = 0:

    integral omega . S . omega dx <= lambda_1^{max} integral |omega|^2 dx

where lambda_1^{max} = ||lambda_1||_{L^infinity}.

**Structural role:** This is the *gate inequality* for 3D blowup. Blowup requires lambda_1^{max} to grow without bound, accumulating faster than viscosity can dissipate. The incompressibility constraint (lambda_1 + lambda_2 + lambda_3 = 0) places a structural restriction on the strain eigenvalues: positive stretching in one direction must be accompanied by compression in others. This is a partial architectural safeguard — it prevents isotropic expansion — but it does not prevent uniaxial stretching, which is the dominant blowup mechanism in all candidate scenarios.

---

### Universal Inequality Summary

| Label | Inequality                          | Dimension | Status       | Role                        |
|-------|--------------------------------------|-----------|--------------|-----------------------------|
| U1    | Energy inequality                    | 2D, 3D   | Unconditional| Primary accounting          |
| U2    | Enstrophy closure                    | 2D       | Unconditional| Regularity (2D)             |
| U3    | BKM criterion                        | 3D       | Conditional  | Blowup diagnostic           |
| U4    | Serrin regularity                    | 3D       | Conditional  | Regularity (conditional)    |
| U5    | Ladyzhenskaya interpolation          | 2D, 3D   | Unconditional| Norm bridge                 |
| U6    | Poincare                             | Bounded  | Unconditional| Energy-dissipation bridge   |
| U7    | Grashof / absorbing ball             | Bounded  | Unconditional| Ultimate boundedness        |
| U8    | Pressure–enstrophy coupling          | 2D, 3D   | Unconditional| Pressure elimination        |
| U9    | Strain–enstrophy gate                | 3D       | Unconditional| Blowup gate                 |

---

## 5. Attractors and Long-Time Behavior

### 5.1 Global Attractor (2D)

In 2D, for a bounded domain with time-independent forcing, the NS system possesses a *global attractor* A: a compact, invariant, finite-dimensional subset of the (infinite-dimensional) phase space that attracts all trajectories.

**Existence:** The absorbing ball bound (U7) and the enstrophy closure (U2) together provide the compactness and dissipativity required for the attractor existence theorem (Ladyzhenskaya, 1972).

**Dimension:** The attractor dimension is bounded above by:

    dim_H(A) <= c G^{2/3} (1 + log G)^{1/3}

(Hausdorff dimension bound, Constantin–Foias–Temam), where G is the Grashof number. The effective number of degrees of freedom of the long-time dynamics is *finite* and controlled by the architecture's parameters (nu, lambda_1, ||**f**||).

**Structure:** The attractor contains all stationary solutions, all periodic orbits, and all heteroclinic/homoclinic connections. It is the *skeleton* of the long-time dynamics — the minimal set that captures all persistent behavior.

**Architectural significance:** The 2D NS architecture reduces an infinite-dimensional PDE to finite-dimensional dynamics on the attractor. The attractor is the architecture's *compression* of the infinite-dimensional phase space into a finite-dimensional invariant set. This compression is made possible by the enstrophy closure: the viscous channel, unopposed by stretching, confines the dynamics to a finite-dimensional core.

### 5.2 The 3D Attractor Problem

In 3D, the existence of a global attractor is *open*, conditional on the regularity problem:

- If global regularity holds (all solutions remain smooth for all time), then the same argument as in 2D produces a global attractor, with dimension bounded by c G^{3/2} or similar.
- If blowup occurs for some initial data, the standard attractor theory breaks down: the semiflow is not well-defined on the energy space for all time, and the notion of "attracts all trajectories" becomes problematic.

**Weak attractor:** Foias–Temam have defined a *weak global attractor* (in the sense of Leray–Hopf weak solutions) that exists unconditionally in 3D. This weak attractor attracts all weak solutions, but its regularity properties are unknown — it might contain singular objects.

**Architectural significance:** The 3D architecture does not guarantee that its long-time dynamics are finite-dimensional. The compression achieved in 2D by enstrophy closure may fail in 3D. The architecture *might* be irreducibly infinite-dimensional in the long run — a qualitative difference with 2D.

### 5.3 Dissipation-Range Structure

At scales below the Kolmogorov dissipation length eta = (nu^3 / epsilon)^{1/4}, viscous dissipation dominates advection. The energy spectrum in the dissipation range decays exponentially:

    E(k) ~ exp(-c k eta)    for k eta >> 1

This exponential decay is an architectural consequence of the viscous channel: the Laplacian operator acts as a spectral filter with transfer function exp(-nu k^2 t), and at high wavenumbers this filter overwhelms the nonlinear transfer.

The dissipation range is the architecture's *built-in regularization scale*. Below eta, the dynamics are effectively linear (viscosity-dominated), and the velocity field is analytic. Above eta, the nonlinear advection channel dominates and produces the complex, chaotic, turbulent dynamics.

### 5.4 Inertial-Range Structure

Between the forcing scale L_f and the dissipation scale eta, the architecture produces an *inertial range* where neither forcing nor dissipation dominates, and energy cascades through the nonlinear advection channel alone. Dimensional analysis (Kolmogorov, 1941) predicts:

    E(k) ~ epsilon^{2/3} k^{-5/3}    for 1/L_f << k << 1/eta

The k^{-5/3} spectrum is not derivable from the PDE alone — it is a *statistical consequence* of the architecture operating in the turbulent regime, at high Reynolds number, under assumptions of isotropy and homogeneity. It is an emergent feature: the PDE does not contain a spectral exponent, but the architecture's channel structure (energy-neutral advection + scale-selective dissipation) produces this scaling as a robust statistical outcome.

**Architectural significance:** The inertial range is where the architecture's nonlinear channel operates *without interference* from either forcing or dissipation. The k^{-5/3} spectrum is the architecture's *equilibrium energy distribution* in this unsupervised regime — the state to which the cascade relaxes when left to its own devices.

### 5.5 The Role of Forcing

Forcing plays three structural roles in the long-time behavior:

1. **Energy injection:** Without forcing, all solutions decay to rest (U1, U6). Forcing is necessary for any non-trivial long-time dynamics. It is the architecture's *fuel*.

2. **Scale selection:** The spatial structure of **f** determines the injection scale L_f, which sets the top of the inertial range and, through the energy cascade, the dissipation rate epsilon. The forcing scale is an *external* parameter — the architecture does not self-select its injection scale.

3. **Attractor structure:** In 2D, the dimension and topology of the global attractor depend on the forcing (through the Grashof number). Different forcings produce qualitatively different long-time dynamics (steady states, periodic orbits, chaos) on the same domain with the same viscosity.

---

## 6. Comparison with ED Mode 2

The Mode 2 analysis reveals fundamental architectural contrasts between the Navier–Stokes and Event Density systems.

### 6.1 Stability

**ED:** Unconditionally stable. The FS/ED primitives define a static structure on the integers. There is no evolution, no instability, and no mechanism for any quantity to grow without bound. Every ED "trajectory" (evaluation of a sum or density function over increasing ranges of integers) converges or is bounded by classical analytic number theory results.

**NS:** Conditionally stable. In 2D, the architecture achieves unconditional stability through enstrophy closure — analogous to ED's unconditional boundedness. In 3D, stability is conditional: the architecture's own dynamics *might* drive the system to a singularity. The 3D NS architecture is the only FS-evaluated system whose self-consistency is an open question.

### 6.2 The Dissipation Simplex

**ED:** The FS/ED framework operates within a *closed dissipation simplex* — the coverage accounting (how prime coverage distributes across width layers) forms a complete, balanced budget with no open channels. The Chebyshev conservation law ensures that all mass is accounted for, and no quantity can escape the accounting.

**NS (2D):** The energy + enstrophy accounting forms a *closed dissipation simplex*. Energy is injected by forcing, cascades inversely, and is dissipated at large scales (or bounded by the domain). Enstrophy cascades forward and is dissipated at small scales. Both budgets close.

**NS (3D):** The energy budget closes (U1 holds unconditionally), but the enstrophy budget does *not* close — the vortex stretching term opens a gap in the accounting that current estimates cannot seal. The 3D NS dissipation simplex has an *open face*: the enstrophy face. This is architecturally unique among FS-evaluated systems.

### 6.3 Attractors

**ED:** The FS/ED architecture has a *unique attractor* in the following sense: the asymptotic distribution of primes, the Dickman function, the Erdos–Kac law, and all large-scale statistical features of the skyline are uniquely determined by the axioms. There is no sensitivity to initial conditions (there are no initial conditions — the integers are fixed). The attractor is the number-theoretic structure itself.

**NS (2D):** A global attractor exists, is compact and finite-dimensional, and contains the full long-time dynamics. The attractor depends on the forcing and the domain, but its *existence* is unconditional.

**NS (3D):** The existence of a classical global attractor is *open*. A weak attractor exists, but its regularity is unknown. The architecture may or may not compress its long-time dynamics to finite dimensions.

### 6.4 Blowup Channels

**ED:** No blowup channel exists. Every quantity in the FS/ED framework (prime counting functions, density functions, sieve remainders) is finite for any finite argument. The architecture does not admit divergences.

**NS (2D):** No blowup channel. Global regularity is proved. The architecture is self-consistent for all time.

**NS (3D):** One blowup channel exists, mediated by vortex stretching (B1–B3 in Section 3.1). This channel is structurally permitted by the architecture but not proven to be dynamically realized. The architecture's self-consistency in 3D is the content of the Clay Millennium Problem.

### 6.5 Summary Table

| Feature                    | ED              | NS (2D)         | NS (3D)           |
|----------------------------|-----------------|-----------------|---------------------|
| Stability                  | Unconditional   | Unconditional   | Open (conditional)  |
| Dissipation simplex        | Closed          | Closed          | Open (enstrophy)    |
| Attractor                  | Unique, static  | Exists, finite-dim | Open               |
| Blowup channel             | None            | None            | Vortex stretching   |
| Controlling inequality     | Chebyshev cons. | Enstrophy (U2)  | None (gap at U3/U9) |
| Dimensionality of dynamics | Fixed (static)  | Finite (attractor) | Unknown            |

---

*End of Mode 2: PDE → Extremal Dynamics. Mode 3 (structural diagnostics and the EXPBD triad) will follow in a subsequent file.*
