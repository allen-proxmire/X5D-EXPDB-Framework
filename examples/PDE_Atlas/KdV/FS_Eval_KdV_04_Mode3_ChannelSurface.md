# AD Evaluation: Korteweg–de Vries Equation — Mode 3: Channels → Constraint Surface

Allen Proxmire

April 2026

---

## Overview

Mode 3 constructs the constraint surface of the KdV architecture. The KdV constraint surface is the *most completely sealed* of any nonlinear PDE in the PDE Atlas — sealed not by one or two closure mechanisms but by *integrability*, which provides infinite conservation laws, an exact linearization (IST), and a complete classification of all solutions. The KdV constraint surface has *zero open faces, zero anomalies, and zero unresolved structural questions*. It is the only nonlinear PDE whose constraint surface is *fully classified* — every point on the surface corresponds to a known solution type (soliton, radiation, or their combination), and the dynamics on the surface are exactly determined by the IST.

We continue with:

    u_t + 6 u u_x + u_{xxx} = 0

---

## 1. Channel Decomposition

### Channel A: Nonlinear Advection (Burgers Heritage)

    A(u) = 6 u u_x = partial_x(3 u^2)

- **Locality:** Local. u u_x depends on u and u_x at each point.
- **Linearity:** Nonlinear. Quadratic (u times u_x). The sole nonlinear channel.
- **Stability role:** Destabilizing (steepening). The advection tilts the wave profile: the crest (large u) travels faster than the trough (small u), steepening the leading edge. Without D_3, this produces Burgers shocks. With D_3, the steepening is arrested and solitons form.
- **Scale action:** First-order in k. The advection rate is proportional to u k — amplifying high-k modes (steepening) at rate proportional to the local amplitude.
- **Interaction with D_3:** The advection and dispersion channels *compete*: A steepens, D_3 spreads. The competition is *exactly balanced* at the soliton scale (rho = UL^2 ~ 1), producing the sech^2 traveling wave. At other scales, one channel dominates: A at large scales (long-wave steepening), D_3 at small scales (short-wave spreading).
- **Interaction with H:** The advection is the *nonlinear part* of the first Hamiltonian structure: u_t = partial_x(delta H_2 / delta u), where the nonlinear contribution to delta H_2 / delta u is 3u^2. The advection is *Hamiltonian-generated* — it is not an arbitrary nonlinearity but one that is compatible with the symplectic structure.

### Channel D_3: Third-Order Dispersion

    D_3(u) = u_{xxx}

- **Locality:** Local. Third-order spatial derivatives at each point.
- **Linearity:** Linear. The third derivative is a linear operator.
- **Stability role:** Stabilizing (dispersive). The Airy dispersion spreads wave packets at rate t^{-1/3}, preventing the advection's steepening from forming shocks. The dispersion is the *anti-shock mechanism*: it regularizes the Burgers singularity by spreading the energy across frequencies.
- **Scale action:** Mode k has dispersion relation omega = -k^3 (cubic). Phase velocity v_ph = -k^2 and group velocity v_gr = -3k^2. High-frequency modes travel faster (in the negative direction), producing the characteristic *Airy wake* behind the soliton.
- **Interaction with A:** The dispersion and advection are *mutually conditioning*: the dispersion determines the *shape* of the soliton (the sech^2 profile is the unique shape for which the advective steepening and dispersive spreading exactly cancel), while the advection determines the *speed* (the soliton speed c = 4 kappa^2 is set by the amplitude through the advection mechanism).
- **Interaction with H:** The dispersion is the *linear part* of the first Hamiltonian structure: the u_{xxx} term comes from the functional derivative of H_2 = integral [(1/2)u_x^2 - u^3] dx (the u_x^2 term produces u_{xxx} upon variation and application of partial_x).

### Channel H: Bi-Hamiltonian Structure

    H: u_t = J_1 (delta H_2 / delta u) = J_2 (delta H_0 / delta u)

with J_1 = partial_x and J_2 = partial_x^3 + (2/3)(u partial_x + partial_x u).

- **Locality:** Local. Both J_1 and J_2 are local differential operators (J_1 involves partial_x; J_2 involves partial_x^3 and u partial_x — all local).
- **Linearity:** J_1 is linear (partial_x). J_2 is *linear as an operator on functions* but depends on u through the coefficient (2/3)(u partial_x + partial_x u). The Hamiltonians H_n are nonlinear functionals of u.
- **Stability role:** Conservative (infinitely rigid). The bi-Hamiltonian structure generates *infinitely many conservation laws* through the Lenard recursion:

      J_2 (delta H_n / delta u) = J_1 (delta H_{n+1} / delta u)    for all n >= 0

  Each H_n is an independent conserved quantity. The infinite hierarchy provides *complete Sobolev control*: H_n controls the H^{n-1} norm, so all norms are bounded for all time.

- **Scale action:** All-scale. Each conservation law H_n controls a different Sobolev level. The infinite hierarchy controls *every* scale simultaneously — an infinite-dimensional version of "conserving everything."
- **Interaction with A and D_3:** The bi-Hamiltonian structure *organizes* the advection and dispersion into a single coherent framework. The KdV equation is not "advection plus dispersion" in an ad hoc sense — it is the *unique third-order Hamiltonian flow* compatible with both J_1 and J_2. The advection and dispersion are *structurally required* by the bi-Hamiltonian compatibility condition.

### Channel I: Integrability (IST + Lax Pair)

    I: L = -partial_{xx} + u,    L_t = [A, L]    (Lax pair)
       u(0) → scattering data → linear evolution → scattering data(t) → u(t)    (IST)

- **Locality:** The *KdV PDE* is local. The *IST* is a nonlocal analytical tool (it involves solving the Schrödinger eigenvalue problem on all of R). But the IST is a *structural property* of the architecture, not a dynamical channel — it does not introduce nonlocal coupling into the PDE.
- **Linearity:** The IST *linearizes* the nonlinear KdV: the scattering data evolve linearly in time. The integrability converts nonlinear dynamics (in physical space) to linear dynamics (in scattering space).
- **Stability role:** Maximally stabilizing. The IST provides:
  - *Exact solutions* for all time (no approximation).
  - *Complete classification* of all solutions (solitons + radiation).
  - *Exact interaction formulas* (phase shifts).
  - *Exact long-time asymptotics* (soliton resolution).
  - *Global smoothness* (the IST maps smooth data to smooth solutions).
- **Scale action:** Complete. The IST controls *every aspect* of the solution — amplitude, phase, location, interaction, asymptotic behavior — at every scale and for all time.
- **Interaction with all channels:** Channel I is the *meta-channel* that organizes all other channels. It does not add a new PDE term; it reveals the *hidden linear structure* within the nonlinear combination of A and D_3 governed by H. The integrability is the *structural glue* that makes the KdV more than the sum of its parts.

### Channel Summary Table

| Channel | Symbol | Term / Feature           | Locality    | Linearity    | Stability            | Scale Action          |
|---------|--------|--------------------------|-------------|--------------|----------------------|-----------------------|
| Advection    | A   | 6u u_x                  | Local       | Nonlinear    | Destabilizing (steep.)| Rate ~ u k            |
| Dispersion   | D_3 | u_{xxx}                 | Local       | Linear       | Stabilizing (dispersive)| omega = -k^3        |
| Bi-Hamiltonian| H  | J_1, J_2 compatible     | Local       | Mixed        | Conservative (infinite)| All-scale (infinite H_n)|
| Integrability | I  | Lax pair + IST          | Structural* | Linearizing  | Maximally stabilizing| Complete control       |

*The PDE is local; the IST is a nonlocal analytical tool, not a dynamical coupling.

### Channel Count Comparison

| Architecture | Dynamical | Structural | Integrability | Total |
|-------------|-----------|------------|---------------|-------|
| **KdV**     | **2 (A, D_3)** | **1 (H)** | **1 (I)**| **4** |
| NLS         | 2 (D, N)  | 2 (H, G)   | 1 (1D)        | 4-5   |
| Burgers     | 1 (T)     | 2 (S, V)    | 1 (Cole–Hopf)| 3-4   |
| HJ          | 1 (T)     | 2 (S, V)    | 0             | 3     |
| FP          | 2 (T, D)  | 2 (C, P)    | 0             | 4     |
| PME         | 1 (D_nl)  | 2 (C, G)    | 0             | 3+1   |
| MCF         | 1 (K)     | 2 (G, T)    | 0             | 3     |

KdV has four channels — tied with NLS and FP. But the KdV's integrability channel I is *qualitatively deeper* than any other architecture's structural channels: it provides *exact linearization* and *complete classification*, not just conservation laws or symmetries.

---

## 2. Dissipation Geometry

### 2.1 Zero Dissipation

The KdV has *zero dissipation in every category*:

| Dissipation Type         | KdV Status              | Reason                          |
|--------------------------|-------------------------|---------------------------------|
| Volumetric diffusion     | Absent                  | No real Laplacian (KdV-9)       |
| Energy decay (Lyapunov)  | Absent                  | dH_n/dt = 0 for all n (KdV-5,6)|
| Entropy production       | Absent                  | Hamiltonian (KdV-5)             |
| Shock dissipation        | Absent                  | No shocks (KdV-3 prevents)      |
| Geometric dissipation    | Absent                  | No surface state (KdV-1)        |
| Mass decay               | Absent                  | dH_0/dt = 0 (KdV-6)            |

The KdV shares this *total absence of dissipation* with only one other architecture: the NLS (which also has zero dissipation in every category). The HJ has zero classical dissipation but has *variational structure* (Hopf–Lax) that serves as a substitute. The KdV has neither dissipation nor a variational substitute — it has *integrability*, which is a *stronger* structural tool than either.

### 2.2 Dispersive Spreading as Structural Control

Despite having no dissipation, the KdV controls its dynamics through *dispersive spreading*:

    ||e^{-t partial_x^3} f||_{L^{infinity}} <= C |t|^{-1/3} ||f||_{L^1}

The Airy kernel spreads the linear flow at rate t^{-1/3}. This spreading is:
- **Non-dissipative:** The L^2 norm is preserved.
- **Oscillatory:** The spreading occurs through phase cancellation, not amplitude decay.
- **Asymmetric:** The Airy function has an oscillatory tail on the negative x-axis and exponential decay on the positive x-axis — the KdV dispersion is directional.
- **Slower than NLS:** t^{-1/3} vs. t^{-1/2} (in 1D). The cubic dispersion spreads more slowly than the quadratic dispersion.

But the KdV's primary control mechanism is *not* dispersive spreading — it is *integrability*. The infinite conservation laws provide *uniform-in-time control of every Sobolev norm*, which is far stronger than any dispersive estimate. The dispersive spreading controls the *radiation component* (the part that disperses); the conservation laws control *everything* (solitons + radiation + their interaction).

### 2.3 The Integrability Substitute for Dissipation

Where parabolic architectures use *dissipation* (Lyapunov functional decrease → convergence to equilibrium) and hyperbolic architectures use *entropy* (shock dissipation → information loss → simplification), the KdV uses *integrability* (infinite conservation laws → infinite rigidity → exact determination of dynamics).

The three closure paradigms:

| Paradigm              | Mechanism                    | Effect                        | Representative |
|-----------------------|------------------------------|-------------------------------|----------------|
| Dissipative           | Energy decrease               | Convergence to equilibrium    | FP/PME/AC/CH   |
| Entropic              | Information loss at shocks   | Simplification via coarsening | HJ/Burgers     |
| **Integrable**        | **Infinite conservation laws**| **Exact determination of dynamics** | **KdV**   |

The integrable paradigm is *strictly stronger* than both alternatives: it does not merely control the dynamics (as dissipation does) or select a unique continuation (as entropy does); it *determines the dynamics exactly*. The KdV solution is not "controlled" — it is *known*.

### 2.4 Comparison of Dissipation Geometries

| Architecture | Dissipation Geometry              | # Conserved Quantities | Exact Solution? |
|-------------|-----------------------------------|-----------------------|-----------------|
| FP          | Volumetric (entropy → Fisher info)| 1 (mass)              | Yes (spectral)  |
| PME         | Volumetric (entropy → L^1)       | 1 + entropy family    | No              |
| HJ          | None (variational substitute)     | 0                     | Yes (Hopf–Lax)  |
| Burgers     | Shock-concentrated               | 1 (mass)              | Yes (Cole–Hopf) |
| NLS         | None (dispersive substitute)     | 3                     | 1D: Yes (IST)   |
| MCF         | Geometric (area → integral H^2)  | 0                     | No              |
| **KdV**     | **None (integrability substitute)** | **Infinite**        | **Yes (IST)**   |
| NS          | Volumetric (viscous)             | 2                     | No              |

---

## 3. Constraint Surface Geometry

### 3.1 Three Dynamical Regions

**Region A: Dispersion-Dominated (Airy Regime, rho >> 1)**

Low amplitude or short wavelength. The linear KdV (u_{xxx}) dominates the nonlinear advection (u u_x). The solution spreads as an Airy wave: ||u||_{L^{infinity}} ~ t^{-1/3}. No coherent structures form — the wave energy disperses across all frequencies.

**Constraint surface properties:** Smooth, globally well-posed, asymptotically linear. The radiation component of the IST decomposition lives in this region. The constraint surface is *smooth and completely characterized* by the reflection coefficient r(k).

**Region B: Balanced (Soliton Regime, rho ~ 1)**

Amplitude and scale matched so that advection and dispersion are commensurate. Solitons form — localized traveling waves with the sech^2 profile. Multi-soliton interactions occur in this region.

**Constraint surface properties:** The soliton manifold is a *finite-dimensional submanifold* of the infinite-dimensional phase space. For N solitons, the manifold has dimension 2N (each soliton has two parameters: kappa_j and position x_{0,j}). The dynamics on the soliton manifold are *exactly known*: each soliton travels at constant speed, and interactions produce exact phase shifts. The constraint surface in this region is *completely classified*.

**Region C: Steepening-Dominated (Dispersive Shock Regime, rho << 1)**

Large amplitude at long wavelength. The advection dominates the dispersion *initially* — the wave steepens. But the dispersion *always* catches up at small scales (because t_disp ~ L^3 → 0 faster than t_nonlin ~ L/U → 0 as L → 0). The result is a *dispersive shock wave* (DSW): an oscillatory wave train that replaces the Burgers shock with a modulated zone of rapid oscillations.

**Constraint surface properties:** The DSW is described by the *Whitham modulation equations* — a system of quasi-linear PDEs for the slowly varying parameters of the oscillations. The Whitham equations are themselves *integrable* (they have a Riemann-invariant structure), providing complete characterization of the DSW region. The constraint surface in this region is *fully classified through Whitham theory*.

### 3.2 Assembly: A Fully Classified Constraint Surface

The three regions assemble into a *single, fully classified constraint surface*:

    Region A (radiation) ∪ Region B (solitons) ∪ Region C (DSW)

The IST provides the *global classification*: every point on the constraint surface corresponds to a unique combination of:
- Discrete spectrum (soliton parameters kappa_1, ..., kappa_N).
- Continuous spectrum (reflection coefficient r(k)).

The dynamics on the surface are *exactly linear in scattering space*: the eigenvalues kappa_j are constant, the norming constants evolve as c_j(t) = c_j(0) exp(8 kappa_j^3 t), and the reflection coefficient evolves as r(k, t) = r(k, 0) exp(8ik^3 t).

**The KdV constraint surface is the only one in the Atlas that is *fully classified*:** every point on the surface has an exact label (scattering data), and the dynamics at every point are exactly known (linear evolution of scattering data).

### 3.3 Why the Surface Has No Open Faces

**No shock face:** The third-order dispersion prevents characteristic crossing → no Burgers-type shocks. The dispersive shock wave (DSW) is *smooth* — it oscillates but does not develop discontinuities.

**No blowup face:** The infinite conservation laws control every Sobolev norm → no norm can diverge → no blowup of any kind.

**No dissipation face:** The Hamiltonian structure preserves energy → no energy loss → no dissipation.

**No entropy face:** No entropy production → no information loss → no irreversibility.

**No nonlocal face:** All dynamical channels are local (the IST is an analytical tool, not a dynamical coupling).

**No oscillatory/chaotic face:** The integrability provides *infinitely many action-angle variables* — the dynamics are *quasi-periodic* on invariant tori, not chaotic. Integrable systems cannot be chaotic (the KAM theorem and the Liouville integrability theorem prevent chaotic behavior for integrable Hamiltonian systems).

Every potential open face is sealed by a specific structural feature:

| Potential Face       | Sealed By                        |
|---------------------|----------------------------------|
| Shock               | Third-order dispersion (D_3)     |
| Blowup              | Infinite conservation laws (H)   |
| Dissipation          | Hamiltonian structure (H)        |
| Entropy              | Hamiltonian structure (H)        |
| Nonlocal             | Locality of the PDE (KdV-2)     |
| Chaos                | Integrability (I)                |

### 3.4 Comparison with Other Constraint Surfaces

| Architecture | Surface Classification    | Open Faces | Fully Classified? |
|-------------|---------------------------|------------|-------------------|
| **KdV**     | **Complete (IST)**        | **0**      | **Yes**           |
| NLS (def.)  | Complete (scattering)     | 0          | Partial (1D only) |
| NLS (foc.1D)| Complete (IST)           | 0          | Yes (1D only)     |
| FP          | Complete (spectral theory)| 0          | Yes (linear)      |
| PME         | Characterized (Barenblatt)| 0          | No (approximate)  |
| HJ          | Characterized (Hopf–Lax) | 0*         | Yes (viscosity)   |
| Burgers     | Characterized (entropy)   | 0*         | Yes (Kruzkov)     |
| MCF         | Partially characterized   | 0**        | No (surgery only)  |
| NS (3D)    | Uncharacterized           | 1+         | No                |
| RD          | Constitutive              | 3+         | No                |

*Shocks are "faces" in the regularity sense but are fully resolved by entropy/viscosity.
**MCF singularity face is required but fully resolved by surgery/level-set.

The KdV has the *most completely classified* constraint surface: every point labeled, every trajectory computed, every interaction quantified. The only competitors are the FP (linear — spectral theory gives exact solutions) and the 1D focusing NLS (integrable — IST gives exact solutions). But the KdV is *the first* integrable PDE to be solved via IST, and its theory is the most developed.

---

## 4. Anomalies and Open Faces

### 4.1 Zero Open Faces

The KdV constraint surface has *zero open faces*:

| Face                | Status    | Sealed By                                |
|---------------------|-----------|------------------------------------------|
| Shock               | Sealed    | Third-order dispersion prevents shocks   |
| Blowup              | Sealed    | Infinite conservation laws (all H^s bounded) |
| Dissipation          | Absent    | Hamiltonian (no dissipation mechanism)   |
| Entropy              | Absent    | No entropy production                    |
| Nonlocal             | Absent    | All channels local                       |
| Chaotic              | Sealed    | Integrability → quasi-periodic dynamics  |
| Pattern-formation    | Absent    | One species, no reaction                 |
| Amplitude divergence | Sealed    | H_1 = integral u^2 = const → L^2 bound  |
| Gradient divergence  | Sealed    | H_2 controls H^1; H_n controls H^{n-1}  |
| Focusing collapse    | Absent    | Real field, no focusing nonlinearity     |

**Anomaly count: zero.** The KdV has *no open faces, no anomalies, and no unresolved structural questions*. This is the strongest closure verdict in the Atlas for any nonlinear PDE.

### 4.2 Integrability as the Universal Seal

The integrability channel I is the *universal seal* that closes every potential anomaly:

1. **Infinite conservation laws** close the blowup and gradient-divergence faces (every Sobolev norm is controlled).
2. **The Lax pair** closes the chaos face (the spectrum of L is constant → the dynamics are isospectral → quasi-periodic, not chaotic).
3. **The IST** closes the classification face (every solution is uniquely decomposed into solitons + radiation with exact formulas).
4. **The bi-Hamiltonian structure** closes the dissipation and entropy faces (two compatible symplectic forms → the dynamics are doubly conservative).

No other architecture has a single structural feature that closes *all* potential anomalies simultaneously. The integrability is the *universal closure mechanism* — the architectural equivalent of a master key that opens (seals) every lock.

### 4.3 KdV as the Only Fully Sealed Nonlinear PDE

Among nonlinear PDEs in the Atlas:
- PME, AC, CH, TFE (n >= 1): fully sealed *within their scope* (no blowup, no shocks), but do not have exact solutions or complete classification. The constraint surface is controlled but not fully classified.
- NLS (defocusing): fully sealed, but the classification is not complete in all dimensions (Strichartz-based, not IST-based, for d >= 2).
- HJ, Burgers: fully sealed through entropy/viscosity, but the singularity (shock/kink) is a structural face that must be *resolved* (not *absent*).
- MCF: the curvature singularity is a required face.
- **KdV: fully sealed, fully classified, with no singularities of any kind and exact solutions for all data.**

The KdV is the *only* nonlinear PDE whose constraint surface is simultaneously:
1. Fully sealed (zero open faces).
2. Fully classified (every point labeled by scattering data).
3. Singularity-free (no shocks, no blowup, no curvature concentration).
4. Exactly solvable (IST provides the exact solution for all time).

---

## 5. Channel Constraints

---

**C1. Real Scalar Field**

    u : R x R → R

Real-valued. No phase, no gauge, no complex structure.

*Scope: All KdV.*

---

**C2. Locality**

    u_t depends on u, u_x, u_{xx}, u_{xxx} at each point only. No nonlocal operators.

*Scope: All KdV.*

---

**C3. First Hamiltonian Structure**

    u_t = J_1 (delta H_2 / delta u),    J_1 = partial_x

The first (simplest) Hamiltonian formulation.

*Scope: All KdV.*

---

**C4. Bi-Hamiltonian Structure**

    u_t = J_2 (delta H_0 / delta u),    J_2 = partial_x^3 + (2/3)(u partial_x + partial_x u)

The second Hamiltonian formulation, compatible with J_1. Generates the Lenard recursion.

*Scope: All KdV.*

---

**C5. Infinite Conservation Laws**

    H_n = integral P_n(u, u_x, ..., u^{(n)}) dx = const    for all n >= 0, all t

Infinitely many independent conserved quantities. H_n controls the H^{n-1} Sobolev norm.

*Scope: All KdV.*

---

**C6. Lax Pair**

    L_t = [A, L]    where L = -partial_{xx} + u, A = -4 partial_{xxx} + 6u partial_x + 3u_x

The spectrum of L is constant in time (isospectral flow).

*Scope: All KdV.*

---

**C7. IST Linearization**

    u(x, 0) → scattering data → linear evolution → scattering data(t) → u(x, t)

The nonlinear KdV is linearized in scattering space. Exact solution for all time.

*Scope: All KdV (Schwartz-class or appropriate decay).*

---

**C8. Soliton Branch**

    u_soliton = 2 kappa^2 sech^2(kappa(x - 4 kappa^2 t - x_0))

Localized, shape-preserving, speed-locked to amplitude. One-parameter family indexed by kappa > 0.

*Scope: All KdV.*

---

**C9. Elastic Collision Law**

    N solitons in → nonlinear interaction → N solitons out (same shapes, phase shifts only)

Exact phase-shift formula known. No energy transfer, no radiation generated.

*Scope: Multi-soliton solutions.*

---

**C10. Airy Dispersive Decay**

    ||u_radiation(t)||_{L^{infinity}} <= C t^{-1/3}

The radiation component decays at the Airy rate. Controls the non-soliton part of the solution.

*Scope: Radiation component, t → infinity.*

---

**C11. Global Smoothness**

    u_0 in H^s(R), s >= -3/4  =>  u in C(R; H^s(R))

Global existence, uniqueness, and smoothness for all time. No blowup, no singularity.

*Scope: All KdV.*

---

**C12. Soliton Resolution**

    u(x, t) → sum solitons + O(t^{-1/3})    as t → infinity

Every solution decomposes exactly into N solitons + dispersive radiation. The decomposition is complete and exact.

*Scope: All KdV (appropriate decay data).*

---

### Channel Constraint Summary

| Label | Constraint                        | Type              | Scope            |
|-------|-----------------------------------|-------------------|------------------|
| C1    | Real scalar field                 | Structural        | All KdV          |
| C2    | Locality                          | Structural        | All KdV          |
| C3    | First Hamiltonian structure       | Symplectic        | All KdV          |
| C4    | Bi-Hamiltonian structure          | Symplectic (dual) | All KdV          |
| C5    | Infinite conservation laws        | Exact identities  | All KdV          |
| C6    | Lax pair                          | Isospectral       | All KdV          |
| C7    | IST linearization                 | Exact solvability | Schwartz data    |
| C8    | Soliton branch                    | Existence         | All KdV          |
| C9    | Elastic collision law             | Exact formula     | Multi-soliton    |
| C10   | Airy dispersive decay             | Decay bound       | Radiation, t→∞   |
| C11   | Global smoothness                 | Regularity        | All KdV          |
| C12   | Soliton resolution                | Decomposition     | Appropriate data |

**All twelve constraints are unconditional** for the KdV on R with appropriate (Schwartz-class or sufficient-decay) data. No sign dependence, no dimensional dependence, no parametric dependence. The most uniform and comprehensive set of channel constraints of any nonlinear PDE in the Atlas.

---

## 6. Comparison with FP, PME, HJ, Burgers, NLS, NS, MCF, AC/CH, TFE, RD, and ED

### 6.1 Constraint Surface Closure Comparison

| Architecture | # Open Faces | Closure Mechanism              | Fully Classified? |
|-------------|-------------|--------------------------------|-------------------|
| **KdV**     | **0**       | **Integrability (IST + infinite H_n)** | **Yes (IST)** |
| NLS (def.)  | 0           | Conservation + Strichartz      | Partial           |
| NLS (foc.1D)| 0           | Integrability (IST)            | Yes               |
| FP          | 0           | Linearity                      | Yes (spectral)    |
| PME         | 0           | Degeneracy + entropy + L^1     | No                |
| AC          | 0           | Max principle + Lyapunov       | No                |
| CH          | 0           | 4th-order + Lyapunov           | No                |
| TFE (n>=1)  | 0           | 4th-order + degeneracy         | No                |
| HJ          | 0*          | Convexity + viscosity          | Yes (Hopf–Lax)   |
| Burgers     | 0*          | Convex flux + L^1              | Yes (Cole–Hopf)   |
| MCF         | 0**         | Area + Huisken                 | Partial (shrinkers)|
| NS (3D)    | 1+          | Open                           | No                |
| RD          | 3+          | Constitutive                   | No                |

*Shocks present but fully resolved. **Required singularity, fully classified.

### 6.2 The Integrable Pole's Position

The KdV occupies the *integrable pole* of the Atlas:

    Diffusive pole: FP, PME, AC/CH, TFE    → smoothing → equilibrium
    Hyperbolic pole: HJ, Burgers            → steepening → shocks + entropy
    Dispersive pole: NLS                     → oscillatory spreading → solitons + scattering
    Integrable pole: KdV                     → exact solvability → soliton resolution

The integrable pole is *nested within* the dispersive pole (KdV is dispersive) but adds a *qualitatively deeper structural layer*: integrability. The NLS has 3 conservation laws and Strichartz estimates; the KdV has *infinitely many* conservation laws and the *IST*. The upgrade from NLS to KdV is the upgrade from *dispersive control* to *exact solvability*.

### 6.3 KdV and ED: The Two Exactly Classified Architectures

The KdV and ED are the *only two architectures in the Atlas with complete structural classification*:

| Feature                    | ED (Event Density)             | KdV                            |
|----------------------------|---------------------------------|--------------------------------|
| Objects                    | Integers                        | Wave solutions                 |
| "Primes"                   | Prime numbers                   | Solitons                       |
| "Composites"               | Composite integers              | Dispersive radiation           |
| Decomposition theorem      | Fundamental theorem of arithmetic| IST soliton resolution        |
| Uniqueness                 | Unique factorization            | Unique scattering data         |
| Interaction law            | Multiplication (associative)    | Elastic collision (phase shift)|
| Classification             | Complete (every integer factored)| Complete (every solution decomposed) |
| Parameters per "prime"     | 1 (the prime p)                 | 1 (the eigenvalue kappa)       |

Both architectures achieve *complete structural self-knowledge* through a decomposition theorem that breaks every object into irreducible components (primes/solitons) with a unique parameterization. The KdV is the *dynamical analogue of the fundamental theorem of arithmetic* — the PDE whose solutions have a unique "prime factorization" into solitons.

### 6.4 Summary Table

| Feature                    | KdV          | NLS      | Burgers  | HJ       | FP       | PME      | NS       | MCF      |
|----------------------------|-------------|----------|----------|----------|----------|----------|----------|----------|
| Conservation laws          | **Infinite** | 3        | 1        | 0        | 1        | 1        | 2        | 0        |
| Exact solvability          | **IST**     | IST (1D) | Cole–Hopf| Hopf–Lax | Spectral | No       | No       | No       |
| Bi-Hamiltonian             | **Yes**     | No       | No       | No       | No       | No       | No       | No       |
| Soliton resolution         | **Exact**   | 1D: exact| No       | No       | No       | No       | No       | No       |
| Open faces                 | **0**       | 0 (def.) | 0*       | 0*       | 0        | 0        | 1+       | 0**      |
| Fully classified surface   | **Yes**     | Partial  | Yes      | Yes      | Yes      | No       | No       | Partial  |
| Parameters                 | **0**       | 1        | 0        | 0        | 2        | 1        | 2        | 0        |
| Reversible                 | **Yes**     | Yes      | No       | No       | No       | No       | No       | No       |
| Blowup                     | **No**      | Foc.d>=2 | Certain* | Certain* | No       | No       | Open(3D) | Certain  |

The KdV is the *unique* architecture with: infinite conservation laws + exact solvability + bi-Hamiltonian + soliton resolution + zero open faces + fully classified surface + zero parameters + reversibility + no blowup. It is the *most completely characterized nonlinear PDE in mathematics*.

---

*End of Mode 3: Channels → Constraint Surface. The AD Criteria and Verdict will follow in the final file.*
