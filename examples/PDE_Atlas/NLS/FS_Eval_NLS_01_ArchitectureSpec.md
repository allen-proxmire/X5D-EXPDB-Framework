# AD Evaluation: Nonlinear Schrödinger Equation — Architectural Specification

Allen Proxmire

April 2026

---

## 1. Implicit Axioms of the NLS Architecture

The Nonlinear Schrödinger Equation (NLS) describes the evolution of a complex-valued wave field psi(x, t) under the combined action of linear dispersion and nonlinear self-interaction. It is the *dispersive pole* of the PDE Atlas — the only architecture whose dynamics are governed by dispersion (oscillatory spreading) rather than diffusion (monotone smoothing) or transport (steepening). Where parabolic architectures (AC, CH, PME, TFE, FP) smooth, and hyperbolic architectures (HJ, Burgers) steepen, the NLS *disperses*: it spreads wave packets through phase interference without dissipating energy.

The NLS occupies a fundamentally new structural position in the Atlas. Every previously evaluated architecture is either *dissipative* (energy decreases: AC, CH, PME, TFE, FP, MCF) or *entropy-producing* (information lost at singularities: HJ, Burgers). The NLS is *conservative* — it preserves energy exactly, produces no entropy, and loses no information. It is a *Hamiltonian PDE*, governed by a symplectic structure rather than a gradient-flow or entropy structure. The dynamics are *time-reversible*: if psi(x, t) is a solution, then psi*(x, -t) is also a solution. No other architecture in the Atlas has this property.

The NLS is also the *first complex-valued* architecture in the Atlas. Every previous state variable (u, v, phi, h, rho, Gamma_t) is real-valued. The NLS field psi = Re(psi) + i Im(psi) has two real components coupled through the imaginary unit i, which enforces the *dispersive* (oscillatory) rather than *diffusive* (decaying) character of the evolution. The factor i in front of psi_t is the single structural choice that separates dispersion from diffusion — replacing i with 1 converts the NLS into a nonlinear heat equation.

### Axiom NLS-1: Complex Field

The state variable is a complex-valued field psi(x, t) : R^d x R → C. The field psi represents a wave amplitude — its modulus |psi|^2 gives the local intensity (or probability density, in the quantum-mechanical context), and its phase arg(psi) gives the local oscillation state. Both amplitude and phase are dynamically active — the NLS evolves both simultaneously.

The complex character is *structural*, not a notational convenience. The real and imaginary parts of psi are coupled through the imaginary unit i in the PDE; they cannot be decoupled into independent equations. The complex field carries *twice* the degrees of freedom of a real scalar field — and uses both.

### Axiom NLS-2: Locality

All interactions are local: the time evolution of psi at x depends only on psi(x, t), nabla psi(x, t), and Delta psi(x, t). There are no nonlocal operators, no integral constraints, no pressure-type coupling. The NLS is *fully local* at both formulation and solution levels.

### Axiom NLS-3: Dispersive Core

The linear part of the NLS is the *free Schrödinger equation*:

    i partial_t psi = -Delta psi

This is a *dispersive* equation, not a diffusive one. The distinction:

- **Diffusion** (partial_t u = Delta u): mode k decays as exp(-k^2 t). Energy is dissipated. The fundamental solution is a Gaussian that *spreads and decays*.
- **Dispersion** (i partial_t psi = -Delta psi): mode k oscillates as exp(-i k^2 t). Energy is *conserved*. The fundamental solution is a complex oscillatory integral that *spreads without decaying*.

The dispersive character arises from the factor i in front of partial_t psi. The operator i partial_t + Delta is *unitary*: it preserves the L^2 norm of psi (||psi(t)||_{L^2} = ||psi_0||_{L^2} for all t). This is the structural basis of mass conservation (NLS-6).

The dispersion relation for mode k is omega(k) = |k|^2, giving:
- Phase velocity: v_ph = omega/k = k (faster for higher frequencies).
- Group velocity: v_gr = d omega/dk = 2k (wave packets spread at speed 2k).

Different frequencies travel at different speeds → wave packets spread → *dispersive broadening*. This spreading is the NLS's substitute for diffusion: it reduces the L^{infinity} norm of psi (the wave packet flattens) without reducing the L^2 norm (the total mass is conserved).

### Axiom NLS-4: Gauge Invariance (Phase Symmetry)

The NLS is invariant under the *gauge transformation*:

    psi → e^{i theta} psi    for any constant theta in R

This means: multiplying psi by a constant phase factor e^{i theta} produces another solution of the same equation. The gauge invariance is a *continuous symmetry* (U(1) symmetry group) that, by Noether's theorem, produces the conservation of mass (NLS-6).

The gauge invariance is the NLS's *defining symmetry* — the analogue of Galilean invariance in NS, geometric invariance in MCF, and conservation-law structure in Burgers. It is the structural expression of the fact that the phase of psi is physically meaningful only up to a global constant.

### Axiom NLS-5: Hamiltonian Structure

The NLS is a *Hamiltonian PDE*: it can be written as:

    i partial_t psi = delta H / delta psi*

where H[psi] is the *Hamiltonian* (energy functional):

    H[psi] = integral [ |nabla psi|^2 ± (1/2) |psi|^4 ] dx

The ± sign corresponds to the defocusing (+) and focusing (-) cases.

The Hamiltonian structure implies:
- **Energy conservation:** dH/dt = 0. The energy is *exactly* conserved for all time. No dissipation, no entropy production, no energy transfer to "heat."
- **Symplectic structure:** The evolution is a canonical transformation on the infinite-dimensional phase space. The dynamics are *volume-preserving* in phase space (Liouville's theorem for infinite-dimensional systems).
- **Time-reversibility:** If psi(x, t) solves NLS, then psi*(x, -t) also solves NLS. The dynamics have no preferred time direction — unlike every parabolic and entropy-producing architecture in the Atlas.

The Hamiltonian structure is the *deepest structural commitment* of the NLS architecture. It is the reason NLS has no dissipation, no monotone convergence, no Lyapunov functional — and simultaneously the reason NLS has exact conservation laws, time-reversibility, and soliton solutions.

### Axiom NLS-6: Mass Conservation (L^2 Norm)

The *mass* (or charge, or probability):

    M[psi] = integral |psi|^2 dx

is exactly conserved: dM/dt = 0. This follows from the gauge invariance (NLS-4) via Noether's theorem, and can be verified directly by multiplying the NLS by psi* and taking the imaginary part.

Mass conservation in the NLS is analogous to probability conservation in FP (integral rho = 1) and mass conservation in PME/CH/TFE/Burgers (integral u = M). But the mechanism is different: FP conserves mass through divergence form; PME/CH/TFE through conservation-law structure; Burgers through flux conservation. NLS conserves mass through *unitary evolution* — the L^2 norm is preserved because the linear propagator is unitary (i partial_t + Delta is a skew-adjoint operator on L^2).

### Axiom NLS-7: Momentum Conservation

The *momentum*:

    P[psi] = Im integral psi* nabla psi dx

is exactly conserved: dP/dt = 0. This follows from the translational invariance of the NLS (invariance under x → x + a) via Noether's theorem.

Momentum conservation is absent from every other architecture in the Atlas (except NS, which conserves momentum through the Navier–Stokes equations). The NLS is the *only non-fluid architecture* with momentum conservation.

### Axiom NLS-8: Cubic Nonlinearity (Focusing/Defocusing)

The nonlinear term is ± |psi|^2 psi — a *cubic* nonlinearity:

    i partial_t psi + Delta psi ± |psi|^2 psi = 0

Two cases with qualitatively different dynamics:

**Defocusing (+):** i psi_t + Delta psi + |psi|^2 psi = 0.
- The nonlinearity *repels* — it acts like a positive potential proportional to |psi|^2, pushing the wave function apart.
- The energy H = integral [|nabla psi|^2 + (1/2)|psi|^4] dx is positive definite → *no blowup* (the energy controls the H^1 norm).
- Global smooth solutions for all initial data in H^1.
- The dynamics are globally well-posed in all dimensions.

**Focusing (-):** i psi_t + Delta psi - |psi|^2 psi = 0.
- The nonlinearity *attracts* — it acts like a negative potential, concentrating the wave function.
- The energy H = integral [|nabla psi|^2 - (1/2)|psi|^4] dx can be negative → *blowup possible* (the energy does not control the H^1 norm by itself).
- In d >= 2: finite-time blowup can occur (||nabla psi(t)||_{L^2} → infinity at a finite time T*).
- In d = 1: global existence (the mass + energy + Gagliardo–Nirenberg inequality closes).

The focusing/defocusing dichotomy is the NLS's *most consequential structural feature*: the sign of the nonlinearity determines whether the architecture is globally well-posed (defocusing) or admits finite-time singularities (focusing, d >= 2). This is the NLS analogue of the NS 2D/3D regularity split — but with a *sign* rather than a *dimension* as the control parameter.

### Axiom NLS-9: No Diffusion

The NLS has *no diffusive term*. The time derivative is i partial_t psi (imaginary, dispersive), not partial_t psi (real, diffusive). The operator i partial_t + Delta is *skew-adjoint*, not *self-adjoint* — it generates a *unitary group* (oscillation), not a *contraction semigroup* (decay).

The absence of diffusion means:
- No Lyapunov functional in the parabolic sense (no energy that monotonically decreases).
- No smoothing: rough initial data remains rough (the L^2 norm is preserved, not decreased).
- No entropy production: information is preserved, not lost.
- No irreversibility: the dynamics are time-reversible.

Adding a diffusive term (epsilon Delta psi with real epsilon, giving the complex Ginzburg–Landau equation) converts the NLS from Hamiltonian to dissipative — a qualitatively different architecture.

### Axiom NLS-10: No Reaction Terms

No source/sink terms. The evolution is conservative: mass, energy, and momentum are all preserved. No creation, destruction, or external forcing.

---

## 2. Canonical PDE in Architectural Form

### 2.1 The Cubic NLS

    i partial_t psi + Delta psi ± |psi|^2 psi = 0                ... (NLS)

with psi : R^d x R → C, and + for defocusing, - for focusing.

### 2.2 Hamiltonian Form

    i partial_t psi = delta H / delta psi*

where:

    H[psi] = integral [ |nabla psi|^2 ± (1/2) |psi|^4 ] dx      ... (Energy)

### 2.3 Conservation Laws

    M = integral |psi|^2 dx                                       (mass, from gauge)
    H = integral [|nabla psi|^2 ± (1/2)|psi|^4] dx               (energy, from time translation)
    P = Im integral psi* nabla psi dx                              (momentum, from spatial translation)

### 2.4 Channel-Labeled Decomposition

    i partial_t psi =    -Delta psi         ±      |psi|^2 psi
                     |__________________|    |___________________|
                       Dispersion (D)          Nonlinearity (N)

    governed by:
      Hamiltonian structure (H)        Phase symmetry (G)
    |__________________________|    |_________________________|
      Energy-conserving flow          Gauge invariance

### 2.5 Scaling Symmetry

The cubic NLS has the *pseudoconformal scaling*:

    psi_lambda(x, t) = lambda^{d/2} psi(lambda x, lambda^2 t)    [mass-preserving rescaling]

The critical (scale-invariant) Sobolev space is H^{d/2 - 1}(R^d). For the cubic NLS:

- d = 1: subcritical (H^{-1/2}, below L^2). Global existence for all L^2 data.
- d = 2: *critical* (L^2 is the critical space). The mass M = ||psi||_{L^2}^2 is the critical quantity. Focusing NLS in 2D can blow up if and only if M > M_* (the mass of the ground-state soliton).
- d = 3: supercritical (H^{1/2}, above L^2). Blowup possible for arbitrarily small data (focusing case).

### 2.6 Soliton Solutions (Focusing, 1D)

The focusing 1D NLS has *soliton* solutions — localized traveling waves:

    psi(x, t) = A sech(A(x - vt)) exp(i(vx/2 + (A^2 - v^2/4)t))

where A is the amplitude and v is the velocity. The soliton:
- Maintains its shape indefinitely (no dispersion, no decay).
- Travels at constant speed v.
- Has mass M = 2A and energy H = 2A^3/3 - v^2 A.
- Is *stable* under perturbation (orbital stability — the perturbed solution stays close to a translated/phase-rotated soliton).

Solitons are the NLS analogue of the PME Barenblatt profiles and the FP Gibbs–Boltzmann equilibrium — localized coherent structures that are attractors of the dynamics. But unlike Barenblatt (which is an *asymptotic* attractor that all solutions converge to) and Gibbs–Boltzmann (a *global* attractor), the NLS soliton is a *local* attractor in the orbital sense — perturbations stay nearby but do not converge to zero.

---

## 3. Channel Identification

### Channel D: Dispersion

    D(psi) = -Delta psi    [inside i psi_t = -Delta psi + ...]

- **Role:** Spreads the wave function in space through phase-dependent interference. Different Fourier modes propagate at different speeds (omega = k^2), causing wave packets to broaden. The dispersion channel is the NLS's analogue of the diffusion channel in parabolic architectures — it controls the spatial distribution of psi — but it operates through *oscillation* (phase rotation) rather than *decay* (amplitude reduction).
- **Locality:** Local. Depends on psi and Delta psi at each point.
- **Linearity:** Linear. The Laplacian is a linear operator.
- **Stability role:** Stabilizing (in a dispersive sense). The dispersion spreads the wave function, reducing the L^{infinity} norm without reducing the L^2 norm. For the free Schrödinger equation (no nonlinearity), ||psi(t)||_{L^{infinity}} <= C t^{-d/2} ||psi_0||_{L^1} — the amplitude decays as t^{-d/2} through dispersive spreading. This *dispersive decay* is the NLS's primary stabilizing mechanism — it competes with the focusing nonlinearity's tendency to concentrate.
- **Scale action:** Mode k oscillates at frequency k^2 (quadratic dispersion). High-frequency modes oscillate faster and spread more rapidly. The dispersion is *frequency-dependent* — unlike diffusion, which damps all modes, dispersion causes modes to *dephase* (lose coherence) rather than decay.

### Channel N: Nonlinearity

    N(psi) = ± |psi|^2 psi

- **Role:** The self-interaction of the wave function. In the focusing case (-), the nonlinearity concentrates the wave function, working against dispersion. In the defocusing case (+), the nonlinearity repels, working with dispersion.
- **Locality:** Local. |psi|^2 psi depends on psi at each point (no derivatives).
- **Linearity:** Nonlinear. Cubic in psi.
- **Stability role:**
  - *Defocusing (+):* Stabilizing. The repulsive nonlinearity enhances dispersion. The energy H = integral [|nabla psi|^2 + (1/2)|psi|^4] dx is positive definite, controlling the H^1 norm → global well-posedness.
  - *Focusing (-):* Destabilizing (in d >= 2). The attractive nonlinearity opposes dispersion and can overcome it, driving the wave function to concentrate at a point → finite-time blowup (||nabla psi|| → infinity).
- **Scale action:** Scale-free (no derivatives). The nonlinearity acts identically at all spatial scales. Its effect is strongest where |psi| is largest (high-amplitude regions).

### Channel H: Hamiltonian Structure

    H: i psi_t = delta H / delta psi*,    dH/dt = 0,    dM/dt = 0,    dP/dt = 0

- **Role:** Structural property of the full evolution. The Hamiltonian structure ensures exact conservation of energy, mass, and momentum. It is the NLS's analogue of the gradient-flow structure in AC/CH/PME/TFE — but with the opposite consequence: gradient flows *dissipate* energy; Hamiltonian flows *conserve* energy.
- **Locality:** The Hamiltonian H is a global functional, but the PDE is local.
- **Linearity:** Nonlinear (through the |psi|^4 term in H).
- **Stability role:** Conservative (neither stabilizing nor destabilizing in the monotone sense). The Hamiltonian structure prevents energy loss but also prevents energy gain — the dynamics are *isentropic* (no entropy production).
- **Scale action:** All-scale. The conservation laws constrain the dynamics at every scale simultaneously.

### Channel G: Gauge Invariance

    G: psi → e^{i theta} psi    is a symmetry for all theta

- **Role:** The U(1) phase symmetry. Generates mass conservation (Noether's theorem). The gauge invariance means that the absolute phase of psi is unobservable — only phase *differences* (interference) matter.
- **Locality:** Global symmetry (same phase rotation everywhere).
- **Linearity:** Linear (phase rotation is a linear operation on the complex plane).
- **Stability role:** Neutral (symmetry, not dynamics). The gauge invariance constrains the admissible dynamics (the PDE must respect the symmetry) but does not stabilize or destabilize.
- **Scale action:** All-scale (the symmetry applies at every frequency).

### Channel Summary Table

| Channel | Symbol | Term / Feature          | Locality | Linearity   | Stability           | Scale Action          |
|---------|--------|-------------------------|----------|-------------|---------------------|-----------------------|
| Dispersion   | D | -Delta psi             | Local    | Linear      | Stabilizing (dispersive)| omega = k^2 (quadratic) |
| Nonlinearity | N | ±\|psi\|^2 psi        | Local    | Nonlinear   | Defoc: stab. Foc: destab.| Scale-free           |
| Hamiltonian  | H | dH/dt = 0, symplectic  | Global*  | Nonlinear   | Conservative        | All-scale             |
| Gauge        | G | psi → e^{i theta} psi | Global   | Linear      | Neutral (symmetry)  | All-scale             |

*H is a global functional; the PDE is local.

### Channel Count Comparison

| Architecture | Dynamical Channels | Structural/Symmetry | Total |
|-------------|-------------------|---------------------|-------|
| **NLS**     | **2 (D, N)**      | **2 (H, G)**        | **4** |
| Burgers/HJ  | 1 (T)             | 2 (S, V)            | 3     |
| MCF         | 1 (K)             | 2 (G, T)            | 3     |
| PME         | 1 (D_nl)          | 2 (C, G)            | 3+1   |
| FP          | 2 (T, D)          | 2 (C, P)            | 3+1   |
| AC          | 2 (R, S)          | 2 (G, M)            | 4     |
| NS          | 2 (A, V)          | 3 (P, C, F)         | 5     |

NLS has four channels — comparable to AC and FP. The distinctive feature is that both structural channels (H and G) are *conservative* (energy-preserving + symmetry), whereas in parabolic architectures the structural channels are *dissipative* (Lyapunov + conservation).

---

## 4. Relation to FP, PME, HJ, Burgers, NS, MCF, AC/CH, TFE, RD, and ED

### 4.1 The Dispersive Pole

The PDE Atlas architectures can be organized along a *smoothing–dispersing–steepening* axis:

    FP (max smooth) → PME/TFE → AC/CH → MCF → NS → Burgers/HJ (max steep)
                                        ↑
                                       NLS (dispersive, orthogonal)

NLS is *orthogonal* to the smoothing–steepening axis. It is neither smoothing (no energy decay) nor steepening (no gradient blowup in the HJ/Burgers sense). It is *dispersive* — a third mode of dynamics that spreads wave packets through phase interference rather than amplitude decay or gradient compression.

The three fundamental dynamical modes:
1. **Diffusion (parabolic):** Spreads + decays. Energy decreases. L^{infinity} norm decreases. Irreversible.
2. **Transport (hyperbolic):** Moves + steepens. Energy conserved (or dissipated at shocks). Finite-time singularity. Irreversible (entropy production at shocks).
3. **Dispersion (Schrödinger):** Spreads + oscillates. Energy conserved. L^{infinity} norm may decrease (dispersive decay). *Reversible* (Hamiltonian, time-reversible).

NLS is the *representative* of the third mode — the only architecture in the Atlas that is purely dispersive with no dissipative or steepening component.

### 4.2 NLS vs. Parabolic Architectures

| Feature                    | NLS                          | Parabolic (FP/PME/AC/CH/TFE) |
|----------------------------|------------------------------|-------------------------------|
| Time derivative            | i psi_t (imaginary)          | u_t (real)                    |
| Operator character         | Skew-adjoint (unitary)       | Self-adjoint (contraction)    |
| Energy                     | Conserved (Hamiltonian)      | Decreasing (Lyapunov)        |
| L^2 norm                   | Conserved (mass)             | May change                    |
| L^{infinity} decay         | Dispersive (t^{-d/2})       | Diffusive (t^{-d/2} or exp.) |
| Smoothing                  | None (no regularity gain)    | Yes (instantaneous C^{infinity}) |
| Reversibility              | Time-reversible              | Irreversible                  |
| Attractor                  | No attractor (Hamiltonian)   | Equilibrium / self-similar    |
| Solitons                   | Yes (focusing, 1D)           | No (monotone dynamics)        |

The deepest difference: parabolic architectures are *dissipative* (they lose information); NLS is *conservative* (it preserves information). This single distinction — encoded in the factor i in front of psi_t — produces all the qualitative differences.

### 4.3 NLS vs. HJ/Burgers

| Feature                    | NLS                          | HJ/Burgers                   |
|----------------------------|------------------------------|-------------------------------|
| PDE type                   | Dispersive (Schrödinger)     | Hyperbolic (transport)        |
| Energy                     | Conserved (Hamiltonian)      | Conserved (Burgers between shocks) / N/A (HJ) |
| Singularity                | Blowup (focusing, d >= 2)   | Shock/kink (certain)          |
| Reversibility              | Time-reversible              | Irreversible (entropy at shocks) |
| Dispersion relation        | omega = k^2 (quadratic)     | omega = k v (linear)          |
| Solitons                   | Yes (focusing)               | No (only shocks)              |
| Contraction                | No (Hamiltonian preserves distances) | L^1 + L^{infinity} (Burgers), L^{infinity} (HJ) |

NLS and HJ/Burgers share the *absence of diffusion* — neither has a smoothing mechanism. But they respond to this absence differently: HJ/Burgers develops shocks (gradient/velocity blowup); NLS develops dispersive spreading (or, in the focusing case, self-focusing blowup). The mechanisms are qualitatively different: HJ/Burgers singularities are *compressive* (characteristics converge); NLS focusing singularities are *concentrating* (the wave function collapses to a point through self-attraction).

### 4.4 NLS vs. NS

| Feature                    | NLS                          | Navier–Stokes                |
|----------------------------|------------------------------|-------------------------------|
| State variable             | Complex scalar psi           | Real vector **u**            |
| Linearity of transport     | Linear (Delta psi) + nonlinear (|psi|^2 psi) | Nonlinear (u.nabla u) |
| Nonlocal channel           | None                         | Pressure (Poisson eq.)       |
| Conservation               | Mass + energy + momentum     | Mass + momentum (+ energy if inviscid) |
| Hamiltonian                | Yes                          | Yes (inviscid Euler)         |
| Diffusion                  | None (dispersive)            | Viscosity (nu Delta u)       |
| Turbulence                 | *Wave turbulence* (weak)     | *Hydrodynamic turbulence* (strong) |
| Blowup                     | Focusing, d >= 2             | Open (3D)                    |

NLS and the inviscid Euler equations share *Hamiltonian structure* — both conserve energy and have no dissipation. But the NLS Hamiltonian is *dispersive* (the linear part is i Delta, producing oscillation), while the Euler Hamiltonian is *transport-based* (the linear part is advection, producing material transport). The two Hamiltonian PDEs produce qualitatively different dynamics: NLS has solitons and wave turbulence; Euler has vortex dynamics and hydrodynamic turbulence.

### 4.5 NLS and ED: Phase-Driven Horizons

The NLS dispersion relation omega = k^2 creates *phase-driven horizons*: regions where different frequency components have dephased sufficiently that the wave packet has effectively spread beyond recognition. These dispersive horizons are the oscillatory analogue of the ED arithmetic horizons (where the sieve has covered enough primes to determine the local density) and the HJ characteristic horizons (where characteristics have crossed and information has been lost at shocks).

All three horizon types — arithmetic (ED), characteristic (HJ/Burgers), and dispersive (NLS) — represent *boundaries of effective information propagation* in their respective architectures. The difference is the mechanism: factorization in ED, characteristic crossing in HJ/Burgers, and phase interference in NLS.

### 4.6 Positioning Table

| Feature                    | NLS              | FP    | PME   | HJ    | Burgers| NS    | MCF   | AC/CH | RD    |
|----------------------------|-----------------|-------|-------|-------|--------|-------|-------|-------|-------|
| Field type                 | **Complex**     | Real  | Real  | Real  | Real   | Real  | Geom. | Real  | Real  |
| PDE type                   | **Dispersive**  | Parab.| Parab.| Hyperb.| Hyperb.| Mixed | Parab.| Parab.| Parab.|
| Energy                     | **Conserved**   | Decreasing | Decreasing | N/A | Dissip.(shocks) | Decreasing* | Decreasing | Decreasing | Constitutive |
| Mass conservation          | **Yes (L^2)**   | Yes   | Yes   | No    | Yes    | Yes   | No    | Variable | Constitutive |
| Momentum conservation      | **Yes**         | No    | No    | No    | No     | **Yes**| No   | No    | No    |
| Hamiltonian                | **Yes**         | No    | No    | No    | No     | Yes(Euler)| No | No    | No    |
| Reversible                 | **Yes**         | No    | No    | No    | No     | No(NS)/Yes(Euler)| No | No | No |
| Solitons                   | **Yes (foc.)**  | No    | No    | No    | No     | No    | No    | No    | No    |
| Blowup                     | Foc., d>=2     | No    | No    | Certain| Certain| Open(3D)| Certain| No | Constitutive |
| Smoothing                  | **None**        | Yes   | Yes   | None  | None   | Yes   | Yes   | Yes   | Yes   |
| Dispersive decay           | **Yes (t^{-d/2})**| No | No   | No    | No     | No    | No    | No    | No    |
| Parameters                 | 1 (sign ±)     | 2     | 1     | 0     | 0      | 2     | 0     | 3     | Many  |

NLS is the *unique dispersive, complex-valued, Hamiltonian, time-reversible, soliton-supporting* architecture in the Atlas. It is structurally orthogonal to both the parabolic wing (diffusion, dissipation, monotone convergence) and the hyperbolic wing (transport, steepening, shock formation). It represents the *third fundamental mode* of PDE dynamics: dispersion.

---

*End of Architectural Specification. The Mode 1 (Axiom → Envelope) analysis will follow in the next file.*
