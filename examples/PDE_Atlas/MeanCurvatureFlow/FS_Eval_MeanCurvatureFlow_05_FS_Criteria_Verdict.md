# AD Evaluation: Mean Curvature Flow — AD Criteria and Verdict

Allen Proxmire

April 2026

---

## Overview

This file applies the six AD evaluation criteria to the Mean Curvature Flow as characterized in Modes 1–3. The MCF evaluation requires a conceptual extension of the AD framework: MCF is the first architecture whose state variable is a geometric object (a surface) rather than a function, whose singularities are *required* rather than anomalous, and whose state variable *ceases to exist* at the terminal time. These features do not map cleanly onto the categories developed for field-based PDEs (AC, CH, PME, TFE, FP, RD, NS), and the verdicts must be interpreted in the geometric context proper to MCF.

Throughout, we reference the axioms MCF-1 through MCF-8, the envelope inequalities E1–E10, the universal inequalities U1–U10, and the channel constraints C1–C12 established in the preceding files.

---

## 1. Minimality

**Question:** Do the MCF axioms form a minimal architectural set?

### 1.1 Assessment of Individual Axioms

**MCF-1 (Interface Hypothesis).** *Minimal.* The commitment to an evolving hypersurface as the state variable is the defining structural choice. Removing it collapses the geometric framework and requires a field-based description (AC, level set). No other axiom implies it. **Minimal.**

**MCF-2 (Locality).** *Minimal.* The velocity depends only on local curvature. Independent of other axioms — one could have nonlocal geometric flows (Mullins–Sekerka, surface diffusion) with the same state variable. **Minimal.**

**MCF-3 (V_n = H).** *Minimal.* The specific geometric law is the defining equation. It is the simplest local, parabolic, geometric evolution law for a hypersurface. Removing it or replacing it (V_n = K, V_n = H^2, V_n = Delta_Gamma H) produces a different geometric flow. **Minimal — this axiom *is* the architecture.**

**MCF-4 (No Bulk Field).** *Minimal.* The absence of a bulk field is an independent structural commitment that distinguishes MCF from all field-based architectures. It is not derivable from the other axioms — one could have V_n = H coupled to a bulk PDE (as in two-phase flow or crystal growth). **Minimal.**

**MCF-5 (Euclidean Ambient Space).** *Non-minimal.* MCF can be formulated in Riemannian manifolds (where H is computed with respect to the ambient metric). The Euclidean restriction is a geometric simplification. **Non-minimal.**

**MCF-6 (Gradient-Flow Structure).** *Derived, not independent.* The gradient-flow structure (MCF is the L^2 gradient flow of the area functional) is a *consequence* of MCF-3: the law V_n = H is exactly the steepest descent of A[Gamma] in the L^2 metric on normal vector fields. Given MCF-3, the gradient-flow structure follows automatically. **Redundant (derived from MCF-3).**

**MCF-7 (No Reaction/Forcing).** *Minimal.* The absence of external forcing is an independent commitment. Adding forcing (V_n = H + f) is a distinct architecture. **Minimal.**

**MCF-8 (No Conservation Law).** *Derived.* The non-conservation of area follows from the gradient-flow structure (dA/dt = -integral H^2 dS < 0 for non-minimal surfaces). This is not an independent axiom but a consequence of MCF-3 and MCF-6. **Redundant (derived).**

### 1.2 Minimality Summary

| Axiom | Content                    | Minimal?    | Comment                              |
|-------|----------------------------|-------------|--------------------------------------|
| MCF-1 | Interface hypothesis      | Yes         | Defines geometric framework          |
| MCF-2 | Locality                  | Yes         | Independent; excludes nonlocal flows |
| MCF-3 | V_n = H                   | Yes         | *Is* the architecture                |
| MCF-4 | No bulk field             | Yes         | Independent; excludes coupled systems|
| MCF-5 | Euclidean geometry        | **No**      | Geometric simplification             |
| MCF-6 | Gradient-flow structure   | Redundant   | Derived from MCF-3                   |
| MCF-7 | No reaction/forcing       | Yes         | Independent commitment               |
| MCF-8 | No conservation           | Redundant   | Derived from MCF-3 + MCF-6          |

**Structural core:** Five minimal axioms (MCF-1, MCF-2, MCF-3, MCF-4, MCF-7). One non-minimal (MCF-5). Two redundant (MCF-6, MCF-8).

**Criterion 1 Verdict: CONDITIONAL.** The structural core (five axioms) is fully minimal — the largest minimal core of any architecture in the Atlas. The single non-minimal element is the Euclidean geometry restriction (MCF-5), the same geometric simplification that appears in every other architecture. Two axioms are formally redundant (derivable from the others). The CONDITIONAL is due solely to MCF-5; the structural core itself would earn a PASS.

MCF has the *strongest minimality profile* of any architecture in the Atlas: five independent minimal axioms, one geometric simplification, zero constitutive selections. Unlike AC/CH (which select a specific free energy) and PME/TFE (which select a specific exponent), MCF has *no constitutive parameter at all* — the equation V_n = H has no adjustable coefficient.

---

## 2. Locality

**Question:** Is the MCF architecture fully local?

### 2.1 Assessment

The MCF velocity law V_n = H depends on the mean curvature at each point, which is determined by the surface's first and second fundamental forms at that point — an *infinitesimal neighborhood on the surface*. This is the strongest form of locality:

- No dependence on distant surface geometry.
- No bulk field coupling.
- No elliptic constraint (no Poisson equation, no Green's function).
- No integral operators.
- No nonlocal enforcement mechanism.

The locality is *intrinsic to the surface*: the relevant information at each point is the local curvature, which is a differential-geometric quantity involving only the surface's local embedding.

### 2.2 Comparison

MCF's locality is *strictly stronger* than every other architecture's:

- AC/CH/PME/TFE/FP/RD: local in the PDE sense (depend on field values and derivatives at each point in a bulk domain).
- NS: has a nonlocal channel (pressure Poisson equation).
- **MCF: local in the geometric sense (depend on curvature at each point *on the surface*, with no bulk domain at all).**

The absence of a bulk domain means there is no possibility of nonlocal coupling through a bulk mechanism — the only information channel is the surface's own geometry.

**Criterion 2 Verdict: PASS.** MCF achieves the strongest locality in the PDE Atlas — intrinsic geometric locality with no bulk field, no nonlocal channel, and no possibility of nonlocal coupling. This is the *maximum locality* that any PDE architecture can achieve.

---

## 3. Determinism

**Question:** Does the MCF architecture uniquely determine the future from the initial data?

### 3.1 Short-Time Well-Posedness

For any smooth closed hypersurface Gamma_0 in R^{d+1}:

- **Existence:** A unique smooth MCF solution exists for a short time t in [0, T) with T > 0.
- **Uniqueness:** The solution is unique among smooth solutions.
- **Smoothing:** If Gamma_0 is C^k (k >= 2), then Gamma_t is C^{infinity} for t > 0 (instantaneous regularization).
- **Geometric invariance:** The solution depends only on the geometric shape of Gamma_0, not on its parametrization.

Short-time determinism is *unconditional* — it holds for all smooth initial surfaces, all dimensions, with no constitutive parameters to tune.

### 3.2 The Singularity Question

For compact non-minimal surfaces, the smooth solution exists only up to a finite time T* < infinity, at which the curvature blows up. Beyond T*, the smooth MCF does not exist.

**Does this break determinism?** The answer depends on the interpretation:

**Classical (smooth) determinism: CONDITIONAL.** The smooth MCF uniquely determines Gamma_t for t in [0, T*). At T*, the smooth description fails. The classical determinism holds *up to the singularity* but not past it.

**Weak/extended determinism: PASS.** The level-set formulation (Evans–Spruck, Chen–Giga–Goto) provides a unique *weak solution* that exists for all t >= 0, passing through singularities via topology change. The level-set solution is unique, well-defined, and deterministic. Similarly, the Brakke varifold solution and the MCF-with-surgery provide extended notions of solution that are determined for all time.

### 3.3 Singularity is Structural, Not Anomalous

The key distinction: the MCF singularity is *not* a failure of determinism (as NS blowup would be). It is the architecture *completing its program*. The surface must shrink to a point (to reach zero area), and this requires curvature blowup. The singularity is the *mechanism* by which the architecture achieves its goal, not an obstacle to well-posedness.

The level-set solution provides a *globally determined* evolution: given Gamma_0, the future Gamma_t is uniquely determined for all t >= 0 (including through singularities). Determinism is not broken — it is *extended* through the singularity by the weak formulation.

### 3.4 Verdict

**Criterion 3 Verdict: CONDITIONAL.** Classical (smooth) determinism holds up to the first singularity time T*. Weak (level-set) determinism holds for all time. The singularity is structural, not anomalous — it is the architecture's mechanism for area minimization, not a failure of well-posedness. The CONDITIONAL reflects the fact that the *smooth* description terminates at T*, even though the *geometric* evolution is uniquely determined for all time through weak solutions.

**Comparison:** NS 3D determinism is FAIL (smooth solutions may not exist globally, and it is *unknown* whether weak solutions are unique). MCF determinism is CONDITIONAL (smooth solutions definitely terminate, but weak solutions are *known* to be unique). The MCF situation is *better resolved* than the NS situation — the answer is complete, even if the answer involves singularities.

---

## 4. Generative Sufficiency

**Question:** Does the MCF generate all of its observed phenomena from the axioms?

### 4.1 Generated Phenomena

| Phenomenon                                | Derivation Method                              |
|-------------------------------------------|------------------------------------------------|
| Finite-time extinction (convex)           | Huisken's theorem (1984)                       |
| Convexity preservation                    | Maximum principle for curvature tensors         |
| Convergence to round sphere               | Huisken's pinching estimate                     |
| Gage–Hamilton–Grayson (curves)            | Curve-shortening flow theory                    |
| Area dissipation identity                 | Direct computation from V_n = H                 |
| Huisken's monotonicity formula            | Backward heat kernel computation                |
| Type I singularity classification         | Blowup analysis + monotonicity                  |
| Self-similar shrinkers (sphere, cylinder) | ODE reduction via self-similar ansatz            |
| Neckpinch formation                       | Barrier arguments + Huisken–Sinestrari          |
| Surgery construction                      | Huisken–Sinestrari surgery program               |
| Level-set weak solutions                  | Evans–Spruck / Chen–Giga–Goto viscosity theory  |
| Topological monotonicity                  | Surgery + maximum principle                      |
| Angenent torus (compact shrinker)         | Shooting method for ODE                          |
| Parabolic smoothing estimates             | Standard parabolic regularity                    |

The MCF generates *all* of its major phenomena from the axioms through rigorous mathematical proofs. The theory is remarkably complete — the classification of singularities, the surgery program, and the weak-solution theory together provide a complete description of the evolution for all time.

### 4.2 Phenomena MCF Cannot Generate

| Phenomenon              | Reason for Absence                       |
|------------------------|------------------------------------------|
| Bulk field dynamics    | No bulk PDE (MCF-4)                     |
| Oscillations           | Gradient-flow monotonicity (MCF-6)      |
| Spatial patterns       | One surface, no reaction (MCF-7)        |
| Chaos                  | Monotone dynamics                        |
| Coarsening             | No conserved bulk quantity               |
| Phase separation       | No double-well potential                 |
| Traveling waves        | No reaction or forcing                   |
| Turbulence             | No transport equation                    |

These absences are structural consequences of the pure-geometric architecture, not generative failures.

### 4.3 Assessment

MCF is *completely generatively sufficient within its geometric scope*. Every phenomenon of curvature-driven surface evolution — extinction, singularity, topology change, self-similar profiles, surgery continuation — is rigorously derived from the axioms. The generative gap is *essentially zero*: the few remaining open problems (complete classification of all Type II singularities, optimal regularity of level-set solutions in high dimensions) are technical refinements within the established framework, not paradigmatic gaps.

**Criterion 4 Verdict: PASS.** Zero generative gap within the geometric scope. Complete theory: every major phenomenon rigorously derived. The MCF theory is one of the most complete geometric PDE theories in mathematics.

---

## 5. Envelope Tightness

**Question:** Is the MCF envelope closed and tight?

### 5.1 Assessment of Envelope Components

**E1 (Area dissipation).** Exact identity. **Tight.**

**E2 (Curvature L^2 dissipation).** Non-closing inequality — reflects the structural necessity of singularity formation. **Not tight** (intentionally: the non-closure is the architectural mechanism for singularity).

**E3 (Small-scale smoothing).** Sharp parabolic estimate (|A| <= C/sqrt(t)). **Tight** before singularity.

**E4 (Extinction-time bound).** Sharp for spheres: T* = R_0^2/(2d). **Tight.**

**E5 (Huisken's monotonicity formula).** Exact monotone quantity. **Tight.**

**E6 (Scale-invariant blowup profiles).** Classified for Type I. **Tight** (for Type I; Type II classification ongoing).

**E7 (Area–curvature–extinction relations).** Sharp for convex surfaces. **Tight.**

**E8 (Topological monotonicity).** Exact: topology only simplifies. **Tight.**

**E9 (Geometric invariance).** Exact structural property. **Tight.**

**E10 (Regularity criterion).** Exact: smooth iff curvature bounded. **Tight** (and resolved — curvature *does* blow up for compact non-minimal surfaces).

### 5.2 The Required Singularity Face

The MCF envelope has one face that is not "closed" in the classical sense: the *curvature-blowup face* (related to E2). But this face is not an anomaly — it is a *required structural feature*:

- It is *certain* (not open, as in NS).
- It is *classified* (Type I shrinkers, Type II eternal solutions).
- It has a *continuation* (surgery, level-set, varifold).
- It is *necessary* for the architecture's goal (area minimization requires extinction requires singularity).

In the standard AD framework (designed for field-based PDEs), a non-closing inequality indicates a structural gap. In the geometric MCF framework, the non-closure of E2 indicates a *structural transition point* — the moment when the smooth description gives way to the weak description. This is not a gap but a *feature*.

### 5.3 Verdict

**Criterion 5 Verdict: CONDITIONAL.** Nine of ten envelope components are tight. The one non-tight component (E2, curvature L^2 dissipation) reflects the structural necessity of singularity formation — it is a *required* non-closure, not an anomalous one. In the smooth regime (before singularity), the envelope is fully tight. In the extended regime (through singularity via weak solutions), the envelope is completed by the surgery program and level-set theory.

The CONDITIONAL reflects the fact that the *smooth envelope* does not close (curvature blows up) even though the *geometric evolution* is fully determined. If the AD framework is extended to include required singularities as a legitimate structural feature (rather than treating all singularities as defects), the verdict would be PASS.

---

## 6. Structural Optimality

**Question:** Is the MCF architecture optimal?

### 6.1 Anomaly Assessment

MCF has *zero anomalies* in the standard FS sense:

- **No nonlocal channel.** All dynamics are local (curvature at each point).
- **No destabilizing sub-channel.** The curvature channel K is uniformly stabilizing (dA/dt <= 0).
- **No oscillatory face.** Gradient flow forbids limit cycles.
- **No chaotic face.** Monotone dynamics.
- **No bulk-blowup face.** No bulk PDE exists.
- **No pattern-formation face.** Single surface, no reaction.

The curvature singularity is *not* an anomaly — it is a required structural feature (see Mode 3, Section 4). The singularity is the architecture's mechanism for achieving its goal, not a defect in its operation.

### 6.2 Structural Economy

MCF is the *most structurally economical* architecture in the PDE Atlas by multiple measures:

- **Fewest channels:** 3 (K, G, T). Every other architecture has 4 or more.
- **Zero bulk degrees of freedom.** Every other architecture has at least one bulk field.
- **Zero constitutive parameters.** The equation V_n = H has no adjustable coefficient (no epsilon, no nu, no D, no m, no n, no b). Every other architecture has at least one constitutive parameter.
- **One generating functional.** The area A[Gamma] generates the entire dynamics through a single variational derivative (H = -delta A / delta Gamma).
- **One equation.** V_n = H. The shortest PDE specification in the Atlas.

No simpler architecture generates the MCF phenomenology. The heat equation (partial_t u = Delta u) is simpler but operates on a fixed domain, not on an evolving surface. Curve shortening (V_n = kappa) is the d = 1 case of MCF, not a different architecture. There is no geometric flow simpler than MCF that is both parabolic and nontrivial.

### 6.3 Comparison

| Feature                  | MCF         | PME        | FP         | AC         | NS              |
|--------------------------|-------------|------------|------------|------------|-----------------|
| Anomalies                | 0           | 0          | 0          | 0          | 2               |
| Constitutive parameters  | **0**       | 1 (m)      | 2 (b, D)   | 3          | 2               |
| Channel count            | **3**       | 4          | 4          | 4          | 5               |
| Bulk fields              | **0**       | 1          | 1          | 1          | 1 (+ pressure)  |
| Non-minimal axioms       | 1           | ~1.5       | ~1.5       | 3          | 3               |
| Required singularity     | **Yes**     | No         | No         | No         | Open            |

### 6.4 Verdict

**Criterion 6 Verdict: PASS.** Zero anomalies. Maximum structural economy (fewest channels, zero bulk fields, zero constitutive parameters, one generating functional, one equation). No simpler architecture generates the same geometric phenomenology. The required singularity is a structural feature, not an anomaly. MCF is the *most structurally optimal* architecture in the PDE Atlas.

---

## 7. FS Verdict Summary

### 7.1 Criteria Scorecard

| Criterion                  | Verdict         | Comment                                              |
|----------------------------|-----------------|------------------------------------------------------|
| **1. Minimality**          | CONDITIONAL     | 5 minimal axioms (strongest core); MCF-5 non-minimal |
| **2. Locality**            | **PASS**        | Strongest locality in Atlas (geometric, no bulk)     |
| **3. Determinism**         | CONDITIONAL     | Smooth: up to T*. Weak: all time. Singularity structural. |
| **4. Gen. Sufficiency**    | **PASS**        | Zero gap. Complete geometric theory.                 |
| **5. Envelope Tightness**  | CONDITIONAL     | 9/10 tight. Singularity face required, not anomalous.|
| **6. Structural Optimality** | **PASS**      | Zero anomalies. Maximum economy. Zero parameters.    |

**Score: 3 PASS + 3 CONDITIONAL.**

### 7.2 Comparison Across the PDE Atlas

| Criterion             | ED   | FP         | PME        | AC         | CH         | TFE(n>=1) | MCF        | NS(3D)   | RD        |
|-----------------------|------|------------|------------|------------|------------|-----------|------------|----------|-----------|
| Minimality            | PASS | COND.      | COND.      | FAIL       | FAIL       | COND.     | **COND.**  | FAIL     | COND.     |
| Locality              | PASS | PASS       | PASS       | PASS       | PASS       | PASS      | **PASS**   | COND.    | PASS      |
| Determinism           | PASS | PASS       | PASS       | PASS       | PASS       | PASS      | **COND.**  | FAIL     | COND.     |
| Gen. Sufficiency      | PASS | PASS       | PASS       | COND.(w)   | COND.(w)   | PASS      | **PASS**   | COND.    | PASS      |
| Envelope Tightness    | PASS | PASS       | PASS       | PASS       | PASS       | PASS      | **COND.**  | COND.    | COND.     |
| Structural Optimality | PASS | PASS       | PASS       | COND.      | COND.      | PASS      | **PASS**   | FAIL     | COND.     |
| **Total PASS**        | **6**| **5**      | **5**      | **3**      | **3**      | **4**     | **3**      | **0**    | **2**     |

### 7.3 Architectural Summary

The Mean Curvature Flow achieves a distinctive FS profile: 3 PASSes + 3 CONDITIONALs. The three PASSes (Locality, Generative Sufficiency, Structural Optimality) are among the *strongest* in the Atlas:

- **Locality:** The strongest locality of any architecture — geometric, intrinsic, no bulk field, no nonlocal coupling.
- **Generative Sufficiency:** Zero generative gap — a complete geometric theory with rigorous classification of singularities, surgery program, and weak solutions.
- **Structural Optimality:** The most economical architecture — zero anomalies, zero constitutive parameters, three channels, one equation.

The three CONDITIONALs (Minimality, Determinism, Envelope Tightness) all trace to the same structural feature: the *required singularity*:

- **Minimality:** CONDITIONAL due to Euclidean geometry restriction (MCF-5), the same weakness as every other architecture. The structural core (5 axioms) is the most minimal in the Atlas.
- **Determinism:** CONDITIONAL because smooth solutions terminate at the singularity time T*. Weak solutions (level-set, surgery) are uniquely determined for all time. The singularity is *resolved* (unlike NS, where it is open).
- **Envelope Tightness:** CONDITIONAL because the curvature dissipation inequality (E2) does not close — reflecting the structural necessity of singularity. The envelope is tight in the smooth regime and *completed* (not closed) in the singular regime.

The MCF profile illustrates a fundamental tension in the AD framework: the criteria were designed for *field-based PDEs* where singularity is always a failure. MCF is a *geometric PDE* where singularity is a *success* — the architecture completing its area-minimization program. The three CONDITIONALs reflect this category mismatch, not a genuine structural deficiency. If the FS criteria were extended to treat required singularities as a legitimate structural feature, MCF's three CONDITIONALs would strengthen to PASSes, giving a score of 6/6 — tying ED for the strongest profile in the Atlas.

### 7.4 MCF's Unique Position

MCF is the *only geometric architecture* in the PDE Atlas. It is the only system where:

1. The state variable is a *surface*, not a function.
2. There are *zero* bulk degrees of freedom.
3. There are *zero* constitutive parameters.
4. Singularity is *required and classified*, not open or anomalous.
5. The state variable *ceases to exist* at the terminal time.
6. *Topology change* is built into the dynamics.

No other architecture possesses any of these features. MCF is structurally *orthogonal* to the entire field-based PDE Atlas — it models a fundamentally different type of mathematical object through a fundamentally different mechanism with a fundamentally different outcome.

### 7.5 Composite Verdict

Mean Curvature Flow is the purest geometric architecture in the PDE Atlas — a parameter-free, bulk-free, maximally local, anomaly-free curvature flow that achieves area minimization through structurally necessary singularity formation, producing a complete theory of surface extinction, topology change, and self-similar blowup that stands as the geometric counterpart to the arithmetic perfection of the Factor Skyline.

---

*End of AD Criteria and Verdict. This completes the AD architectural evaluation of Mean Curvature Flow.*
