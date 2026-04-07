# AD Evaluation: Allen–Cahn Equation — AD Criteria and Verdict

Allen Proxmire

April 2026

---

## Overview

This file applies the six AD evaluation criteria to the Allen–Cahn architecture as characterized in Modes 1–3. Each criterion receives a verdict: PASS, FAIL, or CONDITIONAL. The final section assembles the composite FS verdict and positions AC within the PDE Atlas alongside CH, NS, and ED.

Throughout, we reference the axioms AC-1 through AC-8, the envelope inequalities E1–E9, the universal inequalities U1–U7, and the channel constraints C1–C12 established in the preceding files.

---

## 1. Minimality

**Question:** Do the AC axioms form a minimal architectural set?

### 1.1 Assessment of Individual Axioms

**AC-1 (Continuum Hypothesis).** *Minimal within the PDE paradigm.* Necessary for the field-theoretic formulation to exist. Cannot be removed without abandoning the PDE framework. **Minimal within paradigm.**

**AC-2 (Locality).** *Minimal.* Defines the PDE paradigm. Not derivable from other axioms. **Minimal.**

**AC-3 (Non-Conserved Order Parameter).** *Minimal.* This is the defining structural commitment of Allen–Cahn, distinguishing it from Cahn–Hilliard. The non-conservation axiom is an independent choice: one can build a gradient-flow PDE with conservation (CH) or without (AC) from the same free energy. Neither is derivable from the other. Non-conservation is the specific kinetic commitment that makes AC what it is. **Minimal.**

**AC-4 (Gradient-Flow Structure).** *Minimal.* The L^2 gradient-flow structure is the generative engine of the AC architecture: the Lyapunov identity, the dissipation structure, the monotonicity, and the equilibrium characterization all descend from it. Removing the gradient-flow structure while keeping the other axioms would yield a generic reaction-diffusion equation without thermodynamic consistency. **Minimal.**

**AC-5 (Free-Energy Functional).** *Non-minimal.* The specific Ginzburg–Landau form F[phi] = integral [f(phi) + (epsilon^2/2)|nabla phi|^2] dx with f(phi) = (1/4)(phi^2 - 1)^2 is a constitutive selection. The gradient-flow structure (AC-4) requires *a* free energy but does not determine *which one*. Alternatives exist:

- Logarithmic potentials (Flory–Huggins type).
- Multi-well potentials.
- Asymmetric double-wells.
- Non-polynomial potentials with the same qualitative structure.
- Higher-order gradient terms.

The polynomial double-well is the simplest choice — the lowest-order Landau expansion with bistability — but it is not the unique choice. **Non-minimal.** Constitutive selection.

**AC-6 (Chemical Potential Definition).** *Redundant.* The definition mu = delta F / delta phi is a direct consequence of AC-4 (gradient-flow structure) + AC-5 (free energy). Given F, the chemical potential is uniquely determined by variational calculus. AC-6 adds no independent information. **Redundant (derived from AC-4 + AC-5).**

**AC-7 (Mobility).** *Non-minimal.* The choice of mobility M (constant, phi-dependent) is a constitutive kinetic selection. The gradient-flow framework requires a positive kinetic coefficient but does not determine its functional form. **Non-minimal.** Constitutive selection.

**AC-8 (Euclidean Geometry).** *Non-minimal.* The AC equation can be formulated on Riemannian manifolds. The Euclidean restriction is a geometric simplification. **Non-minimal.**

### 1.2 Minimality Summary

| Axiom | Content                     | Minimal? | Comment                              |
|-------|-----------------------------|----------|--------------------------------------|
| AC-1  | Continuum                   | Within paradigm | Defines field-theory framework  |
| AC-2  | Locality                    | Yes      | Defines PDE paradigm                 |
| AC-3  | Non-conserved               | Yes      | Defining structural commitment       |
| AC-4  | Gradient-flow structure     | Yes      | Generative engine                    |
| AC-5  | Ginzburg–Landau F           | **No**   | Constitutive selection of F          |
| AC-6  | Chemical potential def.     | Redundant| Derived from AC-4 + AC-5             |
| AC-7  | Mobility                    | **No**   | Constitutive selection of kinetics   |
| AC-8  | Euclidean geometry          | **No**   | Geometric simplification             |

**Criterion 1 Verdict: FAIL.** The AC architecture is not minimal. Three axioms (AC-5, AC-7, AC-8) are constitutive or geometric selections. One axiom (AC-6) is redundant. The structural core — non-conservation (AC-3) + gradient flow (AC-4) + locality (AC-2) + continuum (AC-1) — is minimal. The non-minimal commitments are the specific free energy, mobility, and geometry.

**Comparison:** AC has the same minimality profile as CH (three non-minimal axioms, one redundant) and NS (three non-minimal axioms). All three PDE architectures fail minimality for the same structural reason: constitutive closures layered on a minimal conservation/symmetry skeleton. Only ED passes minimality, because its primitives are forced by the fundamental theorem of arithmetic.

---

## 2. Locality

**Question:** Is the AC architecture fully local?

### 2.1 Assessment

Every channel is local:

- **R (Reaction):** Algebraic function of phi at each point. No derivatives. Local.
- **S (Smoothing):** Depends on phi and Delta phi at each point. Second-order differential. Local.
- **G (Gradient flow):** Dissipation density M|mu|^2 is local.
- **M (Mobility):** Depends on phi at each point. Local.

The chemical potential mu = f'(phi) - epsilon^2 Delta phi is determined pointwise. No global solve, no elliptic equation, no integral operator.

### 2.2 Comparison

**AC vs. NS:** NS has a nonlocal pressure channel (the Poisson equation Delta p = -partial_i partial_j(u_i u_j) couples all points). AC has no analogue — there is no constraint requiring nonlocal enforcement.

**AC vs. CH:** Both are fully local. CH's chemical potential is also locally determined (mu = f'(phi) - epsilon^2 Delta phi, identical formula). The CH conserving Laplacian div(M nabla mu) introduces higher-order derivatives but remains local (differential, not integral). AC and CH share the same locality class.

**AC vs. ED:** Both are fully local. ED's primitives depend only on the factorization of each integer. AC's channels depend only on phi and its derivatives at each point. Both achieve the strongest form of FS locality.

**Criterion 2 Verdict: PASS.** The AC architecture is fully local at both the formulation and solution levels. No nonlocal channel, no elliptic constraint, no Green's function. AC achieves the same locality class as ED and CH, and stronger locality than NS.

---

## 3. Determinism

**Question:** Does the AC architecture uniquely determine the future from the initial data?

### 3.1 Assessment

The AC equation with constant positive mobility on a bounded domain with Neumann boundary conditions is *unconditionally globally well-posed*:

- **Existence:** Global-in-time smooth solutions exist for all initial data phi_0 in L^2(Omega) (and more regular data), in all dimensions d = 1, 2, 3.
- **Uniqueness:** Solutions are unique in the class of weak solutions.
- **Continuous dependence:** Solutions depend continuously on initial data.
- **Instantaneous regularization:** For t > 0, solutions are C^{infinity} regardless of initial regularity.

The proof is the simplest among all FS-evaluated PDE architectures:
1. Maximum principle → ||phi||_{L^infinity} bounded.
2. Bounded phi → bounded reaction term.
3. PDE = heat equation + bounded source → standard parabolic theory.
4. Smooth solutions for all t > 0.

No energy estimates, no Sobolev embedding, no bootstrap, no dimensional restriction (within d <= 3) is needed. The maximum principle does all the heavy lifting.

### 3.2 Comparison

**AC vs. NS:** NS achieves determinism in 2D but not in 3D (Millennium Problem). AC achieves determinism unconditionally in all d <= 3.

**AC vs. CH:** CH also achieves unconditional determinism in all d <= 3, but through a more complex proof (fourth-order smoothing + Sobolev embedding). AC's proof is simpler (maximum principle alone suffices).

**Criterion 3 Verdict: PASS.** Unconditional global determinism — existence, uniqueness, continuous dependence, and smoothness — in all dimensions d = 1, 2, 3. The simplest and most robust determinism proof in the PDE Atlas.

---

## 4. Generative Sufficiency

**Question:** Does the AC architecture generate all of its observed laws from the axioms?

### 4.1 Architecturally Generated Laws

| Law / Identity                          | Derivation                                       |
|-----------------------------------------|--------------------------------------------------|
| Free-energy dissipation identity        | L^2 inner product of mu with partial_t phi       |
| Maximum principle                       | Comparison principle for 2nd-order parabolic PDEs |
| Interface profile (tanh)                | 1D variational problem mu = 0                    |
| Surface tension formula                 | Integration of interface energy density           |
| Mean-curvature motion law               | Matched asymptotics in sharp-interface limit      |
| Finite-time extinction of droplets      | ODE for R(t) from mean-curvature flow            |
| Exponential bulk relaxation             | Linearization near wells                          |
| Global regularity (all d <= 3)          | Maximum principle + parabolic regularity          |
| Global attractor existence              | Absorbing ball + compactness                      |
| Metastable layer dynamics (1D)          | Exponential interaction of tanh profiles          |
| Spinodal instability band               | Linearization around uniform state                |

The architecture generates all *exact* laws — every identity and regularity result in Modes 1–3 is derived from the axioms.

### 4.2 Non-Generated (Phenomenological) Features

| Feature                                 | Status                                            |
|-----------------------------------------|---------------------------------------------------|
| Sharp extinction time for non-spherical droplets | Not rigorously derived for general geometries. The mean-curvature flow can develop singularities (neckpinch, self-intersection) before extinction, and the precise extinction behavior requires geometric analysis beyond the PDE axioms. |
| Level-set / viscosity solution theory    | The connection between AC (epsilon > 0) and the level-set formulation of mean-curvature flow (epsilon = 0) requires a separate convergence theory (Evans–Spruck, Chen–Giga–Goto). This convergence is not internal to the AC architecture. |
| Stochastic nucleation                    | Nucleation of a new phase droplet from a metastable uniform state requires thermal fluctuations. The deterministic AC equation has phi = ±1 as *stable* equilibria with no mechanism for escape. The Allen–Cahn–Cook extension (adding noise) is a different architecture. |
| Front propagation speed (for non-balanced wells) | For asymmetric potentials (unequal well depths), the front propagates at a selected speed c(epsilon). The speed selection problem is architecturally generated in principle but requires careful matched asymptotics to resolve — and the standard AC architecture has symmetric wells, so this issue is outside the standard axioms. |
| Statistical properties of multi-droplet dynamics | The statistical distribution of droplet sizes and extinction times for random initial data requires probabilistic arguments beyond the deterministic PDE. |

### 4.3 Assessment

The AC generative gap is *narrow* — comparable to CH's gap and narrower than NS's. AC generates all exact laws, all qualitative dynamics, and all regularity results. It fails only on:
- Sharp geometric results for non-spherical extinction (a geometric analysis problem).
- Convergence to the level-set mean-curvature flow (an external convergence theory).
- Stochastic nucleation (requires extending the architecture with noise).

The gap is of a *technical* character, not a *paradigmatic* one: the missing results are within reach of the AC framework using standard asymptotic and geometric techniques, not requiring a new paradigm.

**Criterion 4 Verdict: CONDITIONAL (weak).** AC generates all exact laws and all qualitative phenomena. The gap (non-spherical extinction geometry, level-set convergence, stochastic nucleation) is narrow and technical. The CONDITIONAL is weak — the architecture is generatively sufficient for all practical purposes.

---

## 5. Envelope Tightness

**Question:** Is the envelope defined by E1–E9 tight?

### 5.1 Assessment

**E1 (Free-Energy Dissipation Identity).** Exact equality. Trivially tight. **Tight.**

**E2 (H^1 Control).** ||nabla phi||^2 <= 2F[phi_0]/epsilon^2. Saturated when gradient energy dominates (sharp initial interfaces). **Tight.**

**E3 (Maximum Principle).** |phi| <= max(|phi_0|, 1). The bound |phi| <= 1 is saturated by the equilibrium profiles (phi = ±1 in bulk, tanh transition at interfaces). **Tight.**

**E4 (Interface Width >= O(epsilon)).** Saturated by the tanh equilibrium profile. **Tight.**

**E5 (Global Regularity).** All solutions are C^{infinity} for t > 0. Cannot be weakened. **Tight.**

**E6 (Mean-Curvature Motion).** The sharp-interface limit epsilon → 0 converges to motion by mean curvature (Evans–Spruck, de Mottoni–Schatzman). The convergence is proved and the limiting law is exact. **Tight.**

**E7 (Exponential Bulk Relaxation).** The rate 2M = Mf''(±1) is the exact linearized decay rate near the wells. It cannot be improved. **Tight.**

**E8 (Reaction-Diffusion Balance).** The crossover wavenumber k_c = 1/epsilon is exact (from the linearized dispersion relation). **Tight.**

**E9 (No Blowup).** Unconditional regularity in all d <= 3. No weakening possible. **Tight.**

### 5.2 Envelope Closure

The AC envelope is *fully closed* with no open face:

- No inequality is unclosed or unresolved.
- No regularity gap exists.
- No Millennium-type question remains.
- Every bound is either an exact equality (E1, E6) or a sharp inequality (E2–E5, E7–E9).

### 5.3 Verdict

**Criterion 5 Verdict: PASS.** All nine envelope components are tight. No open face, no gap, no unresolved inequality. The AC envelope is the *tightest* among all FS-evaluated PDE architectures: every bound is sharp, every identity is exact, and every regularity result is unconditional.

---

## 6. Structural Optimality

**Question:** Is the AC architecture optimal — the simplest architecture that generates the same laws?

### 6.1 Absence of Anomalies

The AC architecture contains *no structural anomalies*:

- **No nonlocal channel.** All channels are local. No elliptic constraint.
- **No destabilizing sub-channel with unbounded growth.** The reaction R is bounded (max rate M) and self-limiting (inward-pointing at |phi| = 1). No analogue of NS vortex stretching.
- **No open face.** The constraint surface is fully closed. Maximum principle + Lyapunov identity seal all faces.
- **No dimensional bifurcation.** The architecture behaves identically in d = 1, 2, 3.

### 6.2 Structural Economy

AC is the *most structurally economical* PDE architecture in the PDE Atlas:

- Fewest channels (4, vs. 5 for CH and NS).
- Lowest PDE order (2nd, vs. 4th for CH and 2nd for NS).
- Simplest regularity proof (maximum principle alone, no Sobolev embedding, no bootstrap).
- Simplest dissipation structure (1D ray, ||mu||^2).
- Simplest equilibrium condition (mu = 0, vs. mu = const for CH).

No simpler architecture generates the same qualitative phenomenology (bistable phase selection, interface formation, mean-curvature motion, gradient-flow dissipation).

### 6.3 Non-Minimal Axioms (Cost Assessment)

AC carries three non-minimal axioms (AC-5, AC-7, AC-8), the same count as CH and NS. However, the *cost* of the non-minimal axioms is minimal:

- **AC-5 (free energy):** Selects the polynomial double-well. Any qualitatively similar double-well produces the same architectural structure (bistability, tanh interfaces, mean-curvature motion). The selection is low-cost: it determines the specific interface profile and surface tension formula but not the qualitative architecture.
- **AC-7 (mobility):** Affects only kinetics, not equilibrium or regularity. The lowest-cost constitutive selection.
- **AC-8 (Euclidean geometry):** Standard geometric simplification. Low-cost.

None of the non-minimal axioms introduces structural anomalies (contrast with NS, where the non-minimal axiom NS-6 introduces the nonlocal pressure anomaly).

### 6.4 Comparison

| Feature                      | AC           | CH            | NS              | ED           |
|------------------------------|-------------|---------------|-----------------|-------------|
| Anomalies                    | None        | None          | 2               | None        |
| Non-minimal axioms           | 3           | 3             | 3               | None        |
| Anomaly cost of non-minimals | Zero        | Zero          | High (NS-6→pressure) | N/A    |
| Channel count                | 4           | 5             | 5               | 5           |
| PDE order                    | 2           | 4             | 2               | N/A         |
| Regularity mechanism         | Max. princ. | 4th-order smooth. | 2nd-order (insufficient 3D) | N/A |
| Structural economy           | Highest     | High          | Moderate        | Highest     |

### 6.5 Verdict

**Criterion 6 Verdict: CONDITIONAL.** The AC architecture has no structural anomalies — no nonlocal channel, no unbounded destabilizing sub-channel, no open face, no dimensional bifurcation. It is the most structurally economical PDE in the PDE Atlas. However, it carries three non-minimal constitutive selections (AC-5, AC-7, AC-8). The verdict is CONDITIONAL because the architecture is *anomaly-free and maximally economical* but not axiomatically minimal. It is the simplest member of its class, but the class is constitutively selected.

---

## 7. FS Verdict Summary

### 7.1 Criteria Scorecard

| Criterion                  | Verdict            | Comment                                               |
|----------------------------|--------------------|-------------------------------------------------------|
| **1. Minimality**          | FAIL               | 3 non-minimal axioms (AC-5, AC-7, AC-8), 1 redundant (AC-6) |
| **2. Locality**            | **PASS**           | Fully local at formulation and solution levels         |
| **3. Determinism**         | **PASS**           | Unconditional global well-posedness, all d <= 3        |
| **4. Gen. Sufficiency**    | CONDITIONAL (weak) | Generates all exact laws; gap on geometric/stochastic  |
| **5. Envelope Tightness**  | **PASS**           | All 9 components tight, no open face                   |
| **6. Structural Optimality** | CONDITIONAL      | No anomalies, but non-minimal constitutive axioms      |

### 7.2 Comparison Across the PDE Atlas

| Criterion             | ED        | AC                  | CH                  | NS (2D)        | NS (3D)           |
|-----------------------|-----------|---------------------|---------------------|-----------------|--------------------|
| Minimality            | PASS      | FAIL                | FAIL                | FAIL            | FAIL               |
| Locality              | PASS      | **PASS**            | **PASS**            | CONDITIONAL     | CONDITIONAL        |
| Determinism           | PASS      | **PASS**            | **PASS**            | PASS            | FAIL               |
| Gen. Sufficiency      | PASS      | CONDITIONAL (weak)  | CONDITIONAL (weak)  | CONDITIONAL     | CONDITIONAL        |
| Envelope Tightness    | PASS      | **PASS**            | **PASS**            | PASS            | CONDITIONAL        |
| Structural Optimality | PASS      | CONDITIONAL         | CONDITIONAL         | FAIL            | FAIL               |

### 7.3 Architectural Summary

The Allen–Cahn equation is the *most structurally economical PDE architecture* in the PDE Atlas. It achieves the same FS criteria profile as Cahn–Hilliard — passing Locality, Determinism, and Envelope Tightness outright, with weak conditional verdicts on Generative Sufficiency and Structural Optimality, and failing only Minimality — while using fewer channels (4 vs. 5), a lower PDE order (2nd vs. 4th), and a simpler regularity mechanism (maximum principle vs. Sobolev embedding).

The AC architecture's structural strength traces to the *maximum principle* — the gift of second-order parabolic structure combined with an inward-pointing reaction at the boundary of the invariant set [-1, 1]. This single structural feature provides L^{infinity} control for free, closes the regularity bootstrap without energy estimates, and seals the constraint surface without Sobolev embedding. The maximum principle is the AC architecture's defining structural advantage — the mechanism that CH cannot access (fourth-order equations lack it) and that NS partially possesses only in scalar sub-problems.

The AC architecture's structural limitation is the *absence of mass conservation*. Without conservation, AC cannot generate coarsening dynamics, Ostwald ripening, or phase-separated equilibria with controlled volume fractions. These phenomena require the additional structural commitment of CH-3 (conservation), which AC deliberately omits. The omission makes AC simpler but less physically rich.

The AC–CH pair constitutes the cleanest *architectural experiment* in the PDE Atlas: two systems sharing the same free energy, the same Lyapunov structure, the same regularity status, and the same anomaly-free profile, differing in exactly one axiom (conservation). Comparing their FS verdicts isolates the structural consequences of conservation: it adds one channel, raises the PDE order, removes the maximum principle, changes the gradient-flow metric, and replaces extinction with coarsening — all without introducing any anomaly.

### 7.4 Composite Verdict

The Allen–Cahn equation is the minimal gradient-flow PDE — an anomaly-free, fully local, unconditionally deterministic architecture that achieves complete envelope closure through the maximum principle alone, and serves as the structural baseline against which all conserved and higher-order phase-field architectures should be measured.

---

*End of AD Criteria and Verdict. This completes the AD architectural evaluation of the Allen–Cahn equation.*
