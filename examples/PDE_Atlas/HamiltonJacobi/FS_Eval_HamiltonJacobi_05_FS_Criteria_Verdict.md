# AD Evaluation: Hamilton–Jacobi Equation — AD Criteria and Verdict

Allen Proxmire

April 2026

---

## Overview

This file applies the six AD evaluation criteria to the Hamilton–Jacobi equation as characterized in Modes 1–3. The HJ evaluation introduces a new structural paradigm to the AD framework: *variational closure without dissipation*. Every previous architecture achieves closure through some form of smoothing or energy decrease; HJ achieves closure through *convexity of the Hamiltonian* and the *viscosity-solution selection principle* — two tools with no smoothing content whatsoever. The HJ verdicts test whether this non-dissipative, hyperbolic closure mechanism produces an FS profile comparable to the dissipative closures of the parabolic architectures.

Throughout, we reference the axioms HJ-1 through HJ-8, the envelope inequalities E1–E10, the universal inequalities U1–U10, and the channel constraints C1–C12 established in the preceding files.

---

## 1. Minimality

**Question:** Do the HJ axioms form a minimal architectural set?

### 1.1 Assessment of Individual Axioms

**HJ-1 (Scalar Potential).** *Minimal within paradigm.* The scalar field u is the state variable. Removing it eliminates the PDE framework. The gradient-centric interpretation (nabla u is the physical quantity) is a structural property, not an additional axiom. **Minimal within paradigm.**

**HJ-2 (Locality).** *Minimal.* Defines the PDE paradigm. Independent of all other axioms. **Minimal.**

**HJ-3 (First-Order Nonlinear Law).** *Minimal.* The law partial_t u + H(nabla u) = 0 is the defining equation. It is the simplest local, nonlinear, hyperbolic evolution for a scalar potential. Removing or replacing it changes the architecture entirely. **Minimal — this axiom *is* the architecture.**

**HJ-4 (Convex Hamiltonian).** *Minimal for the standard theory.* Convexity is the *structural requirement* for the comparison principle, Hopf–Lax formula, and uniqueness of viscosity solutions. It is not a constitutive selection (choosing a specific H from a family) but a *structural condition* on the class of admissible Hamiltonians. Without convexity, the viscosity-solution theory weakens dramatically (possible non-uniqueness, loss of comparison). **Minimal — required for closure.**

**HJ-5 (Euclidean Geometry).** *Non-minimal.* HJ can be formulated on Riemannian manifolds. The Euclidean restriction is a geometric simplification. **Non-minimal.**

**HJ-6 (Hyperbolic Orientation).** *Derived.* The hyperbolic character (finite-speed propagation, characteristics) is a *consequence* of HJ-3 (first-order nonlinear law), not an independent axiom. First-order PDEs are automatically hyperbolic — the hyperbolicity does not need to be imposed separately. **Redundant (derived from HJ-3).**

**HJ-7 (No Diffusion, No Reaction).** *Minimal.* The absence of diffusion and reaction is a *deliberate structural commitment* that isolates the pure first-order nonlinear transport. Adding diffusion produces the viscous HJ equation (a different architecture); adding reaction produces HJ–Bellman (a different architecture). The no-diffusion axiom is what makes HJ hyperbolic rather than parabolic — it is the single most consequential structural choice. **Minimal.**

**HJ-8 (Viscosity-Solution Framework).** *Minimal for global well-posedness.* The viscosity-solution concept is *not* an optional analytical convenience — it is a *structural requirement* for the architecture to be well-posed past gradient blowup. Without it, the HJ equation has no unique global solution. The viscosity framework is to HJ what the Leray–Hopf weak-solution theory is to NS: the extension of the solution concept needed to make the architecture globally defined. **Minimal — required for global well-posedness.**

### 1.2 Minimality Summary

| Axiom | Content                     | Minimal?    | Comment                              |
|-------|-----------------------------|-------------|--------------------------------------|
| HJ-1  | Scalar potential            | Within paradigm | Defines state variable           |
| HJ-2  | Locality                    | Yes         | Defines PDE paradigm                 |
| HJ-3  | partial_t u + H(nabla u) = 0 | Yes       | *Is* the architecture                |
| HJ-4  | Convex Hamiltonian          | Yes         | Required for closure                 |
| HJ-5  | Euclidean geometry          | **No**      | Geometric simplification             |
| HJ-6  | Hyperbolic orientation      | Redundant   | Derived from HJ-3                    |
| HJ-7  | No diffusion, no reaction   | Yes         | Isolates pure transport              |
| HJ-8  | Viscosity-solution framework| Yes         | Required for global well-posedness   |

**Structural core:** Six minimal axioms (HJ-1 paradigm, HJ-2, HJ-3, HJ-4, HJ-7, HJ-8). One non-minimal (HJ-5). One redundant (HJ-6).

**Criterion 1 Verdict: CONDITIONAL.** The structural core (six axioms) is fully minimal — the *largest minimal core* of any architecture in the Atlas (tied with MCF's five-axiom core, if we count HJ-1 and HJ-8 as paradigm-level). The single non-minimal element is the Euclidean geometry restriction (HJ-5). One axiom is redundant (HJ-6, derived from HJ-3).

Like MCF, HJ has *zero constitutive parameters*: the equation partial_t u + H(nabla u) = 0 has no adjustable coefficient (no epsilon, no nu, no D, no m, no n). The convexity of H is a *structural condition*, not a parameter. HJ and MCF are the only two architectures in the Atlas with zero constitutive parameters — the *parameter-free* architectures.

---

## 2. Locality

**Question:** Is the HJ architecture fully local?

### 2.1 Assessment

The HJ velocity law V = -H(nabla u) depends only on nabla u at each point:

- **T (Transport):** H(nabla u) is a pointwise function of nabla u. Local.
- **S (Steepening):** Gradient blowup is a local phenomenon (characteristics converge locally). Local trigger.
- **V (Viscosity):** The viscosity-solution concept is *locally defined* (comparison with test functions at each point). The comparison principle has global consequences but local definition.

No elliptic constraint, no Poisson equation, no Green's function, no integral operator, no pressure coupling. The HJ architecture is fully local at the formulation level.

### 2.2 Comparison

HJ shares the locality class of AC, CH, PME, TFE, FP, RD, and MCF — all fully local. Only NS has a nonlocal channel.

**HJ's locality is particularly significant** because the architecture is *hyperbolic*: information propagates at finite speed along characteristics, respecting a strict domain-of-dependence constraint. This is *stronger* than the locality of parabolic architectures (which have infinite propagation speed for non-degenerate diffusion) — HJ not only has no nonlocal operator, it also has *finite-speed* information propagation.

**Criterion 2 Verdict: PASS.** Fully local at formulation level. Finite-speed propagation (stronger than parabolic locality). No nonlocal channel.

---

## 3. Determinism

**Question:** Does the HJ architecture uniquely determine the future from the initial data?

### 3.1 Assessment

The viscosity-solution theory provides *unconditional global determinism* for the HJ equation:

- **Existence:** For any Lipschitz initial data u_0, a viscosity solution exists for all t >= 0. Existence is constructive: the Hopf–Lax formula gives the solution explicitly for convex H on R^d.

- **Uniqueness:** For convex H, the viscosity solution is unique. Uniqueness follows from the *comparison principle*: if u is a subsolution and v is a supersolution with u(0) <= v(0), then u(t) <= v(t) for all t.

- **Continuous dependence:** The L^{infinity} contraction ||u(t) - v(t)||_{L^inf} <= ||u_0 - v_0||_{L^inf} provides Lipschitz continuous dependence on initial data.

- **Regularity:** The viscosity solution is Lipschitz continuous (nabla u bounded in L^{infinity}) and semiconcave (D^2 u <= C/t) for all t > 0. The solution is *not* C^1 in general (gradient discontinuities at shocks).

### 3.2 The Role of Gradient Blowup

The gradient blowup at time T* does *not* break determinism:

- **Before T*:** The classical (smooth) solution exists and is unique. Determinism is classical.
- **At T*:** The smooth solution ceases to exist (nabla u develops a jump). But the viscosity solution continues *uniquely* through the singularity.
- **After T*:** The viscosity solution exists, is unique, and is Lipschitz continuous. The solution is determined for all t >= 0.

The gradient blowup is a *regularity event*, not a *well-posedness event*. The solution exists and is unique at all times — it just changes regularity class (from C^1 to Lipschitz) at the shock time. Determinism is preserved throughout.

**Comparison with NS and MCF:**

| Architecture | Singularity              | Determinism Past Singularity  |
|-------------|--------------------------|-------------------------------|
| NS (3D)    | Open (vorticity blowup?) | Open (weak solutions not unique?) |
| MCF         | Certain (curvature blowup)| Conditional (surgery/level-set unique) |
| **HJ**      | **Certain (gradient blowup)** | **Unconditional (viscosity unique)** |

HJ has the *strongest determinism* among architectures with singularities: the singularity is certain, and the continuation is unconditionally unique. NS has an open question about both singularity and continuation. MCF has certain singularity with unique continuation through surgery/level-set, but the continuation theory is more complex than HJ's viscosity framework.

### 3.3 Verdict

**Criterion 3 Verdict: PASS.** Unconditional global determinism — existence, uniqueness, and continuous dependence for all Lipschitz initial data, in all dimensions, for all convex H. The viscosity-solution framework provides unique solutions for all time, including through gradient singularities. The determinism is *not conditional* on regularity (unlike NS) — it holds whether or not the solution is smooth.

---

## 4. Generative Sufficiency

**Question:** Does the HJ generate all of its observed phenomena from the axioms?

### 4.1 Generated Phenomena

| Phenomenon                              | Derivation Method                            |
|-----------------------------------------|----------------------------------------------|
| Finite-time gradient blowup             | Characteristic crossing (explicit computation)|
| Shock-formation time T* = 1/max(-u_0'') | Characteristic convergence analysis          |
| Viscosity-solution continuation         | Crandall–Lions theory (comparison principle) |
| Hopf–Lax variational formula            | Legendre transform + inf-convolution         |
| Semiconcavity for t > 0                 | Structure of Hopf–Lax formula               |
| Oleinik one-sided gradient bound        | Entropy condition + characteristics          |
| L^{infinity} contraction                | Comparison principle (Crandall–Lions)        |
| Lipschitz propagation                   | Maximum principle for gradients              |
| Finite-speed propagation                | Characteristic cone (hyperbolicity)          |
| Long-time paraboloid asymptotics        | Hopf–Lax formula, t → infinity              |
| Entropy/viscosity selection             | Vanishing-viscosity limit                    |
| Nonlinear semigroup structure           | Viscosity-solution theory                    |

The HJ generates *all* of its characteristic phenomena from the axioms. The theory is *provably complete*: every question about the qualitative behavior of viscosity solutions of HJ with convex H has been answered.

### 4.2 Phenomena HJ Cannot Generate

| Phenomenon              | Reason for Absence                        |
|------------------------|-------------------------------------------|
| Smoothing              | No diffusion (HJ-7) — the architecture steepens, never smooths |
| Oscillations           | Comparison principle → monotone dynamics  |
| Patterns               | No reaction, single species               |
| Chaos                  | L^{infinity} contraction → Lipschitz stability |
| Phase separation       | No double-well potential                   |
| Coarsening             | No conserved bulk quantity                 |
| Turbulence             | No self-advection, no vector field         |
| Free boundaries        | No degeneracy (non-degenerate transport)   |
| Topology change        | No geometric state variable                |

### 4.3 Assessment

HJ is *completely generatively sufficient within its scope*: the theory of viscosity solutions for first-order HJ equations with convex Hamiltonians is among the most complete in PDE theory. Every phenomenon — gradient blowup, shock formation, variational representation, semiconcavity, long-time asymptotics, entropy selection — is rigorously derived from the axioms with zero gap.

The scope is deliberately narrow (no smoothing, no oscillation, no patterns) but *perfectly covered*. Like PME and FP, the HJ achieves zero generative gap by restricting its scope to a domain where the theory is complete.

**Criterion 4 Verdict: PASS.** Zero generative gap within the architecture's scope. Complete theory: every phenomenon rigorously derived. The viscosity-solution theory for convex HJ is one of the most complete PDE theories in mathematics.

---

## 5. Envelope Tightness

**Question:** Is the HJ envelope closed and tight?

### 5.1 Assessment of Envelope Components

**E1 (Comparison principle).** Exact structural property. Sharp (equality iff u_0 = v_0). **Tight.**

**E2 (Lipschitz propagation).** Sharp: ||nabla u(t)||_{L^inf} <= ||nabla u_0||_{L^inf}, with equality for convex u_0 (no shock). **Tight.**

**E3 (Semiconcavity).** Sharp: D^2 u <= C/t with optimal constant C depending on H. Achieved by specific solutions. **Tight.**

**E4 (Finite-speed propagation).** Sharp: the characteristic cone has the exact opening angle determined by ||nabla u_0||_{L^inf}. **Tight.**

**E5 (Hopf–Lax formula).** Exact: an equality, not an inequality. **Tight.**

**E6 (Oleinik bound).** Sharp: u_x <= 1/t (in 1D) is achieved by the solution with u_0(x) = -|x|. **Tight.**

**E7 (Shock-formation time).** Sharp: T* = 1/max(-u_0'') is the exact shock time (achieved by initial data with the specified concavity). **Tight.**

**E8 (Entropy admissibility).** Exact characterization of the viscosity solution as the vanishing-viscosity limit. **Tight.**

**E9 (Sup-convolution stability).** Exact: u^delta → u uniformly. **Tight.**

**E10 (L^{infinity} contraction).** Sharp: ||u(t) - v(t)||_{L^inf} <= ||u_0 - v_0||_{L^inf}, with equality for non-interacting solutions (supports separated by more than the characteristic speed times t). **Tight.**

### 5.2 The Required Regularity-Loss Face

The HJ envelope includes a *required regularity-loss face*: the transition from C^1 to Lipschitz at the shock time T*. This face is:

- **Required:** Characteristics cross for generic data.
- **Resolved:** Viscosity solutions provide unique, stable continuation.
- **Permanent:** The solution remains Lipschitz (not C^1) for all t > T*.

The regularity-loss face is *not an open face* in the sense that the NS enstrophy face is open (where existence/uniqueness of solutions is uncertain). The HJ regularity-loss face is *fully controlled*: the solution exists, is unique, and is stable — it simply has lower regularity than the initial data.

### 5.3 Closure Mechanisms

The HJ envelope is sealed by four mechanisms:

1. **Convexity of H:** Provides the comparison principle (uniqueness).
2. **Viscosity-solution framework:** Provides existence and continuation past shocks.
3. **L^{infinity} contraction:** Provides stability.
4. **Hopf–Lax formula:** Provides explicit variational representation.

These four mechanisms are *non-dissipative* — none involves energy decrease, entropy production, or gradient damping. The closure is *variational* (cost minimization) rather than *dissipative* (energy decrease).

### 5.3 Verdict

**Criterion 5 Verdict: PASS.** All ten envelope components are tight. The envelope is fully closed within the viscosity-solution framework. The regularity-loss face is required but fully resolved (not open or uncertain). The closure is achieved through convexity + viscosity rather than dissipation — a *new closure mode* unique to HJ in the Atlas.

---

## 6. Structural Optimality

**Question:** Is the HJ architecture optimal?

### 6.1 Anomaly Assessment

HJ has *zero* structural anomalies:

- **No nonlocal channel.** All channels local. Finite-speed propagation.
- **No destabilizing sub-channel (in the anomalous sense).** The steepening channel S is *destabilizing* (produces gradient blowup) but is *not anomalous*: it is the inevitable, predictable, fully classified consequence of first-order nonlinear transport without diffusion. The gradient blowup is *certain and resolved*, not open or uncontrolled.
- **No oscillatory face.** Comparison principle → monotone dynamics.
- **No chaotic face.** L^{infinity} contraction → Lipschitz stability.
- **No amplitude blowup.** u and nabla u remain bounded in L^{infinity} for all time.
- **No unresolved singularity.** The gradient blowup is certain, and the viscosity solution provides unique continuation.

The gradient blowup is a *structural feature*, not an anomaly. It is the architecture's mechanism for resolving characteristic crossing — the inevitable consequence of the axioms, fully understood and completely controlled.

### 6.2 Structural Economy

HJ achieves closure with the *fewest structural resources* of any architecture in the Atlas:

- **Zero constitutive parameters** (tied with MCF).
- **Three channels** (tied with MCF for fewest).
- **Zero dissipation mechanisms** (unique — every other closed architecture has at least one).
- **One generating equation:** partial_t u + H(nabla u) = 0 (the shortest PDE specification in the Atlas, tied with MCF's V_n = H).
- **One closure mechanism:** convexity + viscosity (the simplest closure — one structural condition on H, one solution concept).

No simpler first-order PDE can produce the HJ phenomenology. The linear transport equation (partial_t u + b . nabla u = 0) is simpler but has no shock formation and no nonlinear dynamics. The HJ equation is the *minimal nonlinear hyperbolic PDE* — the simplest equation that produces finite-time singularity from smooth data.

### 6.3 Comparison

| Feature                  | HJ          | MCF        | PME        | FP         | AC         | NS              |
|--------------------------|-------------|------------|------------|------------|------------|-----------------|
| Anomalies                | 0           | 0          | 0          | 0          | 0          | 2               |
| Constitutive parameters  | **0**       | **0**      | 1          | 2          | 3          | 2               |
| Channel count            | **3**       | **3**      | 4          | 4          | 4          | 5               |
| Dissipation mechanisms   | **0**       | 1 (area)   | 4          | 1 (entropy)| 2          | 1 (viscosity)   |
| Closure mechanism        | Convex.+visc.| Area diss.| Deg.+ent.+L^1+cons.| Linearity | Max.pr.+Lyap. | Open (3D) |
| Required singularity     | Yes (gradient)| Yes (curv.)| No       | No         | No         | Open            |

### 6.4 Verdict

**Criterion 6 Verdict: PASS.** Zero anomalies. Maximum structural economy (zero parameters, three channels, zero dissipation, one equation). No simpler architecture generates the same phenomenology. The gradient blowup is structural, not anomalous. HJ achieves the strongest structural optimality verdict tied with MCF — the two *parameter-free, minimal-channel* architectures.

---

## 7. FS Verdict Summary

### 7.1 Criteria Scorecard

| Criterion                  | Verdict         | Comment                                              |
|----------------------------|-----------------|------------------------------------------------------|
| **1. Minimality**          | CONDITIONAL     | 6 minimal axioms (largest core); HJ-5 non-minimal   |
| **2. Locality**            | **PASS**        | Fully local + finite-speed (strongest locality)      |
| **3. Determinism**         | **PASS**        | Unconditional via viscosity solutions (through shocks)|
| **4. Gen. Sufficiency**    | **PASS**        | Zero gap. Complete viscosity-solution theory.         |
| **5. Envelope Tightness**  | **PASS**        | All 10 tight. Variational closure. Regularity face resolved. |
| **6. Structural Optimality** | **PASS**      | Zero anomalies. Zero parameters. Zero dissipation.   |

**Score: 5 PASS + 1 CONDITIONAL** — tying FP and PME for the strongest PDE profile in the Atlas.

### 7.2 Comparison Across the PDE Atlas

| Criterion             | ED   | HJ         | FP         | PME        | MCF        | AC         | CH         | TFE(n>=1) | NS(3D)   | RD        |
|-----------------------|------|------------|------------|------------|------------|------------|------------|-----------|----------|-----------|
| Minimality            | PASS | COND.      | COND.      | COND.      | COND.      | FAIL       | FAIL       | COND.     | FAIL     | COND.     |
| Locality              | PASS | **PASS**   | **PASS**   | **PASS**   | **PASS**   | **PASS**   | **PASS**   | **PASS**  | COND.    | **PASS**  |
| Determinism           | PASS | **PASS**   | **PASS**   | **PASS**   | COND.      | **PASS**   | **PASS**   | **PASS**  | FAIL     | COND.     |
| Gen. Sufficiency      | PASS | **PASS**   | **PASS**   | **PASS**   | **PASS**   | COND.(w)   | COND.(w)   | **PASS**  | COND.    | **PASS**  |
| Envelope Tightness    | PASS | **PASS**   | **PASS**   | **PASS**   | COND.      | **PASS**   | **PASS**   | **PASS**  | COND.    | COND.     |
| Structural Optimality | PASS | **PASS**   | **PASS**   | **PASS**   | **PASS**   | COND.      | COND.      | **PASS**  | FAIL     | COND.     |
| **Total PASS**        | **6**| **5**      | **5**      | **5**      | **3**      | **3**      | **3**      | **4**     | **0**    | **2**     |

### 7.3 The Three 5-PASS Architectures

Three PDEs achieve the maximum PDE score of 5 PASS + 1 CONDITIONAL:

| Architecture | Closure Mode        | Singularity?  | Character     |
|-------------|---------------------|---------------|---------------|
| **FP**      | **Linear**          | None          | Parabolic     |
| **PME**     | **Dissipative**     | None          | Parabolic     |
| **HJ**      | **Variational**     | Gradient shock| Hyperbolic    |

These three architectures represent the *three fundamental closure modes* for PDEs:

1. **Linear closure (FP):** The PDE is linear → existence, uniqueness, and regularity follow from linear operator theory. The simplest closure, applicable only to linear equations.

2. **Dissipative closure (PME):** A Lyapunov functional decreases monotonically → existence follows from energy estimates, uniqueness from contraction, regularity from smoothing. The standard closure for nonlinear parabolic PDEs.

3. **Variational closure (HJ):** A convex Hamiltonian provides a comparison principle and a variational representation (Hopf–Lax) → existence follows from the variational formula, uniqueness from comparison, stability from L^{infinity} contraction. No dissipation, no smoothing, no Lyapunov. A *new closure mode* unique to HJ.

The three architectures exhaust the *fundamental modes of PDE closure*. Every other architecture in the Atlas uses one of these modes (or fails to close, as NS does in 3D): AC/CH use dissipative closure; TFE uses dissipative closure; MCF uses a hybrid of dissipative and geometric; RD is constitutive-dependent. HJ's contribution to the Atlas is the *discovery of the third closure mode*: variational closure without dissipation.

### 7.4 Architectural Summary

The Hamilton–Jacobi equation achieves the joint-strongest FS profile of any PDE in the Atlas, tying with the Fokker–Planck equation and the Porous Medium Equation at 5 PASSes + 1 CONDITIONAL. The three architectures achieve this score through *completely different closure mechanisms*:

- **FP:** Linearity (the simplest mechanism, but restricted to linear equations).
- **PME:** Dissipation (degeneracy + entropy + L^1 contraction + conservation — four cooperating mechanisms).
- **HJ:** Convexity + viscosity (the most economical mechanism — zero dissipation, zero constitutive parameters).

HJ's structural contribution is the demonstration that *closure does not require smoothing*. Every other closed architecture uses some form of smoothing (parabolic, geometric, or linear). HJ shows that convex variational structure alone — without any smoothing, without any energy decrease, without any diffusion — can produce a complete well-posedness theory for a nonlinear PDE with singularities. This is the deepest structural insight of the HJ evaluation.

HJ is the *anti-diffusion pole* of the Atlas: the point of maximum steepening, zero smoothing, and purely hyperbolic character. Together with FP (the diffusion pole) and PME (the nonlinear diffusion landmark), HJ completes the *three-point scaffold* of the PDE Atlas — the three architectures that define the extremes of well-posedness and structural soundness.

### 7.5 Composite Verdict

The Hamilton–Jacobi equation is the purest hyperbolic architecture in the PDE Atlas — a parameter-free, non-dissipative, fully local, variationally closed, first-order nonlinear transport equation that achieves unconditional global determinism through the viscosity-solution framework and convexity of the Hamiltonian, producing the first architecture in the Atlas whose structural closure requires no smoothing, no energy decrease, and no diffusion of any kind.

---

*End of AD Criteria and Verdict. This completes the AD architectural evaluation of the Hamilton–Jacobi Equation.*
