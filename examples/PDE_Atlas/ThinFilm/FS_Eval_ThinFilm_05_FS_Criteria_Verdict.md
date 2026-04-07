# AD Evaluation: Thin-Film Equation — AD Criteria and Verdict

Allen Proxmire

April 2026

---

## Overview

This file applies the six AD evaluation criteria to the Thin-Film Equation as characterized in Modes 1–3. The TFE evaluation is unique in the PDE Atlas because the verdicts are *n-dependent*: the mobility exponent n > 0 determines whether the architecture is fully closed (n >= 1) or has an open positivity face (0 < n < 1). The evaluation therefore produces *two verdict profiles* — one for the physical regime n >= 1, and one for the weak-degeneracy regime 0 < n < 1.

Throughout, we reference the axioms TFE-1 through TFE-8, the envelope inequalities E1–E10, the universal inequalities U1–U10, and the channel constraints C1–C12 established in the preceding files.

---

## 1. Minimality

**Question:** Do the TFE axioms form a minimal architectural set?

### 1.1 Assessment of Individual Axioms

**TFE-1 (Continuum Hypothesis).** *Minimal within paradigm.* Required for the field-theoretic formulation. **Minimal.**

**TFE-2 (Locality).** *Minimal.* Defines the PDE paradigm. **Minimal.**

**TFE-3 (Fourth-Order Degenerate Diffusion).** *Minimal.* This is the defining structural commitment — the single axiom that makes the TFE what it is. The fourth-order character arises from the capillary-pressure mechanism (p = -Delta h, flux driven by nabla p), and the degeneracy (h^n) arises from the viscous-flow velocity profile integrated across the film thickness. Removing either the fourth-order structure or the degeneracy produces a different architecture (CH without degeneracy, PME without fourth order). Neither feature is derivable from the other. **Minimal.**

**TFE-4 (Conservation).** *Minimal.* An independent structural commitment. Conservation shapes the spreading dynamics and couples height decay to support expansion. Removing it (non-conserved fourth-order degenerate diffusion) would produce a different architecture — a "degenerate Allen–Cahn at fourth order" that does not appear in the standard literature. **Minimal.**

**TFE-5 (Euclidean Geometry).** *Non-minimal.* The TFE can be formulated on curved substrates. The flat-substrate restriction is a geometric simplification. **Non-minimal.**

**TFE-6 (Forward Parabolic).** *Minimal within paradigm.* Required for well-posedness. **Minimal.**

**TFE-7 (No Reaction).** *Minimal as a structural commitment.* The absence of reaction, evaporation, condensation, and Marangoni effects is a deliberate choice that isolates the capillary-driven spreading dynamics. Adding any of these would extend the architecture. **Minimal.**

**TFE-8 (Exponent n > 0).** *Partially non-minimal.* The regime n > 0 (degenerate) is structural — it defines the degenerate class. The specific value of n (n = 1, n = 3, etc.) is constitutive — different physical systems correspond to different n. The restriction n > 0 is minimal; the specific n is constitutive. **Partially non-minimal.**

### 1.2 Minimality Summary

| Axiom | Content                           | Minimal?         | Comment                            |
|-------|-----------------------------------|------------------|------------------------------------|
| TFE-1 | Continuum                        | Within paradigm  | Defines field theory               |
| TFE-2 | Locality                         | Yes              | Defines PDE paradigm               |
| TFE-3 | Fourth-order degenerate diffusion| Yes              | *Is* the architecture              |
| TFE-4 | Conservation                     | Yes              | Independent structural commitment  |
| TFE-5 | Euclidean geometry               | **No**           | Geometric simplification           |
| TFE-6 | Forward parabolic                | Within paradigm  | Required for well-posedness        |
| TFE-7 | No reaction                      | Yes              | Defines pure-diffusion class       |
| TFE-8 | Exponent n > 0                   | Partially        | Regime structural; specific n constitutive |

**Criterion 1 Verdict: CONDITIONAL.** The structural core (TFE-2, TFE-3, TFE-4, TFE-7) is fully minimal — four independent, irreducible axioms defining the fourth-order degenerate conserved pure-diffusion architecture. The non-minimal elements are TFE-5 (Euclidean geometry) and the specific value of n (constitutive). This is the *same minimality profile* as the PME (which also has ~1.5 non-minimal elements) and stronger than AC/CH/NS (which each have 3 non-minimal axioms).

**n-dependence:** The minimality verdict does not depend on n. The structural core is minimal for all n > 0.

---

## 2. Locality

**Question:** Is the TFE architecture fully local?

### 2.1 Assessment

Every channel is local:

- **D_4:** -div(h^n nabla Delta h). Involves h and its derivatives up to fourth order at each point. Local.
- **C:** The mass integral is global, but enforced locally through divergence form. No nonlocal solve.
- **G:** The contact-line velocity depends on the local height profile. Local.
- **M:** Parameter. N/A.

No elliptic constraint, no Poisson equation, no Green's function, no integral operator. The TFE is fully local at both formulation and solution levels.

### 2.2 Comparison

The TFE shares the locality class of AC, CH, PME, and RD — all fully local. Only NS has a nonlocal channel (pressure Poisson equation).

**Subtlety:** The TFE's fourth-order structure involves *more derivatives* than the PME's second-order structure, but it remains *local* — higher-order derivatives are still pointwise operators. Fourth-order locality is the same *class* of locality as second-order; it merely involves a wider stencil in numerical discretizations, not a conceptual change in the locality structure.

### 2.3 Verdict

**Criterion 2 Verdict: PASS.** Fully local at both formulation and solution levels, for all n > 0. No nonlocal channel.

**n-dependence:** None. Locality is independent of n.

---

## 3. Determinism

**Question:** Does the TFE uniquely determine the future from the initial data?

### 3.1 Assessment by n-Regime

**n >= 1 (physical regime, including n = 3):**

- **Existence:** Global-in-time weak solutions exist for all h_0 in L^1, h_0 >= 0, in d = 1 and d = 2. Established through compactness methods and approximation by non-degenerate regularizations.
- **Uniqueness:** Solutions are unique in appropriate weak-solution classes. Uniqueness proofs use the energy structure and the degenerate-parabolic comparison framework.
- **Positivity:** h_0 >= 0 implies h(t) >= 0 for all t > 0 (the degeneracy prevents negative excursions).
- **Finite-speed propagation:** Compact support is preserved. The contact line moves at finite speed.
- **Regularity:** h is C^{infinity} in the interior of {h > 0} and Holder continuous across the contact line.

**Determinism verdict for n >= 1: PASS.** Global existence, uniqueness, positivity, finite speed, and regularity are all established.

**0 < n < 1 (weak degeneracy):**

- **Existence:** Weak solutions exist (by similar compactness methods).
- **Uniqueness:** Established in appropriate classes.
- **Positivity:** *May fail.* The fourth-order operator can drive h below zero. Solutions may develop negative excursions near the contact line.
- **Finite-speed propagation:** May fail for very small n (the degeneracy is too weak to confine the support).
- **Regularity:** Interior regularity holds; contact-line regularity is more delicate.

**Determinism verdict for 0 < n < 1: CONDITIONAL.** Existence and uniqueness hold, but positivity may fail. If h becomes negative, the *physical interpretation* breaks down (negative film height is meaningless), even though the *mathematical solution* continues to exist. The determinism is *mathematically intact* but *physically compromised*.

### 3.2 Overall Verdict

**Criterion 3 Verdict: CONDITIONAL.** For n >= 1: full determinism (existence, uniqueness, positivity, regularity). For 0 < n < 1: mathematical determinism holds but physical determinism is compromised by potential positivity failure.

**n-dependence:** The verdict is n-dependent. PASS for n >= 1; CONDITIONAL for 0 < n < 1.

---

## 4. Generative Sufficiency

**Question:** Does the TFE generate all of its observed laws from the axioms?

### 4.1 Generated Phenomena

| Phenomenon                          | Derivation Method                            |
|-------------------------------------|----------------------------------------------|
| Finite-speed contact-line motion    | Comparison with self-similar sub-solutions   |
| Contact-line velocity (Darcy law)   | Matched asymptotics at the contact line       |
| Waiting-time phenomena              | Local regularity analysis near flat profiles |
| Self-similar source-type spreading  | ODE reduction via self-similar ansatz         |
| Fourth-order interior smoothing     | Parabolic regularity theory                   |
| Energy dissipation identity         | Direct computation from PDE                   |
| Contact-angle selection (n = 3)     | Tanner's law from lubrication analysis        |
| Universal convergence to attractor  | Entropy methods + energy estimates             |
| Positivity preservation (n >= 1)    | Entropy functional control                     |
| No blowup (n >= 1)                 | Mass + energy + interpolation bounds           |

The TFE generates *all* of its characteristic phenomena from the axioms. The theory is complete within the architecture's scope: every qualitative behavior of TFE solutions is derived from the axioms through rigorous or formal-asymptotic methods.

### 4.2 Phenomena TFE Cannot Generate

| Phenomenon           | Reason for absence                    |
|---------------------|---------------------------------------|
| Oscillations        | No reaction channel (TFE-7)          |
| Turing patterns     | n = 1 species, no reaction (TFE-7)  |
| Traveling waves     | No bistable/monostable reaction      |
| Spiral waves        | n = 1 species, no reaction           |
| Chaos               | Gradient-flow monotonicity           |
| Blowup              | Fourth-order smoothing + conservation|
| Phase separation    | No double-well potential             |
| Coarsening (CH-type)| No competing phases                  |

These absences are *structural consequences* of the pure-diffusion architecture, not failures of generative sufficiency. The TFE is designed to model capillary-driven film spreading; asking it to produce reaction-diffusion phenomena is outside its scope.

### 4.3 Generative Gap Assessment

The TFE's generative gap is *essentially zero within its scope*:

- Every TFE-specific phenomenon (contact-line motion, waiting times, self-similar spreading, contact-angle selection) is rigorously or formally derived from the axioms.
- The only missing rigorous results are *sharp regularity at the contact line* for general initial data and *optimal convergence rates* to the self-similar attractor — both are technical gaps within the existing framework, not paradigmatic gaps requiring new theory.

### 4.4 Verdict

**Criterion 4 Verdict: PASS.** The TFE generates all of its characteristic phenomena from the axioms. The generative gap is negligible (sharp regularity and optimal rates). Within its scope, the theory is essentially complete.

**n-dependence:** The generative sufficiency does not depend on n. The architecture generates the same qualitative phenomena for all n > 0 (with quantitative differences in spreading rates and regularity exponents).

---

## 5. Envelope Tightness

**Question:** Is the TFE envelope closed and tight?

### 5.1 Assessment of Envelope Components

**E1 (Energy dissipation identity).** Exact equality. **Tight.**

**E2 (Mass conservation).** Exact identity. **Tight.**

**E3 (Fourth-order smoothing).** Sharp estimates (classical fourth-order parabolic theory). **Tight.**

**E4 (Finite-speed bound, n >= 1).** Saturated by self-similar solutions. **Tight** for n >= 1.

**E5 (Self-similar scaling).** Exact exponents alpha, beta determined by n, d. **Tight.**

**E6 (Entropy/energy functionals).** Bounds from the gradient-flow structure. **Tight** (exact identity for the primary energy E).

**E7 (Curvature bounds).** Derived from energy via interpolation. Tight within the energy framework.

**E8 (No blowup, n >= 1).** Sharp decay bound. **Tight** for n >= 1.

**E9 (Energy monotonicity).** Exact Lyapunov property. **Tight.**

**E10 (Positivity, n-dependent).** For n >= 1: positivity preserved (tight). For 0 < n < 1: positivity may fail (open face).

### 5.2 Closure Assessment

**n >= 1:** The envelope is *fully closed*. Four sealing mechanisms operate:
1. Fourth-order smoothing (high-k face sealed).
2. Degeneracy at h = 0 (contact-line face sealed).
3. Conservation (mass face sealed).
4. Gradient-flow monotonicity (oscillation/chaos face sealed).
5. Entropy method (positivity face sealed for n >= 1).

All ten envelope components are tight. No open faces.

**0 < n < 1:** The envelope has *one open face* (positivity, E10). The other nine components remain tight. The architecture has a single parametric gap.

### 5.3 Verdict

**Criterion 5 Verdict: CONDITIONAL.** For n >= 1: PASS (all components tight, fully closed). For 0 < n < 1: one open face (positivity).

**n-dependence:** PASS for n >= 1; CONDITIONAL for 0 < n < 1.

---

## 6. Structural Optimality

**Question:** Is the TFE architecture optimal?

### 6.1 Anomaly Assessment

**n >= 1 (physical regime):**

- **No nonlocal channel.** All channels local.
- **No destabilizing sub-channel.** The sole channel (D_4) is unconditionally stabilizing.
- **No oscillatory mechanism.** Gradient-flow structure forbids oscillations.
- **No chaotic mechanism.** Monotone dynamics.
- **No blowup mechanism.** Fourth-order smoothing + conservation.
- **No positivity violation.** Strong degeneracy (n >= 1) prevents negative h.
- **No dimensional bifurcation.** Same qualitative behavior in d = 1, 2.

*Zero anomalies for n >= 1.*

**0 < n < 1 (weak degeneracy):**

- All the above *except*: positivity may fail. The fourth-order operator, lacking a maximum principle, can produce negative h when the degeneracy is too weak to compensate.

*One parametric anomaly for 0 < n < 1.*

### 6.2 Structural Economy

The TFE has the same channel count as PME (4 channels) and the same channel types (one dynamical, one constraint, one geometric, one parametric). It achieves fourth-order smoothing with the same structural economy as the PME achieves second-order smoothing. No simpler fourth-order degenerate conserved architecture exists.

### 6.3 Comparison

| Feature                  | PME         | TFE (n>=1) | TFE (n<1)   | AC          | CH          |
|--------------------------|-------------|------------|-------------|-------------|-------------|
| Anomalies                | 0           | 0          | 1 (positivity)| 0         | 0           |
| Non-minimal axioms       | ~1.5        | ~1.5       | ~1.5        | 3           | 3           |
| Channel count            | 4           | 4          | 4           | 4           | 5           |
| Constraint surface       | Closed      | Closed     | 1 open face | Closed      | Closed      |
| Structural economy       | Highest (2nd)| Highest (4th)| Highest (4th)| High     | Moderate    |

### 6.4 The Positivity Tension

The TFE's single anomaly (for n < 1) arises from a *structural tension* between two inherited features:

- **Fourth-order character** (from CH): removes the maximum principle.
- **Degeneracy** (from PME): requires h >= 0 for physical consistency.

This tension exists only in the bottom-right corner of the 2×2 hierarchy. In the other three corners:
- AC (top-left): has the maximum principle (second-order). No tension.
- CH (top-right): has no degeneracy (h is not required to be non-negative). No tension.
- PME (bottom-left): has the comparison principle (second-order). No tension.

The TFE is the *only* architecture where these two requirements collide. For n >= 1, the collision is resolved (strong degeneracy wins). For n < 1, it is not.

### 6.5 Verdict

**Criterion 6 Verdict: CONDITIONAL.** For n >= 1: zero anomalies, highest fourth-order structural economy, no simpler architecture generates the same phenomena. For 0 < n < 1: one parametric anomaly (positivity).

**n-dependence:** Effectively PASS for n >= 1; CONDITIONAL for 0 < n < 1.

---

## 7. FS Verdict Summary

### 7.1 Criteria Scorecard

| Criterion                  | n >= 1 (physical) | 0 < n < 1 (weak degen.) | Comment                             |
|----------------------------|-------------------|-------------------------|-------------------------------------|
| **1. Minimality**          | CONDITIONAL       | CONDITIONAL             | ~1.5 non-minimal elements (same both regimes) |
| **2. Locality**            | **PASS**          | **PASS**                | Fully local, all n                  |
| **3. Determinism**         | **PASS**          | CONDITIONAL             | Positivity may fail for n < 1       |
| **4. Gen. Sufficiency**    | **PASS**          | **PASS**                | Complete theory, all n              |
| **5. Envelope Tightness**  | **PASS**          | CONDITIONAL             | Positivity face open for n < 1      |
| **6. Structural Optimality** | **PASS**        | CONDITIONAL             | One anomaly for n < 1               |

**Score summary:**
- n >= 1: 4 PASS + 1 CONDITIONAL = strong profile (comparable to PME's 5 PASS + 1 CONDITIONAL).
- 0 < n < 1: 2 PASS + 4 CONDITIONAL = moderate profile (comparable to NS 2D).

### 7.2 Comparison Across the PDE Atlas

| Criterion             | ED   | PME        | AC         | CH         | TFE (n>=1) | TFE (n<1) | NS (3D)  | RD        |
|-----------------------|------|------------|------------|------------|------------|-----------|----------|-----------|
| Minimality            | PASS | COND.      | FAIL       | FAIL       | COND.      | COND.     | FAIL     | COND.     |
| Locality              | PASS | PASS       | PASS       | PASS       | **PASS**   | **PASS**  | COND.    | PASS      |
| Determinism           | PASS | PASS       | PASS       | PASS       | **PASS**   | COND.     | FAIL     | COND.     |
| Gen. Sufficiency      | PASS | PASS       | COND.(w)   | COND.(w)   | **PASS**   | **PASS**  | COND.    | PASS      |
| Envelope Tightness    | PASS | PASS       | PASS       | PASS       | **PASS**   | COND.     | COND.    | COND.     |
| Structural Optimality | PASS | PASS       | COND.      | COND.      | **PASS**   | COND.     | FAIL     | COND.     |

### 7.3 Architectural Summary

The Thin-Film Equation is the *fourth-order degenerate member* of the gradient-flow PDE family — the bottom-right corner of the 2×2 hierarchy (AC, CH, PME, TFE). It combines the strongest structural features of its three ancestors: fourth-order k^4 smoothing from CH, degenerate mobility and free-boundary geometry from PME, and conservation + gradient-flow structure from both. In the physical regime n >= 1, this combination produces an architecture that is fully closed, anomaly-free, and essentially complete — matching the PME's structural soundness at one higher order of differentiability.

The TFE's single structural vulnerability — the positivity question for 0 < n < 1 — is a *tension* between two inherited features that collide only in the bottom-right corner of the hierarchy: the fourth-order character (which removes the maximum principle) and the degeneracy (which requires non-negative solutions for physical consistency). For n >= 1, the degeneracy is strong enough to resolve this tension; for n < 1, it is not. This n-dependent resolution produces the *only parametric bifurcation* in the PDE Atlas — a single scalar parameter determining whether the architecture is fully self-consistent.

The TFE demonstrates a general FS principle: *combining structural features from different ancestors can introduce new tensions that neither ancestor possesses alone*. The maximum-principle/positivity tension is absent in both CH (no degeneracy, no positivity requirement) and PME (has comparison principle). It emerges only when both features — fourth-order and degenerate — are present simultaneously. The mobility exponent n mediates this emergent tension, serving as the architectural resolution parameter.

### 7.4 Composite Verdicts

**For n >= 1 (physical regime):**

The Thin-Film Equation in the physical regime is a structurally sound, fully local, unconditionally deterministic, anomaly-free, fourth-order degenerate gradient-flow architecture that achieves complete envelope closure through the cooperative action of fourth-order smoothing, degenerate mobility, mass conservation, and gradient-flow monotonicity — the most structurally complex member of the gradient-flow hierarchy that remains fully self-consistent.

**For 0 < n < 1 (weak-degeneracy regime):**

The Thin-Film Equation in the weak-degeneracy regime is a locally well-posed, generatively complete, but positivity-compromised architecture whose single open face — the parametric positivity anomaly at n < 1 — represents the structural cost of combining fourth-order smoothing with insufficient degeneracy, producing the only parameter-dependent self-consistency question in the PDE Atlas.

---

*End of AD Criteria and Verdict. This completes the AD architectural evaluation of the Thin-Film Equation.*
