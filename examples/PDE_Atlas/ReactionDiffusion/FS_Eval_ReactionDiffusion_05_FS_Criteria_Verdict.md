# AD Evaluation: Reaction–Diffusion Systems — AD Criteria and Verdict

Allen Proxmire

April 2026

---

## Overview

This file applies the six AD evaluation criteria to the Reaction–Diffusion architecture as characterized in Modes 1–3. The RD evaluation is fundamentally different from all previous evaluations (NS, CH, AC) because RD is a *class of architectures*, not a single architecture. The FS criteria must therefore be evaluated at two levels: the *class level* (properties shared by all RD systems) and the *instance level* (properties that depend on the constitutive choices RD-8). The verdicts reflect this duality.

---

## 1. Minimality

**Question:** Do the RD axioms form a minimal architectural set?

### 1.1 Structural vs. Constitutive Axioms

The RD axioms divide cleanly into two groups:

**Structural axioms (define the class):**
- RD-1 (Continuum): Necessary for the PDE framework.
- RD-2 (Locality): Defines the differential-operator paradigm.
- RD-3 (Diffusion structure): Specifies second-order elliptic smoothing.
- RD-7 (Time orientation): Forward parabolicity.

These four axioms define *what it means to be an RD system*. None is derivable from the others. Removing any one produces a different architectural class (integral equations without RD-2, hyperbolic systems without RD-7, higher-order PDEs without the second-order restriction in RD-3).

**Constitutive axioms (select an instance):**
- RD-4 (Reaction terms): The specific kinetics **R**(**u**).
- RD-5 (Euclidean geometry): Flat-space Laplacian.
- RD-6 (Boundary conditions): Specific choice of Dirichlet/Neumann/periodic.
- RD-8 (Constitutive choices): All specific parameters (D_i, rate constants, n).

These four axioms select a particular member of the RD class. They are *non-minimal* in the sense that different choices produce different systems, and the class-level architecture does not prefer any specific choice.

### 1.2 RD as a Class, Not a Single Architecture

The minimality question for RD differs from that for AC, CH, or NS because RD is a *parametric family*. For a single system (like AC), minimality asks: "are there redundant axioms?" For a class, minimality asks two questions:

**(a) Are the structural axioms minimal?** Yes. The four structural axioms (RD-1, RD-2, RD-3, RD-7) are independent and irreducible. They define the RD class with no redundancy.

**(b) Are the constitutive axioms minimal?** No — by design. The constitutive axioms (RD-4, RD-5, RD-6, RD-8) are *parameters*, not structural commitments. Different parameter choices produce different systems. The class intentionally carries constitutive freedom as a design feature, not as a defect.

### 1.3 Comparison with Previous Evaluations

| Architecture | Structural axioms | Constitutive axioms | Redundant | Minimality verdict |
|-------------|-------------------|--------------------|-----------|--------------------|
| AC          | 4 (AC-1,2,3,4)   | 3 (AC-5,7,8) + 1 redundant (AC-6) | 1 | FAIL |
| CH          | 4 (CH-1,2,3,4)   | 3 (CH-5,7,8) + 1 redundant (CH-6) | 1 | FAIL |
| NS          | 5 (NS-1,2,5,7,8*)| 3 (NS-3,6,8)      | 0         | FAIL               |
| **RD**      | **4 (RD-1,2,3,7)**| **4 (RD-4,5,6,8)**| **0**     | **See below**       |

*NS-8 (Euclidean) is structural for NS but constitutive for RD — the distinction depends on whether the architecture is a class or a single system.

### 1.4 Verdict

**Criterion 1 Verdict: CONDITIONAL.** The structural core of the RD class (RD-1, RD-2, RD-3, RD-7) is *minimal* — four independent, irreducible axioms with no redundancy. The constitutive axioms (RD-4, RD-5, RD-6, RD-8) are non-minimal by design — they parameterize the class rather than defining it. The verdict is CONDITIONAL because the class-level architecture passes minimality while every specific instance fails it (each instance carries constitutive selections).

---

## 2. Locality

**Question:** Is the RD architecture fully local?

### 2.1 Assessment

Every channel of the RD architecture is local:

- **D (Diffusion):** **D** Delta **u** involves second-order spatial derivatives at each point. Local.
- **R (Reaction):** R_i(**u**) depends on **u** at each point — no derivatives, no integrals. Local.
- **C (Coupling):** Cross-diffusion and cross-reaction are both local operators.
- **M (Rate scales):** Parameters, not spatial operators.

There is no elliptic constraint, no Poisson equation, no Green's function, no integral kernel, and no Lagrange multiplier in any RD system. The architecture is *fully local* at both the formulation level (the PDE is written in local differential form) and the solution level (no nonlocal solve is required to advance the solution).

### 2.2 Comparison

**RD vs. NS:** NS has the nonlocal pressure channel (Poisson equation coupling all points instantaneously). RD has no analogue — there is no incompressibility constraint and no pressure field.

**RD vs. CH:** Both are fully local. CH's fourth-order structure introduces higher derivatives but remains differential (local). The locality class is the same.

**RD vs. AC:** Both are fully local. The same locality class.

**RD vs. ED:** Both are fully local. ED's primitives depend only on each integer's factorization; RD's channels depend only on **u** and its derivatives at each point.

### 2.3 Verdict

**Criterion 2 Verdict: PASS.** The RD architecture is fully local at both formulation and solution levels, for all species counts, all reaction kinetics, and all diffusion structures. Full locality is an *unconditional class-level property* — it does not depend on the constitutive choices. RD achieves the same locality class as ED, AC, and CH, and stronger locality than NS.

---

## 3. Determinism

**Question:** Does the RD architecture uniquely determine the future from the initial data?

### 3.1 Constitutive Dependence of Determinism

Determinism in the RD class is *constitutive-dependent*: it holds for some choices of kinetics and fails for others.

**Sub-class A: Scalar RD with bounded kinetics (AC-type)**

- **Well-posedness:** Unconditionally globally well-posed in all d <= 3.
- **Mechanism:** Maximum principle provides L^{infinity} control; bounded reaction + parabolic regularity gives smoothness.
- **Determinism:** Full (existence, uniqueness, continuous dependence, smoothness).

**Sub-class B: Multi-species RD with bounded kinetics**

- **Well-posedness:** Global existence typically holds (under dissipativity conditions ensuring solutions remain bounded). Uniqueness holds for smooth solutions.
- **Complications:** The absence of the maximum principle (for n >= 2) means that boundedness of solutions must be established by other means (invariant regions, energy estimates, quasi-positivity). For some kinetics, global existence is open.
- **Determinism:** Conditional — holds under structural conditions on **R** and **D** (invariant region, dissipativity) but not unconditionally.

**Sub-class C: Super-linear kinetics (R ~ u^p, p > 1)**

- **Well-posedness:** Finite-time blowup occurs for p <= 1 + 2/d (all positive data) and for large data when p > 1 + 2/d.
- **Determinism:** *Fails.* Solutions cease to exist in finite time. The architecture does not determine the future beyond T*.

### 3.2 Class-Level vs. Instance-Level

At the *class level*, the RD architecture does not guarantee determinism — the class contains instances (super-linear kinetics) where solutions blow up. At the *instance level*, determinism holds for many specific kinetics (bounded, dissipative, quasi-positive) and fails for others (super-linear, non-dissipative).

### 3.3 Comparison

| Architecture | Determinism (2D) | Determinism (3D)  | Determinism (class) |
|-------------|------------------|-------------------|---------------------|
| AC          | PASS             | PASS              | N/A (single system) |
| CH          | PASS             | PASS              | N/A (single system) |
| NS          | PASS             | FAIL (open)       | N/A (single system) |
| **RD**      | **Constitutive** | **Constitutive**  | **CONDITIONAL**     |

### 3.4 Verdict

**Criterion 3 Verdict: CONDITIONAL.** Determinism is constitutive-dependent. The RD class contains sub-classes with unconditional global well-posedness (scalar, bounded kinetics), sub-classes with conditional well-posedness (multi-species, bounded), and sub-classes where blowup occurs (super-linear). No single determinism verdict applies to the entire class. The class-level architecture does not guarantee determinism — it *permits* it for appropriate constitutive choices and *permits blowup* for others.

---

## 4. Generative Sufficiency

**Question:** Does the RD architecture generate all of its observed laws and phenomena from the axioms?

### 4.1 Generated Phenomena

The RD class generates the *broadest range of spatiotemporal phenomena* of any PDE architecture in the PDE Atlas:

| Phenomenon                      | Generated from axioms? | Derivation method                    |
|---------------------------------|------------------------|--------------------------------------|
| Parabolic smoothing             | Yes                    | Linear heat equation theory          |
| Traveling fronts                | Yes                    | Phase-plane analysis of traveling-wave ODE |
| Wave-speed selection            | Yes                    | Variational / equal-area rule        |
| Fisher–KPP minimum speed        | Yes                    | Linearization at leading edge        |
| Turing instability              | Yes                    | Linear stability of homogeneous state|
| Turing pattern wavelength       | Yes                    | Maximization of dispersion relation  |
| Hopf bifurcation / oscillations | Yes                    | Eigenvalue analysis of Jacobian      |
| Excitability and pulses         | Yes                    | Singular perturbation theory (FHN)   |
| Spiral waves                    | Yes (existence)        | Topological arguments + numerical    |
| Spatiotemporal chaos            | Yes (existence)        | Instability of periodic solutions    |
| Fujita blowup threshold         | Yes                    | Comparison principles + scaling      |
| Invariant regions               | Yes                    | Maximum principle generalizations    |
| Global attractor (bounded case) | Yes                    | Absorbing ball + compactness         |

### 4.2 Non-Generated Features

| Feature                                | Status                                           |
|----------------------------------------|--------------------------------------------------|
| Exact spiral wave frequency            | Not rigorously derived for generic kinetics. Known only for specific models and in asymptotic limits. |
| Spatiotemporal chaos statistics         | Not derivable. Statistical properties of chaotic RD solutions (Lyapunov spectra, fractal dimensions, correlation lengths) require numerical computation and statistical mechanics, not PDE analysis alone. |
| Pattern selection among multiple Turing modes | Weakly nonlinear analysis (amplitude equations) selects among competing patterns (spots vs. stripes), but the selection depends on higher-order nonlinear terms that vary across the class. |
| Noise-driven pattern formation          | Stochastic RD (with additive or multiplicative noise) produces phenomena not accessible to the deterministic architecture. |
| Detailed blowup profiles                | Self-similar and non-self-similar blowup profiles are known for specific kinetics (u^p) but not for generic super-linear reactions. |

### 4.3 Assessment

The RD class is the *most generatively sufficient* PDE architecture in the PDE Atlas. It generates:

- Everything AC generates (fronts, phase selection, metastability) — because AC is a sub-class.
- Everything beyond AC that scalar RD generates (excitability, propagation failure, pulled/pushed fronts).
- Everything beyond scalar RD that multi-species RD generates (Turing patterns, oscillations, spirals, chaos).

No other PDE architecture in the Atlas generates Turing patterns, spiral waves, excitable pulses, or spatiotemporal chaos. These phenomena are *unique to the RD class* — they require the combination of local reaction + diffusion + multi-species coupling that only RD provides.

The generative gap (exact spiral frequencies, chaos statistics, noise-driven patterns) is narrow and technical — comparable to the AC/CH gap (exact coarsening exponents) and narrower than the NS gap (entire statistical theory of turbulence).

### 4.4 Verdict

**Criterion 4 Verdict: PASS.** The RD class is the most generatively sufficient PDE architecture in the PDE Atlas. It generates all qualitative spatiotemporal phenomena (patterns, waves, pulses, spirals, chaos, blowup) from the axioms. The generative gap is narrow and technical, confined to quantitative details (exact frequencies, statistical exponents) rather than qualitative phenomena. This is the strongest generative sufficiency verdict of any PDE in the Atlas — RD generates phenomena that no other architecture can access.

---

## 5. Envelope Tightness

**Question:** Is the RD envelope closed and tight?

### 5.1 Class-Level Envelope

The class-level RD envelope (properties shared by all RD systems) consists of the Tier 1 constraints from Mode 1:

- E1: Parabolic smoothing. Tight (sharp estimates known).
- E2: Reaction-diffusion balance (L_RD). Tight (exact scaling).
- E3: Diffusion dominance at high k. Tight.
- E4: Reaction dominance at k = 0. Tight.

These four bounds are *tight and unconditional*. They hold for all RD systems and cannot be improved.

### 5.2 Instance-Level Envelope

The instance-level envelope depends on the constitutive choices:

- **Region A (scalar, bounded):** Fully closed and tight. All bounds from the AC evaluation apply.
- **Region B (multi-species, oscillatory):** *Open.* The oscillatory face, Turing face, and spiral/chaos face are all open — the dynamics can access these behaviors without bound. There is no single closed envelope for this sub-class.
- **Region C (super-linear):** *Open.* The blowup face is open — solutions can escape to infinity.

### 5.3 Why RD Cannot Have a Single Closed Envelope

The RD class cannot have a single closed envelope because it contains sub-classes with *qualitatively incompatible* behaviors:

1. Sub-class A (AC-type) requires a *closed, monotone* envelope (all trajectories converge).
2. Sub-class B (oscillatory) requires an *open, non-monotone* envelope (trajectories can oscillate forever).
3. Sub-class C (blowup) requires an *open, unbounded* envelope (trajectories can escape to infinity).

No single envelope can simultaneously be closed (for A), permit oscillations (for B), and permit blowup (for C). The class-level envelope must therefore be *the intersection* of all instance-level envelopes — which is just the Tier 1 bounds (E1–E4). This intersection is tight but *incomplete*: it captures only the universal properties and says nothing about the rich constitutive-dependent behaviors.

### 5.4 Verdict

**Criterion 5 Verdict: CONDITIONAL.** The class-level envelope (Tier 1: E1–E4) is tight. The instance-level envelope is constitutive-dependent: fully closed for Region A, open with multiple faces for Region B, and open with a blowup face for Region C. No single closed envelope characterizes the entire class. The verdict is CONDITIONAL because the architecture achieves tightness at the class level but cannot achieve closure at the instance level for all members.

---

## 6. Structural Optimality

**Question:** Is the RD architecture optimal — free of anomalies and unnecessary complexity?

### 6.1 Anomaly Assessment

The RD class has *no architectural anomalies* in the FS sense. An anomaly is a structural feature that is both necessary (forced by the axioms) and potentially destructive (threatening self-consistency). The RD class has:

- **No nonlocal channel.** All channels are local. (Contrast: NS has the nonlocal pressure anomaly.)
- **No architectural blowup channel.** Blowup in RD is *constitutive* (depends on the kinetics), not *architectural* (present for all instances). One can close the blowup face by choosing bounded kinetics. (Contrast: NS has an architectural blowup channel in 3D that cannot be removed without changing the axioms.)
- **No dimensional bifurcation.** The RD architecture does not split qualitatively between 2D and 3D (for the same kinetics). (Contrast: NS splits at d = 2 vs. d = 3.)

The three missing walls (no maximum principle for n >= 2, no Lyapunov, no conservation) are *not anomalies* — they are *intentional absences*. The RD class omits these walls *by design*, to permit the oscillatory, pattern-forming, and chaotic dynamics that are the class's raison d'être. An architecture that forced a Lyapunov functional on all members would exclude oscillations; one that forced a maximum principle would exclude multi-species coupling; one that forced conservation would exclude source/sink dynamics. The missing walls are the *price of universality*, not defects.

### 6.2 Structural Looseness as a Design Feature

The RD class is *structurally loose by design*. Its looseness — the multiplicity of open faces, the constitutive dependence of closure, the absence of Lyapunov/conservation/maximum-principle walls — is not a failure of structural optimality but a *necessary consequence of universality*. The class must be loose enough to contain:

- Gradient-flow systems (AC-type): closed, monotone, convergent.
- Oscillatory systems (FHN, Brusselator): open, non-monotone, non-convergent.
- Pattern-forming systems (Turing): spatially structured steady states.
- Chaotic systems (spiral breakup): aperiodic, sensitive-dependent dynamics.
- Blowup systems (Fujita): finite-time singularity formation.

No single structural constraint can accommodate all five classes. The RD architecture achieves universality by imposing only the minimal structural axioms (locality, parabolicity, diffusion + reaction) and leaving everything else to the constitutive parameters.

### 6.3 Comparison

| Feature                      | AC           | CH            | NS              | RD               |
|------------------------------|-------------|---------------|-----------------|------------------|
| Anomalies                    | None        | None          | 2 (architectural)| None (all constitutive) |
| Missing walls                | 0           | 1 (max. princ.)| 0              | 3 (by design)    |
| Open faces                   | 0           | 0             | 1 (architectural)| 3+ (constitutive)|
| Structural economy           | Highest     | High          | Moderate        | Minimal (class)  |
| Universality                 | Narrow      | Narrow        | Moderate        | Broadest         |

### 6.4 Verdict

**Criterion 6 Verdict: CONDITIONAL.** The RD class has no *architectural* anomalies — every open face and every missing wall is constitutive, not structural. The architecture is anomaly-free at the class level. However, specific instances can have open faces (oscillatory, Turing, blowup) that prevent envelope closure. The verdict is CONDITIONAL because the class is structurally clean (no anomalies) but constitutively loose (some instances have open faces). The looseness is by design — it is the architectural price of universality.

---

## 7. FS Verdict Summary

### 7.1 Criteria Scorecard

| Criterion                  | Verdict         | Comment                                                     |
|----------------------------|-----------------|-------------------------------------------------------------|
| **1. Minimality**          | CONDITIONAL     | Structural core minimal; constitutive axioms parameterize class |
| **2. Locality**            | **PASS**        | Fully local, all channels, all instances                     |
| **3. Determinism**         | CONDITIONAL     | Constitutive-dependent: holds for bounded kinetics, fails for u^p |
| **4. Gen. Sufficiency**    | **PASS**        | Most generatively sufficient PDE in the Atlas                |
| **5. Envelope Tightness**  | CONDITIONAL     | Class-level tight; instance-level constitutive-dependent     |
| **6. Structural Optimality** | CONDITIONAL   | No architectural anomalies; constitutive looseness by design |

### 7.2 Comparison Across the PDE Atlas

| Criterion             | ED     | AC             | CH             | NS (2D)   | NS (3D)      | RD              |
|-----------------------|--------|----------------|----------------|-----------|---------------|-----------------|
| Minimality            | PASS   | FAIL           | FAIL           | FAIL      | FAIL          | CONDITIONAL     |
| Locality              | PASS   | PASS           | PASS           | COND.     | COND.         | **PASS**        |
| Determinism           | PASS   | PASS           | PASS           | PASS      | FAIL          | CONDITIONAL     |
| Gen. Sufficiency      | PASS   | COND. (weak)   | COND. (weak)   | COND.     | COND.         | **PASS**        |
| Envelope Tightness    | PASS   | PASS           | PASS           | PASS      | COND.         | CONDITIONAL     |
| Structural Optimality | PASS   | COND.          | COND.          | FAIL      | FAIL          | CONDITIONAL     |

### 7.3 Architectural Summary

The Reaction–Diffusion class occupies a unique position in the PDE Atlas: it is the *broadest PDE architecture evaluated*, the *most generatively sufficient*, and the *only class-level evaluation* (all others evaluate specific systems). Its FS profile — two unconditional PASSes (Locality, Generative Sufficiency) and four CONDITIONALs — reflects its dual nature: universally strong on the properties guaranteed by the structural core (locality, generative breadth), and constitutive-dependent on the properties that vary across the class (determinism, closure, optimality).

The RD class achieves the *highest generative sufficiency* of any architecture in the Atlas. It generates Turing patterns, traveling waves, pulses, spiral waves, excitability, and spatiotemporal chaos — phenomena that no other evaluated architecture can produce. This generative breadth is achieved by *omitting* the structural constraints (Lyapunov functional, conservation law, maximum principle) that confine AC and CH to monotone, convergent dynamics. The omission is deliberate: the RD class is designed to be the universal container for spatially extended nonlinear dynamics, and universality requires structural looseness.

The RD class has *no architectural anomalies*. Every open face (oscillatory, Turing, blowup) and every missing wall (no Lyapunov, no maximum principle, no conservation) is constitutive — it can be opened or closed by choosing appropriate kinetics. This is qualitatively different from NS, where the 3D enstrophy gap and the nonlocal pressure channel are *architectural* anomalies present in every NS solution regardless of constitutive choices. The RD class is structurally clean at the class level; NS is structurally compromised at the architectural level.

The trade-off between the RD class and the gradient-flow architectures (AC, CH) is the fundamental tension of the PDE Atlas: *structural tightness vs. generative breadth*. AC and CH achieve tight, closed, anomaly-free architectures by restricting their dynamics to monotone energy descent. RD achieves maximal generative breadth by removing these restrictions. Neither approach dominates the other — they represent complementary architectural strategies.

### 7.4 Composite Verdict

The Reaction–Diffusion class is the universal second-order parabolic architecture — structurally clean at the class level, constitutively open at the instance level, and the most generatively sufficient PDE framework in the PDE Atlas, achieving its unmatched breadth of spatiotemporal phenomena through the deliberate omission of the structural walls that confine gradient-flow architectures to monotone descent.

---

*End of AD Criteria and Verdict. This completes the AD architectural evaluation of the Reaction–Diffusion class.*
