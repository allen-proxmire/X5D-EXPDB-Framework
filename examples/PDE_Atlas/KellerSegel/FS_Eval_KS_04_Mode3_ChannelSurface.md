# AD Evaluation: Keller–Segel System — Mode 3: Channels → Constraint Surface

Allen Proxmire

April 2026

---

## Overview

Mode 3 constructs the constraint surface of the KS architecture. The KS constraint surface is the *most nonlocal* of any architecture in the Atlas and the *only surface whose blowup face is driven by a nonlocal self-attraction mechanism*. Where the HJ/Burgers blowup face is driven by *local* gradient steepening, the NLS blowup face by *local* self-focusing, and the MCF blowup face by *local* curvature concentration, the KS blowup face is driven by *nonlocal aggregation* — the density generates a global potential through a Poisson equation, and then drifts in the gradient of its own potential. The nonlocality is not a secondary feature (as in NS, where pressure enforces a constraint) but the *primary dynamical mechanism*.

We continue with:

    u_t = Delta u - div(u nabla v),    -Delta v = u

on R^2, with u >= 0, integral u = M.

---

## 1. Channel Decomposition

### Channel D: Diffusion (Local, Stabilizing)

    D(u) = Delta u

- **Locality:** Local. Second-order spatial derivatives at each point.
- **Linearity:** Linear.
- **Stability role:** Stabilizing. Spreads the density, opposing concentration. Damps mode k at rate k^2. The diffusion is the *sole stabilizing mechanism* — the only channel that prevents blowup.
- **Scale action:** Rate ~ k^2. Strongest at small scales (large k), weakest at large scales (small k). The diffusion preferentially smooths fine-grained structure while having little effect on the overall mass distribution.
- **Interaction with A:** The diffusion and aggregation compete at every scale. At small scales, D dominates (k^2 grows faster than the aggregation rate). At large scales, A dominates (the nonlocal potential amplifies long-wavelength perturbations through the 1/k^2 Green's function). The *crossover scale* depends on the mass M — for M < 8 pi, diffusion wins at all scales; for M > 8 pi, aggregation wins at the critical scale.

### Channel A: Aggregation (Nonlocal, Destabilizing)

    A(u) = -div(u nabla v) = -div(u nabla(-Delta)^{-1} u)

- **Locality:** *Nonlocal.* The drift velocity nabla v at x depends on u(y) for all y through the Green's function:

      nabla v(x) = -(1/(2 pi)) integral (x - y) / |x - y|^2 u(y) dy

  Every cell at y contributes to the drift at x through the logarithmic potential. The interaction is *long-range* — the Green's function decays only as 1/|x - y| (in the gradient), not exponentially.

- **Linearity:** Nonlinear in u. The aggregation term is *quadratic*: -div(u nabla(-Delta)^{-1} u) involves the product of u with an integral of u. This is a *nonlocal quadratic nonlinearity* — the most dangerous type in the Atlas. Each factor of u amplifies the other: more cells → stronger potential → faster drift → more concentration → even more cells at the concentration point.

- **Stability role:** Destabilizing. The aggregation drives concentration through the positive feedback loop: u → v → nabla v → drift → more u. The destabilization is *nonlocal*: it operates through the global potential v, coupling all points in the domain.

- **Scale action:** The effective aggregation rate at wavenumber k is:

      sigma_A(k) ~ M k^2 / k^2 = M    [independent of k, for the linearized problem]

  More precisely, the linearized KS around u = M/(area) has growth rate sigma(k) = k^2(M/(8 pi) - 1) for mode k (in appropriate units). For M > 8 pi, *all modes are unstable* — the aggregation amplifies perturbations at every scale simultaneously. The instability is *not* scale-selective (unlike Turing instability, which selects a specific wavelength). It is *mass-selective*: all scales are unstable when M > 8 pi, and all are stable when M < 8 pi.

- **Interaction with D:** The aggregation and diffusion rates at mode k are:
  - Diffusion: sigma_D = -k^2 (stabilizing, grows with k).
  - Aggregation: sigma_A = M k^2 / (8 pi) (destabilizing, also grows with k, but proportional to M).
  - Net: sigma = k^2(M/(8 pi) - 1).
  - Stable (sigma < 0) when M < 8 pi. Unstable (sigma > 0) when M > 8 pi.

  The competition is resolved *uniformly across all scales* by the single parameter M/(8 pi). This is the simplest possible instability criterion: one number (M) compared to one threshold (8 pi) determines stability at *every* scale.

### Channel N: Nonlocal Potential (Mediating)

    N: -Delta v = u    =>    v = (-Delta)^{-1} u = -(1/(2 pi)) integral log|x - y| u(y) dy

- **Locality:** *Nonlocal.* The potential v at x is a global integral of u — it depends on the density distribution everywhere. The Green's function G(x, y) = -(1/(2 pi)) log|x - y| decays *logarithmically* — the slowest possible algebraic decay.
- **Linearity:** Linear in u. The Poisson equation -Delta v = u is a linear elliptic PDE; the Green's function integral is a linear operator.
- **Stability role:** Neutral (the potential is a *medium*, not a force). Channel N mediates the aggregation: it converts the density u into the potential v, whose gradient nabla v provides the drift velocity for Channel A. The potential does not independently stabilize or destabilize — it is the *communication link* between cells at different locations.
- **Scale action:** The Poisson equation has the Green's function response 1/k^2 in Fourier space: v-hat(k) = u-hat(k) / k^2. Low-frequency modes (large scale) of u produce *amplified* potential responses (the Green's function amplifies long wavelengths). This 1/k^2 amplification is why the aggregation is strongest at large scales — the potential is most sensitive to the large-scale mass distribution.

**Comparison with NS pressure:**

| Feature                    | KS Potential v              | NS Pressure p              |
|----------------------------|-----------------------------|----------------------------|
| Equation                   | -Delta v = u                | Delta p = -partial_ij(u_i u_j) |
| Source                     | Density u (positive)        | Velocity gradient (any sign) |
| Gradient role              | **Drives drift (attraction)** | **Enforces constraint (repulsion)** |
| Effect on concentration    | **Promotes**                | **Prevents**               |
| Energy role                | Interaction energy -(1/2)integral u v | Pressure does no work (for div u = 0) |
| Scale response             | 1/k^2 amplification        | 1/k^2 amplification       |

The same mathematical mechanism (Poisson equation with 1/k^2 response) produces *opposite physical effects*: attraction in KS, constraint enforcement in NS.

### Channel B: Blowup (Mass Concentration)

    B: ||u(t)||_{L^{infinity}} → infinity as t → T*    (when M > 8 pi)
       u → M_0 delta(x - x_0) + u_residual    (M_0 >= 8 pi)

- **Locality:** The blowup *trigger* is nonlocal (the aggregation that drives it is nonlocal), but the blowup *event* is local (concentration at a specific point x_0).
- **Linearity:** Nonlinear (emerges from the quadratic nonlocal nonlinearity of A).
- **Stability role:** Maximally destabilizing — the ultimate outcome of the aggregation-diffusion competition when aggregation wins.
- **Scale action:** Concentrates at the smallest scales. As blowup approaches, the density profile sharpens: u ~ lambda^{-2} U_*((x - x_0)/lambda) with lambda → 0. The blowup is a *scale-zero singularity* — mass collapsing from all scales into a point.
- **Interaction with all channels:** Channel B is the *terminal outcome* of the D-A-N interaction when M > 8 pi. The diffusion (D) tries to prevent it; the aggregation (A, mediated by N) overwhelms it. The blowup is the *structural endpoint* of the supercritical free-energy descent.

### Channel Summary Table

| Channel | Symbol | Term / Feature               | Locality      | Linearity   | Stability         | Scale Action              |
|---------|--------|------------------------------|---------------|-------------|-------------------|---------------------------|
| Diffusion    | D | Delta u                     | Local         | Linear      | Stabilizing       | Rate ~ k^2 (small-scale)  |
| Aggregation  | A | -div(u nabla v)             | **Nonlocal**  | Nonlinear   | Destabilizing     | Rate ~ M (mass-controlled) |
| Potential    | N | -Delta v = u                | **Nonlocal**  | Linear      | Neutral (medium)  | 1/k^2 amplification        |
| Blowup       | B | u → delta (M > 8pi)        | Local event*  | Nonlinear   | Terminal destab.  | Concentrates at k → ∞     |

*Nonlocal trigger, local event.

### Channel Count Comparison

| Architecture | Local Channels | Nonlocal Channels | Blowup/Singular Channel | Total |
|-------------|---------------|-------------------|-------------------------|-------|
| **KS**      | **1 (D)**     | **2 (A, N)**      | **1 (B)**               | **4** |
| NS          | 2 (A, V)      | 1 (P)             | 0–1 (open)              | 4–5   |
| NLS         | 2 (D, N)      | 0                 | 0–1 (focusing)          | 3–4   |
| KdV         | 2 (A, D_3)    | 0                 | 0                       | 4     |
| FP          | 2 (T, D)      | 0                 | 0                       | 3–4   |

The KS has the *most nonlocal channels* (2) of any architecture in the Atlas. NS has 1; all others have 0. The KS is the *most nonlocal architecture*.

---

## 2. Dissipation Geometry

### 2.1 Dissipative Gradient Flow

The KS is a *Wasserstein gradient flow* of the free energy F[u]:

    F[u] = integral u log u dx - (1/2) integral u v dx

with dissipation:

    dF/dt = -integral u |nabla(log u - v)|^2 dx = -D_KS(t) <= 0

The dissipation rate D_KS is a *nonlocal Fisher information*: it measures the squared gradient of the *effective potential* log u - v, weighted by u. The effective potential combines the entropy gradient (log u) with the chemoattractant (-v) — the two competing forces.

### 2.2 The Aggregation–Diffusion Competition in Dissipation Space

The dissipation geometry is controlled by the *competition between two terms*:

**Entropy (stabilizing):** integral u log u dx. This term is minimized when u is spread uniformly (maximum entropy). The entropy gradient nabla(log u) drives diffusion.

**Interaction energy (destabilizing):** -(1/2) integral u v dx. This term is minimized (most negative) when u is maximally concentrated (minimum interaction distance). The interaction gradient nabla v drives aggregation.

The free energy F = entropy + interaction is the *balance sheet* of this competition:
- When entropy dominates (M < 8 pi): F is bounded below → the dynamics converge to the entropy-dominated equilibrium (steady state).
- When interaction dominates (M > 8 pi): F is unbounded below → the dynamics descend toward -infinity → blowup.

The log-HLS inequality quantifies the competition:

    interaction energy <= (M/(8 pi)) * entropy + C(M)

For M < 8 pi: the interaction is always controlled by the entropy → F bounded below → stability.
For M > 8 pi: the interaction can exceed the entropy → F unbounded below → instability.

### 2.3 Nonlocal Dissipation Geometry

The KS dissipation is *qualitatively different* from every other dissipation in the Atlas:

| Architecture | Dissipation Functional                    | Local or Nonlocal?        |
|-------------|-------------------------------------------|---------------------------|
| FP          | integral rho |nabla(log rho - V)|^2       | Local (V prescribed)       |
| PME         | integral |nabla(u^{(m+1)/2})|^2           | Local                      |
| AC          | M ||mu||^2                                | Local                      |
| CH          | M ||nabla mu||^2                          | Local                      |
| TFE         | integral h^n |nabla Delta h|^2            | Local                      |
| MCF         | integral H^2 dS                           | Local (on surface)         |
| **KS**      | **integral u |nabla(log u - v)|^2**       | **Nonlocal (v = (-Delta)^{-1} u)** |

The KS dissipation involves v = (-Delta)^{-1} u — a nonlocal functional of u. The dissipation rate at each point x depends not just on u(x) and nabla u(x) but on the *entire* density distribution through v. This is the *only nonlocal dissipation functional* in the Atlas.

The nonlocal dissipation means that the KS's "path down the energy landscape" is influenced by *global information* — the system does not just roll downhill locally but responds to the global density distribution at every step. This is why the KS can produce mass concentration from *diffuse initial data*: the nonlocal interaction energy "sees" the total mass M and determines whether the landscape has a floor (M < 8 pi) or not (M > 8 pi).

### 2.4 Comparison of Dissipation Paradigms

| Paradigm              | Mechanism                    | Free Energy Bounded Below? | Blowup? |
|-----------------------|------------------------------|---------------------------|---------|
| Diffusive (FP/PME)   | Local entropy dissipation    | **Yes** (always)          | No      |
| Gradient (AC/CH/TFE) | Local Lyapunov dissipation   | **Yes** (always)          | No      |
| Geometric (MCF)      | Area dissipation             | **Yes** (area >= 0)       | No*     |
| **Aggregation (KS)** | **Nonlocal entropy–interaction** | **M-dependent**       | **M > 8pi: Yes** |
| Entropic (HJ/Burgers)| Entropy at shocks            | N/A (hyperbolic)          | Shocks  |
| None (NLS/KdV)       | No dissipation               | N/A (Hamiltonian)         | NLS: focusing |

*MCF has curvature blowup but the area is bounded below.

The KS demonstrates a *new dissipation paradigm*: **nonlocal dissipation with mass-dependent energy landscape**. The dissipation is always present (dF/dt <= 0), but the energy landscape changes topology (bounded vs. unbounded below) depending on the mass M. This is the *only architecture where the dissipation drives the dynamics toward blowup* rather than toward equilibrium.

---

## 3. Constraint Surface Geometry

### 3.1 Three Mass-Defined Regions

**Region A: Subcritical (M < 8 pi)**

- Diffusion dominates at all scales.
- Free energy F bounded below → solution remains smooth for all time.
- Solution converges to the unique steady state u_eq (minimizer of F subject to integral u = M).
- The constraint surface in this region is *smooth, closed, and completely characterized*.

**Properties:**
- u(t) in L^1 ∩ L^{infinity} for all t >= 0.
- ||u(t)||_{L^p} <= C(p, M, F[u_0]) for all p.
- F[u(t)] → F[u_eq] as t → infinity.
- Exponential convergence for M << 8 pi; algebraic for M near 8 pi.

**Region B: Critical (M = 8 pi)**

- Diffusion and aggregation exactly balance.
- Free energy F bounded below (marginally): F >= 0.
- Second moment V(t) = const (dV/dt = 0).
- The solution converges to the critical steady state — the rescaled Cauchy profile.
- The constraint surface at M = 8 pi is a *codimension-1 boundary* separating the closed subcritical region from the open supercritical region.

**Region C: Supercritical (M > 8 pi)**

- Aggregation dominates at the critical scale.
- Free energy F unbounded below → F → -infinity in finite time → blowup.
- The density u forms a Dirac delta at the blowup point.
- The constraint surface has an *open blowup face* in this region.

**Properties:**
- ||u(t)||_{L^{infinity}} → infinity as t → T* < infinity.
- u → M_0 delta(x - x_0) + u_residual (M_0 >= 8 pi).
- T* <= V(0) / (4M(M/(8 pi) - 1)).
- The blowup profile is characterized (rescaled Cauchy, Type I or Type II).

### 3.2 Assembly into a Single Constraint Surface

The three regions form a single constraint surface parameterized by the mass M:

    M < 8 pi: Region A (closed, smooth, convergent)
    |
    M = 8 pi: Region B (critical boundary, marginally closed)
    |
    M > 8 pi: Region C (open, blowup face)

The mass M is a *conserved parameter* — it does not change along trajectories. Each trajectory lives entirely within one region. The constraint surface is *stratified by mass*: the subcritical stratum is closed, the critical stratum is a boundary, and the supercritical stratum has an open blowup face.

The mass-stratified structure is *unique in the Atlas*:
- NS: the constraint surface is *not* stratified by a conserved quantity (the enstrophy gap is architectural, not parameter-dependent).
- NLS: the constraint surface is stratified by mass (in d = 2), but the mass is the *L^2 norm of a complex field*, not a physical density.
- TFE: the constraint surface is stratified by the *exponent n* (a constitutive parameter, not a conserved quantity).
- **KS: the constraint surface is stratified by the *physical mass M* (a conserved quantity) with the sharp threshold 8 pi determined by a fundamental inequality.**

### 3.3 The Nonlocal Blowup Face

The supercritical blowup face (Region C) has several distinctive features:

1. **Nonlocal trigger:** The blowup is driven by the nonlocal aggregation mechanism — the density generates a global potential that drives the concentration. The trigger is *not local* (unlike HJ/Burgers steepening, NLS self-focusing, or MCF curvature concentration).

2. **Mass-driven:** The blowup threshold is determined by the *total mass* M, a global conserved quantity. The local amplitude, gradient, or curvature of u at any point does *not* determine whether blowup occurs — only the global mass does. This is structurally unique: every other blowup criterion (BKM for NS, virial for NLS, characteristic crossing for HJ) involves *local or space-time-integrated* quantities, not a single global invariant.

3. **Free-energy-driven:** The blowup is the *terminal state of the gradient-flow descent*. The free energy F decreases monotonically toward -infinity, and the blowup is the mechanism by which F reaches -infinity. The Lyapunov structure *causes* the blowup, not merely *permits* it.

4. **Quantized:** The concentrated mass is always >= 8 pi. The blowup is *discretized* — it occurs in quanta of 8 pi.

5. **Characterized:** The blowup rate (at least 1/(T* - t)), the blowup profile (rescaled Cauchy/ground state), and the post-blowup structure (delta mass + residual) are all known.

### 3.4 Comparison of Blowup Faces Across the Atlas

| Architecture | Blowup Face Type          | Trigger    | Threshold            | Characterized? |
|-------------|---------------------------|------------|----------------------|----------------|
| NS (3D)    | Open (vorticity?)          | Local?     | Open                 | No             |
| NLS (foc.) | Amplitude concentration   | Local      | M_* (sharp, d=2)    | Yes (d=2)      |
| HJ/Burgers | Gradient steepening       | Local      | Always (generic data)| Yes            |
| MCF         | Curvature blowup          | Local      | Always (compact)     | Yes            |
| **KS**      | **Mass concentration**    | **Nonlocal**| **M=8pi (sharp)**   | **Yes**        |
| TFE (n<1)  | Positivity failure         | Local      | n = 1 (parametric)   | Partial        |

The KS blowup face is *unique* in being nonlocal, mass-driven, and free-energy-driven. Every other blowup face in the Atlas is either local (HJ/Burgers/NLS/MCF) or uncharacterized (NS 3D).

---

## 4. Anomalies and Open Faces

### 4.1 Sealed Faces

**Oscillatory/dispersive face: Absent.** The KS has no dispersion (no imaginary time derivative, no odd-order spatial derivative). No oscillatory dynamics, no solitons, no wave phenomena.

**Hamiltonian/reversibility face: Absent.** The KS is dissipative (gradient flow), not Hamiltonian. No time-reversibility, no energy conservation, no symplectic structure.

**Chaotic face: Sealed.** The gradient-flow structure (dF/dt <= 0) forbids limit cycles, strange attractors, and recurrence — the same structural guarantee as in AC/CH/PME/TFE/FP.

**Shock face: Absent.** The KS has no first-order self-advection (u u_x). The diffusion Delta u prevents gradient steepening. No Burgers-type shocks.

**Pattern-formation face: Absent (in the standard sense).** The KS does not form Turing-type spatial patterns. The aggregation instability is *not scale-selective* — all modes grow at the same rate when M > 8 pi. The instability produces *concentration at a point*, not a *periodic pattern*. However, the KS on bounded domains can produce *multi-peak steady states* for subcritical mass — these are equilibrium configurations, not dynamically formed patterns.

**Nonlocal-constraint face (NS-type): Absent.** The KS nonlocality is an *attraction mechanism*, not a *constraint enforcement*. There is no incompressibility constraint, no divergence-free condition, no pressure that enforces a kinematic constraint.

### 4.2 The Open Face: Mass-Concentrating Blowup (M > 8 pi)

The single open face of the KS constraint surface is the *blowup face for M > 8 pi*:

    ||u(t)||_{L^{infinity}} → infinity at T* < infinity
    u → M_0 delta(x - x_0) + u_residual    (M_0 >= 8 pi)

The blowup face is:
- **Required** (for M > 8 pi): the free-energy landscape has no lower bound → the gradient flow must descend to -infinity → blowup is *certain*.
- **Characterized:** Blowup rate, profile, mass quantization, and post-blowup structure are known.
- **Sharp:** The threshold M = 8 pi is exact (best constant in log-HLS). No ambiguity, no open question about where the threshold lies.
- **Nonlocal:** The blowup is driven by the nonlocal aggregation mechanism, not by a local instability.

The KS blowup face is *structurally comparable* to the NLS focusing blowup face (both have sharp mass thresholds, both are well-characterized) but *mechanistically different* (KS is nonlocal and Lyapunov-driven; NLS is local and Hamiltonian).

### 4.3 Anomaly Assessment

| Face                    | Status              |
|-------------------------|---------------------|
| Oscillatory/dispersive  | Absent              |
| Hamiltonian/reversible  | Absent              |
| Chaotic                 | Sealed (gradient flow)|
| Shock                   | Absent              |
| Pattern-formation       | Absent (standard)   |
| NS-type nonlocal constraint | Absent          |
| **Mass-concentrating blowup** | **Open (M > 8pi)** |

**Anomaly count (M < 8 pi): zero.** The subcritical KS is anomaly-free — fully closed, smooth, convergent.

**Anomaly count (M > 8 pi): one open face.** The supercritical KS has a single open blowup face — well-characterized but structurally present.

The KS anomaly profile is *mass-dependent*: anomaly-free for M < 8 pi, one anomaly for M > 8 pi. This parallels the NLS (sign-dependent: anomaly-free for defocusing, one anomaly for focusing d >= 2) and the TFE (n-dependent: anomaly-free for n >= 1, one anomaly for n < 1).

---

## 5. Channel Constraints

---

**C1. Non-Negative Density**

    u(x, t) >= 0    for all x, t (as long as the smooth solution exists)

Maximum principle for the advection-diffusion equation.

*Scope: All KS.*

---

**C2. Nonlocal Potential**

    v = (-Delta)^{-1} u = -(1/(2 pi)) integral log|x - y| u(y) dy

The chemoattractant is determined instantaneously by the density through the 2D Poisson equation.

*Scope: All KS (parabolic–elliptic model).*

---

**C3. Diffusion Channel**

    Delta u:    stabilizing, local, rate ~ k^2

Second-order smoothing. The sole stabilizing mechanism.

*Scope: All KS.*

---

**C4. Aggregation Channel**

    -div(u nabla v):    destabilizing, nonlocal, quadratic in u

Chemotactic drift. The sole destabilizing mechanism. Nonlocal through v = (-Delta)^{-1} u.

*Scope: All KS.*

---

**C5. Free-Energy Dissipation**

    dF/dt = -integral u |nabla(log u - v)|^2 dx <= 0

Wasserstein gradient-flow structure. F decreases monotonically.

*Scope: All KS.*

---

**C6. Log-HLS Inequality (Sharp Constant)**

    interaction energy <= (M/(8 pi)) * entropy + C(M)

Determines the critical mass. Sharp constant M/(8 pi).

*Scope: All KS (2D).*

---

**C7. Critical Mass M = 8 pi**

    M < 8 pi: F bounded below → global existence
    M > 8 pi: F unbounded below → blowup

The sharp threshold partitioning the constraint surface.

*Scope: 2D parabolic–elliptic KS.*

---

**C8. Subcritical Global Existence**

    M < 8 pi    =>    u(t) exists globally, converges to u_eq

Unconditional for M < 8 pi.

*Scope: Subcritical regime.*

---

**C9. Supercritical Blowup**

    M > 8 pi and V(0) < infinity    =>    T* < infinity (finite-time blowup)

Certain blowup for supercritical mass with finite second moment.

*Scope: Supercritical regime.*

---

**C10. Mass Quantization at Blowup**

    Concentrated mass M_0 >= 8 pi at each blowup point

The minimum quantum of concentration is 8 pi. Multiple blowup points each absorb >= 8 pi.

*Scope: At blowup.*

---

**C11. Multi-Center Aggregation**

    For M >> 8 pi: up to floor(M/(8 pi)) simultaneous blowup points possible

Multiple concentration centers, each absorbing at least 8 pi of mass.

*Scope: Large supercritical mass.*

---

**C12. Measure-Valued Continuation**

    Post-blowup: u(t) = u_regular(t) + sum_j M_j delta(x - x_j(t))

Delta masses persist and drift; regular part continues evolving. Possible blowup cascade if residual mass >= 8 pi.

*Scope: Post-blowup.*

---

### Channel Constraint Summary

| Label | Constraint                        | Type              | Scope            |
|-------|-----------------------------------|-------------------|------------------|
| C1    | Non-negative density              | Maximum principle | All KS           |
| C2    | Nonlocal potential                | Elliptic solve    | All KS           |
| C3    | Diffusion channel                 | Stabilizing       | All KS           |
| C4    | Aggregation channel               | Destabilizing     | All KS           |
| C5    | Free-energy dissipation           | Exact identity    | All KS           |
| C6    | Log-HLS inequality                | Sharp bound       | 2D KS            |
| C7    | Critical mass 8 pi               | Threshold          | 2D KS            |
| C8    | Subcritical global existence      | Existence         | M < 8 pi         |
| C9    | Supercritical blowup              | Singularity       | M > 8 pi         |
| C10   | Mass quantization                 | Quantization      | At blowup        |
| C11   | Multi-center aggregation          | Structure         | M >> 8 pi        |
| C12   | Measure-valued continuation       | Post-blowup       | After T*         |

---

## 6. Comparison with FP, PME, HJ, Burgers, NLS, KdV, NS, MCF, AC/CH, TFE, RD, and ED

### 6.1 The Five Poles at Mode 3

| Pole         | Representative | Surface Type                   | Nonlocal? | Blowup Face?        |
|-------------|----------------|--------------------------------|-----------|----------------------|
| Diffusive   | FP/PME         | Contracting (Lyapunov)         | No        | None                 |
| Hyperbolic  | HJ/Burgers     | Shock-resolved (entropy)       | No        | Shock (local, resolved) |
| Dispersive  | NLS/KdV        | Isoenergetic (Hamiltonian)     | No        | NLS focusing (local) |
| Geometric   | MCF            | Area-decreasing (geometric)    | No        | Curvature (local)    |
| **Aggregation** | **KS**     | **Mass-stratified (nonlocal)** | **Yes (2 channels)** | **Mass concentration (nonlocal)** |

The KS is the *only architecture with a nonlocal blowup face*. Every other architecture's blowup (when it occurs) is driven by a *local mechanism* (gradient steepening, self-focusing, curvature concentration). The KS blowup is driven by a *global mechanism* — the nonlocal self-attraction mediated by the chemoattractant potential.

### 6.2 Nonlocality Comparison

| Architecture | Nonlocal Channels | Nonlocality Role                | Blowup Involvement |
|-------------|-------------------|---------------------------------|---------------------|
| **KS**      | **2 (A, N)**      | **Primary mechanism (aggregation)** | **Direct (drives blowup)** |
| NS          | 1 (P)             | Constraint enforcement (pressure) | Indirect (may prevent or permit) |
| All others  | 0                 | N/A                             | N/A                 |

The KS has the *most nonlocal*, *most dynamically consequential* nonlocal structure in the Atlas. The NS nonlocality (pressure) is a *constraint*; the KS nonlocality is a *force*. The NS pressure *may or may not* be involved in blowup (open question); the KS potential *definitely drives* blowup.

### 6.3 KS and ED: Nonlocal Concentration as Structural Event

The KS mass concentration — density collapsing to a point through nonlocal self-interaction — is the dynamical analogue of the ED *prime activation*: at each p^2, the sieve structure concentrates its action at a specific arithmetic location through the nonlocal multiplicative structure of Z. Both represent *concentration events driven by nonlocal self-interaction*:

- KS: cell density at all locations interacts through the Poisson potential → concentration at a point.
- ED: prime coverage at all scales interacts through multiplication → activation at p^2.

Both architectures demonstrate that *nonlocal self-interaction produces concentration* — the universal structural principle underlying both biological aggregation and arithmetic sieving.

### 6.4 Summary Table

| Feature                    | KS               | NS       | NLS      | KdV      | FP       | PME      | Burgers  | MCF      |
|----------------------------|------------------|----------|----------|----------|----------|----------|----------|----------|
| Nonlocal channels          | **2**            | 1        | 0        | 0        | 0        | 0        | 0        | 0        |
| Nonlocality drives blowup  | **Yes**          | Open     | No       | N/A      | N/A      | N/A      | N/A      | N/A      |
| Blowup type                | **Mass delta**   | Open     | Amplitude| None     | None     | None     | Gradient | Curvature|
| Critical threshold          | **M=8pi**        | Open     | M_*      | N/A      | N/A      | N/A      | N/A      | N/A      |
| Gradient flow              | **Wasserstein**  | No       | No       | No       | Wass.    | Wass.    | No       | L^2      |
| F bounded below            | **M-dependent**  | N/A      | Indef.   | N/A      | Yes      | Yes      | N/A      | Yes      |
| Lyapunov drives blowup     | **Yes (M>8pi)**  | N/A      | No       | N/A      | No       | No       | N/A      | No       |
| Dissipation type           | **Nonlocal**     | Local    | None     | None     | Local    | Local    | Shock    | Geometric|

KS is the *unique nonlocal-aggregating, mass-concentrating, Lyapunov-driven, mass-quantized, nonlocal-dissipation* architecture in the Atlas.

---

*End of Mode 3: Channels → Constraint Surface. The AD Criteria and Verdict will follow in the final file.*
