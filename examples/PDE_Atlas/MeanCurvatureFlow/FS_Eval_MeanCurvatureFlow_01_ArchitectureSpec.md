# AD Evaluation: Mean Curvature Flow — Architectural Specification

Allen Proxmire

April 2026

---

## 1. Implicit Axioms of the Mean Curvature Flow Architecture

Mean Curvature Flow (MCF) describes the evolution of a hypersurface Gamma_t subset R^d that moves with normal velocity equal to its mean curvature: V_n = H. It is the simplest *geometric evolution equation* — a PDE whose state variable is not a scalar field on a fixed domain but a *moving surface* in ambient space. The surface deforms under its own curvature, smoothing out bumps, shrinking convex regions, and eventually collapsing to a point (or developing singularities for non-convex surfaces).

MCF occupies a unique position in the PDE Atlas: it is the *only architecture whose state variable is a geometric object* (a surface) rather than a function (a density, a velocity, a height). Every other evaluated architecture evolves a scalar or vector field on a fixed domain; MCF evolves the *domain itself*. This geometric character gives MCF structural features — topology change, singularity formation, intrinsic vs. extrinsic descriptions — that have no counterpart in any field-based PDE.

### Axiom MCF-1: Interface Hypothesis

The state variable is a smooth closed hypersurface Gamma_t subset R^{d+1} (or, more generally, a codimension-one submanifold) evolving in time. The surface Gamma_t is the *complete description* of the system — there is no bulk field, no density, no velocity field, no order parameter. The architecture is *pure geometry*: the only information is the shape of the surface at each instant.

This is a radical departure from every previous evaluation. In AC/CH/PME/TFE/FP/RD/NS, the state is a function on a fixed domain: u(x, t), phi(x, t), rho(x, t), **u**(x, t). In MCF, the state is the *domain boundary itself* — the surface Gamma_t. The passage from function-on-domain to evolving-domain is the structural analogy of passing from Eulerian to Lagrangian description, but more fundamental: MCF has no Eulerian field at all.

**Representations of Gamma_t:**

Multiple equivalent representations exist, each with different analytical properties:

- **Parametric:** Gamma_t = {F(p, t) : p in M}, where F : M x [0, T) → R^{d+1} is an embedding of an abstract manifold M. The MCF becomes a system of PDEs for F.
- **Graph:** Gamma_t = {(x, u(x, t)) : x in Omega} when the surface is a graph over a fixed domain. The MCF becomes a scalar PDE for u.
- **Level set:** Gamma_t = {x : phi(x, t) = 0}, where phi is a level-set function satisfying a PDE on all of R^{d+1}. This is the Evans–Spruck / Chen–Giga–Goto formulation.
- **Phase-field:** Gamma_t is approximated by the diffuse interface of a phase-field equation (Allen–Cahn with epsilon → 0). The MCF is the sharp-interface limit.

### Axiom MCF-2: Locality

The normal velocity of Gamma_t at each point depends only on the *local geometry* of the surface at that point — specifically, on the mean curvature H, which is determined by the first and second fundamental forms of Gamma_t at that point. There is no nonlocal coupling: the motion of a surface element at point p is independent of the surface geometry at distant points q.

This locality is *intrinsic to the surface*: the relevant "neighborhood" is a neighborhood on Gamma_t, not in the ambient space R^{d+1}. The mean curvature H at a point p depends on the surface's first and second derivatives at p — it is a *local geometric quantity*.

### Axiom MCF-3: Geometric Law (V_n = H)

The normal velocity of Gamma_t equals the mean curvature:

    V_n(p, t) = H(p, t)

where:
- V_n is the speed of the surface in the outward normal direction (positive for shrinking convex surfaces).
- H = kappa_1 + ... + kappa_d is the mean curvature (sum of principal curvatures, with sign convention: H > 0 for convex surfaces with outward normal).

This law is the *defining equation* of MCF — the simplest geometric evolution law that is second-order, parabolic, and intrinsic. It is the surface analogue of the heat equation: just as the heat equation partial_t u = Delta u smooths a scalar field, MCF smooths a surface by diffusing its curvature.

### Axiom MCF-4: No Bulk Field

MCF has *no bulk PDE*. There is no scalar field u(x, t), no velocity field **u**(x, t), no density rho(x, t) defined on a fixed domain. The dynamics are entirely confined to the surface Gamma_t. The surface is its own state space — it carries all the information.

This is the most radical structural economy in the PDE Atlas: *zero bulk degrees of freedom*. Every other architecture has at least one bulk field (d-dimensional, evolving on a d-dimensional domain). MCF has zero bulk fields — only the (d-1)-dimensional surface Gamma_t.

### Axiom MCF-5: Euclidean Ambient Space

The surface Gamma_t evolves in flat Euclidean R^{d+1}. The mean curvature H is computed with respect to the Euclidean metric. Surfaces evolving in Riemannian manifolds (Ricci flow, curve-shortening on surfaces) are outside the standard MCF architecture.

### Axiom MCF-6: Gradient-Flow Structure (Area Functional)

MCF is the L^2 gradient flow of the *area functional*:

    A[Gamma] = integral_Gamma 1 dS = (d-dimensional area of Gamma)

The first variation of A in the normal direction gives:

    delta A / delta Gamma = -H    (mean curvature is the variational derivative of area)

The MCF law V_n = H is therefore:

    V_n = -delta A / delta Gamma    (steepest descent of area in the L^2 normal metric)

The gradient-flow structure guarantees:
- Area is monotone decreasing: dA/dt = -integral_Gamma H^2 dS <= 0.
- Stationary surfaces have H = 0 everywhere (minimal surfaces).
- No limit cycles, no oscillations, no recurrence.

The area functional plays the role of the free energy in AC/CH, the entropy in PME, and the surface energy in TFE. It is the *simplest* Lyapunov functional in the Atlas — a single geometric quantity (area) with a single variational derivative (mean curvature).

### Axiom MCF-7: No Reaction, No Forcing

MCF has no external forcing, no reaction terms, and no source/sink mechanisms. The surface evolves under its own curvature alone — a purely *self-driven* geometric evolution. Adding forcing (e.g., V_n = H + f) or reaction (V_n = H + c, motion by mean curvature plus a constant) extends the architecture but is outside the standard MCF.

### Axiom MCF-8: No Conservation Law

Unlike PME, CH, TFE, and FP, the MCF architecture does *not* conserve any integral quantity. In particular:

- **Area is not conserved:** dA/dt = -integral H^2 dS < 0. The area strictly decreases (except for minimal surfaces).
- **Enclosed volume is not conserved:** d(Vol)/dt = -integral H dS ≠ 0 in general. For convex surfaces, the enclosed volume decreases (the surface shrinks).
- **No mass conservation:** There is no density field to conserve.

The absence of conservation is a structural feature, not a defect: MCF is designed to *minimize area*, and area minimization requires area to decrease. Conservation would prevent the area from decreasing, defeating the purpose of the gradient flow.

The *volume-preserving MCF* (V_n = H - H-bar, where H-bar is the average mean curvature) is a different architecture that adds conservation of enclosed volume.

---

## 2. Canonical PDE in Architectural Form

### 2.1 The Geometric Law

    V_n(p, t) = H(p, t)    for p in Gamma_t                     ... (MCF-I)

This is a *geometric PDE* — it specifies the motion of a surface through a relation between the normal velocity and the curvature, without reference to coordinates or parametrizations.

### 2.2 Parametric Form

For a parametrized surface F : M x [0, T) → R^{d+1}:

    partial_t F = H **n**                                          ... (MCF-param)

where **n** is the unit outward normal. This is a system of (d+1) scalar PDEs for the (d+1) components of F. The system is *degenerate parabolic*: the tangential component of partial_t F is not determined by the equation (gauge freedom — one can reparametrize without changing the surface).

Fixing the gauge (e.g., normal parametrization), the equation becomes:

    partial_t F = Delta_Gamma F                                    ... (MCF-Laplace)

where Delta_Gamma is the *Laplace–Beltrami operator* on Gamma_t with the induced metric. This reveals MCF as the *heat equation on the surface* — a second-order parabolic equation, intrinsic to the surface, smoothing the embedding F.

### 2.3 Level-Set Form

For a level-set function phi : R^{d+1} x [0, T) → R with Gamma_t = {phi = 0}:

    partial_t phi = |nabla phi| div(nabla phi / |nabla phi|) = |nabla phi| H    ... (MCF-LS)

This is a *degenerate parabolic PDE* on all of R^{d+1}. The degeneracy occurs where |nabla phi| = 0 (flat regions of phi, where the surface is not well-defined). The level-set formulation allows surfaces to undergo *topology changes* (splitting, merging) without explicit tracking — the level set simply changes connectivity.

### 2.4 Channel-Labeled Decomposition

    V_n = H
        = kappa_1 + ... + kappa_d
    |___________________________|
      Curvature channel (K)

    dA/dt = -integral H^2 dS <= 0
    |_______________________________|
      Geometric dissipation (G)

    Singularity formation at finite time
    |___________________________________|
      Topology-change channel (T)

### 2.5 Explicit Examples

**Curve shortening flow (d = 1):** A closed curve gamma_t in R^2 moves with normal velocity V_n = kappa (curvature). The Gage–Hamilton–Grayson theorem: every embedded closed curve becomes convex and shrinks to a round point in finite time.

**Surface MCF (d = 2):** A closed surface Sigma_t in R^3 moves with V_n = H = kappa_1 + kappa_2. Convex surfaces shrink to round points (Huisken's theorem). Non-convex surfaces can develop singularities (neckpinch) before extinction.

**Shrinking sphere:** A sphere of radius R(t) evolves as:

    dR/dt = -d/R    (since H = d/R for a d-sphere)

giving R(t) = sqrt(R_0^2 - 2d t), extinction at T* = R_0^2 / (2d).

---

## 3. Channel Identification

### Channel K: Curvature (Geometric Diffusion)

    K: V_n = H = kappa_1 + ... + kappa_d

- **Role:** The sole dynamical channel. Drives the surface toward minimal area by smoothing curvature: regions of high positive curvature (bumps, tips) move inward fastest; regions of low curvature (flat patches) move slowly; regions of negative curvature (saddles) move outward. The curvature channel is the geometric analogue of the Laplacian — it is the *Laplace–Beltrami operator on the embedding*.
- **Locality:** Local. The mean curvature H at a point p depends only on the surface's first and second fundamental forms at p — i.e., on the surface's shape in an infinitesimal neighborhood of p.
- **Linearity:** Nonlinear. Although the mean curvature is a *linear function of the second fundamental form*, the second fundamental form depends nonlinearly on the surface parametrization. MCF is a *quasilinear* parabolic equation — the highest-order term is linear in the second derivatives, but the coefficients depend on the first derivatives (the metric). This quasilinearity is the geometric analogue of the nonlinear diffusion in PME (where D(u) depends on u).
- **Stability role:** Stabilizing (smoothing curvature). MCF is a *parabolic regularizer*: it smooths the surface, reducing high-curvature features. The area functional A[Gamma] decreases monotonically. The curvature channel is the architecture's sole mechanism — it simultaneously smooths, shrinks, and eventually annihilates the surface.
- **Scale action:** Curvature scales as 1/R for a feature of size R. The normal velocity V_n = H ~ 1/R, so small features (small R) move fastest: V_n ~ 1/R. The time to eliminate a feature of size R is t ~ R^2 (since dR/dt ~ -1/R gives R^2 ~ t). This is *second-order parabolic scaling* — the same t ~ L^2 scaling as the heat equation, but applied to the geometry rather than to a field.

### Channel G: Geometric Dissipation (Area Functional)

    G: dA/dt = -integral_Gamma H^2 dS <= 0

- **Role:** Structural property of the evolution. The area functional is a strict Lyapunov functional: A decreases along every non-stationary trajectory, with dissipation rate integral H^2 dS. This is the MCF analogue of the free-energy dissipation in AC/CH and the entropy dissipation in PME.
- **Locality:** The dissipation density H^2 is local (H is a local geometric quantity).
- **Linearity:** Nonlinear (H^2 is a nonlinear function of the curvature).
- **Stability role:** Stabilizing. The monotone decrease of area drives the surface toward minimal surfaces (H = 0) or extinction (surface collapses to a point).

### Channel T: Topology Change (Singularity Formation)

    T: Singularity formation at finite time T*

- **Role:** MCF develops *singularities* in finite time — points or regions where the curvature blows up (||H|| → infinity). At singularity time, the surface can undergo topology changes: splitting (a dumbbell pinches off into two components), merging (two surfaces touch and unite), or extinction (the entire surface collapses).
- **Locality:** Singularities form *locally* — at specific points or regions where the curvature concentrates. The topology change, however, is *global* (it changes the connectivity of the surface).
- **Linearity:** Highly nonlinear. Singularity formation is a nonlinear, non-perturbative phenomenon that cannot be captured by linearization.
- **Stability role:** *Structurally necessary but analytically destructive.* Singularity formation is an inevitable consequence of the MCF dynamics (Huisken's theorem: convex surfaces shrink to points in finite time). The singularity is not a failure of the architecture — it is the *completion* of the area-minimization program. But it destroys the smooth description of the surface and requires the architecture to be *extended* (through weak solutions, level-set solutions, or surgery) to continue past the singularity.

### Channel Summary Table

| Channel | Symbol | Feature                   | Locality | Linearity    | Stability    | Scale Action        |
|---------|--------|---------------------------|----------|--------------|--------------|---------------------|
| Curvature    | K | V_n = H                  | Local    | Quasilinear  | Stabilizing  | Rate ~ 1/R (t ~ R^2)|
| Area dissip. | G | dA/dt = -integral H^2 dS | Local    | Nonlinear    | Stabilizing  | All-scale           |
| Topology     | T | Singularity at finite T* | Local*   | Nonlinear    | Necessary**  | Concentrates at small R|

*Singularity forms locally; topology change is global.
**Singularity is an inevitable outcome, not an anomaly — it is how the architecture completes its program.

---

## 4. Relation to AC, CH, PME, TFE, FP, RD, NS, and ED

### 4.1 MCF as the Geometric Limit of Phase-Field Architectures

MCF is the *sharp-interface limit* of the Allen–Cahn equation:

    AC: partial_t phi = epsilon^2 Delta phi + phi - phi^3    →    MCF: V_n = H    as epsilon → 0

The convergence was established by Evans–Spruck, de Mottoni–Schatzman, and others. In this limit, the diffuse interface of AC (width O(epsilon)) sharpens to a geometric surface Gamma_t, and the AC dynamics collapse to the MCF law V_n = H. The double-well reaction (phi - phi^3) and the Laplacian smoothing (epsilon^2 Delta phi) conspire to produce a curvature-driven motion in the limit.

MCF is therefore the *geometric core* of the AC architecture: it is what AC becomes when the interface width goes to zero. The AC evaluation identified mean-curvature motion (N3 in AC Mode 1) as a necessary configuration — MCF is the architecture that *is* that configuration.

Similarly, the *Mullins–Sekerka problem* (sharp-interface limit of Cahn–Hilliard) is a different geometric flow — not pure MCF but MCF coupled with a bulk diffusion equation. CH in the sharp-interface limit does *not* reduce to MCF alone; it reduces to a more complex free-boundary problem because of the conservation constraint.

### 4.2 MCF vs. Free-Boundary Architectures (PME, TFE)

| Feature                    | MCF                         | PME                        | TFE                        |
|----------------------------|-----------------------------|----------------------------|-----------------------------|
| State variable             | Surface Gamma_t             | Density u(x,t) >= 0       | Height h(x,t) >= 0          |
| Bulk field                 | None                        | Yes (u)                    | Yes (h)                     |
| Free boundary              | *Is* the state              | Boundary of support        | Contact line                |
| Motion law                 | V_n = H (curvature)        | V_n ~ grad(u^{m-1}) (Darcy)| V_n ~ h^n grad(Delta h)   |
| Conservation               | No (area decreases)         | Yes (mass)                 | Yes (mass)                  |
| Gradient flow              | Area functional             | Entropy                    | Surface energy              |
| Singularity                | Finite-time pinch-off       | No singularity             | No singularity (n >= 1)    |
| Topology change            | Yes (through singularity)   | No                         | No                          |

The key distinction: PME and TFE have free boundaries that are *consequences* of a bulk PDE (the boundary is where the bulk field reaches zero). MCF has a free boundary that *is the entire state* — there is no bulk, only the boundary. MCF is *pure geometry*; PME/TFE are *bulk PDEs with geometric consequences*.

### 4.3 MCF vs. NS

MCF and NS are both *geometric* in a sense — NS describes the motion of a fluid (a deformable body), and MCF describes the motion of a surface (a deformable boundary). But the structural differences are profound:

| Feature                    | MCF                         | Navier–Stokes              |
|----------------------------|-----------------------------|----------------------------|
| State variable             | Surface Gamma_t             | Velocity field **u**(x,t)  |
| Dimensionality of state    | (d-1)-dimensional surface   | d-dimensional field        |
| Equation type              | Geometric (V_n = H)        | PDE on fixed domain        |
| Nonlocal channel           | None                        | Pressure (Poisson eq.)     |
| Conservation               | None                        | Mass + momentum            |
| Gradient flow              | Yes (area)                  | No                         |
| Turbulence                 | No                          | Yes                        |
| Singularity                | Yes (finite-time)           | Open (3D)                  |
| Topology change            | Yes                         | No (incompressible)        |

MCF is *simpler* than NS (fewer degrees of freedom, gradient-flow structure, no nonlocal channel) but has a *harder singularity problem* (MCF singularities definitely occur; NS singularities are unknown). The MCF singularity is not an architectural failure — it is the architecture completing its program of area minimization.

### 4.4 MCF and ED: Geometry and Boundaries

The FS/ED framework is built on the *skyline* — a geometric object (the boundary profile of the integer columns). MCF is the *evolution* of a geometric boundary. The structural parallel:

- ED: a fixed geometric boundary (the skyline profile), shaped by arithmetic (factorization).
- MCF: an evolving geometric boundary (the surface Gamma_t), shaped by curvature (geometry).

Both architectures are *boundary-centric*: the boundary is not a secondary feature derived from a bulk field; it is the *primary object*. In ED, the skyline boundary encodes the multiplicative structure of the integers. In MCF, the surface boundary evolves under its own geometric law. Both are *pure boundary architectures* — the only two in the Atlas.

### 4.5 Positioning Table

| Feature                    | MCF              | AC       | CH       | PME      | TFE      | FP       | NS       | RD       |
|----------------------------|------------------|----------|----------|----------|----------|----------|----------|----------|
| State variable             | **Surface**      | Field    | Field    | Field    | Field    | Field    | Field    | Field    |
| Bulk PDE                   | **None**         | Yes      | Yes      | Yes      | Yes      | Yes      | Yes      | Yes      |
| Dimensionality             | d-1              | d        | d        | d        | d        | d        | d        | d        |
| Curvature-driven           | **Yes (V_n=H)**  | Limit    | Limit    | No       | No       | No       | No       | No       |
| Conservation               | **No**           | No       | Yes      | Yes      | Yes      | Yes      | Yes      | Constitutive |
| Gradient flow              | Area (L^2)       | F (L^2)  | F (H^{-1})| H (Wass.)| E (wt H^{-1})| F (Wass.)| No  | Gen. no  |
| Finite-time singularity    | **Yes (certain)**| No       | No       | No       | No       | No       | Open(3D) | Constitutive |
| Topology change            | **Yes**          | No       | No       | No       | No       | No       | No       | No       |
| Linearity                  | Quasilinear      | NL       | NL       | NL       | NL       | Linear   | NL       | NL       |
| Locality                   | Local            | Local    | Local    | Local    | Local    | Local    | Nonlocal | Local    |

MCF is the *only* architecture in the Atlas with:
- A surface (not a field) as the state variable.
- No bulk PDE.
- Definite finite-time singularity (not open or constitutive-dependent, but *certain* for closed convex surfaces).
- Topology change as a structural feature.

---

*End of Architectural Specification. The Mode 1 (Axiom → Envelope) analysis will follow in the next file.*
