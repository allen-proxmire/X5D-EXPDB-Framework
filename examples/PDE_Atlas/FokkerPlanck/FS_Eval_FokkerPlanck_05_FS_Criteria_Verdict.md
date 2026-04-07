# AD Evaluation: Fokker–Planck Equation — AD Criteria and Verdict

Allen Proxmire

April 2026

---

## Overview

This file applies the six AD evaluation criteria to the Fokker–Planck equation as characterized in Modes 1–3. The FP evaluation reveals an architecture that achieves its structural soundness through a mechanism fundamentally different from every other PDE in the Atlas: *linearity*. Where AC uses the maximum principle, CH uses fourth-order smoothing, PME uses degenerate entropy dissipation, and TFE uses the cooperation of fourth-order and degeneracy, the FP equation needs none of these — its linearity alone provides unconditional well-posedness, closure, and stability. The FP evaluation tests whether linearity, as a closure mechanism, produces an FS profile comparable to the nonlinear mechanisms that close the other architectures.

Throughout, we reference the axioms FP-1 through FP-8, the envelope inequalities E1–E10, the universal inequalities U1–U10, and the channel constraints C1–C12 established in the preceding files.

---

## 1. Minimality

**Question:** Do the FP axioms form a minimal architectural set?

### 1.1 Assessment of Individual Axioms

**FP-1 (Continuum / Probability Density).** *Minimal within paradigm.* The probability-density interpretation is the defining semantic commitment of the FP architecture. It distinguishes FP from generic parabolic PDEs (which might describe temperature, concentration, or height rather than probability). Removing it collapses the probabilistic interpretation. **Minimal within paradigm.**

**FP-2 (Locality).** *Minimal.* Defines the PDE paradigm. Independent of all other axioms. **Minimal.**

**FP-3 (Drift–Diffusion Decomposition).** *Minimal.* This is the defining structural commitment of the FP architecture — the two-channel (first-order drift + second-order diffusion) structure that distinguishes FP from all other evaluated PDEs. Neither channel is derivable from the other: drift without diffusion gives the continuity equation; diffusion without drift gives the heat equation. The combination is the FP architecture. **Minimal.**

**FP-4 (Conservation / Normalization).** *Minimal.* The conservation of total probability (integral rho = 1) is an independent structural commitment. It follows from the divergence form of the PDE, but the divergence form is itself a structural choice — one could write a non-conservative drift-diffusion equation. Conservation is the axiom that links the PDE to probability theory. **Minimal.**

**FP-5 (Euclidean Geometry).** *Non-minimal.* The FP equation can be formulated on Riemannian manifolds (with the Laplace–Beltrami operator and covariant drift). The Euclidean restriction is a geometric simplification. **Non-minimal.**

**FP-6 (Forward Parabolic).** *Minimal within paradigm.* Required for well-posedness. The backward Kolmogorov equation is the adjoint — a different PDE with a different interpretation. **Minimal within paradigm.**

**FP-7 (No Reaction).** *Minimal as a structural commitment.* The absence of source/sink terms is the axiom that makes the FP equation probability-preserving. Adding a reaction term would break the probability interpretation (total probability would change). This axiom is the *probabilistic* version of the no-reaction axiom in PME/TFE. **Minimal.**

**FP-8 (Constitutive b and D).** *Non-minimal.* The specific drift field b(x) and diffusion tensor D(x) are constitutive selections — different physical systems correspond to different (b, D). The FP architecture requires *some* drift and diffusion but does not specify which. **Non-minimal (constitutive).**

### 1.2 Minimality Summary

| Axiom | Content                        | Minimal?        | Comment                             |
|-------|--------------------------------|-----------------|-------------------------------------|
| FP-1  | Probability density            | Within paradigm | Defines probabilistic interpretation|
| FP-2  | Locality                       | Yes             | Defines PDE paradigm                |
| FP-3  | Drift–diffusion decomposition  | Yes             | *Is* the architecture               |
| FP-4  | Conservation (integral = 1)    | Yes             | Links PDE to probability theory     |
| FP-5  | Euclidean geometry             | **No**          | Geometric simplification            |
| FP-6  | Forward parabolic              | Within paradigm | Required for well-posedness         |
| FP-7  | No reaction                    | Yes             | Probability-preserving              |
| FP-8  | Constitutive b, D              | **No**          | Constitutive selections             |

**Criterion 1 Verdict: CONDITIONAL.** The structural core (FP-2, FP-3, FP-4, FP-7) is fully minimal — four independent, irreducible axioms defining the drift-diffusion probability-density architecture. The non-minimal elements are FP-5 (Euclidean geometry) and FP-8 (specific b, D). This is the *same minimality profile* as PME and TFE (~1.5 non-minimal elements) and stronger than AC/CH/NS (3 non-minimal each).

---

## 2. Locality

**Question:** Is the FP architecture fully local?

### 2.1 Assessment

Every channel is local:

- **T (Drift):** -div(b rho) involves rho, nabla rho, and the prescribed b(x) at each point. Local.
- **D (Diffusion):** div(D nabla rho) involves rho, nabla rho, Delta rho, and D(x) at each point. Local.
- **C (Conservation):** Global integral, locally enforced through divergence form. No nonlocal solve.
- **P (Gradient flow, conditional):** F[rho] is a global functional, but the PDE is local.

No elliptic constraint, no Poisson equation, no Green's function, no integral operator. The FP architecture is fully local at both the formulation and solution levels.

### 2.2 Comparison

The FP shares the locality class of AC, CH, PME, TFE, and RD — all fully local. Only NS has a nonlocal channel. The FP's locality is *unconditional* — it holds for every choice of b and D, with no exceptions.

**Criterion 2 Verdict: PASS.** Fully local at both formulation and solution levels, for all constitutive parameters. No nonlocal channel.

---

## 3. Determinism

**Question:** Does the FP architecture uniquely determine the future from the initial data?

### 3.1 Assessment

The FP equation is a *linear* second-order parabolic PDE with prescribed coefficients. The well-posedness theory is the strongest available for any PDE:

- **Existence:** Global-in-time smooth solutions exist for all initial data rho_0 in L^1(Omega), rho_0 >= 0, integral rho_0 = 1, in all dimensions d >= 1. The existence follows from the standard theory of linear parabolic equations (Friedman, Ladyzhenskaya–Solonnikov–Uraltseva).

- **Uniqueness:** Solutions are unique in the class of integrable functions satisfying the PDE in the distributional sense. Uniqueness follows from the linearity: if rho_1 and rho_2 are two solutions, then rho_1 - rho_2 satisfies a homogeneous linear parabolic equation with zero initial data, and must be identically zero.

- **Positivity:** rho_0 >= 0 implies rho(t) >= 0 for all t > 0. Follows from the linear parabolic maximum principle.

- **Instantaneous regularization:** For t > 0, rho(t) is *real-analytic* (not just C^{infinity} but analytic). This is the strongest regularity available for any PDE — unique to linear parabolic equations with smooth coefficients.

- **Continuous dependence:** Solutions depend continuously on initial data in L^1, L^2, and Wasserstein metrics (for gradient drift: Wasserstein contractivity gives Lipschitz continuous dependence).

### 3.2 No Conditional Hypotheses

The FP well-posedness requires *no conditions* beyond smoothness of the coefficients b, D:
- No smallness condition.
- No dimensional restriction.
- No Serrin-class or BKM-type criterion.
- No conditional regularity.
- No parameter restriction (all b, D with D positive definite).

The linearity of the PDE makes the well-posedness *unconditionally unconditional* — the strongest determinism verdict possible.

### 3.3 Verdict

**Criterion 3 Verdict: PASS.** Unconditional global determinism — existence, uniqueness, positivity, analytic regularity, and continuous dependence — for all initial data, all dimensions d >= 1, and all constitutive parameters (b, D). The strongest determinism in the PDE Atlas, achieved through the simplest mechanism: linearity.

---

## 4. Generative Sufficiency

**Question:** Does the FP generate all of its observed laws from the axioms?

### 4.1 Generated Phenomena

| Phenomenon                              | Derivation Method                           |
|-----------------------------------------|---------------------------------------------|
| Gaussian spreading (b = 0)              | Explicit fundamental solution (heat kernel) |
| Drift-dominated transport               | Method of characteristics                    |
| Gibbs–Boltzmann equilibrium (b = -nabla V) | Stationary FP equation + normalization  |
| Exponential convergence to equilibrium  | Spectral theory + log-Sobolev inequality     |
| Entropy dissipation (H-theorem)         | Direct computation from PDE                  |
| Fisher information identity             | Differentiation of H-theorem                 |
| Wasserstein contractivity (convex V)    | Otto calculus / coupling methods             |
| Spectral decomposition                  | Self-adjoint operator theory                 |
| Moment evolution equations              | Integration of x^k times the PDE            |
| Positivity preservation                 | Linear maximum principle                     |
| Analytic regularization                 | Parametrix / heat kernel methods             |
| Log-Sobolev inequality (convex V)       | Bakry–Emery Gamma calculus                   |

The FP generates *every* observed phenomenon from its axioms. The theory is *provably complete* within the architecture's scope: every question about the qualitative and quantitative behavior of FP solutions has been answered by the linear parabolic theory + information-theoretic methods.

### 4.2 Phenomena FP Cannot Generate

| Phenomenon              | Reason for Absence                            |
|------------------------|-----------------------------------------------|
| Oscillations           | Linear PDE: no nonlinear feedback             |
| Turing patterns        | n = 1 species, no reaction                    |
| Traveling waves        | No bistable/monostable reaction               |
| Spiral waves           | n = 1, no reaction                            |
| Spatiotemporal chaos   | Linear semigroup: no sensitive dependence      |
| Phase separation       | No double-well potential                       |
| Turbulence             | No nonlinear self-advection                    |
| Blowup                 | Linear PDE: no nonlinear amplification         |
| Free boundaries        | Non-degenerate D: infinite propagation speed   |
| Coarsening             | No competing phases                            |

These absences are *structural consequences* of linearity and the drift-diffusion architecture, not failures of the theory. The FP is designed to model probability evolution, not pattern formation or turbulence.

### 4.3 Assessment

The FP is *completely generatively sufficient within its scope*. The scope is narrow (no nonlinear phenomena) but *perfectly covered* — every phenomenon within the scope is rigorously derived. The generative gap is *zero*: no FP phenomenon requires assumptions beyond the axioms.

This is the same verdict as the PME (zero generative gap within scope). The FP achieves it through a different mechanism: the PME's completeness comes from the self-similar reduction and the Barenblatt attractor theorem; the FP's completeness comes from the *spectral theory of linear operators*, which provides exact eigenfunction expansions and explicit convergence rates.

**Criterion 4 Verdict: PASS.** Zero generative gap within the architecture's scope. Complete theory: every phenomenon rigorously derived from the axioms.

---

## 5. Envelope Tightness

**Question:** Is the FP envelope closed and tight?

### 5.1 Assessment

**E1 (Mass conservation).** Exact identity. **Tight.**

**E2 (Positivity).** The linear maximum principle. **Tight** (sharp: equality when rho_0 touches zero at a point).

**E3 (Entropy dissipation).** Exact identity dH/dt = -I. **Tight.**

**E4 (Fisher information).** Exact identity. **Tight.**

**E5 (Log-Sobolev inequality).** Sharp: the Gaussian (Ornstein–Uhlenbeck) case saturates the inequality with equality in the limiting sense. The constant 1/(2 lambda) is optimal for lambda-convex V. **Tight.**

**E6 (Poincare / spectral gap).** Sharp: the spectral gap lambda_1 is the exact asymptotic convergence rate. **Tight.**

**E7 (Exponential convergence).** Rates are sharp: lambda_1 for L^2, 2 lambda for entropy, lambda for Wasserstein. Each rate is achieved by initial data concentrated on the corresponding eigenfunction (for spectral gap) or at the edge of the convexity basin (for Wasserstein). **Tight.**

**E8 (Gaussian smoothing).** Sharp estimates: the heat kernel bounds are optimal. **Tight.**

**E9 (Drift–diffusion energy balance).** Exact identity for the L^2 evolution. **Tight.**

**E10 (Wasserstein contractivity).** Sharp: the rate lambda equals the convexity constant of V, which cannot be improved. **Tight.**

### 5.2 Closure

The FP envelope is *fully closed* with no open faces:

1. **Linearity** seals the blowup, oscillation, and chaos faces (linear PDEs cannot blow up, oscillate nonlinearly, or exhibit chaos).
2. **Positivity** (linear maximum principle) seals the negativity face.
3. **Conservation** (divergence form) seals the mass face.
4. **Non-degeneracy** (D > 0) means there is no degeneracy face to seal.
5. **Entropy dissipation** (for gradient drift) provides the convergence guarantee.

The closure is *unconditionally parameter-independent*: it holds for all (b, D) with D positive definite.

### 5.3 Verdict

**Criterion 5 Verdict: PASS.** All ten envelope components are tight. The envelope is fully closed with no open faces, sealed by linearity + positivity + conservation + non-degeneracy. The closure is parameter-independent. This is the tightest envelope of any *drift-containing* PDE in the Atlas.

---

## 6. Structural Optimality

**Question:** Is the FP architecture optimal?

### 6.1 Anomaly Assessment

The FP has *zero* structural anomalies:

- **No nonlocal channel.** All channels local.
- **No destabilizing sub-channel.** The drift T is linear (cannot produce unbounded amplification); the diffusion D is stabilizing.
- **No oscillatory face.** Linearity prevents nonlinear oscillation; gradient-flow structure (when present) prevents limit cycles.
- **No chaotic face.** Linear semigroup — no sensitive dependence.
- **No blowup face.** Linear parabolic PDE — global smooth solutions.
- **No degeneracy face.** D > 0 everywhere — no free boundaries, no compact support.
- **No positivity face.** Linear maximum principle — rho >= 0 unconditionally.

Zero anomalies for *all* constitutive parameters. This is the *unconditionally strongest* anomaly-free verdict in the Atlas among dynamical PDEs.

### 6.2 Structural Economy

The FP achieves closure through the *most economical mechanism*: linearity alone. Compare the closure mechanisms across the Atlas:

| Architecture | Closure Mechanism(s)                         | Count | Mechanism Type |
|-------------|----------------------------------------------|-------|----------------|
| **FP**      | **Linearity**                               | **1** | **Structural** |
| AC          | Maximum principle + Lyapunov                 | 2     | Nonlinear      |
| CH          | Fourth-order smoothing + Lyapunov            | 2     | Nonlinear      |
| PME         | Degeneracy + entropy + L^1 contraction + conservation | 4 | Nonlinear |
| TFE (n>=1)  | Fourth-order + degeneracy + conservation + Lyapunov | 4 | Nonlinear |

FP uses *one* mechanism where PME and TFE use four. The linearity is the *minimum-cost closure*: it provides everything that the nonlinear mechanisms provide (existence, uniqueness, regularity, stability, convergence) at zero structural cost beyond the linearity axiom itself.

### 6.3 Optimality Within the Drift-Diffusion Class

The FP is the *canonical minimal member* of the drift-diffusion class. Extensions include:

- **Nonlinear FP (McKean–Vlasov):** b = b[rho] (density-dependent drift). Adds self-interaction. No longer linear.
- **FP with reaction:** partial_t rho = -div(b rho) + div(D nabla rho) + R(rho). Adds creation/destruction. Breaks probability conservation.
- **Fractional FP:** Replace Delta with (-Delta)^s. Adds nonlocal diffusion. Breaks locality.
- **Degenerate FP (Kramers):** D degenerates in some directions. Adds hypoellipticity.
- **Kinetic FP:** Phase-space (x, v) formulation. Adds velocity variable and Hamiltonian structure.

All extensions add channels, complexity, and structural challenges. None is simpler. The FP is the *floor* of the drift-diffusion hierarchy.

### 6.4 Verdict

**Criterion 6 Verdict: PASS.** Zero anomalies for all parameters. Maximum structural economy (one closure mechanism: linearity). Canonical minimal member of the drift-diffusion class. No simpler architecture generates the same phenomenology.

---

## 7. FS Verdict Summary

### 7.1 Criteria Scorecard

| Criterion                  | Verdict         | Comment                                          |
|----------------------------|-----------------|--------------------------------------------------|
| **1. Minimality**          | CONDITIONAL     | ~1.5 non-minimal elements (FP-5, specific b/D)  |
| **2. Locality**            | **PASS**        | Fully local, all parameters                      |
| **3. Determinism**         | **PASS**        | Unconditional, all d, all b/D, analytic regularity |
| **4. Gen. Sufficiency**    | **PASS**        | Zero generative gap, provably complete theory    |
| **5. Envelope Tightness**  | **PASS**        | All 10 components tight, parameter-independent closure |
| **6. Structural Optimality** | **PASS**      | Zero anomalies, one-mechanism closure, minimal in class |

**Score: 5 PASS + 1 CONDITIONAL** — matching the PME's score, the highest of any PDE in the Atlas.

### 7.2 Comparison Across the PDE Atlas

| Criterion             | ED   | FP         | PME        | AC         | CH         | TFE (n>=1) | NS (3D)  | RD        |
|-----------------------|------|------------|------------|------------|------------|------------|----------|-----------|
| Minimality            | PASS | COND.      | COND.      | FAIL       | FAIL       | COND.      | FAIL     | COND.     |
| Locality              | PASS | **PASS**   | **PASS**   | **PASS**   | **PASS**   | **PASS**   | COND.    | **PASS**  |
| Determinism           | PASS | **PASS**   | **PASS**   | **PASS**   | **PASS**   | **PASS**   | FAIL     | COND.     |
| Gen. Sufficiency      | PASS | **PASS**   | **PASS**   | COND.(w)   | COND.(w)   | **PASS**   | COND.    | **PASS**  |
| Envelope Tightness    | PASS | **PASS**   | **PASS**   | **PASS**   | **PASS**   | **PASS**   | COND.    | COND.     |
| Structural Optimality | PASS | **PASS**   | **PASS**   | COND.      | COND.      | **PASS**   | FAIL     | COND.     |
| **Total PASS**        | **6**| **5**      | **5**      | **3**      | **3**      | **4**      | **0**    | **2**     |

FP and PME *tie* for the strongest FS profile among dynamical PDEs. Both achieve 5 PASSes + 1 CONDITIONAL, failing only on Minimality (due to geometric simplification and constitutive parameters).

### 7.3 Architectural Summary

The Fokker–Planck equation achieves the joint-strongest FS profile of any PDE in the Atlas, tying with the Porous Medium Equation at 5 PASSes + 1 CONDITIONAL. The two architectures achieve this score through *completely different mechanisms*:

- **PME:** Nonlinear degenerate diffusion. Closure by four cooperating nonlinear mechanisms (degeneracy, entropy, L^1 contraction, conservation). One dynamical channel. Free-boundary geometry. Self-similar Barenblatt attractor.

- **FP:** Linear drift-diffusion. Closure by a single mechanism: linearity. Two dynamical channels (drift + diffusion). No free boundary. Gibbs–Boltzmann attractor.

The PME is the *structurally soundest nonlinear PDE*. The FP is the *structurally soundest linear PDE*. Together, they define the upper boundary of structural soundness in the PDE Atlas — one from the nonlinear side, one from the linear side.

The FP's structural advantage is *analytical tractability*: spectral decomposition, closed-form solutions, exact convergence rates, and the full power of linear operator theory. Its structural limitation is *dynamical poverty*: linearity excludes oscillations, patterns, chaos, free boundaries, phase separation, and turbulence. The FP trades dynamical richness for analytical control — the extreme end of the constraint-universality trade-off that runs through the entire Atlas.

The FP's deepest structural contribution to the Atlas is the demonstration that *linearity alone is a complete closure mechanism*. Every other closed architecture needs nonlinear tools (maximum principles, Lyapunov functionals, degenerate comparison). FP shows that these tools, powerful as they are, are *not necessary* for closure — linearity suffices. This identification of linearity as a stand-alone closure mechanism is a new structural insight of the AD evaluation framework.

### 7.4 Composite Verdict

The Fokker–Planck equation is the structurally soundest linear PDE in the PDE Atlas — a fully local, unconditionally deterministic, analytically complete, anomaly-free drift-diffusion architecture that achieves maximum structural closure through linearity alone, producing the explicit Gibbs–Boltzmann equilibrium as the universal attractor of probability-density evolution and standing as the stochastic mirror of the Event Density framework's static arithmetic perfection.

---

*End of AD Criteria and Verdict. This completes the AD architectural evaluation of the Fokker–Planck Equation.*
