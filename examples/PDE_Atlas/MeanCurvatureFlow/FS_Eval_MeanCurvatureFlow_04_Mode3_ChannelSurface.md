# AD Evaluation: Mean Curvature Flow — Mode 3: Channels → Constraint Surface

Allen Proxmire

April 2026

---

## Overview

Mode 3 constructs the constraint surface of the MCF architecture. The MCF constraint surface is *structurally unprecedented* in the PDE Atlas: it is the only surface that includes a *required singularity face* as part of its normal operation. In every other architecture, singularity (blowup) is either impossible (AC, CH, PME, FP), a parameter-dependent structural vulnerability (TFE for n < 1), an open question (NS in 3D), or a constitutive possibility (RD with super-linear kinetics). In MCF, singularity is *certain* for non-convex compact surfaces and is the mechanism by which the architecture achieves its goal of area minimization. The singularity face is not an anomaly to be sealed — it is a *structural feature* of the constraint surface.

We continue with:

    V_n = H    on Gamma_t

---

## 1. Channel Decomposition

### Channel K: Curvature (Geometric Diffusion)

    K: V_n = H = kappa_1 + ... + kappa_d

- **Locality:** Local. H at each point p depends only on the surface geometry in an infinitesimal neighborhood of p (the first and second fundamental forms at p). No nonlocal coupling. This is the *strongest locality* in the Atlas — not just "no integral operators" but "no dependence on the surface beyond an infinitesimal neighborhood on the surface itself."
- **Linearity:** Quasilinear. The mean curvature H is a *linear* function of the second fundamental form A_ij, but the second fundamental form depends *nonlinearly* on the surface parametrization (through the metric g_ij, which depends on the first derivatives of the embedding). The MCF equation is quasilinear parabolic: linear in the highest-order derivatives, with coefficients depending on the lower-order derivatives.
- **Stability role:** Stabilizing (smoothing). The curvature channel damps all non-constant features of the surface shape. The area functional A[Gamma] decreases monotonically: dA/dt = -integral H^2 dS <= 0. High-curvature features (small bumps, sharp corners) are eliminated fastest (rate ~ 1/R for feature of size R).
- **Scale action:** The velocity V_n = H ~ 1/R produces a *scale-dependent* speed: small features move fast, large features move slow. The elimination time for a feature of size R is t ~ R^2 (parabolic scaling). There is no intrinsic length scale — the curvature channel has no parameter. The scaling t ~ R^2 is the universal geometric scaling of MCF.

### Channel G: Geometry (Interface-Only Dynamics)

    G: Gamma_t is the complete state; no bulk field exists

- **Locality:** The geometry channel is *intrinsic* to the surface. The dynamics of Gamma_t at each point depend on the local surface geometry, not on any ambient field or bulk quantity.
- **Linearity:** N/A (structural property, not a PDE term).
- **Stability role:** Neutral. The interface-only character does not stabilize or destabilize — it constrains the architecture to have zero bulk degrees of freedom.
- **Scale action:** The surface carries all its own scales. The principal curvatures kappa_1, ..., kappa_d determine the local length scales. There are no external scales imposed by a bulk field.

**Structural significance:** Channel G is the feature that makes MCF fundamentally different from all other architectures. In AC/CH/PME/TFE/FP/RD/NS, the dynamics are described by a PDE on a *fixed domain*. In MCF, there is no fixed domain — the domain *is* the evolving surface. This means:

- No function spaces on fixed domains (L^2(Omega), H^1(Omega), etc.) — the spaces change with time.
- No fixed Fourier modes — the "modes" are surface harmonics on the evolving surface.
- No fixed boundary conditions — the surface has no boundary (it is closed).

The absence of a bulk field is the most radical structural economy in the Atlas: zero external degrees of freedom.

### Channel T: Topology Change (Singularity Formation)

    T: At singularity time T*, Gamma_t develops curvature blowup and may change topology

- **Locality:** Singularity formation is *local*: it occurs at specific points or curves where the curvature concentrates. The topology change (splitting, extinction) has *global* consequences but is *triggered locally*.
- **Linearity:** Highly nonlinear. Singularity formation is a nonlinear concentration phenomenon — the curvature feeds on itself through the quasilinear structure of the MCF equation.
- **Stability role:** *Structurally necessary.* Channel T is not a destabilizing anomaly — it is the mechanism by which the architecture resolves topological complexity. A genus-g surface cannot reach the global area minimum (zero area) without reducing its genus, and genus reduction requires singularity formation (surgery or weak-solution continuation).
- **Scale action:** Concentrates at the smallest scales. Near a singularity, the curvature blows up: ||A||_{L^infinity} ~ 1/sqrt(T* - t) → infinity. The singularity is a *scale-zero event* — the curvature concentrates at a point (or a curve/surface of vanishing extent).

### Channel Summary Table

| Channel | Symbol | Feature                  | Locality | Linearity    | Stability         | Scale Action        |
|---------|--------|--------------------------|----------|--------------|-------------------|---------------------|
| Curvature    | K | V_n = H                 | Local    | Quasilinear  | Stabilizing       | Rate ~ 1/R, t ~ R^2|
| Geometry     | G | No bulk field            | Intrinsic| N/A          | Neutral           | Surface-intrinsic   |
| Topology     | T | Singularity & topology Δ | Local*   | Nonlinear    | Structurally req. | Concentrates at R→0 |

*Local trigger, global consequence.

### Channel Count: The Minimal Architecture

| Architecture | Dynamical | Structural | Geometric | Singular | Total |
|-------------|-----------|------------|-----------|----------|-------|
| **MCF**     | **1 (K)** | **1 (G)**  | **0**     | **1 (T)**| **3** |
| PME         | 1 (D_nl)  | 1 (C)      | 1 (G)     | 0        | 3+1   |
| TFE         | 1 (D_4)   | 1 (C)      | 1 (G)     | 0        | 3+1   |
| FP          | 2 (T,D)   | 1 (C)      | 0         | 0        | 3+1   |
| AC          | 2 (R,S)   | 0           | 0         | 0        | 2+2   |

MCF has *three* channels — the fewest of any architecture in the Atlas. But one of those three is the topology-change channel T, which has no counterpart in any other architecture. MCF is the *only* architecture where singularity formation is a structural channel rather than an anomaly or an open question.

---

## 2. Dissipation Geometry

### 2.1 Gradient Flow of the Area Functional

MCF is the L^2 gradient flow of the area:

    A[Gamma] = integral_Gamma 1 dS

The L^2 inner product on normal vector fields along Gamma is:

    <V, W>_{L^2} = integral_Gamma V W dS

The variational derivative of A is:

    delta A / delta Gamma = -H    (first variation of area in the normal direction)

The MCF law V_n = H is therefore:

    V_n = -delta A / delta Gamma    (steepest descent of area)

### 2.2 The Dissipation Metric: ∫H² dS

The dissipation rate is:

    dA/dt = -integral_Gamma H^2 dS

The quantity integral H^2 dS = ||H||_{L^2(Gamma)}^2 is the *total squared mean curvature* — a global measure of how far Gamma deviates from being a minimal surface (H = 0). This is the MCF dissipation metric, playing the role of:

- M ||mu||^2 in AC.
- M ||nabla mu||^2 in CH.
- (4m/(m-1)) ||nabla(u^{(m+1)/2})||^2 in PME.
- integral h^n |nabla Delta h|^2 dx in TFE.
- I[rho | rho_eq] (Fisher information) in FP.

### 2.3 Comparison of Dissipation Metrics

| Architecture | Generating Functional        | Dissipation Metric                  | Metric Space      |
|-------------|------------------------------|-------------------------------------|--------------------|
| AC          | Ginzburg–Landau F            | M \|\|mu\|\|^2                     | L^2                |
| CH          | Ginzburg–Landau F            | M \|\|nabla mu\|\|^2              | H^{-1}            |
| PME         | Entropy H                    | \|\|nabla(u^{(m+1)/2})\|\|^2      | Wasserstein        |
| TFE         | Surface energy E             | integral h^n \|nabla Delta h\|^2   | Weighted H^{-1}    |
| FP          | Free energy F                | I[rho \| rho_eq] (Fisher info)     | Wasserstein        |
| **MCF**     | **Area A[Gamma]**           | **integral H^2 dS**                | **L^2 on Gamma**   |

The MCF dissipation metric is the *simplest geometric* dissipation in the Atlas: the integral of H^2 over the surface. It is:
- Intrinsic to the surface (defined on Gamma, not in the ambient space).
- Coordinate-free (H is a geometric invariant).
- Positive definite (H^2 >= 0, with equality only for minimal surfaces).
- Dimensionally natural: [H^2 dS] = [length^{d-2}], matching the dimensional analysis of dA/dt.

### 2.4 The Geometric Nature of MCF Dissipation

Every other architecture's dissipation metric involves *functional derivatives* of a field on a fixed domain — norms of mu, nabla mu, nabla u^{(m+1)/2}, etc., integrated over Omega. MCF's dissipation is a *geometric integral* over the evolving surface — it measures the total squared curvature of a moving shape, not the gradient of a function on a fixed domain.

This geometric character means that the MCF dissipation:
- Changes its *domain of integration* at each instant (the surface Gamma_t moves).
- Is defined intrinsically (no reference to ambient coordinates or a bulk domain).
- Is *scale-free* (no parameter like epsilon, D, nu appears in the dissipation — only the curvature H).

The geometric nature of the dissipation is the Mode 3 expression of MCF's defining structural feature: the state variable is a surface, so the dissipation is a surface integral. No other architecture has this property because no other architecture has a surface as its state variable.

---

## 3. Constraint Surface Geometry

### 3.1 Three Regimes of the Constraint Surface

The MCF constraint surface is stratified into three regimes, corresponding to the curvature's magnitude:

**Regime A: Smooth (Curvature Bounded)**

When sup_Gamma |A|^2 < C for some constant C, the surface is smooth and the MCF is a well-posed quasilinear parabolic PDE. Properties:

- Gamma_t is C^{infinity} (instantaneous regularization for t > 0).
- The area decreases monotonically.
- The curvature distribution smooths (Huisken's pinching estimates for convex surfaces).
- No topology change.
- Standard parabolic estimates hold.

This regime is the *smooth interior* of the constraint surface — analogous to the interior of the PME's support ({u > 0}) or the bulk of the FP domain. All estimates are unconditional and the dynamics are well-controlled.

**Regime B: Pre-Singular (Curvature Concentrating)**

As the curvature approaches blowup (sup |A|^2 → infinity), the surface enters the pre-singular regime:

- Huisken's monotonicity formula controls the local geometry near the developing singularity.
- The rescaled surface (blowup limit) approaches a self-similar shrinker.
- The curvature concentrates at specific points or curves.
- The surface remains smooth but the curvature grows without bound.

This regime is the *boundary layer* of the constraint surface — the transition from smooth to singular. Huisken's monotonicity formula is the key analytical tool here: it provides *monotone control* of the local geometry even as the curvature diverges. The monotone quantity Theta(t) decreases through this regime, classifying the approaching singularity type.

**Regime C: Singular (Curvature Blowup, Topology Change)**

At the singularity time T*:

- sup_Gamma |A(t)|^2 → infinity.
- The surface ceases to be smooth at one or more points.
- Topology change occurs (neckpinch, extinction).
- The classical MCF description breaks down.
- Continuation requires an *extended architecture*: level-set solutions (Evans–Spruck), surgery (Huisken–Sinestrari), or Brakke's varifold solutions.

This regime is the *singular boundary* of the constraint surface — the face where the smooth description terminates. It is not an anomaly (like the NS enstrophy gap) but a *required structural feature*: the area-minimization program for compact non-minimal surfaces *must* pass through this face to reach its conclusion (zero area).

### 3.2 Assembly into a Single Constraint Surface

The three regimes assemble as follows:

    Regime A (smooth)  →  Regime B (pre-singular)  →  Regime C (singular)  →  [extension] → restart at Regime A

The flow is *one-directional*: the dynamics move from A through B to C, not backward. This is enforced by the gradient-flow structure (area decreasing) and the monotonicity formula (Theta decreasing).

After a singularity (Regime C), the post-surgery surface re-enters Regime A (smooth), and the cycle repeats until all components have gone extinct. The total number of passes through Regime C (singularities) is *finite* — bounded by the initial topological complexity.

### 3.3 Singularity as a Required Face

The MCF constraint surface includes the singular face (Regime C) as a *required component*, not as a defect or an open question:

**Why the singularity is required:**

1. Every compact surface has A > 0. The gradient flow drives A → 0. But A = 0 means no surface — the surface must vanish. Vanishing requires shrinking to a point, which requires H → infinity at the extinction point. Therefore: *extinction requires singularity*.

2. A non-convex surface (genus g > 0) cannot continuously deform to a point without changing its topology (genus must become 0). Topology change under a smooth flow is impossible (smooth diffeomorphisms preserve topology). Therefore: *topology simplification requires singularity*.

3. The MCF is a gradient flow — it monotonically reduces area. The area of a compact surface is bounded below by 0. The only surface with area 0 is the empty set. Therefore: *the gradient flow must reach the empty set in finite time*. Reaching the empty set from a non-empty surface requires a singularity.

**Comparison with other architectures:**

| Architecture | Singularity Status                    | Role                           |
|-------------|---------------------------------------|-------------------------------|
| NS (3D)    | Open question (architectural gap)     | Would be a failure of self-consistency |
| RD          | Constitutive (super-linear kinetics)  | Constitutive possibility       |
| TFE (n<1)  | Positivity failure (parametric gap)   | Structural vulnerability       |
| **MCF**     | **Certain (for compact non-minimal)** | **Required structural feature**|
| AC/CH/PME/FP| Impossible                           | N/A                            |

MCF is the *only* architecture where singularity is both *certain* and *structural* (not a failure or a vulnerability but a *necessary mechanism* for achieving the architecture's stated goal).

---

## 4. Anomalies and Open Faces

### 4.1 Sealed Faces

**Oscillatory face: Sealed.** The gradient-flow structure (dA/dt <= 0) forbids limit cycles, sustained oscillations, and recurrence. The area is a strict Lyapunov functional.

**Chaotic face: Sealed.** No mechanism for sensitive dependence on initial conditions. The MCF dynamics are monotone (area decreasing) and smoothing (curvature regularizing). Adjacent surfaces evolve in a controlled fashion — the Hausdorff distance between two close surfaces evolves continuously.

**Bulk-blowup face: Sealed (absent).** There is no bulk PDE, so there is no bulk to blow up. The only blowup occurs at the *interface level* (curvature blowup on Gamma_t), not in a bulk field.

**Nonlocal face: Sealed (absent).** All channels are local. No Poisson equation, no Green's function, no pressure-type coupling. The velocity at each point depends only on the local curvature.

**Pattern-formation face: Sealed (absent).** One "species" (the surface), no reaction channel, no coupling. Turing instability requires multiple species + reaction. Spatial patterns cannot form on the surface under MCF — the dynamics only smooth.

### 4.2 The Singular Face: Required, Not Anomalous

The curvature-blowup face (Regime C) is *open* in the classical sense: the smooth solution ceases to exist. But it is not an *anomaly* in the FS sense because:

1. It is *expected and proven* (not open or uncertain).
2. It is *structurally necessary* (the architecture cannot complete its program without it).
3. It has a *well-understood structure* (Type I/II classification, shrinker attractors).
4. It has a *continuation* (surgery, level-set, varifold solutions extend past the singularity).

The singular face is a *structural feature of the constraint surface*, not a gap in it. The constraint surface is *designed to include this face* — it is part of the architecture's operation, not a failure of its operation.

**FS classification:** The MCF singular face is a *required structural boundary* — a face that the dynamics must cross as part of their normal operation. This is a new type of constraint-surface feature, not seen in any other architecture:

- AC/CH/PME/FP: no singularities (the constraint surface has no singular face).
- NS: the singular face is an *open question* (the surface might or might not have it).
- RD: the singular face is *constitutive* (some instances have it, others don't).
- **MCF: the singular face is *required*** (every compact non-minimal surface must cross it).

### 4.3 Anomaly Count

| Face               | Status              |
|--------------------|---------------------|
| Oscillatory        | Sealed (gradient flow) |
| Chaotic            | Sealed (monotone dynamics) |
| Bulk-blowup        | Absent (no bulk PDE) |
| Nonlocal           | Absent (fully local) |
| Pattern-formation  | Absent (single surface, no reaction) |
| **Curvature singularity** | **Required structural boundary** |

**Anomaly count: zero** (in the standard FS sense). The curvature singularity is not an anomaly — it is a required structural feature. If we classify it separately: the MCF architecture has zero anomalies and one *required singularity*, which is a new category in the PDE Atlas.

---

## 5. Channel Constraints

---

**C1. Geometric Invariance**

    The MCF law V_n = H is independent of parametrization, coordinate system, and ambient orientation.

All MCF quantities (H, A, kappa_i, |A|^2) are geometric invariants. The constraint surface is defined in the space of *shapes*, not in a function space.

*Scope: All MCF.*

---

**C2. Curvature-Driven Velocity Law**

    V_n = H = kappa_1 + ... + kappa_d    at every point of Gamma_t

The normal velocity is exactly the mean curvature. No other quantity (pressure, density, velocity field) contributes.

*Scope: All MCF.*

---

**C3. Area Dissipation**

    dA/dt = -integral_Gamma H^2 dS <= 0

The area is a strict Lyapunov functional. Dissipation rate = total squared mean curvature.

*Scope: All MCF (smooth regime).*

---

**C4. No Bulk Field**

    The state is Gamma_t alone. No scalar, vector, or tensor field on a fixed domain.

Zero bulk degrees of freedom. The architecture is pure geometry.

*Scope: All MCF.*

---

**C5. Parabolic Smoothing**

    Features of size R smoothed in time O(R^2). Curvature bounded by C/sqrt(t) for t > 0.

Standard second-order parabolic regularization applied to the surface geometry.

*Scope: Smooth regime (before singularity).*

---

**C6. Finite-Time Extinction (Convex Surfaces)**

    Convex Gamma_0 => Gamma_t → round point at T* <= A_0 / (4 pi d)

Huisken's theorem. Universal convergence to sphere near extinction.

*Scope: Convex initial surfaces.*

---

**C7. Singularity Formation (Non-Convex Compact Surfaces)**

    Non-convex compact Gamma_0 => sup |A|^2 → infinity at some T* < infinity

Singularity is *certain*. The curvature must blow up.

*Scope: All compact non-minimal surfaces.*

---

**C8. Topology Change via Singularity**

    At singularity time: genus can decrease, components can change, surface can split or vanish.
    Between singularities: topology is frozen.

Topology change is monotone (simplifying only) and occurs only at singular times.

*Scope: All compact MCF through singularities.*

---

**C9. No Oscillations**

    dA/dt <= 0 => no limit cycles, no recurrence, no periodic orbits with A > 0.

*Scope: All MCF.*

---

**C10. No Chaos**

    Monotone dynamics (area strictly decreasing) + smoothing => no sensitive dependence in geometric quantities.

*Scope: All MCF (smooth regime).*

---

**C11. No Bulk Blowup**

    No bulk PDE exists, so no bulk blowup is possible. The only blowup is curvature concentration at the surface level.

*Scope: All MCF.*

---

**C12. Shrinker Classification as Blowup Attractors**

    Near Type I singularity: rescaled surface → self-similar shrinker Sigma satisfying H = <x,n>/2
    Classified examples: S^d, S^k x R^{d-k}, Angenent torus, Abresch–Langer curves

The shrinkers are the *universal profiles* of singularity formation.

*Scope: Type I singularities.*

---

### Channel Constraint Summary

| Label | Constraint                        | Type              | Scope              |
|-------|-----------------------------------|-------------------|--------------------|
| C1    | Geometric invariance              | Structural        | All MCF            |
| C2    | Curvature-driven velocity         | Kinematic law     | All MCF            |
| C3    | Area dissipation                  | Lyapunov identity | Smooth regime      |
| C4    | No bulk field                     | Structural        | All MCF            |
| C5    | Parabolic smoothing               | Regularity        | Smooth regime      |
| C6    | Finite-time extinction (convex)   | Existence bound   | Convex surfaces    |
| C7    | Singularity formation (non-convex)| Structural        | Compact non-minimal|
| C8    | Topology change via singularity   | Topological       | Through singularities |
| C9    | No oscillations                   | Gradient flow     | All MCF            |
| C10   | No chaos                          | Monotonicity      | Smooth regime      |
| C11   | No bulk blowup                    | Structural        | All MCF            |
| C12   | Shrinker classification           | Attractor         | Type I singularities|

---

## 6. Comparison with AC, CH, PME, TFE, RD, NS, and FP

### 6.1 Constraint Surface Closure Across the Atlas

| Architecture | Surface Status          | Singular Face    | Mechanism                         |
|-------------|-------------------------|------------------|-----------------------------------|
| ED          | Closed (static)         | None             | Unique factorization              |
| FP          | Closed (all params)     | None             | Linearity                         |
| PME         | Closed (all m > 1)      | None             | Degeneracy + entropy + L^1 + cons.|
| AC          | Closed (d <= 3)         | None             | Max principle + Lyapunov          |
| CH          | Closed (d <= 3)         | None             | 4th-order + Lyapunov              |
| TFE (n>=1)  | Closed                 | None             | 4th-order + degeneracy + cons.    |
| **MCF**     | **Closed + required singularity** | **Required** | **Curvature + area dissipation** |
| TFE (n<1)  | Open (positivity)       | Parametric       | Insufficient degeneracy           |
| NS (3D)    | Open (enstrophy)        | Open question    | Insufficient viscosity            |
| RD          | Constitutive            | Constitutive     | None universal                    |

MCF introduces a *new category*: a constraint surface that is closed with respect to all *anomalous* faces (oscillation, chaos, bulk blowup, nonlocality, patterns) but includes a *required structural singularity* as part of its normal operation. No other architecture has this structure.

### 6.2 Channel Structure Comparison

| Feature                    | MCF          | AC    | CH    | PME   | TFE   | FP    | NS    | RD    |
|----------------------------|--------------|----- |-------|-------|-------|-------|-------|-------|
| State variable             | **Surface**  | Field| Field | Field | Field | Field | Field | Field |
| Channel count              | **3**        | 4    | 5     | 4     | 4     | 4     | 5     | 4     |
| Bulk PDE                   | **None**     | Yes  | Yes   | Yes   | Yes   | Yes   | Yes   | Yes   |
| Required singularity       | **Yes**      | No   | No    | No    | No    | No    | Open  | Const.|
| Topology change            | **Yes**      | No   | No    | No    | No    | No    | No    | No    |
| Gradient flow              | Area (L^2)  | F(L^2)| F(H^{-1})| H(W)| E(wH^{-1})| F(W)| No | Gen.no|
| Intrinsic scale            | **None**     | eps  | eps   | m     | n     | D,\|b\|| nu  | Const.|
| Dissipation metric         | **∫H²dS**   | \|\|mu\|\|²| \|\|∇mu\|\|²| gradient| weighted| Fisher| epsilon| N/A |

### 6.3 MCF's Unique Structural Position

MCF is the *only* architecture in the Atlas that:

1. Has a *geometric* state variable (surface, not function).
2. Has *zero* bulk degrees of freedom.
3. Has a *required singularity* as a structural feature.
4. Has *topology change* built into its dynamics.
5. Has *no intrinsic length scale* (parameter-free equation).
6. Has a *terminal state* (the surface ceases to exist).

No other architecture possesses any of these features (except NS, which has an *open* singularity question — not a required one). MCF is structurally *orthogonal* to every other architecture: it models a completely different type of mathematical object (a surface) through a completely different mechanism (curvature flow) with a completely different outcome (extinction through singularity).

### 6.4 MCF and the Hierarchy of Structural Complexity

The PDE Atlas architectures can be ordered by structural complexity:

    FP (linear, drift+diffusion) < PME (nonlinear, degenerate) < AC (nonlinear, reaction+diffusion)
    < CH (fourth-order, conserved) < TFE (fourth-order, degenerate) < MCF (geometric, singular)
    < NS (nonlinear, nonlocal, open regularity) < RD (class, full zoo)

MCF sits *between* the fully-closed gradient-flow architectures (FP, PME, AC, CH, TFE) and the open/constitutive architectures (NS, RD). It shares the gradient-flow structure of the former group (area decreasing, no oscillation) but has the singularity formation of the latter group (curvature blowup, classification of blowup profiles). MCF is the *gateway architecture*: the simplest system where singularity is a structural feature rather than an anomaly.

---

*End of Mode 3: Channels → Constraint Surface. The AD Criteria and Verdict will follow in the final file.*
