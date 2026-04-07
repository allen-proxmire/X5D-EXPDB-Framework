# AD Evaluation: Keller–Segel System — AD Criteria and Verdict

Allen Proxmire

April 2026

---

## Overview

This file applies the six AD evaluation criteria to the parabolic–elliptic Keller–Segel system as characterized in Modes 1–3. The KS evaluation is the *first nonlocal architecture* to receive a full FS verdict (NS was evaluated earlier but its nonlocality is a constraint-enforcement mechanism; the KS nonlocality is a dynamical driver). The KS verdicts test whether a *nonlocal aggregation architecture* — with its mass-concentrating blowup, nonlocal dissipation, and mass-bifurcated constraint surface — can achieve structural soundness comparable to the local architectures that dominate the 5-PASS tier.

The KS evaluation produces *mass-dependent verdicts*: the subcritical regime (M < 8 pi) is qualitatively different from the supercritical regime (M > 8 pi), and the verdicts reflect this bifurcation.

Throughout, we reference the axioms KS-1 through KS-10, the envelope inequalities E1–E10, the universal inequalities U1–U10, and the channel constraints C1–C12 established in the preceding files.

---

## 1. Minimality

**Question:** Do the KS axioms form a minimal architectural set?

### 1.1 Assessment of Individual Axioms

**KS-1 (Density u >= 0).** *Minimal within paradigm.* The non-negative density is the primary state variable. **Minimal.**

**KS-2 (Chemoattractant v).** *Derived.* The chemoattractant v is not an independent state variable — it is *slaved* to u through the Poisson equation -Delta v = u. Given u, v is uniquely determined. KS-2 is a consequence of KS-7 (nonlocal aggregation structure), not an independent axiom. **Redundant (derived from KS-7).**

**KS-3 (Diffusion Delta u).** *Minimal.* The diffusion is the stabilizing channel. Removing it produces a purely aggregating equation (u_t = -div(u nabla v), which blows up immediately for any nonzero mass). The diffusion is *necessary* for the architecture to have a nontrivial global-existence regime. **Minimal.**

**KS-4 (Chemotactic drift -div(u nabla v)).** *Minimal.* The chemotactic drift is the destabilizing channel — the defining mechanism of the KS architecture. Removing it gives the heat equation (pure diffusion). The drift is what makes KS different from FP/PME and produces the aggregation dynamics. **Minimal.**

**KS-5 (Chemoattractant dynamics -Delta v = u).** *Minimal.* The Poisson equation is the *nonlocal coupling mechanism* — the structural commitment that makes KS nonlocal. Replacing it with a local relation (e.g., v = u) would produce a local equation (u_t = Delta u - div(u nabla u)) — a different architecture (a type of porous-medium or Burgers-like equation, not chemotaxis). The elliptic coupling is what produces the *long-range attraction*. **Minimal — this is the nonlocality axiom.**

**KS-6 (Mass conservation).** *Derived.* Mass conservation follows from the divergence form of the u-equation: u_t = div(nabla u - u nabla v). With no-flux boundary conditions, integral u = const automatically. **Redundant (derived from KS-3 + KS-4).**

**KS-7 (Nonlocal aggregation).** *Structural consequence.* The nonlocal aggregation -div(u nabla(-Delta)^{-1} u) is the *combined effect* of KS-4 (drift) and KS-5 (Poisson equation). It is not an independent axiom but the structural consequence of the drift + elliptic coupling. **Redundant (derived from KS-4 + KS-5).**

**KS-8 (Blowup mechanism).** *Derived.* The blowup for M > 8 pi is a *consequence* of the axioms (diffusion + aggregation + Poisson coupling + mass conservation), not an additional assumption. It is proved from the free-energy analysis and the second-moment identity. **Redundant (derived).**

**KS-9 (Critical mass 8 pi).** *Derived.* The critical mass is the best constant in the log-HLS inequality — a *mathematical consequence* of the specific form of the Poisson equation in 2D. It is not imposed but computed. **Redundant (derived from KS-5 in 2D).**

**KS-10 (No Hamiltonian structure).** *Structural consequence.* The absence of Hamiltonian structure follows from the dissipative character of the equation (dF/dt <= 0). **Redundant (derived from the structure).**

### 1.2 Minimality Summary

| Axiom  | Content                     | Minimal?    | Comment                              |
|--------|-----------------------------|-------------|--------------------------------------|
| KS-1   | Density u >= 0              | Yes         | Primary state variable               |
| KS-2   | Chemoattractant v           | Redundant   | Derived from KS-5                    |
| KS-3   | Diffusion Delta u           | Yes         | Stabilizing channel                  |
| KS-4   | Chemotactic drift           | Yes         | Destabilizing channel                |
| KS-5   | Poisson equation -Delta v=u | Yes         | Nonlocality axiom                    |
| KS-6   | Mass conservation           | Redundant   | Derived from divergence form         |
| KS-7   | Nonlocal aggregation        | Redundant   | Derived from KS-4 + KS-5            |
| KS-8   | Blowup mechanism            | Redundant   | Derived from free-energy analysis    |
| KS-9   | Critical mass 8 pi          | Redundant   | Derived from log-HLS                 |
| KS-10  | No Hamiltonian              | Redundant   | Derived from dissipative structure   |

**Structural core:** Four minimal axioms (KS-1, KS-3, KS-4, KS-5). Six redundant (all derived from the core). Zero non-minimal constitutive selections.

The KS has a *remarkably small* structural core: four axioms — density, diffusion, chemotactic drift, and Poisson coupling — from which the entire theory (mass conservation, free energy, critical mass, blowup, quantization) is *derived*. No constitutive parameters (the diffusion coefficient and chemotactic sensitivity can be normalized to 1 by rescaling). No geometric simplification (the architecture is intrinsically 2D through the critical-mass phenomenon, though it is defined in any dimension).

**Criterion 1 Verdict: CONDITIONAL.** The structural core (four axioms) is fully minimal with zero constitutive parameters. The CONDITIONAL is due to six redundant axioms (all derived — the standard classification for architectures with harmless redundancies). The minimality is *substantively strong*: four axioms generate infinite structural consequences (free energy, critical mass, blowup, quantization) with zero adjustable parameters.

---

## 2. Locality

**Question:** Is the KS architecture fully local?

### 2.1 Assessment

The KS is *not fully local*. It has *two nonlocal channels*:

- **Channel A (Aggregation):** -div(u nabla v) with v = (-Delta)^{-1} u. The drift velocity nabla v at x depends on u(y) for all y through the Green's function. *Nonlocal.*
- **Channel N (Potential):** -Delta v = u → v(x) = -(1/(2 pi)) integral log|x - y| u(y) dy. The potential at x is a global integral of u. *Nonlocal.*

The diffusion channel D (Delta u) is local. But the aggregation mechanism — the *primary dynamical driver* — is nonlocal.

### 2.2 Comparison

| Architecture | Nonlocal Channels | Role of Nonlocality         |
|-------------|-------------------|-----------------------------|
| **KS**      | **2 (A, N)**      | **Primary mechanism (aggregation)** |
| NS          | 1 (P pressure)    | Constraint enforcement      |
| All others  | 0                 | N/A                         |

The KS is the *most nonlocal architecture* in the Atlas (2 nonlocal channels vs. NS's 1). Moreover, the KS nonlocality is *dynamically more consequential* than NS's: in NS, the pressure enforces a kinematic constraint (incompressibility) without doing net work; in KS, the chemoattractant *drives the dynamics* (aggregation) and *causes the blowup*. The KS nonlocality is a *force*; the NS nonlocality is a *constraint*.

**Criterion 2 Verdict: FAIL.** The KS architecture is *not fully local*. It has two nonlocal channels, and the nonlocality is the *primary dynamical mechanism*, not a secondary constraint. This is the first outright FAIL on Locality in the Atlas (NS received CONDITIONAL because its nonlocality is a constraint, not a driving force). The KS nonlocality is structurally deeper: it *drives* the aggregation, the blowup, and the entire mass-concentration program.

---

## 3. Determinism

**Question:** Does the KS architecture uniquely determine the future from the initial data?

### 3.1 Assessment by Mass Regime

**M < 8 pi (subcritical):**

- **Local well-posedness:** In L^p for p > 1 (and in H^s for appropriate s). Standard theory for advection-diffusion with smooth drift.
- **Global existence:** Unconditional. The log-HLS inequality bounds the free energy from below, providing uniform-in-time L^p estimates. The solution exists for all time, remains smooth, and converges to the unique steady state.
- **Uniqueness:** Unconditional in the energy class.
- **Continuous dependence:** In L^1, L^p, and Wasserstein metrics.

**Verdict for M < 8 pi: PASS.** Complete global determinism — existence, uniqueness, continuous dependence, smoothness, convergence to equilibrium.

**M = 8 pi (critical):**

- **Global existence:** Holds for most initial data (the critical mass does not blow up generically).
- **Uniqueness:** Unconditional.
- **Slow convergence:** The approach to the critical steady state is algebraic (not exponential).

**Verdict for M = 8 pi: PASS.** Global determinism with slow convergence.

**M > 8 pi (supercritical):**

- **Local existence:** Smooth solutions exist for a short time.
- **Finite-time blowup:** Certain — ||u(t)||_{L^inf} → infinity at some T* < infinity.
- **Uniqueness before blowup:** Solutions are unique in the smooth class up to T*.
- **Post-blowup continuation:** Measure-valued solutions exist (delta masses + regular part) but the *uniqueness of post-blowup continuation* is not fully established. The measure-valued framework provides a natural continuation, but the rigorous uniqueness theory is incomplete.

**Verdict for M > 8 pi: CONDITIONAL.** Determinism holds up to blowup (existence, uniqueness, continuous dependence for the smooth solution on [0, T*)). At and past blowup, the classical solution ceases to exist. Measure-valued continuation exists but uniqueness is not fully established. The CONDITIONAL reflects the *post-blowup ambiguity*.

### 3.2 Comparison

| Architecture | Determinism (subcritical/defocusing) | Determinism (supercritical/focusing) |
|-------------|--------------------------------------|---------------------------------------|
| **KS**      | **PASS (M < 8pi)**                  | **CONDITIONAL (M > 8pi, post-blowup uncertain)** |
| NLS         | PASS (defocusing)                    | CONDITIONAL (focusing d >= 2)        |
| HJ/Burgers  | PASS (entropy/viscosity solutions)  | PASS (entropy solutions unique)       |
| NS          | PASS (2D)                            | FAIL (3D, existence/uniqueness open)  |

The KS determinism profile is *structurally similar* to the NLS: both have PASS in the subcritical regime and CONDITIONAL in the supercritical. The difference: the NLS post-blowup is *unresolved* (no standard weak continuation); the KS post-blowup has a *natural continuation* (measure-valued solutions) whose *uniqueness* is partially but not fully established.

### 3.3 Overall Verdict

**Criterion 3 Verdict: CONDITIONAL (mass-dependent).**

| Mass Regime  | Determinism |
|-------------|-------------|
| M < 8 pi   | **PASS**    |
| M = 8 pi   | **PASS**    |
| M > 8 pi   | CONDITIONAL |

---

## 4. Generative Sufficiency

**Question:** Does the KS generate all of its observed phenomena from the axioms?

### 4.1 Generated Phenomena

| Phenomenon                              | Derivation Method                            |
|-----------------------------------------|----------------------------------------------|
| Diffusive spreading (subcritical)       | Standard parabolic theory + free-energy bound|
| Aggregation-driven concentration        | Free-energy analysis + second-moment identity|
| Finite-time blowup (M > 8 pi)         | Virial identity + log-HLS                    |
| Critical mass M = 8 pi                 | Best constant in log-HLS inequality          |
| Mass quantization at 8 pi             | Concentration-compactness analysis            |
| Multi-center aggregation               | Energy partition + mass counting              |
| Steady-state convergence (subcritical) | Free-energy minimization + spectral gap       |
| Blowup rate >= 1/(T* - t)             | Self-similar analysis                         |
| Blowup profile (rescaled Cauchy)       | Matched asymptotics + modulation theory       |
| Free-energy dissipation identity       | Direct computation from PDE                   |
| Second-moment identity dV/dt = 4M(1-M/(8pi)) | Direct computation                   |
| Measure-valued post-blowup continuation| Weak convergence + delta-mass tracking        |
| Log-HLS inequality                     | Variational analysis (sharp constant)         |

The KS generates *all* of its major phenomena from the axioms. The theory is *remarkably complete*:
- The critical mass 8 pi is *exactly computed* (from the log-HLS best constant).
- The blowup criterion is *exact* (M > 8 pi with finite second moment).
- The mass quantization is *proved* (concentration-compactness).
- The blowup profile is *characterized* (Type I and Type II classifications, active research but substantial progress).
- The subcritical steady state is *completely characterized*.

### 4.2 Phenomena KS Cannot Generate

| Phenomenon              | Reason for Absence                     |
|------------------------|----------------------------------------|
| Shocks                 | Diffusion prevents (KS-3)             |
| Dispersion / solitons  | No dispersive term (KS-10)            |
| Hamiltonian dynamics   | Dissipative (gradient flow)            |
| Integrability          | No Lax pair, no IST                    |
| Chaos                  | Gradient flow prevents (dF/dt <= 0)   |
| Turing patterns        | Instability not scale-selective        |

### 4.3 Assessment

The KS has a *small but non-negligible generative gap*:
- The *exact blowup rate* (Type I vs. Type II classification) is partially but not fully resolved for all initial data.
- The *uniqueness of post-blowup continuation* is not fully established.
- The *detailed dynamics at the critical mass M = 8 pi* (rate of convergence, stability of the critical steady state under perturbation) are largely but not completely characterized.

These gaps are *narrower* than the NS gap (where the existence of smooth solutions is open) but *wider* than the KdV gap (which is essentially zero). The KS generative gap is comparable to the NLS focusing gap (blowup dynamics partially characterized, post-blowup continuation open).

**Criterion 4 Verdict: CONDITIONAL (weak).** The KS generates all major phenomena from the axioms with exact critical-mass determination, exact blowup criterion, and proved mass quantization. The gap is small: incomplete blowup-type classification and unresolved post-blowup uniqueness. The CONDITIONAL is *weak* — the theory is substantially complete.

---

## 5. Envelope Tightness

**Question:** Is the KS envelope closed and tight?

### 5.1 Assessment

**E1 (Mass conservation).** Exact identity. **Tight.**
**E2 (Free-energy dissipation).** Exact identity. **Tight.**
**E3 (Log-HLS inequality).** Sharp: best constant M/(8 pi), equality for Cauchy distribution. **Tight.**
**E4 (Entropy-potential competition).** Sharp dichotomy at M = 8 pi. **Tight.**
**E5 (A priori bounds, M < 8 pi).** Derived from E3 + E4. Uniform L^p bounds. **Tight.**
**E6 (Second-moment identity).** Exact: dV/dt = 4M(1 - M/(8 pi)). **Tight.**
**E7 (Blowup criterion).** Sharp: M > 8 pi → blowup. **Tight.**
**E8 (Blowup rate).** Lower bound 1/(T* - t) established. Upper bound depends on type. **Partially tight.**
**E9 (Global existence, M < 8 pi).** Unconditional. **Tight.**
**E10 (Concentration-compactness).** Mass quantization at 8 pi proved. **Tight.**

### 5.2 Closure Assessment

**M < 8 pi:** The envelope is *fully closed*. Free-energy bounds + log-HLS + mass conservation provide complete control. All estimates tight. No open faces.

**M = 8 pi:** The envelope is *marginally closed*. Global existence holds; convergence is slow. The critical regime is at the boundary of the log-HLS inequality.

**M > 8 pi:** The envelope has an *open blowup face*. The blowup is certain, well-characterized (rate, profile, quantization), but the post-blowup continuation is not fully resolved. The open face is *well-characterized but present*.

### 5.3 Verdict

**Criterion 5 Verdict: CONDITIONAL (mass-dependent).**

| Mass Regime  | Envelope      |
|-------------|---------------|
| M < 8 pi   | **Fully closed (PASS)** |
| M = 8 pi   | Marginally closed (PASS) |
| M > 8 pi   | Open blowup face (CONDITIONAL) |

The subcritical envelope is the *tightest nonlocal envelope* in the Atlas — tighter than NS's enstrophy gap (which is unresolved), with a sharp threshold (8 pi) determined by a fundamental inequality. The supercritical envelope is well-characterized but has a genuine blowup face.

---

## 6. Structural Optimality

**Question:** Is the KS architecture optimal?

### 6.1 Anomaly Assessment

**M < 8 pi:**

- No shock anomalies (diffusion prevents steepening).
- No dispersive anomalies (no dispersion).
- No Hamiltonian anomalies (gradient flow).
- No chaotic anomalies (gradient flow prevents chaos).
- No blowup anomalies (subcritical: diffusion wins).
- **Two nonlocal channels** (structural feature, not anomaly in the standard sense — the nonlocality is the *defining mechanism* of the architecture).

**Zero anomalies for M < 8 pi** (the nonlocal channels are features, not defects).

**M > 8 pi:**

- All the above, plus:
- **One blowup face** — mass-concentrating singularity. The blowup is *certain, well-characterized, and driven by the architecture's defining mechanism* (nonlocal aggregation). It is a structural feature (like MCF's curvature blowup) rather than an anomaly (like NS's open regularity gap).

**One structural face for M > 8 pi** (blowup — well-characterized, not anomalous in the FS sense).

### 6.2 Structural Economy

The KS achieves its dynamics with *high structural economy*:
- **Four minimal axioms** (density, diffusion, drift, Poisson coupling).
- **Zero constitutive parameters** (diffusion and chemotactic coefficients normalized).
- **One conserved quantity** (mass M) that controls the *entire* dynamics.
- **One sharp threshold** (8 pi) derived from a fundamental inequality.
- **One free-energy functional** generating the complete well-posedness theory.

The structural amplification — from four axioms and one conserved quantity to the complete subcritical theory (global existence, steady-state convergence, sharp threshold, mass quantization) — is *comparable to the KdV's* amplification from seven axioms to infinite conservation laws. The KS achieves less (no integrability, no exact solvability) but from *fewer axioms*.

### 6.3 The Nonlocality Cost

The KS's *structural cost* is its nonlocality: two nonlocal channels (the most in the Atlas). This nonlocality is *necessary* for the architecture's defining phenomenology — without the Poisson coupling, the KS degenerates to a local equation without long-range attraction. The nonlocality is the *price of aggregation*.

No local architecture in the Atlas can produce mass-concentrating blowup driven by self-attraction — this requires the nonlocal potential. The KS's nonlocality is therefore *structurally necessary*, not gratuitous. But it is a *structural cost* that prevents a PASS on Locality (Criterion 2).

### 6.4 Verdict

**Criterion 6 Verdict: CONDITIONAL (mass-dependent).**

| Mass Regime  | Structural Optimality |
|-------------|----------------------|
| M < 8 pi   | CONDITIONAL (zero anomalies, but nonlocal channels are a structural cost) |
| M > 8 pi   | CONDITIONAL (one blowup face + nonlocal channels) |

The KS is structurally optimal *within the class of nonlocal aggregation PDEs* — no simpler nonlocal architecture produces the same phenomenology. But the nonlocality itself is a structural cost that distinguishes the KS from the fully local 5-PASS architectures.

---

## 7. FS Verdict Summary

### 7.1 Criteria Scorecard

| Criterion                  | M < 8 pi        | M > 8 pi        | Overall         |
|----------------------------|-----------------|-----------------|-----------------|
| **1. Minimality**          | CONDITIONAL     | CONDITIONAL     | CONDITIONAL     |
| **2. Locality**            | FAIL            | FAIL            | **FAIL**        |
| **3. Determinism**         | **PASS**        | CONDITIONAL     | CONDITIONAL     |
| **4. Gen. Sufficiency**    | CONDITIONAL (w) | CONDITIONAL (w) | CONDITIONAL (w) |
| **5. Envelope Tightness**  | **PASS**        | CONDITIONAL     | CONDITIONAL     |
| **6. Structural Optimality** | CONDITIONAL   | CONDITIONAL     | CONDITIONAL     |

**Overall Score: 0 PASS + 1 FAIL + 5 CONDITIONAL.**

For the *subcritical regime alone*: 2 PASS + 1 FAIL + 3 CONDITIONAL — a strong profile marred only by the Locality FAIL.

### 7.2 Comparison Across the PDE Atlas

| Criterion             | ED   | KdV  | FP   | PME  | HJ   | Burg.| NLS(d)| NLS(f1D)| MCF  | TFE  | AC   | CH   | **KS** | NS(3D)| RD   |
|-----------------------|------|------|------|------|------|------|-------|---------|------|------|------|------|--------|-------|------|
| Minimality            | PASS | C    | C    | C    | C    | C    | C     | C       | C    | C    | F    | F    | **C**  | F     | C    |
| Locality              | PASS | P    | P    | P    | P    | P    | P     | P       | P    | P    | P    | P    | **F**  | C     | P    |
| Determinism           | PASS | P    | P    | P    | P    | P    | P     | P       | C    | P    | P    | P    | **C**  | F     | C    |
| Gen. Sufficiency      | PASS | P    | P    | P    | P    | P    | P     | P       | P    | P    | C    | C    | **C(w)**| C    | P    |
| Envelope Tightness    | PASS | P    | P    | P    | P    | P    | P     | P       | C    | P    | P    | P    | **C**  | C     | C    |
| Structural Optimality | PASS | P    | P    | P    | P    | P    | P     | P       | P    | P    | C    | C    | **C**  | F     | C    |
| **Total PASS**        | 6    | 5    | 5    | 5    | 5    | 5    | 5     | 5       | 3    | 4    | 3    | 3    | **0**  | 0     | 2    |

### 7.3 The Locality FAIL: Structural, Not Defective

The KS's FAIL on Locality is *unique in the Atlas*: it is the first outright FAIL on Locality (NS received CONDITIONAL). The FAIL reflects the fact that the KS nonlocality is not a constraint (as in NS) but the *primary dynamical mechanism*:

- NS nonlocality (pressure): *enforces* a constraint. CONDITIONAL.
- **KS nonlocality (chemoattractant): *drives* the dynamics. FAIL.**

The distinction is principled: a nonlocal *constraint* is a structural feature that can be removed by relaxing the constraint (incompressibility → compressible NS, which is local). A nonlocal *driving force* is integral to the architecture and cannot be removed without destroying the phenomenology (removing the Poisson coupling → no chemotaxis, no aggregation, no blowup).

The FAIL is a *structural classification*, not a value judgment. The KS's nonlocality is *necessary for its phenomenology* and *well-motivated by the physics* (chemical signals diffuse and create long-range gradients). The FAIL simply registers that the architecture is *not local*.

### 7.4 Architectural Summary

The Keller–Segel system occupies a *unique structural position* in the PDE Atlas: it is the *aggregation pole* — the only architecture whose primary dynamical mechanism is nonlocal self-attraction, the only architecture with mass-concentrating blowup, and the only gradient flow whose Lyapunov descent drives the singularity rather than preventing it.

The KS achieves its dynamics with remarkable economy: four minimal axioms, zero constitutive parameters, one conserved quantity (mass M), and one sharp threshold (8 pi) derived from a fundamental inequality. From these minimal ingredients, the entire theory emerges — subcritical global existence, supercritical blowup, mass quantization, multi-center aggregation, measure-valued continuation.

The KS's *structural cost* is its nonlocality: two nonlocal channels that are necessary for the aggregation phenomenology but prevent a PASS on Locality. This cost is *inherent* — no local architecture can produce the KS's defining phenomena. The nonlocality is the *price of aggregation*, just as the fourth-order character is the price of conservation in CH/TFE, and the imaginary time derivative is the price of dispersion in NLS/KdV.

The KS's deepest contribution to the PDE Atlas is the demonstration that *gradient-flow structure does not guarantee global existence* — the free-energy landscape, not just the Lyapunov monotonicity, determines whether the dynamics converge to equilibrium or collapse to singularity. The KS is the *only architecture where the energy landscape has a hole* through which the gradient flow falls.

### 7.5 Composite Verdict

The Keller–Segel system is the aggregation pole of the PDE Atlas — a nonlocal, mass-conserving, Wasserstein gradient-flow architecture whose diffusion–aggregation competition is governed by the single invariant M relative to the sharp threshold 8 pi, producing the only mass-concentrating blowup in the Atlas, the only Lyapunov-driven singularity, and the only architecture whose nonlocality is a primary dynamical mechanism rather than a constraint — standing as the structural demonstration that gradient-flow monotonicity does not prevent singularity when the energy landscape is unbounded below.

---

*End of AD Criteria and Verdict. This completes the AD architectural evaluation of the Keller–Segel System.*
