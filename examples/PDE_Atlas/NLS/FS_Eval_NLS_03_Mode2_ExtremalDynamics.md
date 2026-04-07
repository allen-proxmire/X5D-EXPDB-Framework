# AD Evaluation: Nonlinear Schrödinger Equation — Mode 2: PDE → Extremal Dynamics

Allen Proxmire

April 2026

---

## Overview

Mode 2 moves from the static envelope to the dynamics. The NLS dynamical landscape is *qualitatively unlike* every other architecture in the Atlas. Where parabolic architectures monotonically converge to equilibria and hyperbolic architectures develop shocks and decay, the NLS *oscillates, disperses, and conserves*: wave packets spread through phase interference, solitons persist indefinitely through a nonlinearity-dispersion balance, and the Hamiltonian structure preserves energy, mass, and momentum exactly. There is no monotone convergence, no entropy production, no irreversibility — only the interplay of dispersion and nonlinearity within the rigid framework of conservation laws.

The NLS is the *only architecture in the Atlas where interesting dynamics persist forever without decaying*. In every other architecture, the dynamics either converge to an equilibrium (AC, CH, PME, TFE, FP), develop singularities (HJ, Burgers, MCF, focusing NLS d >= 2), or decay to zero (NS unforced). The defocusing NLS *scatters* — the solution approaches a free linear solution — but the linear solution itself oscillates forever without decaying in L^2. The NLS dynamics have *no terminal state*.

Throughout:

    i partial_t psi + Delta psi ± |psi|^2 psi = 0

on R^d, with psi : R^d x R → C.

---

## 1. Fundamental Time and Length Scales

### 1.1 Two Competing Time Scales

The NLS dynamics are governed by the competition between two processes:

**Dispersive time scale:** The time for a wave packet of spatial scale L to spread appreciably:

    t_disp ~ L^2

This comes from the dispersion relation omega = k^2: a wave packet of width L has Fourier components at wavenumber k ~ 1/L, which oscillate at frequency omega ~ 1/L^2 and cause the packet to spread on time scale t ~ L^2. The dispersive time scale is *quadratic* in L — the same scaling as diffusion (t_diff ~ L^2/D), but with a fundamentally different mechanism: diffusion decays amplitude; dispersion rotates phase.

**Nonlinear time scale:** The time for the nonlinearity to produce an O(1) phase shift:

    t_nonlin ~ 1 / |psi|^2

The cubic nonlinearity |psi|^2 psi shifts the phase of psi at rate |psi|^2. When |psi|^2 is large (high amplitude), the phase shifts fast; when |psi|^2 is small, the phase shifts slowly. The nonlinear time scale depends on the *amplitude* of the solution, not on the spatial scale.

### 1.2 The Dispersion–Nonlinearity Ratio

The ratio of the two time scales:

    rho = t_disp / t_nonlin = L^2 |psi|^2

measures which mechanism dominates at a given scale L and amplitude |psi|:

**rho >> 1 (dispersion-dominated, linear regime):**

The wave packet spreads faster than the nonlinearity can act. The solution behaves approximately like the free Schrödinger equation i psi_t + Delta psi = 0. The nonlinearity is a small perturbation. This is the regime of *scattering*: at long times, the dispersive spreading reduces |psi|, making rho → infinity, and the solution approaches a free linear flow.

**rho ~ 1 (soliton / nonlinear balance):**

Dispersion and nonlinearity are commensurate. The dispersive spreading is exactly balanced by the focusing nonlinearity's tendency to concentrate. This balance produces *solitons* — localized, shape-preserving structures that neither spread nor concentrate. The soliton is the *fixed point of the dispersion-nonlinearity competition*.

**rho << 1 (nonlinearity-dominated, focusing collapse):**

The nonlinearity acts faster than dispersion can spread. The wave function concentrates: |psi| increases, which increases |psi|^2, which further accelerates the concentration — a *self-focusing feedback loop*. In d >= 2 (focusing), this loop can run to completion in finite time, producing *blowup* (||nabla psi|| → infinity as psi concentrates at a point).

### 1.3 Three Dynamical Regimes

**Regime (A): Linear / Dispersive (rho >> 1)**

Low amplitude or large spatial scale. The nonlinearity is negligible. The solution spreads as a linear Schrödinger wave, with ||psi(t)||_{L^{infinity}} ~ t^{-d/2}. The dynamics are essentially the *free Schrödinger equation* — the NLS architecture operating at minimum nonlinearity.

**Regime (B): Soliton / Balanced (rho ~ 1)**

Amplitude and scale are matched so that dispersion = nonlinearity. The solution maintains a coherent localized structure — a *soliton* in 1D, a *standing wave* e^{i omega t} Q(x) in general. The dynamics are *quasi-stationary*: the soliton persists indefinitely, modulated by slow drift, rotation, and interaction with other solitons.

**Regime (C): Collapse / Blowup (rho << 1, focusing)**

High amplitude at small scale. The focusing nonlinearity overwhelms dispersion. The wave function concentrates at a point, with ||nabla psi(t)||_{L^2} → infinity at a finite time T*. The blowup is *self-similar* near the singularity: the collapsing profile approaches a rescaled version of the ground-state soliton Q.

### 1.4 Contrast with Other Architectures

| Feature                    | NLS                         | FP/PME/TFE                  | HJ/Burgers               | NS                    |
|----------------------------|-----------------------------|------------------------------|---------------------------|-----------------------|
| Time scale                 | t_disp ~ L^2 (dispersive)  | t_diff ~ L^2/D (diffusive)  | T* ~ 1/max(-v_0') (shock) | t_visc ~ L^2/nu      |
| Nonlinear time scale       | t_nonlin ~ 1/\|psi\|^2     | t_reaction ~ 1/\|\|R'\|\|   | N/A (transport only)      | t_adv ~ L/U           |
| Competition                | Dispersion vs. nonlinearity | Diffusion vs. reaction       | Transport vs. nothing     | Advection vs. viscosity|
| Outcome of competition     | Soliton (balanced), scatter (dispersion wins), blowup (nonlin. wins) | Equilibrium (diffusion wins) | Shock (transport wins) | Turbulence (unresolved) |
| Mechanism                  | Phase interference          | Amplitude decay              | Gradient compression      | Pressure + viscosity   |
| Reversibility              | **Reversible**              | Irreversible                 | Irreversible              | Irreversible           |

The NLS competition (dispersion vs. nonlinearity) is *qualitatively different* from every other competition in the Atlas: it operates through *phase* (oscillation, interference) rather than *amplitude* (decay, growth). The outcome of the competition is *phase-determined*: when the phases of different Fourier components align (constructive interference → concentration), the nonlinearity wins; when they dephase (destructive interference → spreading), dispersion wins.

---

## 2. Extremal Behaviors

### E1. Dispersive Spreading (Linear Flow)

For the free Schrödinger equation (no nonlinearity):

    ||e^{it Delta} psi_0||_{L^{infinity}} <= C |t|^{-d/2} ||psi_0||_{L^1}

The L^{infinity} norm decays as t^{-d/2} — the same rate as diffusion, but through a different mechanism. The decay is caused by *phase cancellation*: different Fourier components rotate at different rates (omega = k^2), and their superposition averages out to zero at each point. The total mass ||psi||_{L^2}^2 is conserved — the amplitude decreases only because the wave function *spreads* over an expanding region.

Dispersive spreading is the NLS's primary stabilizing mechanism — the analogue of diffusion in parabolic architectures. But it is *weaker* than diffusion: it reduces L^{infinity} but does not improve regularity (no H^s gain), does not reduce energy (H conserved), and does not reduce total variation.

### E2. Soliton Formation (Focusing, 1D)

The focusing 1D NLS supports *solitons* — localized traveling waves:

    psi_sol(x, t) = A sech(A(x - vt)) exp(i(vx/2 + (A^2 - v^2/4)t))

The soliton:
- Has fixed amplitude A and speed v.
- Maintains its shape for all time (no dispersion, no decay).
- Has mass M = 2A and energy H = 2A^3/3 - v^2 A.
- Is *orbitally stable*: small perturbations remain close to a translated/phase-rotated soliton.

The soliton is the *canonical coherent structure* of the NLS — a balance between dispersion (which would spread the wave packet) and focusing nonlinearity (which would concentrate it). This balance is the dispersive analogue of the AC interface (balance between reaction and diffusion) and the PME Barenblatt profile (balance between mass conservation and nonlinear spreading).

### E3. Multi-Soliton Interactions (Elastic Collisions)

In the integrable 1D NLS, multi-soliton solutions exhibit *elastic collisions*: two solitons pass through each other, exchange a phase shift, and emerge with their shapes, amplitudes, and speeds unchanged. The interaction is:

- *Elastic:* No energy, mass, or momentum is transferred between solitons.
- *Nonlinear:* The solitons interact during the collision (they are not superimposed — the nonlinearity couples them).
- *Phase-shifting:* Each soliton acquires a phase and position shift after the collision, but no amplitude change.

Elastic soliton collisions are *unique to the NLS* in the Atlas. No other architecture has localized structures that interact nonlinearly yet emerge unchanged. The elasticity is a consequence of *complete integrability* — the NLS has infinitely many conservation laws that constrain the interaction.

### E4. Scattering to Linear Flow (Defocusing)

For the defocusing NLS in d >= 3 (and d = 2 with appropriate modifications):

    psi(t) → e^{it Delta} psi_+    as t → +infinity

The solution approaches a *free linear solution* asymptotically. The nonlinearity becomes negligible because dispersive spreading reduces ||psi||_{L^{infinity}} to the point where |psi|^2 is too small to matter. The solution "forgets" the nonlinearity at long times.

Scattering is the NLS's version of "convergence to equilibrium" — but the "equilibrium" is not a fixed point; it is a *freely dispersing wave*. The solution does not settle down to a static configuration but approaches *linear dynamics*. This is qualitatively different from every parabolic architecture (which converges to a static equilibrium) and every hyperbolic architecture (which develops shocks and decays through entropy production).

### E5. Blowup / Collapse (Focusing, d >= 2)

For the focusing NLS in d >= 2, solutions with sufficiently negative energy (or sufficiently large mass, in d = 2) blow up in finite time:

    ||nabla psi(t)||_{L^2} → infinity    as t → T*

The blowup mechanism is *self-focusing*: the attractive nonlinearity concentrates the wave function at a point faster than dispersion can spread it. Near the blowup time T*, the solution approaches a *rescaled ground-state soliton*:

    psi(x, t) ~ (1/lambda(t))^{d/2} Q((x - x_0)/lambda(t)) e^{i phase}

with lambda(t) → 0 as t → T* (the length scale shrinks to zero). The blowup rate depends on the dimension and the relation to the critical mass:

- d = 2 (L^2-critical): lambda(t) ~ sqrt(T* - t) / sqrt(log|log(T* - t)|) (log-log blowup rate — Merle–Raphaël).
- d >= 3 (supercritical): lambda(t) ~ (T* - t)^{1/2} (self-similar, faster blowup).

The NLS blowup is *concentration* (amplitude grows at a point) — qualitatively different from HJ/Burgers blowup (gradient steepens → discontinuity) and MCF blowup (curvature grows → surface collapses). The NLS singularity is in the *amplitude*, not in the *gradient* or *curvature*.

### E6. Quasi-Periodic / Breather Dynamics (Focusing)

In the integrable 1D focusing NLS, *breather* solutions exist — localized oscillating structures:

    psi_breather(x, t) = [complex formula involving sech and oscillatory terms]

Breathers are *oscillating solitons*: they pulsate in amplitude while maintaining their overall shape and location. They represent the simplest *time-periodic* solutions of the NLS — structures that oscillate forever without decaying.

Breathers are *unique to the dispersive pole*. No parabolic architecture has periodic solutions (Lyapunov monotonicity forbids them). HJ/Burgers have no periodic solutions (entropy production forbids them). Only the Hamiltonian NLS, with its time-reversible, energy-conserving structure, can support indefinitely oscillating coherent structures.

### E7. Time-Reversibility

If psi(x, t) solves the NLS, then psi*(x, -t) also solves it. The dynamics are *exactly reversible*: running the movie backward produces another valid solution. This is a necessary consequence of the Hamiltonian structure (NLS-5) and the absence of diffusion (NLS-9).

Time-reversibility is *unique to the NLS* in the Atlas. Every other architecture has an arrow of time: parabolic PDEs smooth forward and roughen backward; hyperbolic PDEs produce entropy at shocks (forward only); MCF decreases area (forward only). The NLS has *no arrow of time* — forward and backward evolution are structurally identical.

### E8. Conservation-Law-Driven Rigidity

The three conservation laws (mass M, energy H, momentum P) impose *rigid constraints* on the dynamics:

- M = const: the L^2 norm cannot change → the solution cannot decay to zero or grow to infinity in L^2.
- H = const: the energy cannot increase or decrease → the kinetic energy ||nabla psi||^2 and the potential energy ± integral |psi|^4 can exchange, but their sum is fixed.
- P = const: the center of mass moves at constant velocity → the wave packet cannot accelerate.

These conservation laws create a *rigidity* that no dissipative architecture has: the solution is confined to a *level set* of (M, H, P) in the infinite-dimensional phase space. The dynamics are restricted to this level set — an infinite-codimension-3 submanifold. The conservation laws are *architectural constraints* that bound the dynamics from every direction simultaneously.

---

## 3. Universal Inequalities

---

**U1. Mass Conservation**

    ||psi(t)||_{L^2}^2 = M    for all t

Exact identity. Unitary evolution.

---

**U2. Energy Conservation**

    H[psi(t)] = integral [|nabla psi|^2 ± (1/2)|psi|^4] dx = H[psi_0]    for all t

Exact identity. Hamiltonian invariant.

---

**U3. Momentum Conservation**

    P[psi(t)] = Im integral psi* nabla psi dx = P[psi_0]    for all t

Exact identity. Translational invariance.

---

**U4. Linear Dispersive Estimate**

    ||e^{it Delta} f||_{L^{infinity}} <= C |t|^{-d/2} ||f||_{L^1}

The free Schrödinger propagator decays at rate t^{-d/2} in L^{infinity}. This is the primary dispersive control — the NLS analogue of parabolic smoothing estimates.

---

**U5. Strichartz Estimates**

For admissible pairs (q, r) with 2/q + d/r = d/2, q >= 2:

    ||e^{it Delta} f||_{L^q_t L^r_x(R x R^d)} <= C ||f||_{L^2(R^d)}

Mixed space-time control. The fundamental analytical tool for NLS well-posedness: converts dispersive properties of the linear flow into bounds on the nonlinear solution through a fixed-point argument.

---

**U6. Local Well-Posedness**

For psi_0 in H^s(R^d) with s >= max(0, d/2 - 1):

    There exists T > 0 and a unique solution psi in C([0,T]; H^s)

Local existence holds universally — both focusing and defocusing, all d, all signs.

---

**U7. Global Well-Posedness (Defocusing)**

For defocusing (+) cubic NLS:

    d = 1: Global in L^2 (and H^s for all s >= 0)
    d = 2: Global in L^2
    d = 3: Global in H^1

The positive-definite energy H >= 0 controls ||nabla psi||_{L^2}^2 <= H, providing uniform-in-time H^1 bounds.

---

**U8. Virial / Morawetz Inequalities (Focusing Blowup)**

**Virial identity (d = 2, focusing):**

    d^2/dt^2 integral |x|^2 |psi|^2 dx = 8 H

If H < 0: the variance is concave → reaches zero in finite time → blowup.

**Morawetz estimate (defocusing):**

    integral_0^T integral |psi(x,t)|^4 / |x| dx dt <= C(M, H)

Controls the space-time integral of |psi|^4 — key for proving scattering.

---

**U9. Scattering (Defocusing, d >= 3)**

    ||psi(t) - e^{it Delta} psi_+||_{H^1} → 0    as t → +infinity

The solution approaches a free linear flow. The nonlinearity turns off asymptotically because dispersive spreading makes |psi|^2 negligible.

---

**U10. Critical Thresholds (Focusing)**

**d = 2 (L^2-critical cubic NLS):**

    M < M_* = ||Q||_{L^2}^2: global existence + scattering
    M = M_*: soliton Q is the unique optimizer (global, no scattering)
    M > M_*: blowup possible

The ground-state mass M_* is the *sharp threshold*. The Gagliardo–Nirenberg inequality:

    integral |psi|^4 dx <= C_{GN} ||psi||_{L^2}^2 ||nabla psi||_{L^2}^2

with optimal constant C_{GN} = 2/||Q||_{L^2}^2 provides the exact relationship between mass, energy, and blowup.

---

### Universal Inequality Summary

| Label | Inequality                        | Type            | Status              | Role                        |
|-------|-----------------------------------|-----------------|---------------------|-----------------------------|
| U1    | Mass conservation                 | Exact identity  | All NLS             | Primary invariant           |
| U2    | Energy conservation               | Exact identity  | All NLS             | Secondary invariant         |
| U3    | Momentum conservation             | Exact identity  | All NLS             | Tertiary invariant          |
| U4    | Dispersive estimate               | Decay bound     | Linear flow         | Primary spreading control   |
| U5    | Strichartz estimates              | Space-time      | All NLS             | Nonlinear control           |
| U6    | Local well-posedness              | Existence       | All NLS             | Short-time determinism      |
| U7    | Global well-posedness (defocusing)| Global existence| Defocusing          | Complete well-posedness     |
| U8    | Virial/Morawetz                   | Blowup/control  | Focusing/defocusing | Blowup criteria + scattering|
| U9    | Scattering (defocusing)           | Asymptotics     | Defocusing, d >= 3  | Long-time behavior          |
| U10   | Critical thresholds               | Sharp boundary  | Focusing, d = 2     | Blowup/global boundary      |

**Three exact conservation laws (U1–U3) + seven analytical inequalities (U4–U10).** The conservation laws are unconditional and exact; the inequalities are the dispersive analytical tools that convert conservation into control.

---

## 4. Attractors and Long-Time Behavior

### 4.1 No Dissipative Attractor

The NLS has *no attractor* in the conventional (parabolic) sense:

- No Lyapunov functional → no monotone convergence → no fixed-point attractor.
- Hamiltonian flow preserves phase-space volume → cannot contract to a lower-dimensional set.
- Time-reversibility → no preferred time direction → no "late-time" vs. "early-time" distinction.

The NLS dynamics are *non-convergent* in the strongest sense: the solution does not approach any fixed configuration, and the distance between two solutions (in L^2 or H^1) is *exactly preserved* (not decreasing, as in L^1-contracting or L^{infinity}-contracting architectures).

### 4.2 Two Long-Time Regimes

Despite the absence of a dissipative attractor, the NLS has well-characterized long-time behavior:

**Defocusing: Scattering**

For the defocusing NLS (d >= 3, or d = 2 with appropriate modifications):

    psi(t) ~ e^{it Delta} psi_+    as t → infinity

The solution *scatters* to a free linear flow. The "attractor" is not a fixed point but the *linear Schrödinger group* — the solution approaches a freely dispersing wave. The scattering is *not* convergence to equilibrium (the free wave oscillates forever) but convergence to *linear dynamics* (the nonlinearity becomes negligible).

**Focusing (1D): Soliton Resolution**

For the integrable focusing 1D NLS, generic solutions decompose into:

    psi(t) ~ sum_{j=1}^N psi_soliton_j(t) + radiation(t)

where:
- The soliton components maintain their shapes, amplitudes, and speeds forever.
- The radiation component disperses (scatters to linear flow).
- The decomposition is *exact* as t → infinity: the solution separates cleanly into solitons + radiation.

This is the *soliton resolution conjecture* (proved for the integrable 1D NLS via inverse scattering): every solution decomposes into a finite number of solitons plus a dispersive radiation tail. The solitons are the "attractors" — the coherent structures that persist forever — and the radiation is the "transient" that disperses away.

**Focusing (d >= 2): Blowup or Ground-State Dynamics**

For the focusing NLS in d >= 2:
- Solutions with M < M_* (sub-critical mass) scatter.
- Solutions with M = M_* exhibit ground-state dynamics (the soliton Q is the threshold object).
- Solutions with M > M_* may blow up (concentrate to a point in finite time).

The "attractor" in the focusing case is the *ground-state soliton Q* — it is the critical object that separates the scattering regime from the blowup regime.

### 4.3 Comparison of Long-Time Behavior

| Architecture | Long-Time Behavior                   | "Attractor"               | Mechanism         |
|-------------|--------------------------------------|---------------------------|-------------------|
| **NLS (def.)**| **Scattering to linear flow**      | **Free Schrödinger group**| **Dispersive decay** |
| **NLS (foc. 1D)**| **Soliton resolution**          | **Solitons + radiation**  | **Integrability** |
| **NLS (foc. d>=2)**| **Blowup or scatter**          | **Ground state Q**        | **Critical mass** |
| FP          | Convergence to Gibbs–Boltzmann       | Gibbs equilibrium         | Entropy dissipation|
| PME         | Convergence to Barenblatt            | Self-similar profile      | Entropy + L^1     |
| HJ          | Convergence to paraboloid            | Hopf–Lax minimum          | Variational       |
| Burgers     | N-wave decay                         | Entropy solution          | Shock dissipation |
| MCF         | Extinction (sphere)                  | Round sphere              | Area dissipation  |
| AC          | Phase selection (±1)                 | Uniform states            | Lyapunov          |
| NS (2D)    | Attractor (compact set)              | Unknown structure         | Viscous dissipation|

The NLS long-time behavior is unique in the Atlas:
- **No convergence to a fixed point** (unlike FP, PME, AC, CH).
- **No irreversible simplification** (unlike HJ, Burgers, MCF).
- **Coherent structures (solitons) persist forever** (unlike every other architecture, where localized structures eventually decay or annihilate).

The NLS "attractor" is not a point or a finite-dimensional set — it is a *decomposition principle*: every solution eventually separates into solitons (persistent) + radiation (dispersing). This decomposition is the *dispersive analogue* of the phase-separation in CH and the shock-coarsening in Burgers — a process by which the solution simplifies into canonical components.

---

## 5. Comparison with FP, PME, HJ, Burgers, NS, MCF, AC/CH, TFE, RD, and ED

### 5.1 The Three-Pole Structure

The PDE Atlas has three fundamental dynamical poles, and NLS completes the triangle:

**Diffusive pole (FP, PME, AC/CH, TFE):**
- Mechanism: amplitude decay through smoothing.
- Energy: decreasing (Lyapunov).
- Long-time: convergence to equilibrium.
- Time direction: irreversible (arrow of time).

**Hyperbolic pole (HJ, Burgers):**
- Mechanism: gradient compression through transport.
- Energy: conserved between shocks, dissipated at shocks.
- Long-time: shock decay, N-wave.
- Time direction: irreversible (entropy production at shocks).

**Dispersive pole (NLS):**
- Mechanism: phase interference through dispersion.
- Energy: *exactly conserved* (Hamiltonian).
- Long-time: scattering (defocusing) or soliton resolution (focusing 1D).
- Time direction: *reversible* (no arrow of time).

### 5.2 Feature-by-Feature Comparison

| Feature                    | NLS              | FP/PME/TFE      | HJ/Burgers       | NS            | MCF           |
|----------------------------|--------------------|------------------|-------------------|---------------|---------------|
| Propagation                | Dispersive (phase) | Diffusive (ampl.)| Transport (charac.)| Mixed        | Geometric     |
| Energy                     | **Conserved**      | Decreasing       | Conserved*/dissip.| Decreasing   | Decreasing    |
| Mass                       | **Conserved (L^2)**| Conserved        | Conserved (Burgers)| Conserved   | Not conserved |
| Reversibility              | **Yes**            | No               | No                | No           | No            |
| Smoothing                  | **None**           | Yes              | None              | Yes          | Yes           |
| Solitons                   | **Yes**            | No               | No                | No           | No            |
| Blowup                     | Focusing, d >= 2   | No               | Certain (shocks)  | Open (3D)    | Certain       |
| Attractor                  | **Scattering/solitons** | Equilibrium | Shock/N-wave      | Open         | Extinction    |
| Long-time simplification   | **Soliton resolution** | Convergence  | Shock merging     | Open         | Topological   |
| Conservation laws           | **3 (M, H, P)**   | 0-1              | 1 (Burgers)       | 2 (mass+mom.)| 0             |
| Integrability (1D)          | **Yes**            | No               | Yes (Hopf-Cole)   | No           | No            |

### 5.3 NLS and ED: Oscillatory Horizons

The NLS and ED architectures share a structural parallel through the concept of *oscillatory horizons*:

- **ED:** The sieve boundary at prime p separates integers divisible by p from those not yet sieved. As the sieve advances (activating more primes), the horizon expands and the density of surviving integers decreases — a *discrete, multiplicative* spreading process.

- **NLS:** The dispersive spreading creates *phase horizons* — boundaries beyond which different frequency components have dephased sufficiently that their superposition is effectively random. As time advances, the phase horizon expands and the effective amplitude |psi| decreases — a *continuous, oscillatory* spreading process.

Both architectures spread "density" (event density in ED, wave amplitude in NLS) through a process that reduces local concentration while preserving a global invariant (total prime density asymptotically in ED, total mass ||psi||_{L^2} in NLS). The mechanisms are different (multiplicative sieving vs. phase interference) but the structural pattern is the same: *spreading that preserves a conserved total*.

### 5.4 Summary

| Feature                    | NLS          | FP    | PME   | HJ    | Burgers| NS    | MCF   | AC/CH | RD    |
|----------------------------|--------------| ------|-------|-------|--------|-------|-------|-------|-------|
| Field type                 | **Complex**  | Real  | Real  | Real  | Real   | Real  | Geom. | Real  | Real  |
| PDE type                   | **Dispersive**| Parab.| Parab.| Hyperb.| Hyperb.| Mixed| Parab.| Parab.| Parab.|
| Energy                     | **Conserved**| Decr. | Decr. | N/A   | Dissip.| Decr.*| Decr. | Decr. | Const.|
| Reversible                 | **Yes**      | No    | No    | No    | No     | No    | No    | No    | No    |
| Solitons                   | **Yes**      | No    | No    | No    | No     | No    | No    | No    | No    |
| Hamiltonian                | **Yes**      | No    | No    | No    | No     | Yes(E)| No    | No    | No    |
| Conservation laws          | **3**        | 1     | 1     | 0     | 1      | 2     | 0     | 0-1   | Const.|
| Blowup                     | Foc.,d>=2   | No    | No    | Certain| Certain| Open | Certain| No   | Const.|
| Smoothing                  | **None**     | Yes   | Yes   | None  | None   | Yes   | Yes   | Yes   | Yes   |
| Long-time                  | **Scatter/soliton**| Equil.| Baren.| Paraboloid| N-wave| Open | Extinct.| Equil.| Const.|
| Parameters                 | 1 (sign)    | 2     | 1     | 0     | 0      | 2     | 0     | 3     | Many  |

NLS is the *unique dispersive, complex-valued, Hamiltonian, time-reversible, soliton-supporting, three-conservation-law* architecture in the Atlas. It completes the three-pole structure: diffusive (parabolic) — hyperbolic (transport) — **dispersive (Schrödinger)**.

---

*End of Mode 2: PDE → Extremal Dynamics. Mode 3 (Channels → Constraint Surface) will follow in a subsequent file.*
