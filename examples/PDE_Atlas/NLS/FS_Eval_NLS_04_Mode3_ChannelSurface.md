# AD Evaluation: Nonlinear Schrödinger Equation — Mode 3: Channels → Constraint Surface

Allen Proxmire

April 2026

---

## Overview

Mode 3 constructs the constraint surface of the NLS architecture. The NLS constraint surface is *structurally unprecedented* in the PDE Atlas: it is the first surface sealed by *unitarity and dispersion* rather than by dissipation, entropy, or convex variational structure. The NLS has no Lyapunov functional, no entropy production, no monotone convergence — and yet it has a well-defined constraint surface with controlled dynamics, because the *conservation laws* (mass, energy, momentum) and *dispersive estimates* (Strichartz inequalities) provide structural control without any dissipation mechanism.

The NLS constraint surface also introduces the concept of *oscillatory closure* — closure achieved through phase cancellation rather than amplitude decay. Where parabolic surfaces are sealed by the monotone decrease of a Lyapunov functional, and hyperbolic surfaces are sealed by entropy admissibility + contraction, the NLS surface is sealed by the *unitary propagator* (which preserves L^2) combined with *dispersive decay* (which reduces L^{infinity} through interference). This is a *new mode of constraint-surface closure* unique to the dispersive pole of the Atlas.

We continue with:

    i partial_t psi + Delta psi ± |psi|^2 psi = 0

---

## 1. Channel Decomposition

### Channel D: Dispersion

    D(psi) = -Delta psi    [inside i psi_t = -Delta psi ± |psi|^2 psi]

- **Locality:** Local. Depends on psi and Delta psi at each point. Second-order spatial derivatives.
- **Linearity:** Linear. The Laplacian is a linear operator.
- **Stability role:** Stabilizing (dispersively). The free Schrödinger group e^{it Delta} is an *isometry* on L^2 (preserves ||psi||_{L^2}) and a *decay operator* on L^{infinity} (||e^{it Delta} f||_{L^inf} ~ t^{-d/2}). The stabilization is achieved through *phase cancellation* — different Fourier components rotate at different rates and interfere destructively — not through amplitude damping. The dispersion channel *spreads* without *dissipating*.
- **Scale action:** Mode k oscillates at frequency omega = k^2 (quadratic dispersion). High-frequency modes oscillate faster and dephase more rapidly. The dispersion is *frequency-selective*: it separates frequencies through differential phase rotation, not through differential amplitude damping. The effective "damping" rate in L^{infinity} is t^{-d/2} — the same rate as second-order diffusion — but with no L^2 decay.

### Channel N: Nonlinearity

    N(psi) = ± |psi|^2 psi

- **Locality:** Local. |psi|^2 psi depends on psi at each point (no spatial derivatives).
- **Linearity:** Nonlinear. Cubic in psi. The sole nonlinear channel in the NLS.
- **Stability role:**
  - *Defocusing (+):* Stabilizing. The repulsive self-interaction enhances dispersive spreading. The energy H = integral [|nabla psi|^2 + (1/2)|psi|^4] dx is positive definite → ||nabla psi||^2 <= H → uniform H^1 control → global existence.
  - *Focusing (-):* Destabilizing (in d >= 2). The attractive self-interaction opposes dispersion. When the nonlinearity dominates dispersion (high amplitude, small scale), the wave function self-focuses → concentration → blowup (||nabla psi|| → infinity).
- **Scale action:** Scale-free (no derivatives). The nonlinearity acts at all spatial scales with the same strength — its effect depends on the local *amplitude* |psi|, not on the spatial structure. This is the same scale-free character as the reaction channel in AC/RD — but the NLS nonlinearity preserves mass (|psi|^2 psi has the same L^2 norm structure as psi), while the AC reaction does not.

### Channel H: Hamiltonian Structure

    H: i psi_t = delta H / delta psi*,    dH/dt = 0,    dM/dt = 0,    dP/dt = 0

- **Locality:** The Hamiltonian H[psi] is a global functional. The PDE is local.
- **Linearity:** Nonlinear (through the |psi|^4 term in H).
- **Stability role:** Conservative. The Hamiltonian structure *preserves* three quantities (M, H, P) and *preserves* the symplectic structure of the phase space. It neither stabilizes nor destabilizes in the monotone sense — it constrains the dynamics to an isoenergetic surface but does not drive them toward or away from any particular state. The Hamiltonian structure is the NLS's *rigidity channel* — it provides the conservation laws that control the dynamics without imposing any directionality.
- **Scale action:** All-scale. The conservation laws constrain the dynamics at every spatial and temporal scale simultaneously. The energy H couples the kinetic (||nabla psi||^2) and potential (integral |psi|^4) contributions, linking the small-scale (gradient) and large-scale (amplitude) behaviors.

### Channel G: Gauge Invariance

    G: psi → e^{i theta} psi    is a symmetry for all theta in R

- **Locality:** Global symmetry (the same phase rotation everywhere).
- **Linearity:** Linear (phase rotation is multiplication by a scalar).
- **Stability role:** Neutral (symmetry constraint). Gauge invariance generates mass conservation via Noether's theorem. It restricts the admissible dynamics (the PDE must commute with phase rotation) but does not stabilize or destabilize.
- **Scale action:** All-scale (the symmetry applies at every frequency and every amplitude).

### Channel Summary Table

| Channel | Symbol | Term / Feature          | Locality | Linearity   | Stability              | Scale Action           |
|---------|--------|-------------------------|----------|-------------|------------------------|------------------------|
| Dispersion   | D | -Delta psi             | Local    | Linear      | Stabilizing (dispersive)| omega = k^2            |
| Nonlinearity | N | ±\|psi\|^2 psi        | Local    | Nonlinear   | ±: stab/destab         | Scale-free             |
| Hamiltonian  | H | dH/dt = 0, symplectic  | Global*  | Nonlinear   | Conservative (rigid)   | All-scale              |
| Gauge        | G | psi → e^{i theta} psi | Global   | Linear      | Neutral (symmetry)     | All-scale              |

*H is a global functional; the PDE is local.

### Channel Structure Comparison

| Architecture | Dynamical Channels | Conservation/Symmetry | Closure Type          |
|-------------|--------------------|-----------------------|-----------------------|
| **NLS**     | **2 (D, N)**       | **2 (H, G)**          | **Dispersive Hamiltonian** |
| FP          | 2 (T, D)           | 2 (C, P)              | Linear                |
| PME         | 1 (D_nl)           | 2 (C, entropy)        | Dissipative           |
| HJ          | 1 (T)              | 2 (S, V)              | Variational           |
| Burgers     | 1 (T)              | 2 (S, V)              | Entropic-contractive  |
| MCF         | 1 (K)              | 2 (G, T)              | Geometric-dissipative |
| NS          | 2 (A, V)           | 3 (P, C, F)           | Open (3D)             |

NLS has four channels — the same count as AC and FP. But the NLS channels are qualitatively different: both structural channels (H, G) are *conservative* (preserving quantities), while in parabolic architectures the structural channels are *dissipative* (decreasing quantities). This conservative character is the structural signature of the dispersive pole.

---

## 2. Dissipation Geometry

### 2.1 The Complete Absence of Dissipation

The NLS has *no dissipation mechanism of any kind*:

| Dissipation Type         | NLS Status              | Reason                          |
|--------------------------|-------------------------|---------------------------------|
| Volumetric diffusion     | **Absent**              | No real Laplacian (i Delta, not Delta) |
| Energy decay (Lyapunov)  | **Absent**              | dH/dt = 0 (Hamiltonian)        |
| Entropy production       | **Absent**              | No entropy functional           |
| Shock dissipation        | **Absent**              | No first-order transport        |
| Geometric dissipation    | **Absent**              | No surface state variable       |
| Mass decay               | **Absent**              | dM/dt = 0 (unitary)            |

The NLS is the *only architecture in the Atlas with zero dissipation in every category*. HJ has no classical dissipation but has variational closure; Burgers has shock-concentrated dissipation; every parabolic architecture has volumetric dissipation. The NLS has *none*.

### 2.2 Oscillatory Spreading as a Substitute for Dissipation

Despite having no dissipation, the NLS has a mechanism that *functions like* dissipation in certain respects: *dispersive spreading*. The L^{infinity} norm of the free Schrödinger flow decays:

    ||e^{it Delta} f||_{L^{infinity}} <= C |t|^{-d/2} ||f||_{L^1}

This decay is not caused by energy loss (the L^2 norm is constant) but by *phase cancellation*: at each point x, the contributions from different Fourier components of f rotate at different rates (e^{-ik^2 t}) and interfere destructively, producing a net amplitude that decreases as t^{-d/2}.

**Comparison with diffusive decay:**

| Feature                    | Diffusive Decay (Heat)          | Dispersive Decay (Schrödinger) |
|----------------------------|---------------------------------|--------------------------------|
| L^{infinity} rate          | t^{-d/2}                       | t^{-d/2}                      |
| L^2 norm                   | **Decreasing**                  | **Conserved**                  |
| Mechanism                  | Energy dissipation              | Phase cancellation             |
| Regularity gain            | Yes (C^{infinity} for t > 0)   | **No** (H^s preserved)        |
| Reversibility              | No (irreversible)              | **Yes** (time-reversible)      |
| Monotonicity               | Yes (||u||_{L^inf} non-increasing) | **No** (||psi||_{L^inf} can increase and decrease) |

The dispersive decay has the *same rate* as diffusive decay but *none of the other properties*. It is a *pseudo-dissipation* — it reduces the sup norm without reducing the energy, without gaining regularity, and without being monotone. The NLS L^{infinity} norm can *increase* (through constructive interference / refocusing) after initially decreasing — unlike diffusive decay, which is monotone.

### 2.3 The Hamiltonian Constraint Surface: Conservation Instead of Dissipation

The NLS constraint surface is not shaped by dissipation (which reduces dimensions) but by *conservation* (which fixes dimensions):

- Mass M = const: the dynamics are confined to the *mass shell* {psi : ||psi||_{L^2}^2 = M}.
- Energy H = const: the dynamics are further confined to the *energy surface* {psi : H[psi] = E} within the mass shell.
- Momentum P = const: the dynamics are further confined to a *momentum surface*.

The intersection of these three level sets is an *infinite-codimension-3 submanifold* of the phase space. The dynamics are confined to this submanifold but are *free within it* — there is no gradient-flow direction, no preferred equilibrium, no attractor on the submanifold.

This is qualitatively different from every other constraint surface in the Atlas:
- Parabolic surfaces: dynamics descend a Lyapunov functional → contract to equilibrium.
- Hyperbolic surfaces: dynamics produce entropy → contract through information loss.
- **NLS surface: dynamics circulate on a conserved level set → no contraction, no expansion**.

### 2.4 Comparison of Dissipation/Conservation Geometries

| Architecture | Geometry Type               | Mechanism                     | Dimension Trend       |
|-------------|------------------------------|-------------------------------|-----------------------|
| FP/PME/AC/CH/TFE | Dissipative (contracting) | Lyapunov → equilibrium    | Decreasing (→ attractor) |
| MCF         | Dissipative-geometric        | Area → extinction             | Decreasing (→ point)  |
| HJ          | Variational (non-dissipative)| Hopf–Lax → paraboloid        | Fixed (viscosity sol.)  |
| Burgers     | Entropic-contractive         | Shocks → N-wave              | Decreasing (L^1 contract)|
| **NLS**     | **Conservative (isoenergetic)** | **Conservation laws → level set** | **Fixed (Hamiltonian)** |
| NS          | Viscous (partially contracting)| Energy inequality            | Decreasing (if regular) |

The NLS is the only architecture whose constraint surface has *fixed effective dimension* — the conservation laws constrain the dynamics to a fixed-codimension submanifold, and the Hamiltonian flow preserves the dimension of the accessible region within that submanifold. There is no contraction, no expansion, and no topological simplification of the dynamics over time.

---

## 3. Constraint Surface Geometry

### 3.1 Three Dynamical Regions

**Region A: Dispersion-Dominated (rho >> 1, linear regime)**

Low amplitude or large spatial scale. The nonlinearity is negligible. The solution behaves like the free Schrödinger equation: ||psi(t)||_{L^inf} ~ t^{-d/2}, the wave packet spreads, and the solution effectively linearizes.

**Constraint surface properties:**
- Fully controlled by the linear dispersive estimates (E4, E5 from Mode 1).
- Global existence unconditional.
- Scattering: the solution approaches a free linear flow as t → infinity.
- The constraint surface is *smooth and well-posed* in this region.

**Region B: Balanced (rho ~ 1, soliton regime)**

Amplitude and scale matched so that dispersion and nonlinearity are commensurate. The solution maintains coherent localized structures:
- Solitons (focusing 1D): traveling waves with fixed shape.
- Standing waves: psi = e^{i omega t} Q(x) with Q solving the ground-state equation.
- Breathers (integrable 1D): oscillating localized structures.

**Constraint surface properties:**
- The soliton manifold is a *finite-dimensional submanifold* of the infinite-dimensional phase space, parameterized by (amplitude, position, velocity, phase).
- Orbital stability: perturbations of solitons remain close to the soliton manifold.
- The constraint surface is *smooth and stable* in this region.

**Region C: Nonlinearity-Dominated (rho << 1, collapse regime, focusing d >= 2)**

High amplitude at small scale. The focusing nonlinearity overwhelms dispersion. The wave function concentrates:

    ||nabla psi(t)||_{L^2} → infinity    as t → T*

**Constraint surface properties:**
- The constraint surface has a *singular face* in this region: the solution escapes to infinite gradient in finite time.
- The blowup profile is characterized: near T*, the solution approaches a rescaled ground-state Q.
- The blowup rate is known: lambda(t) ~ (T* - t)^{1/2} (self-similar) or lambda(t) ~ (T* - t)^{1/2}/sqrt(log|log(T*-t)|) (log-log, d = 2 L^2-critical).
- The singular face is *partially resolved*: the blowup dynamics are well-characterized, but the post-blowup continuation is not standard (unlike HJ/Burgers, where entropy solutions continue past shocks).

### 3.2 Assembly into a Single Constraint Surface

The three regions form a single constraint surface parameterized by the ratio rho = t_disp / t_nonlin:

    Region A (dispersion-dominated) → Region B (balanced) → Region C (collapse, focusing)

**Defocusing (+):** Only Regions A and B are accessible. Region C does not exist — the positive-definite energy prevents the nonlinearity from dominating. The constraint surface is *fully closed* (no singular face). The dynamics flow from B to A (solitons disperse) or remain in A (scattering).

**Focusing (-), d = 1:** Regions A and B are accessible. Region C is not reached — the 1D focusing NLS is globally well-posed (mass conservation suffices). The constraint surface is *fully closed* with solitons as persistent coherent structures.

**Focusing (-), d = 2:** All three regions are accessible. Region C is reached when M > M_* (mass above the ground-state threshold). The constraint surface has a *singular face* at M = M_* — solutions with M > M_* can cross into Region C and blow up.

**Focusing (-), d >= 3:** All three regions are accessible. Region C is reached for large H^1 data. The constraint surface has a *singular face* that is broader than in d = 2 (no sharp mass threshold; blowup depends on energy and profile).

### 3.3 Structural Comparison of Constraint Surface Types

| Architecture | Surface Type               | Sealed By                      | Singular Face?           |
|-------------|----------------------------|--------------------------------|--------------------------|
| FP          | Dissipative (contracting)  | Linearity + entropy            | None                     |
| PME         | Dissipative (contracting)  | Degeneracy + entropy + L^1     | None                     |
| AC/CH       | Dissipative (contracting)  | Lyapunov + smoothing           | None                     |
| HJ          | Variational (non-contract.)| Convexity + viscosity          | Gradient kink (required) |
| Burgers     | Entropic-contractive       | Convex flux + L^1              | Shock (required)         |
| MCF         | Dissipative-geometric      | Area + Huisken                 | Curvature blowup (req.) |
| **NLS (def.)** | **Conservative (isoenergetic)** | **Conservation + Strichartz** | **None**          |
| **NLS (foc., d=1)** | **Conservative**    | **Conservation + integrability** | **None**          |
| **NLS (foc., d=2)** | **Conservative**    | **Conservation + Strichartz** | **Collapse (M > M_*)** |
| NS (3D)    | Partially dissipative      | Viscosity (insufficient?)      | Open                     |

---

## 4. Anomalies and Open Faces

### 4.1 Sealed Faces

**Diffusion face: Absent.** The NLS has no diffusion channel. There is no face to seal — the question of diffusive smoothing does not arise.

**Entropy/Lyapunov face: Absent.** The NLS has no entropy functional and no Lyapunov functional. The question of monotone convergence does not arise.

**Shock face: Absent.** The NLS has no first-order transport (no v v_x term). Characteristic-crossing shocks cannot form. The gradient of psi can blow up (in the focusing case), but through *concentration* (amplitude blowup), not through *steepening* (gradient compression).

**Pattern-formation face: Absent.** Single species, no reaction. No Turing mechanism.

**Nonlocal face: Absent.** All channels local. No pressure equation.

**Amplitude blowup (defocusing): Sealed.** The positive-definite energy controls ||nabla psi||_{L^2} <= H. Combined with mass conservation and Gagliardo–Nirenberg, this gives uniform bounds on all relevant norms. No blowup possible.

### 4.2 The Open Face: Focusing Collapse (d >= 2)

The single open face of the NLS constraint surface is the *focusing collapse face* — the region where the focusing nonlinearity overwhelms dispersion and drives ||nabla psi|| → infinity:

**d = 2, focusing cubic (L^2-critical):**

    Open face at M > M_* = ||Q||_{L^2}^2

The face is *sharp*: the threshold mass M_* is exactly known (it is the mass of the ground-state soliton Q). Below M_*, the surface is closed (global existence + scattering). Above M_*, blowup is possible.

This is the most precisely characterized open face in the Atlas:
- NS 3D: the enstrophy face is *open* (blowup unknown).
- TFE n < 1: the positivity face is *parametrically open* (positivity uncertain).
- RD (super-linear): the blowup face is *constitutively open* (blowup for u^p, p > 1 + 2/d).
- **NLS focusing d = 2: the collapse face has a *sharp threshold* M_* with exact value.**

**d >= 3, focusing cubic:**

    Open face for large H^1 data

The threshold is less sharp — it depends on both mass and energy (not just mass). The Kenig–Merle concentration-compactness framework identifies threshold solutions, but the complete classification of blowup vs. global existence for all initial data remains partially open.

### 4.3 Anomaly Assessment

| Face                    | Status (Defocusing)  | Status (Focusing, d=1) | Status (Focusing, d>=2) |
|-------------------------|----------------------|------------------------|-------------------------|
| Diffusion               | Absent               | Absent                 | Absent                  |
| Entropy/Lyapunov        | Absent               | Absent                 | Absent                  |
| Shock                   | Absent               | Absent                 | Absent                  |
| Pattern-formation       | Absent               | Absent                 | Absent                  |
| Nonlocal                | Absent               | Absent                 | Absent                  |
| Amplitude blowup        | **Sealed** (E > 0)   | **Sealed** (M controls)| **Open** (collapse)     |

**Anomaly count:**
- Defocusing: **zero** anomalies. Fully closed.
- Focusing, d = 1: **zero** anomalies. Fully closed (integrability + mass conservation).
- Focusing, d = 2: **one** open face (collapse at M > M_*). Sharp threshold.
- Focusing, d >= 3: **one** open face (collapse for large data). Partially characterized.

The NLS anomaly profile is *sign-dependent*: the defocusing architecture is anomaly-free; the focusing architecture has one open face in d >= 2. This mirrors the NS dimensional dependence (2D anomaly-free, 3D open) and the TFE parametric dependence (n >= 1 anomaly-free, n < 1 open), but with a *sign* rather than a *dimension or parameter* as the control variable.

### 4.4 NLS as the Unitarity-Sealed Architecture

The NLS constraint surface is the *only* surface in the Atlas sealed by **unitarity + dispersion**:

- **Unitarity** (from the imaginary time derivative i psi_t): preserves the L^2 norm → mass conservation → amplitude control.
- **Dispersion** (from the Laplacian Delta psi): spreads the wave function → L^{infinity} decay → nonlinearity control.
- **Conservation laws** (from Hamiltonian + gauge symmetry): energy and momentum are exact invariants → additional structural constraints.
- **Strichartz estimates** (from the dispersive oscillatory integral): space-time norm control → nonlinear fixed-point closure.

No other architecture uses this combination. Parabolic architectures use dissipation; hyperbolic architectures use entropy + contraction; MCF uses area dissipation. The NLS uses *conservation + oscillatory decay* — a fundamentally different mode of closure.

---

## 5. Channel Constraints

---

**C1. Complex Field**

    psi : R^d x R → C

The state variable is complex-valued. The real and imaginary parts are coupled through i.

*Scope: All NLS.*

---

**C2. U(1) Gauge Invariance**

    psi → e^{i theta} psi    is a symmetry for all theta

Generates mass conservation via Noether's theorem.

*Scope: All NLS.*

---

**C3. Hamiltonian Structure**

    i psi_t = delta H / delta psi*,    dH/dt = 0

Symplectic flow. Energy-conserving. Time-reversible. No dissipation.

*Scope: All NLS.*

---

**C4. Mass Conservation**

    ||psi(t)||_{L^2}^2 = M = const    for all t

Exact L^2 invariance. Unitary evolution.

*Scope: All NLS.*

---

**C5. Energy Conservation**

    H[psi(t)] = integral [|nabla psi|^2 ± (1/2)|psi|^4] dx = const

Hamiltonian invariant. Positive definite (defocusing) or indefinite (focusing).

*Scope: All NLS.*

---

**C6. Momentum Conservation**

    P[psi(t)] = Im integral psi* nabla psi dx = const

Translation-invariance Noether charge.

*Scope: All NLS.*

---

**C7. Dispersive Decay**

    ||e^{it Delta} f||_{L^{infinity}} <= C |t|^{-d/2} ||f||_{L^1}

The linear propagator decays at rate t^{-d/2} in L^{infinity}. Oscillatory, not dissipative.

*Scope: Free Schrödinger group (linear part).*

---

**C8. Strichartz Admissibility**

    ||psi||_{L^q_t L^r_x} <= C(||psi_0||_{L^2} + ||N(psi)||_{L^{q'}_t L^{r'}_x})

Mixed space-time control for admissible pairs (q, r) with 2/q + d/r = d/2.

*Scope: All NLS.*

---

**C9. Soliton Branch (Focusing)**

    Focusing NLS admits soliton solutions psi = e^{i omega t} Q(x) with Q solving
    -Delta Q + omega Q - |Q|^2 Q = 0

The ground state Q is orbitally stable in 1D and is the critical object for blowup/global thresholds in d >= 2.

*Scope: Focusing NLS.*

---

**C10. Scattering (Defocusing)**

    ||psi(t) - e^{it Delta} psi_+||_{H^1} → 0    as t → infinity

Solutions approach free linear flow asymptotically. The nonlinearity becomes negligible.

*Scope: Defocusing NLS, d >= 3 (and d = 2 with modifications).*

---

**C11. Virial / Morawetz Constraints**

    d^2/dt^2 integral |x|^2 |psi|^2 dx = 8H    [d = 2, focusing cubic]

If H < 0: variance is concave → blowup in finite time. Provides sufficient condition for collapse.

*Scope: Focusing NLS with appropriate spatial decay.*

---

**C12. Critical Mass / Energy Thresholds**

    d = 2, focusing: M < M_* = ||Q||_{L^2}^2 => global existence
                     M > M_*                   => blowup possible

The ground-state mass M_* is the exact threshold. Sharp — the most precise blowup boundary in the Atlas.

*Scope: Focusing cubic NLS, d = 2.*

---

### Channel Constraint Summary

| Label | Constraint                        | Type              | Scope                  |
|-------|-----------------------------------|-------------------|------------------------|
| C1    | Complex field                     | Structural        | All NLS                |
| C2    | U(1) gauge invariance             | Symmetry          | All NLS                |
| C3    | Hamiltonian structure             | Structural        | All NLS                |
| C4    | Mass conservation                 | Exact identity    | All NLS                |
| C5    | Energy conservation               | Exact identity    | All NLS                |
| C6    | Momentum conservation             | Exact identity    | All NLS                |
| C7    | Dispersive decay                  | Estimate          | Linear flow            |
| C8    | Strichartz admissibility          | Space-time        | All NLS                |
| C9    | Soliton branch                    | Existence         | Focusing               |
| C10   | Scattering                        | Asymptotics       | Defocusing, d >= 3     |
| C11   | Virial/Morawetz                   | Blowup condition  | Focusing, radial       |
| C12   | Critical thresholds               | Sharp boundary    | Focusing, d = 2        |

**Six constraints (C1–C6) hold unconditionally for all NLS.** Six (C7–C12) are regime-dependent (linear flow, focusing/defocusing, dimension). The six unconditional constraints are all *conservation/symmetry* properties — the NLS's structural backbone.

---

## 6. Comparison with FP, PME, HJ, Burgers, NS, MCF, AC/CH, TFE, RD, and ED

### 6.1 Closure Mechanism Comparison

| Architecture | Closure Mode             | Key Tool                     | Dissipation? | Reversible? |
|-------------|--------------------------|------------------------------|-------------|-------------|
| FP          | Linear                   | Linearity + spectral theory  | Yes         | No          |
| PME         | Dissipative              | Lyapunov + L^1 contraction   | Yes         | No          |
| HJ          | Variational              | Convexity + Hopf–Lax        | No          | No          |
| Burgers     | Entropic-contractive     | Convex flux + Kruzkov L^1    | At shocks   | No          |
| MCF         | Geometric-dissipative    | Area + Huisken monotonicity  | Yes         | No          |
| **NLS**     | **Dispersive Hamiltonian**| **Conservation + Strichartz**| **No**      | **Yes**     |
| NS          | Open (3D)                | Viscosity (insufficient?)    | Yes         | No          |
| AC/CH/TFE   | Dissipative              | Lyapunov + smoothing         | Yes         | No          |

NLS is the *only* architecture that is both *non-dissipative* and *reversible*. HJ is non-dissipative but irreversible (entropy at shocks); Burgers is irreversible (shock dissipation); all parabolic architectures are dissipative and irreversible. NLS is the unique *conservative reversible* architecture.

### 6.2 The Atlas's Three Poles at Mode 3

| Pole         | Representative | Surface Type          | Singular Face?            | Closure        |
|-------------|----------------|-----------------------|---------------------------|----------------|
| Diffusive   | FP/PME         | Contracting           | None                      | Lyapunov + smoothing |
| Hyperbolic  | HJ/Burgers     | Non-contracting       | Shock/kink (required)     | Convexity + entropy |
| **Dispersive** | **NLS**     | **Isoenergetic**      | **Collapse (focusing, d>=2)** | **Conservation + Strichartz** |

The three poles have *three different constraint surface geometries*:
- Diffusive: the surface *contracts* (Lyapunov decreases → attractor).
- Hyperbolic: the surface *folds* (characteristics cross → shock → entropy resolution).
- **Dispersive: the surface *oscillates on a conserved level set* (energy preserved → no contraction, no folding → solitons + scattering).**

### 6.3 NLS and ED: Oscillatory Horizons at Mode 3

At the Mode 3 level, the NLS–ED parallel becomes precise:

- **ED constraint surface:** The skyline profile is a *static geometric object* defined by the multiplicative structure of Z. The "dynamics" are the evaluation of sums/densities as the horizon (sieve boundary) advances. The constraint surface is *fixed and complete* — every feature is determined by the axioms of arithmetic.

- **NLS constraint surface:** The wave function psi evolves on a *conserved level set* {M = const, H = const, P = const}. The dynamics are *oscillatory* — the wave function circulates on the level set, dispersing and refocusing, without ever settling to a fixed point. The constraint surface is *fixed in topology* (conservation laws preserve the level set) but *dynamically active* (the solution moves within the level set forever).

Both architectures have *fixed constraint surfaces* — not contracting (parabolic), not folding (hyperbolic), but *structurally static* in their topology. The dynamics in ED are the "exploration" of a fixed arithmetic landscape; the dynamics in NLS are the "exploration" of a fixed isoenergetic surface. Both are *conservative explorations of fixed geometric objects*.

### 6.4 Summary Table

| Feature                    | NLS              | FP    | PME   | HJ    | Burgers| NS    | MCF   | AC/CH |
|----------------------------|--------------------|-------|-------|-------|--------|-------|-------|-------|
| Constraint surface type    | **Isoenergetic**   | Contracting| Contracting| Variational| Entropic| Open(3D)| Geometric| Contracting|
| Closure mechanism          | **Conserv.+Strichartz** | Linearity| Dissipation| Conv.+visc.| L^1+entropy| Open| Area| Lyapunov|
| Dissipation                | **None**           | Volumetric| Volumetric| None| Shock| Volumetric| Geometric| Volumetric|
| Reversibility              | **Yes**            | No    | No    | No    | No     | No    | No    | No    |
| Conservation laws          | **3 (M,H,P)**     | 1 (M) | 1 (M) | 0    | 1 (M)  | 2     | 0     | 0-1   |
| Singular face (focusing)   | Collapse (d>=2)   | None  | None  | Kink  | Shock  | Open  | Curvature| None  |
| Soliton manifold           | **Yes**            | No    | No    | No    | No     | No    | No    | No    |

NLS is the *unique isoenergetic, conservative, reversible, soliton-supporting* constraint surface in the Atlas — the dispersive pole's contribution to the Atlas's structural geometry.

---

*End of Mode 3: Channels → Constraint Surface. The AD Criteria and Verdict will follow in the final file.*
