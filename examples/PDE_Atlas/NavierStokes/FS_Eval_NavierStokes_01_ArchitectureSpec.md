# AD Evaluation: Navier–Stokes Equations — Architectural Specification

Allen Proxmire

April 2026

---

## 1. Implicit Axioms of the Navier–Stokes Architecture

The incompressible Navier–Stokes equations rest on a set of implicit architectural axioms — assumptions that are not derived from deeper principles but are instead *chosen* as the foundation on which the entire dynamical system is erected. Identifying these axioms is the first step in an AD evaluation, because each axiom defines a structural boundary: a point where the architecture commits to a specific representation and forecloses alternatives.

### Axiom NS-1: Continuum Hypothesis

The fluid is modeled as a continuous medium. The velocity field **u**(x, t), pressure field p(x, t), and density field rho(x, t) are assumed to be well-defined at every point x in the domain Omega and at every time t >= 0. This axiom suppresses the molecular discreteness of matter and replaces it with a smooth manifold of field variables. The continuum hypothesis is valid when the Knudsen number Kn = lambda / L (mean free path over characteristic length) satisfies Kn << 1, but the equations carry no internal mechanism for detecting or correcting when this assumption fails.

### Axiom NS-2: Locality

All interactions are local: the time evolution of **u** at a point x depends only on the values of **u**, p, and their spatial derivatives at x (and, through the pressure, on a global constraint — see NS-6). There is no action at a distance in the momentum equation itself. This is a *differential* locality: the architecture encodes physics through PDEs, not integral equations.

### Axiom NS-3: Newtonian Constitutive Law (Linear Stress–Strain)

The deviatoric stress tensor is assumed to be linearly proportional to the rate-of-strain tensor:

    tau_ij = 2 mu S_ij,    S_ij = (1/2)(partial_i u_j + partial_j u_i)

where mu is the dynamic viscosity. This is the *constitutive axiom*: it selects Newtonian fluids from the larger space of possible rheologies (shear-thinning, viscoelastic, Bingham, etc.). The architecture has no mechanism for representing or transitioning to non-Newtonian behavior.

### Axiom NS-4: Isotropy

The fluid response is isotropic: the stress tensor depends on the strain rate tensor through scalar coefficients (mu), not through any preferred direction. This axiom, combined with NS-3, yields the specific form of the viscous term. Anisotropic media (liquid crystals, fiber suspensions, magnetohydrodynamic flows with imposed fields) violate this axiom.

### Axiom NS-5: Conservation Laws

The architecture enforces conservation of mass and conservation of momentum as exact, pointwise identities:

- **Mass conservation:** partial_t rho + div(rho **u**) = 0
- **Momentum conservation:** partial_t(rho **u**) + div(rho **u** (x) **u**) = div(sigma) + **f**

where sigma is the Cauchy stress tensor and **f** is the body force density. These are not approximations; they are the structural skeleton of the system.

### Axiom NS-6: Incompressibility

For the incompressible equations specifically, the density is assumed constant (rho = const), reducing mass conservation to a divergence-free constraint:

    div(**u**) = 0

This is a *kinematic constraint*, not a dynamical equation: it contains no time derivative and must be satisfied instantaneously at every point. This axiom converts the system from hyperbolic (compressible) to a mixed parabolic-elliptic type and introduces the pressure Poisson equation as the enforcement mechanism.

### Axiom NS-7: Smooth Forcing

External forces **f**(x, t) are assumed to be given smooth (or at least sufficiently regular) functions. The architecture does not self-generate forcing; it receives it as an external input channel.

### Axiom NS-8: Euclidean Ambient Space

The equations are formulated on flat Euclidean space R^d (d = 2, 3) or on domains Omega subset R^d with prescribed boundary conditions. The metric is flat. Curvature effects (flows on manifolds, general-relativistic fluids) are outside the architecture.

---

## 2. Canonical Navier–Stokes PDE in Architectural Form

We write the incompressible Navier–Stokes equations in their standard architectural form, with each structural channel explicitly labeled.

### 2.1 Momentum Equation

For incompressible flow with constant density rho (normalized to rho = 1 without loss of generality):

    partial_t **u** + (**u** . nabla)**u** = -nabla p + nu Delta **u** + **f**

where:
- **u**(x, t) : R^d x [0, T) -> R^d is the velocity field
- p(x, t) : R^d x [0, T) -> R is the kinematic pressure (pressure divided by density)
- nu = mu / rho > 0 is the kinematic viscosity
- **f**(x, t) is the external body force per unit mass
- Delta = nabla^2 is the Laplacian

### 2.2 Incompressibility Constraint

    div(**u**) = nabla . **u** = 0

This constraint holds for all (x, t) in the domain. It is not an evolution equation — it is a *structural constraint* that the velocity field must satisfy at every instant.

### 2.3 Pressure Projection

Taking the divergence of the momentum equation and applying the incompressibility constraint yields the pressure Poisson equation:

    Delta p = -div((**u** . nabla)**u**) + div(**f**)
            = -partial_i partial_j (u_i u_j) + div(**f**)

The pressure is *not* an independent thermodynamic variable in the incompressible system. It is a Lagrange multiplier enforcing the divergence-free constraint. The pressure Poisson equation is an *elliptic* equation — its solution at any point depends on the entire domain instantaneously. This is the single nonlocal channel in the otherwise local architecture.

### 2.4 Helmholtz–Leray Decomposition

The momentum equation can be rewritten in projection form using the Leray projector P (projection onto divergence-free fields):

    partial_t **u** = P[-(**u** . nabla)**u** + nu Delta **u** + **f**]

This form makes explicit that the time evolution lives entirely in the divergence-free subspace. The Leray projector P absorbs both the pressure gradient and the incompressibility constraint into a single operator.

### 2.5 Initial and Boundary Conditions

    **u**(x, 0) = **u**_0(x),    div(**u**_0) = 0
    Boundary conditions: **u** = 0 on partial Omega (no-slip), or periodic, or decay at infinity

The initial data must itself satisfy the divergence-free constraint — the architecture is not self-correcting on this point.

---

## 3. Structural Channels of Navier–Stokes

The Navier–Stokes architecture routes information through five identifiable structural channels. Each channel has a distinct mathematical character, a distinct physical role, and a distinct scaling behavior.

### Channel 1: Advection (Nonlinear Transport)

    A(**u**) = (**u** . nabla)**u**

- **Type:** Quadratic nonlinearity, hyperbolic character
- **Role:** Transports momentum along the flow itself. This is the self-interaction of the velocity field — the mechanism by which the fluid carries its own velocity.
- **Key property:** Energy-conserving in the L^2 sense (for divergence-free fields, the advection term redistributes energy across scales without creating or destroying it).
- **Scaling:** If **u** ~ U and length ~ L, then A ~ U^2 / L.
- **Structural character:** This is the sole nonlinear channel. It is responsible for turbulence, energy cascade, vortex stretching (in 3D), and the formation of small scales. It is the source of all analytical difficulty in the Navier–Stokes regularity problem.

### Channel 2: Diffusion / Viscosity

    D(**u**) = nu Delta **u**

- **Type:** Linear, parabolic (second-order elliptic in space)
- **Role:** Smooths the velocity field by dissipating kinetic energy into heat. The viscous term acts as a low-pass filter, preferentially damping high-frequency (small-scale) components of **u**.
- **Key property:** Monotonically decreases the L^2 norm of velocity (energy dissipation): d/dt ||**u**||^2 <= -2 nu ||nabla **u**||^2 (in the absence of forcing).
- **Scaling:** D ~ nu U / L^2. The ratio of advection to diffusion defines the Reynolds number: Re = UL / nu.
- **Structural character:** This is the regularizing channel. It provides the parabolic smoothing that, in 2D, is sufficient to guarantee global regularity. In 3D, the question is whether this channel is strong enough to control the advection channel at all times.

### Channel 3: Pressure Projection

    Pi(**u**) = -nabla p,    where Delta p = -partial_i partial_j (u_i u_j)

- **Type:** Nonlocal, elliptic, instantaneous
- **Role:** Enforces the incompressibility constraint by redistributing momentum to keep the velocity field divergence-free. Pressure acts as the Lagrange multiplier for the constraint div(**u**) = 0.
- **Key property:** The pressure gradient is the *unique* gradient field that, when added to the unconstrained momentum tendency, produces a divergence-free result. It carries no energy of its own — it mediates constraint enforcement, not dynamics.
- **Scaling:** nabla p ~ U^2 / L (balances advection at leading order).
- **Structural character:** This is the *nonlocal* channel. The solution of the Poisson equation couples every point in the domain to every other point, instantaneously. This is the mechanism by which a local disturbance in velocity is felt globally through pressure adjustment.

### Channel 4: External Forcing

    F(**u**) = **f**(x, t)

- **Type:** Prescribed, external
- **Role:** Injects energy and momentum into the system from outside the architecture. In physical applications, **f** represents gravity, electromagnetic forces, boundary-driven flow, or stochastic stirring.
- **Key property:** The forcing channel is the only channel that can inject energy; without it, the system is purely dissipative and all solutions decay to rest.
- **Scaling:** Problem-dependent; f ~ F_0 (characteristic forcing amplitude).
- **Structural character:** This is the *input* channel. The architecture does not generate its own dynamics — it transforms the input provided by forcing and initial conditions.

### Channel 5: Incompressibility Constraint

    C(**u**) : div(**u**) = 0

- **Type:** Algebraic (not differential in time), holonomic constraint
- **Role:** Restricts the velocity field to the submanifold of divergence-free vector fields at every instant. This is the kinematic backbone of the incompressible architecture.
- **Key property:** The constraint is *maintained*, not *enforced dynamically*. If the initial data satisfies div(**u**_0) = 0 and the evolution is exact, the constraint is preserved for all time. In numerical discretizations, constraint drift can occur and must be corrected (pressure projection methods, divergence cleaning).
- **Structural character:** This is the *constraint* channel. It is not a force or a flux — it is a structural restriction on the space of admissible states. It converts the system from an unconstrained PDE on R^d-valued fields to a constrained evolution on a submanifold.

### Summary Table

| Channel           | Term                          | Type                | Character           |
|-------------------|-------------------------------|---------------------|---------------------|
| Advection         | (u . nabla)u                  | Quadratic nonlinear | Hyperbolic, local   |
| Diffusion         | nu Delta u                    | Linear              | Parabolic, local    |
| Pressure          | -nabla p                      | Nonlocal            | Elliptic, global    |
| Forcing           | f(x,t)                        | Prescribed          | External input      |
| Incompressibility | div(u) = 0                    | Algebraic           | Holonomic constraint|

---

## 4. Comparison with Event Density (ED) Architecture

The Navier–Stokes architecture and the Event Density architecture occupy fundamentally different positions in the space of mathematical structures. This section identifies the key architectural divergences.

### 4.1 Discrete vs. Continuous Domain

The Factor Skyline and its ED extension operate on the *integers* — a discrete, countable domain. Each integer n is a distinct structural object with a unique factorization, and the FS primitives (width, height, activation, coverage, escape) act on these discrete objects. The Navier–Stokes equations operate on *continuous fields* over R^d. The domain is uncountable, the state space is infinite-dimensional (a function space), and the dynamics are governed by PDEs, not combinatorial identities. This is the most fundamental architectural difference: ED is combinatorial-geometric; NS is analytic-geometric.

### 4.2 Algebraic vs. Dynamical

The FS/ED architecture is *static-algebraic*: the integers do not evolve in time. The structure of the skyline is determined once and for all by the multiplicative structure of Z. The FS primitives describe *what is*, not *what happens*. Navier–Stokes is *dynamical*: the velocity field evolves under a nonlinear PDE. The architecture describes a *process* — the time evolution of a physical state — not a fixed configuration. Time is a structural variable in NS; it plays no role in ED.

### 4.3 Nonlinearity

The FS/ED architecture is *linear* in the sense that its primitives (width, height, activation) are defined by factorization, which composes multiplicatively but does not involve feedback or self-interaction. The Navier–Stokes architecture contains a *quadratic nonlinearity* — the advection term (u . nabla)u — in which the velocity field acts on itself. This self-referential structure is the source of turbulence, energy cascade, and the analytical difficulty of the regularity problem. ED has no analogous mechanism.

### 4.4 Conservation Structure

Both architectures enforce conservation laws, but of different kinds. In ED/FS, the Chebyshev conservation law (sum of log p / p = log x + O(1)) is an *asymptotic accounting identity* for how prime mass distributes across the skyline. In NS, conservation of mass and momentum are *exact pointwise identities* holding at every instant — they are the structural skeleton from which the PDE is derived.

### 4.5 Constraint vs. Freedom

The incompressibility constraint div(u) = 0 has no direct analogue in ED. The FS architecture imposes constraints through factorization (every integer has a unique factorization), but these are *algebraic identities*, not differential constraints. The incompressibility constraint is a *field-level restriction* on an infinite-dimensional state space, enforced by a nonlocal elliptic equation (the pressure Poisson equation). This introduces a qualitatively different kind of structural coupling — pressure-mediated nonlocality — that has no counterpart in the AD framework.

### 4.6 Regularity Question

The central open problem for NS (in 3D) is *regularity*: does a smooth solution remain smooth for all time, or can singularities form in finite time? This question is intrinsically dynamical and has no analogue in ED, where the objects (integers, prime factorizations) are exactly defined and never blow up. The AD evaluation of NS will therefore encounter a fundamentally different kind of structural question: not "what does the architecture describe?" but "does the architecture remain self-consistent under its own dynamics?"

---

*End of Architectural Specification. The FS criteria evaluation (structural channels, EXPBD triad, failure modes) will follow in subsequent files.*
