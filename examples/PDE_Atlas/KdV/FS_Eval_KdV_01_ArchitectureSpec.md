# AD Evaluation: Korteweg–de Vries Equation — Architectural Specification

Allen Proxmire

April 2026

---

## 1. Implicit Axioms of the KdV Architecture

The Korteweg–de Vries (KdV) equation describes the evolution of a real-valued wave amplitude u(x, t) under the combined action of nonlinear advection and linear third-order dispersion. It is the *canonical integrable dispersive equation* — the real-valued, odd-order counterpart of the NLS. Where the NLS is a complex-valued, even-order (Laplacian), Hamiltonian dispersive PDE, the KdV is a real-valued, odd-order (third derivative), Hamiltonian dispersive PDE. Together, the NLS and KdV span the two fundamental classes of integrable dispersive waves: Schrödinger-type (even order, complex) and KdV-type (odd order, real).

The KdV occupies a *precise structural position* in the PDE Atlas: it is the *dispersive conservation law* — combining the conservation-law structure of Burgers (partial_t u + partial_x f(u) = 0) with the dispersive spreading of the NLS (i psi_t + Delta psi = 0), but in an odd-order, real-valued framework. Where Burgers has nonlinear advection *without* dispersion (producing shocks), and the linear Schrödinger equation has dispersion *without* nonlinear advection, the KdV has *both* — and the balance between them produces *solitons*: localized traveling waves that propagate without distortion.

The KdV is historically the *first* soliton equation (Zabusky–Kruskal, 1965) and the *first* equation shown to be completely integrable via the inverse scattering transform (Gardner–Greene–Kruskal–Miura, 1967). It is the prototype for integrable systems, infinite-dimensional Hamiltonian PDEs, and the theory of soliton interactions. In the PDE Atlas, the KdV represents the *integrable dispersive-transport hybrid* — the architecture that fuses the hyperbolic pole (Burgers-type transport) with the dispersive pole (Schrödinger-type spreading) in a completely integrable framework.

### Axiom KdV-1: Real Scalar Field

The state variable is a real-valued scalar field u(x, t) : R x R → R. Unlike the NLS (which has a complex field psi in C), the KdV operates on a real field — no phase, no gauge symmetry, no U(1) invariance. The field u represents a wave amplitude (surface elevation of shallow water, ion-acoustic wave amplitude, etc.) and is directly physical.

The real-valued character places the KdV closer to the hyperbolic architectures (HJ, Burgers — both real-valued) than to the NLS (complex-valued). The KdV is the *real-valued dispersive architecture* — dispersion without the complexification that the Schrödinger equation requires.

### Axiom KdV-2: Locality

All interactions are local: the time evolution of u at x depends only on u, u_x, u_{xx}, and u_{xxx} at x. No nonlocal operators, no integral constraints, no pressure coupling. Fully local at formulation and solution levels.

### Axiom KdV-3: Third-Order Dispersion

The linear dispersive term is u_{xxx} — a *third-order* spatial derivative. The dispersion relation for the linearized KdV (u_t + u_{xxx} = 0) is:

    omega(k) = -k^3

Key properties:
- **Odd-order dispersion:** omega(k) = -k^3 is an odd function of k. This means the dispersion is *asymmetric* — left-moving and right-moving waves have different phase velocities. The odd-order character distinguishes KdV from NLS (even-order, omega = k^2, symmetric).
- **Third-order:** The dispersion involves three spatial derivatives, making the KdV a *third-order PDE* — intermediate between the second-order NLS (or heat equation) and the fourth-order CH/TFE.
- **Dispersive (not diffusive):** The coefficient of u_{xxx} is real (not multiplied by i as in the NLS or by a positive constant as in diffusion). The linear KdV u_t + u_{xxx} = 0 is dispersive: different frequencies propagate at different speeds (v_ph = -k^2), causing wave packets to spread. But the spreading is *non-dissipative*: the L^2 norm is conserved.
- **Infinite-speed propagation:** Like the NLS and unlike the PME/HJ, the KdV has infinite propagation speed — compactly supported initial data becomes nonzero everywhere instantly.

### Axiom KdV-4: Nonlinear Advection

The nonlinear term is u u_x — the same *self-advection* as in the inviscid Burgers equation. The field u transports itself at speed proportional to u. This is a *first-order* nonlinearity involving one spatial derivative.

The nonlinear advection is the *Burgers heritage* of the KdV: it is the mechanism that would produce shocks if dispersion were absent. The KdV equation is, in a precise sense, "Burgers + third-order dispersion":

    KdV: u_t + u u_x + u_{xxx} = 0
    Burgers: u_t + u u_x = 0

The dispersion (u_{xxx}) is the *regularizing term* that prevents the Burgers-type shock formation. Instead of shocks, the balance between nonlinear steepening (u u_x) and dispersive spreading (u_{xxx}) produces *solitons*.

### Axiom KdV-5: Hamiltonian Structure

The KdV is a Hamiltonian PDE with two compatible Hamiltonian structures (bi-Hamiltonian):

**First Hamiltonian structure:**

    u_t = partial_x (delta H_1 / delta u)

with H_1 = integral [(1/2) u_x^2 - (1/6) u^3] dx (the "energy").

**Second Hamiltonian structure:**

    u_t = (partial_x^3 + (2/3)(u partial_x + partial_x u)) (delta H_0 / delta u)

with H_0 = (1/2) integral u^2 dx (the "mass").

The bi-Hamiltonian structure is the *algebraic foundation of integrability*: the two compatible Hamiltonian structures generate, through the Lenard recursion, an infinite sequence of conservation laws and commuting Hamiltonian flows. The bi-Hamiltonian structure is *unique to KdV* in the Atlas — no other evaluated architecture has two compatible Hamiltonian structures.

### Axiom KdV-6: Conservation Laws (Infinitely Many)

The KdV has *infinitely many* independent conservation laws:

    H_0 = integral u dx                                    (mass)
    H_1 = integral u^2 dx                                  (momentum / L^2 norm)
    H_2 = integral [(1/2) u_x^2 - (1/6) u^3] dx           (energy)
    H_3 = integral [u_{xx}^2 + (5/3) u u_x^2 + (5/36) u^4] dx
    ...

Each H_n is a polynomial functional of u and its derivatives, conserved exactly: dH_n/dt = 0 for all n. The existence of infinitely many conservation laws is the hallmark of *complete integrability* — it means the KdV has "as many conservation laws as degrees of freedom" (in an appropriate infinite-dimensional sense).

The infinitely many conservation laws provide *infinitely many constraints* on the dynamics — far more than the NLS's three (mass, energy, momentum) or the Burgers/HJ's one or two. This infinite rigidity is the structural reason that KdV solitons interact *elastically* (no energy transfer, no shape change) and that the KdV is *exactly solvable* via inverse scattering.

### Axiom KdV-7: Complete Integrability (Inverse Scattering Transform)

The KdV is *completely integrable* via the inverse scattering transform (IST):

1. **Direct scattering:** Map u(x, 0) to scattering data {eigenvalues, norming constants, reflection coefficient} of the Schrödinger operator -partial_{xx} + u.
2. **Time evolution:** The scattering data evolve *linearly* in time (trivial ODE for each component).
3. **Inverse scattering:** Reconstruct u(x, t) from the evolved scattering data via the Gel'fand–Levitan–Marchenko integral equation.

The IST converts the nonlinear KdV into a *linear problem* in scattering space. It is the infinite-dimensional analogue of solving a system of ODEs by finding action-angle variables. The integrability is the *deepest structural feature* of the KdV — it means the KdV is, in a precise sense, a *linear system in disguise*.

### Axiom KdV-8: Euclidean Geometry (1D)

The KdV is formulated on R (one spatial dimension) with the standard derivative. The restriction to one dimension is *structural*, not merely a simplification: the KdV's integrability, soliton structure, and bi-Hamiltonian framework are *intrinsically one-dimensional*. Higher-dimensional generalizations (KP equation, etc.) exist but are different architectures.

### Axiom KdV-9: No Diffusion

No second-order dissipative term. The KdV is purely dispersive + advective. Adding viscosity (nu u_{xx}) gives the KdV–Burgers equation — a different, non-integrable architecture that dissipates energy and destroys solitons.

### Axiom KdV-10: No Reaction / No Forcing

No source/sink terms. The evolution is conservative: all H_n are preserved. The KdV is autonomous and self-driven.

---

## 2. Canonical PDE in Architectural Form

### 2.1 The KdV Equation

    u_t + 6 u u_x + u_{xxx} = 0                              ... (KdV)

(The factor 6 is a conventional normalization that simplifies the soliton formulas. Other normalizations exist; the structural content is independent of this choice.)

### 2.2 Conservation-Law Form

    u_t + partial_x (3 u^2 + u_{xx}) = 0

The KdV is a *conservation law with third-order dispersive flux*: the flux is F(u) = 3u^2 + u_{xx}, which includes both the Burgers-type quadratic flux (3u^2) and a dispersive correction (u_{xx}). The conservation form ensures that integral u dx is preserved.

### 2.3 Hamiltonian Form

    u_t = partial_x (delta H_2 / delta u) = partial_x (u_{xx} + 3u^2) = u_{xxx} + 6 u u_x

with H_2 = integral [(1/2)u_x^2 - u^3] dx.

### 2.4 Channel-Labeled Decomposition

    u_t + 6 u u_x + u_{xxx} = 0

    =    -6 u u_x          -        u_{xxx}
    |__________________|    |___________________|
      Nonlinear advection      Third-order dispersion
      (Channel A)               (Channel D_3)

    governed by:
      Bi-Hamiltonian structure (H)     Integrability / IST (I)
    |________________________________|  |__________________________|
      Two compatible symplectic forms    Infinite conservation laws

### 2.5 Soliton Solutions

The KdV admits *soliton* (solitary wave) solutions:

    u(x, t) = 2 kappa^2 sech^2(kappa (x - 4 kappa^2 t - x_0))

where kappa > 0 is the amplitude parameter and x_0 is the initial position. The soliton:
- Has amplitude 2 kappa^2 and speed 4 kappa^2 — *taller solitons travel faster*.
- Has width ~ 1/kappa — *taller solitons are narrower*.
- Is a localized, positive, shape-preserving traveling wave.

The amplitude-speed relation (speed proportional to amplitude) is a *structural feature* that distinguishes KdV solitons from NLS solitons (where speed and amplitude are independent parameters). The KdV soliton is *uniquely determined* by a single parameter (kappa), while the NLS soliton has two independent parameters (amplitude and speed).

### 2.6 Multi-Soliton Interactions

The N-soliton solution describes N solitons that interact nonlinearly but emerge from the interaction with their shapes, amplitudes, and speeds *exactly preserved*:

    N solitons in → [nonlinear interaction] → N solitons out (same shapes, shifted positions + phases)

The interaction is *elastic*: no energy, mass, or information is transferred between solitons. Each soliton acquires a *phase shift* (position displacement) from the interaction but is otherwise unchanged. This elasticity is a consequence of the integrability (KdV-7) and the infinite conservation laws (KdV-6).

---

## 3. Channel Identification

### Channel A: Nonlinear Advection (Burgers Heritage)

    A(u) = 6 u u_x

- **Role:** Self-advection — u transports itself at speed proportional to u. This is the *same* nonlinear mechanism as in the Burgers equation (u u_x), producing steepening of the wave profile. Without the dispersion channel, the advection would form shocks (Burgers dynamics). With dispersion, the steepening is balanced and solitons form.
- **Locality:** Local. u u_x depends on u and u_x at each point.
- **Linearity:** Nonlinear. Quadratic (u times u_x).
- **Stability role:** Destabilizing (steepening). The advection tilts the wave profile: the peak (large u) moves faster than the trough (small u), steepening the leading edge. This is the Burgers steepening mechanism — the *transport pole* of the KdV dynamics.
- **Scale action:** First-order in k. The advection rate is proportional to u k. Scale-free in terms of the nonlinearity itself (no derivatives beyond first order).

### Channel D_3: Third-Order Dispersion

    D_3(u) = u_{xxx}

- **Role:** Dispersive spreading — different Fourier modes travel at different speeds (v_ph = -k^2), causing wave packets to spread. The dispersion *counters* the advection's steepening: it spreads the wave just as fast as the advection steepens it, producing a stable balance (the soliton).
- **Locality:** Local. u_{xxx} involves third spatial derivatives at each point.
- **Linearity:** Linear. The third derivative is a linear operator.
- **Stability role:** Stabilizing (dispersive). The dispersion prevents shock formation by spreading the wave energy across frequencies. In the absence of nonlinearity, the dispersion alone produces the *Airy function* spreading: ||u(t)||_{L^{infinity}} ~ t^{-1/3} (slower than the Schrödinger t^{-d/2} because the KdV dispersion omega = k^3 is cubic, not quadratic).
- **Scale action:** Mode k has phase velocity v_ph = -k^2 (quadratic in k) and group velocity v_gr = -3k^2. High-frequency modes travel faster than low-frequency modes. The dispersive scaling is *cubic* in k: the dispersion relation omega = -k^3 gives a *third-order* spreading rate, intermediate between the NLS's second-order (omega = k^2) and no higher-order PDE in the Atlas.

### Channel H: Bi-Hamiltonian Structure

    H: u_t = partial_x (delta H_2 / delta u) = J_1 (delta H_2 / delta u)
       u_t = J_2 (delta H_0 / delta u)

where J_1 = partial_x and J_2 = partial_x^3 + (2/3)(u partial_x + partial_x u) are the two compatible Hamiltonian operators.

- **Role:** The bi-Hamiltonian structure generates the infinite hierarchy of conservation laws through the *Lenard recursion*: starting from H_0, each application of J_2 J_1^{-1} produces the next conservation law. The bi-Hamiltonian structure is the *algebraic engine* of integrability.
- **Locality:** J_1 = partial_x is local; J_2 involves partial_x^3 and u partial_x — also local.
- **Linearity:** The Hamiltonian operators J_1, J_2 are linear (J_2 depends on u but acts linearly on the variational derivative). The Hamiltonian functionals H_n are nonlinear in u.
- **Stability role:** Conservative. Each H_n is exactly conserved. The bi-Hamiltonian structure provides *infinitely many rigid constraints* on the dynamics.
- **Scale action:** All-scale. The conservation laws control u at every Sobolev level simultaneously (H_0 controls L^1, H_1 controls L^2, H_2 controls H^1, H_3 controls H^2, etc.).

### Channel I: Integrability (Inverse Scattering Transform)

    I: u(x, 0) → {scattering data} → [linear evolution] → {scattering data(t)} → u(x, t)

- **Role:** The IST provides the *exact solution* of the KdV for all time. It converts the nonlinear PDE into a linear evolution in scattering space. The integrability is the structural feature that makes KdV *exactly solvable* — not just well-posed but *explicitly computable*.
- **Locality:** The IST itself is *nonlocal* (it involves solving the Schrödinger eigenvalue problem -psi_{xx} + u psi = lambda psi on all of R). But the *KdV PDE* is local — the IST is an analytical tool, not a dynamical channel. The integrability is a *structural property* of the architecture, not a nonlocal coupling.
- **Linearity:** The scattering data evolve *linearly* in time — the IST linearizes the nonlinear KdV.
- **Stability role:** Maximally stabilizing. Integrability provides *complete control*: the solution is determined for all time by the initial scattering data, and the scattering data evolve trivially (linearly). No finite-time blowup, no loss of regularity, no dynamical surprises.
- **Scale action:** All-scale. The IST controls every aspect of the solution: the discrete spectrum (solitons), the continuous spectrum (radiation), and their interaction.

### Channel Summary Table

| Channel | Symbol | Term / Feature           | Locality | Linearity   | Stability            | Scale Action          |
|---------|--------|--------------------------|----------|-------------|----------------------|-----------------------|
| Advection    | A   | 6 u u_x                | Local    | Nonlinear   | Destabilizing (steep.)| Rate ~ u k (1st-order) |
| Dispersion   | D_3 | u_{xxx}                | Local    | Linear      | Stabilizing (dispersive)| omega = -k^3 (3rd-order) |
| Bi-Hamiltonian| H  | Two compatible J_1, J_2| Local    | Mixed       | Conservative (rigid) | All-scale (infinite H_n) |
| Integrability | I  | IST / Lax pair          | Structural| Linearizing | Maximally stabilizing| Complete control       |

### Channel Count Comparison

| Architecture | Dynamical | Structural/Symmetry | Integrability | Total |
|-------------|-----------|---------------------|---------------|-------|
| **KdV**     | **2 (A, D_3)** | **1 (H)**     | **1 (I)**     | **4** |
| NLS         | 2 (D, N)  | 2 (H, G)            | 1 (1D foc.)  | 4-5   |
| Burgers     | 1 (T)     | 2 (S, V)            | 1 (Cole–Hopf) | 3-4  |
| HJ          | 1 (T)     | 2 (S, V)            | 0             | 3     |
| FP          | 2 (T, D)  | 2 (C, P)            | 0             | 4     |
| PME         | 1 (D_nl)  | 2 (C, G)            | 0             | 3+1   |

KdV has four channels — comparable to NLS and FP. The distinctive feature is the *integrability channel* I, which is shared (in specific regimes) with the NLS (integrable in 1D focusing) and Burgers (Cole–Hopf linearizable), but is *structurally deepest* in the KdV: the bi-Hamiltonian structure + IST + infinite conservation laws make KdV the *most completely integrable* architecture in the Atlas.

---

## 4. Relation to FP, PME, HJ, Burgers, NLS, NS, MCF, AC/CH, TFE, RD, and ED

### 4.1 KdV as the Dispersive Conservation Law

The KdV equation sits at the *intersection* of two structural lineages:

**From Burgers (hyperbolic pole):** The nonlinear advection u u_x is the Burgers mechanism — self-transport, steepening, would-be shock formation.

**From NLS (dispersive pole):** The third-order dispersion u_{xxx} is the odd-order dispersive mechanism — spreading, phase interference, oscillatory dynamics.

The KdV *fuses* these two mechanisms:

    KdV = Burgers advection + odd-order dispersion + integrability

The fusion produces something that neither Burgers nor NLS alone can generate: *real-valued solitons* that travel at amplitude-dependent speed. Burgers alone produces shocks (no solitons). NLS alone produces complex solitons (with phase). KdV produces *real, localized, positive, speed-amplitude-locked solitons* — a qualitatively new coherent structure.

### 4.2 KdV vs. Burgers: Dispersion Regularizes Transport

| Feature                    | KdV                          | Burgers                      |
|----------------------------|------------------------------|------------------------------|
| Advection                  | u u_x (same)                 | u u_x (same)                 |
| Dispersion                 | **u_{xxx} (third-order)**    | **None**                     |
| Shock formation            | **No** (dispersion prevents) | **Yes** (no regularization)  |
| Solitons                   | **Yes** (adv. + disp. balance)| **No** (only shocks)        |
| Integrability              | **IST + Lax pair**           | **Cole–Hopf** (linearizable) |
| Conservation laws          | **Infinitely many**          | One (mass)                   |
| Energy                     | Conserved (Hamiltonian)      | Dissipated at shocks         |
| Reversibility              | **Yes** (Hamiltonian)        | No (entropy at shocks)       |
| Weak solutions needed      | **No** (global smooth)       | Yes (entropy solutions)      |

The single structural addition — third-order dispersion — transforms Burgers (shock-forming, entropy-producing, irreversible) into KdV (soliton-forming, energy-conserving, reversible). Dispersion is the *anti-shock mechanism*: it spreads the wave just fast enough to prevent the Burgers steepening from forming a discontinuity.

### 4.3 KdV vs. NLS: Real vs. Complex Dispersion

| Feature                    | KdV                          | NLS                          |
|----------------------------|------------------------------|------------------------------|
| Field type                 | **Real** (u in R)            | **Complex** (psi in C)       |
| Dispersion order           | **Third** (u_{xxx})          | **Second** (Delta psi)       |
| Dispersion relation        | omega = -k^3 (odd, asymmetric)| omega = k^2 (even, symmetric)|
| Nonlinearity               | u u_x (advective, 1st deriv.)| \|psi\|^2 psi (algebraic, 0th deriv.) |
| Soliton speed              | **Locked to amplitude** (c = 4 kappa^2) | **Independent of amplitude** |
| Gauge invariance           | **No** (real field)          | **Yes** (U(1) phase)         |
| Spatial dimension          | **1D only** (structurally)   | Any d                        |
| Integrability              | **IST + bi-Hamiltonian**    | IST (1D focusing only)       |
| Conservation laws          | **Infinitely many**          | 3 (or infinite in integrable 1D) |
| Hamiltonian structures     | **Two** (bi-Hamiltonian)     | One                          |

The KdV and NLS are the two *fundamental integrable dispersive PDEs*: KdV for real-valued, odd-order dispersion; NLS for complex-valued, even-order dispersion. Together they represent the *complete integrable dispersive sector* of the PDE Atlas.

### 4.4 KdV vs. Parabolic Architectures

| Feature                    | KdV                          | AC/CH/PME/TFE/FP             |
|----------------------------|------------------------------|-------------------------------|
| Smoothing                  | **Dispersive** (no amplitude decay) | **Diffusive** (amplitude decay) |
| Regularity                 | Global smooth (integrable)   | Global smooth (parabolic)     |
| Energy                     | **Conserved** (Hamiltonian)  | Decreasing (Lyapunov)        |
| Reversibility              | **Yes**                      | No                            |
| Solitons                   | **Yes**                      | No                            |
| Attractor                  | Soliton resolution           | Equilibrium / self-similar    |
| Integrability              | **Yes** (IST)                | No (except heat eq. trivially)|

The KdV achieves the *same regularity outcome* as the parabolic architectures (global smooth solutions, no blowup) but through a *completely different mechanism*: integrability + conservation laws rather than diffusion + Lyapunov. The KdV is globally smooth not because it dissipates energy but because it has *too many conservation laws* for the solution to develop singularities.

### 4.5 KdV and ED: Spectral Horizons

The KdV's inverse scattering transform maps the initial data u(x, 0) to scattering data of the Schrödinger operator -psi_{xx} + u psi = lambda psi. The scattering data consist of:
- **Discrete spectrum:** Eigenvalues lambda_n < 0 → solitons (localized, persistent).
- **Continuous spectrum:** Reflection coefficient r(k) → radiation (dispersing, transient).

This spectral decomposition parallels the ED *sieve decomposition*: in ED, each integer is classified by its factorization (primes = "solitonic" = persistent; composites = "radiative" = eliminated by sieving). The KdV spectral decomposition is the *continuous, dynamical analogue* of the ED factorization decomposition: solitons are the "primes" of the wave field (persistent, localized, parameterized by a single number), and radiation is the "composite" background (transient, dispersing, parameterized by a continuous function).

### 4.6 Positioning Table

| Feature                    | KdV              | NLS      | Burgers  | HJ       | FP       | PME      | NS       | MCF      |
|----------------------------|------------------|----------|----------|----------|----------|----------|----------|----------|
| Field type                 | **Real**         | Complex  | Real     | Real     | Real     | Real     | Real     | Geometric|
| PDE order                  | **3rd**          | 2nd      | 1st      | 1st      | 2nd      | 2nd      | 2nd      | 2nd      |
| Dispersion                 | **omega = -k^3** | omega=k^2| None     | None     | None     | None     | None     | None     |
| Advection                  | **u u_x**        | None     | v v_x    | H(u_x)  | b.nabla rho| None  | u.nabla u| None     |
| Solitons                   | **Yes (real)**   | Yes (complex)| No   | No       | No       | No       | No       | No       |
| Integrability              | **IST + bi-Ham.**| IST (1D) | Cole–Hopf| Hopf–Lax| Spectral | No       | No       | No       |
| Conservation laws          | **Infinite**     | 3 (or inf.)| 1     | 0        | 1        | 1        | 2        | 0        |
| Hamiltonian structures     | **2 (bi-Ham.)**  | 1        | 0        | 0        | 0        | 0        | 1 (Euler)| 0        |
| Reversibility              | **Yes**          | Yes      | No       | No       | No       | No       | No(NS)/Yes(E)| No   |
| Smoothing                  | **Dispersive**   | Dispersive| None    | None     | Diffusive| Diffusive| Diffusive| Geometric|
| Blowup                     | **No**           | Foc.d>=2 | Certain  | Certain  | No       | No       | Open(3D) | Certain  |
| Parameters                 | **0**            | 1 (sign) | 0        | 0        | 2        | 1        | 2        | 0        |

KdV is the *unique real-valued, third-order, bi-Hamiltonian, completely integrable, soliton-supporting, infinitely-many-conservation-law, shock-free, globally-smooth dispersive PDE* in the Atlas. It occupies the intersection of the hyperbolic pole (Burgers advection) and the dispersive pole (NLS-type dispersion), fused by integrability into a uniquely complete architecture.

---

*End of Architectural Specification. The Mode 1 (Axiom → Envelope) analysis will follow in the next file.*
