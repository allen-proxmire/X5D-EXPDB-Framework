# AD Evaluation: Inviscid Burgers Equation — AD Criteria and Verdict

Allen Proxmire

April 2026

---

## Overview

This file applies the six AD evaluation criteria to the Inviscid Burgers equation as characterized in Modes 1–3. The Burgers evaluation completes the *hyperbolic pair* of the PDE Atlas: HJ (the potential formulation) and Burgers (the conservation-law formulation) are one derivative apart, share the same singularity time, the same comparison principle, and the same parameter-free character — but Burgers adds the conservation-law structure (L^1 contraction, Rankine–Hugoniot, shock-concentrated dissipation, mass conservation, total variation decay) that HJ lacks. The Burgers verdicts test whether this conservation-law enrichment changes the FS profile relative to HJ.

Throughout, we reference the axioms BA-1 through BA-8, the envelope inequalities E1–E10, the universal inequalities U1–U10, and the channel constraints C1–C12 established in the preceding files.

---

## 1. Minimality

**Question:** Do the Burgers axioms form a minimal architectural set?

### 1.1 Assessment of Individual Axioms

**BA-1 (Scalar Velocity).** *Minimal within paradigm.* The scalar velocity field v is the state variable — directly physical (unlike HJ's auxiliary potential). Removing it eliminates the PDE framework. **Minimal within paradigm.**

**BA-2 (Locality).** *Minimal.* Defines the PDE paradigm. Independent of all other axioms. **Minimal.**

**BA-3 (First-Order Nonlinear Conservation Law).** *Minimal.* The law partial_t v + partial_x(v^2/2) = 0 is the defining equation — simultaneously a conservation law and a self-advection equation. It is the simplest nonlinear conservation law (scalar, one spatial dimension, quadratic flux). Removing or replacing it changes the architecture entirely. **Minimal — this axiom *is* the architecture.**

**BA-4 (Convex Flux).** *Minimal for the standard theory.* The strict convexity f''(v) = 1 > 0 is the structural requirement for comparison, L^1 contraction, entropy uniqueness, Oleinik bound, and Rankine–Hugoniot. Without convexity, the entropy-solution theory weakens (possible non-uniqueness, compound waves). Convexity is a *structural condition*, not a constitutive parameter — f(v) = v^2/2 is the unique simplest strictly convex flux. **Minimal — required for closure.**

**BA-5 (Hyperbolic Orientation).** *Derived.* The hyperbolic character (characteristics, finite speed) follows from BA-3 (first-order conservation law). First-order conservation laws are automatically hyperbolic. **Redundant (derived from BA-3).**

**BA-6 (No Diffusion).** *Minimal.* The absence of viscosity is the deliberate structural commitment that makes Burgers hyperbolic rather than parabolic. Adding nu partial_{xx} v gives the viscous Burgers equation — exactly solvable via Cole–Hopf but globally smooth and shock-free, a qualitatively different architecture. **Minimal.**

**BA-7 (No Reaction).** *Minimal.* The absence of source/sink terms makes the equation a pure conservation law with conserved mass. Adding reaction breaks mass conservation. **Minimal.**

**BA-8 (Entropy-Solution Framework).** *Minimal for global well-posedness.* The Kruzkov entropy framework is structurally required for unique global solutions past shock formation. Without it, weak solutions are non-unique and the architecture is ill-posed. **Minimal — required for global well-posedness.**

### 1.2 Minimality Summary

| Axiom | Content                        | Minimal?    | Comment                              |
|-------|--------------------------------|-------------|--------------------------------------|
| BA-1  | Scalar velocity                | Within paradigm | Directly physical state variable |
| BA-2  | Locality                       | Yes         | Defines PDE paradigm                 |
| BA-3  | Conservation law               | Yes         | *Is* the architecture                |
| BA-4  | Convex flux                    | Yes         | Required for closure                 |
| BA-5  | Hyperbolic orientation         | Redundant   | Derived from BA-3                    |
| BA-6  | No diffusion                   | Yes         | Isolates pure transport              |
| BA-7  | No reaction                    | Yes         | Preserves conservation               |
| BA-8  | Entropy-solution framework     | Yes         | Required for global well-posedness   |

**Structural core:** Six minimal axioms (BA-1 paradigm, BA-2, BA-3, BA-4, BA-6, BA-7, BA-8 — counting BA-1 as paradigm-level gives six independent structural axioms). Zero non-minimal axioms (no geometric simplification needed — Burgers is intrinsically one-dimensional or trivially extends to multi-d). One redundant axiom (BA-5, derived from BA-3).

**Criterion 1 Verdict: CONDITIONAL.** The structural core is fully minimal — six independent axioms with zero constitutive parameters, zero non-minimal elements, and one redundant axiom. The CONDITIONAL (rather than PASS) is a *technical classification*: the AD framework classifies all PDEs with redundant axioms as CONDITIONAL on Minimality, even when the redundancy is harmless. The Burgers minimality is *substantively* the strongest in the Atlas: zero constitutive parameters (tied with HJ and MCF), zero non-minimal axioms (unique — every other architecture has at least one geometric simplification), and one harmless redundancy.

If the FS Minimality criterion counted only *independent* axioms and ignored harmless redundancies, Burgers would receive PASS — making it the *only PDE in the Atlas* to pass Minimality outright (even ED passes trivially as a static structure). The CONDITIONAL is a consequence of the criterion's formal structure, not a genuine structural weakness.

---

## 2. Locality

**Question:** Is the Burgers architecture fully local?

### 2.1 Assessment

The Burgers equation v_t + v v_x = 0 depends on v and v_x at each point. No nonlocal operators, no integral constraints, no pressure equation, no Green's function.

- **T (Transport):** v v_x is local (pointwise product of v and its derivative).
- **S (Steepening):** Shock formation is locally triggered (characteristics converge locally).
- **V (Entropy):** Entropy condition is locally defined (entropy inequalities at each point).

The architecture is fully local at the formulation level. Additionally, the *finite-speed propagation* (characteristics at speed v, bounded for bounded data) ensures that information travels at finite speed — a *stronger* locality than parabolic architectures (which have infinite propagation speed for non-degenerate diffusion).

### 2.2 Comparison

Burgers shares the locality class of HJ, AC, CH, PME, TFE, FP, MCF, and RD — all fully local. Only NS has a nonlocal channel (pressure). Burgers' finite-speed propagation gives it *stronger effective locality* than any parabolic architecture.

**Criterion 2 Verdict: PASS.** Fully local at formulation level. Finite-speed propagation (stronger than parabolic locality). No nonlocal channel.

---

## 3. Determinism

**Question:** Does the Burgers architecture uniquely determine the future from the initial data?

### 3.1 Assessment

The Kruzkov entropy-solution theory provides *unconditional global determinism*:

- **Existence:** For any bounded measurable initial data v_0, an entropy solution exists for all t >= 0. The existence is constructive: the vanishing-viscosity limit v = lim_{nu → 0} v^nu provides the solution explicitly.

- **Uniqueness:** For convex flux, the entropy solution is unique. Uniqueness follows from the *L^1 contraction* (Kruzkov's theorem): if two entropy solutions start with the same data, their L^1 distance is zero for all time.

- **Continuous dependence:** The L^1 contraction ||v_1(t) - v_2(t)||_{L^1} <= ||v_{1,0} - v_{2,0}||_{L^1} provides Lipschitz continuous dependence in L^1. The L^{infinity} contraction provides the same in L^{infinity}. Continuous dependence in *two* norms simultaneously — the strongest stability in the Atlas.

- **Regularity:** The entropy solution is BV (bounded variation) — v is bounded, has bounded total variation, and has at most countably many jump discontinuities. The solution is *not* C^1 in general (shocks are genuine discontinuities), but it is BV, which is the natural regularity class for conservation laws.

### 3.2 The Role of Shock Formation

Shock formation does *not* break determinism:

- **Before T*:** Classical (smooth) solution exists and is unique.
- **At T*:** v develops a discontinuity. The classical PDE is no longer defined at the shock.
- **After T*:** The entropy solution exists, is unique, and is stable. Determinism is uninterrupted.

The shock is a *regularity event* (loss of differentiability), not a *well-posedness event* (loss of existence or uniqueness). The solution is uniquely determined for all time in the BV class.

**Comparison:**

| Architecture | Singularity        | Determinism Past Singularity           |
|-------------|--------------------|-----------------------------------------|
| NS (3D)    | Open               | Open (weak solutions not known unique)  |
| MCF         | Certain (curvature)| Conditional (surgery/level-set unique)  |
| HJ          | Certain (gradient) | Unconditional (viscosity unique)        |
| **Burgers** | **Certain (shock)**| **Unconditional (entropy unique, L^1 contraction)** |

Burgers has the *strongest determinism among architectures with singularities*: the singularity is certain, the continuation is unconditionally unique, and the stability is in *two norms* (L^1 and L^{infinity}).

### 3.3 Verdict

**Criterion 3 Verdict: PASS.** Unconditional global determinism — existence, uniqueness, and continuous dependence (in L^1 and L^{infinity}) for all bounded initial data, for all time, including through shocks. The strongest determinism of any architecture with singularities.

---

## 4. Generative Sufficiency

**Question:** Does Burgers generate all of its observed phenomena from the axioms?

### 4.1 Generated Phenomena

| Phenomenon                              | Derivation Method                            |
|-----------------------------------------|----------------------------------------------|
| Finite-time shock formation             | Characteristic crossing (explicit T*)        |
| Rankine–Hugoniot shock speed            | Conservation form + jump condition            |
| Entropy-solution continuation           | Kruzkov theory (comparison + L^1 contraction)|
| L^1 contraction                         | Kruzkov's theorem                             |
| L^{infinity} contraction                | Comparison principle                          |
| Oleinik one-sided gradient bound (1/t)  | Entropy condition + characteristics           |
| Total variation decay                   | BV theory for conservation laws               |
| Mass conservation                       | Conservation form + divergence theorem        |
| Energy dissipation at shocks            | Entropy condition + Rankine–Hugoniot          |
| N-wave asymptotic profile               | Self-similar reduction + matching             |
| Shock interaction and merging           | Riemann problem + wave interaction theory     |
| Rarefaction waves                       | Riemann problem for v_L < v_R                 |
| Cole–Hopf exact solution (viscous case) | Linearization via exponential transform       |
| Vanishing-viscosity convergence         | Compensated compactness / BV estimates        |

The Burgers architecture generates *all* of its characteristic phenomena from the axioms. The theory of scalar conservation laws with convex flux is *one of the most complete theories in PDE mathematics* — every question about the qualitative and quantitative behavior of entropy solutions has been answered.

### 4.2 Phenomena Burgers Cannot Generate

| Phenomenon              | Reason for Absence                        |
|------------------------|-------------------------------------------|
| Smoothing              | No diffusion (BA-6)                       |
| Oscillations           | L^1 contraction forbids them              |
| Patterns               | No reaction, single species               |
| Chaos                  | Double contraction (L^1 + L^{infinity})   |
| Phase separation       | No double-well                             |
| Turbulence             | No vector field, no pressure               |
| Free boundaries        | Non-degenerate transport                   |
| Geometry               | No surface state variable                  |

### 4.3 Assessment

Burgers is *completely generatively sufficient within its scope*. The theory of entropy solutions for scalar conservation laws with convex flux is provably complete — every phenomenon is rigorously derived, every estimate is sharp, and every structural question is resolved. The generative gap is *zero*.

**Criterion 4 Verdict: PASS.** Zero generative gap. Complete theory. Every phenomenon rigorously derived from the axioms. The scalar conservation-law theory is one of the most complete in all of PDE mathematics.

---

## 5. Envelope Tightness

**Question:** Is the Burgers envelope closed and tight?

### 5.1 Assessment of Envelope Components

**E1 (L^1 contraction).** Exact: ||v_1 - v_2||_{L^1} non-increasing. Sharp (equality for non-interacting solutions). **Tight.**

**E2 (L^{infinity} contraction).** Exact: ||v_1 - v_2||_{L^inf} non-increasing. Sharp. **Tight.**

**E3 (Finite-speed propagation).** Sharp: cone opening = ||v_0||_{L^inf}. Achieved by characteristics. **Tight.**

**E4 (Oleinik bound).** Sharp: v_x <= 1/t is achieved by specific solutions (e.g., v_0(x) = -|x|). Universal. **Tight.**

**E5 (Rankine–Hugoniot).** Exact: s = (v_L + v_R)/2. Not an approximation. **Tight.**

**E6 (Entropy admissibility).** Exact characterization of the unique entropy solution. **Tight.**

**E7 (Shock-formation time).** Sharp: T* = -1/min(v_0') achieved by data with the specified slope. **Tight.**

**E8 (Total variation decay).** Sharp: TV non-increasing, with strict decrease at shock merging events. **Tight.**

**E9 (Vanishing-viscosity stability).** Exact: v = lim_{nu→0} v^nu uniformly. **Tight.**

**E10 (Mass conservation + energy dissipation).** Mass: exact conservation. Energy: exact dissipation rate at each shock. **Tight.**

### 5.2 Closure

The Burgers envelope is *fully closed* within the entropy-solution framework, sealed by four mechanisms:

1. **Convex flux:** Provides the comparison principle (uniqueness foundation).
2. **Entropy admissibility:** Selects the unique physical weak solution.
3. **L^1 contraction:** Provides the strongest stability (Kruzkov).
4. **Rankine–Hugoniot:** Provides exact shock propagation (no ambiguity at discontinuities).

The required shock face is *resolved* by the entropy framework: shocks form, propagate, and merge — all under complete analytical control. The shock face is structural, not anomalous.

### 5.3 Verdict

**Criterion 5 Verdict: PASS.** All ten envelope components are tight. The envelope is fully closed. The shock face is required and resolved. The closure is achieved through entropy + L^1 contraction — the conservation-law closure mode, unique to Burgers in the Atlas.

---

## 6. Structural Optimality

**Question:** Is the Burgers architecture optimal?

### 6.1 Anomaly Assessment

Burgers has *zero* structural anomalies:

- **No nonlocal channel.** All channels local. Finite-speed propagation.
- **No destabilizing sub-channel (anomalous sense).** The steepening channel S is destabilizing but *self-limiting* (shocks reduce total variation) and *fully resolved* (entropy solutions provide unique continuation).
- **No oscillatory face.** L^1 contraction → monotone dynamics.
- **No chaotic face.** Double contraction (L^1 + L^{infinity}) → maximally anti-chaotic.
- **No amplitude blowup.** v remains bounded: ||v(t)||_{L^inf} <= ||v_0||_{L^inf}.
- **No unresolved singularity.** Shock formation is certain and completely controlled by the entropy framework.

### 6.2 Structural Economy

Burgers achieves closure with *maximum structural economy*:

- **Zero constitutive parameters** (tied with HJ and MCF — the three parameter-free architectures).
- **Three channels** (tied with HJ and MCF for fewest).
- **Zero non-minimal axioms** (unique in the Atlas — every other architecture has at least one geometric simplification or constitutive selection).
- **One equation:** partial_t v + partial_x(v^2/2) = 0 (the shortest conservation-law specification possible).
- **Double contraction:** L^1 + L^{infinity} simultaneously (unique in the Atlas).

No simpler conservation law can produce the Burgers phenomenology. The linear transport equation partial_t v + c partial_x v = 0 is simpler but has no shock formation (it is linear). The Burgers equation is the *minimal nonlinear scalar conservation law* — the simplest PDE that produces shocks from smooth data within a conservation-law framework.

### 6.3 Comparison with HJ

Burgers and HJ have *identical* FS profiles on five of six criteria. The structural difference:

| Feature                  | Burgers                       | HJ                          |
|--------------------------|-------------------------------|-----------------------------|
| Conservation law         | **Yes**                       | No                          |
| L^1 contraction          | **Yes** (Kruzkov)             | No                          |
| Mass conservation        | **Yes**                       | No                          |
| Shock-concentrated dissip.| **Yes**                      | No (zero dissipation)       |
| Rankine–Hugoniot         | **Yes**                       | No                          |
| Total variation decay    | **Yes**                       | No                          |
| Closure mode             | Entropic-contractive          | Variational                 |

Burgers has *more structural tools* than HJ — all arising from the conservation-law form. Both achieve the same AD score, but Burgers achieves it with a *richer* structural toolkit. The conservation-law form is a *structural enrichment* that adds tools without adding anomalies.

### 6.4 Verdict

**Criterion 6 Verdict: PASS.** Zero anomalies. Maximum structural economy. Zero parameters. Double contraction. Zero non-minimal axioms. The conservation-law enrichment over HJ adds structural tools without adding complexity or anomalies. Burgers is the *most structurally complete* hyperbolic architecture in the Atlas.

---

## 7. FS Verdict Summary

### 7.1 Criteria Scorecard

| Criterion                  | Verdict         | Comment                                              |
|----------------------------|-----------------|------------------------------------------------------|
| **1. Minimality**          | CONDITIONAL     | 6 minimal axioms, 0 non-minimal, 1 redundant (BA-5) |
| **2. Locality**            | **PASS**        | Fully local + finite-speed (strongest locality)      |
| **3. Determinism**         | **PASS**        | Unconditional via entropy solutions (L^1 + L^inf contraction) |
| **4. Gen. Sufficiency**    | **PASS**        | Zero gap. Complete conservation-law theory.           |
| **5. Envelope Tightness**  | **PASS**        | All 10 tight. Entropy + L^1 closure.                |
| **6. Structural Optimality** | **PASS**      | Zero anomalies. Zero parameters. Double contraction. |

**Score: 5 PASS + 1 CONDITIONAL** — tying FP, PME, and HJ for the strongest PDE profile in the Atlas.

### 7.2 Comparison Across the PDE Atlas

| Criterion             | ED   | Burgers    | HJ         | FP         | PME        | MCF        | TFE(n>=1) | AC         | CH         | NS(3D)   | RD        |
|-----------------------|------|------------|------------|------------|------------|------------|-----------|------------|------------|----------|-----------|
| Minimality            | PASS | COND.      | COND.      | COND.      | COND.      | COND.      | COND.     | FAIL       | FAIL       | FAIL     | COND.     |
| Locality              | PASS | **PASS**   | **PASS**   | **PASS**   | **PASS**   | **PASS**   | **PASS**  | **PASS**   | **PASS**   | COND.    | **PASS**  |
| Determinism           | PASS | **PASS**   | **PASS**   | **PASS**   | **PASS**   | COND.      | **PASS**  | **PASS**   | **PASS**   | FAIL     | COND.     |
| Gen. Sufficiency      | PASS | **PASS**   | **PASS**   | **PASS**   | **PASS**   | **PASS**   | **PASS**  | COND.(w)   | COND.(w)   | COND.    | **PASS**  |
| Envelope Tightness    | PASS | **PASS**   | **PASS**   | **PASS**   | **PASS**   | COND.      | **PASS**  | **PASS**   | **PASS**   | COND.    | COND.     |
| Structural Optimality | PASS | **PASS**   | **PASS**   | **PASS**   | **PASS**   | **PASS**   | **PASS**  | COND.      | COND.      | FAIL     | COND.     |
| **Total PASS**        | **6**| **5**      | **5**      | **5**      | **5**      | **3**      | **4**     | **3**      | **3**      | **0**    | **2**     |

### 7.3 The Four 5-PASS Architectures

Four PDEs now achieve the maximum PDE score of 5 PASS + 1 CONDITIONAL:

| Architecture | Closure Mode             | Singularity?     | Character            |
|-------------|--------------------------|------------------|----------------------|
| **FP**      | **Linear**               | None             | Parabolic, drift+diff.|
| **PME**     | **Dissipative**          | None             | Parabolic, degenerate |
| **HJ**      | **Variational**          | Gradient kink    | Hyperbolic, potential |
| **Burgers** | **Entropic-contractive** | Velocity shock   | Hyperbolic, cons. law |

These four architectures represent the *four fundamental closure modes* for PDEs:

1. **Linear closure (FP):** Linearity of the PDE → linear parabolic theory.
2. **Dissipative closure (PME):** Lyapunov + smoothing → energy/entropy estimates.
3. **Variational closure (HJ):** Convexity + viscosity → comparison + Hopf–Lax.
4. **Entropic-contractive closure (Burgers):** Convex flux + Kruzkov → L^1 contraction + Rankine–Hugoniot.

The four closures exhaust the *known fundamental modes of PDE well-posedness*. Every other architecture in the Atlas uses one of these modes (AC/CH/TFE use dissipative; MCF uses dissipative-geometric) or fails to close (NS in 3D). The PDE Atlas's four 5-PASS architectures are the *structural pillars* of PDE theory.

### 7.4 Burgers vs. HJ: The Conservation-Law Addition

Burgers and HJ are *structurally dual* (one derivative apart) and share the same AD score (5 PASS + 1 CONDITIONAL). The structural difference:

- HJ has *variational closure* (Hopf–Lax, L^{infinity} contraction, semiconcavity).
- Burgers has *entropic-contractive closure* (Kruzkov, L^1 + L^{infinity} contraction, Rankine–Hugoniot, TV decay, mass conservation, shock-concentrated dissipation).

Burgers is the *richer* architecture: it has all of HJ's tools plus the conservation-law additions. The conservation-law form is a *free structural enrichment* — it adds tools without adding complexity, parameters, or anomalies. Burgers demonstrates that the conservation-law form is a *pure structural benefit* within the hyperbolic framework.

### 7.5 Architectural Summary

The Inviscid Burgers equation achieves the joint-strongest FS profile of any PDE in the Atlas, tying with FP, PME, and HJ at 5 PASSes + 1 CONDITIONAL. It is the *conservation-law member* of the 5-PASS quartet — the representative of entropic-contractive closure, the architecture with double contraction (L^1 + L^{infinity}), shock-concentrated dissipation, and the full conservation-law toolkit (Rankine–Hugoniot, mass conservation, total variation decay).

Burgers is the *scalar ancestor of the Euler and Navier–Stokes equations* — the reduced core that isolates the nonlinear self-advection mechanism. The fact that Burgers achieves 5 PASSes while NS achieves 0 demonstrates that the difficulty of the NS regularity problem lies *not in self-advection* (which Burgers handles completely) but in the *structural additions* — vectorization, incompressibility, and pressure — that Euler/NS impose on top of the Burgers transport. The Burgers evaluation *localizes the NS open problem*: the problem is in the interaction of transport with pressure and incompressibility, not in the transport itself.

### 7.6 Composite Verdict

The Inviscid Burgers equation is the purest conservation-law architecture in the PDE Atlas — a parameter-free, fully local, entropy-closed nonlinear transport equation whose structural singularities are resolved by convex flux and L^1 contraction, producing the only architecture with simultaneous L^1 and L^{infinity} contraction, shock-concentrated dissipation, and the complete conservation-law toolkit, and standing as the scalar foundation from which the Euler and Navier–Stokes equations are built.

---

*End of AD Criteria and Verdict. This completes the AD architectural evaluation of the Inviscid Burgers Equation.*
