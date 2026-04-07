# AD Evaluation: Keller–Segel System — Architectural Specification

Allen Proxmire

April 2026

---

## 1. Implicit Axioms of the Keller–Segel Architecture

The Keller–Segel (KS) system models the collective motion of biological cells (bacteria, amoebae, immune cells) that both diffuse randomly and migrate toward a self-produced chemical signal — a process called *chemotaxis*. It is the canonical PDE for *self-organized aggregation*: the cells produce a chemoattractant, the chemoattractant diffuses and creates a concentration gradient, and the cells drift up this gradient, concentrating in regions of high cell density. The resulting positive feedback loop — more cells → more signal → more attraction → more cells — is the architecture's *defining dynamical mechanism* and the source of its most dramatic structural feature: *finite-time blowup through mass concentration*.

The KS system occupies a fundamentally new position in the PDE Atlas. Every previously evaluated architecture is either *local* (no coupling between distant points through an elliptic equation) or, if nonlocal (NS pressure), the nonlocality is a *constraint enforcement mechanism* (incompressibility) rather than a *dynamical driver*. In the KS system, the nonlocality is the *primary dynamical mechanism*: the chemoattractant field v is determined by a *global elliptic solve* (Poisson equation), and the gradient of v is what drives the aggregation. The nonlocality is not a constraint — it is the *engine* of the dynamics.

The KS system is also the first architecture with *mass-concentrating blowup* — a singularity in which a finite amount of mass concentrates at a single point in finite time, producing a Dirac delta in the density u. This is qualitatively different from every other blowup type in the Atlas:
- NS (3D): vorticity may blow up (open), but mass is spread by incompressibility.
- NLS (focusing): amplitude concentrates, but the L^2 norm (mass) is preserved.
- HJ/Burgers: gradients steepen, but the function itself remains bounded.
- MCF: curvature blows up at a point, but mass is not a concept (no density).
- KS: the *density itself* concentrates into a delta function — the most physical and dramatic form of blowup.

### Axiom KS-1: Density Field u(x, t) >= 0

The primary state variable is a non-negative scalar density field u(x, t) : R^d x [0, T) → [0, infinity), representing the local cell concentration. The non-negativity is a physical requirement: cell density cannot be negative. The density u is the *directly physical quantity* — it represents the number of cells per unit volume at each point.

### Axiom KS-2: Chemoattractant Field v(x, t)

The secondary state variable is a scalar field v(x, t) : R^d x [0, T) → R, representing the concentration of the chemoattractant (the chemical signal produced by the cells). The field v is *not* an independent dynamical variable in the parabolic–elliptic model — it is *slaved* to the density u through an elliptic equation (Poisson equation). In the parabolic–parabolic model, v has its own dynamics (diffusion + production + degradation).

The KS system is a *two-field architecture* — the first in the Atlas with two coupled scalar fields where one is slaved to the other through an elliptic equation. This coupling is the structural origin of the nonlocality.

### Axiom KS-3: Diffusion of u

The cells undergo random motion (Brownian-type diffusion):

    Diffusion term: Delta u

This is the standard second-order diffusion — the same stabilizing mechanism as in FP, PME (for non-degenerate diffusion), AC, and RD. The diffusion spreads the cell density, opposing concentration. It is the *stabilizing channel* of the KS architecture.

### Axiom KS-4: Chemotactic Drift

The cells drift up the gradient of the chemoattractant v:

    Chemotactic term: -div(u nabla v) = -nabla u . nabla v - u Delta v

This is a *first-order advection* of u by the velocity field nabla v. The drift is:
- *Density-dependent:* The flux is u nabla v — the drift velocity is nabla v, but the flux is proportional to both u and nabla v. Where there are more cells (u large), the chemotactic flux is larger.
- *Signal-dependent:* The drift direction is nabla v — the cells move toward higher v, which is where more cells are (because cells produce v). This creates the *positive feedback loop*: cells → signal → drift toward cells → more cells → more signal → ...
- *Destabilizing:* The chemotactic drift concentrates the cell density, opposing the diffusion's spreading. The drift is the *aggregation mechanism* — the sole source of dynamical instability in the KS system.

### Axiom KS-5: Chemoattractant Dynamics

In the *parabolic–elliptic* (simplified) KS system:

    -Delta v = u    (or 0 = Delta v - v + u in the full parabolic–elliptic model)

The chemoattractant v is determined *instantaneously* by the cell density u through an elliptic equation. This is the KS analogue of the NS pressure Poisson equation — a global elliptic solve that couples distant points. The solution is:

    v(x) = integral G(x, y) u(y) dy

where G is the Green's function of -Delta (or of -Delta + I). In 2D: G(x, y) = -(1/(2 pi)) log|x - y|. In 3D: G(x, y) = 1/(4 pi |x - y|).

The chemoattractant thus creates a *nonlocal potential* — each cell at y contributes to the signal at x through the Green's function. The chemoattractant gradient nabla v at x is:

    nabla v(x) = integral nabla_x G(x, y) u(y) dy

This is a *nonlocal integral* of the density u — the drift velocity at x depends on the cell distribution *everywhere*. The nonlocality is the *defining structural feature* of the KS system.

In the *parabolic–parabolic* model:

    tau v_t = Delta v - v + u

the chemoattractant has its own dynamics (diffusion + degradation + production by cells). The parabolic–elliptic model corresponds to tau = 0 (instantaneous chemoattractant equilibration).

### Axiom KS-6: Mass Conservation for u

The cell density u is conserved in total:

    d/dt integral u(x, t) dx = 0

This follows from the divergence form of the u-equation:

    u_t = Delta u - div(u nabla v) = div(nabla u - u nabla v)

with no-flux boundary conditions. The total cell mass M = integral u dx is an exact invariant. No cells are created or destroyed — they are only redistributed.

Mass conservation is the *primary structural constraint* of the KS system. It controls the large-scale behavior: the total mass M determines whether blowup occurs (in 2D, blowup iff M > 8 pi for the classical parabolic–elliptic KS).

### Axiom KS-7: Nonlocal Aggregation

The combination of KS-4 (chemotactic drift) and KS-5 (chemoattractant determined by elliptic solve) produces a *nonlocal aggregation* mechanism:

    u_t = Delta u - div(u nabla(-Delta)^{-1} u) = Delta u + div(u nabla v)

where v = (-Delta)^{-1} u is the *nonlocal potential* generated by u itself. The aggregation term can be written as:

    -div(u nabla v) = -div(u integral nabla G(x, y) u(y) dy)

This is a *nonlocal, self-interacting advection*: the density u generates a potential v, and then drifts in the gradient of its own potential. The self-interaction is *attractive* (cells are attracted to regions of high cell density) and *nonlocal* (the attraction is mediated by the Green's function, which couples all points in the domain).

The nonlocal aggregation is the KS's *defining architectural feature* — the only architecture in the Atlas where a density field generates a nonlocal potential and then drifts in the gradient of that potential. The NS pressure is also generated by a Poisson equation, but it enforces a *constraint* (incompressibility); the KS chemoattractant generates a *driving force* (aggregation). The structural roles are opposite: NS pressure *prevents* concentration (it pushes fluid apart when it tries to compress); KS chemoattractant *drives* concentration (it pulls cells together).

### Axiom KS-8: Blowup Mechanism (Mass Concentration)

The competition between diffusion (KS-3, stabilizing) and aggregation (KS-4 + KS-7, destabilizing) can be *won by aggregation* — when the cell mass is sufficiently large, the aggregation overwhelms the diffusion and the density concentrates at a point in finite time:

    ||u(t)||_{L^{infinity}} → infinity    as t → T*    (blowup)

At the blowup time T*, the density u forms a *Dirac delta*:

    u(x, T*) contains a component M_0 delta(x - x_0)

where M_0 is the concentrated mass and x_0 is the concentration point. This is *mass-concentrating blowup* — a finite amount of mass is squeezed into zero volume.

The blowup is controlled by the *critical mass* (in 2D):

    M_crit = 8 pi    [for the classical parabolic–elliptic KS in R^2]

- M < 8 pi: global existence (diffusion wins).
- M = 8 pi: threshold (the ground-state steady solution is the critical object).
- M > 8 pi: blowup in finite time (aggregation wins).

The critical mass 8 pi is the *sharp threshold* — the KS analogue of the NLS critical mass M_* = ||Q||_{L^2}^2. It is determined by the *best constant in the logarithmic Hardy–Littlewood–Sobolev inequality* — a variational characterization linking the KS blowup to the geometry of the logarithmic potential.

### Axiom KS-9: Scaling Symmetry (Critical Mass in 2D)

The 2D parabolic–elliptic KS has the scaling symmetry:

    u_lambda(x, t) = lambda^2 u(lambda x, lambda^2 t),    v_lambda(x, t) = v(lambda x, lambda^2 t)

Under this scaling:

    M_lambda = integral u_lambda dx = integral u dx = M    (mass-preserving)

The *mass* is the scaling-invariant quantity — the same critical role as the L^2 norm in the NLS. The 2D KS is *L^1-critical*: the mass (L^1 norm of u) is the quantity that determines global existence vs. blowup.

The criticality structure:
- d = 1: subcritical. Global existence for all masses.
- d = 2: *L^1-critical*. Blowup iff M > 8 pi (critical mass).
- d >= 3: supercritical. Blowup can occur for arbitrarily small mass.

### Axiom KS-10: No Hamiltonian Structure

The KS system is *not Hamiltonian*. It has a *free-energy functional*:

    F[u] = integral u log u dx + (1/2) integral u v dx = integral u log u dx - (1/2) integral |nabla v|^2 dx

that satisfies:

    dF/dt = -integral u |nabla(log u - v)|^2 dx <= 0

The free energy *decreases* — the KS system is a *gradient flow* of F in the Wasserstein metric (the same metric as the PME and FP gradient flows). The gradient-flow structure makes the KS dissipative — but unlike FP and PME (where the free energy is bounded below and drives convergence to equilibrium), the KS free energy is *not bounded below* when M > 8 pi (in 2D). The free energy can decrease to -infinity in finite time — this is the *free-energy signature of blowup*.

The KS free-energy structure is *intermediate* between:
- FP/PME (free energy bounded below → global existence, convergence to equilibrium).
- NLS/KdV (energy conserved, no free-energy dissipation).
- NS (energy decreases but no sharp threshold linking energy to blowup).

The KS free energy provides the *sharpest connection between energy landscape and singularity* of any architecture: the free energy is bounded below iff M < 8 pi iff global existence holds. The three conditions are *equivalent*.

---

## 2. Canonical PDE in Architectural Form

### 2.1 The Parabolic–Elliptic Keller–Segel System

    u_t = Delta u - chi div(u nabla v)                       ... (KS-u)
    0 = Delta v - v + u    (or -Delta v = u on R^2)          ... (KS-v)

with chi > 0 the chemotactic sensitivity. For simplicity, we set chi = 1.

### 2.2 Reduced Form (2D, Newtonian Potential)

On R^2 with v = -(1/(2 pi)) log|.| * u (Newtonian potential):

    u_t = Delta u - div(u nabla v) = Delta u + div(u nabla(-Delta)^{-1} u)

This is a *single nonlocal PDE* for u — the v-equation has been eliminated by substituting the explicit Green's function.

### 2.3 Channel-Labeled Decomposition

    u_t =    Delta u           -        div(u nabla v)
         |______________|    |__________________________|
           Diffusion (D)       Chemotactic aggregation (A)

    where v satisfies:
         -Delta v = u    (or Delta v - v + u = 0)
    |__________________________________________|
      Nonlocal potential (N)

    producing (when A > D):
         Mass concentration → Dirac delta blowup
    |________________________________________________|
      Blowup mechanism (B)

### 2.4 Free-Energy Structure

    F[u] = integral u log u dx - (1/(4 pi)) integral integral u(x) log|x-y| u(y) dx dy

    dF/dt = -integral u |nabla log u - nabla v|^2 dx = -D(t) <= 0

The free energy F is the difference of two terms:
- *Entropy:* integral u log u dx (favors spreading — increases as u spreads).
- *Interaction energy:* -(1/(4 pi)) integral integral u(x) log|x-y| u(y) dx dy (favors aggregation — decreases as u concentrates).

When M > 8 pi, the interaction energy wins: F → -infinity as u concentrates, and the blowup is energetically *favorable*.

### 2.5 Boundary and Initial Conditions

    u(x, 0) = u_0(x) >= 0,    integral u_0 dx = M
    u_0 in L^1(R^d) ∩ L^{infinity}(R^d)    (or similar)

---

## 3. Channel Identification

### Channel D: Diffusion (Stabilizing)

    D(u) = Delta u

- **Role:** Spreads the cell density, opposing aggregation. The standard second-order diffusion — the same mechanism as in FP, AC, and the RD class.
- **Locality:** Local. Second-order spatial derivatives at each point.
- **Linearity:** Linear.
- **Stability role:** Stabilizing. Damps high-frequency modes at rate k^2. Prevents concentration of u at small scales.
- **Scale action:** Mode k damped at rate k^2. The diffusion is strongest at small scales and weakest at large scales.

### Channel A: Chemotactic Aggregation (Destabilizing)

    A(u) = -div(u nabla v) = -nabla u . nabla v - u Delta v

where v = (-Delta)^{-1} u (or solution of Delta v - v + u = 0).

- **Role:** Drives cells up the chemoattractant gradient. Concentrates u in regions of high v (which are regions of high u — positive feedback). The *sole destabilizing mechanism* of the KS architecture.
- **Locality:** *Nonlocal.* The drift velocity nabla v at x depends on u(y) for all y in the domain (through the Green's function of -Delta). The nonlocality is *intrinsic* — it arises from the biophysics (the chemoattractant diffuses and creates a long-range signal).
- **Linearity:** Nonlinear in u. The aggregation term -div(u nabla v) = -div(u nabla(-Delta)^{-1} u) is *quadratic* in u (the product of u with an integral of u). This is a *nonlocal quadratic nonlinearity* — the most dangerous type: each factor of u amplifies the other through the nonlocal coupling.
- **Stability role:** Destabilizing. The aggregation drives concentration — more cells → more signal → more drift → more concentration. This positive feedback is the *blowup engine*.
- **Scale action:** The aggregation operates at *all scales simultaneously*: the nonlocal potential v = (-Delta)^{-1} u couples every scale of u to every other scale. The effect is strongest at large scales (where the logarithmic/algebraic Green's function is largest) and weakest at small scales. This is the *opposite* of the diffusion's scale action (strongest at small, weakest at large). The competition between D (small-scale stabilization) and A (large-scale destabilization) is the *fundamental dynamical tension* of the KS system.

### Channel N: Nonlocal Potential

    N: v = (-Delta)^{-1} u    (or solution of -Delta v = u)

- **Role:** Mediates the aggregation. The chemoattractant v is the *nonlocal messenger* that communicates the cell density at distant points. The potential v at x is the integral of u over the entire domain, weighted by the Green's function G(x, y).
- **Locality:** *Nonlocal.* v at x depends on u(y) for all y. The Green's function G(x, y) ~ -log|x-y| (2D) or G(x, y) ~ 1/|x-y| (3D) decays *algebraically* — the coupling is long-range.
- **Linearity:** Linear in u (v depends linearly on u through the Green's function).
- **Stability role:** Neutral (the potential itself is neither stabilizing nor destabilizing — it is the *medium* through which the aggregation acts).
- **Scale action:** The Poisson equation -Delta v = u couples all scales. Low-k modes of u generate low-k modes of v through 1/k^2 amplification (the Green's function amplifies long wavelengths). This low-k amplification is what makes the aggregation strongest at large scales.

**Comparison with NS pressure:** The NS pressure also satisfies a Poisson equation (-Delta p = source), but its *role* is opposite:
- NS pressure: *enforces incompressibility* (a constraint). The pressure gradient pushes fluid *apart* when it tries to compress.
- KS potential: *drives aggregation* (a force). The potential gradient pulls cells *together*.

Both are nonlocal (elliptic solve), but their dynamical roles are structurally opposed. NS pressure *prevents* concentration; KS potential *drives* it.

### Channel B: Blowup Mechanism (Mass Concentration)

    B: ||u(t)||_{L^{infinity}} → infinity    as t → T*    (when M > 8 pi in 2D)

- **Role:** The emergent consequence of the D–A competition when aggregation wins. The density u concentrates at a point, forming a Dirac delta. The blowup is *mass-concentrating* — a finite amount of mass is squeezed into zero volume.
- **Locality:** Local in trigger (concentration occurs at a specific point x_0). Global in consequence (the mass redistribution affects the entire solution).
- **Linearity:** Nonlinear (emerges from the quadratic nonlocal nonlinearity).
- **Stability role:** Destabilizing (the most extreme dynamical outcome).
- **Scale action:** Concentrates at the smallest scales. As blowup approaches, the density profile sharpens: u ~ lambda^{-2} U(x/lambda) with lambda → 0. The blowup is a *scale-zero singularity* — mass collapsing to a point.

### Channel Summary Table

| Channel | Symbol | Term / Feature               | Locality    | Linearity   | Stability         | Scale Action              |
|---------|--------|------------------------------|-------------|-------------|-------------------|---------------------------|
| Diffusion    | D | Delta u                     | Local       | Linear      | Stabilizing       | Rate ~ k^2 (small-scale)  |
| Aggregation  | A | -div(u nabla v)             | **Nonlocal**| Nonlinear   | Destabilizing     | Strongest at large scale   |
| Potential    | N | -Delta v = u                | **Nonlocal**| Linear in u | Neutral (medium)  | 1/k^2 amplification        |
| Blowup       | B | Mass concentration → delta  | Local*      | Nonlinear   | Destabilizing     | Concentrates at k → ∞     |

*Local trigger, global consequence.

### Channel Count Comparison

| Architecture | Local Channels | Nonlocal Channels | Blowup Channel | Total |
|-------------|---------------|-------------------|----------------|-------|
| **KS**      | **1 (D)**     | **2 (A, N)**      | **1 (B)**      | **4** |
| NS          | 2 (A, V)      | 1 (P pressure)    | 0-1 (open)     | 4-5   |
| NLS         | 2 (D, N)      | 0                 | 0-1 (focusing) | 3-4   |
| FP          | 2 (T, D)      | 0                 | 0              | 3-4   |
| PME         | 1 (D_nl)      | 0                 | 0              | 3-4   |

KS is the *only* architecture with *two nonlocal channels* (A and N are both mediated by the elliptic solve). NS has one nonlocal channel (pressure); all other architectures have zero. The KS is the *most nonlocal* architecture in the Atlas.

---

## 4. Relation to FP, PME, HJ, Burgers, NLS, KdV, NS, MCF, AC/CH, TFE, RD, and ED

### 4.1 KS as the Aggregation Pole

The PDE Atlas now has *five structural poles*:

    Diffusive pole: FP / PME / AC / CH / TFE    (smoothing → equilibrium)
    Hyperbolic pole: HJ / Burgers                (steepening → shocks)
    Dispersive pole: NLS / KdV                    (oscillatory spreading → solitons)
    Geometric pole: MCF                           (curvature → extinction)
    Aggregation pole: KS                          (nonlocal attraction → mass concentration)

The KS introduces the *fifth pole*: a nonlocal, self-attractive, mass-concentrating architecture that is structurally distinct from all four previous poles. The aggregation mechanism (density generates a potential and drifts in its own potential's gradient) has no counterpart in any other architecture.

### 4.2 KS vs. NS: Opposite Roles for the Nonlocal Channel

| Feature                    | Keller–Segel                 | Navier–Stokes              |
|----------------------------|------------------------------|-----------------------------|
| Nonlocal equation          | -Delta v = u                 | Delta p = -partial_i partial_j(u_i u_j) |
| Nonlocal field             | Chemoattractant v            | Pressure p                  |
| Role of nonlocal field     | **Drives aggregation**       | **Enforces incompressibility** |
| Effect on density          | **Concentrates** (attracts)  | **Prevents concentration** (pushes apart) |
| Blowup mechanism           | Mass concentration (delta)   | Vorticity blowup (open)     |
| Critical threshold          | 8 pi (2D, exact)            | Open (3D)                   |
| Conservation               | Mass (integral u = M)        | Mass + momentum              |
| Gradient-flow structure    | Yes (Wasserstein)            | No                           |

The KS and NS nonlocal channels have *structurally opposite roles*: the NS pressure prevents concentration (it is a *repulsive* nonlocal force), while the KS chemoattractant drives concentration (it is an *attractive* nonlocal force). The two architectures are *nonlocal duals*: same mathematical mechanism (Poisson equation), opposite physical effect.

### 4.3 KS vs. NLS: Mass-Concentrating vs. Amplitude-Concentrating Blowup

| Feature                    | Keller–Segel                 | NLS (focusing)              |
|----------------------------|------------------------------|-----------------------------|
| Blowup type                | **Mass concentration** (u → delta) | **Amplitude concentration** (||nabla psi|| → ∞) |
| What concentrates          | The density u itself          | The gradient nabla psi      |
| L^1 norm at blowup         | Preserved (mass conserved)   | Preserved (L^2 conserved)   |
| L^{infinity} norm at blowup| → infinity (delta function)  | → infinity (amplitude blowup)|
| Critical threshold (2D)    | M = 8 pi (mass)              | M = M_* (L^2 mass)         |
| Mechanism                  | Nonlocal self-attraction     | Local self-focusing          |
| Nonlocality                | **Yes** (Poisson equation)   | No (fully local)             |
| Post-blowup                | Measure-valued solutions     | Open                         |

The KS and NLS blowup types are structurally analogous (both concentrate something at a point past a critical threshold) but mechanistically different (nonlocal attraction for KS, local self-focusing for NLS). The KS blowup is more *physical* — it concentrates the density itself (the directly observable quantity), while the NLS concentrates the gradient (a derivative of the observable).

### 4.4 KS vs. PME/FP: Gradient Flow with Blowup

The KS, PME, and FP are all *Wasserstein gradient flows*:

| Architecture | Free Energy F                    | Bounded Below? | Blowup?  |
|-------------|----------------------------------|----------------|----------|
| FP          | integral rho V dx + sigma^2 integral rho log rho dx | Yes (V confining) | No |
| PME         | integral u^m / (m-1) dx          | Yes (m > 1)    | No       |
| **KS**      | **integral u log u - (1/2) integral u v** | **No (M > 8pi)** | **Yes** |

The KS free energy F is *unbounded below* when M > 8 pi — it can decrease to -infinity in finite time. The FP and PME free energies are bounded below and drive convergence to equilibrium. The KS is the *only gradient-flow architecture in the Atlas with blowup* — the first demonstration that gradient-flow structure does not prevent singularities when the energy landscape is unbounded below.

### 4.5 KS and ED: Horizons and Concentration

The KS blowup — mass concentrating at a point — has a structural parallel with the ED *activation* process: at each prime p^2, a new width layer "activates" in the Factor Skyline, concentrating the coverage structure. The KS mass concentration is the continuous, dynamical analogue of the ED discrete activation: a density (of cells / of coverage) concentrates at a point (in space / at p^2) through a self-reinforcing mechanism (chemotaxis / sieve coverage).

Both processes represent *density concentration driven by self-interaction*: in ED, the coverage at a prime p interacts with the coverage at other primes through the multiplicative structure; in KS, the cell density at a point x interacts with the cell density at other points through the chemoattractant potential.

### 4.6 Positioning Table

| Feature                    | KS               | NS       | NLS      | FP       | PME      | KdV      | Burgers  | MCF      |
|----------------------------|------------------|----------|----------|----------|----------|----------|----------|----------|
| Nonlocal channels          | **2 (A, N)**     | 1 (P)    | 0        | 0        | 0        | 0        | 0        | 0        |
| Nonlocality role           | **Drives aggregation** | Enforces constraint | N/A | N/A | N/A | N/A | N/A | N/A |
| Blowup type                | **Mass concentration** | Vorticity(?) | Amplitude| None| None| None | Gradient | Curvature|
| Critical threshold (2D)    | **M = 8pi (exact)** | Open  | M_*      | N/A      | N/A      | N/A      | N/A      | N/A      |
| Gradient-flow structure    | **Wasserstein**  | No       | No       | Wasserstein| Wasserstein| No  | No       | L^2      |
| Free energy bounded below  | **No (M>8pi)**   | N/A      | Indef.(foc.)| Yes  | Yes      | N/A      | N/A      | Yes(area)|
| Conservation               | Mass (L^1)       | Mass+mom.| Mass+en.+mom.| Mass| Mass   | Infinite | Mass     | None     |
| Mass-concentrating blowup  | **Yes (delta)**  | No       | No       | No       | No       | No       | No       | No       |
| Parameters                 | 1 (chi)          | 2        | 1 (sign) | 2        | 1 (m)    | 0        | 0        | 0        |

KS is the *unique nonlocal-aggregating, mass-concentrating, gradient-flow-with-blowup, critical-mass-threshold* architecture in the Atlas. It is structurally orthogonal to every other architecture: no other PDE has nonlocal self-attraction as its primary dynamical mechanism, mass-concentrating blowup as its singularity type, or an unbounded-below free energy driving a gradient flow to singularity.

---

*End of Architectural Specification. The Mode 1 (Axiom → Envelope) analysis will follow in the next file.*
