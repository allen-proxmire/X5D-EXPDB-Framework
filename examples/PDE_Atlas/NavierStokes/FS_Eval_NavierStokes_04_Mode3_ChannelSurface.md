# AD Evaluation: Navier–Stokes Equations — Mode 3: Channels → Constraint Surface

Allen Proxmire

April 2026

---

## Overview

Mode 3 of the AD evaluation constructs the *constraint surface* — the geometric object in channel space that encodes all structural relationships among the NS channels. Where Mode 1 identified the envelope (what is permitted) and Mode 2 identified the extremal dynamics (what the PDE does at its limits), Mode 3 asks: *what is the shape of the space in which the channels operate?*

The constraint surface is defined by the set of all simultaneously satisfiable channel states. It is the intersection of the hyperplanes, cones, and submanifolds imposed by the axioms, the PDE, and the universal inequalities. Every admissible NS evolution traces a trajectory *on* this surface. The surface's geometry — its dimension, its boundaries, its singular loci — determines which channel combinations are possible and which are forbidden.

We continue with the notation established in Modes 1–2:

    partial_t **u** = -(**u** . nabla)**u** - nabla p + nu Delta **u** + **f**
                    =     -A(**u**)       + P(**u**)  +   V(**u**)   + F
    subject to C: div(**u**) = 0

---

## 1. Channel Decomposition

The Navier–Stokes PDE decomposes into five channels, each with a definite structural character. We tabulate each channel's properties along four axes: locality, linearity, energy role, and scale action.

### Channel A: Advection

    A(**u**) = (**u** . nabla)**u**

- **Locality:** Local. A depends only on **u** and its first spatial derivatives at each point.
- **Linearity:** Quadratic nonlinear. A is bilinear in **u**: A(**u**) = B(**u**, **u**) where B(**v**, **w**) = (**v** . nabla)**w**.
- **Energy role:** Conservative (null). The advection term does zero net work on **u** in L^2:

      (A(**u**), **u**) = integral (**u** . nabla)**u** . **u** dx = 0    [for div(**u**) = 0]

  Advection redistributes energy across space and across Fourier modes, but creates and destroys none.

- **Scale action:** Transfers energy between scales via triadic interactions in Fourier space. In 3D, the net transfer is *forward* (large scales → small scales); in 2D, energy transfers *inversely* (small → large) while enstrophy transfers forward. The advection channel is the architecture's *mixer* — it stirs without heating.

### Channel V: Viscosity / Diffusion

    V(**u**) = nu Delta **u**

- **Locality:** Local. V depends on **u** and its second spatial derivatives at each point.
- **Linearity:** Linear. V is a bounded linear operator on appropriate Sobolev spaces.
- **Energy role:** Dissipative. V removes energy at rate epsilon(t) = nu ||nabla **u**||^2 >= 0.

      (V(**u**), **u**) = nu (Delta **u**, **u**) = -nu ||nabla **u**||^2 <= 0

  V is the architecture's sole energy sink.

- **Scale action:** Preferentially damps small scales. In Fourier space, V acts as multiplication by -nu |k|^2. The damping rate grows quadratically with wavenumber: mode k decays at rate nu k^2. The viscous channel is a *low-pass filter* — it removes high-frequency content and smooths the velocity field.

### Channel P: Pressure Projection

    P(**u**) = -nabla p,    where Delta p = -partial_i partial_j (u_i u_j) + div(**f**)

- **Locality:** Nonlocal. The pressure at point x depends on the velocity field over the *entire* domain Omega, mediated by the elliptic Green's function of the Laplacian:

      p(x) = integral G(x, y) [-partial_i partial_j (u_i u_j)(y) + div **f**(y)] dy

  A local perturbation of **u** at any point y produces an instantaneous pressure response at every point x. The Green's function G(x,y) decays as |x-y|^{2-d} — algebraically, not exponentially — so the coupling is *long-range*.

- **Linearity:** Nonlinear in **u** (quadratic, through the source term u_i u_j), but *linear as an operator on its source*. Given the right-hand side, the Poisson solve is linear. The nonlinearity enters through the coupling to the velocity field.

- **Energy role:** Conservative (null). Pressure does no work on an incompressible field:

      (P(**u**), **u**) = -(nabla p, **u**) = integral p (div **u**) dx = 0

  Like advection, pressure is energy-invisible. It is a *constraint enforcer*, not a dynamical agent.

- **Scale action:** All-scale coupling. The Poisson equation couples every wavenumber to every other (through the nonlinear source term). In Fourier space, the Leray projector P_k = I - k k^T / |k|^2 acts on each mode, but the source term u_i u_j produces convolutions that mix all modes. Pressure transmits information across the full spectrum instantaneously.

### Channel F: Forcing

    F = **f**(x, t)

- **Locality:** Local (the forcing is a prescribed function of space and time; its value at x does not depend on the solution at other points).
- **Linearity:** External (not a function of **u** at all). F is a prescribed input, not an operator on the state.
- **Energy role:** Source. F injects energy at rate P_f(t) = (**f**, **u**):

      (F, **u**) = integral **f** . **u** dx = P_f(t)

  The sign of P_f is not determined *a priori* — forcing can inject or extract energy depending on its alignment with the velocity field. But for sustained forcing (e.g., time-independent or statistically stationary), the long-time average of P_f is positive, balancing the time-averaged dissipation.

- **Scale action:** Scale-selective, determined by the spatial structure of **f**. If **f** is concentrated at large scales (low wavenumbers), energy is injected at those scales and must cascade through the advection channel to reach the dissipation range. The forcing scale L_f = 2 pi / k_f is an external parameter that sets the top of the inertial range.

### Channel C: Incompressibility Constraint

    C: div(**u**) = 0

- **Locality:** This constraint is *local* as a differential equation (it involves only first derivatives of **u** at each point), but its *enforcement* is nonlocal (through the pressure Poisson equation). The constraint is a local condition with a global enforcement mechanism.
- **Linearity:** Linear in **u**.
- **Energy role:** Constraint (neither creates, destroys, nor redistributes energy). C restricts the state space but does not act as a force.
- **Scale action:** All-scale. The divergence-free condition applies at every wavenumber independently: hat{k} . hat{**u**}(k) = 0 for all k. Each Fourier mode is projected onto the plane perpendicular to its wavevector. This is a *mode-by-mode* constraint, but its enforcement (through P) couples all modes.

### Channel Summary Table

| Channel | Symbol | Locality  | Linearity        | Energy Role    | Scale Action           |
|---------|--------|-----------|------------------|----------------|------------------------|
| Advection  | A   | Local     | Quadratic nonlin.| Null (0 work)  | Cross-scale transfer   |
| Viscosity  | V   | Local     | Linear           | Dissipative    | Damps small scales     |
| Pressure   | P   | Nonlocal  | Quad. (in **u**) | Null (0 work)  | Couples all scales     |
| Forcing    | F   | Local     | External         | Source         | Injects at L_f         |
| Constraint | C   | Local/Global | Linear        | None           | All-scale restriction  |

---

## 2. Dissipation Partition

### 2.1 The Energy Simplex

The energy identity (Mode 2, Energy-I) can be written as a partition of the instantaneous energy change rate:

    dE/dt = W_A + W_V + W_P + W_F

where:
- W_A = -(A(**u**), **u**) = 0          (advection work)
- W_V = (V(**u**), **u**) = -epsilon     (viscous dissipation)
- W_P = (P(**u**), **u**) = 0            (pressure work)
- W_F = (F, **u**) = P_f                 (forcing power)

The partition lives on a *degenerate simplex*: two of the four channel contributions are identically zero for all admissible states.

### 2.2 The Null Edge

The channels A and P lie on the *null edge* of the energy simplex — the locus where a channel's contribution to the energy budget is identically zero. This is not a special case or a fine-tuning; it is an axiomatic identity:

**Advection null identity:** ((**u** . nabla)**u**, **u**) = 0 for all divergence-free **u** with appropriate boundary conditions. This follows from the skew-symmetry of the advection operator in the incompressible setting.

**Pressure null identity:** (nabla p, **u**) = 0 for all divergence-free **u**. This follows from the definition of the Leray projection: nabla p is the gradient (irrotational) component of the unconstrained tendency, and is L^2-orthogonal to the divergence-free subspace.

The null edge is a *structural feature*, not a dynamical accident. Both identities are algebraic consequences of the incompressibility axiom (NS-6). If incompressibility were relaxed (compressible NS), both identities would fail: advection would do pressure-volume work, and the pressure gradient would do compressive work.

**Consequence:** The energy partition is effectively one-dimensional:

    dE/dt = -epsilon + P_f

Energy accounting in NS is a two-body problem: dissipation vs. forcing. All of the nonlinear complexity (turbulence, cascade, mixing, vortex dynamics) produced by the advection and pressure channels is *energetically silent*. The architecture's most complex channels are invisible in its primary accounting.

### 2.3 The Enstrophy Simplex

At the enstrophy level, the partition is richer. The enstrophy equation (Mode 2, Enst-3D) partitions as:

    d Omega/dt = S + D_omega + F_omega

where:
- S = integral omega . S . omega dx       (stretching production, 3D only)
- D_omega = -nu ||nabla omega||^2          (enstrophy dissipation)
- F_omega = integral (curl **f**) . omega dx  (enstrophy forcing)

In 3D, the stretching term S is the contribution of the advection sub-channel A_stretch (see Section 4). It has *no definite sign* and can be positive (enstrophy production) or negative (enstrophy destruction). The enstrophy simplex in 3D is therefore *two-dimensional*: the stretching-dissipation-forcing triangle has an interior, and the dynamics can visit any point in it.

In 2D, S = 0 identically, and the enstrophy simplex collapses to the same one-dimensional structure as the energy simplex: dissipation vs. forcing.

### 2.4 Contrast with ED's Dissipation Partition

In the FS/ED framework, the dissipation partition is *fully populated*: all channels contribute to the accounting. The coverage-escape-activation partition distributes prime mass across three non-degenerate channels, each carrying a positive fraction of the total. The ED dissipation simplex is a genuine 2-simplex (triangle) with all three vertices occupied.

In NS:
- The *energy* simplex is degenerate: two channels (A, P) are null, reducing it to a line segment between dissipation and forcing.
- The *enstrophy* simplex (3D) is a genuine 2-simplex: stretching, dissipation, and forcing occupy the three vertices.
- The *enstrophy* simplex (2D) collapses to a line segment (same degeneracy as the energy simplex).

The architectural lesson: NS hides its complexity below the primary accounting level. The energy budget looks trivially simple (one-dimensional), but the enstrophy budget (in 3D) reveals the nontrivial structure. ED's architecture, by contrast, reveals its full complexity at the primary level.

---

## 3. Constraint Surface and Universality Classes

The constraint surface of the NS architecture is parameterized by the activity levels of the five channels. Different regions of this surface correspond to qualitatively different dynamical regimes — *universality classes* in the FS sense.

### Class I: Stokes Flow (V + P + C; A inactive)

**Active channels:** V, P, C.
**Inactive channels:** A, F (or F present but subordinate).
**Governing equation:**

    partial_t **u** = -nabla p + nu Delta **u** + **f**,    div(**u**) = 0

The advection term is dropped (formally: Re → 0). This is the *linear* limit of NS.

**Properties:**
- The PDE is linear, parabolic, and globally well-posed in any dimension.
- All solutions are smooth for all time, for any initial data.
- The energy equation is unchanged (A was energy-null anyway).
- The enstrophy equation is unchanged in its closing structure (S was the only problematic term).
- Vortex stretching is absent (it is part of A).
- The pressure Poisson equation becomes linear: Delta p = div **f**.
- The Stokes operator -P Delta is self-adjoint, positive definite, and its eigenfunctions form a complete basis for the divergence-free subspace.

**Universality inequalities:** U1, U2, U5, U6, U7, U8 all hold. U3 (BKM) and U4 (Serrin) are vacuous (regularity is unconditional). U9 (stretching gate) is vacuous (no stretching).

**Extremal behaviors:** No blowup channels. No cascade. No turbulence. All solutions decay exponentially to a steady state (if **f** is time-independent) or track the forcing smoothly.

### Class II: Euler Flow (A + P + C; V inactive)

**Active channels:** A, P, C.
**Inactive channels:** V, F (or F subordinate).
**Governing equation:**

    partial_t **u** + (**u** . nabla)**u** = -nabla p,    div(**u**) = 0

The viscous term is dropped (nu = 0). This is the *inviscid* limit.

**Properties:**
- The PDE is nonlinear, hyperbolic (in a generalized sense), and *not* globally well-posed in 3D.
- Energy is exactly conserved (for smooth solutions): dE/dt = 0.
- Enstrophy is exactly conserved in 2D (for smooth solutions): d Omega/dt = 0.
- In 3D, the enstrophy equation retains the stretching term, and enstrophy can grow without bound: d Omega/dt = S(t). There is no dissipative counterbalance.
- Vortex stretching is present in 3D and is the *sole* mechanism for enstrophy change.
- The pressure is still nonlocal and enforces incompressibility.

**Universality inequalities:** U1 becomes an equality (energy conservation). U2 becomes an equality in 2D (enstrophy conservation). U3 (BKM) holds and is the *only* regularity criterion. U5 (Ladyzhenskaya) holds. U6 and U7 are irrelevant (no dissipation). U9 (stretching gate) holds with the dissipation term set to zero — the gate has no viscous counterweight.

**Extremal behaviors:**
- 3D finite-time blowup is *expected* (Euler blowup is widely believed, and recent numerical evidence supports it for specific initial data).
- 2D: global regularity holds (Yudovich theorem: bounded initial vorticity implies unique global solutions).
- No dissipation range. No cascade to dissipation. Energy redistribution without sink.

### Class III: Forced-Dissipative Turbulence (A + V + P + F + C; all active)

**Active channels:** All five.
**Governing equation:** Full NS.

    partial_t **u** + (**u** . nabla)**u** = -nabla p + nu Delta **u** + **f**,    div(**u**) = 0

This is the generic regime at high Reynolds number with sustained forcing.

**Properties:**
- All five channels are active and interacting.
- Energy is injected by F, redistributed by A, and dissipated by V.
- The inertial range exists between the forcing scale and the dissipation scale.
- In 3D, vortex stretching is active and competes with viscous damping.
- In 2D, the dual cascade (inverse energy, forward enstrophy) operates.
- Pressure couples all scales nonlocally.
- Statistical steady states (turbulence) emerge when the time-averaged forcing power equals the time-averaged dissipation: <P_f> = <epsilon>.

**Sub-class III-a: 2D Forced-Dissipative**
- All universality inequalities U1–U9 hold (U3, U4 are vacuous — regularity is unconditional).
- Global attractor exists with finite Hausdorff dimension.
- No blowup channels. Inverse energy cascade to large scales; forward enstrophy cascade.

**Sub-class III-b: 3D Forced-Dissipative**
- All universality inequalities U1–U9 hold.
- Global attractor existence is conditional on regularity.
- Blowup channels B1–B3 are structurally open.
- Forward energy cascade; Kolmogorov k^{-5/3} spectrum in the inertial range.

**Universality inequalities:** All U1–U9 apply.

**Extremal behaviors:** All behaviors identified in Mode 2, Sections 3.1–3.5, are accessible in this class.

### Class IV: Decaying Turbulence (A + V + P + C; F inactive)

**Active channels:** A, V, P, C.
**Inactive channels:** F.
**Governing equation:** Unforced NS.

**Properties:**
- Energy decays monotonically: dE/dt = -epsilon <= 0.
- All solutions decay to **u** = 0 as t → infinity.
- The decay rate is exponential on bounded domains (Poincare), algebraic on R^d.
- In 3D, transient singularities are structurally possible before eventual smoothing.
- No attractor other than the trivial fixed point **u** = 0.

**Universality inequalities:** U1, U2, U5, U6, U8, U9 apply. U7 (absorbing ball) gives the trivial ball {0}.

### Universality Class Summary

| Class | Channels          | Dimension | Regularity       | Attractor        | Cascade          |
|-------|-------------------|-----------|------------------|------------------|------------------|
| I     | V + P + C         | 2D, 3D   | Unconditional    | Steady state     | None             |
| II    | A + P + C         | 2D        | Unconditional    | None (conserv.)  | None (conserv.)  |
| II    | A + P + C         | 3D        | Open (likely no) | None             | Enstrophy growth |
| III-a | All               | 2D        | Unconditional    | Finite-dim.      | Dual cascade     |
| III-b | All               | 3D        | Open             | Open             | Forward cascade  |
| IV    | A + V + P + C     | 2D, 3D   | 2D: yes; 3D: open | {0}            | Decaying         |

---

## 4. Vortex Stretching as a Structural Anomaly

### 4.1 Sub-Channel Decomposition of Advection

The advection channel A can be decomposed into two structurally distinct sub-channels by examining its action on the vorticity field. Write the vorticity equation:

    partial_t omega + (**u** . nabla)omega = (omega . nabla)**u** + nu Delta omega + curl **f**

The advection contribution to the left-hand side is (**u** . nabla)omega, which is *transport* of vorticity by the flow. The term on the right, (omega . nabla)**u**, is generated by the curl of the advection term and represents *stretching and tilting* of vorticity by the velocity gradient. We define:

**A_transport:** The transport sub-channel. Moves vorticity (and velocity) from one spatial location to another, following the flow. In Fourier space, this is the component of the triadic interaction that shifts energy between modes without changing total enstrophy.

    A_transport: omega -> (**u** . nabla)omega

**A_stretch:** The stretching sub-channel. Amplifies or suppresses vorticity magnitude by aligning vortex lines with the strain field. This is the component that changes the *magnitude* of vorticity along material elements.

    A_stretch: omega -> (omega . nabla)**u**

### 4.2 Energy Properties of the Sub-Channels

Both A_transport and A_stretch are energy-neutral:

    (A(**u**), **u**) = (A_transport, **u**) + (A_stretch, **u**) = 0

This is guaranteed by the overall energy-null property of A (Section 1). The sub-channel decomposition respects the energy constraint — neither sub-channel does net energy work.

**Proof that the full advection term is energy-null remains as before.** The decomposition into sub-channels is a vorticity-level decomposition and does not alter the energy accounting.

### 4.3 Enstrophy Properties of the Sub-Channels

**A_transport:** Enstrophy-neutral in both 2D and 3D:

    integral [(**u** . nabla)omega] . omega dx = -(1/2) integral (div **u**) |omega|^2 dx = 0

The transport of vorticity by a divergence-free flow preserves enstrophy (by the same skew-symmetry argument as energy preservation by advection). Transport stirs vorticity without amplifying it.

**A_stretch:** Enstrophy-neutral in 2D, enstrophy-*active* in 3D:

- **2D:** The stretching term is identically zero. Omega is a scalar, and (omega . nabla)**u** = omega (partial_3 u_1, partial_3 u_2) — but there is no x_3 direction. The sub-channel does not exist.

- **3D:** The stretching term contributes:

      integral [(omega . nabla)**u**] . omega dx = integral omega_i S_ij omega_j dx = S(t)

  where S(t) is the stretching production from Mode 2 (Section 2.3). This quantity has no definite sign. It can be positive (enstrophy production, when omega aligns with extensional strain) or negative (enstrophy destruction, when omega aligns with compressional strain).

### 4.4 The Anomaly Statement

**Theorem (Structural Anomaly).** The sub-channel A_stretch is the unique architectural feature of the Navier–Stokes system with the following combined properties:

1. It is energy-neutral (does no work in the energy budget).
2. It is enstrophy-destabilizing (can produce enstrophy without bound in 3D).
3. It exists only in d >= 3 (identically absent in d = 2).
4. It is the sole mechanism that prevents the enstrophy inequality from closing in 3D.
5. Its removal (by restricting to 2D, or by imposing A_stretch = 0) immediately yields global regularity.

No other channel or sub-channel in the NS architecture has this combination of properties. The viscous channel V is energy-dissipative and always regularizing. The pressure channel P is energy-neutral but also enstrophy-neutral (pressure does no enstrophy work, since curl(nabla p) = 0). The forcing channel F is energy-active but structurally benign (smooth forcing cannot cause blowup). The constraint C restricts but does not destabilize.

**A_stretch is the architecture's singular point of vulnerability.** It is the unique channel through which the 3D NS system can potentially escape its own regularity constraints. In FS terms, it is a *structural anomaly*: a feature that is architecturally necessary (forced by the combination of 3D geometry, incompressibility, and quadratic advection) yet potentially destructive to the architecture's self-consistency.

### 4.5 Dimensional Origin of the Anomaly

The anomaly is ultimately dimensional. The curl of a vector field in R^d produces:

- d = 2: a scalar (one component). Vorticity has no direction to be stretched in.
- d = 3: a vector (three components). Vorticity can be stretched, tilted, and amplified by the velocity gradient.

The vorticity equation in d dimensions takes the form:

    partial_t omega + (**u** . nabla)omega = (omega . nabla)**u** - omega (div **u**) + nu Delta omega + curl **f**

The stretching term (omega . nabla)**u** involves the contraction of a d-vector (omega) with the d x d gradient matrix (nabla **u**). In 2D, this contraction yields a scalar times the identity — pure rotation, no stretching. In 3D, the contraction yields a genuine vector that can differ in both magnitude and direction from omega — stretching and tilting.

The incompressibility constraint div **u** = 0 imposes trace(nabla **u**) = 0, ensuring that the eigenvalues of the strain rate tensor sum to zero (lambda_1 + lambda_2 + lambda_3 = 0). This prevents isotropic expansion but permits uniaxial stretching (lambda_1 > 0, lambda_2 + lambda_3 < 0), which is the blowup mechanism. In 2D, trace-free strain means lambda_1 + lambda_2 = 0 — strain is pure shear, and vorticity is only rotated, never amplified.

---

## 5. Nonlocal Pressure Projection

### 5.1 The Pressure as a Nonlocal Operator

The pressure channel P is unique among NS channels in being *nonlocal*. We characterize its nonlocality precisely.

Given the velocity field **u** at time t, the pressure is determined by:

    Delta p = -partial_i partial_j (u_i u_j) + div **f**

with boundary conditions inherited from the domain geometry. The solution is:

    p(x) = integral_Omega G(x, y) Q(y) dy

where G is the Green's function of -Delta on Omega and Q = -partial_i partial_j (u_i u_j) + div **f** is the source. The Green's function satisfies:

    G(x, y) ~ c_d |x - y|^{2-d}    as |x - y| -> 0    [d >= 3]
    G(x, y) ~ -(1/(2pi)) log|x - y|                     [d = 2]

The *algebraic* decay of G (not exponential) means that the pressure response to a localized velocity perturbation extends to the entire domain with power-law decay. This is *genuine nonlocality* — not the pseudo-nonlocality of a finite-speed wave equation, but the instantaneous, infinite-speed coupling of an elliptic constraint.

### 5.2 Information Propagation

In the NS architecture, information propagates through two mechanisms:

1. **Advective transport:** Local, finite-speed (at most ||**u**||_{L^infinity}). A perturbation at x is carried along material trajectories at the local flow velocity.

2. **Pressure transmission:** Nonlocal, infinite-speed. A perturbation at x produces an instantaneous pressure response at every other point in the domain.

The pressure channel is the *faster* information channel — infinitely faster, in fact. This means that the incompressibility constraint is enforced *before* any local information can propagate. A local disturbance is immediately "known" globally through the pressure field.

**Physical interpretation:** The infinite propagation speed is a consequence of the incompressibility assumption (NS-6). In the compressible NS equations, pressure perturbations propagate at the speed of sound c_s. The incompressible limit corresponds to c_s → infinity, and the elliptic pressure equation is the limiting form of a hyperbolic wave equation in this limit.

### 5.3 Scale Coupling

The Leray projector P, which encodes the combined effect of pressure and incompressibility, acts in Fourier space as:

    [P hat{**u**}](k) = (I - k k^T / |k|^2) hat{**u**}(k)

This is *diagonal in Fourier space* — each mode is projected independently onto the plane perpendicular to k. However, the pressure's role in the *nonlinear* dynamics involves the projection of the advection term:

    P[(**u** . nabla)**u**] = (**u** . nabla)**u** + nabla p

The advection term, being quadratic, generates triadic interactions: modes k_1 and k_2 interact to produce a contribution at k = k_1 + k_2 (and k_1 - k_2). The Leray projection then acts on the result, modifying the triadic coupling coefficients. The net effect is that *pressure mediates the scale-to-scale energy transfer*. Without the projection, the triadic interactions would include compressive modes (longitudinal to k); the projection removes these, restricting transfer to transverse (solenoidal) modes.

Pressure thus plays a dual structural role:
1. It couples all spatial points (nonlocality in physical space).
2. It constrains the mode-to-mode transfer (anisotropy in Fourier space).

### 5.4 Contrast with ED Locality

In the FS/ED framework, all channels are *local*: the width, height, activation, coverage, and escape at integer n depend only on the factorization of n, not on the factorization of distant integers. The ED architecture has no elliptic constraint, no Green's function, and no mechanism for one integer's structure to influence another's.

The NS pressure channel introduces a qualitative departure from FS locality. In FS terms, the pressure is an *architectural halo* — a field that mediates global coupling without carrying dynamical energy. But unlike the ED halo (which is derived from local mobility), the NS pressure halo is derived from a *global constraint* (incompressibility) and has no local constitutive origin. This makes the NS architecture fundamentally less local than ED in the FS sense.

---

## 6. Channel Constraints

The following constraints define the *channel signature* of the Navier–Stokes architecture — the set of structural identities and inequalities that all admissible channel states must satisfy. They are labeled C1–C14.

---

**C1. Advection Energy Nullity**

    (A(**u**), **u**) = 0    for all **u** in V (divergence-free)

The advection channel does no net work in the energy budget. This is an *exact algebraic identity*, not an inequality.

---

**C2. Pressure Energy Nullity**

    (P(**u**), **u**) = (nabla p, **u**) = 0    for all **u** in V

The pressure channel does no net work in the energy budget. Combined with C1, this establishes the null edge of the energy simplex.

---

**C3. Viscous Dissipation Monopoly**

    All energy dissipation passes through V:    dE/dt + epsilon = P_f,    epsilon = nu ||nabla **u**||^2 >= 0

No other channel can dissipate energy. The viscous channel is the architecture's sole thermodynamic irreversibility.

---

**C4. Forcing Injection Monopoly**

    All energy injection passes through F:    P_f = (**f**, **u**)

No other channel can inject energy from outside the system. The forcing channel is the architecture's sole external input.

---

**C5. Advection Transport Enstrophy Nullity**

    integral [(**u** . nabla)omega] . omega dx = 0    for all **u** in V

The transport sub-channel of advection is enstrophy-neutral. Vorticity transport by a divergence-free flow preserves total enstrophy.

---

**C6. Vortex Stretching Dimensional Selection**

    A_stretch exists   iff   d >= 3   and   omega ≠ 0

The stretching sub-channel is absent in 2D (identically zero) and requires nonzero vorticity in 3D. This is a *dimensional selection rule*: the architecture's most dangerous sub-channel is activated only by the combination of three-dimensional geometry and nontrivial rotation.

---

**C7. 2D Enstrophy Closure**

    d = 2   =>   d Omega/dt <= -nu ||nabla omega||^2 + ||curl **f**|| ||omega||

In 2D, the enstrophy equation has no production term, and the enstrophy inequality closes. This constraint is the structural basis for 2D global regularity.

---

**C8. 3D Enstrophy Non-Closure**

    d = 3   =>   d Omega/dt = S(t) - nu ||nabla omega||^2 + F_omega

where |S(t)| can exceed nu ||nabla omega||^2 for large ||omega||. The enstrophy inequality does not close in 3D. This is a *structural non-closure* — a gap in the constraint surface through which the dynamics might escape.

---

**C9. Pressure Determination**

    p is uniquely determined (up to a constant) by **u** and **f** at each instant:
    Delta p = -partial_i partial_j(u_i u_j) + div **f**

The pressure channel carries no independent degrees of freedom. It is a *slave variable* — entirely determined by the velocity field and forcing through an elliptic equation.

---

**C10. Incompressibility Propagation**

    div(**u**_0) = 0   =>   div(**u**(t)) = 0   for all t in [0, T)

The incompressibility constraint, once satisfied by the initial data, is propagated exactly by the PDE. The constraint surface is *flow-invariant*.

---

**C11. Scaling Covariance**

    If (**u**, p) solves NS with forcing **f** and viscosity nu, then
    (lambda **u**(lambda x, lambda^2 t), lambda^2 p(lambda x, lambda^2 t))
    solves NS with forcing lambda^3 **f**(lambda x, lambda^2 t) and the same nu.

The channel structure is covariant under parabolic rescaling. This constraint implies that all channel relationships hold at every scale simultaneously.

---

**C12. Strain Trace Constraint**

    tr(S) = (1/2) tr(nabla **u** + (nabla **u**)^T) = div **u** = 0

The eigenvalues of the strain rate tensor sum to zero at every point. This is the pointwise consequence of incompressibility for the strain field. It restricts the geometry of vortex stretching: extension in one direction requires compression in the complementary directions.

---

**C13. BKM Regularity Gate**

    Smooth solution extends past T   iff   integral_0^T ||omega||_{L^infinity} dt < infinity

Regularity is controlled by a single channel-derived quantity: the time-integrated maximum vorticity. This is the architecture's *regularity gate* — the single checkpoint that the evolution must pass to remain smooth.

---

**C14. Pressure–Advection Locking**

    nabla p = -(I - P)[A(**u**) - F]

The pressure gradient is the irrotational (gradient) component of the unconstrained tendency. It is *locked* to the advection term: every change in advection produces an instantaneous, precisely canceling pressure adjustment to maintain incompressibility. This locking is the mechanism by which the nonlocal channel P tracks the local channel A.

---

### Channel Constraint Summary

| Label | Constraint                           | Type                | Scope     |
|-------|--------------------------------------|---------------------|-----------|
| C1    | Advection energy nullity             | Algebraic identity  | All       |
| C2    | Pressure energy nullity              | Algebraic identity  | All       |
| C3    | Viscous dissipation monopoly         | Structural          | All       |
| C4    | Forcing injection monopoly           | Structural          | All       |
| C5    | Transport enstrophy nullity          | Algebraic identity  | All       |
| C6    | Stretching dimensional selection     | Dimensional rule    | d >= 3    |
| C7    | 2D enstrophy closure                 | Inequality (closed) | d = 2     |
| C8    | 3D enstrophy non-closure             | Inequality (open)   | d = 3     |
| C9    | Pressure determination               | Elliptic identity   | All       |
| C10   | Incompressibility propagation        | Flow invariance     | All       |
| C11   | Scaling covariance                   | Symmetry            | All       |
| C12   | Strain trace constraint              | Pointwise identity  | All       |
| C13   | BKM regularity gate                  | Conditional         | d = 3     |
| C14   | Pressure–advection locking           | Structural coupling | All       |

---

## 7. Comparison with ED Mode 3

### 7.1 Locality

**ED:** All channels are local. The width, height, activation, coverage, and escape primitives at integer n are determined solely by the factorization of n. No integer's FS structure depends on any other integer's structure. The ED constraint surface is a product of local constraints — one per integer.

**NS:** Four of five channels (A, V, F, C) are local; one channel (P) is nonlocal. The pressure Poisson equation couples every point in the domain to every other point at every instant. The NS constraint surface is *not* a product of local constraints — it is a global surface defined by an elliptic PDE. This is the single deepest structural difference between ED and NS at the channel level.

### 7.2 Dissipation Partition

**ED:** The dissipation partition (coverage-escape-activation) is fully populated. All three channels carry a positive fraction of the prime mass at every scale. The partition simplex is a genuine 2-simplex with all vertices occupied and a nontrivial interior.

**NS:** The energy partition is degenerate — two channels (A, P) are energy-null, collapsing the simplex to a 1-simplex (line segment) between dissipation and forcing. The enstrophy partition in 3D is a genuine 2-simplex (stretching, dissipation, forcing), but in 2D it collapses again. NS hides its structural complexity below the primary (energy) level; ED displays it at the primary level.

### 7.3 Blowup Channel

**ED:** No blowup channel exists. Every ED quantity (prime counting functions, density functions, sieve errors, coverage fractions) is finite for any finite argument. The ED architecture is unconditionally self-consistent — its constraint surface has no open boundaries.

**NS:** The stretching sub-channel A_stretch opens a blowup gate in 3D (C8, C13). The 3D constraint surface has an *open boundary* in the enstrophy direction — a face through which the dynamics might escape. This open boundary is the geometric signature of the regularity problem. In 2D, the boundary closes (C7), and the surface is compact.

### 7.4 Halo Structure

**ED:** The ED "halo" — the probabilistic envelope surrounding each integer's expected coverage — is derived from *local mobility*: the probability that a prime p divides n depends only on the residue of n modulo p, which is a local property. The halo is a local object with local origins.

**NS:** The NS "halo" is the pressure field — the nonlocal envelope that mediates constraint enforcement. Unlike ED's halo, the NS pressure halo is derived from a *global constraint* (incompressibility), not from local constitutive behavior. It has no local origin: the pressure at a point is determined by the velocity field over the entire domain. The NS halo is irreducibly nonlocal.

### 7.5 Architectural Summary

| Feature                    | ED                         | NS                            |
|----------------------------|----------------------------|-------------------------------|
| Channel locality           | All local                  | P is nonlocal                 |
| Energy partition dimension | 2 (full 2-simplex)         | 0 (degenerate line)           |
| Secondary partition dim.   | N/A                        | 2 (3D enstrophy), 0 (2D)     |
| Constraint surface boundary| Closed (all faces compact) | Open face in 3D (enstrophy)   |
| Blowup gate                | None                       | A_stretch (3D only)           |
| Halo origin                | Local (residue classes)    | Global (elliptic constraint)  |
| Self-consistency           | Unconditional              | 2D: unconditional; 3D: open   |
| Regularity controller      | N/A (static)               | BKM (C13): ||omega||_{L^inf}  |

---

*End of Mode 3: Channels → Constraint Surface. The EXPBD triad analysis and structural diagnostics will follow in subsequent files.*
