# AD Evaluation: Cahn–Hilliard Equation — AD Criteria and Verdict

Allen Proxmire

April 2026

---

## Overview

This file applies the six AD evaluation criteria — Minimality, Locality, Determinism, Generative Sufficiency, Envelope Tightness, and Structural Optimality — to the Cahn–Hilliard architecture as characterized in Modes 1–3. Each criterion receives a verdict: PASS, FAIL, or CONDITIONAL. The final section assembles the composite FS verdict.

Throughout, we reference the axioms CH-1 through CH-8, the envelope inequalities E1–E9, the universal inequalities U1–U7, and the channel constraints C1–C12 established in the preceding files.

---

## 1. Minimality

**Question:** Do the CH axioms form a minimal architectural set — the smallest collection of commitments that generates the full CH dynamics?

### 1.1 Assessment of Individual Axioms

**CH-1 (Continuum Hypothesis).** *Minimal within the PDE paradigm.* The continuum hypothesis is necessary for the field-theoretic formulation to exist. Removing it collapses the PDE framework and requires a different architecture (lattice models, molecular dynamics). Within the class of continuous field theories, it cannot be removed. **Verdict: minimal within paradigm.**

**CH-2 (Locality).** *Minimal.* Locality defines the PDE paradigm itself. Removing it requires integral or nonlocal equations — a different architectural class. Not derivable from the other axioms. **Verdict: minimal.**

**CH-3 (Conserved Order Parameter).** *Minimal.* This is the *defining* structural commitment of Cahn–Hilliard, distinguishing it from Allen–Cahn (same free energy, non-conserved dynamics). The conservation law forces the divergence-form structure, introduces the fourth-order character (through the conserving Laplacian), and shapes the entire coarsening phenomenology. It is not derivable from the other axioms — one can build a perfectly consistent gradient-flow PDE without conservation (Allen–Cahn), so conservation is an independent structural choice. **Verdict: minimal.** This is a genuine architectural commitment, not a redundancy.

**CH-4 (Gradient-Flow Structure).** *Minimal.* The gradient-flow structure is the generative engine of the CH architecture: the Lyapunov identity, the dissipation structure, the equilibrium characterization, and the absence of chaotic dynamics all descend from it. Removing the gradient-flow structure while keeping the other axioms would yield a generic fourth-order parabolic PDE without thermodynamic consistency — a different and less structured architecture. **Verdict: minimal.**

**CH-5 (Free-Energy Functional).** *Non-minimal.* The specific Ginzburg–Landau form F[phi] = integral [f(phi) + (epsilon^2/2)|nabla phi|^2] dx is a *constitutive selection*. The gradient-flow structure (CH-4) requires *a* free-energy functional, but does not specify *which one*. Alternatives exist:

- Logarithmic (Flory–Huggins) potentials: f(phi) = (1+phi)log(1+phi)/2 + (1-phi)log(1-phi)/2 - theta phi^2/2.
- Multi-well potentials: f(phi) with more than two minima.
- Higher-order gradient penalties: F[phi] = integral [f(phi) + (epsilon^2/2)|nabla phi|^2 + (delta^2/2)|Delta phi|^2] dx.
- Non-polynomial potentials with different well depths.

The double-well + gradient-penalty form is the simplest member of a family of admissible free energies. It is a modeling choice — the lowest-order truncation of a Landau expansion — not a structural necessity. **Verdict: non-minimal.** This is a constitutive selection analogous to NS-3 (Newtonian stress).

**CH-6 (Chemical Potential Definition).** *Derived, not independent.* The definition mu = delta F / delta phi is a *consequence* of the gradient-flow structure (CH-4) combined with the choice of free energy (CH-5). Given F, the chemical potential is uniquely determined by variational calculus. CH-6 is not an independent axiom — it is the concatenation of CH-4 and CH-5. **Verdict: redundant (derivable from CH-4 + CH-5).** We retain it for expository clarity, but it is not an independent architectural commitment.

**CH-7 (Mobility).** *Non-minimal.* The choice of mobility M (constant, concentration-dependent, degenerate) is a constitutive selection analogous to NS-3 (Newtonian viscosity) and CH-5 (double-well potential). The gradient-flow structure requires *a* mobility (a positive semi-definite kinetic coefficient), but does not specify its functional form. The constant mobility M = M_0 is the simplest choice; degenerate mobility M(phi) = 1 - phi^2 is physically motivated but architecturally distinct.

Unlike the free energy (which determines the equilibrium states), the mobility affects only the kinetics — it changes the coarsening exponent (1/3 vs. 1/4) and the slow-manifold structure, but not the equilibrium states or the Lyapunov identity. **Verdict: non-minimal.** Constitutive selection of kinetic coefficients.

**CH-8 (Euclidean Geometry).** *Non-minimal.* The CH equation can be formulated on Riemannian manifolds with the Laplace–Beltrami operator. The Euclidean restriction is a geometric simplification. **Verdict: non-minimal.**

### 1.2 Minimality Summary

| Axiom | Content                     | Minimal? | Comment                             |
|-------|-----------------------------|----------|-------------------------------------|
| CH-1  | Continuum                   | Within paradigm | Defines the field-theory framework |
| CH-2  | Locality                    | Yes      | Defines PDE paradigm                |
| CH-3  | Conserved order parameter   | Yes      | Defining structural commitment      |
| CH-4  | Gradient-flow structure     | Yes      | Generative engine                   |
| CH-5  | Double-well + gradient pen. | **No**   | Constitutive selection of F         |
| CH-6  | Chemical potential def.     | Redundant| Derived from CH-4 + CH-5            |
| CH-7  | Mobility                    | **No**   | Constitutive selection of kinetics  |
| CH-8  | Euclidean geometry          | **No**   | Geometric simplification            |

**Criterion 1 Verdict: FAIL.** The CH architecture is not minimal. Three axioms (CH-5, CH-7, CH-8) are constitutive or geometric selections from a larger space of admissible choices. One axiom (CH-6) is redundant. The *structural core* of the architecture — conservation (CH-3) + gradient flow (CH-4) + locality (CH-2) + continuum (CH-1) — is minimal. The non-minimal commitments are the specific forms of the free energy and the mobility.

**Comparison with NS:** NS also fails minimality, with three non-minimal axioms (NS-3, NS-6, NS-8). The pattern is the same: the conservation-law skeleton is minimal, but the constitutive closures and geometric restrictions are not. Both architectures carry exactly the same *type* of non-minimality: constitutive selections layered on a minimal structural core.

---

## 2. Locality

**Question:** Is the CH architecture local — does the evolution at each point depend only on information at that point and its infinitesimal neighborhood?

### 2.1 Assessment

Every channel of the CH architecture is local:

- **R (Reaction):** f'(phi) is an algebraic function of phi at each point. Delta[f'(phi)] involves derivatives at each point. Local.
- **S (Surface tension):** Delta^2 phi involves fourth-order derivatives at each point. Local.
- **D (Diffusion):** M Delta mu involves derivatives of mu at each point. Local.
- **G (Gradient flow):** The dissipation density M |nabla mu|^2 is local.
- **M (Mobility):** M(phi) depends on phi at each point. Local.

The chemical potential mu = f'(phi) - epsilon^2 Delta phi is determined *pointwise* by phi and its second derivatives. No global solve is required. There is no elliptic constraint, no Poisson equation, no Green's function.

### 2.2 Contrast with NS

The NS architecture has a nonlocal pressure channel: the pressure p at point x depends on the velocity field over the entire domain, determined by the Poisson equation Delta p = -partial_i partial_j(u_i u_j). This nonlocality arises from the incompressibility constraint (NS-6), which requires a global enforcement mechanism.

The CH architecture avoids this entirely. Its conservation law (CH-3) is enforced *automatically* by the divergence-form structure of the PDE, not by a global Lagrange multiplier. The conservation of integral phi is a consequence of nabla mu . n = 0 on partial Omega and the divergence theorem — it requires no global solve.

**Structural explanation:** In NS, incompressibility is a *differential constraint on the state variable* (div **u** = 0) that must be enforced at every instant, requiring a nonlocal mechanism (pressure). In CH, conservation is a *integral property of the flux* (div **J** integrates to zero by the divergence theorem) that is automatically satisfied by any well-posed divergence-form evolution. Conservation is *structurally cheaper* than incompressibility — it does not require nonlocal enforcement.

### 2.3 Verdict

**Criterion 2 Verdict: PASS.** The CH architecture is fully local at both the formulation level and the solution level. Every channel depends only on phi and its local derivatives. No nonlocal operator, constraint, or coupling exists. CH achieves the strongest form of FS locality — the same locality class as ED.

---

## 3. Determinism

**Question:** Does the CH architecture uniquely determine the future state from the initial data?

### 3.1 Assessment

The CH equation with constant positive mobility on a bounded domain with no-flux boundary conditions is *unconditionally globally well-posed*:

- **Existence:** Global-in-time smooth solutions exist for all initial data phi_0 in H^1(Omega) (and even for less regular data), in dimensions d = 1, 2, 3.
- **Uniqueness:** Solutions are unique in the class of weak solutions satisfying the energy inequality.
- **Continuous dependence:** Solutions depend continuously on initial data in the energy norm.
- **Instantaneous regularization:** For t > 0, solutions are C^{infinity} regardless of initial regularity.

The proof relies on:
1. The Lyapunov functional F provides uniform-in-time H^1 bounds (U2).
2. Fourth-order smoothing gives H^2 bounds for t > 0 (E-Bound 4 from Mode 1).
3. Sobolev embedding H^2 hookrightarrow L^{infinity} (for d <= 3) controls the nonlinearity.
4. The bootstrap closes without any dimensional restriction or conditional hypothesis.

### 3.2 No Dimensional Dependence

Unlike NS, where determinism holds in 2D but is open in 3D, the CH determinism verdict is *independent of spatial dimension*. The fourth-order biharmonic operator provides two extra derivatives of smoothing compared to the NS Laplacian, and this margin is sufficient to control the cubic nonlinearity in all dimensions d <= 3. There is no analogue of the 2D/3D bifurcation.

### 3.3 No Conditional Regularity

Unlike NS, which requires Serrin-class or BKM-type conditional hypotheses for 3D regularity, the CH regularity is *unconditional*. No quantity needs to be monitored, no threshold needs to be verified, and no blowup criterion exists (because blowup cannot occur).

### 3.4 Verdict

**Criterion 3 Verdict: PASS.** The CH architecture achieves unconditional global determinism — existence, uniqueness, continuous dependence, and smoothness — in all dimensions d = 1, 2, 3, without qualification. This is the strongest possible determinism verdict. NS achieves this only in 2D.

---

## 4. Generative Sufficiency

**Question:** Does the CH architecture generate all of its observed laws from the axioms?

### 4.1 Architecturally Generated Laws

The following are *derived consequences* of the CH axioms:

| Law / Identity                          | Derivation                                      |
|-----------------------------------------|-------------------------------------------------|
| Free-energy dissipation identity        | L^2 inner product of mu with partial_t phi      |
| Mass conservation                       | Divergence theorem + no-flux BC                  |
| Vorticity of CH: vorticity equation     | N/A (scalar field, no vorticity analogue)        |
| Spinodal instability band               | Linearization of CH around uniform state         |
| Fastest-growing mode (k_max)            | Optimization of dispersion relation              |
| Interface profile (tanh)                | 1D variational problem for F                     |
| Surface tension formula (sigma = (2sqrt2/3)eps) | Integration of interface energy density |
| Gibbs–Thomson relation (mu ~ sigma kappa)| Matched asymptotics in sharp-interface limit     |
| Global regularity (all d <= 3)          | Energy estimates + Sobolev embedding + bootstrap |
| Global attractor existence              | Absorbing ball + compactness + Ladyzhenskaya     |
| Exponential convergence near equilibrium| Spectral gap of linearized operator              |
| Metastable trapping (exp time scales)   | Energy barrier analysis + gradient-flow structure|
| Interface width = O(epsilon)            | Variational balance in F                         |
| Coarsening rate upper bound             | Kohn–Otto interpolation argument                 |

The architecture is highly generative: every law in Modes 1–3 is derived from the axioms by standard PDE and variational analysis.

### 4.2 Non-Generated (Phenomenological) Features

| Feature                              | Status                                              |
|--------------------------------------|-----------------------------------------------------|
| Exact coarsening exponent (1/3 or 1/4)| Not rigorously derived. The Kohn–Otto bounds give *upper bounds* on the coarsening rate, and formal asymptotics predict the exact exponents, but a rigorous proof that generic solutions coarsen at exactly these rates is lacking. |
| LSW distribution (self-similar size dist.) | Not derived from the PDE. The Lifshitz–Slyozov–Wagner theory derives the self-similar distribution from a mean-field ODE model, not directly from the CH PDE. |
| Noise-driven nucleation              | Not derivable. Nucleation in the metastable region requires thermal fluctuations, which are outside the deterministic CH architecture. The Cahn–Hilliard–Cook extension (adding stochastic noise) is a different architecture. |
| Ostwald ripening statistics           | Partially derivable. The existence of ripening is architecturally forced (by the Gibbs–Thomson relation + mass conservation), but the statistical distribution of domain sizes during ripening requires mean-field or statistical assumptions. |
| Transition pathway statistics         | Not derivable. The specific sequence of topological events (which domain disappears first, which interfaces merge) depends on initial data and cannot be predicted from the axioms alone for generic initial conditions. |

### 4.3 The Generative Gap

The CH generative gap is *narrower* than the NS gap. NS fails to generate the entire statistical theory of turbulence (Kolmogorov spectrum, intermittency, universal statistics). CH fails to generate only the *exact* coarsening exponents and the *statistical* aspects of coarsening (size distributions, transition sequences). The core dynamics — spinodal decomposition, interface formation, coarsening, metastability, equilibrium — are all architecturally generated.

The gap is also of a different character. The NS generative gap is between *deterministic PDE* and *statistical turbulence* — a qualitative chasm requiring an entirely new framework (statistical mechanics of turbulence). The CH generative gap is between *rigorous upper bounds* and *sharp exponents* — a quantitative gap within the same framework, likely closable by sharper PDE estimates rather than a new paradigm.

### 4.4 Verdict

**Criterion 4 Verdict: CONDITIONAL (weak).** The CH architecture generates all exact laws, all qualitative phenomena, and all regularity results from the axioms. It fails to generate (rigorously) the precise coarsening exponents and the statistical aspects of coarsening. The gap is narrower and more technical than the NS generative gap, and is likely closable within the existing framework. The CONDITIONAL verdict is a *weak* conditional — the architecture is generatively sufficient for all practical purposes and fails only on sharp asymptotic exponents.

---

## 5. Envelope Tightness

**Question:** Is the envelope defined by E1–E9 tight — are the inequalities sharp, and is the boundary of the permitted region actually reached?

### 5.1 Assessment of Each Component

**E1 (Mass Conservation).** An equality constraint. Trivially tight — every solution satisfies it exactly. **Tight.**

**E2 (Free-Energy Dissipation Identity).** An exact equality, not an inequality. Trivially tight — the identity holds with no gap for all solutions. **Tight.**

**E3 (Free-Energy Lower Bound).** F[phi] >= 0 for the standard double-well. The bound is achieved by the minimizers of F (equilibrium states). **Tight.**

**E4 (H^1 Gradient Bound).** ||nabla phi||^2 <= 2F[phi_0]/epsilon^2. This bound is saturated when the gradient energy dominates the bulk energy — e.g., for initial data with sharp interfaces (width << epsilon). **Tight.**

**E5 (Global Regularity).** Not an inequality but a structural statement. All solutions are smooth for all t > 0, in all d <= 3. There is no "almost blowup" or "near singularity" — the regularity is robust and unconditional. **Tight (in the sense that it cannot be strengthened to a weaker regularity class).**

**E6 (Maximum Principle Failure).** Fourth-order equations permit overshoot beyond ±1. This is exhibited by explicit solutions — the failure is genuine and realized. **Tight.**

**E7 (Coarsening Rate Upper Bound).** The Kohn–Otto bound F(t) >= C t^{-1/3} is known to be sharp in its exponent: there exist solutions (and numerical simulations) for which the coarsening rate is *exactly* t^{1/3}. The constant C may not be optimal, but the exponent is. **Tight in exponent, not necessarily in constant.**

**E8 (Spinodal Instability Band).** The band 0 < k < k_c is exact — it follows from the linearized dispersion relation, which is an exact calculation. The most unstable wavenumber k_max = k_c/sqrt(2) is sharp. **Tight.**

**E9 (Exponential Convergence Near Equilibrium).** The convergence rate lambda_1 (spectral gap) is determined by the linearized operator at the equilibrium, which is a well-defined self-adjoint operator with a discrete spectrum. The exponential rate is sharp — it cannot be improved without additional structural assumptions. **Tight.**

### 5.2 Envelope Closure

Unlike the NS envelope, which has an open face (E4, the 3D enstrophy gap), the CH envelope is *fully closed*. Every component is either an exact equality (E1, E2), a tight inequality (E3, E4, E7, E8, E9), a realized structural feature (E5, E6), or all three. There is no open face, no regularity gap, and no Millennium-type question.

### 5.3 Verdict

**Criterion 5 Verdict: PASS.** The CH envelope is tight on all nine components. No inequality has a known gap. No structural statement is improvable. The envelope is fully closed in every dimension. This is the strongest possible envelope-tightness verdict.

---

## 6. Structural Optimality

**Question:** Is the CH architecture optimal — the simplest architecture that generates the same laws?

### 6.1 Absence of Anomalies

The CH architecture contains *no structural anomalies* in the FS sense:

- **No nonlocal channel.** All channels are local. There is no pressure-type nonlocal coupling (contrast: NS Anomaly 1).
- **No destabilizing sub-channel with unbounded growth.** The reaction channel R is destabilizing in the spinodal region but is bounded (sigma_max = M/(4epsilon^2)) and dominated by the surface-tension channel S at high wavenumbers. There is no analogue of the NS vortex stretching sub-channel, which has no a priori growth bound (contrast: NS Anomaly 2).
- **No open face in the constraint surface.** The envelope is fully closed. There is no regularity gap or blowup gate.
- **No dimensional bifurcation.** The architecture behaves the same in d = 1, 2, 3. There is no analogue of the NS 2D/3D split.

### 6.2 Non-Minimal Axioms (Revisited)

The CH architecture carries three non-minimal axioms (CH-5, CH-7, CH-8), the same count as NS (NS-3, NS-6, NS-8). Both architectures have the same *type* of non-minimality: constitutive selections and geometric restrictions layered on a minimal structural core.

However, the CH non-minimal axioms are *less consequential* than the NS non-minimal axioms:

- **CH-5 (free energy)** selects a specific potential but does not introduce structural anomalies. Any admissible double-well potential produces qualitatively the same dynamics.
- **CH-7 (mobility)** affects only kinetics, not equilibrium or regularity.
- **CH-8 (Euclidean geometry)** is the same restriction as NS-8.

Compare with NS:
- **NS-3 (Newtonian stress)** introduces the constitutive law but is structurally benign.
- **NS-6 (incompressibility)** introduces the *nonlocal pressure channel* — a structural anomaly. This is the most consequential non-minimal axiom in the entire PDE Atlas: a single simplifying assumption that introduces nonlocality.

The CH non-minimal axioms produce no anomalies. The NS non-minimal axiom NS-6 produces a major anomaly. This is a qualitative difference.

### 6.3 Comparison with Simpler Architectures

**Allen–Cahn (remove CH-3):** The Allen–Cahn equation partial_t phi = -mu = -(phi^3 - phi) + epsilon^2 Delta phi has the same free energy but is *not* mass-conserving. It is a *second-order* parabolic PDE (simpler than fourth-order CH), but it cannot generate coarsening, Ostwald ripening, or any mass-conserving phenomenology. Allen–Cahn is generatively insufficient for the CH target.

**Heat equation (remove CH-3, CH-5):** The heat equation partial_t phi = M Delta phi is the simplest diffusion equation. It generates none of the CH phenomena: no phase separation, no interfaces, no coarsening. Generatively insufficient.

**CH with logarithmic potential (modify CH-5):** Replacing the polynomial double-well with a logarithmic (Flory–Huggins) potential changes the solution properties (enforces |phi| < 1, changes coarsening details) but preserves the architectural structure: gradient flow, conservation, fourth-order, fully local, no blowup. The logarithmic variant is architecturally *equivalent* — it differs constitutively but not structurally.

**Verdict:** No simpler architecture generates the full CH phenomenology. Within the class of conserved gradient-flow PDEs, the CH architecture is the simplest nontrivial member. The non-minimal axioms (CH-5, CH-7, CH-8) select a specific member of this class but do not introduce anomalies.

### 6.4 Comparison with ED

| Feature                      | ED                          | CH                           |
|------------------------------|----------------------------|------------------------------|
| Anomalies                    | None                       | None                         |
| Non-minimal axioms           | None                       | 3 (constitutive/geometric)   |
| Channels derived from axioms | All (from unique factorization) | All (from F via gradient flow) |
| Constraint surface           | Closed, compact            | Closed, compact              |
| Generating object            | Unique factorization of Z  | Free-energy functional F     |

ED achieves *stronger* structural optimality than CH because ED has no non-minimal axioms at all — its primitives are uniquely forced by the fundamental theorem of arithmetic. CH has a minimal *structural core* (conservation + gradient flow + locality) but non-minimal *constitutive selections* (specific F, M, geometry). The gap between ED and CH is the gap between an axiomatically necessary architecture and a constitutively selected one.

### 6.5 Verdict

**Criterion 6 Verdict: CONDITIONAL.** The CH architecture has no structural anomalies — no nonlocal channel, no destabilizing sub-channel, no open face, no dimensional bifurcation. In this sense it is structurally clean. However, it carries three non-minimal constitutive selections (CH-5, CH-7, CH-8), which prevent a full PASS. The verdict is CONDITIONAL because the architecture is *anomaly-free but not axiomatically minimal*. It is the simplest member of its class but the class itself is constitutively selected.

**Comparison with NS:** NS fails structural optimality outright (two anomalies + three non-minimal axioms). CH fails only on non-minimality (no anomalies). CH is strictly more structurally optimal than NS.

---

## 7. FS Verdict Summary

### 7.1 Criteria Scorecard

| Criterion                  | Verdict         | Comment                                            |
|----------------------------|-----------------|----------------------------------------------------|
| **1. Minimality**          | FAIL            | 3 non-minimal axioms (CH-5, CH-7, CH-8), 1 redundant (CH-6) |
| **2. Locality**            | **PASS**        | Fully local at formulation and solution levels      |
| **3. Determinism**         | **PASS**        | Unconditional global well-posedness, all d <= 3     |
| **4. Gen. Sufficiency**    | CONDITIONAL (weak) | Generates all exact laws; gap only on sharp exponents |
| **5. Envelope Tightness**  | **PASS**        | All 9 components tight, no open face               |
| **6. Structural Optimality** | CONDITIONAL   | No anomalies, but non-minimal constitutive axioms  |

### 7.2 Comparison with NS and ED

| Criterion             | ED           | CH                  | NS (2D)        | NS (3D)           |
|-----------------------|--------------|---------------------|-----------------|--------------------|
| Minimality            | PASS         | FAIL                | FAIL            | FAIL               |
| Locality              | PASS         | **PASS**            | CONDITIONAL     | CONDITIONAL        |
| Determinism           | PASS (trivial)| **PASS**           | PASS            | FAIL               |
| Gen. Sufficiency      | PASS         | CONDITIONAL (weak)  | CONDITIONAL     | CONDITIONAL        |
| Envelope Tightness    | PASS         | **PASS**            | PASS            | CONDITIONAL        |
| Structural Optimality | PASS         | CONDITIONAL         | FAIL            | FAIL               |

### 7.3 Architectural Summary

The Cahn–Hilliard architecture is the *most structurally sound PDE system* evaluated in the PDE Atlas. It passes three of six AD criteria outright (Locality, Determinism, Envelope Tightness), achieves weak conditional verdicts on two (Generative Sufficiency, Structural Optimality), and fails only on Minimality — the same criterion that every constitutively closed PDE system fails.

The architecture's structural strength traces to two features acting in concert: the *gradient-flow structure* (CH-4), which provides an exact Lyapunov functional and forbids energy growth, limit cycles, and chaos; and the *fourth-order biharmonic smoothing* (arising from CH-3 + CH-5), which controls the cubic nonlinearity in all dimensions d <= 3 and provides unconditional regularity.

The CH architecture has *no structural anomalies* — no nonlocal channel, no destabilizing sub-channel, no open envelope face, no dimensional bifurcation. It is the only PDE architecture in the PDE Atlas that matches ED's anomaly-free status. The sole architectural gap between CH and ED is that ED is axiomatically minimal (its structure is forced by the fundamental theorem of arithmetic) while CH carries constitutive selections (the specific free energy, mobility, and geometry).

### 7.4 Composite Verdict

The Cahn–Hilliard equation is an architecturally coherent, fully local, unconditionally deterministic, anomaly-free gradient-flow PDE — the closest dynamical analogue to the static structural perfection of the Factor Skyline, and the benchmark against which all other PDE architectures in the PDE Atlas should be measured.

---

*End of AD Criteria and Verdict. This completes the AD architectural evaluation of the Cahn–Hilliard equation.*
