# AD Evaluation: Ricci Flow — Mode 2: PDE → Extremal Dynamics

Allen Proxmire

April 2026

---

## Overview

Mode 2 moves from the static envelope to the dynamics. The RF dynamical landscape is the *most geometrically rich* of any PDE in the Atlas: the flow smooths curvature, concentrates curvature, forms singularities, changes topology, and ultimately classifies the geometry of the manifold — all through a single equation acting on the metric tensor. The dynamics are *self-referential* in the deepest sense: the metric g determines the curvature Ric(g), the curvature drives the evolution of g, and the evolution changes the curvature — a closed feedback loop between the geometry and its evolution.

The RF dynamics are *qualitatively unprecedented*: no other architecture evolves the *domain itself* (the metric that defines what "space" means). Every other architecture evolves a quantity *on* a fixed space; RF evolves the *structure of space*. The consequences — curvature smoothing, neckpinch formation, surgery, and topological classification — have no analogues in any field-based PDE.

Throughout:

    partial_t g_{ij} = -2 Ric_{ij}(g)

on a smooth closed Riemannian manifold (M^n, g(t)), primarily n = 3.

---

## 1. Fundamental Time and Length Scales

### 1.1 Three Fundamental Scales

**Parabolic time scale:** The time for the parabolic smoothing to act at spatial scale L:

    t_par ~ L^2

Standard second-order parabolic scaling, identical to the heat equation, FP, PME, and MCF. The Lichnerowicz Laplacian damps metric perturbations at rate k^2 in Fourier-like decomposition.

**Curvature scale:** The intrinsic geometric scale set by the curvature:

    L_curv ~ 1 / sqrt(|Rm|)

At a point where |Rm| = K, the geometry is "curved at scale" L_curv = 1/sqrt(K). This is the *intrinsic* length scale — not imposed by a parameter (like epsilon in AC/CH or D in FP) but *determined by the geometry itself*. As curvature concentrates (K → infinity), the curvature scale shrinks to zero (L_curv → 0).

**Singularity time scale:** The time for curvature concentration to produce a singularity:

    t_sing ~ 1 / max|Rm|

If the maximum curvature is K, the curvature can potentially blow up in time O(1/K) (from the reaction term 2|Ric|^2 in the scalar curvature evolution, which grows as K^2 and reaches infinity in time ~1/K).

### 1.2 The Curvature–Parabolic Ratio

    rho = t_par / t_sing = L^2 * max|Rm|

measures which mechanism dominates at scale L:

**rho << 1 (parabolic-dominated, smoothing regime):**

The parabolic smoothing acts faster than the curvature can concentrate. The metric smooths: curvature inhomogeneities are reduced, the geometry becomes more uniform. This is the *regularization regime* — the RF acting like a geometric heat equation, diffusing curvature from high to low.

**rho ~ 1 (balanced, neckpinch regime):**

The parabolic smoothing and curvature concentration are commensurate. The geometry develops a *neck* — a long thin region (approximately S^2 x R) where the curvature is high but the smoothing cannot prevent further concentration. This is the regime where singularities form: the neck pinches to zero radius in finite time.

**rho >> 1 (curvature-dominated, singularity regime):**

The curvature concentration overwhelms the parabolic smoothing. The curvature blows up: |Rm| → infinity at one or more points. The geometry approaches a *canonical singularity model* (gradient shrinking soliton). This is the *blowup regime* — the RF's structural endpoint.

### 1.3 Geometric Scales: Unique in the Atlas

The RF scales are *geometric* — determined by the *curvature of the evolving metric*, not by constitutive parameters or external conditions:

| Architecture | Characteristic Scale              | Set By                     |
|-------------|-----------------------------------|----------------------------|
| FP          | L_diff = sqrt(D t)                | Diffusion coefficient D    |
| PME         | L_diff = sqrt(u^{m-1} t)          | Density u + exponent m     |
| AC/CH       | epsilon (interface width)          | Interfacial parameter      |
| NLS         | L_disp = sqrt(t)                   | Dispersion coefficient     |
| HJ/Burgers  | L_shock = 1/max|nabla u_0|        | Initial gradient           |
| MCF         | L_curv = 1/sqrt(|H|)              | Mean curvature             |
| **RF**      | **L_curv = 1/sqrt(|Rm|)**         | **Riemann curvature**      |

The RF and MCF both have *intrinsic curvature scales* — but at different structural levels. MCF's scale is set by the *extrinsic* mean curvature (how the surface curves in ambient space); RF's scale is set by the *intrinsic* Riemann curvature (how space itself curves). RF's scale is the most fundamental — it measures the curvature of the *metric structure of space*.

---

## 2. Extremal Behaviors

### E1. Curvature Smoothing (Parabolic Regularization)

For short times and in low-curvature regions, Ricci Flow acts like a *geometric heat equation*:

- Curvature inhomogeneities are smoothed (high-curvature bumps flatten, low-curvature valleys fill).
- The metric becomes *more uniform* (curvature ratios improve — Hamilton's pinching estimates).
- Higher derivatives of curvature are controlled by the curvature itself (Shi estimates: |nabla^k Rm| <= C |Rm| / t^{k/2}).
- The metric becomes C^{infinity} instantaneously (for t > 0, the metric is smooth regardless of initial regularity, as long as the curvature stays bounded).

The smoothing is the *stabilizing mechanism* of RF — the geometric analogue of diffusive smoothing in FP/PME and of curvature smoothing in MCF.

### E2. Curvature Concentration (Formation of High-Curvature Regions)

The curvature evolution equation for the full Riemann tensor has the schematic form:

    partial_t Rm = Delta Rm + Rm * Rm

The quadratic reaction term Rm * Rm can *amplify* curvature: regions of high curvature generate even higher curvature through the nonlinear interaction. The concentration is:

- *Self-reinforcing:* High curvature → larger Rm * Rm → faster curvature growth → even higher curvature.
- *Scale-dependent:* The concentration is strongest where the curvature is already large (small L_curv).
- *Geometry-dependent:* The specific form of Rm * Rm depends on the algebraic type of the curvature (positive, negative, mixed). Positive curvature concentrates *faster* than negative curvature spreads.

The curvature concentration is the *destabilizing mechanism* of RF — the geometric analogue of the advective steepening in Burgers/HJ and the nonlocal aggregation in KS.

### E3. Finite-Time Singularity Formation

For closed 3-manifolds with positive Ricci curvature (Hamilton, 1982):

    sup_M |Rm(g(t))| → infinity    as t → T* < infinity

The curvature blows up in finite time. For general closed 3-manifolds (not necessarily positively curved), singularities also form — generically through neckpinches.

The singularity time T* satisfies:

    T* <= C / max_{t=0} |Rm|    (upper bound from the ODE comparison dK/dt ~ K^2)
    T* >= c / max_{t=0} |Rm|    (lower bound from the parabolic smoothing)

The singularity time is *determined by the initial curvature* — in the same way that the Burgers shock time T* = -1/min(v_0') is determined by the initial velocity gradient.

### E4. Canonical Singularity Models (Gradient Shrinking Solitons)

Near a Type I singularity, the rescaled geometry converges to a *gradient shrinking Ricci soliton*:

    Ric + Hess(f) = (1/(2 tau)) g    (soliton equation, tau = T* - t)

The canonical models for n = 3:

- **Round sphere S^3:** The *extinction model*. A manifold with positive Ricci curvature shrinks to a round point. The rescaled geometry approaches S^3 as t → T*. Hamilton (1982): 3-manifolds with Ric > 0 converge to round S^3.

- **Round cylinder S^2 x R:** The *neckpinch model*. A thin neck on the manifold pinches to zero radius. The rescaled geometry near the neck approaches S^2 x R. The generic singularity model for 3-manifolds.

- **Bryant soliton:** A rotationally symmetric *steady soliton* on R^3 with positive curvature. The model for Type II singularities (faster-than-self-similar blowup).

### E5. Neckpinch Formation (Type I Singularity)

The generic singularity for 3-dimensional RF is the *neckpinch*:

1. A thin neck (topologically S^2 x [0, L]) develops on the manifold.
2. The neck radius R(t) shrinks: R(t) ~ sqrt(2(T* - t)).
3. The geometry near the neck approaches the round cylinder S^2 x R.
4. At T*: the neck radius reaches zero — the manifold pinches.
5. The topology changes: one connected component splits into two (or a handle is removed).

The neckpinch is the RF analogue of:
- MCF's neckpinch (a dumbbell-shaped surface pinching at the neck).
- KS's mass concentration (density concentrating at a point).
- Burgers' shock formation (velocity gradient steepening to a discontinuity).

But the RF neckpinch is *geometrically richer*: it changes the *topology of space* (not just the shape of a surface or the profile of a density).

### E6. Degenerate Singularities (Type II)

Type II singularities have |Rm|(T* - t) → infinity — the curvature grows *faster* than the self-similar rate. The rescaled geometry converges to an *ancient solution* (defined for all t in (-infinity, T*)):

- **Bryant soliton:** A steady gradient soliton with cigar-like geometry (one end rounds off, the other extends to infinity). The simplest Type II model.
- **Other ancient solutions:** More exotic ancient solutions exist but are less well-characterized.

Type II singularities are *rarer* than Type I (generic singularities are Type I), but they can occur for special initial data. Their blowup rates are *faster* than the self-similar rate — making them analytically more challenging.

### E7. Topology Change via Surgery

At each singularity, the Hamilton–Perelman surgery procedure:

1. **Detects** the high-curvature region (using the canonical neighborhood theorem — the geometry near the singularity is epsilon-close to a standard model).
2. **Cuts** the manifold at the neck (removing the thin cylindrical region).
3. **Caps** the cut ends with standard spherical caps (round 3-balls).
4. **Restarts** the flow on the (topologically modified) manifold.

Each surgery:
- Removes a handle (reduces genus) or separates a connected component.
- Reduces the topological complexity of M.
- Preserves the Perelman monotonicity (W-entropy, reduced volume, noncollapsing).
- Is *controlled*: the surgery parameters can be chosen so that the geometric estimates survive the surgery.

After *finitely many* surgeries, the manifold either:
- Becomes *extinct* (all components shrink to round points — happens for manifolds that are connected sums of S^3 and S^2 x S^1).
- Reaches a *thick-thin decomposition* (the thick parts carry hyperbolic geometry; the thin parts are graph manifolds).

The surgery program is the *most sophisticated singularity-resolution mechanism* in the Atlas — far more complex than HJ/Burgers entropy solutions, MCF level-set/surgery, or KS measure-valued continuation.

### E8. Long-Time Convergence

For RF solutions that survive past all singularities (possibly after surgery):

**Normalized RF on 3-manifolds:**

- **Positive curvature → round sphere:** Hamilton (1982). The metric converges to a round S^3 metric. Exponential convergence.
- **Negative curvature → hyperbolic metric:** Thurston's hyperbolization. The normalized RF converges to the unique hyperbolic metric on the manifold. Exponential convergence in the negatively curved components.
- **Mixed curvature → geometric decomposition:** The thick parts converge to their canonical geometric forms; the thin parts collapse onto lower-dimensional structures.

**General convergence:**

- The long-time limit of RF (or normalized RF) on a closed 3-manifold is one of Thurston's *eight model geometries*: S^3, R^3, H^3, S^2 x R, H^2 x R, Nil, Sol, SL(2,R). The RF drives the metric toward the *canonical geometric structure* — the unique optimal geometry for the given topology.

The long-time convergence is the RF analogue of:
- FP's convergence to Gibbs–Boltzmann (the unique equilibrium for the given potential).
- PME's convergence to Barenblatt (the unique self-similar profile for the given mass).
- AC's convergence to ±1 (the unique equilibrium phases).
- KdV's soliton resolution (the unique decomposition into canonical components).

But the RF convergence is *geometrically deeper*: it converges to a *canonical geometry for the given topology* — a result about the *structure of space itself*.

---

## 3. Universal Inequalities

---

**U1. Scalar Curvature Evolution**

    partial_t R = Delta R + 2|Ric|^2

The scalar curvature satisfies a reaction-diffusion equation. The reaction term 2|Ric|^2 >= (2/n)R^2 is non-negative → by the maximum principle:

    R_min(t) >= -n/(2(t + C))    (R_min increases toward 0)

For initially positive R: R remains positive for all time.

---

**U2. Maximum Principle for Scalar Curvature**

    R(x, t) >= R_min(0)    when R(0) >= 0

Positive scalar curvature is *preserved* by Ricci Flow. More generally, R_min is non-decreasing, providing a universal lower bound on the scalar curvature.

---

**U3. Shi Estimates**

If |Rm| <= K on M x [0, alpha/K] (alpha sufficiently small), then:

    |nabla^m Rm| <= C(n, m, alpha) K^{1 + m/2} / t^{m/2}    on M x (0, alpha/K]

Derivative bounds from curvature bounds. The *regularity mechanism*: curvature control → full derivative control → smoothness. The Shi estimates are the RF analogue of the parabolic smoothing estimates for the heat equation.

---

**U4. Perelman's F-Functional Monotonicity**

    dF/dt = 2 integral_M |Ric + Hess(f)|^2 e^{-f} dmu >= 0

F increases. Equality iff Ric + Hess(f) = 0 (gradient steady soliton).

---

**U5. Perelman's W-Entropy Monotonicity**

    dW/dt >= 0    (W increases forward in time)

Equality iff (M, g, f, tau) is a gradient shrinking soliton. The W-entropy:
- Controls the geometry near singularities.
- Provides noncollapsing estimates (U7).
- Classifies blowup limits.

---

**U6. Reduced Volume Monotonicity**

    tilde{V}(tau) is non-increasing in tau (non-decreasing forward in time)

The reduced volume is a *spacetime-localized* monotone quantity (defined using the L-functional and reduced distance). It provides:
- Noncollapsing without the need for a comparison function f.
- Control of the geometry at scales comparable to sqrt(tau).
- Classification of singularity types through the asymptotic value of tilde{V}.

---

**U7. kappa-Noncollapsing Theorem**

If |Rm| <= r^{-2} on B(x, r) at time t, then:

    Vol(B(x, r)) >= kappa r^n

for a universal kappa > 0 (depending on the initial data and the time). Balls with bounded curvature have *volume bounded below*. The manifold cannot collapse — it cannot become infinitely thin while maintaining bounded curvature.

The noncollapsing theorem is the *structural foundation* of the singularity classification: it ensures that blowup limits are noncollapsed, hence classifiable as gradient solitons.

---

**U8. Canonical Neighborhood Theorem (n = 3)**

For every epsilon > 0, there exists r_0 > 0 such that if |Rm(x, t)| >= r_0^{-2}, then the point (x, t) has a neighborhood that is epsilon-close (in the C^{[1/epsilon]} topology) to one of:
- A shrinking round sphere S^3 (extinction cap).
- A shrinking round cylinder S^2 x R (neck).
- A cap (standard cap attached to a half-cylinder).

The canonical neighborhood theorem says: *near any point of sufficiently high curvature, the geometry is standard*. This is the structural basis of surgery — the surgeon knows exactly what the geometry looks like near the singularity and can cut and cap with precision.

---

**U9. Blowup Criteria**

    sup_M |Rm(g(t))| < infinity for all t in [0, T)    iff    g(t) is smooth on [0, T]

The solution extends past time T iff the curvature remains bounded up to T. Curvature blowup is the *only* mechanism for singularity — there are no other obstructions to smooth continuation. This is the RF analogue of the BKM criterion for NS and the curvature criterion for MCF. Unlike NS (where the criterion is *open*), the RF criterion is *resolved*: we know that curvature does blow up for generic 3-manifolds.

---

**U10. Classification of Singularity Types**

**Type I:** |Rm| <= C/(T* - t). Self-similar blowup rate. The blowup limit is a *gradient shrinking soliton*. For n = 3: round S^3 or round S^2 x R (or quotients).

**Type II:** |Rm|(T* - t) → infinity. Faster-than-self-similar. The blowup limit is an *ancient solution*. For n = 3: the Bryant soliton or more exotic ancient solutions.

**Type III:** Immortal solutions (t → infinity). Curvature decays as |Rm| ~ 1/t. The blowup limit (after rescaling) is an *expanding soliton*.

The classification is *complete for n = 3*: Perelman's noncollapsing + canonical neighborhoods + surgery provide the full classification of all singularity types and their resolutions.

---

### Universal Inequality Summary

| Label | Inequality                        | Type            | Status        | Role                           |
|-------|-----------------------------------|-----------------|---------------|--------------------------------|
| U1    | Scalar curvature evolution        | Exact identity  | Unconditional | Primary curvature evolution    |
| U2    | Maximum principle for R           | Lower bound     | Unconditional | Curvature positivity           |
| U3    | Shi estimates                     | Derivative bounds| Conditional*  | Regularity mechanism           |
| U4    | Perelman F monotonicity           | Monotone        | Unconditional | Gradient-flow structure        |
| U5    | Perelman W monotonicity           | Monotone        | Unconditional | Deepest structural tool        |
| U6    | Reduced volume monotonicity       | Monotone        | Unconditional | Spacetime control              |
| U7    | Noncollapsing                     | Volume bound    | Unconditional | Prevents collapsing            |
| U8    | Canonical neighborhoods           | Classification  | n = 3, high K | Singularity geometry           |
| U9    | Blowup criteria                   | Iff condition   | Unconditional | Smooth iff bounded curvature   |
| U10   | Singularity classification        | Type I/II/III   | n = 3         | Complete for 3-manifolds       |

*Conditional on curvature bound; unconditional statement: if curvature bounded, then all derivatives bounded.

---

## 4. Attractors and Long-Time Behavior

### 4.1 Three Long-Time Regimes

**Regime A: Positive Curvature → Extinction (Round Sphere)**

For closed 3-manifolds with positive Ricci curvature (Hamilton 1982):

    g(t) / (T* - t) → g_{S^3}    (round sphere metric)

The manifold shrinks to a round point in finite time. The rescaled metric converges to the round S^3 — the *extinction attractor*. This is the RF analogue of MCF's convex-surface extinction (Huisken 1984).

**Regime B: Negative Curvature → Hyperbolic Metric**

For closed 3-manifolds admitting a hyperbolic structure (normalized RF):

    g(t) → g_{hyp}    (hyperbolic metric of constant sectional curvature -1)

The normalized RF converges to the unique hyperbolic metric — the *hyperbolic attractor*. The convergence is exponential (spectral gap of the linearized operator on the space of metrics). This is the RF analogue of FP's convergence to Gibbs–Boltzmann.

**Regime C: Mixed Curvature → Geometric Decomposition + Surgery**

For general closed 3-manifolds (neither positively nor negatively curved):

1. The RF develops singularities (neckpinches) in finite time.
2. Surgery separates the manifold into pieces.
3. Some pieces become extinct (positive-curvature components → round points).
4. Surviving pieces undergo further flow and possible further surgery.
5. After finitely many surgeries, the remaining pieces converge to their canonical geometries.

The ultimate long-time behavior is the *geometric decomposition* — the manifold decomposes into pieces, each carrying one of Thurston's eight model geometries.

### 4.2 RF Attractors Are Geometric Structures

The RF "attractors" are not functions, not profiles, not measures — they are *Riemannian metrics* (equivalence classes of metrics modulo diffeomorphisms):

| Architecture | Attractor Type                    | What It Is                    |
|-------------|-----------------------------------|-------------------------------|
| FP          | Gibbs–Boltzmann rho_eq           | A probability density          |
| PME         | Barenblatt profile               | A density profile              |
| KdV         | N solitons + radiation           | A wave decomposition           |
| NLS         | Solitons / free flow             | A complex wave                 |
| HJ/Burgers  | Paraboloid / N-wave             | A potential / velocity profile |
| MCF         | Round sphere (extinction)        | A geometric shape              |
| **RF**      | **Einstein metrics / geometric pieces** | **A Riemannian geometry** |

The RF attractor is the *most structurally complex*: it is a *geometry* — an equivalence class of metrics that defines the curvature, topology, and global structure of the manifold. The attractor is not a function on a fixed domain but the *domain itself in its canonical form*.

### 4.3 The Geometrization Program as "Attractor Theory"

The Hamilton–Perelman program can be interpreted as *the attractor theory of Ricci Flow*:

1. **Start:** An arbitrary Riemannian 3-manifold (M, g_0).
2. **Flow:** RF evolves g_0 toward lower curvature.
3. **Singularities:** Curvature concentrations reveal the topological structure.
4. **Surgery:** Singularities are resolved, simplifying the topology.
5. **Long-time:** The surviving pieces converge to their canonical geometries.
6. **Attractor:** The decomposition of M into geometric pieces (Thurston decomposition).

The *attractor is the topology of M expressed as geometry*. The RF does not merely converge to an equilibrium — it *computes the topological classification of the manifold* by driving the geometry toward its canonical form. This is the *deepest attractor theory* in the Atlas: the attractor is not a function or a shape but a *topological classification*.

### 4.4 Comparison of Attractor Structures

| Architecture | Attractor                      | Structural Depth    | Classification?      |
|-------------|--------------------------------|---------------------|-----------------------|
| **RF**      | **Geometric pieces (Thurston)** | **Deepest (topology)**| **Yes (geometrization)** |
| KdV         | Solitons + radiation (IST)    | Deep (scattering)    | Yes (IST)             |
| MCF         | Round sphere / shrinkers      | Geometric (extrinsic)| Partial (shrinkers)   |
| FP          | Gibbs–Boltzmann               | Analytical           | Yes (spectral)        |
| PME         | Barenblatt                    | Self-similar          | Yes (explicit)        |
| NLS (def.)  | Free Schrödinger group        | Dispersive            | Yes (scattering)      |
| KS          | Steady state / delta          | Analytical            | Yes (mass threshold)  |
| NS (2D)    | Compact attractor              | Unknown              | No                    |

---

## 5. Comparison with FP, PME, HJ, Burgers, NLS, KdV, NS, MCF, AC/CH, TFE, RD, KS, and ED

### 5.1 RF as the Geometric Parabolic Pole

The Atlas's *parabolic hierarchy*:

    FP (linear scalar) → PME (nonlinear scalar) → AC/CH (scalar + reaction) → TFE (4th-order scalar)
                                                                                    ↓
    NS (vector + pressure) ← — — — — — — — — — — — — — — — — — — — — MCF (extrinsic geometry)
                                                                                    ↓
                                                                              **RF (intrinsic geometry)**

RF is the *apex of the parabolic hierarchy*: it applies parabolic smoothing to the *most fundamental geometric object* (the metric tensor) and produces the *most profound results* (topological classification).

### 5.2 RF vs. MCF: Intrinsic vs. Extrinsic Geometry

| Feature                    | Ricci Flow                    | MCF                          |
|----------------------------|-------------------------------|------------------------------|
| State variable             | Intrinsic metric g_{ij}       | Extrinsic embedding F        |
| Curvature                  | Ricci (intrinsic)             | Mean (extrinsic)             |
| Ambient space              | None needed                   | Required (R^{d+1})          |
| Smoothing                  | Curvature → uniform           | Surface → sphere             |
| Singularity                | Curvature blowup (neck, extinction) | Curvature blowup (neck, extinction) |
| Surgery                    | Hamilton–Perelman (cuts + caps)| Huisken–Sinestrari           |
| Topological result         | **Geometrization**           | Genus reduction              |
| Soliton models             | Round S^n, S^{n-1} x R, Bryant | Round S^d, S^k x R^{d-k}, Angenent |
| Monotone quantity           | Perelman W + reduced vol      | Huisken's Theta              |
| Millennium Problem          | **Solved (Poincare)**        | No                           |

RF and MCF are *structural siblings* — both curvature-driven geometric flows with singularities, surgery, and soliton models. But RF operates at a *deeper level* (intrinsic geometry of space vs. extrinsic shape of surfaces) and produces *deeper results* (topological classification vs. genus reduction).

### 5.3 RF vs. NS: Two Complex Parabolic Architectures

| Feature                    | Ricci Flow                    | Navier–Stokes                |
|----------------------------|-------------------------------|------------------------------|
| State complexity           | g_{ij} (6 comp. for n=3)    | u_i (3 comp.)                |
| Nonlinearity               | Quasilinear (Ric(g))        | Quadratic (u . nabla u)     |
| Nonlocal channel           | **None** (fully local)       | Pressure (Poisson)           |
| Gauge freedom              | Diffeomorphisms (DeTurck)    | Pressure gauge                |
| Singularity                | **Certain (3D, classified)** | **Open (3D, unresolved)**    |
| Surgery                    | Hamilton–Perelman              | None                          |
| Monotone quantities        | Perelman F, W, tilde{V}     | Energy inequality (weak)      |
| Topological consequence    | **Geometrization**           | None                          |
| Millennium Problem          | **Solved**                   | **Open**                      |

The contrast is stark: RF and NS are both quasilinear parabolic PDEs with gauge freedom and potential singularities in 3D. But RF has a *complete singularity theory* (Perelman), while NS does not. The structural tool that makes RF tractable — Perelman's monotonicity — has *no NS analogue*. The RF evaluation demonstrates that *3D nonlinear parabolic PDE singularities can be completely resolved* — the failure to resolve NS singularities is not a limitation of PDE theory in general but a specific structural gap in the NS architecture (the nonlocal pressure + incompressibility + vector character prevent the Perelman-type tools from applying).

### 5.4 RF and ED: The Two Classificatory Architectures (Deepest Level)

The RF–ED parallel reaches its *deepest form* at the attractor level:

| Feature                    | ED                            | RF                            |
|----------------------------|-------------------------------|-------------------------------|
| Objects classified         | Integers                      | Closed 3-manifolds            |
| Classification theorem     | Fundamental theorem of arithmetic | Geometrization theorem    |
| Irreducible components     | Primes                        | Geometric pieces (Thurston)   |
| Decomposition              | n = p_1^{a_1} ... p_k^{a_k} | M = M_1 # ... # M_k (connected sum) + geometric pieces |
| Uniqueness                 | Unique factorization          | Unique geometric decomposition |
| Method                     | Sieve / factorization         | Ricci Flow + surgery           |
| Parameters per component   | 1 (the prime p)               | 1 (the geometry type: S^3, H^3, etc.) |

Both architectures *classify their objects into irreducible components*. The FTA classifies integers; the geometrization theorem classifies 3-manifolds. Both classifications are *unique* (every object has exactly one decomposition) and *complete* (every object is classified). The RF is the *geometric-topological analogue of the fundamental theorem of arithmetic*.

### 5.5 Summary Table

| Feature                    | RF               | MCF      | FP/PME   | NS       | NLS/KdV  | KS       | HJ/Burg. |
|----------------------------|------------------|----------|----------|----------|----------|----------|----------|
| State variable             | **Metric g_{ij}**| Surface  | Scalar   | Vector   | Scalar/complex | Scalar | Scalar  |
| Curvature type             | **Intrinsic**    | Extrinsic| N/A      | N/A      | N/A      | N/A      | N/A      |
| Smoothing                  | Curvature diff.  | Curvature| Scalar diff.| Viscous| Dispersive| Diffusive| None   |
| Singularity                | **Classified**   | Classified| None    | Open(3D) | NLS: foc.| Mass conc.| Shocks  |
| Surgery                    | **Hamilton–Perelman** | H–S | N/A     | None     | None     | Measure  | None     |
| Topological result         | **Geometrization**| Genus red.| None   | None     | None     | None     | None     |
| Monotone quantity          | **Perelman W**   | Huisken Theta| Entropy| Energy   | Conserved| Free energy| Hopf–Lax|
| Millennium Problem         | **Solved**       | No       | No       | Open     | No       | No       | No       |
| Nonlocal channel           | **None**         | None     | None     | Yes (P)  | None     | Yes (2)  | None     |
| Parameters                 | **0**            | 0        | 1-2      | 2        | 0-1      | 0-1      | 0        |

RF is the *unique intrinsic-geometric, metric-tensor-valued, curvature-driven, diffeomorphism-invariant, surgery-requiring, topology-classifying, Millennium-Problem-solving, fully-local, parameter-free* architecture in the Atlas. It occupies the *deepest structural position* of any PDE ever evaluated.

---

*End of Mode 2: PDE → Extremal Dynamics. Mode 3 (Channels → Constraint Surface) will follow in a subsequent file.*
