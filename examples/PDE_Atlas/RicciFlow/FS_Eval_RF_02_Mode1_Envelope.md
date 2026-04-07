# AD Evaluation: Ricci Flow — Mode 1: Axiom → Envelope

Allen Proxmire

April 2026

---

## Overview

Mode 1 traces the path from the Ricci Flow axioms (RF-1 through RF-10) to the architectural envelope. The RF envelope is the *most structurally profound* of any PDE in the PDE Atlas: it is the first envelope whose state variable is a *Riemannian metric*, whose singularities are *curvature concentrations that change topology*, and whose closure relies on *Perelman's monotonicity formulas* — the deepest structural tools ever developed for a nonlinear PDE.

The RF envelope introduces a structural principle that has no precedent in the Atlas: **geometric surgery as architectural continuation**. Where HJ/Burgers continue past shocks via entropy solutions, MCF continues past curvature blowup via level-set solutions, and KS continues past mass concentration via measure-valued solutions, Ricci Flow continues past curvature blowup via *surgery* — a procedure that cuts the manifold at the singularity, caps the cut ends with standard spherical caps, and restarts the flow. The surgery is not a weak-solution formulation but a *geometric construction* that modifies the topology of the manifold at each singularity.

Throughout:

    partial_t g_{ij} = -2 Ric_{ij}(g)

on a smooth closed Riemannian manifold (M^n, g(t)), primarily n = 3.

---

## 1. Forbidden Configurations

### F1. Scalar Diffusion

**Axiom source:** RF-1 (Metric State Variable), RF-2 (∂_t g = -2 Ric).

Ricci Flow does not diffuse a scalar field — it diffuses the *metric tensor*. The state variable g_{ij} has n(n+1)/2 components (6 for n = 3), not 1. The "diffusion" acts on the *geometry of space*, not on a function defined on space. The Ricci tensor Ric_{ij}(g) is a *geometric quantity* (involving curvature) that depends on g and its first and second derivatives — it is not a scalar Laplacian.

No scalar or vector field PDE can replicate RF's dynamics: the evolution of g changes distances, angles, volumes, and curvatures simultaneously — a fundamentally richer evolution than any field-on-a-fixed-domain PDE.

### F2. Hamiltonian Reversibility

**Axiom source:** RF-5 (Curvature-Driven Dissipation), RF-10 (Perelman's Entropy).

Ricci Flow is *dissipative* in Perelman's sense: the F-functional and W-entropy are *monotone non-decreasing*. The flow has a preferred time direction — forward in time corresponds to increasing entropy (Perelman W). Time-reversibility is forbidden.

However, the dissipation is *not classical Lyapunov dissipation* (no free energy decreases toward a minimum). Instead, Perelman's monotone quantities increase — the "entropy" of the geometry increases. This is closer to the thermodynamic arrow of time than to the gradient-flow energy decrease of AC/CH/PME.

### F3. Shock Formation

**Axiom source:** RF-2, RF-3 (Parabolic Character).

Ricci Flow is *parabolic* (second-order in g, acting like a heat equation for the metric). There is no first-order transport term (no u u_x, no v v_x). Shocks — discontinuities arising from characteristic crossing — are structurally absent. The RF singularities are *curvature concentrations* (smooth solutions whose curvature grows to infinity), not *discontinuities* (where the solution jumps).

### F4. Oscillatory Dispersion

**Axiom source:** RF-2, RF-3.

The time derivative partial_t g is *real* (not i partial_t g as in NLS). The evolution is *parabolic* (smoothing), not *dispersive* (oscillating). No wave-like behavior, no soliton-type oscillations, no phase interference. The RF solitons (gradient shrinking solitons) are *self-similar shapes*, not traveling waves.

### F5. Entropy Increase (Classical Sense)

**Axiom source:** RF-10 (Perelman Monotonicity).

Perelman's W-entropy *increases* along the flow (dW/dt >= 0). The F-functional also increases (under coupled evolution). But the *classical* notion of entropy (integral u log u for a density) does not directly apply — RF does not evolve a density. The forbidden configuration is the *decrease* of Perelman's W-entropy: the W-entropy cannot decrease under Ricci Flow. This is the RF's "second law of thermodynamics."

### F6. Nonlocal Forcing

**Axiom source:** RF-9 (No External Forcing), RF-2 (Local PDE).

Ricci Flow is *fully local*: the Ricci tensor at x depends on the metric g and its derivatives at x, not on the metric at distant points. There is no Poisson equation, no integral kernel, no nonlocal coupling. RF is local in the strongest sense — no nonlocal channel of any kind.

### F7. Global Regularity in All Cases

**Axiom source:** RF-7 (Singularities).

Ricci Flow develops singularities in finite time for many initial metrics (including all closed 3-manifolds that are not already Einstein). Global smooth solutions without singularity are the *exception*, not the rule. The formation of singularities is *structurally necessary* for the topology-classification program — the singularities reveal the topological decomposition of M.

### F8. Integrability

**Axiom source:** RF-2 (Nonlinear, Quasilinear PDE on Metrics).

Ricci Flow has no Lax pair, no bi-Hamiltonian structure, no inverse scattering transform, and no infinite hierarchy of conservation laws. The system is *not integrable* in the KdV/NLS sense. Perelman's monotone quantities (F, W, reduced volume) provide powerful control but are *finite in number* (three, not infinitely many). RF is a *non-integrable geometric PDE* — its resolution relies on PDE estimates and surgery, not on algebraic integrability.

### F9. Absence of Self-Similar Solutions

**Axiom source:** RF-8 (Scaling Symmetry).

Ricci Flow *does* have self-similar solutions — *gradient Ricci solitons*:

    Ric + Hess(f) = lambda g

These solitons are the canonical singularity models (round sphere S^n, cylinder S^{n-1} x R, Bryant soliton). They are the RF analogues of MCF's self-similar shrinkers, KdV's sech^2 solitons, and PME's Barenblatt profiles. Self-similar solutions are *not forbidden* — they are *necessary structural elements* of the singularity theory.

### F10. Static Topology

**Axiom source:** RF-7 (Singularities), RF-10 (Surgery).

Ricci Flow can *change the topology of the manifold* through the surgery procedure:
1. The flow develops a singularity (neck pinch).
2. The surgeon cuts the manifold at the neck.
3. The cut ends are capped with standard spherical caps.
4. The flow restarts on the (topologically modified) manifold.

Each surgery *simplifies* the topology: it reduces the number of prime summands in the connected-sum decomposition of M. After finitely many surgeries, the manifold decomposes into its geometric pieces (Thurston decomposition). *Static topology* — a topology that never changes during the flow — is forbidden for generic initial metrics.

### Summary of Forbidden Configurations

| Label | Forbidden Configuration               | Excluding Axiom(s)        |
|-------|---------------------------------------|---------------------------|
| F1    | Scalar diffusion (field on fixed domain)| RF-1, RF-2              |
| F2    | Hamiltonian reversibility             | RF-5, RF-10              |
| F3    | Shock formation                       | RF-2, RF-3               |
| F4    | Oscillatory dispersion                | RF-2, RF-3               |
| F5    | Perelman W-entropy decrease           | RF-10                    |
| F6    | Nonlocal forcing/coupling             | RF-2, RF-9               |
| F7    | Global regularity (all cases)         | RF-7                     |
| F8    | Integrability (Lax pair / IST)        | RF-2 (non-integrable)    |
| F9    | Absence of self-similar solutions     | RF-8 (solitons exist)    |
| F10   | Static topology                       | RF-7, RF-10 (surgery)    |

---

## 2. Necessary Configurations

### N1. Metric Tensor as State Variable

**Source:** RF-1.

The state g_{ij}(x, t) is a positive-definite symmetric 2-tensor on M — the Riemannian metric. It encodes all geometric information: lengths, angles, volumes, curvatures, geodesics. The metric has n(n+1)/2 independent components at each point (6 for n = 3).

### N2. Curvature Hierarchy (Rm, Ric, R)

**Source:** RF-1, RF-2.

The metric g determines the full curvature hierarchy:
- Riemann tensor Rm_{ijkl}: the complete curvature information. n^2(n^2-1)/12 independent components.
- Ricci tensor Ric_{ij} = g^{kl} Rm_{kilj}: the trace of Rm. n(n+1)/2 components.
- Scalar curvature R = g^{ij} Ric_{ij}: the trace of Ric. 1 component.

Ricci Flow evolves g by -2 Ric, which is the *trace part* of the full curvature. The Weyl tensor (the traceless part of Rm) evolves as a consequence but is not directly prescribed by the flow equation.

### N3. Curvature-Driven Parabolic Smoothing

**Source:** RF-2, RF-3.

The Ricci tensor Ric_{ij}(g) involves second derivatives of g (through the Christoffel symbols), making partial_t g = -2 Ric a *second-order parabolic system* (modulo gauge). The parabolic character provides:
- **Short-time existence:** For any smooth initial metric g_0, a unique smooth RF solution exists for a short time t in [0, T) (Hamilton, 1982).
- **Instantaneous smoothing:** If g_0 is C^k (k >= 2), then g(t) is C^{infinity} for t > 0.
- **Maximum principles:** Various curvature conditions are preserved and improved by the flow.

### N4. Diffeomorphism Invariance

**Source:** RF-4.

The RF equation partial_t g = -2 Ric is invariant under diffeomorphisms: if phi : M → M is a diffeomorphism and g(t) is a solution, then phi*g(t) is also a solution. This gauge freedom is *structural* — it reflects the fact that the geometry (equivalence class of metrics modulo diffeomorphisms) is the physically meaningful object, not the metric in a specific coordinate system.

### N5. DeTurck Trick (Strict Parabolicity)

**Source:** RF-3, RF-4.

The RF equation is *degenerate parabolic* — the symbol of the linearized operator has a kernel corresponding to the diffeomorphism gauge directions. The DeTurck trick adds a Lie derivative term L_X g that breaks the gauge symmetry and makes the equation strictly parabolic:

    partial_t g = -2 Ric + L_X g    (strictly parabolic)

This modified equation has the same geometric solutions as the original RF (the added term is a diffeomorphism, not a change in geometry). The DeTurck trick is the structural tool that converts the *weakly parabolic* RF into a *strictly parabolic* system, enabling the application of standard parabolic PDE theory.

### N6. Perelman's Monotone Quantities

**Source:** RF-10.

Perelman's three monotone quantities are the *deepest structural tools* of Ricci Flow:

**F-functional:**

    F(g, f) = integral_M (R + |nabla f|^2) e^{-f} dmu_g

Monotone under the coupled flow (partial_t g = -2 Ric, partial_t f = -Delta f + |nabla f|^2 - R): dF/dt >= 0.

**W-entropy:**

    W(g, f, tau) = integral_M [tau(R + |nabla f|^2) + f - n] (4 pi tau)^{-n/2} e^{-f} dmu_g

Monotone under the coupled backward flow (with tau = T - t): dW/dtau <= 0, equivalently dW/dt >= 0 (W increases forward in time).

**Reduced volume:**

    tilde{V}(tau) = (4 pi tau)^{-n/2} integral_M exp(-l(q, tau)) dmu_g(tau)

where l is the *reduced distance* (a distance function on spacetime defined via the L-functional). The reduced volume is monotone non-increasing: dtilde{V}/dtau <= 0.

These quantities:
- Control the geometry near singularities (the W-entropy prevents collapsing).
- Classify singularity types (the blowup limit is a gradient shrinking soliton when the reduced volume is close to its maximal value).
- Provide the *no-collapsing theorem* (kappa-noncollapsing: balls with bounded curvature have volume bounded below).
- Enable the *canonical neighborhood theorem* (near a singularity, the geometry is close to a standard model).

### N7. Singularity Formation

**Source:** RF-7.

For closed 3-manifolds that are not already Einstein metrics, Ricci Flow develops singularities in finite time:

    sup_M |Rm(g(t))| → infinity    as t → T*

The singularity types (for 3-manifolds):
- **Neck singularity:** The manifold develops a long thin S^2 x R neck that pinches to zero radius. The generic singularity type.
- **Extinction singularity:** The entire manifold shrinks to a round point (for positive Ricci curvature). Analogous to MCF convex-surface extinction.
- **Degenerate neckpinch:** A neck pinch with non-standard asymptotics.

### N8. Canonical Singularity Models (Ricci Solitons)

**Source:** RF-7, RF-8.

Near a singularity, the rescaled geometry converges to a *gradient shrinking Ricci soliton*:

    Ric + Hess(f) = (1/(2 tau)) g

The canonical models (for n = 3):
- **Round sphere S^3:** The extinction singularity model.
- **Round cylinder S^2 x R:** The neck singularity model.
- **Bryant soliton:** A rotationally symmetric steady soliton (Type II singularity model).

These solitons play the same role as MCF's shrinking spheres and cylinders (MCF Mode 1, N6), KdV's sech^2 solitons, and NLS's ground-state Q. They are the *universal blowup profiles* — the canonical shapes that every singularity approaches.

### N9. Scaling Symmetry

**Source:** RF-8.

If g(t) solves RF, then lambda g(lambda t) also solves RF. The parabolic scaling:
- Space rescales as lambda^{1/2} (lengths scale as sqrt(lambda)).
- Time rescales as lambda.
- Curvature rescales as lambda^{-1} (|Rm| decreases under rescaling).

The scaling symmetry identifies the *critical quantities*: |Rm| is scale-invariant in the sense that |Rm| * (T* - t) is a dimensionless quantity that classifies the singularity type (Type I: |Rm|(T* - t) bounded; Type II: |Rm|(T* - t) → infinity).

### N10. Surgery (Topological Continuation)

**Source:** RF-7, RF-10 (Hamilton–Perelman program).

When RF develops a singularity (neck pinch), the flow is continued via *surgery*:

1. **Identify the singular region:** A long thin neck (approximately S^2 x R) where the curvature is large.
2. **Cut:** Remove the neck.
3. **Cap:** Attach standard spherical caps (round 3-balls) to the cut ends.
4. **Restart:** Resume RF on the (topologically modified) manifold.

The surgery procedure:
- **Changes topology:** Each surgery reduces the number of prime summands in the connected-sum decomposition (or separates the manifold into components).
- **Is finitely many:** Perelman showed that only *finitely many* surgeries are needed before the flow either becomes extinct (all components shrink to points or collapse) or reaches a thick-thin decomposition.
- **Preserves the Perelman monotonicity:** The W-entropy and reduced volume continue to be monotone after surgery (with appropriate modifications).
- **Classifies topology:** After all surgeries, the remaining components carry one of Thurston's eight model geometries → the geometrization theorem.

### Summary of Necessary Configurations

| Label | Necessary Configuration                       | Source               |
|-------|-----------------------------------------------|----------------------|
| N1    | Metric tensor g_{ij} as state variable        | RF-1                 |
| N2    | Curvature hierarchy (Rm, Ric, R)              | RF-1, RF-2           |
| N3    | Curvature-driven parabolic smoothing          | RF-2, RF-3           |
| N4    | Diffeomorphism invariance                     | RF-4                 |
| N5    | DeTurck trick (strict parabolicity)           | RF-3, RF-4           |
| N6    | Perelman's monotone quantities (F, W, tilde{V})| RF-10              |
| N7    | Singularity formation (curvature blowup)      | RF-7                 |
| N8    | Canonical singularity models (Ricci solitons) | RF-7, RF-8           |
| N9    | Scaling symmetry (parabolic)                  | RF-8                 |
| N10   | Surgery (topological continuation)             | RF-7, RF-10          |

---

## 3. Envelope Inequalities (E1–E10)

---

**E1. Scalar Curvature Evolution**

    partial_t R = Delta R + 2 |Ric|^2

The scalar curvature R satisfies a *reaction-diffusion equation*: the Laplacian Delta R smooths R (diffusion), while the reaction term 2|Ric|^2 >= (2/n) R^2 is non-negative and quadratic. By the maximum principle:

    R_min(t) >= -n / (2(t + C))

The minimum scalar curvature increases (or stays constant if initially non-negative). For initially positive R: R stays positive for all time. The scalar curvature evolution is the *primary curvature control* — the simplest consequence of the RF equation.

---

**E2. Volume Evolution**

    d/dt Vol(M, g(t)) = -integral_M R dmu_g

Volume decreases when the average scalar curvature is positive; increases when negative. For the normalized RF (constant volume), the average curvature r = integral R / Vol evolves to determine the long-time behavior.

---

**E3. Maximum Principle for Curvature**

Hamilton's maximum principle for tensors: if the Riemann curvature tensor Rm satisfies an algebraic curvature condition C at t = 0 (e.g., Ric > 0, positive curvature operator, positive isotropic curvature), and if C is *preserved by the ODE* d/dt Rm = Rm^2 + Rm# (the reaction equation for the curvature), then C is preserved by the full PDE for all t > 0.

Key preserved conditions (for n = 3):
- Ric > 0 → Ric > 0 for all t → convergence to round S^3 (Hamilton, 1982).
- Positive curvature operator → positive curvature operator → convergence to space form.
- 2-positive curvature → 2-positive → classification of 4-manifolds (restricted).

---

**E4. Shi Estimates (Derivative Bounds from Curvature Bounds)**

If |Rm| <= K on M x [0, T] and T <= alpha/K, then:

    |nabla^k Rm| <= C(n, k, alpha) K / t^{k/2}    for t in (0, T]

Shi's estimates bound *all derivatives of curvature* by the curvature bound itself (with a time-dependent factor t^{-k/2} for the k-th derivative). This is the RF analogue of the parabolic smoothing estimate ||nabla^k u|| <= C t^{-k/2} ||u|| for the heat equation. The Shi estimates convert a *curvature bound* into *full regularity* — if the curvature is bounded, the metric is smooth (C^{infinity}).

**Structural role:** The Shi estimates are the *regularity mechanism* of RF: curvature control → derivative control → smoothness. They are the reason that the RF singularity is purely in the *curvature* (|Rm| → infinity) — if the curvature stayed bounded, the metric would remain smooth.

---

**E5. Perelman's F-Functional Monotonicity**

    dF/dt = 2 integral_M |Ric + Hess(f)|^2 e^{-f} dmu_g >= 0

The F-functional increases along the coupled flow. Equality holds iff Ric + Hess(f) = 0, i.e., iff (M, g) is a *gradient steady Ricci soliton*. The F-monotonicity:
- Provides a *lower bound* on the F-functional (it cannot decrease).
- Identifies *steady solitons* as the critical points of F.
- Connects RF to a *gradient-flow structure* on the space of metrics.

---

**E6. Perelman's W-Entropy Monotonicity**

    dW/dt >= 0    (W-entropy increases forward in time)

with equality iff (M, g) is a *gradient shrinking Ricci soliton*. The W-entropy:
- Controls the geometry near singularities.
- Provides *no-collapsing estimates* (E7 below).
- Classifies the *type of singularity* (the blowup limit must be a shrinking soliton when W is close to its maximum).
- Is the *deepest monotone quantity* in the Atlas — more powerful than Huisken's monotonicity formula (MCF), the log-HLS inequality (KS), or the Strichartz estimates (NLS).

---

**E7. Noncollapsing Theorem (kappa-Noncollapsing)**

**Perelman's noncollapsing:** There exists kappa > 0 such that if |Rm| <= r^{-2} on a ball B(x, r) at time t, then:

    Vol(B(x, r)) >= kappa r^n

The manifold *cannot collapse* — balls with bounded curvature must have volume bounded below. This prevents the manifold from becoming "infinitely thin" (like a long thin tube with bounded curvature but vanishing cross-section).

**Structural role:** The noncollapsing theorem is the *key structural estimate* that enables the classification of singularities: without it, the blowup limits could be arbitrarily collapsed (thin) and unclassifiable. With it, the blowup limits are noncollapsed → they must be shrinking solitons or their quotients → the singularity is classified.

---

**E8. Canonical Neighborhood Theorem**

For 3-dimensional RF, there exists epsilon > 0 such that every point (x, t) with |Rm(x, t)| >= r^{-2} (sufficiently large curvature) has a neighborhood that is epsilon-close (in the pointed Cheeger–Gromov sense) to one of:
- A shrinking round sphere S^3 (extinction model).
- A shrinking round cylinder S^2 x R (neck model).
- A cap (standard spherical cap attached to a cylinder).

The canonical neighborhood theorem says: *near a singularity, the geometry looks like a standard model*. This is the structural basis of the surgery procedure — the surgeon knows *exactly* what the geometry looks like near the singularity (a neck or a cap) and can cut and cap accordingly.

---

**E9. Blowup Criteria**

A smooth RF solution exists on [0, T) if and only if:

    sup_M |Rm(g(t))| < infinity    for all t in [0, T)

Equivalently: the solution becomes singular at T if and only if:

    lim_{t → T} sup_M |Rm(g(t))| = infinity

This is the RF analogue of the BKM criterion for NS (smooth iff vorticity bounded) and the regularity criterion for MCF (smooth iff second fundamental form bounded). The RF criterion is *resolved* (unlike NS, where the BKM criterion is conditional): we *know* that curvature blows up for generic initial metrics on closed 3-manifolds.

---

**E10. Classification of Singularity Types**

**Type I:** |Rm| <= C / (T* - t). Self-similar rate. The blowup limit is a *gradient shrinking Ricci soliton* (round sphere, round cylinder, or quotient).

**Type II:** |Rm| (T* - t) → infinity. Faster than self-similar. The blowup limit is an *ancient solution* (defined for all t in (-infinity, T*)). Example: Bryant soliton.

**Type III:** Immortal solutions (existing for all t in [0, infinity)). The curvature decays as |Rm| ~ 1/t. The blowup limit (at t → infinity, after rescaling) is an *expanding soliton*.

The classification is *complete for n = 3*: every singularity is either Type I (neck or extinction) or Type II (degenerate neckpinch). The Perelman monotonicity + noncollapsing + canonical neighborhoods provide the complete classification.

---

### Envelope Summary

**Tier 1 — Evolution Identities and Maximum Principles:**
- E1: Scalar curvature evolution (reaction-diffusion, R_min non-decreasing).
- E2: Volume evolution (d Vol/dt = -integral R).
- E3: Curvature maximum principles (preserved curvature conditions).
- E4: Shi estimates (curvature bound → full derivative control).

**Tier 2 — Perelman Monotonicity:**
- E5: F-functional monotonicity (gradient-flow structure).
- E6: W-entropy monotonicity (deepest monotone quantity).
- E7: Noncollapsing theorem (volume lower bound from curvature bound).

**Tier 3 — Singularity Structure:**
- E8: Canonical neighborhood theorem (near singularity → standard model).
- E9: Blowup criteria (smooth iff curvature bounded).
- E10: Singularity classification (Type I/II/III, complete for n = 3).

### Closure Assessment

The RF envelope is *closed with required singularities* — the same structural category as MCF:

- **Pre-singularity:** The envelope is fully closed. The Shi estimates (E4) convert curvature bounds into full regularity. The Perelman monotonicity (E5–E7) controls the geometry at all scales. The canonical neighborhood theorem (E8) classifies the geometry near high-curvature regions.

- **At singularity:** The curvature blows up (E9). The singularity is *fully classified* (E10): the blowup limit is a gradient shrinking soliton (Type I) or an ancient solution (Type II). The canonical neighborhood theorem (E8) ensures that the geometry near the singularity is a standard neck, cap, or sphere.

- **Post-singularity:** The surgery procedure (N10) continues the flow past the singularity. The topology changes (connected-sum decomposition simplifies). The Perelman monotonicity is preserved through surgery.

The RF envelope is *not fully closed in the classical sense* (singularities occur) but is *fully resolved* (every singularity is classified, and the surgery provides a geometric continuation). The "open face" is the singularity itself — but it is a *required, classified, and resolved* structural face, not an unresolved anomaly.

---

## 4. Central Architectural Finding

### 4.1 The RF Envelope: Geometric Parabolic with Resolved Singularities

The RF envelope is the *most structurally complex and profound* of any PDE in the Atlas:

| Feature                    | RF                            | All Other PDEs              |
|----------------------------|---------------------------------|----------------------------|
| State variable             | Metric tensor g_{ij}           | Scalar/vector/complex field or surface |
| Curvature type             | Intrinsic (Ric)                | Extrinsic (MCF) or none    |
| Monotone quantity          | Perelman W (deepest in Atlas)  | Lyapunov, Huisken Theta, etc. |
| Singularity classification | Complete (Type I/II/III)       | Complete (MCF, HJ/Burgers) or open (NS) |
| Surgery                    | Hamilton–Perelman (geometric)  | Level-set (MCF), entropy (HJ/Burgers), or none |
| Topological consequence    | Geometrization (classifies 3-manifolds) | Genus reduction (MCF) or none |
| Millennium Problem         | Solved (Poincare)              | Open (NS) or N/A           |

### 4.2 Perelman's Monotonicity as the Master Tool

Perelman's W-entropy and reduced volume are the *structural master tools* of Ricci Flow — they replace and surpass every other monotone quantity in the Atlas:

| Architecture | Monotone Quantity          | What It Controls                  |
|-------------|----------------------------|------------------------------------|
| AC/CH       | Free energy F              | H^1 norm, convergence to equilibrium |
| PME         | Entropy functionals        | L^p norms, convergence to Barenblatt |
| FP          | Relative entropy H         | L^1 norm, convergence to Gibbs     |
| MCF         | Huisken's Theta            | Local geometry near singularity     |
| KS          | Free energy F              | Global existence / blowup threshold |
| **RF**      | **Perelman W + reduced vol** | **Noncollapsing + singularity classification + canonical neighborhoods + surgery viability** |

Perelman's quantities control *more* than any other monotone quantity: not just a norm or a convergence rate but the *entire singularity structure* — noncollapsing, canonical neighborhoods, blowup limits, and the viability of the surgery procedure. They are the *most powerful structural tools* ever developed for a nonlinear PDE.

### 4.3 RF as the Geometric Parabolic Pole

The PDE Atlas now has a *geometric hierarchy*:

| Level                  | Architecture | State Variable      | Curvature Type | Topological Result     |
|------------------------|-------------|---------------------|----------------|------------------------|
| Scalar field           | FP/PME/AC/CH/TFE/HJ/Burgers/NLS/KdV/KS | u, phi, psi, rho | None | None |
| Vector field           | NS          | **u**(x,t)          | None           | None                  |
| Extrinsic geometry     | MCF         | Surface Gamma_t     | Extrinsic (H)  | Genus reduction       |
| **Intrinsic geometry** | **RF**      | **Metric g_{ij}**   | **Intrinsic (Ric)** | **Geometrization** |

RF is the *apex of the geometric hierarchy*: the most general state variable (metric tensor), the most intrinsic curvature (Ricci), and the deepest topological consequence (geometrization of 3-manifolds).

### 4.4 RF and ED: The Two Classificatory Architectures

The RF and ED share the *deepest structural parallel* in the Atlas: both architectures *classify their objects*:

- **ED:** The fundamental theorem of arithmetic classifies every integer by its prime factorization.
- **KdV:** The IST classifies every KdV solution by its scattering data.
- **RF:** The geometrization theorem classifies every closed 3-manifold by its geometric decomposition.

Ricci Flow's classification is the *most profound*: it classifies the *topology of 3-dimensional spaces* — the geometric structure of the universe itself. The classification proceeds through the flow (evolving the metric), the singularities (revealing the topological decomposition), and the surgery (implementing the decomposition). The RF is the *dynamical proof of the geometrization conjecture* — the PDE that *computes the topology of space*.

---

*End of Mode 1: Axiom → Envelope. Mode 2 (PDE → Extremal Dynamics) will follow in a subsequent file.*
