# AD Evaluation: Ricci Flow — Architectural Specification

Allen Proxmire

April 2026

---

## 1. Implicit Axioms of the Ricci Flow Architecture

Ricci Flow (RF) describes the evolution of a Riemannian metric g_{ij}(x, t) on a smooth manifold M under the curvature-driven law partial_t g_{ij} = -2 Ric_{ij}. It is the *intrinsic geometric parabolic* equation — the PDE that smooths the *geometry of space itself*, not a field on a fixed space or a surface in an ambient space, but the *metric tensor* that defines distances, angles, and curvature on the manifold. Where MCF smooths the *extrinsic* shape of a surface embedded in Euclidean space, Ricci Flow smooths the *intrinsic* geometry of a Riemannian manifold without reference to any ambient space.

Ricci Flow occupies the *deepest geometric position* in the PDE Atlas. Every other architecture evolves a *field on a fixed domain* (u, phi, psi, rho on R^d) or a *surface in a fixed ambient space* (Gamma_t in R^{d+1} for MCF). Ricci Flow evolves the *domain itself* — the metric g_{ij} that defines what "distance" and "curvature" mean on M. The state variable is not a function or a surface but a *Riemannian metric* — the most fundamental geometric object in differential geometry. The evolution changes the geometry of M: distances stretch or shrink, curvatures flatten or concentrate, and the *topology of space can change* through singularity formation and surgery.

Ricci Flow is the architecture that proved the *Poincare conjecture* (Perelman, 2002–2003) and the *geometrization conjecture* (Thurston's conjecture, proved by Perelman via Ricci Flow with surgery). It is the *only PDE in the Atlas that has resolved a Clay Millennium Problem* — and it did so by evolving a geometry to its canonical form, precisely as the AD evaluation framework examines: the axioms determine the dynamics, the dynamics determine the singularities, and the singularities determine the topology.

### Axiom RF-1: Riemannian Metric g_{ij}(x, t)

The state variable is a smooth Riemannian metric g_{ij}(x, t) on a closed smooth manifold M^n (typically n = 3 for the topological applications). The metric g is a *positive-definite symmetric (0,2)-tensor field* — it assigns an inner product to each tangent space T_x M, defining lengths, angles, volumes, and curvatures at every point.

This is the *most complex state variable* in the PDE Atlas:
- Scalar fields (u, phi, psi, rho): one real number per point. AC, CH, PME, TFE, FP, HJ, Burgers, KdV, KS.
- Vector fields (**u**): d real numbers per point. NS.
- Complex fields (psi): 2 real numbers per point. NLS.
- Surfaces (Gamma_t): a geometric object in ambient space. MCF.
- **Metric tensors (g_{ij}): n(n+1)/2 real numbers per point** (the independent components of a symmetric 2-tensor). For n = 3: 6 components per point. RF.

The metric g_{ij} is not just a collection of numbers — it carries the *full geometric content of M*: the Riemann curvature tensor Rm_{ijkl}, the Ricci tensor Ric_{ij}, the scalar curvature R, geodesics, volumes, and the topology of M (through the Gauss–Bonnet theorem and its generalizations).

### Axiom RF-2: Evolution Equation (∂_t g = -2 Ric)

The metric evolves by:

    partial_t g_{ij} = -2 Ric_{ij}

where Ric_{ij} is the Ricci curvature tensor — a contraction of the Riemann curvature tensor:

    Ric_{ij} = R^k_{ikj} = g^{kl} Rm_{kilj}

The Ricci tensor is the *trace* of the full curvature: it captures the part of the curvature that measures how volumes change under parallel transport (the Ricci tensor determines how a small ball of geodesics expands or contracts relative to flat space). The evolution law:

- Where Ric > 0 (positive curvature): g *shrinks* (the manifold contracts in the positively curved direction).
- Where Ric < 0 (negative curvature): g *grows* (the manifold expands in the negatively curved direction).
- Where Ric = 0 (Ricci-flat): g is *stationary* (the manifold does not evolve). Ricci-flat metrics (e.g., Calabi–Yau metrics) are the *equilibria* of Ricci Flow.

The factor -2 is a normalization convention (matching Hamilton's original formulation).

### Axiom RF-3: Geometric Parabolicity

The Ricci Flow equation partial_t g_{ij} = -2 Ric_{ij} is *weakly parabolic* — parabolic modulo the diffeomorphism gauge. The Ricci tensor Ric_{ij}(g) depends on g and its first and second derivatives (through the Christoffel symbols and their derivatives), making the evolution equation *second-order in g*. However, the Ricci tensor is *not elliptic* as a function of g — it is degenerate due to the diffeomorphism invariance (RF-4).

The DeTurck trick: by adding a Lie derivative term (a diffeomorphism gauge-fixing), the equation can be made *strictly parabolic*:

    partial_t g_{ij} = -2 Ric_{ij} + L_X g_{ij}

where X is a vector field depending on g and a fixed background metric. The DeTurck-modified flow is a *strictly parabolic system* — a nonlinear heat equation for the metric components. This gives short-time existence and uniqueness (Hamilton, 1982).

The geometric parabolicity means: *Ricci Flow is the heat equation for Riemannian metrics*. Just as the heat equation Delta u smooths a scalar field, Ricci Flow smooths a metric — reducing curvature inhomogeneities, flattening bumps, and driving the geometry toward uniformity.

### Axiom RF-4: Diffeomorphism Invariance (Gauge Freedom)

The Ricci Flow equation is *diffeomorphism-invariant*: if g(t) is a solution and phi : M → M is a diffeomorphism, then phi*g(t) (the pullback metric) is also a solution. This is the *gauge freedom* of Ricci Flow — analogous to the tangential reparametrization freedom in MCF and the gauge freedom in Yang–Mills theory.

The gauge freedom means that Ricci Flow does not determine the *coordinates* on M — only the *geometry* (the equivalence class of metrics modulo diffeomorphisms). The DeTurck trick fixes the gauge, making the equation strictly parabolic, but the underlying geometric content is gauge-invariant.

### Axiom RF-5: Curvature-Driven Dissipation

The Ricci Flow is a *curvature smoother*: it reduces curvature inhomogeneities over time. The key estimates:

- **Maximum principle for scalar curvature:** R_min(t) is non-decreasing. The minimum scalar curvature increases (or stays constant). Regions of very negative curvature are smoothed out.
- **Hamilton's curvature estimates:** The Riemann curvature tensor satisfies parabolic evolution equations with quadratic reaction terms. Under appropriate curvature conditions (e.g., positive curvature operator, positive isotropic curvature), the curvature ratios improve over time (pinching estimates).
- **Perelman's monotonicity:** The W-entropy and the reduced volume are monotone quantities that control the geometry near singularities (see RF-10 refinement below).

The curvature smoothing is the RF analogue of the diffusion smoothing in FP/PME and the area dissipation in MCF. The mechanism is *parabolic*: the Ricci tensor acts like a Laplacian on the metric, spreading curvature from regions of high concentration to regions of low concentration.

### Axiom RF-6: Volume Evolution

The volume of M evolves as:

    d/dt Vol(M, g(t)) = -integral_M R dmu_g

where R is the scalar curvature and dmu_g is the volume form of g. The volume:
- *Decreases* when R > 0 (positive average curvature — the manifold is "too curved" and shrinks).
- *Increases* when R < 0 (negative average curvature — the manifold is "too flat" in a hyperbolic sense and expands).
- Is *constant* when the average R equals zero.

For the *normalized Ricci Flow* (partial_t g = -2 Ric + (2r/n) g, where r = integral R / Vol is the average scalar curvature), the volume is constant. The normalized flow is used for long-time analysis on closed manifolds.

### Axiom RF-7: Singularities via Curvature Blowup

Ricci Flow can develop *singularities* in finite time — points where the curvature tensor Rm blows up:

    sup_M |Rm(t)| → infinity    as t → T*

The singularity types (for 3-manifolds, classified by Hamilton and Perelman):

- **Type I (self-similar shrinking):** |Rm| ~ 1/(T* - t). The blowup rate is self-similar. The rescaled geometry near the singularity converges to a *gradient shrinking soliton* (a self-similar Ricci Flow solution). Examples: shrinking round sphere S^3, shrinking cylinder S^2 x R.

- **Type II (faster-than-self-similar):** |Rm|(T* - t) → infinity. The blowup is faster than self-similar. The rescaled geometry converges to an *ancient solution* (a solution defined for all t in (-infinity, T*)). Example: the Bryant soliton.

- **Neck singularity:** The manifold develops a long, thin neck (approximately S^2 x R) that pinches to zero radius. This is the generic singularity type for 3-manifolds.

- **Extinction singularity:** The entire manifold shrinks to a round point (like MCF's convex surface extinction). Occurs for manifolds with positive Ricci curvature (Hamilton, 1982: 3-manifolds with Ric > 0 converge to round S^3).

### Axiom RF-8: Scaling Symmetry

Ricci Flow has the parabolic scaling symmetry:

    g_lambda(x, t) = lambda g(x, lambda t)

If g(t) is a solution, then lambda g(lambda t) is also a solution (with rescaled time). This is the same parabolic scaling as the heat equation (space scales as lambda^{1/2}, time as lambda).

The scaling symmetry identifies the *critical dimension* of the curvature: Rm has dimensions [length]^{-2}, so |Rm| g has dimension [length]^0 — the quantity |Rm| is scale-invariant in the appropriate sense.

### Axiom RF-9: No External Forcing

Ricci Flow is *autonomous*: the metric evolves under its own curvature, with no external forcing, no boundary conditions (on closed manifolds), and no prescribed fields. The evolution is *self-generated* — the curvature of the metric drives the metric's evolution, which changes the curvature, which drives the evolution.

### Axiom RF-10: Perelman's Entropy and Gradient-Flow Structure

Perelman (2002) discovered that Ricci Flow has a *deep variational structure*:

**Perelman's F-functional:**

    F(g, f) = integral_M (R + |nabla f|^2) e^{-f} dmu_g

is monotone non-decreasing under the coupled system partial_t g = -2 Ric, partial_t f = -Delta f + |nabla f|^2 - R.

**Perelman's W-entropy:**

    W(g, f, tau) = integral_M [tau(R + |nabla f|^2) + f - n] (4 pi tau)^{-n/2} e^{-f} dmu_g

is monotone non-decreasing under the coupled system (with tau = T* - t).

**Gradient-flow interpretation:** The Ricci Flow is the *gradient flow of the F-functional* on the space of Riemannian metrics modulo diffeomorphisms. This is not a classical gradient flow (the space of metrics is infinite-dimensional and not a vector space) but a *formal gradient flow* in a precise sense identified by Perelman.

The Perelman monotonicity formulas are the *deepest structural tools* of Ricci Flow — they control the geometry near singularities, prevent *collapsing* (the manifold cannot become infinitely thin without curvature blowup), and enable the classification of singularity types. They play the role that Huisken's monotonicity formula plays in MCF and that the log-HLS inequality plays in KS.

---

## 2. Canonical PDE in Architectural Form

### 2.1 The Ricci Flow Equation

    partial_t g_{ij} = -2 Ric_{ij}(g)                              ... (RF)

where Ric_{ij}(g) is the Ricci curvature of the metric g. In local coordinates:

    Ric_{ij} = partial_k Gamma^k_{ij} - partial_j Gamma^k_{ik} + Gamma^k_{kl} Gamma^l_{ij} - Gamma^k_{jl} Gamma^l_{ik}

with Christoffel symbols Gamma^k_{ij} = (1/2) g^{kl}(partial_i g_{jl} + partial_j g_{il} - partial_l g_{ij}).

### 2.2 DeTurck-Modified (Strictly Parabolic) Form

    partial_t g_{ij} = -2 Ric_{ij} + nabla_i V_j + nabla_j V_i

where V^k = g^{pq}(Gamma^k_{pq} - tilde{Gamma}^k_{pq}) is the DeTurck vector field (difference of Christoffel symbols with a fixed background metric tilde{g}). This is a *strictly parabolic system* — a nonlinear heat equation for the metric components.

### 2.3 Channel-Labeled Decomposition

    partial_t g_{ij} =    -2 Ric_{ij}
                      |________________________|
                        Curvature-driven evolution (C)

    modulo:    diffeomorphism gauge (D)
             |___________________________|

    producing:
      Curvature smoothing (P, parabolic)     Curvature blowup (S, singularity)
    |____________________________________|  |___________________________________|

    controlled by:
      Perelman's W-entropy (monotone)    Perelman's reduced volume (no-collapsing)
    |_____________________________________|

### 2.4 Self-Similar Solutions (Ricci Solitons)

A *Ricci soliton* is a self-similar solution of Ricci Flow:

    Ric + (1/2) L_X g = lambda g

where X is a vector field and lambda is a constant. Soliton types:
- **Shrinking** (lambda > 0): the metric shrinks self-similarly. Examples: round sphere S^n, cylinder S^{n-1} x R.
- **Steady** (lambda = 0): the metric is stationary modulo diffeomorphisms. Example: Bryant soliton.
- **Expanding** (lambda < 0): the metric expands self-similarly.

Ricci solitons are the RF analogues of:
- MCF self-similar shrinkers (sphere, cylinder, Angenent torus).
- KdV solitons (sech^2).
- NLS solitons (sech).
- PME Barenblatt profiles.

They are the *canonical blowup profiles* near singularities: rescaled Ricci Flow near a singularity converges to a Ricci soliton.

---

## 3. Channel Identification

### Channel C: Curvature Evolution

    C(g) = -2 Ric_{ij}(g)

- **Role:** The sole dynamical mechanism. The Ricci curvature drives the metric evolution: positive curvature → shrinkage, negative curvature → expansion, zero curvature → stationarity. The Ricci tensor acts as a *geometric Laplacian* on the metric — it is the trace of the Riemann curvature, which involves second derivatives of g, making the evolution *second-order parabolic* (modulo gauge).
- **Locality:** Local. Ric_{ij}(g) depends on g and its first and second derivatives at each point. No nonlocal coupling — the curvature at x is determined by the metric in an infinitesimal neighborhood of x.
- **Linearity:** Nonlinear. Ric_{ij} is a *quasilinear* function of g — linear in the second derivatives of g but with coefficients depending on g itself (through the inverse metric g^{kl} and the Christoffel symbols). The same quasilinear structure as MCF (V_n = H is quasilinear in the embedding F).
- **Stability role:** *Dual-natured.* The curvature channel is:
  - *Stabilizing (smoothing):* In the sense that it acts like a heat equation on the metric — spreading curvature, reducing gradients, flattening bumps. Hamilton's maximum principles show that certain curvature conditions (positive Ricci, positive sectional curvature) are *preserved and improved* by the flow.
  - *Destabilizing (concentrating):* The quadratic reaction terms in the curvature evolution (Rm * Rm) can amplify curvature, driving it to infinity in finite time → singularity formation.

  The dual nature (smoothing + concentrating) is the structural tension that produces the rich dynamics of Ricci Flow.

- **Scale action:** The Ricci tensor has dimension [length]^{-2}, so the evolution rate is ~ |Ric| ~ |Rm| ~ 1/L^2 at curvature scale L. Regions of high curvature (small L) evolve fastest. The flow has the parabolic scaling t ~ L^2 — the same as MCF, FP, PME, and the heat equation.

### Channel D: Diffeomorphism Gauge

    D: g_{ij} → phi*g_{ij}    for any diffeomorphism phi : M → M

- **Role:** Gauge freedom. The Ricci Flow equation is invariant under diffeomorphisms — changing coordinates does not change the geometric content. The gauge must be fixed (e.g., by the DeTurck trick) to make the equation strictly parabolic.
- **Locality:** The gauge transformation phi*g is local in the sense that it involves g and the Jacobian of phi at each point.
- **Linearity:** The gauge group (Diff(M)) is *nonlinear* — diffeomorphisms do not form a vector space.
- **Stability role:** Neutral. The gauge does not stabilize or destabilize — it is a *redundancy* in the description, not a dynamical force.
- **Scale action:** The gauge freedom is scale-free — it applies at every scale.

### Channel P: Parabolic Smoothing

    P: partial_t g ~ Delta_L g + lower-order terms

where Delta_L is the *Lichnerowicz Laplacian* — the geometric Laplacian acting on symmetric 2-tensors. In the DeTurck-modified flow, the highest-order term is the Lichnerowicz Laplacian, which provides *second-order parabolic smoothing* of the metric.

- **Role:** The regularizing mechanism. The parabolic smoothing:
  - Gives *short-time existence and uniqueness* (Hamilton, 1982).
  - *Smooths* the metric: if g_0 is C^k (k >= 2), then g(t) is C^{infinity} for t > 0.
  - Provides *curvature bounds* through maximum principles and integral estimates.
- **Locality:** Local (the Lichnerowicz Laplacian is a second-order local operator).
- **Linearity:** Linear (as a differential operator on symmetric 2-tensors). The nonlinearity enters through the lower-order (reaction) terms.
- **Stability role:** Stabilizing. The parabolic smoothing is the *primary regularizing mechanism* — it is what makes Ricci Flow work as a geometric tool.
- **Scale action:** Damping rate ~ k^2 (second-order parabolic). High-frequency geometric oscillations are smoothed fastest.

### Channel S: Singularity Formation

    S: sup_M |Rm(t)| → infinity    as t → T*

- **Role:** The emergent consequence of the curvature channel's dual nature. When the curvature concentration (quadratic reaction terms Rm * Rm) overwhelms the curvature smoothing (Lichnerowicz Laplacian), the curvature blows up in finite time.
- **Locality:** Local trigger (curvature concentrates at specific points or regions). Global consequence (the singularity can change the topology of M through surgery).
- **Linearity:** Nonlinear (emerges from the quadratic Rm * Rm reaction in the curvature evolution).
- **Stability role:** Destabilizing (loss of smooth metric). But *structurally necessary* (like MCF's curvature blowup): the singularity is the mechanism by which Ricci Flow resolves topological complexity and drives M toward its canonical geometric form.
- **Scale action:** Concentrates at the smallest scales. Near the singularity, the curvature blows up as |Rm| ~ 1/(T* - t), and the geometry approaches a Ricci soliton at scale sqrt(T* - t).

### Channel Summary Table

| Channel | Symbol | Feature                       | Locality | Linearity    | Stability              | Scale Action        |
|---------|--------|-------------------------------|----------|--------------|------------------------|---------------------|
| Curvature    | C | -2 Ric_{ij}                 | Local    | Quasilinear  | Dual (smooth + concentrate) | Rate ~ 1/L^2    |
| Gauge        | D | Diffeomorphism invariance    | Local    | Nonlinear    | Neutral (redundancy)   | Scale-free          |
| Parabolic    | P | Lichnerowicz Laplacian       | Local    | Linear       | Stabilizing (smoothing)| Rate ~ k^2          |
| Singularity  | S | Curvature blowup             | Local*   | Nonlinear    | Necessary (topology change)| Concentrates at small scale |

*Local trigger, global (topological) consequence.

---

## 4. Relation to FP, PME, HJ, Burgers, NLS, KdV, NS, MCF, AC/CH, TFE, RD, KS, and ED

### 4.1 Ricci Flow as the Intrinsic Geometric Parabolic Pole

The PDE Atlas now has a *hierarchy of geometric architectures*:

**Extrinsic geometry:** MCF (V_n = H) — evolves a surface *in* ambient space. The state is an embedding F : M → R^{d+1}.

**Intrinsic geometry:** Ricci Flow (partial_t g = -2 Ric) — evolves the geometry *of* a manifold, without reference to any ambient space. The state is a metric g_{ij} on M.

MCF smooths the *extrinsic shape* of a codimension-1 surface. Ricci Flow smooths the *intrinsic geometry* of an n-dimensional manifold. Both are curvature-driven, parabolic, and produce singularities — but at different structural levels:

| Feature                    | MCF                          | Ricci Flow                    |
|----------------------------|------------------------------|-------------------------------|
| State variable             | Embedding F (surface in R^{d+1}) | Metric g_{ij} (intrinsic geometry) |
| Curvature type             | Extrinsic (mean curvature H) | Intrinsic (Ricci curvature Ric) |
| Ambient space              | Required (R^{d+1})          | Not needed (intrinsic)         |
| Smoothing mechanism        | Curvature flow on surface    | Heat equation for metric       |
| Singularity type           | Curvature blowup → pinch    | Curvature blowup → neck/extinction |
| Surgery                    | Huisken–Sinestrari           | Hamilton–Perelman              |
| Canonical form             | Round sphere (extinction)    | Constant curvature / geometric pieces |
| Topological consequence    | Genus reduction              | **Geometrization (topology classified)** |
| Millennium Problem         | No                           | **Yes (Poincare conjecture)** |

Ricci Flow is *structurally deeper* than MCF: it operates on the *intrinsic geometry of space*, not on the shape of a surface in a fixed space. The topological consequences are correspondingly deeper: MCF simplifies surfaces (genus reduction); Ricci Flow *classifies 3-manifolds* (the geometrization theorem).

### 4.2 RF vs. FP/PME: Heat Equation for Metrics

Ricci Flow is the *geometric analogue* of the heat equation:

    Heat equation: partial_t u = Delta u                (smooths a scalar field)
    Ricci Flow:    partial_t g_{ij} = -2 Ric_{ij}       (smooths a metric tensor)

Both are second-order parabolic, both smooth their state variable, and both have short-time existence and uniqueness. The structural difference: the heat equation is *linear* (no singularities); Ricci Flow is *quasilinear* (the coefficients depend on the solution through the metric). The quasilinearity produces the *curvature reaction terms* (Rm * Rm) that can drive singularity formation — absent in the linear heat equation.

The relationship to FP/PME is:
- FP: the *linear* heat equation for probability densities.
- PME: the *nonlinear* heat equation for densities (degenerate diffusion).
- **RF: the *geometric* heat equation for metrics (curvature-driven diffusion).**

### 4.3 RF vs. NS: Two Complex PDE Architectures

RF and NS are the *two most structurally complex* PDE architectures in the Atlas:

| Feature                    | Ricci Flow                    | Navier–Stokes              |
|----------------------------|-------------------------------|-----------------------------|
| State variable             | Metric tensor g_{ij} (6 comp.)| Velocity vector u_i (3 comp.) |
| Nonlinearity               | Quasilinear (Ric(g))         | Quadratic (u . nabla u)     |
| Nonlocal channel           | None (fully local)            | Pressure (Poisson eq.)      |
| Gauge freedom              | Diffeomorphisms               | Pressure gauge               |
| Smoothing                  | Parabolic (Lichnerowicz)      | Parabolic (viscosity)       |
| Singularity                | Certain (3D, positive curv.)  | Open (3D)                   |
| Surgery                    | Hamilton–Perelman              | No surgery theory            |
| Topological consequence    | Geometrization theorem         | None                        |
| Gradient-flow structure    | Yes (Perelman F-functional)   | No                           |
| Millennium Problem         | Solved (Poincare)              | Open (regularity)           |

Both are quasilinear, parabolic, and develop singularities in 3D. But Ricci Flow has a *resolved singularity theory* (Perelman's surgery program classifies and resolves all singularities), while NS does not. The structural tool that makes Ricci Flow tractable — Perelman's entropy monotonicity — has no analogue in the NS architecture. Ricci Flow demonstrates that *geometric PDE singularities can be completely resolved* even when they are as complex as the NS singularities.

### 4.4 RF and KS: Curvature Concentration vs. Mass Concentration

RF and KS share a structural parallel: both have a *competing smoothing-concentration* dynamic, both develop *singularities through concentration*, and both have *sharp criteria* for singularity formation:

| Feature                    | Ricci Flow                    | Keller–Segel                  |
|----------------------------|-------------------------------|-------------------------------|
| Smoothing mechanism        | Lichnerowicz Laplacian        | Diffusion Delta u             |
| Concentration mechanism    | Curvature reaction (Rm^2)     | Nonlocal aggregation          |
| What concentrates          | Curvature                     | Mass (density)                |
| Singularity type           | Curvature blowup             | Mass delta                    |
| Critical threshold         | Curvature pinching conditions | M = 8 pi (2D)               |
| Nonlocality                | None (fully local)            | Two nonlocal channels         |
| Surgery                    | Hamilton–Perelman              | Measure-valued continuation   |

Both architectures demonstrate the *smoothing-concentration duality*: a stabilizing mechanism (parabolic smoothing) competing with a destabilizing mechanism (curvature reaction / nonlocal aggregation), with the outcome determined by a critical condition.

### 4.5 RF and ED: Topological Classification

The deepest connection between Ricci Flow and ED is *classificatory*: both architectures *classify their objects*:

- **ED:** The fundamental theorem of arithmetic classifies every integer by its prime factorization.
- **KdV:** The IST classifies every solution by its scattering data (solitons + radiation).
- **RF:** The geometrization theorem classifies every closed 3-manifold by decomposition into geometric pieces.

Ricci Flow + surgery *classifies the topology of 3-manifolds* — the most profound classificatory achievement in the Atlas. The flow evolves the metric to its canonical geometric form, the singularities reveal the topological decomposition, and the surgery resolves the singularities while preserving the classification. The result: every closed 3-manifold is decomposed into pieces, each carrying one of Thurston's eight model geometries.

### 4.6 Positioning Table

| Feature                    | RF               | MCF      | FP/PME   | NS       | NLS      | KdV      | KS       | HJ/Burg. |
|----------------------------|------------------|----------|----------|----------|----------|----------|----------|----------|
| State variable             | **Metric g_{ij}**| Surface  | Scalar   | Vector   | Complex  | Scalar   | Scalar   | Scalar   |
| Components per point       | **n(n+1)/2**    | d+1      | 1        | d        | 2        | 1        | 1        | 1        |
| Curvature type             | **Intrinsic (Ric)** | Extrinsic (H) | N/A | N/A    | N/A      | N/A      | N/A      | N/A      |
| Ambient space              | **None needed**  | Required | N/A      | Fixed    | Fixed    | Fixed    | Fixed    | Fixed    |
| Parabolic smoothing        | Yes (Lichnerowicz)| Yes (H) | Yes (Delta)| Yes (nu Delta) | No | No   | Yes (Delta)| No     |
| Singularity                | Certain (3D)     | Certain  | No       | Open(3D) | Foc.d>=2 | No       | M>8pi    | Certain  |
| Surgery                    | **Hamilton–Perelman** | Huisken–Sinestrari | N/A | No | No | No    | Measure  | No       |
| Topological result         | **Geometrization**| Genus reduction | N/A | N/A   | N/A      | N/A      | N/A      | N/A      |
| Gradient-flow structure    | **Perelman F**   | Area (L^2) | Wasserstein | No   | Hamiltonian | Hamiltonian | Wasserstein | Variational |
| Monotone formula           | **Perelman W + reduced vol** | Huisken Theta | Entropy | N/A | Conserved | Conserved | Log-HLS | Hopf–Lax |
| Millennium Problem         | **Solved**       | No       | No       | Open     | No       | No       | No       | No       |
| Locality                   | Fully local      | Local    | Local    | Nonlocal | Local    | Local    | Nonlocal | Local    |
| Parameters                 | **0**            | 0        | 1-2      | 2        | 1        | 0        | 0-1      | 0        |

Ricci Flow is the *unique intrinsic-geometric, metric-tensor-valued, curvature-driven, diffeomorphism-invariant, surgery-requiring, topology-classifying, Millennium-Problem-solving* architecture in the Atlas. It is structurally the *deepest* PDE ever evaluated — operating not on fields or surfaces but on the fabric of space itself.

---

*End of Architectural Specification. The Mode 1 (Axiom → Envelope) analysis will follow in the next file.*
