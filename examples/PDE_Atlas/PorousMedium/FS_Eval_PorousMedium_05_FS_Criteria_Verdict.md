# AD Evaluation: Porous Medium Equation — AD Criteria and Verdict

Allen Proxmire

April 2026

---

## Overview

This file applies the six AD evaluation criteria to the Porous Medium Equation as characterized in Modes 1–3. The PME occupies a unique position in the PDE Atlas: it is the *structurally simplest* nontrivial PDE, with the fewest channels, the fewest degrees of freedom, and the most completely characterized long-time behavior. Its AD evaluation reveals whether structural simplicity translates into architectural soundness.

Throughout, we reference the axioms PME-1 through PME-8, the envelope inequalities E1–E10, the universal inequalities U1–U10, and the channel constraints C1–C12 established in the preceding files.

---

## 1. Minimality

**Question:** Do the PME axioms form a minimal architectural set?

### 1.1 Assessment of Individual Axioms

**PME-1 (Continuum Hypothesis).** *Minimal within the PDE paradigm.* Required for the field-theoretic formulation. Cannot be removed without abandoning the PDE framework. **Minimal within paradigm.**

**PME-2 (Locality).** *Minimal.* Defines the PDE paradigm. Independent of all other axioms. **Minimal.**

**PME-3 (Nonlinear Diffusion).** *Minimal.* This is the defining structural commitment of the PME. The degenerate diffusion operator Delta(u^m) is the *only dynamical channel* — removing it eliminates the PDE entirely. The nonlinearity (density-dependent diffusion coefficient) is what separates PME from the linear heat equation and produces all of the architecture's distinctive features (finite-speed propagation, free boundaries, self-similar spreading). **Minimal.** This axiom *is* the architecture.

**PME-4 (Conservation of Mass).** *Minimal.* Conservation is an independent structural commitment that shapes the entire phenomenology. Removing conservation (replacing partial_t u = Delta(u^m) with a non-divergence-form equation) would produce a qualitatively different system. Conservation is not derivable from the other axioms — one can have nonlinear diffusion without conservation (e.g., partial_t u = u^{m-1} Delta u, which is not in divergence form). **Minimal.**

**PME-5 (Euclidean Geometry).** *Non-minimal.* The PME can be formulated on Riemannian manifolds with the Laplace–Beltrami operator. The Euclidean restriction is a geometric simplification, not a structural necessity. **Non-minimal.**

**PME-6 (Forward Parabolic).** *Minimal within the well-posed paradigm.* Forward parabolicity is required for well-posedness. Reversing the time orientation produces an ill-posed equation. This is a universal requirement for all parabolic PDEs, not specific to PME, but it is an independent axiom. **Minimal within paradigm.**

**PME-7 (No Reaction).** *Minimal — as a structural commitment.* The absence of a reaction term is a *deliberate architectural choice*, not a default. It is the axiom that makes PME a pure diffusion architecture. Adding a reaction term R(u) would extend the architecture to the porous-medium reaction-diffusion class — a different, richer system. The no-reaction axiom is what isolates the effects of nonlinear diffusion, making PME the structural baseline for the entire degenerate-parabolic class.

However, this axiom is also *restrictive*: it limits the architecture's generative scope (no patterns, no oscillations, no waves). Whether this counts as "minimal" depends on the evaluative frame. As a structural commitment that defines the PME class: **minimal.** As a restriction that limits generative scope: noted but accepted (the restriction is the architecture's purpose).

**PME-8 (Exponent m > 1).** *Non-minimal.* The specific value of m is a constitutive parameter — different physical systems correspond to different m. The qualitative behavior is the same for all m > 1, so any specific value (m = 2, m = 3, etc.) is a constitutive selection. The restriction m > 1 (rather than m = 1 or m < 1) is a *structural* choice that selects the slow-diffusion regime; but within m > 1, the specific value is constitutive. **Partially non-minimal:** the regime m > 1 is structural; the specific value of m is constitutive.

### 1.2 Minimality Summary

| Axiom | Content                     | Minimal?         | Comment                                |
|-------|-----------------------------|------------------|----------------------------------------|
| PME-1 | Continuum                  | Within paradigm  | Defines field theory                   |
| PME-2 | Locality                   | Yes              | Defines PDE paradigm                   |
| PME-3 | Nonlinear diffusion        | Yes              | *Is* the architecture                  |
| PME-4 | Conservation               | Yes              | Independent structural commitment      |
| PME-5 | Euclidean geometry         | **No**           | Geometric simplification               |
| PME-6 | Forward parabolic          | Within paradigm  | Required for well-posedness            |
| PME-7 | No reaction                | Yes              | Defines pure-diffusion class           |
| PME-8 | Exponent m > 1             | Partially        | Regime structural; specific m constitutive |

**Criterion 1 Verdict: CONDITIONAL.** The PME structural core (PME-2, PME-3, PME-4, PME-7) is *fully minimal* — four independent, irreducible axioms that define the pure degenerate-diffusion architecture with no redundancy. This is the *most minimal structural core* of any PDE in the PDE Atlas: four axioms compared to four for AC/CH and five for NS.

The non-minimal elements are: PME-5 (Euclidean geometry, a geometric simplification) and the specific value of m within the m > 1 regime (a constitutive parameter). These are the *fewest non-minimal elements* of any PDE in the Atlas (AC/CH have three non-minimal axioms each; NS has three; RD has four constitutive axioms).

The verdict is CONDITIONAL rather than PASS because PME-5 and the specific m are non-minimal, and CONDITIONAL rather than FAIL because the non-minimality is minimal (one geometric simplification + one constitutive parameter).

---

## 2. Locality

**Question:** Is the PME architecture fully local?

### 2.1 Assessment

Every element of the PME is local:

- **D_nl (Nonlinear diffusion):** Delta(u^m) = div(m u^{m-1} nabla u). Depends on u, nabla u, and Delta u at each point. Local.
- **C (Conservation):** The mass integral integral u dx is a global quantity, but its conservation is *enforced locally* through the divergence-form structure of the PDE and the no-flux boundary conditions. No nonlocal solve is required — the divergence theorem does the work.
- **G (Free boundary):** The free-boundary velocity V_n depends on the density gradient at the interface. Local.
- **M (Exponent):** Parameter. N/A.

There is no elliptic constraint, no Poisson equation, no Green's function, no integral operator, and no nonlocal coupling of any kind.

### 2.2 Comparison

**PME vs. NS:** NS has the nonlocal pressure channel (Poisson equation Delta p = -partial_i partial_j(u_i u_j)). PME has no analogue — there is no constraint requiring nonlocal enforcement.

**PME vs. CH:** Both are fully local. CH's conservation is also enforced locally (through the divergence-form bilaplacian). The locality class is the same.

**PME vs. AC:** Both are fully local. Same locality class.

**PME vs. RD:** Both are fully local. Same locality class.

### 2.3 Verdict

**Criterion 2 Verdict: PASS.** The PME is fully local at both formulation and solution levels. No nonlocal channel, no elliptic constraint, no Green's function. PME achieves the same locality class as ED, AC, CH, and RD — the strongest form of FS locality.

---

## 3. Determinism

**Question:** Does the PME uniquely determine the future from the initial data?

### 3.1 Assessment

The PME with m > 1 is *unconditionally globally well-posed* for all non-negative initial data in L^1(R^d):

- **Existence:** Global-in-time weak solutions exist for all u_0 in L^1(R^d), u_0 >= 0, in all dimensions d >= 1. Solutions are constructed via approximation (e.g., replacing the degenerate equation with non-degenerate approximations and taking limits).

- **Uniqueness:** Solutions are unique in the class of weak solutions satisfying the energy inequality. The uniqueness follows from the *L^1 contraction property*: if two solutions start with the same initial data, their L^1 distance is zero for all time.

- **Continuous dependence:** The L^1 contraction ||u(t) - v(t)||_{L^1} <= ||u_0 - v_0||_{L^1} provides Lipschitz continuous dependence on initial data — the strongest form of continuous dependence.

- **Positivity:** u_0 >= 0 implies u(t) >= 0 for all t > 0.

- **Regularity:** u is smooth (C^{infinity}) in the interior of {u > 0} and Holder continuous across the free boundary. The regularity is *position-dependent* (full smoothness inside, limited at the boundary) but there is no loss of existence or uniqueness.

### 3.2 No Conditional Hypotheses

Unlike NS (where 3D regularity requires conditional hypotheses like Serrin or BKM), the PME well-posedness is *unconditional*:

- No dimensional restriction (holds for all d >= 1).
- No smallness condition (holds for all masses M > 0).
- No conditional regularity criterion (no PME analogue of BKM).
- No blowup possibility (L^{infinity} norm decays).
- No uniqueness gap (L^1 contraction gives unconditional uniqueness).

### 3.3 Verdict

**Criterion 3 Verdict: PASS.** The PME achieves unconditional global determinism — existence, uniqueness, continuous dependence, and positivity — for all non-negative L^1 initial data, in all dimensions d >= 1, for all m > 1. This is the strongest determinism verdict possible. The L^1 contraction property provides a stability mechanism that is *strictly stronger* than what any other FS-evaluated architecture achieves.

---

## 4. Generative Sufficiency

**Question:** Does the PME generate all of its observed laws from the axioms?

### 4.1 Generated Phenomena

The PME generates the following from the axioms by rigorous mathematical derivation:

| Phenomenon                          | Derivation Method                                 |
|-------------------------------------|---------------------------------------------------|
| Finite-speed propagation            | Comparison with Barenblatt sub/super-solutions    |
| Free-boundary formation             | Degeneracy analysis + comparison principle         |
| Free-boundary velocity law (Darcy)  | Matched asymptotics + weak solution theory         |
| Waiting-time phenomena              | Local regularity analysis near flat interfaces     |
| Barenblatt self-similar profiles    | ODE reduction via self-similar ansatz              |
| Universal convergence to Barenblatt | Entropy methods (Carrillo–Toscani) + L^1 contraction |
| Algebraic decay rates (alpha, beta) | Scaling analysis + rigorous bounds                 |
| L^1 contraction                     | Comparison principle + Kato inequality              |
| Entropy dissipation                 | Direct computation from PDE                        |
| Positivity preservation             | Comparison with u = 0 sub-solution                 |
| Holder regularity at free boundary  | De Giorgi–Nash–Moser + Caffarelli–Friedman          |
| No blowup                          | Mass conservation + comparison with Barenblatt      |

The PME generates *all* of its observed laws from the axioms. There is no phenomenon attributed to the PME that requires assumptions beyond the axioms. The theory is *complete*: every question about the qualitative behavior of PME solutions has been answered.

### 4.2 Phenomena PME Cannot Generate

The PME's generative scope is *deliberately limited* by the no-reaction axiom (PME-7):

| Phenomenon                 | Status       | Reason for absence                           |
|---------------------------|-------------|----------------------------------------------|
| Oscillations              | Cannot generate | No reaction channel (PME-7)              |
| Turing patterns           | Cannot generate | n = 1, no reaction (PME-7)               |
| Traveling waves           | Cannot generate | No bistable/monostable reaction (PME-7)  |
| Spiral waves              | Cannot generate | n = 1, no reaction (PME-7)               |
| Spatiotemporal chaos      | Cannot generate | No reaction, L^1 contraction (PME-7)     |
| Phase separation          | Cannot generate | No double-well structure (PME-7)          |
| Blowup                    | Cannot generate | Diffusion is purely spreading (PME-3,4,7) |

These absences are not *failures* of generative sufficiency — they are *structural consequences* of the architecture's deliberate restriction to pure diffusion. The PME is designed to isolate the effects of nonlinear diffusion; asking it to generate reaction-dependent phenomena is asking the wrong question.

### 4.3 Assessment

The PME is *completely generatively sufficient within its domain*: every phenomenon that nonlinear degenerate diffusion can produce, the PME generates from its axioms. The generative gap is *zero* within the architecture's scope.

The architecture's scope is narrow (no oscillations, no patterns, no waves, no chaos) but *perfectly covered*: there is no phenomenon within the scope that requires additional assumptions.

### 4.4 Verdict

**Criterion 4 Verdict: PASS.** The PME is completely generatively sufficient within its architectural scope. Every law, every qualitative behavior, and every quantitative rate is derived from the axioms with no gap. The architecture generates *everything it is designed to generate*, with a complete and rigorous theory. This is the strongest generative sufficiency verdict in the Atlas — the only architecture where the theory is *provably complete*.

The narrow scope (no reaction phenomena) is a design choice, not a generative failure. Within its scope, the PME has the *zero generative gap* that every other architecture fails to achieve.

---

## 5. Envelope Tightness

**Question:** Is the PME envelope closed and tight?

### 5.1 Assessment of Each Component

**E1 (Degenerate parabolic inequality).** The one-sided property (free boundary only advances) is realized by the Barenblatt solution. **Tight.**

**E2 (Finite-speed propagation bound).** R(t) <= C t^{beta} is saturated by the Barenblatt solution. **Tight.**

**E3 (Barenblatt scaling laws).** The exponents alpha and beta are exact — determined uniquely by m and d. **Tight.**

**E4 (Entropy dissipation).** The specific dissipation identity dH/dt = -(4m/(m-1))||nabla(u^{(m+1)/2})||^2 is an exact equality. **Tight.**

**E5 (L^1 contraction).** Exact contraction — ||u(t) - v(t)||_{L^1} <= ||u_0 - v_0||_{L^1} with equality achievable for ordered data. **Tight.**

**E6 (Comparison principle).** Exact — u_0 <= v_0 implies u(t) <= v(t) with equality if and only if u_0 = v_0. **Tight.**

**E7 (Free-boundary velocity).** V_n = -(m/(m-1)) partial_n(u^{m-1}) is an exact law at smooth points. **Tight.**

**E8 (Mass conservation).** Exact identity. **Tight.**

**E9 (No blowup).** ||u(t)||_{L^{infinity}} <= C t^{-alpha} is sharp — saturated by the Barenblatt solution. **Tight.**

**E10 (Monotone smoothing).** All convex entropies decrease — exact property, not an approximation. **Tight.**

### 5.2 Envelope Closure

The PME envelope is *fully closed* with *no open faces*. The four sealing mechanisms:

1. **Degeneracy at u = 0:** Prevents mass from leaking into vacuum; enforces finite-speed propagation.
2. **Entropy dissipation:** Prevents interior concentration or oscillation; forces monotone smoothing.
3. **L^1 contraction:** Prevents solutions from diverging; forces convergence to Barenblatt.
4. **Mass conservation:** Prevents escape to infinity; constrains the attractor parameter.

No direction in function space is left unsealed. The envelope is closed from every direction.

### 5.3 Verdict

**Criterion 5 Verdict: PASS.** All ten envelope components are tight (exact identities or sharp bounds saturated by Barenblatt). The envelope is fully closed with no open faces, sealed by four independent mechanisms. This is the tightest envelope of any PDE in the PDE Atlas — every bound is sharp, every identity is exact, and the universal attractor is explicit.

---

## 6. Structural Optimality

**Question:** Is the PME architecture optimal — free of anomalies, structurally economical, and the simplest system that generates its observed laws?

### 6.1 Absence of Anomalies

The PME has *zero* structural anomalies:

- **No nonlocal channel.** All channels are local.
- **No destabilizing sub-channel.** The sole channel (D_nl) is unconditionally stabilizing — it dissipates all convex entropies and contracts all L^1 distances.
- **No open face.** The constraint surface is fully closed by four independent mechanisms.
- **No dimensional bifurcation.** The architecture behaves qualitatively the same in all d >= 1.
- **No blowup mechanism.** The L^{infinity} norm decays.
- **No oscillatory mechanism.** All entropies are monotone decreasing.
- **No chaotic mechanism.** L^1 contraction ensures stability.

### 6.2 Structural Economy

The PME is the *most structurally economical* nontrivial PDE in the PDE Atlas:

- Fewest dynamical channels: 1 (nonlinear diffusion).
- Fewest total channels: 3+1 (diffusion + conservation + free boundary + exponent).
- Fewest constitutive parameters: 1 (the exponent m).
- Fewest non-minimal axioms: 1.5 (PME-5 + specific m value).
- Simplest attractor: 1-parameter family (Barenblatt, parameterized by mass M).

No simpler PDE generates the PME phenomenology (finite-speed propagation, free boundaries, self-similar spreading). The linear heat equation (m = 1) is simpler but lacks all of these features. Any equation with fewer structural commitments than PME either reduces to the heat equation or is not a well-defined PDE.

### 6.3 Optimality Within the Degenerate Diffusion Class

The PME is the *canonical minimal member* of the degenerate diffusion class. Extensions include:

- **PME + reaction:** partial_t u = Delta(u^m) + R(u). Adds a reaction channel. Richer but less structurally pure.
- **PME + convection:** partial_t u = Delta(u^m) + div(u **v**). Adds a transport channel.
- **Doubly nonlinear:** partial_t u = div(|nabla u|^{p-2} nabla(u^m)). More general diffusion.
- **Multi-species PME:** partial_t u_i = Delta(u_i^{m_i}) + coupling. Multiple species.

All of these extend the PME by adding channels or complexity. None is simpler. The PME is the *floor* of the degenerate-diffusion hierarchy — the base case from which all extensions depart.

### 6.4 Comparison Across the Atlas

| Feature                      | PME           | AC            | CH            | NS              | RD               |
|------------------------------|-------------|---------------|---------------|-----------------|------------------|
| Anomalies                    | 0           | 0             | 0             | 2 (architectural)| 0 (class level)  |
| Non-minimal axioms           | ~1.5        | 3             | 3             | 3               | 4 (constitutive) |
| Channel count                | 3+1         | 4             | 5             | 5               | 4                |
| Constitutive parameters      | 1 (m)       | 3 (M, eps, f) | 3 (M, eps, f) | 2 (nu, f)       | Many             |
| Attractor complexity         | 1-param     | Finite set    | Manifold      | High-dim (2D)   | Constitutive     |
| Structural economy           | **Highest** | High          | Moderate      | Moderate        | Broad (class)    |

### 6.5 Verdict

**Criterion 6 Verdict: PASS.** The PME has zero anomalies, the highest structural economy of any PDE in the Atlas, and is the canonical minimal member of the degenerate diffusion class. No simpler architecture generates the same phenomenology. The single non-minimal element (Euclidean geometry + specific m value) is the minimum possible constitutive freedom for a physically meaningful PDE. The PME achieves the *strongest structural optimality verdict* of any PDE in the Atlas.

---

## 7. FS Verdict Summary

### 7.1 Criteria Scorecard

| Criterion                  | Verdict         | Comment                                                 |
|----------------------------|-----------------|---------------------------------------------------------|
| **1. Minimality**          | CONDITIONAL     | Structural core fully minimal; PME-5 and specific m non-minimal |
| **2. Locality**            | **PASS**        | Fully local at formulation and solution levels           |
| **3. Determinism**         | **PASS**        | Unconditional global well-posedness, all d >= 1, all m > 1 |
| **4. Gen. Sufficiency**    | **PASS**        | Zero generative gap within scope; provably complete theory |
| **5. Envelope Tightness**  | **PASS**        | All 10 components tight, 4 independent sealing mechanisms |
| **6. Structural Optimality** | **PASS**      | Zero anomalies, highest structural economy in Atlas      |

### 7.2 Comparison Across the PDE Atlas

| Criterion             | ED     | PME            | AC             | CH             | NS (2D)   | NS (3D)      | RD              |
|-----------------------|--------|----------------|----------------|----------------|-----------|--------------|-----------------|
| Minimality            | PASS   | CONDITIONAL    | FAIL           | FAIL           | FAIL      | FAIL         | CONDITIONAL     |
| Locality              | PASS   | **PASS**       | **PASS**       | **PASS**       | COND.     | COND.        | **PASS**        |
| Determinism           | PASS   | **PASS**       | **PASS**       | **PASS**       | PASS      | FAIL         | CONDITIONAL     |
| Gen. Sufficiency      | PASS   | **PASS**       | COND. (weak)   | COND. (weak)   | COND.     | COND.        | **PASS**        |
| Envelope Tightness    | PASS   | **PASS**       | **PASS**       | **PASS**       | PASS      | COND.        | CONDITIONAL     |
| Structural Optimality | PASS   | **PASS**       | COND.          | COND.          | FAIL      | FAIL         | CONDITIONAL     |

### 7.3 Architectural Summary

The Porous Medium Equation achieves the *strongest FS profile of any PDE* in the Atlas: five outright PASSes and one CONDITIONAL (on Minimality, due to the Euclidean geometry simplification and the constitutive exponent m). No other PDE achieves more than three outright PASSes. The PME is the only PDE that passes both Generative Sufficiency and Structural Optimality — a combination that no other PDE achieves because the tension between generative breadth and structural tightness usually forces a trade-off. The PME resolves this tension by restricting its scope to pure nonlinear diffusion, where the theory is complete, and excelling within that scope.

The PME's architectural strength traces to its *radical simplicity*: one dynamical channel (nonlinear diffusion), one conserved quantity (mass), one constitutive parameter (m), and one universal attractor (Barenblatt). This simplicity is not a limitation but an achievement — it produces the *most completely understood* PDE dynamics in mathematics, with explicit self-similar solutions, rigorous convergence theorems, sharp regularity results, and a theory that is provably complete within its scope.

The PME demonstrates a structural principle that is unique in the PDE Atlas: *maximum architectural soundness through minimum architectural complexity*. By committing to the fewest possible channels and the simplest possible dynamics, the PME achieves a level of structural closure, tightness, and optimality that richer architectures (NS, RD, even CH) cannot match.

### 7.4 Composite Verdict

The Porous Medium Equation is the structurally soundest PDE in the PDE Atlas — a radically simple, fully local, unconditionally deterministic, provably complete, anomaly-free architecture that achieves maximum structural tightness through minimum dynamical complexity, producing a single universal attractor from a single degenerate diffusion channel.

---

*End of AD Criteria and Verdict. This completes the AD architectural evaluation of the Porous Medium Equation.*
