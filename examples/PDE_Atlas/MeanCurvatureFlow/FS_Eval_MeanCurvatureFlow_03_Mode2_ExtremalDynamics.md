# AD Evaluation: Mean Curvature Flow — Mode 2: PDE → Extremal Dynamics

Allen Proxmire

April 2026

---

## Overview

Mode 2 moves from the static envelope to the dynamics. The MCF dynamical landscape is *geometrically rich but dynamically monotone*: the surface smooths, shrinks, develops singularities, changes topology, and eventually vanishes — all while the area functional decreases monotonically. There are no oscillations, no patterns, no chaos, no sustained dynamics. The drama of MCF is purely *geometric*: what shapes does the surface pass through on its way to extinction, and what singularities does it encounter?

MCF is the only architecture in the Atlas where the dynamics *necessarily terminate* (all compact surfaces go extinct in finite time). Every other architecture either persists forever (AC, CH, PME, TFE, FP at equilibrium) or has an open question about persistence (NS in 3D). MCF is the *finite-lifetime* architecture — the only one whose state variable has a guaranteed expiration date.

Throughout:

    V_n = H    on Gamma_t subset R^{d+1}

---

## 1. Fundamental Time and Length Scales

### 1.1 The Curvature-Driven Time Scale

MCF has a single fundamental scaling relation linking space and time:

    V_n = H ~ 1/R    =>    dR/dt ~ -1/R    =>    R^2 ~ T* - t    =>    t ~ R^2

where R is the local radius of curvature. A feature of size R is eliminated in time O(R^2). This is the *parabolic scaling* t ~ L^2 — the same as the heat equation — but applied to the surface geometry rather than to a scalar field.

The time scale is *entirely geometric*: it is set by the surface's own curvature, not by any external parameter (no epsilon, no nu, no D, no m). The surface carries its own clock — the curvature determines how fast it moves.

**Key scaling relations for a sphere of radius R:**

    V_n = d/R    (mean curvature of S^d)
    dR/dt = -d/R
    R(t) = sqrt(R_0^2 - 2dt)
    T* = R_0^2 / (2d)    (extinction time)
    A(t) = omega_d R(t)^d = omega_d (R_0^2 - 2dt)^{d/2}    (area)
    H(t) = d / R(t) = d / sqrt(R_0^2 - 2dt)    (curvature, blows up at T*)

### 1.2 Curvature Sets the Speed

The normal velocity V_n = H provides a *scale-dependent speed*:

- Large features (large R): slow motion, V_n ~ 1/R << 1.
- Small features (small R): fast motion, V_n ~ 1/R >> 1.
- Flat regions (R → infinity): V_n → 0 (no motion).
- High-curvature regions (R → 0): V_n → infinity (singularity).

This scale-dependent speed produces a *universal smoothing hierarchy*: small features are eliminated first (fast motion at small scales), followed by progressively larger features (slower motion at larger scales). The surface monotonically simplifies — the curvature distribution narrows toward the mean, and the shape approaches a sphere (for convex surfaces) or develops canonical singularities (for non-convex surfaces).

### 1.3 Three Geometric Regimes

**Regime (A): Convex (H > 0 everywhere)**

Every point of Gamma_t has positive mean curvature. The surface:
- Remains convex for all time (convexity is preserved by MCF — Huisken, 1984).
- Becomes increasingly spherical (the principal curvatures kappa_1, ..., kappa_d converge to each other).
- Shrinks monotonically (dA/dt < 0).
- Goes extinct at finite time T* by collapsing to a round point.

The convex regime is the *simplest* MCF dynamics: monotone shrinking to a universal profile (the sphere). It is the geometric analogue of AC's exponential convergence to phi = ±1 — a monotone approach to a canonical final state.

**Regime (B): Non-Convex (H changes sign or is positive but surface is non-convex)**

The surface has regions of different curvature. The high-curvature regions evolve faster than the low-curvature regions, leading to:

- **Neckpinch:** A narrow neck (high curvature) shrinks faster than the adjacent bulges (lower curvature), pinching off in finite time. The singularity splits the surface into two (or more) components.
- **Cusp formation:** A pointed region develops infinite curvature.
- **Type I singularity:** The blowup rate is ||A||^2 ~ 1/(T* - t), and the rescaled surface converges to a self-similar shrinker (sphere, cylinder).
- **Type II singularity:** The blowup is faster than self-similar (||A||^2 >> 1/(T* - t)), and the rescaled surface converges to a translating soliton or an eternal solution.

The non-convex regime is where the MCF *geometric drama* occurs: the surface deforms, develops singularities, changes topology, and eventually fragments into convex components that then follow Regime (A) to extinction.

**Regime (C): Non-Compact / Asymptotically Flat**

For non-compact surfaces (infinite graphs, surfaces with flat ends):
- The surface may not go extinct (the flat regions do not shrink).
- The dynamics are dominated by local curvature: curved regions evolve while flat regions remain stationary.
- The long-time behavior depends on the decay rate of curvature at infinity.
- Special solutions: translating solitons (surfaces that move by translation under MCF) and rotating solitons.

### 1.4 Contrast with Other Architectures

| Feature                    | MCF                    | AC/CH                  | PME/TFE               | NS            | FP            |
|----------------------------|------------------------|------------------------|------------------------|---------------|---------------|
| What evolves               | Surface Gamma_t        | Field phi/u on domain  | Field u/h on domain    | Field **u** on domain | Density rho on domain |
| Speed set by               | Curvature 1/R          | Gradient of mu         | Gradient of u^m or p   | Advection + viscosity | Drift + diffusion |
| Time scale                 | t ~ R^2 (no parameter) | t ~ L^2/eps^2 or L^4  | t ~ L^2/u^{m-1}       | t ~ L^2/nu    | t ~ L^2/D     |
| Intrinsic scale            | None (scale-free)      | epsilon                | Depends on m, n        | nu            | D, \|b\|      |
| Bulk PDE                   | None                   | Yes                    | Yes                    | Yes           | Yes           |
| Singularity                | Certain (compact)      | None                   | None (PME), n-dep (TFE)| Open (3D)     | None          |

The MCF time scale t ~ R^2 is *purely geometric* — set by the surface itself with no external parameter. Every other architecture has a constitutive parameter (epsilon, nu, D, m) that sets the time scale. This parameter-free scaling is the signature of MCF's geometric purity.

---

## 2. Extremal Behaviors

### E1. Finite-Time Extinction for Convex Closed Surfaces

**Huisken's Theorem (1984):** Every smooth convex closed hypersurface Gamma_0 in R^{d+1} evolves under MCF to a single point in finite time T*, becoming asymptotically spherical:

    Gamma_t → sphere of radius sqrt(2d(T* - t))    as t → T*

The extinction is:
- *Universal:* All convex surfaces, regardless of initial shape, converge to the same spherical profile.
- *Finite-time:* T* <= A_0 / (4 pi d).
- *Self-similar near extinction:* The rescaled surface (T* - t)^{-1/2} Gamma_t → S^d(sqrt(2d)).

**Curve shortening (d = 1):** The Gage–Hamilton–Grayson theorem strengthens Huisken's result: every embedded closed curve in R^2 (convex or not) becomes convex and shrinks to a round point. For curves, *all* embeddings go extinct through a sphere — the non-convex detour is only temporary.

### E2. Curvature Blowup at Singularities

At a singularity time T*:

    lim_{t → T*} sup_Gamma |A(t)|^2 = infinity

The second fundamental form blows up — the curvature becomes infinite at one or more points. The blowup rate depends on the singularity type:

**Type I:** |A|^2 <= C / (T* - t). The curvature grows at the self-similar rate. The rescaled surface converges to a shrinker.

**Type II:** |A|^2 (T* - t) → infinity. The curvature grows faster than self-similar. The rescaled surface converges to an eternal solution (translating soliton, ancient solution).

### E3. Topology Change via Singularity

At singularity time, the surface can undergo topological transitions:

**Neckpinch (genus reduction):** A dumbbell-shaped surface (genus 0, one component) pinches at the neck, splitting into two components. The genus is preserved locally (each component may inherit topology from the original), but the global topology simplifies.

**Component extinction:** A small convex component shrinks to a point and disappears, reducing the number of connected components.

**MCF with surgery (Huisken–Sinestrari):** The post-singularity evolution is defined by:
1. Stop at the singularity time T*.
2. Identify the singular region (neck or extinction point).
3. Perform surgery: cut the surface at the neck and cap with standard spherical caps.
4. Restart MCF from the surgered surface.

The surgery procedure produces a *piecewise-smooth continuation* of the MCF past singularities. The total number of surgeries is finite (each surgery reduces the topological complexity).

### E4. Smoothing of Small-Scale Features

MCF is a parabolic regularizer: features of spatial scale R on the surface are smoothed in time O(R^2). Specifically:

- Short-wavelength oscillations (lambda << mean curvature radius) are damped exponentially.
- The curvature concentrates toward its mean: the ratio kappa_max / kappa_min → 1 for convex surfaces (Huisken's pinching estimate).
- The surface becomes C^{infinity} instantaneously for short time (parabolic regularization).

The smoothing is *unconditional* — it operates at all points of the surface where the curvature is finite. The only limitation is at singularities, where the curvature is infinite and the smoothing description breaks down.

### E5. Self-Similar Shrinkers

MCF admits *self-similar shrinking solutions* — surfaces Gamma_t that shrink homothetically:

    Gamma_t = sqrt(T* - t) Sigma

where Sigma satisfies the shrinker equation:

    H = <x, n> / 2

Classified shrinkers include:
- **S^d (sphere):** The universal convex shrinker. All convex surfaces converge to it near extinction.
- **S^k x R^{d-k} (cylinder):** The universal neckpinch shrinker. Neckpinch singularities converge to it near pinch time.
- **Angenent torus (S^1 x S^{d-1}):** A non-trivial compact shrinker (d >= 2). Represents a more complex singularity type.
- **Abresch–Langer curves:** Complete classification of shrinker curves in R^2.

The shrinkers are the MCF analogues of the PME's Barenblatt profiles and the FP's Gibbs–Boltzmann equilibrium — the universal profiles to which solutions converge near their critical events (extinction for PME/FP, singularity for MCF).

### E6. Monotone Quantities (Huisken's Monotonicity Formula)

The Gaussian density ratio:

    Theta(t) = (4 pi (T* - t))^{-d/2} integral_Gamma exp(-|x - x_0|^2 / (4(T* - t))) dS

is *monotone non-increasing* in t for any spacetime center (x_0, T*). This is the most powerful analytical tool in MCF:

- It controls the local geometry near singularities.
- Its limit as t → T* classifies the singularity type (Theta → density of the shrinker).
- It provides a *monotone quantity* that replaces the role of entropy in other gradient-flow architectures.

The monotonicity formula is the MCF's *structural masterpiece* — a single geometric quantity that encodes all information about the approach to singularity.

### E7. Scale-Invariant Blowup Profiles

Near a Type I singularity at (x_0, T*), the rescaled surface:

    tilde{Gamma}_s = (T* - t)^{-1/2} (Gamma_t - x_0),    s = -log(T* - t)

converges to a shrinker Sigma as s → infinity:

    tilde{Gamma}_s → Sigma    smoothly on compact subsets

The blowup profile is *scale-invariant*: zooming in on the singularity (rescaling by (T* - t)^{-1/2}) reveals a fixed shape (the shrinker) that does not depend on the specific surface or its initial data. The blowup profile is the *universal geometry* of the singularity.

### E8. No Oscillations, No Chaos

The gradient-flow structure (dA/dt <= 0) forbids:
- Limit cycles (area monotone → no periodic orbits with A > A_min).
- Sustained oscillations (area decreasing → no recurrence).
- Chaos (gradient flows on finite-dimensional manifolds are monotone → no sensitive dependence in the relevant geometric quantities).

The MCF dynamics are *monotonically simplifying*: the surface becomes smoother, more symmetric, topologically simpler, and smaller over time. There is no mechanism for complexity generation — only complexity reduction.

---

## 3. Universal Inequalities

---

**U1. Area Dissipation Identity**

    dA/dt = -integral_Gamma H^2 dS

Exact identity. The area decreases at a rate equal to the total squared mean curvature. Tight (saturated by minimal surfaces where H = 0).

---

**U2. Curvature L^2 Dissipation**

    d/dt integral_Gamma H^2 dS <= -2 integral_Gamma |nabla H|^2 dS + C integral_Gamma |A|^4 dS

The total squared curvature evolves under a reaction-diffusion-type inequality on the surface. The gradient term (stabilizing) competes with the |A|^4 term (potentially destabilizing). When |A| is large, the destabilizing term can win → curvature blowup → singularity.

---

**U3. Extinction-Time Bound for Convex Surfaces**

    T* <= A_0 / (4 pi d)    [with A_0 = initial area]

For a sphere: T* = R_0^2 / (2d) = A_0 / (d omega_d R_0^{d-2} * 2d). The bound is sharp for spheres. Every convex surface goes extinct in finite time bounded by its initial area.

---

**U4. Huisken's Monotonicity Formula**

    d/dt [(4 pi (T* - t))^{-d/2} integral_Gamma exp(-|x|^2 / (4(T* - t))) dS] <= 0

Monotone non-increasing Gaussian density ratio. The most powerful structural inequality in MCF — provides localized control near singularities without requiring global estimates.

---

**U5. Gradient-Flow Inequality**

    A[Gamma_t] + integral_0^t integral_Gamma H^2 dS ds = A[Gamma_0]

Integrated form of U1. Total area plus total dissipation equals initial area. Closed energy accounting with no gap (for smooth solutions).

---

**U6. Scale-Invariant Curvature Bounds (Before Singularity)**

For smooth MCF on [0, T):

    sup_Gamma |A(t)|^2 <= C / t    for 0 < t < T    (interior estimate)

The curvature is bounded by 1/t — the standard parabolic regularization estimate. This bound holds *until the singularity forms*.

---

**U7. Blowup-Rate Bounds Near Singularity**

**Type I:**

    sup_Gamma |A(t)|^2 <= C / (T* - t)

**Type II:**

    sup_Gamma |A(t)|^2 * (T* - t) → infinity    as t → T*

The blowup rate classifies the singularity. Type I is "controlled" (self-similar); Type II is "wild" (faster-than-self-similar). Every singularity is either Type I or Type II — there are no intermediate types.

---

**U8. Topological Monotonicity**

Between singularities:
    genus(Gamma_t) = constant,    number of components = constant

At singularities:
    total genus can only decrease (or stay the same)
    number of components can increase (splitting) or decrease (extinction)

But the *total topological complexity* (genus + number of components, in an appropriate metric) is non-increasing. The surface only simplifies topologically.

---

**U9. Regularity Criterion**

    sup_{[0,T)} sup_Gamma |A|^2 < infinity    iff    Gamma_t is smooth on [0, T]

The solution is smooth if and only if the curvature remains bounded. This is the MCF analogue of the BKM criterion for NS — but with a *resolved* answer for compact surfaces: the curvature *does* blow up (for non-minimal compact surfaces). The criterion is diagnostic, not predictive (we already know the answer).

---

**U10. Shrinker Classification**

Near a Type I singularity, the blowup limit is a self-similar shrinker:

    tilde{Gamma}_s → Sigma    where H_Sigma = <x, n> / 2

The shrinkers are classified:
- d = 1: complete classification (circle, Abresch–Langer curves).
- d >= 2: partial classification (sphere, cylinder, Angenent torus; others known but not fully classified).

The shrinkers are the *attractors of singularity formation* — the universal geometric profiles that the surface approaches as it pinches.

---

### Universal Inequality Summary

| Label | Inequality                        | Type            | Status              | Role                        |
|-------|-----------------------------------|-----------------|---------------------|-----------------------------|
| U1    | Area dissipation identity         | Exact equality  | Unconditional       | Primary accounting          |
| U2    | Curvature L^2 dissipation         | Inequality      | Non-closing         | Singularity indicator       |
| U3    | Extinction-time bound             | Upper bound     | Convex surfaces     | Finite-lifetime guarantee   |
| U4    | Huisken monotonicity              | Monotone        | Unconditional       | Most powerful tool          |
| U5    | Gradient-flow energy identity     | Exact equality  | Unconditional       | Energy accounting           |
| U6    | Pre-singularity curvature bound   | Interior est.   | Before singularity  | Parabolic regularity        |
| U7    | Blowup-rate bounds                | Type I/II       | At singularity      | Singularity classification  |
| U8    | Topological monotonicity          | Non-increasing  | Unconditional       | Simplification only         |
| U9    | Regularity criterion              | Iff condition   | Diagnostic          | Smooth iff bounded |A|      |
| U10   | Shrinker classification           | Attractor       | Type I singularities| Blowup profiles             |

---

## 4. Attractors and Long-Time Behavior

### 4.1 Two Attractor Regimes

MCF has *two distinct attractor types*, corresponding to the two ways a surface can reach its terminal state:

**Extinction Attractor: The Round Sphere**

For convex surfaces (and, by Grayson's theorem, for all embedded curves in R^2), the terminal attractor is the *round sphere S^d*. Near extinction:

    Gamma_t → sphere of radius sqrt(2d(T* - t))

The sphere is the *universal extinction profile*: all convex surfaces converge to it as they shrink to a point. It is the geometric analogue of the Barenblatt profile (PME) and the Gibbs–Boltzmann equilibrium (FP) — a unique, explicit, universal profile determined by the architecture alone.

**Singularity Attractors: Shrinkers**

For non-convex surfaces, the terminal behavior is more complex. Near a Type I singularity, the surface approaches a *shrinker*:

- **Neckpinch → Cylinder S^k x R^{d-k}:** The surface near the neck approaches a shrinking cylinder. The neck radius goes to zero at rate sqrt(T* - t), and the rescaled neck profile is exactly the cylinder.
- **Compact singularity → Sphere S^d or Angenent torus:** The surface near a compact singularity approaches a compact shrinker.

The shrinkers are the *singularity attractors* of MCF — the universal geometric profiles that the surface approaches as it develops a singularity. Unlike the extinction attractor (unique, the sphere), the singularity attractors form a *family* — there are multiple shrinkers, and the specific one selected depends on the geometry of the surface near the singular point.

### 4.2 The Attractor Hierarchy

The MCF attractors form a hierarchy, ordered by their role in the dynamics:

    Initial surface → [smoothing] → non-convex singularity → [surgery] → convex components → [extinction] → points

Each stage has its own attractor:
- Smoothing: no attractor (transient, the surface deforms toward simpler geometry).
- Singularity: shrinker attractor (cylinder, torus, etc.).
- Extinction: sphere attractor (unique, universal).

The hierarchy terminates at *extinction*: the surface reaches zero area and ceases to exist. MCF is the *only architecture in the Atlas with a terminal state* — a point at which the state variable no longer exists. Every other architecture (AC, CH, PME, TFE, FP, NS, RD) has perpetual states (the solution exists for all time, possibly converging to a nonzero equilibrium).

### 4.3 Comparison of Attractor Structures

| Architecture | Attractor Type                    | Explicit? | Universal? | Terminal?  |
|-------------|-----------------------------------|-----------|------------|------------|
| **MCF**     | **Sphere (extinction)**           | **Yes**   | **Yes (convex)** | **Yes (vanishes)** |
| **MCF**     | **Shrinkers (singularity)**       | **Yes**   | **Type-dependent** | **No (continues post-surgery)** |
| PME         | Barenblatt profile                | Yes       | Yes        | No (u → 0 but exists) |
| TFE         | Source-type profile               | ODE       | Yes        | No         |
| FP          | Gibbs–Boltzmann                   | Yes       | Yes (confining)| No     |
| AC          | phi = ±1 (uniform)               | Trivial   | Yes        | No         |
| CH          | Phase-separated domains           | Implicit  | Conditional| No         |
| NS (2D)    | Attractor (compact set)           | No        | No         | No         |
| RD          | Constitutive (full zoo)           | Constitutive | No      | No         |

The MCF extinction attractor is unique in the Atlas:
- It is *terminal*: the state variable ceases to exist.
- It is *geometric*: a surface (sphere), not a function.
- It is *universal* for convex initial data.
- It has an *explicit form*: the round sphere of radius sqrt(2d(T* - t)).

### 4.4 Geometric vs. Functional Attractors

Every other architecture's attractor is a *function* on a fixed domain (a density profile, a phase configuration, a velocity field). The MCF attractor is a *geometric shape* — a sphere, a cylinder, a torus. The distinction is fundamental:

- Functional attractors exist in function spaces (L^2, H^1, etc.) and are characterized by norms and regularity.
- Geometric attractors exist in shape space (the space of embedded surfaces) and are characterized by curvature, area, and topology.

MCF's attractors are the *simplest* in the Atlas — not because they have the fewest parameters (the PME Barenblatt profile has only one parameter, M) but because they are *geometric objects* (spheres, cylinders) rather than functions satisfying ODEs or PDEs. The sphere is characterized by a single number (its radius), which is the most minimal description of any attractor in the Atlas.

---

## 5. Comparison with AC, CH, PME, TFE, RD, NS, and FP

### 5.1 MCF as the Sharp-Interface Limit of AC

    AC (epsilon > 0): partial_t phi = epsilon^2 Delta phi + phi - phi^3
    MCF (epsilon → 0): V_n = H

The AC evaluation identified mean-curvature motion as a necessary configuration (N3 in AC Mode 1). MCF *is* this necessary configuration — the geometric content of AC stripped of the bulk field and the diffuse interface. The passage from AC to MCF is a *dimensional reduction*: from a d-dimensional bulk PDE to a (d-1)-dimensional geometric flow.

### 5.2 MCF vs. CH (Geometric Interface Motion)

CH in the sharp-interface limit produces the *Mullins–Sekerka problem*, not pure MCF:

    CH → V_n = -Delta_Gamma H    [surface diffusion, fourth-order geometric flow]

or

    CH → V_n = [nabla mu . n]_+^-    [Mullins–Sekerka, bulk-mediated]

The CH sharp-interface limit is *more complex* than MCF because conservation of the order parameter introduces a bulk diffusion equation that couples to the interface motion. Pure MCF has no bulk equation; the CH sharp interface does. MCF is *simpler* than the CH geometric limit.

### 5.3 MCF vs. PME/TFE (Free-Boundary vs. Geometric Curvature)

| Feature                    | MCF                          | PME / TFE                    |
|----------------------------|------------------------------|------------------------------|
| Free boundary              | *Is* the state               | Boundary of a bulk field     |
| Motion law                 | V_n = H (curvature)          | V_n ~ grad(u^m) (Darcy)     |
| Bulk field                 | None                         | Yes (u or h)                 |
| Conservation               | No                           | Yes (mass)                   |
| Singularity                | Certain (curvature blowup)   | None (PME) / n-dep (TFE)    |
| Topology change            | Yes                          | No                           |
| Intrinsic scale            | None                         | Depends on m, n              |

The key distinction: PME/TFE free boundaries are *consequences of a bulk PDE* (the boundary is where u or h reaches zero). MCF's surface *is* the PDE — there is no bulk. The motion laws are different: PME/TFE boundaries move by pressure or density gradients (Darcy law), while MCF surfaces move by curvature (a purely geometric quantity). The PME/TFE motion laws depend on the bulk solution; the MCF motion law is intrinsic to the surface.

### 5.4 MCF vs. NS (Geometric vs. Transport-Driven)

NS evolves a velocity field under the combined action of advection, pressure, and viscosity. MCF evolves a surface under curvature alone. The architectures are *structurally orthogonal*: NS is about transport (moving fluid); MCF is about geometry (moving surfaces). NS has a nonlocal channel (pressure); MCF is fully local. NS has an open regularity problem in 3D; MCF has a proven singularity formation. NS can exhibit turbulence; MCF cannot oscillate or form patterns.

The only structural parallel: both develop singularities through a quadratic nonlinearity (vortex stretching in NS, curvature concentration in MCF), and both have a regularity criterion of the form "smooth iff the critical quantity stays bounded" (BKM for NS, curvature bound for MCF). But the outcomes differ: the NS blowup question is *open*; the MCF blowup question is *resolved*.

### 5.5 MCF vs. FP (Geometry vs. Probability)

FP and MCF are at opposite ends of the Atlas's structural spectrum:

- FP: linear, bulk field, drift + diffusion, probability-preserving, explicit equilibrium, no geometry.
- MCF: quasilinear, no bulk field, pure curvature, area-decreasing, finite-time extinction, pure geometry.

The only connection: both are gradient flows (FP of free energy in Wasserstein metric; MCF of area in L^2 metric). Both converge to explicit, universal attractors (Gibbs–Boltzmann for FP; round sphere for MCF). Both are fully local. But the architectures model completely different objects (probability distributions vs. surfaces) through completely different mechanisms (drift-diffusion vs. curvature flow).

### 5.6 Summary: MCF as the Pure Geometric-Dissipation Architecture

| Feature                    | MCF              | AC    | CH    | PME   | TFE   | FP    | NS    | RD    |
|----------------------------|------------------|-------|-------|-------|-------|-------|-------|-------|
| State variable             | **Surface**      | Field | Field | Field | Field | Field | Field | Field |
| Bulk PDE                   | **None**         | Yes   | Yes   | Yes   | Yes   | Yes   | Yes   | Yes   |
| Curvature-driven           | **Yes (V_n=H)**  | Limit | Limit | No    | No    | No    | No    | No    |
| Conservation               | **No**           | No    | Yes   | Yes   | Yes   | Yes   | Yes   | Const.|
| Singularity                | **Certain**      | No    | No    | No    | n-dep | No    | Open  | Const.|
| Topology change            | **Yes**          | No    | No    | No    | No    | No    | No    | No    |
| Attractor type             | **Geometric**    | Funct.| Funct.| Funct.| Funct.| Funct.| Funct.| Funct.|
| Terminal state             | **Yes (extinct)**| No    | No    | No    | No    | No    | No    | No    |
| Gradient flow              | Area (L^2)       | F(L^2)| F(H^{-1})| H(W)| E(wH^{-1})| F(W)| No  | Gen.no|
| Intrinsic scale            | **None**         | eps   | eps   | m     | n     | D,\|b\|| nu  | Const.|

MCF is the *unique geometric architecture* in the Atlas: the only PDE whose state is a surface, whose dynamics are curvature-driven, whose singularities are certain, whose topology changes, and whose state variable eventually ceases to exist. It is the purest expression of geometric dissipation — area minimization through curvature flow, with nothing else.

---

*End of Mode 2: PDE → Extremal Dynamics. Mode 3 (Channels → Constraint Surface) will follow in a subsequent file.*
