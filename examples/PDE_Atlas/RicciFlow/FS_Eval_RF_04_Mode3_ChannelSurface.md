# AD Evaluation: Ricci Flow — Mode 3: Channels → Constraint Surface

Allen Proxmire

April 2026

---

## Overview

Mode 3 constructs the constraint surface of the Ricci Flow architecture. The RF constraint surface is the *most geometrically profound* of any PDE in the PDE Atlas: it is defined not on a function space (like every scalar or vector PDE) or a space of surfaces (like MCF) but on the *space of Riemannian metrics modulo diffeomorphisms* — the infinite-dimensional space of geometries on a manifold. The constraint surface's topology, singularity structure, and closure properties are all *intrinsically geometric* — they describe properties of *space itself*, not of fields or shapes.

The RF constraint surface has a *fully classified singularity face* — the only PDE in the Atlas where every singularity type is completely characterized (Type I: shrinking solitons; Type II: ancient solutions; complete for n = 3). The singularity face is not open (like NS's enstrophy gap) or constitutive (like RD's blowup possibilities) but *resolved*: every singularity is classified, every blowup limit is identified, and the surgery procedure provides a geometric continuation past every singularity.

We continue with:

    partial_t g_{ij} = -2 Ric_{ij}(g)

---

## 1. Channel Decomposition

### Channel C: Curvature Smoothing

    C(g) = Delta_L g    [Lichnerowicz Laplacian, the leading-order term of -2 Ric]

- **Locality:** Local. The Lichnerowicz Laplacian involves g and its first and second derivatives at each point. No nonlocal coupling.
- **Linearity:** Linear (as a differential operator on symmetric 2-tensors). The Lichnerowicz Laplacian Delta_L h_{ij} = Delta h_{ij} + 2 Rm_{ikjl} h^{kl} - Ric_{ik} h^k_j - Ric_{jk} h^k_i is a *linear second-order elliptic operator* on the space of symmetric 2-tensors, with coefficients depending on g.
- **Stability role:** Stabilizing. The curvature smoothing damps high-frequency metric perturbations at rate k^2 (second-order parabolic). It smooths the metric, reduces curvature inhomogeneities, and drives the geometry toward uniformity. The smoothing is the *primary regularizing mechanism* — the reason RF has short-time existence (Hamilton 1982) and instantaneous C^{infinity} regularization.
- **Scale action:** Rate ~ k^2 at wavenumber k. High-frequency geometric oscillations are damped fastest. At curvature scale L_curv = 1/sqrt(|Rm|): smoothing rate ~ |Rm| (faster at higher curvature, but the reaction term also grows — producing the competition).
- **Interaction with R:** The smoothing and reaction channels compete: C damps curvature fluctuations; R amplifies them. The competition determines whether the geometry smooths (C wins → uniformization) or concentrates (R wins → singularity). The outcome depends on the *algebraic structure* of the curvature tensor — positive curvature pinches (smooths toward a sphere); mixed curvature can develop necks (concentrates along thin cylinders).

### Channel R: Curvature Reaction

    R(g): the Rm * Rm terms in partial_t Rm = Delta Rm + Rm * Rm

- **Locality:** Local. The reaction terms involve algebraic combinations of the Riemann curvature tensor at each point — no derivatives of Rm, no nonlocal coupling.
- **Linearity:** Nonlinear. The reaction terms are *quadratic* in Rm — the product of curvature with itself. This is the RF's sole nonlinear mechanism (the Lichnerowicz Laplacian is linear; the nonlinearity enters through the quadratic curvature reaction).
- **Stability role:** Dual-natured:
  - *Stabilizing (pinching):* For positive curvature, the Rm * Rm reaction *improves* the curvature pinching — the eigenvalues of the curvature operator become more nearly equal. Hamilton's pinching estimates show that positive Ricci curvature becomes more isotropic under the flow.
  - *Destabilizing (concentrating):* The quadratic growth rate |Rm|^2 can overwhelm the linear smoothing rate |Rm|, driving the curvature to infinity. The reaction term is the *singularity engine* — the mechanism by which RF develops curvature blowup.
- **Scale action:** The reaction rate is ~ |Rm|^2 ~ 1/L_curv^4, growing as the *fourth power* of the inverse curvature scale. At high curvature (small L_curv), the reaction dominates the smoothing (which grows only as 1/L_curv^2). The crossover occurs at L_curv ~ 1/sqrt(|Rm|) — the scale where smoothing and reaction are commensurate.
- **Interaction with C:** The C-R competition is the *fundamental dynamical tension* of RF:
  - Low curvature (|Rm| small): C dominates → smoothing → uniformization.
  - High curvature (|Rm| large): R dominates → concentration → singularity.
  - The transition between the two regimes is controlled by Perelman's monotone quantities (which prevent the transition from being uncontrolled).

### Channel D: Diffeomorphism Gauge

    D(g) = L_X g = nabla_i X_j + nabla_j X_i    [Lie derivative, DeTurck vector field]

- **Locality:** Local. The Lie derivative involves the vector field X and first derivatives of g at each point.
- **Linearity:** Linear in X (but X depends on g through the DeTurck construction).
- **Stability role:** Neutral. The gauge term is a *diffeomorphism* — it changes the coordinate representation of g without changing the geometry. Adding L_X g to the evolution is equivalent to applying a time-dependent diffeomorphism to the solution. The gauge term:
  - Converts the *weakly parabolic* RF (degenerate due to diffeomorphism invariance) into a *strictly parabolic* system (the DeTurck-modified flow).
  - Does not change any geometric quantity (curvature, volume, topology).
  - Is the *structural resolution of the gauge degeneracy* — the RF analogue of fixing the Coulomb gauge in electromagnetism or choosing harmonic coordinates in general relativity.
- **Scale action:** Scale-free. The gauge freedom applies at every scale.

### Channel S: Singularity Formation

    S: sup_M |Rm(g(t))| → infinity    as t → T*

- **Locality:** Local in trigger (curvature concentrates at specific points or regions). Global in consequence (the singularity changes the topology of M through surgery).
- **Linearity:** Nonlinear (emerges from the quadratic Rm * Rm reaction overwhelming the linear Delta_L smoothing).
- **Stability role:** *Structurally necessary.* The singularity is not an anomaly but the *mechanism by which RF reveals the topological structure* of M. Each singularity corresponds to a topological feature (a connected-sum factor, a handle, a spherical component) that the surgery procedure resolves. Without singularities, RF could not classify topology — the singularities are the *information-bearing events* that encode the topological decomposition.
- **Scale action:** Concentrates at the smallest scales. Near the singularity: |Rm| ~ 1/(T* - t) (Type I) or faster (Type II). The curvature scale L_curv = 1/sqrt(|Rm|) → 0 as t → T*. The geometry approaches a *canonical model* at the shrinking scale.
- **Interaction with all channels:** Channel S is the *terminal outcome* of the C-R competition when R wins. It is the structural partner of Channel D (gauge): the gauge resolves the *coordinate ambiguity*; the singularity resolves the *topological ambiguity*. Together, D and S handle the two fundamental redundancies of the RF architecture: diffeomorphism invariance (resolved by DeTurck) and topological complexity (resolved by surgery at singularities).

### Channel Summary Table

| Channel | Symbol | Feature                       | Locality | Linearity    | Stability              | Scale Action              |
|---------|--------|-------------------------------|----------|--------------|------------------------|---------------------------|
| Curvature smoothing | C | Delta_L g             | Local    | Linear       | Stabilizing            | Rate ~ k^2 (~ |Rm|)     |
| Curvature reaction  | R | Rm * Rm                | Local    | Nonlinear    | Dual (pinch + concentrate) | Rate ~ |Rm|^2          |
| Diffeomorphism gauge| D | L_X g                  | Local    | Linear in X  | Neutral (gauge)        | Scale-free                |
| Singularity         | S | |Rm| → infinity         | Local*   | Nonlinear    | Necessary (topology)   | Concentrates at L_curv → 0 |

*Local trigger, global (topological) consequence.

### Channel Count Comparison

| Architecture | Smoothing | Reaction/Concentration | Gauge | Singularity | Total |
|-------------|-----------|------------------------|-------|-------------|-------|
| **RF**      | **1 (C)** | **1 (R)**              | **1 (D)** | **1 (S)** | **4** |
| MCF         | 1 (K)     | 0 (curvature is the smoothing) | 0 | 1 (T) | 3 |
| NLS         | 1 (D)     | 1 (N)                  | 1 (G) | 0-1         | 3-4   |
| KdV         | 1 (D_3)   | 1 (A)                  | 0     | 0            | 2+2   |
| FP          | 1 (D)     | 0                      | 0     | 0            | 2+2   |
| NS          | 1 (V)     | 1 (A)                  | 1 (P) | 0-1          | 4-5   |

RF has four channels — comparable to NLS and NS. The distinctive feature is the *geometric character* of every channel: the smoothing is *curvature diffusion* (not scalar diffusion), the reaction is *curvature-curvature interaction* (not a constitutive nonlinearity), the gauge is *diffeomorphism invariance* (not pressure or phase), and the singularity is *curvature blowup with topological consequence* (not gradient steepening or amplitude concentration).

---

## 2. Dissipation Geometry

### 2.1 Geometric Dissipation: Curvature Smoothing

The RF dissipation acts on the *curvature of space* — the most intrinsic quantity in Riemannian geometry. The dissipation mechanism:

1. The Lichnerowicz Laplacian Delta_L spreads curvature from regions of high concentration to regions of low concentration (curvature diffusion).
2. The spreading reduces curvature gradients (nabla Rm decreases in appropriate norms — Shi estimates).
3. The overall curvature inhomogeneity decreases (the metric becomes more uniform).

This is the *most intrinsic dissipation* in the Atlas: it acts on the *geometry of space itself*, not on a field defined on space (FP/PME), a surface embedded in space (MCF), or a velocity field on space (NS).

### 2.2 The Curvature Competition

The RF dissipation has a *dual character*:

**Smoothing (Channel C):** Delta_L Rm damps curvature at rate ~ |Rm|. The smoothing is *linear in Rm* — it acts uniformly on all curvature components, reducing inhomogeneity.

**Reaction (Channel R):** Rm * Rm amplifies curvature at rate ~ |Rm|^2. The reaction is *quadratic in Rm* — it grows faster than the smoothing at high curvature. The reaction term has a *specific algebraic structure*: it depends on the type of curvature (positive, negative, mixed, isotropic, anisotropic). Different curvature types produce different reaction dynamics:

- **Positive isotropic curvature:** The reaction term *improves pinching* — the curvature becomes more isotropic (all sectional curvatures approach each other). The reaction is *stabilizing* for isotropic positive curvature.
- **Positive anisotropic curvature:** The reaction can *amplify anisotropy* in some directions while reducing it in others. The net effect depends on the specific curvature eigenvalues.
- **Mixed curvature:** The reaction can produce *curvature concentration* — regions of high positive curvature next to regions of low or negative curvature create a gradient that the reaction amplifies.

The competition between C and R is *not a simple scalar balance* (as in KS, where diffusion competes with aggregation through a single scalar M) but a *tensorial balance* — the competition depends on the *full algebraic structure* of the curvature tensor at each point. This tensorial complexity is what makes RF's singularity structure richer than any scalar PDE's.

### 2.3 Perelman's Monotonicity as Dissipation Control

The Perelman monotone quantities (F, W, reduced volume) control the curvature competition:

**F-functional:** dF/dt = 2 integral |Ric + Hess(f)|^2 e^{-f} dmu >= 0. The F-functional *increases*, identifying the *direction of geometric improvement*. Equality holds for gradient steady solitons — the geometric equilibria.

**W-entropy:** dW/dt >= 0. The W-entropy increases, controlling the *scale-dependent geometry* near singularities. Equality holds for gradient shrinking solitons — the canonical singularity models.

**Reduced volume:** tilde{V}(tau) non-increasing. The reduced volume controls the *spacetime-localized geometry*, preventing the manifold from collapsing (becoming infinitely thin without curvature blowing up).

Together, these three quantities form a *dissipation hierarchy*:
- F controls the *global* geometry (integral estimate).
- W controls the *scale-dependent* geometry (localized at scale sqrt(tau)).
- tilde{V} controls the *spacetime-localized* geometry (localized in both space and time).

### 2.4 Comparison of Dissipation Geometries

| Architecture | Dissipation Acts On             | Intrinsic Level        | Control Tools              |
|-------------|----------------------------------|------------------------|----------------------------|
| FP          | Scalar density rho               | Field on domain        | Entropy, Fisher info       |
| PME         | Scalar density u                 | Field on domain        | Entropy, L^1 contraction   |
| AC/CH       | Order parameter phi              | Field on domain        | Ginzburg-Landau F          |
| MCF         | Extrinsic curvature H            | Surface in space       | Area, Huisken Theta        |
| KS          | Density u (via nonlocal v)       | Field + nonlocal coupling | Free energy, log-HLS    |
| NS          | Velocity **u**                   | Vector field on domain | Energy inequality          |
| **RF**      | **Intrinsic curvature Rm**       | **Geometry of space**  | **Perelman F, W, tilde{V}** |

RF dissipation is the *most intrinsic*: it acts on the geometry itself, controlled by the deepest monotone quantities in the Atlas.

---

## 3. Constraint Surface Geometry

### 3.1 Three Curvature-Defined Regions

**Region A: Low Curvature (Smoothing Dominates)**

|Rm| is small relative to the smoothing capacity. The Lichnerowicz Laplacian dominates the Rm * Rm reaction. The geometry smooths:
- Curvature inhomogeneities decrease.
- The metric approaches a *locally homogeneous* form.
- For negatively curved manifolds: the normalized RF converges to a hyperbolic metric (constant negative sectional curvature).
- For small perturbations of Einstein metrics: the RF converges back to the Einstein metric (linearized stability).

**Constraint surface properties:** Smooth, globally well-posed, convergent. The constraint surface in this region is *closed and completely characterized*. The dynamics are *parabolic smoothing* — identical in character to the FP or PME dynamics, but acting on the metric tensor rather than a scalar field.

**Region B: Intermediate Curvature (Neckpinch Regime)**

|Rm| is commensurate with the smoothing capacity at the characteristic scale. The geometry develops *necks* — long thin regions (topologically S^2 x [0, L]) where the curvature is high but not yet infinite. The neck geometry is close to the *round cylinder* S^2 x R — the canonical singularity model.

**Constraint surface properties:** The canonical neighborhood theorem (E8 from Mode 1) applies: every point with sufficiently high curvature has a neighborhood that is epsilon-close to a standard model (sphere, cylinder, or cap). The constraint surface in this region is *classified*: the geometry is known (it is close to a canonical model) even though the curvature is large.

**Region C: High Curvature (Singularity Regime)**

|Rm| → infinity at one or more points. The curvature reaction overwhelms the smoothing. The geometry approaches a *canonical singularity model*:

- Type I: |Rm| ~ 1/(T* - t). Blowup limit = gradient shrinking soliton (round S^3, round S^2 x R).
- Type II: |Rm|(T* - t) → infinity. Blowup limit = ancient solution (Bryant soliton).

**Constraint surface properties:** The singularity is *fully classified* (for n = 3):
- The blowup limit is identified (shrinking soliton or ancient solution).
- The geometry near the singularity is known (canonical neighborhood).
- The surgery procedure resolves the singularity (cut at the neck, cap with spheres).
- The topological consequence is known (connected-sum decomposition simplifies).

### 3.2 Assembly: A Geometric Constraint Surface

The three regions form a single constraint surface on the *space of Riemannian metrics modulo diffeomorphisms*:

    Region A (low curvature, smoothing) → Region B (intermediate, neckpinch) → Region C (high curvature, singularity)

The flow is *one-directional toward singularity* for manifolds that are not already Einstein: the curvature reaction eventually overwhelms the smoothing at some location, driving the geometry through Region B into Region C. After surgery, the surviving components re-enter Region A (with simplified topology) and the process repeats — until the manifold is either extinct or decomposed into its geometric pieces.

The constraint surface is *not defined on a fixed function space* (like every other PDE) but on the *space of Riemannian metrics on M modulo diffeomorphisms* — the **moduli space of geometries**. The constraint surface's geometry reflects the geometry of this moduli space, which has its own curvature, topology, and structure. The RF dynamics are a flow *on the moduli space*, and the singularities correspond to *boundary points of the moduli space* where the metric degenerates.

### 3.3 Why the Singularity Face Is Classified, Not Open

The RF singularity face is *qualitatively different* from every other singularity face in the Atlas:

| Architecture | Singularity Face          | Classified?    | Resolved?                  |
|-------------|---------------------------|----------------|----------------------------|
| NS (3D)    | Vorticity blowup (open)   | **No**         | **No** (open question)      |
| NLS (foc.) | Amplitude concentration   | Partial (d=2)  | Partial (no post-blowup)   |
| KS          | Mass concentration        | Yes (threshold) | Partial (measure-valued)   |
| HJ/Burgers | Gradient steepening       | Yes             | Yes (entropy/viscosity)    |
| MCF         | Curvature blowup          | Yes (shrinkers) | Yes (surgery/level-set)    |
| **RF**      | **Curvature blowup**      | **Yes (complete for n=3)** | **Yes (Hamilton–Perelman surgery)** |

The RF singularity face is *fully classified AND fully resolved*:
- **Classified:** Every singularity type is identified (Type I → shrinking soliton; Type II → ancient solution). The classification is *complete for n = 3*.
- **Resolved:** The surgery procedure provides a *geometric continuation* past every singularity. The surgery preserves Perelman's monotonicity, controls the geometry, and eventually terminates (finitely many surgeries needed).

The RF singularity face is the *gold standard* for singularity resolution in the Atlas: complete classification + complete resolution. The only comparables are HJ/Burgers (complete for scalar 1D conservation laws) and MCF (complete for convex surfaces, partial for general surfaces).

---

## 4. Anomalies and Open Faces

### 4.1 Sealed Faces

**Shock face: Absent.** RF is parabolic (no first-order transport). No characteristic crossing, no gradient steepening, no discontinuities.

**Dispersive face: Absent.** RF is parabolic (no imaginary time derivative, no odd-order dispersion). No oscillation, no solitons in the NLS/KdV sense, no wave phenomena.

**Nonlocal face: Absent.** RF is *fully local* — the Ricci tensor at x depends on g and its derivatives at x. No Poisson equation, no integral kernel, no nonlocal coupling. RF is local in the strongest sense (unlike NS and KS).

**Chaotic face: Sealed.** Perelman's monotone quantities (F, W, reduced volume) are *monotone* — they increase (or decrease) along the flow without oscillation. The Perelman monotonicity prevents chaotic behavior: the flow cannot revisit previous geometric states (the entropy increases irreversibly). The RF dynamics are *monotone in the Perelman sense*, ruling out limit cycles, strange attractors, and recurrence.

**Entropy face: Sealed.** Perelman's W-entropy increases: dW/dt >= 0. The "geometric entropy" of the metric increases monotonically — no entropy decrease is possible. This seals the entropy face unconditionally.

**Collapse face: Sealed.** Perelman's kappa-noncollapsing theorem prevents the manifold from collapsing (becoming infinitely thin without curvature blowing up). Balls with bounded curvature must have volume bounded below: Vol(B(x, r)) >= kappa r^n when |Rm| <= r^{-2}.

### 4.2 The Singularity Face: Classified and Resolved

The single structural face of the RF constraint surface is the *curvature blowup face*:

    sup_M |Rm(g(t))| → infinity    as t → T*

This face is:
- **Required:** Generic closed 3-manifolds develop singularities under RF. The singularities are *necessary* for the topology-classification program — they reveal the connected-sum structure.
- **Classified:** Every singularity is Type I (shrinking soliton: S^3, S^2 x R) or Type II (ancient solution: Bryant soliton). The classification is complete for n = 3.
- **Resolved:** The Hamilton–Perelman surgery procedure continues the flow past every singularity. The surgery is *controlled* (preserves monotonicity), *finite* (finitely many surgeries), and *topologically meaningful* (each surgery simplifies the manifold).
- **Not anomalous:** The singularity is not a *failure* of the architecture (as NS blowup would be) but its *mechanism for topological classification*. The singularities are the *information-bearing events* that encode the topology of M.

### 4.3 Anomaly Assessment

| Face                    | Status              |
|-------------------------|---------------------|
| Shock                   | Absent (parabolic)  |
| Dispersive              | Absent (no i∂_t)   |
| Nonlocal                | Absent (fully local)|
| Chaotic                 | Sealed (Perelman monotonicity) |
| Entropy                 | Sealed (W increases)|
| Collapse                | Sealed (kappa-noncollapsing) |
| **Curvature blowup**   | **Required, classified, resolved** |

**Anomaly count: zero.** The curvature blowup is a *required structural feature*, not an anomaly. It is the mechanism by which RF achieves its purpose (topological classification). The constraint surface is *closed* in the FS sense: every face is either absent, sealed, or resolved. No unresolved structural questions remain (for n = 3).

The RF constraint surface is *closed with required geometric singularities* — the same structural category as MCF, but at a deeper geometric level (intrinsic metrics vs. extrinsic surfaces) and with a more complete singularity theory (Hamilton–Perelman vs. Huisken–Sinestrari).

---

## 5. Channel Constraints

---

**C1. Metric Field g_{ij}**

    g_{ij}(x, t): positive-definite symmetric 2-tensor on M^n

The state variable. n(n+1)/2 components per point (6 for n = 3). Encodes all geometric information.

*Scope: All RF.*

---

**C2. Curvature Tensor Hierarchy**

    Rm_{ijkl}, Ric_{ij} = g^{kl} Rm_{kilj}, R = g^{ij} Ric_{ij}

The curvature is determined by g and its first and second derivatives. The Ricci tensor drives the evolution.

*Scope: All RF.*

---

**C3. Curvature Smoothing Channel**

    Delta_L g: Lichnerowicz Laplacian, second-order parabolic smoothing of the metric

The primary regularizing mechanism. Rate ~ k^2. Provides short-time existence and instantaneous regularization.

*Scope: All RF.*

---

**C4. Curvature Reaction Channel**

    Rm * Rm: quadratic curvature interaction

The nonlinear mechanism. Can improve pinching (stabilize) or amplify concentration (destabilize).

*Scope: All RF.*

---

**C5. Diffeomorphism Gauge (DeTurck)**

    partial_t g = -2 Ric + L_X g    (DeTurck-modified, strictly parabolic)

The gauge-fixing term that converts the weakly parabolic RF into a strictly parabolic system. Geometric content unchanged.

*Scope: All RF (for existence/uniqueness proofs).*

---

**C6. Perelman F Monotonicity**

    dF/dt = 2 integral |Ric + Hess(f)|^2 e^{-f} dmu >= 0

Identifies gradient steady solitons as critical points. Gradient-flow structure.

*Scope: All RF.*

---

**C7. Perelman W Monotonicity**

    dW/dt >= 0

The deepest monotone quantity. Controls singularity structure. Identifies gradient shrinking solitons as blowup limits.

*Scope: All RF.*

---

**C8. Reduced Volume Monotonicity**

    tilde{V}(tau) non-increasing in tau

Spacetime-localized control. Prevents collapsing at all scales.

*Scope: All RF.*

---

**C9. kappa-Noncollapsing**

    |Rm| <= r^{-2} on B(x,r)    =>    Vol(B(x,r)) >= kappa r^n

Volume lower bound from curvature bound. The structural foundation of singularity classification.

*Scope: All RF.*

---

**C10. Canonical Neighborhoods (n = 3)**

    |Rm(x,t)| >= r_0^{-2}    =>    neighborhood of (x,t) is epsilon-close to standard model (S^3, S^2 x R, cap)

Complete geometric description of high-curvature regions. The structural basis of surgery.

*Scope: n = 3, sufficiently high curvature.*

---

**C11. Canonical Singularity Models**

    Type I blowup limit: gradient shrinking Ricci soliton (S^3, S^2 x R, or quotient)
    Type II blowup limit: ancient solution (Bryant soliton, etc.)

Complete classification of singularity types for n = 3.

*Scope: At singularity.*

---

**C12. Surgery (Topological Continuation)**

    At singularity: cut at neck → cap with spheres → restart RF
    Finitely many surgeries → manifold decomposes into geometric pieces

The Hamilton–Perelman surgery program. Controlled, finite, topology-classifying.

*Scope: Post-singularity (n = 3).*

---

### Channel Constraint Summary

| Label | Constraint                        | Type              | Scope            |
|-------|-----------------------------------|-------------------|------------------|
| C1    | Metric field g_{ij}               | State variable    | All RF           |
| C2    | Curvature hierarchy               | Geometric         | All RF           |
| C3    | Curvature smoothing               | Stabilizing       | All RF           |
| C4    | Curvature reaction                | Dual (stab/destab)| All RF           |
| C5    | DeTurck gauge                     | Gauge-fixing      | All RF           |
| C6    | Perelman F monotonicity           | Monotone          | All RF           |
| C7    | Perelman W monotonicity           | Monotone          | All RF           |
| C8    | Reduced volume monotonicity       | Monotone          | All RF           |
| C9    | kappa-noncollapsing               | Volume bound      | All RF           |
| C10   | Canonical neighborhoods           | Classification    | n=3, high curv.  |
| C11   | Canonical singularity models      | Blowup limits     | At singularity   |
| C12   | Surgery                           | Continuation      | Post-singularity |

**All twelve constraints hold for n = 3** within their specified scope. The constraints C10–C12 are specific to n = 3 (the dimension relevant for the Poincare and geometrization conjectures). For general n, the theory is less complete (canonical neighborhoods and singularity classification are not fully established for n >= 4).

---

## 6. Comparison with FP, PME, HJ, Burgers, NLS, KdV, NS, MCF, AC/CH, TFE, RD, KS, and ED

### 6.1 Constraint Surface Classification Across the Atlas

| Architecture | Surface Type                | Singularity Face           | Resolution            |
|-------------|-------------------------------|----------------------------|-----------------------|
| FP/PME/AC/CH/TFE | Contracting (Lyapunov)  | None                       | N/A                   |
| KdV         | Integrable (IST)              | None                       | N/A                   |
| NLS (def.)  | Isoenergetic (Hamiltonian)    | None                       | N/A                   |
| HJ/Burgers  | Entropy-resolved              | Shock/kink (classified, resolved) | Entropy/viscosity |
| MCF         | Area-decreasing (geometric)   | Curvature blowup (classified, resolved) | Surgery/level-set |
| NLS (foc.)  | Isoenergetic (focusing)       | Amplitude (partial)        | Partial               |
| KS          | Mass-stratified (nonlocal)    | Mass concentration (characterized) | Measure-valued   |
| NS (3D)    | Open (unresolved)             | Open (vorticity?)          | Open                  |
| RD          | Constitutive                  | Constitutive               | Constitutive          |
| **RF**      | **Geometric (intrinsic)**    | **Curvature blowup (fully classified + resolved)** | **Hamilton–Perelman surgery** |

### 6.2 The Geometric Hierarchy at Mode 3

| Level                  | Architecture | Constraint Surface              | Singularity Resolution    |
|------------------------|-------------|----------------------------------|---------------------------|
| Scalar field           | FP/PME/AC/CH/TFE/HJ/Burgers/NLS/KdV/KS | Function-space surface | Entropy/viscosity/none |
| Vector field           | NS          | Function-space (vector)          | Open                      |
| Extrinsic geometry     | MCF         | Shape-space surface              | Surgery/level-set         |
| **Intrinsic geometry** | **RF**      | **Moduli space of metrics**      | **Hamilton–Perelman surgery** |

RF operates on the *deepest constraint surface* in the Atlas: the moduli space of Riemannian metrics (metrics modulo diffeomorphisms). This is an infinite-dimensional space with its own geometric structure — curvature, geodesics, and topology — that is qualitatively richer than any function space or shape space.

### 6.3 RF and ED: Geometric Classification

The RF and ED constraint surfaces share the *deepest structural parallel* in the Atlas: both are *classificatory*:

| Feature                    | ED                           | RF                            |
|----------------------------|------------------------------|-------------------------------|
| Objects                    | Integers                     | Closed 3-manifolds            |
| Constraint surface         | Skyline (prime structure)    | Moduli space (metric structure)|
| Classification theorem     | FTA                          | Geometrization theorem         |
| Irreducible components     | Primes                       | Geometric pieces              |
| Classification method      | Factorization                | Ricci Flow + surgery           |
| Completeness               | Complete (every integer)     | Complete (every 3-manifold)    |

Both architectures use their constraint surfaces as *classification tools*: the ED skyline classifies integers through their multiplicative structure; the RF moduli space classifies 3-manifolds through their geometric structure. The structural parallel is *exact*: both are complete, unique decomposition theorems for their respective object classes.

### 6.4 Summary

| Feature                    | RF               | MCF      | FP/PME   | NS       | NLS/KdV  | KS       | HJ/Burg. |
|----------------------------|------------------|----------|----------|----------|----------|----------|----------|
| Constraint surface type    | **Moduli space** | Shape space | Function sp. | Function sp. | Function sp. | Nonlocal func. sp. | Function sp. |
| Smoothing channel          | **Curvature**    | Curvature| Scalar   | Viscous  | Dispersive| Diffusive| None     |
| Reaction channel           | **Rm * Rm**      | N/A      | Various  | Advective| Nonlinear| Aggregative| Transport |
| Gauge channel              | **Diffeomorphism**| None    | None     | Pressure | Phase    | None     | None      |
| Singularity face           | **Classified+resolved** | Classified+resolved | None | Open | Partial | Characterized | Classified+resolved |
| Monotone tools             | **Perelman (3)** | Huisken (1)| Lyapunov| Energy   | Conserved| Free energy| Entropy  |
| Topological consequence    | **Geometrization**| Genus red.| None   | None     | None     | None     | None      |
| Locality                   | **Fully local**  | Local    | Local    | Nonlocal | Local    | Nonlocal | Local     |
| Parameters                 | **0**            | 0        | 1-2      | 2        | 0-1      | 0-1      | 0         |

RF is the *unique intrinsic-geometric, moduli-space, curvature-smoothing, diffeomorphism-gauge, fully-classified-singularity, Perelman-monotone, topology-classifying, fully-local, parameter-free* architecture in the Atlas. Its constraint surface is the *deepest and most completely characterized* of any PDE ever evaluated.

---

*End of Mode 3: Channels → Constraint Surface. The AD Criteria and Verdict will follow in the final file.*
