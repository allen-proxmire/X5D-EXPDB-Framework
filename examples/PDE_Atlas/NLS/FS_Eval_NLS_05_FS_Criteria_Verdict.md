# AD Evaluation: Nonlinear Schrödinger Equation — AD Criteria and Verdict

Allen Proxmire

April 2026

---

## Overview

This file applies the six AD evaluation criteria to the cubic Nonlinear Schrödinger Equation as characterized in Modes 1–3. The NLS evaluation completes the *three-pole scaffold* of the PDE Atlas: the diffusive pole (FP/PME), the hyperbolic pole (HJ/Burgers), and now the *dispersive pole* (NLS). The NLS verdicts test whether dispersive Hamiltonian closure — the sixth closure mode discovered in the Atlas — produces an FS profile comparable to the five previously identified modes.

The NLS evaluation is *sign-dependent*: the focusing/defocusing dichotomy (the sign of ±|psi|^2 psi) produces different verdicts on Determinism and Envelope Tightness. The evaluation therefore produces *two verdict profiles* — one for the defocusing case and one for the focusing case — paralleling the NS dimensional split and the TFE parametric split.

Throughout, we reference the axioms NLS-1 through NLS-10, the envelope inequalities E1–E10, the universal inequalities U1–U10, and the channel constraints C1–C12 established in the preceding files.

---

## 1. Minimality

**Question:** Do the NLS axioms form a minimal architectural set?

### 1.1 Assessment of Individual Axioms

**NLS-1 (Complex Field).** *Minimal.* The complex-valued state variable psi in C is the defining structural commitment of the NLS architecture. Replacing psi with a real field converts the NLS into a nonlinear heat or wave equation — a qualitatively different architecture. The complex character couples amplitude and phase into a single dynamical object, producing the dispersive (oscillatory) evolution that defines the NLS. **Minimal — the complex field *is* the dispersive structure.**

**NLS-2 (Locality).** *Minimal.* Defines the PDE paradigm. Independent of other axioms. **Minimal.**

**NLS-3 (Dispersive Core).** *Minimal.* The operator i partial_t + Delta is the *free Schrödinger operator* — the linear part of the NLS. It is the unique second-order, isotropic, dispersive (skew-adjoint) operator on a complex scalar field. Replacing i partial_t with partial_t (real) gives the heat equation; replacing Delta with -Delta (wrong sign) gives an ill-posed equation. The dispersive core is uniquely determined by the requirements of second order, isotropy, unitarity, and dispersion. **Minimal.**

**NLS-4 (Gauge Invariance).** *Derived.* The U(1) gauge symmetry psi → e^{i theta} psi is a *consequence* of the PDE structure: the NLS commutes with phase rotation because the nonlinearity |psi|^2 psi depends on |psi|^2 (phase-invariant). Gauge invariance does not need to be imposed separately — it follows from the form of the equation. **Redundant (derived from NLS-3 + NLS-8).**

**NLS-5 (Hamiltonian Structure).** *Derived.* The Hamiltonian structure i psi_t = delta H / delta psi* is a *consequence* of the PDE structure: the NLS can be written in Hamiltonian form with H = integral [|nabla psi|^2 ± (1/2)|psi|^4] dx. This Hamiltonian formulation is not an additional axiom but a structural property of the equation. **Redundant (derived from NLS-3 + NLS-8).**

**NLS-6 (Mass Conservation).** *Derived.* Mass conservation follows from gauge invariance (NLS-4) via Noether's theorem, and gauge invariance follows from the PDE structure. **Redundant (derived).**

**NLS-7 (Momentum Conservation).** *Derived.* Momentum conservation follows from translational invariance of the PDE + Noether's theorem. **Redundant (derived).**

**NLS-8 (Cubic Nonlinearity ±|psi|^2 psi).** *Partially minimal.* The *form* of the nonlinearity (|psi|^2 psi) is the simplest gauge-invariant cubic nonlinearity — it is minimal given NLS-1 (complex field) and NLS-4 (gauge invariance). The *sign* (±) is a constitutive/structural choice:
- Defocusing (+): repulsive self-interaction.
- Focusing (-): attractive self-interaction.

The cubic power (not quadratic, not quartic) is a *constitutive selection* — other powers |psi|^{p-1} psi produce different NLS variants. The *sign* is a structural bifurcation parameter (like TFE's n or NS's dimension d). **Partially minimal:** the gauge-invariant form is minimal; the specific power p = 3 is constitutive; the sign ± is a structural bifurcation.

**NLS-9 (No Diffusion).** *Minimal.* The absence of diffusion (no real part in the time derivative: i psi_t, not psi_t) is the structural commitment that makes the equation dispersive rather than diffusive. Adding diffusion (epsilon Delta psi with real epsilon) converts NLS to the complex Ginzburg–Landau equation — a different, dissipative architecture. **Minimal.**

**NLS-10 (No Reaction).** *Minimal.* No source/sink terms. The evolution is conservative. **Minimal.**

### 1.2 Minimality Summary

| Axiom  | Content                     | Minimal?    | Comment                              |
|--------|-----------------------------|-------------|--------------------------------------|
| NLS-1  | Complex field               | Yes         | Defines dispersive structure         |
| NLS-2  | Locality                    | Yes         | Defines PDE paradigm                 |
| NLS-3  | Dispersive core (i∂_t + Δ) | Yes         | Unique dispersive operator           |
| NLS-4  | Gauge invariance            | Redundant   | Derived from NLS-3 + NLS-8          |
| NLS-5  | Hamiltonian structure       | Redundant   | Derived from PDE form                |
| NLS-6  | Mass conservation           | Redundant   | Derived from NLS-4 (Noether)        |
| NLS-7  | Momentum conservation       | Redundant   | Derived from translation (Noether)  |
| NLS-8  | ±\|ψ\|²ψ nonlinearity     | Partially   | Form minimal; power constitutive; sign structural |
| NLS-9  | No diffusion                | Yes         | Dispersive, not diffusive            |
| NLS-10 | No reaction                 | Yes         | Conservative                         |

**Structural core:** Five minimal axioms (NLS-1, NLS-2, NLS-3, NLS-9, NLS-10) plus one partially minimal (NLS-8: form minimal, power constitutive). Four redundant (NLS-4 through NLS-7, all derived from the PDE structure via Noether's theorem or direct verification).

**Non-minimal elements:**
- The specific cubic power p = 3 (constitutive — other powers produce different NLS variants).
- No geometric simplification is needed (NLS is naturally on R^d with no Euclidean restriction — there is no Riemannian manifold generalization that is standard).

**Criterion 1 Verdict: CONDITIONAL.** The structural core (five independent axioms + one partially minimal) is highly minimal. The non-minimal element is the specific power p = 3 in the nonlinearity (a constitutive selection from the family |psi|^{p-1} psi). The four redundant axioms (NLS-4 through NLS-7) are all *derived from the PDE structure* — they add no independent information. The CONDITIONAL is due to the constitutive power selection, the same type of non-minimality that produces CONDITIONAL in PME (exponent m), TFE (exponent n), and every other parameterized architecture.

---

## 2. Locality

**Question:** Is the NLS architecture fully local?

### 2.1 Assessment

Every channel is local:

- **D (Dispersion):** Delta psi involves psi and its second spatial derivatives at each point. Local.
- **N (Nonlinearity):** |psi|^2 psi depends on psi at each point (no derivatives). Local.
- **H (Hamiltonian):** The Hamiltonian H is a global functional, but the PDE i psi_t = delta H / delta psi* is local. The dynamics at each point depend only on psi and its local derivatives.
- **G (Gauge):** Phase rotation is a global symmetry but imposes no nonlocal coupling.

No elliptic constraint, no Poisson equation, no Green's function, no integral operator. The NLS is *fully local* at both formulation and solution levels.

### 2.2 Comparison

NLS shares the locality class of HJ, Burgers, AC, CH, PME, TFE, FP, MCF, and RD — all fully local. Only NS has a nonlocal channel.

The NLS has *infinite-speed propagation* (like FP and unlike PME/HJ/Burgers), but this arises from the dispersive spreading, not from a nonlocal coupling. The propagation is "instant" in the sense that compactly supported data becomes nonzero everywhere immediately, but the amplitude at large distances is exponentially small — the propagation is *effectively local* at any finite time horizon.

**Criterion 2 Verdict: PASS.** Fully local at formulation and solution levels. No nonlocal channel.

---

## 3. Determinism

**Question:** Does the NLS architecture uniquely determine the future from the initial data?

### 3.1 Assessment by Regime

**Defocusing (+), all d:**

- **Local well-posedness:** In H^s for s >= max(0, d/2 - 1). Unconditional.
- **Global well-posedness:** In H^1 for d <= 3. The positive-definite energy H >= 0 controls ||nabla psi||^2 <= H, providing uniform H^1 bounds. Global existence follows from Strichartz estimates + energy control.
- **Uniqueness:** Unconditional in the energy class H^1.
- **Continuous dependence:** In H^1 via the Strichartz framework.

**Verdict for defocusing: PASS.** Unconditional global determinism in all physically relevant dimensions.

**Focusing (-), d = 1:**

- **Global well-posedness:** In L^2 (mass conservation alone suffices for the cubic NLS in 1D, via the Gagliardo–Nirenberg inequality). For the integrable cubic NLS, the inverse scattering transform provides complete solvability.
- **Uniqueness and continuous dependence:** Unconditional.

**Verdict for focusing d = 1: PASS.** Complete global determinism (and complete integrability).

**Focusing (-), d = 2 (L^2-critical):**

- **Global well-posedness:** If M < M_* = ||Q||_{L^2}^2 (mass below the ground-state threshold). Proved by Dodson (2016) — global existence and scattering for sub-critical mass.
- **Blowup:** If M > M_* with H < 0 (negative energy), finite-time blowup occurs (virial identity). The blowup is well-characterized (Merle–Raphaël log-log rate).
- **At threshold M = M_*:** The ground-state soliton Q is the unique optimizer. Global existence holds, but scattering may fail.

**Verdict for focusing d = 2: CONDITIONAL.** Determinism holds globally for M < M_* (resolved, PASS). For M > M_*, blowup occurs — the classical solution ceases to exist. The blowup dynamics are well-characterized but the post-blowup continuation is not standard (unlike HJ/Burgers, where entropy/viscosity solutions continue past shocks). The CONDITIONAL reflects the blowup face, which is *sharp* (exact threshold M_*) but *not continued* (no standard weak-solution theory past blowup).

**Focusing (-), d = 3:**

- **Global well-posedness:** For small H^1 data (scattering results of Colliander–Keel–Staffilani–Takaoka–Tao and others for the energy-critical NLS). For large data, blowup can occur.
- **Blowup:** Well-characterized for radial data (Kenig–Merle concentration-compactness). Partially open for general non-radial data.

**Verdict for focusing d = 3: CONDITIONAL.** Small-data global existence holds. Large-data blowup exists. The threshold between global and blowup is partially characterized (energy-based, not as sharp as the d = 2 mass threshold).

### 3.2 Overall Verdict

**Criterion 3 Verdict: CONDITIONAL (sign- and dimension-dependent).**

| Regime              | Determinism        |
|--------------------|--------------------|
| Defocusing, all d  | **PASS** (unconditional global) |
| Focusing, d = 1    | **PASS** (global, integrable) |
| Focusing, d = 2    | CONDITIONAL (sharp threshold M_*) |
| Focusing, d >= 3   | CONDITIONAL (partial threshold) |

The defocusing NLS has the *strongest determinism* of any dispersive PDE — unconditional global well-posedness in all dimensions, comparable to FP and PME. The focusing NLS has *sign-dependent determinism*: globally well-posed below the critical threshold, blowup above it. The threshold is sharp in d = 2 (M_*) and partially characterized in d >= 3.

---

## 4. Generative Sufficiency

**Question:** Does the NLS generate all of its observed phenomena from the axioms?

### 4.1 Generated Phenomena

| Phenomenon                              | Derivation Method                            |
|-----------------------------------------|----------------------------------------------|
| Dispersive spreading (t^{-d/2})        | Stationary-phase analysis of Schrödinger group |
| Solitons (focusing 1D)                 | ODE reduction + variational methods           |
| Multi-soliton elastic collisions        | Inverse scattering transform (integrable 1D)  |
| Breathers and quasi-periodic orbits     | Inverse scattering + Lax pair                  |
| Scattering to linear flow (defocusing)  | Strichartz + Morawetz estimates                |
| Finite-time blowup (focusing, d >= 2)  | Virial identity + concentration-compactness    |
| Critical mass threshold M_* (d = 2)    | Sharp Gagliardo–Nirenberg + ground state Q     |
| Blowup rate (log-log, d = 2)           | Merle–Raphaël modulation theory                |
| Self-similar blowup profiles            | ODE reduction + rescaling                      |
| Mass, energy, momentum conservation     | Direct computation from PDE + Noether           |
| Strichartz estimates                    | Oscillatory integral theory (TT* argument)      |
| Orbital stability of solitons           | Grillakis–Shatah–Strauss theory                |

The NLS generates *all* of its major phenomena from the axioms. The theory is *remarkably complete*:
- 1D integrable NLS: *exactly solvable* (inverse scattering gives the complete solution).
- Defocusing NLS (all d): *global well-posedness + scattering* (complete long-time theory).
- Focusing NLS (d = 2): *sharp threshold* M_* + *blowup dynamics* fully characterized.
- Focusing NLS (d = 3): *partial threshold* + concentration-compactness classification.

### 4.2 Phenomena NLS Cannot Generate

| Phenomenon              | Reason for Absence                           |
|------------------------|----------------------------------------------|
| Shocks                 | No first-order transport (NLS-3)             |
| Diffusive smoothing    | No real Laplacian (NLS-9)                    |
| Entropy production     | Hamiltonian, reversible (NLS-5)              |
| Turing patterns        | Single species, no reaction (NLS-10)         |
| Coarsening             | No conserved order parameter with wells       |
| Free boundaries        | No degeneracy (non-degenerate dispersion)    |
| Turbulence (NS-type)   | No pressure, no incompressibility             |
| Monotone convergence   | No Lyapunov (Hamiltonian)                    |

### 4.3 Assessment

The NLS generates *every* phenomenon within its scope — dispersive spreading, solitons, scattering, blowup, elastic collisions, breathers — with a *complete or near-complete* theory. The generative gap is *very small*:

- The 1D integrable NLS is *exactly solvable* (zero gap).
- The defocusing NLS is *completely resolved* in all relevant dimensions (zero gap).
- The focusing d = 2 NLS has a *sharp threshold and characterized blowup* (near-zero gap).
- The focusing d >= 3 NLS has *partial threshold characterization* (small gap — the Kenig–Merle program is deep and ongoing but not yet fully complete for all data).

**Criterion 4 Verdict: PASS.** The NLS generates all characteristic phenomena within its scope. The integrable 1D NLS is exactly solvable. The defocusing NLS is completely resolved. The focusing NLS has sharp (d = 2) or partial (d >= 3) threshold theories. The generative gap is negligible — comparable to the PME and FP gaps.

---

## 5. Envelope Tightness

**Question:** Is the NLS envelope closed and tight?

### 5.1 Assessment

**E1 (Mass conservation).** Exact identity. **Tight.**
**E2 (Energy conservation).** Exact identity. **Tight.**
**E3 (Momentum conservation).** Exact identity. **Tight.**
**E4 (Dispersive estimate).** Sharp: the constant C is optimal (achieved by Gaussians). **Tight.**
**E5 (Strichartz estimates).** Sharp at the endpoint (Keel–Tao theorem). **Tight.**
**E6 (Local well-posedness).** Sharp in the scaling sense (the regularity threshold s = d/2 - 1 is critical). **Tight.**
**E7 (Global well-posedness, defocusing).** Complete — unconditional in H^1 for d <= 3. **Tight.**
**E8 (Virial/Morawetz).** Sharp: the virial identity is exact; the Morawetz estimates have optimal constants. **Tight.**
**E9 (Scattering, defocusing).** Complete — proved in the relevant dimensions. **Tight.**
**E10 (Critical thresholds).** *Sharp in d = 2* (M_* = ||Q||_{L^2}^2 is exact). Partially characterized in d >= 3. **Tight in d = 2; partially tight in d >= 3.**

### 5.2 Closure Assessment

**Defocusing (+):** The envelope is *fully closed*. Conservation laws + Strichartz + positive-definite energy provide complete control. No open faces. All estimates tight.

**Focusing (-), d = 1:** The envelope is *fully closed*. Mass conservation + Gagliardo–Nirenberg + integrability provide complete control.

**Focusing (-), d = 2:** The envelope is *closed at the sharp threshold*. M < M_*: fully closed (global + scattering). M > M_*: blowup face is *sharp and characterized* (exact threshold, exact blowup rate, exact blowup profile).

**Focusing (-), d >= 3:** The envelope is *partially open*. The threshold between global existence and blowup is partially characterized. The blowup dynamics are known for specific classes of data (radial, finite variance) but not for all initial data.

### 5.3 Verdict

**Criterion 5 Verdict: CONDITIONAL (sign-dependent).**

| Regime              | Envelope           |
|--------------------|--------------------|
| Defocusing, all d  | **Fully closed (PASS)** |
| Focusing, d = 1    | **Fully closed (PASS)** |
| Focusing, d = 2    | Sharp threshold (strong CONDITIONAL) |
| Focusing, d >= 3   | Partially open (CONDITIONAL) |

The *best-case* envelope (defocusing) is fully closed and tight — comparable to FP and PME. The *worst-case* envelope (focusing, d >= 3) has a partially open blowup face. The overall verdict is CONDITIONAL, reflecting the sign-dependent closure.

---

## 6. Structural Optimality

**Question:** Is the NLS architecture optimal?

### 6.1 Anomaly Assessment

**Defocusing NLS (+):**

- No nonlocal channel (all channels local).
- No destabilizing sub-channel (N is stabilizing for defocusing).
- No shock face (no first-order transport).
- No dissipation anomaly (no dissipation at all — Hamiltonian).
- No blowup face (positive-definite energy controls everything).

**Zero anomalies.** The defocusing NLS is *completely anomaly-free* — the most structurally clean dispersive architecture imaginable.

**Focusing NLS (-), d = 1:**

- No anomalies (global existence, integrability, soliton stability). **Zero anomalies.**

**Focusing NLS (-), d >= 2:**

- One structural face: focusing collapse (||nabla psi|| → infinity).
- The collapse face is *not an anomaly in the NS sense* (the blowup is well-characterized, with sharp or partial thresholds). It is a *structural feature* of the focusing architecture — the nonlinearity's attraction can overcome dispersion's spreading.
- The collapse face is *sign-dependent*: it disappears if the sign is flipped to defocusing.

**One structural face (focusing, d >= 2).** Not anomalous in the standard FS sense (well-characterized, threshold known) but an open face in the constraint surface.

### 6.2 Structural Economy

The NLS achieves its dynamics with *high structural economy*:

- **One constitutive parameter:** The sign ± (and, for the general NLS family, the power p). This is fewer parameters than AC (3), CH (3), NS (2), FP (2), TFE (1), PME (1) — tied with HJ and Burgers (both have the convexity of H/f as a structural condition but zero free parameters). MCF has zero parameters.
- **Four channels:** D, N, H, G. Comparable to AC (4) and FP (4), more than HJ/Burgers/MCF (3 each), fewer than NS (5).
- **Three exact conservation laws:** M, H, P. More conservation laws than any other architecture except NS (which has 2: mass + momentum).
- **One closure mode:** Dispersive Hamiltonian (conservation + Strichartz). Unique in the Atlas.

### 6.3 Comparison

| Feature                  | NLS (def.)   | NLS (foc., d=1) | NLS (foc., d>=2) | FP   | PME  | HJ   | Burgers | MCF  | NS(3D) |
|--------------------------|-------------|------------------|-------------------|------|------|------|---------|------|--------|
| Anomalies                | 0           | 0                | 1 (collapse)      | 0    | 0    | 0    | 0       | 0    | 2      |
| Parameters               | 1 (sign)    | 1 (sign)         | 1 (sign)          | 2    | 1    | 0    | 0       | 0    | 2      |
| Conservation laws        | **3**       | **3**            | **3**             | 1    | 1    | 0    | 1       | 0    | 2      |
| Channels                 | 4           | 4                | 4                 | 4    | 4    | 3    | 3       | 3    | 5      |
| Reversible               | **Yes**     | **Yes**          | **Yes**           | No   | No   | No   | No      | No   | No     |
| Solitons                 | No          | **Yes**          | **Yes** (ground st.)| No | No   | No   | No      | No   | No     |

### 6.4 Verdict

**Criterion 6 Verdict: CONDITIONAL (sign-dependent).**

| Regime              | Structural Optimality |
|--------------------|-----------------------|
| Defocusing, all d  | **PASS** (zero anomalies, high economy) |
| Focusing, d = 1    | **PASS** (zero anomalies, integrable, solitons) |
| Focusing, d >= 2   | CONDITIONAL (one collapse face, well-characterized) |

The defocusing NLS is *structurally optimal*: zero anomalies, high economy, unique closure mode, three conservation laws. The focusing NLS (d >= 2) has one structural face (collapse) that prevents a full PASS — but the face is well-characterized (sharp threshold in d = 2, partial in d >= 3), placing it above NS (two architectural anomalies, both unresolved) and comparable to MCF (one required singularity face, fully classified).

---

## 7. FS Verdict Summary

### 7.1 Criteria Scorecard

| Criterion                  | Defocusing      | Focusing d=1    | Focusing d=2    | Focusing d>=3   |
|----------------------------|-----------------|-----------------|-----------------|-----------------|
| **1. Minimality**          | CONDITIONAL     | CONDITIONAL     | CONDITIONAL     | CONDITIONAL     |
| **2. Locality**            | **PASS**        | **PASS**        | **PASS**        | **PASS**        |
| **3. Determinism**         | **PASS**        | **PASS**        | CONDITIONAL     | CONDITIONAL     |
| **4. Gen. Sufficiency**    | **PASS**        | **PASS**        | **PASS**        | **PASS**        |
| **5. Envelope Tightness**  | **PASS**        | **PASS**        | CONDITIONAL     | CONDITIONAL     |
| **6. Structural Optimality** | **PASS**      | **PASS**        | CONDITIONAL     | CONDITIONAL     |
| **Total PASS**             | **5**           | **5**           | **2**           | **2**           |

### 7.2 Comparison Across the PDE Atlas

| Criterion             | ED   | NLS(def.)| NLS(foc.1D)| FP   | PME  | HJ   | Burgers | MCF  | TFE(n>=1)| AC   | CH   | NS(3D) | RD   |
|-----------------------|------|----------|------------|------|------|------|---------|------|----------|------|------|--------|------|
| Minimality            | PASS | COND.    | COND.      | COND.| COND.| COND.| COND.   | COND.| COND.    | FAIL | FAIL | FAIL   | COND.|
| Locality              | PASS | **PASS** | **PASS**   |**PASS**|**PASS**|**PASS**|**PASS**|**PASS**|**PASS**|**PASS**|**PASS**| COND.| **PASS**|
| Determinism           | PASS | **PASS** | **PASS**   |**PASS**|**PASS**|**PASS**|**PASS**| COND.|**PASS**|**PASS**|**PASS**| FAIL | COND.|
| Gen. Sufficiency      | PASS | **PASS** | **PASS**   |**PASS**|**PASS**|**PASS**|**PASS**|**PASS**|**PASS**| COND.| COND.| COND.| **PASS**|
| Envelope Tightness    | PASS | **PASS** | **PASS**   |**PASS**|**PASS**|**PASS**|**PASS**| COND.|**PASS**|**PASS**|**PASS**| COND.| COND.|
| Structural Optimality | PASS | **PASS** | **PASS**   |**PASS**|**PASS**|**PASS**|**PASS**|**PASS**|**PASS**| COND.| COND.| FAIL | COND.|
| **Total PASS**        | **6**| **5**    | **5**      | **5**| **5**| **5**| **5**   | **3**| **4**    | **3**| **3**| **0**  | **2**|

### 7.3 The Six 5-PASS Architectures

Six PDEs now achieve the maximum PDE score of 5 PASS + 1 CONDITIONAL:

| Architecture    | Closure Mode             | Singularity?          | Character            |
|----------------|--------------------------|----------------------|----------------------|
| **FP**         | Linear                   | None                 | Parabolic, drift+diff.|
| **PME**        | Dissipative              | None                 | Parabolic, degenerate |
| **HJ**         | Variational              | Gradient kink        | Hyperbolic, potential |
| **Burgers**    | Entropic-contractive     | Velocity shock       | Hyperbolic, cons. law |
| **NLS (def.)** | **Dispersive Hamiltonian**| **None**             | **Dispersive, complex**|
| **NLS (foc.1D)**| **Dispersive Hamiltonian**| **None (solitons)** | **Dispersive, integrable**|

These six architectures represent the *six fundamental closure modes* and *three dynamical poles* of PDE theory:

**Diffusive pole:** FP (linear closure), PME (dissipative closure).
**Hyperbolic pole:** HJ (variational closure), Burgers (entropic-contractive closure).
**Dispersive pole:** NLS defocusing (dispersive Hamiltonian closure), NLS focusing 1D (dispersive Hamiltonian + integrability closure).

The three poles, six closure modes, and six 5-PASS architectures form the *complete structural scaffold* of the FS PDE Atlas.

### 7.4 Architectural Summary

The Nonlinear Schrödinger Equation achieves the joint-strongest FS profile of any PDE in the Atlas in its defocusing and 1D focusing variants: 5 PASSes + 1 CONDITIONAL, tying with FP, PME, HJ, and Burgers. The NLS represents the *dispersive pole* of the Atlas — the third fundamental dynamical mode after diffusion (parabolic) and transport (hyperbolic).

The NLS introduces *four structural firsts* to the Atlas:
1. **First complex-valued field** (psi in C — two coupled real components via i).
2. **First Hamiltonian PDE** (energy-conserving, symplectic, time-reversible).
3. **First dispersive architecture** (oscillatory spreading through phase interference).
4. **First soliton-supporting architecture** (localized, shape-preserving waves from dispersion-nonlinearity balance).

The NLS's structural contribution is the demonstration that *conservation + dispersion* constitute a complete closure mode: three conservation laws (mass, energy, momentum) + Strichartz estimates (dispersive space-time control) provide existence, uniqueness, and stability without any dissipation, any entropy, or any smoothing. This *dispersive Hamiltonian closure* is the sixth and final closure mode discovered in the Atlas — completing the catalog of fundamental mechanisms by which nonlinear PDEs can be globally well-posed.

The focusing/defocusing dichotomy — controlled by a single sign — is the NLS's structural bifurcation. In the defocusing case and in 1D focusing, the architecture is maximally sound (5 PASS). In higher-dimensional focusing, the collapse face opens — well-characterized (sharp threshold in d = 2) but unresolved post-blowup (no standard weak continuation). The NLS focusing blowup is better understood than the NS 3D blowup (the NLS threshold is sharp; the NS threshold is open) but less completely resolved than the HJ/Burgers blowup (which has a complete weak-solution continuation).

### 7.5 Composite Verdict

The Nonlinear Schrödinger Equation is the dispersive pole of the PDE Atlas — a complex-valued, Hamiltonian, time-reversible, soliton-supporting architecture that achieves maximum structural closure through conservation laws and dispersive estimates alone, introducing the sixth fundamental closure mode to the Atlas and completing the three-pole scaffold of diffusion, transport, and dispersion that spans the full range of nonlinear PDE dynamics.

---

*End of AD Criteria and Verdict. This completes the AD architectural evaluation of the Nonlinear Schrödinger Equation.*
