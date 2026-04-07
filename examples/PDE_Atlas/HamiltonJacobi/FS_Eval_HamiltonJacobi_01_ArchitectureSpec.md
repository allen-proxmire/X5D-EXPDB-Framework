# AD Evaluation: Hamilton–Jacobi Equation — Architectural Specification

Allen Proxmire

April 2026

---

## 1. Implicit Axioms of the Hamilton–Jacobi Architecture

The Hamilton–Jacobi (HJ) equation describes the evolution of a scalar potential u(x, t) under a first-order nonlinear transport law. It is the *pure hyperbolic* corner of the PDE Atlas — the only architecture whose dynamics are first-order in time and first-order in space, with no diffusion, no reaction, and no smoothing of any kind. The absence of diffusion means the HJ equation *steepens* rather than smooths: gradients can grow without bound in finite time, producing *shocks* in the gradient field nabla u even from smooth initial data.

The HJ equation occupies a position in the PDE landscape diametrically opposite to the parabolic architectures (AC, CH, PME, TFE, FP). Where those architectures smooth, the HJ equation steepens. Where they have Lyapunov functionals and monotone convergence, the HJ equation has characteristics and caustics. Where they produce equilibria, the HJ equation produces singularities. The HJ equation is the *anti-diffusion* architecture — the minimal PDE that demonstrates what happens when smoothing is entirely absent.

The HJ equation is also the *dual* of the Navier–Stokes architecture in a precise sense: the inviscid Burgers equation (the gradient of HJ) is the one-dimensional, scalar reduction of the Euler equations (the inviscid limit of NS). Where NS operates on a vector velocity field with incompressibility and pressure, HJ operates on a scalar potential with no constraints. HJ is NS stripped of everything except the nonlinear transport.

### Axiom HJ-1: Field Hypothesis (Scalar Potential)

The state variable is a scalar field u(x, t) defined on R^d x [0, T) (or a bounded domain). The field u represents a *potential* — its gradient nabla u is the physically meaningful quantity (velocity in fluid mechanics, wavefront normal in optics, action gradient in classical mechanics). The scalar u itself is determined up to an additive constant; only its spatial derivatives carry information.

This is a departure from every previous architecture: in AC/CH/PME/TFE/FP, the field (phi, u, h, rho) is the primary physical quantity. In HJ, the *gradient* of u is primary, and u itself is an auxiliary potential. This gradient-centric structure is the reason that HJ dynamics are about gradient evolution — steepening, shocks, and caustics in nabla u.

### Axiom HJ-2: Locality

All interactions are local: the time evolution of u at x depends only on nabla u(x, t) — the gradient at the same point. There are no nonlocal operators, no integral constraints, and no pressure-type coupling. The HJ equation is *fully local* at the formulation level.

**Subtlety at the solution level:** The *viscosity solution* of HJ (see HJ-8) involves a global selection principle — choosing the "correct" weak solution among many possible ones. This selection is not a nonlocal *operator* (it does not couple u at different points through a PDE), but it is a *global principle* (the viscosity-solution concept involves test functions at every point). The HJ architecture is local in formulation but requires a global selection principle for well-posedness.

### Axiom HJ-3: First-Order Nonlinear Law

The evolution is governed by a first-order PDE:

    partial_t u + H(nabla u, x) = 0

where H : R^d x R^d → R is the *Hamiltonian* — a prescribed function of the gradient nabla u (and possibly of x). The equation is:
- *First-order in time:* partial_t u appears without higher time derivatives.
- *First-order in space:* Only nabla u (first spatial derivatives) appears, not Delta u or higher.
- *Nonlinear:* H is a nonlinear function of nabla u (generically).

The first-order character is the defining structural feature: no diffusion (which would add Delta u), no biharmonic (which would add Delta^2 u), no reaction (which would add R(u)). The dynamics are *pure transport* along characteristics, with no smoothing mechanism.

### Axiom HJ-4: Convex Hamiltonian

The canonical HJ architecture assumes H(p) is *convex* in the momentum variable p = nabla u. The standard cases:

- **Quadratic:** H(p) = |p|^2 / 2. The *eikonal Hamiltonian* — the simplest convex H.
- **General convex:** H(p) convex, superlinear (H(p) / |p| → infinity as |p| → infinity).
- **Mechanical:** H(p, x) = |p|^2 / 2 + V(x), separating kinetic and potential energy.

Convexity of H is a *structural requirement* for the well-posedness of viscosity solutions: it ensures the comparison principle (unique viscosity solutions exist), the Hopf–Lax formula (explicit representation of solutions), and the connection to optimal control and calculus of variations.

Non-convex Hamiltonians are possible (and arise in some applications) but introduce additional complications (loss of comparison principle in some forms, multiple viscosity solutions, non-uniqueness). The standard HJ architecture assumes convexity.

### Axiom HJ-5: Euclidean Geometry

The equation is formulated on flat Euclidean R^d with the standard gradient. The Hamiltonian H(nabla u) depends on nabla u through the Euclidean norm |nabla u|^2. Extensions to Riemannian manifolds (Hamilton–Jacobi on manifolds) replace the Euclidean gradient with the Riemannian gradient and the norm with the Riemannian norm. The Euclidean restriction is a geometric simplification.

### Axiom HJ-6: Hyperbolic Orientation (Characteristics)

The HJ equation is *hyperbolic* — it propagates information along *characteristics*. The characteristic equations are the Hamilton ODE system:

    dx/dt = nabla_p H(p),    dp/dt = -nabla_x H(p, x)

where p = nabla u along the characteristic. For H(p) = |p|^2/2:

    dx/dt = p = nabla u,    dp/dt = 0

The characteristics are straight lines in the (x, t) plane, traveled at speed nabla u. Information propagates at *finite speed* along these lines — the propagation speed is |nabla_p H(nabla u)|, which is finite for bounded nabla u.

The hyperbolic character is the fundamental structural distinction from all parabolic architectures (AC, CH, PME, TFE, FP): parabolic equations smooth; hyperbolic equations transport. Parabolic equations have infinite propagation speed (for non-degenerate diffusion); hyperbolic equations have finite propagation speed. Parabolic equations gain regularity over time; hyperbolic equations can *lose* regularity (gradient blowup, shock formation).

### Axiom HJ-7: No Diffusion, No Reaction

The HJ equation has no second-order terms (no Delta u, no diffusion) and no zeroth-order terms (no R(u), no reaction). The dynamics are *purely first-order nonlinear transport*:

    partial_t u + H(nabla u) = 0    [no Delta u, no R(u), no f(x,t)]

This is the most radical structural economy in the PDE Atlas (rivaled only by MCF's "no bulk field"): the HJ equation has *only* the nonlinear first-order term. Every other architecture has at least a second-order diffusion term (AC, CH, PME, TFE, FP, RD) or a first-order transport *plus* second-order diffusion (NS, FP).

The absence of diffusion means:
- No smoothing: rough initial data stays rough (or gets rougher).
- No Lyapunov functional (in the parabolic sense): there is no energy that monotonically decreases through a dissipation mechanism.
- No regularization: classical solutions can break down in finite time (gradient blowup).

### Axiom HJ-8: Viscosity-Solution Framework

Because classical (smooth) solutions of the HJ equation can break down in finite time (nabla u develops shocks), the architecture *requires* a weak-solution framework for global well-posedness. The standard framework is the *viscosity solution* theory of Crandall–Lions (1983):

A function u is a *viscosity solution* of partial_t u + H(nabla u) = 0 if:
- At every point where u has a smooth upper tangent (test function touching from above), the equation is satisfied in the <= sense (subsolution condition).
- At every point where u has a smooth lower tangent (test function touching from below), the equation is satisfied in the >= sense (supersolution condition).

The viscosity framework provides:
- **Existence:** Viscosity solutions exist globally in time for all Lipschitz initial data.
- **Uniqueness:** For convex H, the viscosity solution is unique (comparison principle).
- **Stability:** Viscosity solutions are stable under uniform convergence.
- **Connection to vanishing viscosity:** The viscosity solution is the limit of u^epsilon satisfying partial_t u^epsilon + H(nabla u^epsilon) = epsilon Delta u^epsilon as epsilon → 0.

The viscosity-solution framework is not an optional extension — it is a *structural requirement* for the HJ architecture to be well-posed beyond the time of first gradient blowup. Without it, the HJ equation has no global solution theory.

**Comparison with NS:** The NS regularity problem (3D) asks whether smooth solutions exist globally. The HJ gradient-blowup problem is *resolved*: smooth solutions definitely break down, and viscosity solutions provide the unique global continuation. The HJ architecture is more *honest* about its singularities than NS — it acknowledges them and provides a complete framework for continuing past them.

---

## 2. Canonical PDE in Architectural Form

### 2.1 The Hamilton–Jacobi Equation

    partial_t u + H(nabla u) = 0                                    ... (HJ)

For the quadratic Hamiltonian H(p) = |p|^2 / 2:

    partial_t u + (1/2)|nabla u|^2 = 0                              ... (HJ-quad)

### 2.2 The Method of Characteristics

The classical solution is constructed by solving the characteristic ODE:

    dx/dt = nabla_p H(nabla u(x, t))
    du/dt = nabla_p H . nabla u - H(nabla u) = L(nabla_p H, nabla u)

where L(v, p) = p . v - H(p) is the *Lagrangian* (Legendre transform of H). For H(p) = |p|^2/2:

    dx/dt = nabla u(x(0), 0)    [straight line]
    du/dt = |nabla u|^2 / 2      [quadratic growth along characteristic]

The characteristics are straight lines in the (x, t) plane, with slope determined by the initial gradient. When two characteristics cross (which generically happens in finite time for non-trivial initial data), the classical solution becomes multi-valued — this is the *gradient catastrophe*.

### 2.3 The Hopf–Lax Formula

For the quadratic Hamiltonian on R^d, the viscosity solution has the explicit representation:

    u(x, t) = inf_y { u_0(y) + |x - y|^2 / (2t) }               ... (Hopf–Lax)

This is an *infimal convolution* of the initial data u_0 with the quadratic cost |x - y|^2/(2t). The Hopf–Lax formula:
- Gives the viscosity solution directly (no PDE solving required).
- Is a *variational* formula: the solution is the minimum over all "paths" connecting y at time 0 to x at time t.
- Connects HJ to *optimal transport* and *calculus of variations*: u(x, t) is the value function of a control/optimization problem.

### 2.4 Channel-Labeled Decomposition

    partial_t u + H(nabla u) = 0

    =     partial_t u           +        H(nabla u)
    |__________________|    |________________________|
      Time evolution          Nonlinear transport (T)
      (rate of change)        (Hamiltonian acting on gradient)

    producing:
      Gradient steepening → shock formation in nabla u
    |___________________________________________________|
      Steepening channel (S)

    resolved by:
      Viscosity-solution selection
    |______________________________|
      Viscosity channel (V)

### 2.5 Connection to Inviscid Burgers

Differentiating the HJ equation (HJ-quad) with respect to x_i:

    partial_t v_i + v_j partial_j v_i = 0,    v = nabla u

This is the *inviscid Burgers equation* (in d dimensions) for the velocity v = nabla u. The Burgers equation is the *gradient* of the HJ equation — the HJ equation is the *potential form* of Burgers.

Burgers is the simplest model for *shock formation*: smooth initial velocity profiles steepen and form discontinuities (shocks) in finite time. The HJ gradient catastrophe and the Burgers shock are the *same phenomenon* described at different levels (potential vs. velocity).

### 2.6 Boundary and Initial Conditions

**Initial condition:**

    u(x, 0) = u_0(x)

where u_0 is Lipschitz continuous (to ensure that the viscosity solution is well-defined).

**Boundary conditions:** On R^d, no boundary conditions are needed. On bounded domains, various boundary conditions (Dirichlet, state constraint, Neumann) can be imposed, each with its own viscosity-solution theory.

---

## 3. Channel Identification

### Channel T: Transport (First-Order Nonlinear)

    T(u) = H(nabla u)

- **Role:** The sole dynamical mechanism. Transports the potential u along characteristics at speed nabla_p H(nabla u). This is a *nonlinear transport* — the speed depends on the gradient of the solution itself, creating a feedback loop: the gradient determines the speed, and the speed determines how the gradient evolves.
- **Locality:** Local. H(nabla u) depends on nabla u at each point.
- **Linearity:** Nonlinear. H(nabla u) is a nonlinear function of nabla u for non-trivial H. The nonlinearity is first-order (in the gradient), unlike AC/CH (which have nonlinear zeroth-order reaction) or NS (which has nonlinear first-order advection of a vector field).
- **Stability role:** *Destabilizing.* The nonlinear transport steepens gradients rather than smoothing them. Regions where nabla u is large move faster, overtaking regions where nabla u is small, producing gradient concentration and eventually gradient blowup (shock formation). This is the *anti-diffusion* character of HJ: where diffusion smooths gradients, HJ's nonlinear transport steepens them.
- **Scale action:** First-order in k. In Fourier space, the transport rate is proportional to k (wavenumber), not k^2 (as in diffusion). High-frequency modes are amplified at rate k (compared to damping at rate k^2 in parabolic equations). This first-order scaling is *critical*: it is fast enough to produce finite-time blowup of the gradient but slow enough that the solution u itself remains bounded (only nabla u blows up, not u).

### Channel S: Steepening (Gradient Blowup / Shock Formation)

    S: ||nabla u(t)||_{L^infinity} → infinity    as t → T* (shock time)

- **Role:** The structural consequence of the nonlinear transport. The steepening channel is not a separate PDE term — it is an *emergent dynamical feature* of Channel T. When characteristics converge (cross), the gradient of u steepens without bound, producing a *gradient catastrophe* at finite time T*.
- **Locality:** The steepening is local: it occurs at specific points where characteristics converge.
- **Linearity:** Nonlinear (emerges from the nonlinearity of T).
- **Stability role:** Destabilizing. The steepening is the mechanism by which smooth solutions break down. It is the HJ analogue of vortex stretching in NS — a nonlinear amplification mechanism that can drive a regularity-relevant quantity to infinity.
- **Scale action:** Concentrates at the smallest scales. As the gradient steepens, the spatial scale of the gradient profile shrinks toward zero. At the shock time T*, the gradient develops a discontinuity (delta function in the second derivative).

**Comparison with NS vortex stretching:** Both the HJ steepening and the NS vortex stretching are nonlinear amplification mechanisms that can produce singularity in finite time. But the HJ steepening is *resolved* (viscosity solutions continue past the shock) while the NS vortex stretching is *unresolved* (it is unknown whether NS solutions blow up in 3D). HJ is *more honest* about its singularities than NS.

### Channel V: Viscosity (Weak-Solution Selection)

    V: u = viscosity solution (Crandall–Lions framework)

- **Role:** Selects the *unique physically relevant* weak solution after gradient blowup. Among the infinitely many possible weak solutions of the HJ equation (which are not unique in the distributional sense), the viscosity solution is the one selected by the vanishing-viscosity limit:

      u = lim_{epsilon → 0} u^epsilon,    where partial_t u^epsilon + H(nabla u^epsilon) = epsilon Delta u^epsilon

  The viscosity solution is the *regularized limit* — the solution obtained by adding infinitesimal diffusion and then taking it away.

- **Locality:** The viscosity-solution concept is *local* in its definition (comparison with test functions at each point) but *global* in its consequences (the uniqueness and selection principle apply to the entire solution).
- **Linearity:** Nonlinear (the viscosity-solution concept is inherently nonlinear — it involves sup and inf operations, not linear superposition).
- **Stability role:** Stabilizing. The viscosity-solution selection eliminates the non-physical (entropy-violating) weak solutions and selects the unique solution that is consistent with the Second Law of thermodynamics (entropy increase across shocks). This is the HJ analogue of the entropy condition for conservation laws.
- **Scale action:** The viscosity channel operates at the *shock scale* — the infinitesimal scale where the gradient discontinuity forms. It does not affect the smooth parts of the solution.

### Channel Summary Table

| Channel | Symbol | Feature                      | Locality | Linearity   | Stability         | Scale Action        |
|---------|--------|------------------------------|----------|-------------|-------------------|---------------------|
| Transport    | T | H(nabla u) = 0              | Local    | Nonlinear   | Destabilizing     | Rate ~ k (first-order) |
| Steepening   | S | Gradient blowup at T*       | Local    | Nonlinear   | Destabilizing     | Concentrates at small scales |
| Viscosity    | V | Viscosity-solution selection | Local*   | Nonlinear   | Stabilizing (selection) | Operates at shock scale |

*Local in definition; global in consequence.

### Channel Count Comparison

| Architecture | Dynamical | Structural | Selection | Total |
|-------------|-----------|------------|-----------|-------|
| **HJ**      | **1 (T)** | **1 (S)**  | **1 (V)** | **3** |
| MCF         | 1 (K)     | 1 (G)      | 1 (T)     | 3     |
| PME         | 1 (D_nl)  | 1 (C)      | 0         | 3+1   |
| FP          | 2 (T,D)   | 1 (C)      | 0         | 3+1   |
| AC          | 2 (R,S)   | 0           | 0         | 2+2   |

HJ and MCF both have *three channels* — tied for the fewest in the Atlas. But the HJ channels are fundamentally different from MCF's: HJ has a transport channel (first-order, destabilizing), a steepening channel (emergent singularity), and a viscosity channel (selection principle). MCF has a curvature channel (second-order, stabilizing), a geometry channel (no bulk), and a topology channel (structural singularity). The two minimal architectures are structurally orthogonal: HJ is hyperbolic and steepening; MCF is parabolic and smoothing.

---

## 4. Relation to Burgers, NS, FP, AC/CH, PME/TFE, RD, and ED

### 4.1 HJ and Inviscid Burgers

The inviscid Burgers equation is the *gradient* of HJ:

    HJ: partial_t u + (1/2)|nabla u|^2 = 0    [potential]
    Burgers: partial_t v + v . nabla v = 0      [velocity, v = nabla u]

The two equations describe the *same* dynamics at different levels:
- HJ describes the evolution of the potential u (the value function).
- Burgers describes the evolution of the velocity v = nabla u (the gradient of the value function).

Shocks in Burgers (discontinuities in v) correspond to *kinks* in HJ (points where u is continuous but nabla u has a jump discontinuity). The viscosity solution of HJ corresponds to the entropy solution of Burgers.

### 4.2 HJ and Navier–Stokes

The inviscid Burgers equation is the *one-dimensional scalar reduction* of the Euler equations (inviscid NS). The relationship:

    HJ ——[gradient]——> Inviscid Burgers ——[vectorize, add incompressibility + pressure]——> Euler ——[add viscosity]——> NS

Each step adds structural complexity:
- Gradient → velocity: from scalar to vector.
- Add incompressibility + pressure: from compressible to incompressible, adding the nonlocal pressure channel.
- Add viscosity: from hyperbolic to parabolic, adding the diffusion channel.

HJ is the *most reduced* version of the NS architecture — NS stripped of incompressibility, pressure, viscosity, and vector character. What remains is the pure nonlinear transport.

### 4.3 HJ vs. FP: The Hyperbolic-Parabolic Duality

HJ and FP occupy *opposite corners* of the PDE Atlas:

| Feature                    | HJ                       | FP                          |
|----------------------------|--------------------------|-----------------------------|
| Type                       | Hyperbolic (first-order) | Parabolic (second-order)    |
| Smoothing                  | **None** (steepening)    | **Maximum** (Gaussian)      |
| Propagation speed          | Finite (characteristics) | Infinite (heat kernel)      |
| Gradient behavior          | Blowup (shocks)          | Decay (smoothing)           |
| Lyapunov functional        | None (parabolic sense)   | Free energy F (exact)       |
| Well-posedness             | Viscosity solutions      | Classical (linear PDE)      |
| Singularity                | Certain (gradient shock)  | Impossible (linear)         |
| Linearity                  | Nonlinear                | **Linear**                  |
| Equilibrium                | None (dynamics terminate) | Gibbs–Boltzmann (explicit)  |

HJ and FP are *structural duals*: every feature of FP (smoothing, infinite speed, linearity, Lyapunov, no singularity) is *reversed* in HJ (steepening, finite speed, nonlinearity, no Lyapunov, certain singularity). Together, they bracket the range of scalar PDE dynamics: FP is the *most well-behaved* PDE, and HJ is the *most ill-behaved* (in the sense that classical solutions break down).

### 4.4 HJ vs. Parabolic Architectures (AC/CH/PME/TFE)

All parabolic architectures in the Atlas have *diffusion channels* that smooth gradients. HJ has no diffusion and *steepens* gradients. The structural opposition:

| Feature                    | HJ                       | AC/CH/PME/TFE               |
|----------------------------|--------------------------|-----------------------------|
| Highest-order term         | First (H(nabla u))      | Second (Delta u) or fourth  |
| Gradient behavior          | Steepening → blowup     | Smoothing → regularity      |
| Classical regularity       | Finite-time breakdown    | Global (all d <= 3)         |
| Weak solutions needed      | Yes (viscosity)          | Sometimes (Leray–Hopf etc.) |
| Diffusion channel          | **Absent**               | Present (stabilizing)       |
| Lyapunov functional        | None                     | Yes (F, E, H, A)           |

The absence of diffusion is the *single structural feature* that separates HJ from the entire parabolic wing of the Atlas. Adding even infinitesimal diffusion (epsilon Delta u) to HJ produces the *viscous HJ equation*, which is parabolic and globally smooth — the diffusion channel, no matter how weak, prevents gradient blowup. The HJ architecture is what happens when diffusion is set to *exactly zero*.

### 4.5 HJ and Optimal Transport / Calculus of Variations

The Hopf–Lax formula connects HJ to optimal transport:

    u(x, t) = inf_y { u_0(y) + c(x, y, t) }

where c(x, y, t) = |x - y|^2 / (2t) is the *transport cost*. The viscosity solution of HJ is the *value function* of an optimal control problem: u(x, t) is the minimum cost of reaching position x at time t from any starting position y.

This variational interpretation connects HJ to:
- **Optimal transport** (Monge–Kantorovich): the HJ solution describes the optimal assignment of initial to final positions.
- **Calculus of variations** (Euler–Lagrange): the characteristics are the *extremal paths* of the action functional.
- **Classical mechanics** (Hamilton's equations): the characteristic ODEs are Hamilton's equations of motion.
- **Weak KAM theory** (Fathi): the long-time behavior of HJ solutions is governed by *Mather measures* and *Aubry sets* — invariant objects of the Hamiltonian dynamics.

This variational/optimal-transport connection gives HJ a structural depth that no other first-order PDE possesses. The HJ equation is not just a PDE — it is the *interface between PDE theory and variational analysis*.

### 4.6 HJ and ED: Characteristics and Horizons

The HJ characteristics — the straight lines along which information propagates — are the dynamical analogue of the ED *horizons* — the boundaries beyond which the prime structure of the skyline cannot be seen. Both are *propagation boundaries* that separate regions of influence from regions of ignorance. The structural parallel:

- ED: the horizon at prime p divides the integers into those divisible by p (known) and those not yet sieved (unknown). The horizon propagates as the sieve advances.
- HJ: the characteristic from a point (y, 0) traces the region influenced by the initial data at y. When characteristics cross, a *caustic* forms — a singularity boundary analogous to the ED sieve boundary.

### 4.7 Positioning Table

| Feature                    | HJ              | Burgers  | NS       | FP       | AC/CH    | PME/TFE  | RD       | MCF      |
|----------------------------|-----------------|----------|----------|----------|----------|----------|----------|----------|
| PDE type                   | **Hyperbolic**  | Hyperb.  | Mixed    | Parabolic| Parabolic| Parabolic| Parabolic| Parabolic|
| Order                      | **1st**         | 1st      | 2nd      | 2nd      | 2nd/4th  | 2nd/4th  | 2nd      | 2nd      |
| Diffusion                  | **None**        | None     | Viscosity| Linear D | Nonlin.  | Degen.   | Linear D | Curvature|
| Smoothing                  | **None**        | None     | Viscous  | Gaussian | Parabolic| Parabolic| Parabolic| Geometric|
| Gradient behavior          | **Steepening**  | Shock    | Open(3D) | Smoothing| Smoothing| Smoothing| Constitutive| Smoothing|
| Singularity                | **Certain**     | Certain  | Open     | Impossible| Impossible| Impossible*| Constitutive| Certain  |
| Weak solutions             | **Viscosity**   | Entropy  | Leray    | N/A      | N/A      | N/A      | N/A      | Level-set|
| Conservation               | No              | Yes      | Yes      | Yes      | No/Yes   | Yes      | Constitutive| No      |
| Variational                | **Hopf–Lax**   | No       | No       | Wasserstein| L^2/H^{-1}| Wasserstein| Gen. no| Area (L^2)|
| Linearity                  | Nonlinear       | Nonlinear| Nonlinear| **Linear**| Nonlinear| Nonlinear| Nonlinear| Quasilinear|
| Locality                   | Local           | Local    | Nonlocal | Local    | Local    | Local    | Local    | Local    |

*TFE: positivity failure possible for n < 1, but not gradient blowup.

HJ is the *unique hyperbolic, non-diffusive, first-order* architecture in the Atlas. It is the polar opposite of FP (linear, parabolic, maximally smooth) and the reduced ancestor of NS (adding diffusion, incompressibility, pressure, and vector character). HJ demonstrates the *minimum PDE structure* from which transport-driven singularity can emerge.

---

*End of Architectural Specification. The Mode 1 (Axiom → Envelope) analysis will follow in the next file.*
