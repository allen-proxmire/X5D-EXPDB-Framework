# AD Evaluation: Korteweg–de Vries Equation — Mode 1: Axiom → Envelope

Allen Proxmire

April 2026

---

## Overview

Mode 1 traces the path from the KdV axioms (KdV-1 through KdV-10) to the architectural envelope. The KdV envelope is the *most tightly sealed* of any nonlinear PDE in the PDE Atlas — sealed not by one or two closure mechanisms but by an *infinite hierarchy of conservation laws* combined with the *inverse scattering transform*. Where the NLS has three conservation laws and Strichartz estimates, and the Burgers/HJ have one or two conservation laws and entropy/viscosity admissibility, the KdV has *infinitely many conservation laws* and an *exact linearization* (the IST). The KdV envelope is *overdetermined* — it has far more structural constraints than any finite set of analytical estimates could provide.

The KdV introduces a new closure mode: **integrability closure** — the most powerful closure mechanism in the Atlas. Integrability provides existence, uniqueness, global regularity, exact soliton resolution, and complete control of the long-time asymptotics, all from a single structural property (the Lax pair / bi-Hamiltonian structure). No other architecture achieves this level of structural completeness.

Throughout:

    u_t + 6 u u_x + u_{xxx} = 0

on R, with u : R x R → R.

---

## 1. Forbidden Configurations

### F1. Diffusive Smoothing

**Axiom source:** KdV-9 (No Diffusion), KdV-5 (Hamiltonian).

The KdV has no second-order term. The time evolution is Hamiltonian (energy-conserving) and dispersive (spreading through phase interference), not diffusive (decaying through amplitude damping). The L^2 norm ||u(t)||_{L^2}^2 is exactly conserved — no mode is damped. Initial data in H^s produces solutions in H^s with the Sobolev index preserved, not improved.

No parabolic regularization, no instantaneous C^{infinity} smoothing, no Lyapunov-driven decay. The KdV achieves global smoothness through *integrability*, not through *diffusion*.

### F2. Irreversible Decay

**Axiom source:** KdV-5 (Hamiltonian), KdV-9 (No Diffusion).

The KdV is time-reversible: if u(x, t) solves KdV, then u(-x, -t) also solves KdV (using the x → -x symmetry of the odd-order equation). There is no Lyapunov functional, no monotone quantity, no arrow of time.

All infinitely many conservation laws H_n are *exactly constant* — none increases or decreases. The dynamics circulate on the intersection of the level sets {H_n = const for all n}, which is an extremely rigid constraint but carries no preferred direction.

### F3. Shock Formation

**Axiom source:** KdV-3 (Third-Order Dispersion), KdV-4 (Advection), combined.

The nonlinear advection u u_x, acting alone, would produce Burgers-type shocks. But the third-order dispersion u_{xxx} *prevents* shock formation: the dispersive spreading counteracts the advective steepening at every scale.

Formally: the KdV has global smooth solutions for all Schwartz-class initial data (Kato, 1983; Kenig–Ponce–Vega, 1993 for H^s data). No gradient blowup, no discontinuity formation, no weak-solution theory needed. The dispersion is the *structural regularizer* that replaces the viscosity of the Burgers equation.

### F4. Finite-Speed Propagation

**Axiom source:** KdV-3 (Third-Order Dispersion).

The linear KdV u_t + u_{xxx} = 0 has the dispersive kernel (Airy function) with support on all of R for any t > 0. Compactly supported initial data becomes nonzero everywhere instantly — infinite-speed propagation. The propagation speed is "infinite" in the sense that the support becomes all of R immediately, but the *amplitude* at large distances decays rapidly (as the Airy function tail).

Finite-speed propagation — characteristic cones, compact-support preservation — is forbidden. The KdV is dispersive (infinite speed, like NLS and FP) not hyperbolic (finite speed, like HJ and Burgers).

### F5. Entropy Production

**Axiom source:** KdV-5 (Hamiltonian), KdV-6 (Infinite Conservation Laws).

The KdV produces no entropy. The evolution preserves *every* H_n exactly. No information is lost, no energy is dissipated, no irreversibility occurs. The Hamiltonian flow on the infinite-dimensional phase space is *volume-preserving* (symplectic) and *isentropic*.

### F6. Mass Loss

**Axiom source:** KdV-6.

    H_0 = integral u dx = const

The mass (zeroth conservation law) is exactly preserved. No creation, no destruction, no leakage.

### F7. Energy Dissipation

**Axiom source:** KdV-5, KdV-6.

    H_2 = integral [(1/2) u_x^2 - u^3] dx = const

The energy (second conservation law) is exactly preserved. No dissipation mechanism exists — not at shocks (no shocks), not in the bulk (no diffusion), not at boundaries (no boundaries).

### F8. Pattern-Forming Instabilities

**Axiom source:** KdV-1 (Real Scalar), KdV-10 (No Reaction).

One species, no reaction, no diffusion-reaction coupling. Turing instabilities require at least two species with differential diffusion and reaction. The KdV has dispersive spreading, not diffusive spreading, and no reaction at all. Pattern formation of the RD type is structurally absent.

The KdV *does* produce localized coherent structures (solitons), but these arise from the *advection-dispersion balance*, not from a pattern-forming instability. Solitons are *traveling waves*, not *spatially periodic patterns*.

### F9. Finite-Time Blowup

**Axiom source:** KdV-6 (Infinite Conservation Laws), KdV-7 (Integrability).

The KdV has *no finite-time blowup* of any kind:
- No gradient blowup (dispersion prevents steepening).
- No amplitude blowup (conservation of H_1 = integral u^2 dx gives L^2 bound; higher conservation laws give H^s bounds for all s).
- No regularity loss (the IST maps smooth initial data to smooth solutions for all time).

The structural mechanism: the infinite hierarchy of conservation laws controls *every Sobolev norm simultaneously*. Since H_n controls the H^{n-1} Sobolev norm of u, and all H_n are conserved, the solution remains bounded in H^s for all s and all time. No blowup is possible because blowup would require some norm to diverge, and every norm is controlled by a conservation law.

This is the *strongest no-blowup result* in the Atlas: KdV has global smooth solutions not through diffusion (AC/CH/PME/TFE/FP), not through energy estimates + Strichartz (NLS defocusing), but through *infinite conservation laws that control every regularity level*. The overkill is structural — any single conservation law (say H_2 controlling H^1) would suffice for global existence in 1D, but the KdV has *infinitely many*.

### F10. Nonlocal Forcing

**Axiom source:** KdV-2 (Locality), KdV-10 (No Reaction/Forcing).

No external potential, no forcing, no nonlocal coupling. The KdV is autonomous and fully local.

### Summary of Forbidden Configurations

| Label | Forbidden Configuration               | Excluding Axiom(s)        |
|-------|---------------------------------------|---------------------------|
| F1    | Diffusive smoothing                   | KdV-5, KdV-9             |
| F2    | Irreversible decay                    | KdV-5, KdV-9             |
| F3    | Shock formation                       | KdV-3, KdV-4 (combined)  |
| F4    | Finite-speed propagation              | KdV-3                    |
| F5    | Entropy production                    | KdV-5, KdV-6             |
| F6    | Mass loss                             | KdV-6                    |
| F7    | Energy dissipation                    | KdV-5, KdV-6             |
| F8    | Pattern-forming instabilities         | KdV-1, KdV-10            |
| F9    | Finite-time blowup                    | KdV-6, KdV-7             |
| F10   | Nonlocal forcing                      | KdV-2, KdV-10            |

---

## 2. Necessary Configurations

### N1. Real Scalar Field

**Source:** KdV-1.

The state u(x, t) is real-valued. No phase, no gauge symmetry, no complex structure. The KdV soliton sech^2 is a *real, positive, localized* function — the simplest possible coherent structure.

### N2. Third-Order Dispersion

**Source:** KdV-3.

The dispersion relation omega = -k^3 is *odd* (asymmetric in k) and *cubic* (third-order). This produces:
- Asymmetric spreading: left-moving and right-moving wave packets spread at different rates.
- Airy-function kernel: the fundamental solution of u_t + u_{xxx} = 0 is the Airy function Ai(x / (3t)^{1/3}) / (3t)^{1/3}.
- Dispersive decay: ||u(t)||_{L^{infinity}} <= C t^{-1/3} ||u_0||_{L^1} for the linear flow (slower than the NLS rate t^{-d/2} because the dispersion is cubic, not quadratic).

### N3. Quadratic Nonlinearity (Advection)

**Source:** KdV-4.

The nonlinear term 6 u u_x = partial_x(3 u^2) is a *quadratic conservation-law flux*. It is the same self-advection as in Burgers but with a specific coefficient (6, by convention). The quadratic nonlinearity is the *simplest nonlinearity compatible with the KdV integrability structure* — changing the power (e.g., u^2 u_x) breaks integrability.

### N4. Bi-Hamiltonian Structure

**Source:** KdV-5.

Two compatible Hamiltonian operators J_1 = partial_x and J_2 = partial_x^3 + (2/3)(u partial_x + partial_x u) generate the KdV flow from two different Hamiltonian functionals:

    u_t = J_1 (delta H_2 / delta u) = J_2 (delta H_0 / delta u)

The compatibility of J_1 and J_2 (they satisfy the Magri–Lenard recursion relation) is the *algebraic engine* that generates the infinite hierarchy of conservation laws.

### N5. Infinite Conservation Laws

**Source:** KdV-6.

The Lenard recursion generates H_0, H_1, H_2, H_3, ... — infinitely many independent polynomial conservation laws. Each H_n is an integral of a polynomial in u, u_x, u_{xx}, ..., u^{(n)}. The first few:

    H_0 = integral u dx
    H_1 = integral u^2 dx
    H_2 = integral [(1/2) u_x^2 - u^3] dx
    H_3 = integral [u_{xx}^2 + 5 u u_x^2 + (5/6) u^4] dx (up to normalization)

The conservation of H_n controls the H^{n-1} Sobolev norm. Infinitely many conservation laws → control of every H^s norm → global smoothness.

### N6. Complete Integrability (IST)

**Source:** KdV-7.

The Lax pair representation:

    L = -partial_{xx} + u    (Schrödinger operator)
    A = -4 partial_{xxx} + 6 u partial_x + 3 u_x    (third-order operator)

satisfies L_t = [A, L] if and only if u solves KdV. The Lax pair:
- Provides the *isospectral property*: the spectrum of L is constant in time.
- Connects KdV to the Schrödinger scattering problem.
- Enables the IST: u(0) → scattering data → linear evolution → scattering data(t) → u(t).

The IST provides the *exact solution* of the KdV for all time. It is the ultimate structural tool: it converts the nonlinear PDE into a *linear problem* in scattering space.

### N7. Soliton Solutions

**Source:** KdV-3, KdV-4, KdV-7.

    u(x, t) = 2 kappa^2 sech^2(kappa(x - 4 kappa^2 t - x_0))

Solitons are *exact, localized, traveling-wave solutions*. They are:
- Positive (u > 0 in the soliton region).
- Localized (exponentially decaying tails).
- Shape-preserving (no dispersion, no steepening — exact balance).
- Speed-locked to amplitude: c = 4 kappa^2 (taller = faster).

### N8. Elastic Soliton Collisions

**Source:** KdV-6, KdV-7.

N-soliton solutions exhibit *elastic collisions*: solitons pass through each other with no change in shape, amplitude, or speed — only a phase shift (position displacement). The elasticity is a consequence of integrability: the infinite conservation laws constrain the interaction so tightly that no energy transfer is possible.

### N9. Dispersive Radiation

**Source:** KdV-3, KdV-7.

The non-soliton component of the solution (the *radiation*) disperses as t → infinity:

    ||u_radiation(t)||_{L^{infinity}} ~ t^{-1/3}    (Airy decay rate)

The radiation is the *continuous-spectrum component* of the IST decomposition. It spreads according to the linear KdV dispersion relation omega = -k^3, decaying in amplitude while preserving its L^2 norm.

### N10. Global Smoothness

**Source:** KdV-6, KdV-7.

For initial data u_0 in H^s(R) with s >= -3/4 (Kenig–Ponce–Vega, Colliander–Keel–Staffilani–Takaoka–Tao):

    u(t) in C(R; H^s(R))    for all t in R

Global existence, uniqueness, and continuous dependence. For Schwartz-class data: u(t) in Schwartz class for all t. The solution is *as smooth as the initial data* — and it stays that way forever.

### Summary of Necessary Configurations

| Label | Necessary Configuration                     | Source               |
|-------|---------------------------------------------|----------------------|
| N1    | Real scalar field                           | KdV-1                |
| N2    | Third-order dispersion (omega = -k^3)       | KdV-3                |
| N3    | Quadratic nonlinearity (6u u_x)             | KdV-4                |
| N4    | Bi-Hamiltonian structure                    | KdV-5                |
| N5    | Infinite conservation laws                  | KdV-6                |
| N6    | Complete integrability (IST + Lax pair)     | KdV-7                |
| N7    | Soliton solutions (sech^2)                  | KdV-3, KdV-4, KdV-7 |
| N8    | Elastic soliton collisions                  | KdV-6, KdV-7        |
| N9    | Dispersive radiation (Airy decay t^{-1/3})  | KdV-3, KdV-7        |
| N10   | Global smoothness (all H^s, all time)       | KdV-6, KdV-7        |

---

## 3. Envelope Inequalities (E1–E10)

---

**E1. Mass Conservation**

    H_0 = integral u(x, t) dx = integral u_0(x) dx    for all t

Exact identity. The zeroth conservation law.

---

**E2. Momentum Conservation (L^2 Norm)**

    H_1 = integral u(x, t)^2 dx = integral u_0(x)^2 dx    for all t

Exact identity. Controls the L^2 norm. The first nontrivial conservation law.

---

**E3. Energy Conservation**

    H_2 = integral [(1/2) u_x^2 - u^3] dx = const    for all t

Exact identity. Controls the H^1 seminorm (via the u_x^2 term) up to the nonlinear correction (u^3 term).

---

**E4. Higher-Order Invariants**

    H_n = polynomial functional of (u, u_x, ..., u^{(n)}) = const    for all t, all n

Infinitely many exact identities. H_n controls the H^{n-1} Sobolev seminorm. The infinite hierarchy provides *uniform-in-time control of every Sobolev norm*:

    ||u(t)||_{H^s}^2 <= C(s, {H_n(u_0)})    for all t, all s

This is the *strongest a priori estimate* in the Atlas: no other architecture controls *every* Sobolev norm simultaneously through exact conservation laws.

---

**E5. Linear Dispersive Estimate (Airy)**

For the linear KdV flow e^{-t partial_x^3}:

    ||e^{-t partial_x^3} f||_{L^{infinity}} <= C |t|^{-1/3} ||f||_{L^1}

The dispersive decay rate is t^{-1/3} — slower than the NLS rate t^{-d/2} (which is t^{-1/2} in 1D) because the KdV dispersion omega = -k^3 is cubic (third-order), producing the Airy-function spreading.

---

**E6. Local Well-Posedness**

For u_0 in H^s(R) with s >= -3/4:

    There exists a unique local solution u in C([0, T]; H^s)

The KdV is locally well-posed at the *sharp regularity threshold* s = -3/4 (Kenig–Ponce–Vega; Colliander–Keel–Staffilani–Takaoka–Tao). This is below L^2 (s = 0) — the KdV is well-posed for *rougher data than any other nonlinear dispersive PDE* in the Atlas.

---

**E7. Global Well-Posedness**

For u_0 in H^s(R) with s >= -3/4:

    The solution extends globally: u in C(R; H^s(R))

Global existence for all time, in both directions (t → ±infinity). The proof uses the conservation laws (for s >= 0) or the I-method and almost-conservation laws (for -3/4 <= s < 0).

The KdV is the *only nonlinear PDE in the Atlas with unconditional global well-posedness at negative Sobolev regularity*. Every other architecture requires at least L^2 (s = 0) or H^1 (s = 1) data for global existence.

---

**E8. Soliton Resolution (IST)**

For generic Schwartz-class initial data u_0, the long-time behavior decomposes:

    u(x, t) ~ sum_{j=1}^N 2 kappa_j^2 sech^2(kappa_j(x - 4 kappa_j^2 t - delta_j)) + radiation(x, t)

where:
- N solitons emerge, with parameters kappa_j determined by the discrete eigenvalues of the Schrödinger operator -partial_{xx} + u_0.
- The radiation disperses: ||radiation(t)||_{L^{infinity}} ~ t^{-1/3}.
- The decomposition is *exact* as t → infinity.

This is the *KdV soliton resolution theorem* — the complete description of the long-time dynamics. Every solution decomposes into solitons (persistent) + radiation (dispersing). The soliton resolution is the KdV analogue of the NLS soliton resolution (for the integrable 1D focusing NLS), but it applies to *all* KdV solutions (not just a specific sub-class).

---

**E9. Phase-Shift Formula for Soliton Collisions**

When two solitons with parameters kappa_1 > kappa_2 interact, each acquires a phase shift:

    delta_1 = (1/kappa_1) log((kappa_1 + kappa_2) / (kappa_1 - kappa_2))    [faster soliton shifts forward]
    delta_2 = -(1/kappa_2) log((kappa_1 + kappa_2) / (kappa_1 - kappa_2))   [slower soliton shifts backward]

The phase shifts are *exact* (not approximate). The solitons emerge from the interaction with identical shapes, amplitudes, and speeds — only their positions are shifted. This is the *most precise interaction formula* in the Atlas: no other architecture has an exact, closed-form expression for the interaction of coherent structures.

---

**E10. Dispersive Tail Decay**

The radiation component satisfies:

    ||u_radiation(x, t)||_{L^{infinity}} <= C t^{-1/3}    as t → infinity

The decay rate t^{-1/3} is the *Airy decay rate* — determined by the cubic dispersion omega = -k^3. The radiation disperses through phase interference, spreading its L^2 mass over an expanding region while maintaining ||u_radiation||_{L^2} = const.

The soliton-radiation decomposition + tail decay provides the *complete asymptotic description* of KdV solutions: solitons persist, radiation disperses, and the interaction between them is fully characterized.

---

### Envelope Summary

**Tier 1 — Infinite Conservation Law Hierarchy (exact, all KdV):**
- E1: Mass conservation (H_0).
- E2: Momentum / L^2 conservation (H_1).
- E3: Energy conservation (H_2).
- E4: Higher-order invariants (H_3, H_4, ..., H_n, ...).

**Tier 2 — Dispersive + Well-Posedness Control:**
- E5: Airy dispersive estimate (t^{-1/3}).
- E6: Local well-posedness (sharp: s >= -3/4).
- E7: Global well-posedness (unconditional, all s >= -3/4).

**Tier 3 — Soliton Resolution + Asymptotics:**
- E8: Soliton resolution (exact decomposition via IST).
- E9: Phase-shift formula (exact interaction formula).
- E10: Dispersive tail decay (t^{-1/3} Airy rate).

**Every constraint is unconditional.** No sign dependence (unlike NLS), no dimensional dependence (KdV is intrinsically 1D), no parametric dependence (zero parameters). The envelope is *the most uniformly tight of any nonlinear PDE in the Atlas*.

---

## 4. Central Architectural Finding

### 4.1 Integrability Closure: The Strongest Closure Mode

The KdV envelope is sealed by **integrability closure** — the *most powerful closure mode in the PDE Atlas*:

| Closure Mode              | Representative | Key Tools                        | # Conservation Laws |
|---------------------------|----------------|----------------------------------|---------------------|
| Linear                    | FP             | Linearity + spectral theory      | 1 (mass)            |
| Dissipative               | PME            | Lyapunov + smoothing + contraction| 1 + entropy family |
| Variational               | HJ             | Convexity + viscosity + Hopf–Lax | 0                   |
| Entropic-contractive      | Burgers        | Convex flux + Kruzkov + L^1      | 1 (mass)            |
| Geometric-dissipative     | MCF            | Area dissipation + Huisken       | 0                   |
| Dispersive Hamiltonian    | NLS            | Conservation + Strichartz        | 3                   |
| **Integrability**         | **KdV**        | **IST + Lax pair + bi-Hamiltonian** | **Infinite**     |

The integrability closure is *strictly stronger* than all other modes:
- It provides *infinitely many conservation laws* (vs. 0–3 for other architectures).
- It provides an *exact linearization* (IST) — the nonlinear PDE is solved by a linear problem.
- It provides *exact soliton resolution* — the complete long-time decomposition into coherent structures.
- It provides *exact interaction formulas* — closed-form expressions for soliton collisions.

No other architecture achieves any of these. The integrability closure is *qualitatively above* all other closure modes — it does not merely control the solution; it *determines it exactly*.

### 4.2 KdV as the Integrable Pole

The PDE Atlas now has *four structural poles*:

    Diffusive pole: FP / PME / AC / CH / TFE    (smoothing, decay, Lyapunov)
    Hyperbolic pole: HJ / Burgers                (steepening, shocks, entropy)
    Dispersive pole: NLS                          (spreading, oscillation, Hamiltonian)
    Integrable pole: KdV                          (exact solvability, infinite conservation, soliton resolution)

The integrable pole is *not independent* of the dispersive pole — the KdV is dispersive (it has the NLS's spreading property). But it adds *integrability* as an additional structural layer, producing a level of control that the NLS's finite conservation laws cannot match.

The integrable pole also intersects the hyperbolic pole: the KdV's advection term u u_x is the Burgers mechanism. The KdV is the *unique intersection* of all three non-diffusive poles: dispersive (u_{xxx}) + hyperbolic (u u_x) + integrable (Lax pair + IST).

### 4.3 The KdV Envelope vs. All Others

| Architecture | Envelope Status       | # Conservation Laws | Exact Solution? | Soliton Resolution? |
|-------------|------------------------|--------------------|-----------------|--------------------|
| ED          | Closed (static)        | N/A                | N/A             | N/A                |
| **KdV**     | **Closed (integrable)**| **Infinite**       | **Yes (IST)**   | **Yes (exact)**    |
| FP          | Closed (linear)        | 1                  | Yes (spectral)  | No                 |
| PME         | Closed (dissipative)   | 1 + entropy family | No              | No (Barenblatt)    |
| HJ          | Closed (variational)   | 0                  | Yes (Hopf–Lax)  | No                 |
| Burgers     | Closed (entropic)      | 1                  | Yes (Cole–Hopf) | No                 |
| NLS (def.)  | Closed (dispersive)    | 3                  | No (except 1D)  | No (scattering)    |
| NLS (foc.1D)| Closed (dispersive)    | Infinite (integrable)| Yes (IST)    | Yes (exact)        |
| MCF         | Closed + req. sing.    | 0                  | No              | No                 |
| NS (3D)    | Open                   | 2                  | No              | No                 |

The KdV is the *most completely characterized nonlinear PDE in mathematics*: infinitely many conservation laws, exact solution via IST, exact soliton resolution, exact interaction formulas, global smoothness at the sharpest possible Sobolev threshold. No other nonlinear PDE (except the 1D focusing NLS, which shares the integrable structure) achieves this level of completeness.

### 4.4 The KdV–ED Parallel: Complete Structural Knowledge

The KdV and ED share a structural parallel at the deepest level: both architectures have *complete knowledge of their own structure*:

- **ED:** The multiplicative structure of Z is *completely determined* by the fundamental theorem of arithmetic. Every integer has a unique factorization. The distribution of primes is (asymptotically) completely known (PNT, Mertens, Chebyshev). The structure is *closed and complete*.

- **KdV:** The solution structure is *completely determined* by the inverse scattering transform. Every solution has a unique decomposition into solitons + radiation. The long-time behavior is completely known (soliton resolution). The structure is *closed and complete*.

Both architectures achieve *complete structural self-knowledge* — the rarest and most valuable property in the PDE Atlas.

---

*End of Mode 1: Axiom → Envelope. Mode 2 (PDE → Extremal Dynamics) will follow in a subsequent file.*
