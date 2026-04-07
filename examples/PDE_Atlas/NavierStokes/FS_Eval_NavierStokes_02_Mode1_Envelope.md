# AD Evaluation: Navier–Stokes Equations — Mode 1: Axiom → Envelope

Allen Proxmire

April 2026

---

## Overview

Mode 1 of the AD evaluation traces the path from the axioms identified in the Architectural Specification to the *envelope* — the maximal set of constraints that the architecture imposes on all admissible states and evolutions. The envelope is the boundary of what the architecture permits. Everything inside is structurally possible; everything outside is axiomatically forbidden.

For the Navier–Stokes architecture, the envelope is defined by the interplay of the eight axioms (NS-1 through NS-8) and the five structural channels (advection, diffusion, pressure, forcing, incompressibility). The derivation proceeds in five stages: forbidden configurations, necessary configurations, extremal bounds, structural invariants, and the minimal inequality set.

Throughout, we work with the incompressible Navier–Stokes equations on a domain Omega subset R^d (d = 2 or 3) with kinematic viscosity nu > 0:

    partial_t **u** + (**u** . nabla)**u** = -nabla p + nu Delta **u** + **f**
    div(**u**) = 0
    **u**(x,0) = **u**_0(x),   div(**u**_0) = 0

---

## 1. Forbidden Configurations

A *forbidden configuration* is a state, operator, evolution, or coupling that is axiomatically excluded by the NS architecture. These are not merely unlikely or unphysical — they are structurally impossible within the system as defined.

### F1. Compressible Velocity Fields

**Axiom source:** NS-6 (Incompressibility).

Any velocity field **u** with div(**u**) ≠ 0 at any point (x, t) is forbidden. The incompressibility constraint is not approximate; it is exact and instantaneous. There is no relaxation parameter, no penalty, and no mechanism within the architecture for a velocity field to be "slightly compressible." The space of admissible states is the closed submanifold

    V = { **u** in H^1(Omega; R^d) : div(**u**) = 0 }

and the evolution is confined to V for all time. Sound waves, shock waves, density stratification, and all compressibility-mediated phenomena are axiomatically absent.

### F2. Nonlocal Momentum Transfer Without Pressure Mediation

**Axiom source:** NS-2 (Locality), NS-6 (Incompressibility).

The only nonlocal coupling in the architecture is mediated by the pressure Poisson equation. Any mechanism by which momentum at point x is directly influenced by the velocity at a distant point y — without passing through the pressure field — is forbidden. In particular:

- Integral operators on **u** (convolution kernels, fractional Laplacians, Boltzmann collision integrals) are outside the architecture.
- Long-range body forces that depend on the velocity field itself (e.g., self-gravitating fluids where **f** = **f**[**u**]) are outside the architecture unless **f** is treated as externally prescribed.

Pressure is the *sole nonlocal messenger*. All information about distant flow conditions reaches a given point through, and only through, the pressure gradient.

### F3. Non-Newtonian Stress Response

**Axiom source:** NS-3 (Newtonian Constitutive Law).

The deviatoric stress is axiomatically fixed at tau_ij = 2 mu S_ij. The following stress responses are forbidden:

- **Shear-thinning/thickening:** tau = mu(|S|) S, where viscosity depends on strain rate magnitude.
- **Viscoelasticity:** Stress with memory, tau(t) = integral K(t - s) S(s) ds, or upper-convected Maxwell models.
- **Yield stress (Bingham):** tau = tau_0 + mu S for |tau| > tau_0, rigid below yield.
- **Rate-type models:** Oldroyd-B, FENE-P, Giesekus, and all models with a separate stress evolution equation.

The architecture commits to a single scalar parameter mu governing all viscous response. No strain-rate dependence, no memory, no yield.

### F4. Anisotropic Viscosity

**Axiom source:** NS-4 (Isotropy).

The viscous operator nu Delta **u** treats all spatial directions identically. The following are forbidden:

- Direction-dependent viscosity tensors: nu_ijkl S_kl with nu_ijkl ≠ nu (delta_ik delta_jl + delta_il delta_jk).
- Preferred-direction diffusion (e.g., enhanced dissipation along a magnetic field line in MHD).
- Stratified viscosity models where nu depends on orientation relative to gravity or a boundary.

The architecture's viscous channel is a *scalar Laplacian*. It cannot encode any structural anisotropy.

### F5. Density Variation

**Axiom source:** NS-6 (Incompressibility), NS-5 (Conservation).

Under the incompressible assumption with rho = const, the following are forbidden:

- Buoyancy-driven flows where density varies spatially (Boussinesq approximation requires an additional equation for density or temperature — it extends the architecture).
- Stratified fluids with rho = rho(z).
- Multiphase flows with density jumps across interfaces.
- Variable-density mixing (rho = rho(x, t) satisfying a transport equation).

The architecture carries exactly one density value, globally and for all time.

### F6. Curved or Non-Euclidean Domains (Intrinsic Curvature)

**Axiom source:** NS-8 (Euclidean Ambient Space).

The equations are formulated with the flat-space Laplacian and the standard gradient. The following are forbidden:

- Navier–Stokes on Riemannian manifolds (where the Laplacian is the Laplace–Beltrami operator and the advection term involves covariant derivatives).
- General-relativistic fluid dynamics.
- Flows on the surface of a sphere treated as an intrinsically curved 2-manifold.

The architecture assumes R^d with the Euclidean metric. Boundaries with arbitrary shape are permitted (as subsets of R^d), but the *ambient space itself* carries no curvature.

### F7. Stochastic or Singular Forcing

**Axiom source:** NS-7 (Smooth Forcing).

The forcing **f**(x, t) is assumed smooth (or sufficiently regular). The following are forbidden within the strict architecture:

- White-noise-in-time forcing (stochastic NS, requiring Ito calculus and a different solution concept).
- Delta-function forcing (point sources of momentum).
- Forcing with spatial singularities stronger than what the regularity theory can absorb.

The forcing channel accepts smooth inputs only. Stochastic extensions and distributional forcing extend the architecture beyond its axioms.

### F8. Vacuum or Zero-Viscosity Limit as an Admissible State

**Axiom source:** NS-3 (Newtonian Constitutive Law), architecture requires nu > 0.

The Euler equations (nu = 0) are the formal inviscid limit of Navier–Stokes, but within the NS architecture as defined, nu > 0 is a fixed parameter. The inviscid limit is a *different architecture* — it removes the diffusion channel entirely, changes the PDE type from parabolic to hyperbolic, and eliminates the regularizing mechanism. The NS envelope is defined for strictly positive viscosity.

### Summary of Forbidden Configurations

| Label | Forbidden Configuration            | Excluding Axiom(s)     |
|-------|-------------------------------------|------------------------|
| F1    | Compressible velocity fields        | NS-6                   |
| F2    | Non-pressure-mediated nonlocality   | NS-2, NS-6             |
| F3    | Non-Newtonian stress                | NS-3                   |
| F4    | Anisotropic viscosity               | NS-4                   |
| F5    | Density variation                   | NS-5, NS-6             |
| F6    | Curved ambient space                | NS-8                   |
| F7    | Stochastic/singular forcing         | NS-7                   |
| F8    | Zero viscosity (Euler limit)        | NS-3 (nu > 0 required) |

---

## 2. Necessary Configurations

A *necessary configuration* is a structure that every admissible NS system *must* exhibit — not by choice, but by axiomatic compulsion. These are the structural consequences that the axioms force into existence.

### N1. Divergence-Free Velocity Field (Permanent Constraint)

**Source:** NS-6.

Every admissible velocity field satisfies div(**u**) = 0 at every point and every time. This is not a tendency or an approximation — it is an exact, instantaneous, permanent kinematic constraint. The space of admissible states is the infinite-dimensional submanifold V of divergence-free fields in H^1(Omega; R^d).

### N2. Pressure as Lagrange Multiplier

**Source:** NS-5 + NS-6.

The incompressibility constraint, combined with momentum conservation, *forces* the existence of a scalar field p satisfying the pressure Poisson equation:

    Delta p = -partial_i partial_j (u_i u_j) + div(**f**)

This is not an independent equation added by hand — it is a *necessary consequence* of applying the divergence operator to the momentum equation and imposing div(**u**) = 0. The pressure is axiomatically determined (up to a constant) by the velocity field and the forcing. It has no independent dynamics, no equation of state, and no thermodynamic content.

### N3. Quadratic Self-Advection

**Source:** NS-5 (Conservation) + NS-2 (Locality).

The requirement that momentum be conserved locally, combined with the restriction to differential (local) interactions, forces the advection term to take the form (**u** . nabla)**u** — a *quadratic* nonlinearity. This is not a modeling choice; it is the unique expression of local momentum transport by a velocity field transporting itself. The quadratic structure is architecturally necessary: linear advection would fail to conserve momentum, and higher-order nonlinearities would violate the constitutive assumptions.

### N4. Linear Isotropic Viscous Dissipation

**Source:** NS-3 + NS-4.

The Newtonian constitutive law and isotropy together force the viscous term to be exactly nu Delta **u** (for incompressible flow where div(**u**) = 0, the second viscosity drops out). The viscous operator is:

- Linear in **u** (forced by NS-3).
- Second-order in spatial derivatives (forced by the constitutive law relating stress to strain rate, which involves first derivatives of **u**; divergence of stress then involves second derivatives).
- Isotropic (forced by NS-4): the scalar Laplacian, not a tensorial or directional diffusion.

No other viscous operator is consistent with the axioms.

### N5. Energy Dissipation

**Source:** NS-3 + NS-4 + NS-5 + NS-6.

Taking the L^2 inner product of the momentum equation with **u** and integrating over Omega yields the energy identity:

    d/dt (1/2) integral |**u**|^2 dx = -nu integral |nabla **u**|^2 dx + integral **f** . **u** dx

The first term on the right is the *viscous dissipation rate* epsilon = nu ||nabla **u**||^2, which is non-negative. In the absence of forcing (**f** = 0), kinetic energy is strictly monotone decreasing unless **u** = 0. This is a *necessary* consequence of the axioms — any admissible NS evolution dissipates energy through the viscous channel.

The advection and pressure terms vanish identically from the energy equation:
- Advection: integral (**u** . nabla)**u** . **u** dx = 0 (for div(**u**) = 0, by integration by parts).
- Pressure: integral nabla p . **u** dx = 0 (for div(**u**) = 0, by the divergence theorem).

These cancellations are *structurally necessary*, not accidental.

### N6. Galilean Invariance

**Source:** NS-2 (Locality) + NS-8 (Euclidean Space) + NS-5 (Conservation).

The NS equations are invariant under Galilean boosts: if **u**(x, t) solves NS with pressure p(x, t), then **u**'(x', t) = **u**(x' - **V**t, t) - **V** solves NS with pressure p'(x', t) = p(x' - **V**t, t), for any constant velocity **V**. This invariance is forced by the axioms: the equations involve only derivatives of **u** and p, and the Euclidean structure admits uniform translations. Galilean invariance is a *necessary symmetry* of the architecture.

### N7. Vorticity Transport (Derived Necessary Structure)

**Source:** All axioms combined.

Taking the curl of the momentum equation yields the vorticity equation (omega = curl **u**):

    partial_t omega + (**u** . nabla)omega = (omega . nabla)**u** + nu Delta omega + curl **f**    [3D]
    partial_t omega + (**u** . nabla)omega = nu Delta omega + curl **f**                           [2D]

This is not an independent equation — it is a *derived necessary consequence* of the NS architecture. The vortex stretching term (omega . nabla)**u** in 3D is forced by the three-dimensionality of the curl and the quadratic advection. In 2D it vanishes identically (omega is a scalar, and there is no stretching direction). The 2D/3D asymmetry in the vorticity equation is an architectural consequence, not a modeling choice.

### N8. Leray Projection Structure

**Source:** NS-5 + NS-6.

The Helmholtz–Leray decomposition of L^2(Omega; R^d) into divergence-free fields and gradient fields is a necessary structural feature. Every vector field **v** in L^2 decomposes uniquely as **v** = P**v** + nabla phi, where P is the Leray projector. The NS evolution lives entirely in the range of P. This projection structure is forced by the combination of conservation and incompressibility — the architecture has no choice but to evolve on a constrained submanifold, and the Leray projector is the unique orthogonal projection onto that submanifold.

### Summary of Necessary Configurations

| Label | Necessary Configuration                 | Forcing Axiom(s)         |
|-------|-----------------------------------------|--------------------------|
| N1    | Divergence-free velocity field          | NS-6                     |
| N2    | Pressure as Lagrange multiplier         | NS-5, NS-6               |
| N3    | Quadratic self-advection                | NS-2, NS-5               |
| N4    | Linear isotropic viscous dissipation    | NS-3, NS-4               |
| N5    | Energy dissipation                      | NS-3, NS-4, NS-5, NS-6  |
| N6    | Galilean invariance                     | NS-2, NS-5, NS-8         |
| N7    | Vorticity transport equation            | All                       |
| N8    | Leray projection structure              | NS-5, NS-6               |

---

## 3. Extremal Bounds

The forbidden and necessary configurations define the *qualitative* boundary of the envelope. The *extremal bounds* sharpen this boundary into quantitative inequalities — the tightest constraints that the axioms impose on the magnitudes and rates of all dynamical quantities.

### E-Bound 1: Energy Inequality (Global)

For any Leray–Hopf weak solution on R^d or a bounded domain with no-slip conditions:

    (1/2)||**u**(t)||_{L^2}^2 + nu integral_0^t ||nabla **u**(s)||_{L^2}^2 ds
        <= (1/2)||**u**_0||_{L^2}^2 + integral_0^t integral **f** . **u** dx ds

This is the *fundamental energy inequality* of the NS architecture. It states that kinetic energy at time t, plus all energy dissipated up to time t, cannot exceed the initial energy plus the total work done by forcing. For strong (smooth) solutions, this is an *equality*. For weak solutions, the inequality is one-sided: energy may be lost (anomalous dissipation) but never spontaneously gained.

**Sharpness:** The inequality is saturated by smooth solutions. It is strict (with a gap) only if the solution develops singularities where energy is dissipated without being captured by the classical viscous term — a phenomenon that, if it occurs, signals the boundary of the architecture's self-consistency.

### E-Bound 2: Enstrophy Inequality (2D)

In two dimensions, the enstrophy Omega(t) = (1/2)||omega(t)||_{L^2}^2 satisfies:

    d/dt Omega(t) = -nu ||nabla omega||_{L^2}^2 + integral (curl **f**) . omega dx

In 2D, the vortex stretching term vanishes, so enstrophy is monotone decreasing in the absence of forcing. This yields the *a priori* bound:

    ||omega(t)||_{L^2} <= ||omega_0||_{L^2} + (1/nu) integral_0^t ||curl **f**(s)||_{L^2} ds

This bound is *exclusive to 2D*. It is the structural reason why 2D Navier–Stokes has global regularity: enstrophy control implies velocity gradient control, which closes the bootstrap.

### E-Bound 3: Enstrophy Balance (3D) — The Open Envelope

In three dimensions, the enstrophy equation acquires the vortex stretching term:

    d/dt (1/2)||omega||_{L^2}^2 = integral (omega . nabla)**u** . omega dx - nu ||nabla omega||_{L^2}^2 + integral (curl **f**) . omega dx

The stretching term integral (omega . nabla)**u** . omega dx has no definite sign. Using Holder and Sobolev inequalities, the best available estimate is:

    |integral (omega . nabla)**u** . omega dx| <= C ||omega||_{L^2}^{1/2} ||nabla omega||_{L^2}^{3/2} ||omega||_{L^2}    [by Ladyzhenskaya-type]

or schematically:

    d/dt Omega <= C Omega^{3/2} / nu^{1/2} - nu ||nabla omega||^2 + forcing terms

The cubic growth rate on the right-hand side *cannot be controlled* by the quadratic dissipation for all time, using currently known estimates. This is the structural signature of the 3D regularity problem: the NS envelope in 3D does not close. The axioms imply enstrophy balance but do not exclude finite-time enstrophy blowup.

**This is the central open boundary of the NS envelope.**

### E-Bound 4: Pressure Estimates

The pressure satisfies the Poisson equation Delta p = -partial_i partial_j(u_i u_j), from which Calderon–Zygmund theory yields:

    ||p||_{L^q} <= C_q ||**u**||_{L^{2q}}^2    for 1 < q < infinity

and

    ||nabla p||_{L^q} <= C_q ||**u** (x) nabla **u**||_{L^q}

Pressure is controlled by the velocity field, but with a *loss*: the pressure norm involves a higher power of the velocity than does the velocity norm itself. This loss is architecturally necessary — the pressure Poisson equation introduces exactly one derivative's worth of loss in the Sobolev scale.

### E-Bound 5: Maximum Principle Failure

Unlike the scalar heat equation (partial_t theta = nu Delta theta), the Navier–Stokes system does *not* satisfy a maximum principle for the velocity. The advection term and the pressure gradient can amplify velocity locally. Specifically:

    sup_{x,t} |**u**(x,t)| is NOT bounded by sup_x |**u**_0(x)| in general.

This failure is axiomatic: the quadratic advection and the nonlocal pressure projection are both capable of concentrating velocity, and no structural mechanism within the architecture prevents this concentration. In 3D, this failure is intimately connected to the possibility of finite-time blowup.

**The maximum principle failure is a structural feature, not a bug.** The architecture permits velocity amplification because the advection channel redistributes kinetic energy across scales without dissipating it, and the pressure channel adjusts nonlocally.

### E-Bound 6: Vortex Stretching Bound (3D)

The vortex stretching term (omega . nabla)**u** can be bounded in terms of the strain rate tensor S:

    |(omega . nabla)**u**| = |omega . S . hat{omega}| * |omega| <= |lambda_max(S)| * |omega|^2

where lambda_max(S) is the largest eigenvalue of the strain rate tensor. This yields:

    d/dt |omega|^2 <= 2 |lambda_max(S)| |omega|^2 + dissipation + forcing

along a material trajectory (neglecting diffusion). The exponential growth rate |lambda_max(S)| is not bounded *a priori* in 3D. The architecture permits, but does not require, superexponential vorticity growth.

### E-Bound 7: Serrin-Type Conditional Regularity

The axioms, combined with standard functional analysis, yield the following conditional result: if a weak solution satisfies

    **u** in L^q(0, T; L^p(R^3))    with   2/q + 3/p <= 1,   p > 3

then the solution is smooth on (0, T]. This is a *conditional envelope bound*: the architecture guarantees regularity whenever the velocity is controlled in a sufficiently strong space-time norm. The open question is whether the architecture's own dynamics can push the solution outside this controlled region.

### E-Bound 8: Decay Estimates (Unforced Case)

For **f** = 0 on R^d, the energy inequality implies:

    ||**u**(t)||_{L^2}^2 <= ||**u**_0||_{L^2}^2

and via Fourier splitting (Schonbek, Wiegner):

    ||**u**(t)||_{L^2} = O(t^{-(d/4)})    as t -> infinity

for initial data in L^1 intersection L^2. The architecture guarantees that unforced flows decay — viscosity wins in the long run. The decay rate t^{-d/4} is sharp.

### E-Bound 9: Dimensional Scaling (Criticality)

The NS equations are invariant under the scaling:

    **u**_lambda(x, t) = lambda **u**(lambda x, lambda^2 t),   p_lambda(x, t) = lambda^2 p(lambda x, lambda^2 t)

The critical (scale-invariant) space is L^d(R^d) for the velocity. In 3D, this is L^3(R^3). The energy space L^2 is *subcritical* (d = 2) or *supercritical* (d = 3) relative to the scaling:

- d = 2: ||**u**_lambda||_{L^2} = ||**u**||_{L^2} * lambda^{2/2 - 1} = ||**u**||_{L^2}  → critical (borderline).
- d = 3: ||**u**_lambda||_{L^2} = ||**u**||_{L^2} * lambda^{3/2 - 1} = ||**u**||_{L^2} * lambda^{1/2} → supercritical.

The supercriticality of the energy space in 3D is the *dimensional origin* of the regularity problem: energy control alone does not control the scaling-critical norm, leaving a gap through which singularities might pass.

---

## 4. Structural Invariants

A *structural invariant* is a quantity or relation that holds for *every* admissible NS evolution, regardless of initial data, forcing, domain, or Reynolds number. Invariants define the skeleton of the envelope — the relationships that cannot be broken without breaking the architecture.

### I1. Incompressibility Preservation

If div(**u**_0) = 0, then div(**u**(t)) = 0 for all t in the interval of existence.

**Proof sketch:** Apply div to the momentum equation. By NS-6 and the pressure Poisson equation, div(partial_t **u**) = 0, so the divergence-free condition is propagated exactly.

This is the most fundamental structural invariant: the constraint surface is *invariant under the flow*.

### I2. Energy Balance (Exact, for Smooth Solutions)

    d/dt E(t) = -epsilon(t) + P_f(t)

where E(t) = (1/2)||**u**||^2 is kinetic energy, epsilon(t) = nu||nabla **u**||^2 is viscous dissipation, and P_f(t) = integral **f** . **u** dx is the power input from forcing. This is an exact identity, not an inequality, for smooth solutions.

### I3. Helicity Invariance (Inviscid Limit, 3D)

The helicity H = integral **u** . omega dx is conserved by the Euler equations (nu = 0, **f** = 0) in 3D:

    d/dt H = 0    [Euler, 3D]

For Navier–Stokes with nu > 0:

    d/dt H = -2 nu integral omega . (nabla x omega) dx + forcing terms

Helicity is *not* an exact invariant of viscous NS, but it is a *structural invariant of the inviscid limit*. Its near-conservation at high Reynolds numbers is an architectural feature — the advection channel alone preserves helicity; only the diffusion channel destroys it.

### I4. Circulation Theorem (Kelvin, Inviscid Limit)

For the Euler equations, the circulation Gamma = oint_C **u** . d**l** around any material curve C is conserved. For NS:

    d/dt Gamma = nu oint_C Delta **u** . d**l** + oint_C **f** . d**l**

Viscosity and forcing modify circulation; incompressibility and advection alone preserve it. This is the integral form of the vorticity equation and an architectural invariant of the conservative (inviscid) subsystem.

### I5. Galilean Invariance

The NS equations are invariant under **u** -> **u** - **V**, x -> x - **V**t for constant **V**. This is a *symmetry invariant*: no admissible NS evolution can distinguish between inertial frames. The physical content is that only *relative* velocities matter, never absolute ones.

### I6. Scaling Symmetry

The NS equations are invariant under the parabolic scaling **u** -> lambda **u**(lambda x, lambda^2 t), p -> lambda^2 p(lambda x, lambda^2 t). This symmetry is exact and structural. It implies that all dimensionless ratios (Reynolds number, Strouhal number, etc.) are the natural parameters of the architecture, and that solutions at different scales are related by explicit rescaling.

### I7. Pressure–Velocity Coupling

The relation Delta p = -partial_i partial_j (u_i u_j) holds at every instant. This is not a dynamical law — it is a *structural identity* linking pressure to velocity through the incompressibility constraint. The pressure is uniquely determined (up to a constant) by the velocity field at each instant. This coupling is an invariant of the architecture: it cannot be relaxed, modified, or turned off.

---

## 5. Minimal Inequality Set (The NS Envelope)

The envelope of the Navier–Stokes architecture is defined by the following irreducible set of inequalities. These are the minimal constraints that every admissible NS evolution must satisfy. They are labeled E1–E9 for reference in subsequent AD evaluation files.

---

**E1. Incompressibility (Hard Constraint)**

    div(**u**(x, t)) = 0    for all (x, t) in Omega x [0, T)

This is not an inequality but an *equality constraint* — the most rigid element of the envelope. It defines the admissible state space.

---

**E2. Energy Inequality**

    (1/2)||**u**(t)||^2 + nu integral_0^t ||nabla **u**(s)||^2 ds <= (1/2)||**u**_0||^2 + integral_0^t (f, u) ds

Holds for all Leray–Hopf weak solutions. Equality holds for smooth solutions. The gap (if any) measures anomalous dissipation.

---

**E3. Enstrophy Control (2D)**

    ||omega(t)||_{L^2}^2 <= ||omega_0||_{L^2}^2 + (2/nu) integral_0^t ||curl **f**||_{L^2}^2 ds    [d = 2]

This bound closes the regularity bootstrap in 2D. It has no 3D analogue.

---

**E4. Enstrophy Balance (3D, Open)**

    d/dt ||omega||^2 <= C ||omega||^3 / nu^{1/2} - nu ||nabla omega||^2 + forcing    [d = 3]

The cubic growth term is not dominated by quadratic dissipation for all time. **This inequality does not close.** It is the open boundary of the 3D envelope.

---

**E5. Pressure–Velocity Coupling**

    ||p||_{L^q} <= C_q ||**u**||_{L^{2q}}^2    for 1 < q < infinity

The pressure is controlled by the velocity in all L^q norms, but with a quadratic loss. This is architecturally sharp — the Poisson equation loses exactly one degree in the nonlinearity.

---

**E6. Serrin Conditional Regularity**

    **u** in L^q(0,T; L^p(R^3)),  2/q + 3/p <= 1,  p > 3   =>   **u** is smooth on (0, T]

The architecture guarantees regularity whenever the velocity is controlled in a scale-critical space-time norm. This defines a *conditional boundary* of the envelope: inside the Serrin class, the architecture is self-consistent; outside, it is unknown.

---

**E7. Decay Law (Unforced)**

    ||**u**(t)||_{L^2} <= C t^{-d/4}    for **u**_0 in L^1 ∩ L^2, **f** = 0

All unforced flows decay. Viscosity always wins asymptotically. The rate t^{-d/4} is dimensionally determined and sharp.

---

**E8. Scaling Criticality**

    ||**u**_lambda||_{L^d} = ||**u**||_{L^d}    (scale-invariant norm)

The critical Lebesgue space is L^d. In 3D:
- L^2 is supercritical (energy is too weak to control scaling).
- L^3 is critical (scale-invariant).
- L^p for p > 3 is subcritical (sufficient for regularity).

The envelope's dimensional structure is: *the architecture provides energy-level control (E2), but regularity requires critical-level control (E6), and the gap between them (E4) is the 3D open problem.*

---

**E9. Maximum Principle Failure**

    sup_{x in Omega} |**u**(x, t)| is NOT bounded by sup_x |**u**_0(x)| in general.

Unlike scalar parabolic equations, the NS system permits local velocity amplification through advection and pressure. This is a *negative envelope bound* — a statement about what the architecture does NOT guarantee. It delineates the outer boundary of the envelope by exclusion.

---

### Envelope Summary

The NS architectural envelope is defined by nine constraints (E1–E9) organized into three tiers:

**Tier 1 — Hard Constraints (always hold):**
- E1: Incompressibility (exact equality).
- E2: Energy inequality (always holds, equality for smooth solutions).
- E5: Pressure–velocity coupling (always holds).
- E7: Unforced decay (always holds).

**Tier 2 — Dimension-Dependent Closure:**
- E3: Enstrophy control closes the envelope in 2D → *global regularity*.
- E4: Enstrophy balance fails to close in 3D → *open problem*.
- E8: Scaling criticality explains the dimensional gap.

**Tier 3 — Conditional and Negative Bounds:**
- E6: Serrin regularity defines the conditional interior of the envelope.
- E9: Maximum principle failure defines the outer boundary by exclusion.

The architecture's central structural feature, viewed through Mode 1, is the **2D/3D asymmetry**: the same axioms produce a closed envelope in two dimensions and an open envelope in three dimensions. The vortex stretching term — which is architecturally necessary (N7) and present only in 3D — is the structural mechanism responsible for this asymmetry. The 3D regularity problem, in FS terms, is the question of whether the open inequality E4 can be closed by a deeper structural argument, or whether the architecture genuinely permits finite-time escape from its own envelope.

---

*End of Mode 1: Axiom → Envelope. Mode 2 (EXPBD triad analysis) will follow in a subsequent file.*
