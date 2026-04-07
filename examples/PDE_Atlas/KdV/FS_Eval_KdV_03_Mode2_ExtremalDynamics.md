# AD Evaluation: Korteweg–de Vries Equation — Mode 2: PDE → Extremal Dynamics

Allen Proxmire

April 2026

---

## Overview

Mode 2 moves from the static envelope to the dynamics. The KdV dynamical landscape is the *most completely understood* of any nonlinear PDE in the Atlas: the inverse scattering transform provides the exact solution for all time, the soliton resolution theorem gives the complete long-time decomposition, and the infinite conservation laws control every regularity level. There are no open questions about the KdV dynamics — every qualitative and quantitative feature is rigorously established. The KdV Mode 2 analysis is therefore not a catalog of what is known and unknown (as in NS or even NLS) but a *complete description* of a fully understood dynamical system.

Throughout:

    u_t + 6 u u_x + u_{xxx} = 0

on R, with u : R x R → R.

---

## 1. Fundamental Time and Length Scales

### 1.1 Two Competing Time Scales

**Dispersive time scale:** The time for the linear KdV dispersion (u_{xxx}) to spread a wave packet of scale L:

    t_disp ~ L^3

The cubic dispersion relation omega = -k^3 gives group velocity v_gr = -3k^2 = -3/L^2 for a wave packet of scale L, so the spreading time is t ~ L / |v_gr| ~ L^3. This is *third-order* scaling — slower than the NLS's second-order (t ~ L^2) and faster than a hypothetical fourth-order dispersion (t ~ L^4). The L^3 scaling is the temporal signature of the KdV's third-order derivative.

**Nonlinear steepening time scale:** The time for the advection (6u u_x) to steepen a profile of amplitude U at scale L:

    t_nonlin ~ L / U = 1 / (U k)

where k = 1/L. This is the same steepening time as Burgers (the advection u u_x has the same structure). If the amplitude U is large or the scale L is small (large k), the steepening is fast.

### 1.2 The Dispersion–Nonlinearity Ratio

    rho = t_disp / t_nonlin = L^3 / (L / U) = U L^2

This ratio determines which mechanism dominates at a given scale and amplitude:

**rho >> 1 (dispersion-dominated, Airy regime):**

Large amplitude or large scale. The dispersive spreading overwhelms the nonlinear steepening. The solution behaves like the linear Airy equation u_t + u_{xxx} = 0: the wave packet spreads at rate t^{-1/3} without forming coherent structures. This is the regime of the *dispersive radiation tail* — the non-soliton component that spreads to zero amplitude.

**rho ~ 1 (balanced, soliton regime):**

The dispersion and nonlinearity are exactly commensurate. The dispersive spreading is precisely counteracted by the advective steepening, producing a *soliton* — a localized, shape-preserving traveling wave. The soliton amplitude U and width L satisfy U L^2 = const (specifically, the soliton profile u = 2 kappa^2 sech^2(kappa x) has U = 2 kappa^2 and L ~ 1/kappa, so U L^2 = 2 — confirming rho ~ 1).

The soliton is the *fixed point* of the dispersion-nonlinearity competition: it is the unique profile for which the two mechanisms exactly cancel. This is the dispersive analogue of the PME Barenblatt profile (balance of nonlinear spreading and mass conservation) and the AC interface profile (balance of reaction and diffusion).

**rho << 1 (steepening regime, Burgers-like):**

Small amplitude at small scale. The advection steepens faster than dispersion can spread. In a pure Burgers equation, this would form a shock. In the KdV, the dispersion *eventually* catches up — at sufficiently small scales, the t_disp ~ L^3 scaling makes dispersion dominant (because L^3 decreases faster than L / U for fixed U as L → 0). The result: the steepening is *arrested* by dispersion before a shock forms, producing instead a *dispersive shock wave* (DSW) — an oscillatory structure that replaces the Burgers shock with a modulated wave train.

### 1.3 Contrast with Other Architectures

| Feature                    | KdV                         | NLS                      | Burgers              | FP/PME                |
|----------------------------|-----------------------------|--------------------------|----------------------|-----------------------|
| Dispersive time            | t ~ L^3 (cubic)             | t ~ L^2 (quadratic)      | None (no dispersion) | t ~ L^2 (diffusion)  |
| Nonlinear time             | t ~ L/U (advective)         | t ~ 1/\|psi\|^2 (algebraic)| t ~ L/U (advective)| t ~ 1/\|\|R'\|\|    |
| Ratio rho                  | U L^2                       | L^2 \|psi\|^2           | N/A (rho = infinity) | N/A (rho = 0)        |
| Soliton at rho ~ 1         | **Yes (sech^2)**           | Yes (sech, complex)      | No (shock instead)   | No (equilibrium)     |
| rho << 1 outcome           | DSW (oscillatory shock)     | Blowup (focusing, d>=2)  | Shock (discontinuity)| Equilibrium          |
| rho >> 1 outcome           | Airy spreading (t^{-1/3})  | Schrödinger spreading (t^{-d/2})| N/A          | Diffusive decay       |

The KdV's *third-order* dispersion (L^3) produces dynamics that are qualitatively intermediate between the NLS's *second-order* dispersion (L^2) and no dispersion at all (Burgers). The KdV dispersive time scale is *slower* than the NLS's at large scales but *faster* at small scales — producing a different balance point and different soliton structures.

---

## 2. Extremal Behaviors

### E1. Airy Dispersive Spreading

For the linear KdV flow e^{-t partial_x^3}:

    ||e^{-t partial_x^3} f||_{L^{infinity}} <= C |t|^{-1/3} ||f||_{L^1}

The decay rate t^{-1/3} is slower than the NLS rate t^{-1/2} (in 1D) because the KdV dispersion is cubic (omega = k^3), not quadratic (omega = k^2). The Airy function Ai(x/(3t)^{1/3}) / (3t)^{1/3} is the fundamental solution — an oscillatory function with slow algebraic decay, concentrated on the negative x-axis (the "dispersive wake" behind the wave).

The Airy spreading is the KdV's *stabilizing mechanism*: it prevents shocks by spreading energy across frequencies and reduces the amplitude of the dispersive radiation to zero as t → infinity.

### E2. Soliton Formation

The KdV soliton:

    u(x, t) = 2 kappa^2 sech^2(kappa(x - 4 kappa^2 t - x_0))

emerges from the *exact balance* between advective steepening (u u_x pushes the leading edge) and dispersive spreading (u_{xxx} resists the steepening). The soliton is:

- **Positive:** u > 0 everywhere in the soliton region. No sign changes.
- **Localized:** Exponentially decaying tails: u ~ 4 kappa^2 exp(-2 kappa |x|) for large |x|.
- **Shape-preserving:** The profile sech^2 is maintained for all time.
- **Speed-locked to amplitude:** c = 4 kappa^2. Taller solitons travel faster — a structural property with no analogue in the NLS (where soliton speed and amplitude are independent).
- **Width-locked to amplitude:** width ~ 1/kappa. Taller solitons are narrower. The amplitude-width product is fixed: (amplitude)(width^2) = 2 (constant).

The number of solitons that emerge from given initial data u_0 is determined by the *number of bound states* of the Schrödinger operator L = -partial_{xx} + u_0: each bound state (negative eigenvalue -kappa_j^2) produces one soliton with amplitude 2 kappa_j^2 and speed 4 kappa_j^2.

### E3. Multi-Soliton Elastic Collisions

The N-soliton solution describes N solitons with parameters kappa_1 > kappa_2 > ... > kappa_N interacting nonlinearly:

**Before collision (t → -infinity):** N separated solitons, ordered by speed (fastest on the right, since speed = 4 kappa^2).

**During collision:** The solitons overlap and interact nonlinearly. The superposition is *not* a simple sum — the interaction produces a complex intermediate profile.

**After collision (t → +infinity):** N separated solitons emerge with *exactly the same* amplitudes, speeds, and shapes. Each soliton has acquired a *phase shift* — a displacement in position:

    delta_j = (1/kappa_j) sum_{i>j} log((kappa_j + kappa_i)/(kappa_j - kappa_i)) - (1/kappa_j) sum_{i<j} log((kappa_i + kappa_j)/(kappa_i - kappa_j))

The collision is *perfectly elastic*: no energy transfer, no radiation generated, no shape change. This elasticity is the signature of *complete integrability* — the infinite conservation laws constrain the interaction so tightly that no deformation is possible.

### E4. Soliton Resolution (IST Decomposition)

For generic Schwartz-class initial data u_0, the IST provides the exact long-time decomposition:

    u(x, t) = sum_{j=1}^N [soliton_j(x, t)] + [dispersive radiation(x, t)] + [interaction terms → 0]

as t → infinity, where:
- N = number of bound states of -partial_{xx} + u_0 (can be zero — no solitons emerge from some data).
- Each soliton_j has amplitude 2 kappa_j^2 determined by the j-th eigenvalue.
- The radiation disperses at rate t^{-1/3}.
- The interaction terms decay faster than the radiation.

The soliton resolution is *exact*: it is not an approximation or an asymptotic expansion but the *complete description* of the solution at large times. Every solution of KdV eventually separates into well-defined solitons and radiation — with no residual, no error, and no unexplained component.

### E5. Dispersive Radiation

The non-soliton component of the solution — the *radiation* — corresponds to the continuous spectrum of the Schrödinger operator L = -partial_{xx} + u_0. It evolves according to the linear KdV dispersion:

    u_radiation(x, t) ~ (1/(3t)^{1/3}) integral r(k) Ai((x - 12k^2 t)/(3t)^{1/3}) dk + ...

where r(k) is the reflection coefficient from the IST. The radiation:
- Disperses at rate ||u_radiation||_{L^{infinity}} ~ t^{-1/3}.
- Preserves its L^2 norm (mass is conserved within the radiation component).
- Oscillates with increasing frequency (shorter wavelengths spread to the left — the Airy wake).
- Interacts with solitons only through exponentially small overlap as they separate.

### E6. Global Smoothness

The KdV has *no blowup of any kind*:

- No gradient blowup (dispersion prevents steepening → no shocks).
- No amplitude blowup (conservation of H_1 = integral u^2 → L^2 bound; higher H_n → H^s bounds).
- No regularity loss (IST maps smooth data to smooth solutions for all time).

Global smoothness holds in H^s for all s >= -3/4 — the *sharpest global well-posedness result* for any nonlinear dispersive PDE. The proof uses:
- For s >= 0: direct conservation-law estimates (H_n controls H^{n-1} norm).
- For -3/4 <= s < 0: the I-method (Colliander–Keel–Staffilani–Takaoka–Tao), which constructs "almost-conservation laws" below the L^2 level.

### E7. Time-Reversibility

The KdV is Hamiltonian → time-reversible: if u(x, t) solves KdV, then u(-x, -t) also solves KdV (using the reflection x → -x appropriate for the odd-order equation). The dynamics have no preferred time direction, no arrow of time, no entropy production. Solitons travel forward and backward with equal ease.

### E8. Infinite Conservation-Law Rigidity

The infinitely many conservation laws H_0, H_1, H_2, ... impose *infinite rigidity* on the dynamics:

- Each H_n constrains the H^{n-1} Sobolev norm.
- The conservation laws are *functionally independent* — each constrains a different aspect of the solution.
- Together, they determine the *isospectral manifold* — the set of all potentials u with the same Schrödinger spectrum as u_0.
- The KdV flow is an *isospectral flow* on this manifold: the spectrum of L = -partial_{xx} + u is constant in time.

The infinite rigidity means that the KdV solution is *maximally constrained* — far more constrained than any finite set of conservation laws could impose. The solution has "zero degrees of freedom" in the sense that it is uniquely determined by its initial data through the IST, with no ambiguity, no non-uniqueness, and no freedom for the dynamics to deviate from the prescribed path.

---

## 3. Universal Inequalities

---

**U1. Mass Conservation**

    H_0 = integral u(x, t) dx = const    for all t

---

**U2. Momentum / L^2 Conservation**

    H_1 = integral u(x, t)^2 dx = const    for all t

Controls the L^2 norm uniformly.

---

**U3. Energy Conservation**

    H_2 = integral [(1/2) u_x^2 - u^3] dx = const    for all t

Controls the H^1 seminorm up to the nonlinear correction.

---

**U4. Higher-Order Invariants**

    H_n = integral P_n(u, u_x, ..., u^{(n)}) dx = const    for all t, all n >= 0

Each H_n is a polynomial functional controlling the H^{n-1} Sobolev norm. The infinite hierarchy provides:

    ||u(t)||_{H^s} <= C(s, {H_n(u_0)})    for all t, all s >= 0

Uniform-in-time control of every Sobolev norm. The strongest a priori estimate in the Atlas.

---

**U5. Airy Dispersive Estimate**

    ||e^{-t partial_x^3} f||_{L^{infinity}} <= C |t|^{-1/3} ||f||_{L^1}

Linear KdV propagator decay. The Airy kernel gives t^{-1/3} decay — the fundamental dispersive estimate for third-order dispersion.

---

**U6. Local Well-Posedness**

For u_0 in H^s(R) with s >= -3/4:

    There exists a unique local solution u in C([0, T]; H^s)

Sharp threshold: s = -3/4 is the critical Sobolev index for the cubic KdV.

---

**U7. Global Well-Posedness**

For u_0 in H^s(R) with s >= -3/4:

    u in C(R; H^s(R))    (global in both time directions)

Unconditional global existence. No smallness condition, no sign condition, no conditional hypothesis.

---

**U8. Soliton Resolution (IST)**

    u(x, t) ~ sum_{j=1}^N 2 kappa_j^2 sech^2(kappa_j(x - 4 kappa_j^2 t - delta_j)) + O(t^{-1/3})

as t → infinity. The N solitons are determined by the discrete spectrum of -partial_{xx} + u_0. The remainder is the dispersive radiation, decaying at rate t^{-1/3}.

---

**U9. Phase-Shift Formula**

For a two-soliton interaction (kappa_1 > kappa_2):

    Delta x_1 = (1/kappa_1) log((kappa_1 + kappa_2)/(kappa_1 - kappa_2))    [faster soliton shifts forward]
    Delta x_2 = -(1/kappa_2) log((kappa_1 + kappa_2)/(kappa_1 - kappa_2))   [slower soliton shifts backward]

Exact, closed-form. No approximation. The most precise interaction formula in the Atlas.

---

**U10. Dispersive Tail Decay**

    ||u_radiation(t)||_{L^{infinity}} <= C t^{-1/3}    as t → infinity

The radiation component decays at the Airy rate. The soliton components persist unchanged.

---

### Universal Inequality Summary

| Label | Inequality                        | Type            | Status        | Role                        |
|-------|-----------------------------------|-----------------|---------------|-----------------------------|
| U1    | Mass conservation                 | Exact identity  | Unconditional | Zeroth invariant            |
| U2    | L^2 conservation                  | Exact identity  | Unconditional | First invariant             |
| U3    | Energy conservation               | Exact identity  | Unconditional | Second invariant            |
| U4    | Higher-order invariants           | Exact identities| Unconditional | Infinite Sobolev control    |
| U5    | Airy dispersive estimate          | Decay bound     | Linear flow   | Primary dispersive control  |
| U6    | Local well-posedness              | Existence       | Unconditional | Short-time (s >= -3/4)     |
| U7    | Global well-posedness             | Global existence| Unconditional | All-time (s >= -3/4)       |
| U8    | Soliton resolution                | Decomposition   | Schwartz data | Complete long-time behavior |
| U9    | Phase-shift formula               | Exact formula   | Multi-soliton | Interaction control         |
| U10   | Dispersive tail decay             | Decay bound     | Radiation     | Tail asymptotics            |

**All ten inequalities are unconditional.** No sign dependence, no dimensional dependence, no parametric dependence. The KdV has the most uniform set of universal inequalities of any nonlinear PDE in the Atlas.

---

## 4. Attractors and Long-Time Behavior

### 4.1 No Dissipative Attractor

The KdV is Hamiltonian → no dissipative attractor. The dynamics preserve phase-space volume (symplectic flow) and cannot contract to a lower-dimensional set. There is no Lyapunov functional, no monotone convergence, no fixed-point attractor.

### 4.2 Soliton Resolution as the "Attractor"

The KdV's long-time behavior is not convergence to a fixed point but *decomposition into canonical components*:

    u(x, t) → N solitons + dispersive radiation    as t → ±infinity

The solitons are the *persistent components* — they survive forever, maintaining their shapes, amplitudes, and speeds. The radiation is the *transient component* — it disperses to zero amplitude (but preserves its L^2 mass).

The soliton resolution is the KdV analogue of:
- PME: convergence to Barenblatt profile (one canonical profile).
- FP: convergence to Gibbs–Boltzmann (one equilibrium).
- NLS: scattering or soliton resolution (for integrable 1D).
- Burgers: N-wave decay (shock coarsening).

But the KdV resolution is *more precise* than any of these: it provides the *exact number* of solitons (from the discrete spectrum), the *exact parameters* (from the eigenvalues), the *exact interaction formulas* (phase shifts), and the *exact radiation asymptotics* (Airy decay). No other nonlinear PDE has this level of long-time detail.

### 4.3 The Soliton as a "Prime" of the Wave Field

The soliton resolution has a structural parallel with the prime factorization of integers:

| Feature              | Integer Factorization (ED)        | KdV Soliton Resolution          |
|---------------------|------------------------------------|---------------------------------|
| Objects             | Integers n                         | Wave fields u(x)                |
| "Primes"            | Prime numbers p                    | Solitons (kappa_j)              |
| "Composites"        | Composite integers                 | Radiation (continuous spectrum)  |
| Decomposition       | n = p_1^{a_1} ... p_k^{a_k}      | u ~ sum solitons + radiation    |
| Uniqueness          | Fundamental theorem of arithmetic  | IST uniqueness                  |
| Parameters          | Primes p_j and exponents a_j       | Eigenvalues kappa_j and norming constants |
| Persistence         | Primes are indecomposable          | Solitons are shape-preserving   |
| Interaction          | Multiplication                    | Elastic collision               |

The solitons are the "primes" of the wave field: indecomposable, persistent, parameterized by a single number, and interacting elastically. The radiation is the "composite" background: decomposable, transient, and structurally subordinate. The KdV IST is the *dynamical analogue* of the fundamental theorem of arithmetic — a unique decomposition of the wave field into irreducible components.

### 4.4 Comparison of Long-Time Behavior

| Architecture | Long-Time Behavior                   | "Attractor"               | Exactness     |
|-------------|--------------------------------------|---------------------------|---------------|
| **KdV**     | **Soliton resolution (IST)**        | **N solitons + Airy tail**| **Exact**     |
| NLS (foc.1D)| Soliton resolution (IST)            | N solitons + radiation    | Exact         |
| NLS (def.)  | Scattering to linear flow            | Free Schrödinger group    | Proved        |
| FP          | Convergence to Gibbs–Boltzmann       | Gibbs equilibrium         | Proved        |
| PME         | Convergence to Barenblatt            | Self-similar profile      | Proved        |
| HJ          | Convergence to paraboloid            | Hopf–Lax minimum          | Proved        |
| Burgers     | N-wave decay                         | Entropy solution          | Proved        |
| MCF         | Extinction (sphere)                  | Round sphere              | Proved        |
| AC          | Phase selection (±1)                 | Uniform states            | Proved        |
| NS (2D)    | Attractor (compact set)              | Unknown structure         | Existence only|

The KdV long-time behavior is the *most completely characterized* in the Atlas: exact decomposition, exact parameters, exact interaction formulas, exact radiation asymptotics. The only architecture with comparable exactness is the integrable 1D focusing NLS (which shares the IST structure).

---

## 5. Comparison with FP, PME, HJ, Burgers, NLS, NS, MCF, AC/CH, TFE, RD, and ED

### 5.1 The Four-Pole Structure with KdV

The KdV completes a *four-pole scaffold* for the Atlas:

**Diffusive pole (FP, PME, AC/CH, TFE):**
- Smoothing through amplitude decay.
- Lyapunov → equilibrium.
- Irreversible.

**Hyperbolic pole (HJ, Burgers):**
- Steepening through nonlinear transport.
- Entropy → shocks.
- Irreversible.

**Dispersive pole (NLS):**
- Spreading through phase interference.
- Hamiltonian → conservation.
- Reversible.

**Integrable pole (KdV):**
- Exact solvability through IST.
- Bi-Hamiltonian → infinite conservation laws.
- Reversible + exactly decomposable.

The integrable pole is *nested within* the dispersive pole (KdV is dispersive) but adds *integrability* as a structural layer that no merely dispersive architecture achieves. The NLS is dispersive + Hamiltonian; the KdV is dispersive + Hamiltonian + *bi-Hamiltonian + completely integrable*.

### 5.2 KdV vs. Burgers: Dispersion Regularizes Transport

    Burgers: u_t + u u_x = 0               → shocks (certain, irreversible)
    KdV:     u_t + 6u u_x + u_{xxx} = 0    → solitons (certain, reversible)

The single addition of u_{xxx} transforms the Burgers dynamics completely:
- Shocks → solitons.
- Entropy production → energy conservation.
- Irreversibility → time-reversibility.
- L^1 contraction → Hamiltonian phase-space preservation.
- Finite-time singularity → global smoothness.
- One conservation law → infinitely many.

This is the *most dramatic structural transformation in the Atlas*: one third-order term converts a shock-forming, entropy-producing, irreversible architecture into a soliton-forming, energy-conserving, reversible, completely integrable architecture.

### 5.3 KdV vs. NLS: Real vs. Complex Integrability

Both KdV and (1D focusing) NLS are completely integrable via IST. The structural differences:

| Feature                    | KdV                          | NLS (1D focusing)             |
|----------------------------|------------------------------|-------------------------------|
| Field type                 | Real                         | Complex                       |
| Dispersion order           | 3rd (u_{xxx})               | 2nd (Delta psi)               |
| Nonlinearity               | Advective (u u_x)           | Algebraic (\|psi\|^2 psi)   |
| Soliton profile            | sech^2 (positive, real)      | sech (complex, with phase)    |
| Speed–amplitude relation   | Locked (c = 4 kappa^2)      | Independent (c and A free)    |
| Lax operator               | Schrödinger (-d^2/dx^2 + u) | Zakharov–Shabat (matrix)      |
| Bi-Hamiltonian             | **Yes** (two structures)     | No (one structure)            |
| Dimension                  | 1D only (structurally)       | 1D for integrability          |

The KdV integrability is *deeper* than the NLS integrability in one respect: the bi-Hamiltonian structure. The KdV has *two* compatible Hamiltonian structures; the NLS has one. The bi-Hamiltonian structure generates the infinite conservation laws through an *algebraic recursion* (Lenard), while the NLS generates its conservation laws through a different mechanism (the trace formula of the Zakharov–Shabat system).

### 5.4 Summary Table

| Feature                    | KdV              | NLS      | Burgers  | HJ       | FP       | PME      | NS       | MCF      |
|----------------------------|------------------|----------|----------|----------|----------|----------|----------|----------|
| Field type                 | **Real**         | Complex  | Real     | Real     | Real     | Real     | Real     | Geometric|
| PDE order                  | **3rd**          | 2nd      | 1st      | 1st      | 2nd      | 2nd      | 2nd      | 2nd      |
| Dispersion                 | **omega = -k^3** | omega=k^2| None     | None     | None     | None     | None     | None     |
| Advection                  | **6u u_x**       | None     | v v_x    | H(u_x)  | b.nabla rho| None  | u.nabla u| None     |
| Solitons                   | **sech^2 (real)**| sech (complex)| No  | No       | No       | No       | No       | No       |
| Integrability              | **IST + bi-Ham.**| IST (1D) | Cole–Hopf| Hopf–Lax| Spectral | No       | No       | No       |
| Conservation laws          | **Infinite**     | 3 (or inf.)| 1     | 0        | 1        | 1        | 2        | 0        |
| Reversibility              | **Yes**          | Yes      | No       | No       | No       | No       | No       | No       |
| Blowup                     | **No**           | Foc.d>=2 | Certain  | Certain  | No       | No       | Open(3D) | Certain  |
| Long-time                  | **Soliton resol.**| Scatter/soliton| N-wave| Paraboloid| Gibbs | Barenblatt| Open   | Extinction|
| Parameters                 | **0**            | 1 (sign) | 0        | 0        | 2        | 1        | 2        | 0        |

KdV is the *unique real-valued, third-order, bi-Hamiltonian, completely integrable, infinite-conservation-law, soliton-resolving, globally-smooth, reversible, parameter-free* architecture in the Atlas. It is the integrable pole — the architecture with the *most structural resources* and the *most complete dynamical understanding*.

---

*End of Mode 2: PDE → Extremal Dynamics. Mode 3 (Channels → Constraint Surface) will follow in a subsequent file.*
