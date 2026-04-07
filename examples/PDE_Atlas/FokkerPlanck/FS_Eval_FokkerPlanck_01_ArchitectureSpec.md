# AD Evaluation: Fokker–Planck Equation — Architectural Specification

Allen Proxmire

April 2026

---

## 1. Implicit Axioms of the Fokker–Planck Architecture

The Fokker–Planck (FP) equation describes the time evolution of a probability density rho(x, t) under the combined action of deterministic drift and stochastic diffusion. It is the *deterministic PDE* that governs the probability distribution of a stochastic process described by a stochastic differential equation (SDE). The FP equation is the canonical architecture for probability-density evolution — the PDE of statistical mechanics, Brownian motion, stochastic control, and kinetic theory.

The FP equation occupies a unique position in the PDE Atlas: it is the *only* architecture whose state variable is intrinsically a probability density (rho >= 0, integral rho = 1), the *only* architecture with a first-order drift channel coupled to second-order diffusion, and the *only* architecture that is the deterministic shadow of a stochastic process. It is the "stochastic corner" of the PDE Atlas — the point where the deterministic PDE framework makes contact with probability theory.

### Axiom FP-1: Continuum Hypothesis (Probability Density)

The system is modeled by a scalar probability density field rho(x, t) >= 0 defined at every point x in a domain Omega subset R^d (d >= 1) and every time t >= 0. The field rho represents the probability density of finding a particle (or an ensemble of particles) at position x at time t. The integral integral rho dx gives the probability of the particle being in a region, and the total probability integral_Omega rho dx = 1 is normalized.

This axiom is a *probabilistic continuum hypothesis*: it replaces the discrete random walk of individual particles with a smooth density field. It is valid when the number of particles (or the ensemble) is large enough for the density to be well-defined, and when the underlying stochastic process has a smooth transition kernel.

### Axiom FP-2: Locality

All interactions are local: the time evolution of rho at x depends only on rho, nabla rho, and Delta rho at x, plus the prescribed drift field b(x) and diffusion tensor D(x) evaluated at x. There are no nonlocal operators, no integral constraints requiring a global solve, and no pressure-type enforcement mechanisms. The FP equation is *fully local* at both formulation and solution levels — the same locality class as AC, CH, PME, TFE, and RD.

### Axiom FP-3: Drift–Diffusion Decomposition

The evolution of rho is decomposed into two structural contributions:

1. **Drift (first-order transport):** -div(b rho) = -b . nabla rho - (div b) rho. The drift field b(x) transports rho along its integral curves. This is a *first-order* (advective) contribution that moves probability without spreading it.

2. **Diffusion (second-order smoothing):** div(D nabla rho) = D_{ij} partial_i partial_j rho + (partial_i D_{ij}) partial_j rho. The diffusion tensor D(x) spreads rho, smoothing concentration gradients. This is a *second-order* (parabolic) contribution that smears probability.

The drift–diffusion decomposition is the defining structural feature of the FP architecture: two channels of different order (first and second) acting simultaneously on the same density field. This is qualitatively different from all previously evaluated architectures:

- AC, CH, PME, TFE: pure diffusion (no first-order drift).
- NS: has advection (first-order) but it is *nonlinear* (u . nabla u, self-advection). FP's drift is *linear* (b . nabla rho, advection by a prescribed external field).
- RD: has reaction (zeroth-order) + diffusion. FP has drift (first-order) + diffusion, with no reaction.

### Axiom FP-4: Conservation of Total Probability (Mass Conservation)

The total probability is exactly conserved:

    d/dt integral_Omega rho(x, t) dx = 0

This follows from the divergence form of the FP equation:

    partial_t rho = -div(b rho) + div(D nabla rho) = -div(b rho - D nabla rho)

with no-flux boundary conditions (b rho - D nabla rho) . n = 0 on partial Omega. The FP equation is a *continuity equation* — it conserves total probability by construction.

Conservation of probability is the FP analogue of mass conservation in PME, CH, and TFE. But there is a stronger constraint: the total probability is normalized to 1 (not to an arbitrary mass M). This normalization is a *structural commitment* specific to the probabilistic interpretation.

### Axiom FP-5: Euclidean Geometry

The equation is formulated on flat Euclidean R^d or bounded domains Omega subset R^d with the standard Laplacian and gradient. The same geometric commitment as all previous evaluations.

### Axiom FP-6: Forward Parabolic Orientation

The FP equation evolves forward in time: it describes how the probability density at time t = 0 evolves to later times t > 0. The backward version (the *backward Kolmogorov equation* or *adjoint FP equation*) is a different PDE with a different interpretation (expected values of functions of the terminal state). The forward orientation is the natural one for tracking the evolution of an initial probability distribution.

### Axiom FP-7: No Reaction Term

The FP equation has no source/sink terms — it is *probability-preserving*. No probability is created or destroyed; it is only transported (by drift) and spread (by diffusion). This is analogous to PME-7 and TFE-7 (no reaction), but with the specific probabilistic motivation that creation/destruction of probability would violate the axioms of probability theory.

Formally, one can add source/sink terms to produce a *Fokker–Planck equation with creation and annihilation* (used in birth-death processes, chemical master equations, etc.), but this extends the architecture beyond the standard FP.

### Axiom FP-8: Constitutive Drift and Diffusion Fields

The drift field b : R^d → R^d and diffusion tensor D : R^d → R^{d x d} are prescribed *external* fields — they do not depend on rho. This is the *linear* FP equation: rho enters linearly in the PDE. The drift and diffusion are structural parameters of the environment through which the particle moves, not properties of the density itself.

Key sub-cases:
- **Gradient drift:** b(x) = -nabla V(x) for some potential V. This produces the *gradient FP equation*, which has an explicit equilibrium (the Gibbs–Boltzmann distribution) and a gradient-flow structure (Wasserstein gradient flow of the free energy).
- **Non-gradient drift:** b is not the gradient of any potential. The dynamics may have no equilibrium, no Lyapunov functional, and non-trivial long-time behavior (limit cycles in the drift flow → rotating probability densities).
- **Constant diffusion:** D = sigma^2 I (isotropic, spatially uniform). The simplest case.
- **Spatially varying diffusion:** D = D(x), possibly anisotropic. Produces inhomogeneous spreading.
- **Degenerate diffusion:** D with rank < d at some points. Produces hypoelliptic behavior.

The constitutive fields (b, D) play the same role as the reaction kinetics R(u) in the RD class: they parameterize the FP architecture, selecting specific dynamics from the general class.

---

## 2. Canonical PDE in Architectural Form

### 2.1 The Fokker–Planck Equation

    partial_t rho = -div(b rho) + div(D nabla rho)                      ... (FP-I)

Equivalently, in terms of the *probability flux* **J**:

    partial_t rho = -div(**J**),    **J** = b rho - D nabla rho           ... (FP-flux)

The flux has two contributions:
- **Drift flux:** b rho (transports rho along b).
- **Diffusive flux:** -D nabla rho (spreads rho down the concentration gradient).

### 2.2 Expanded Form (Constant D = sigma^2 I)

For constant isotropic diffusion:

    partial_t rho = -b . nabla rho - (div b) rho + sigma^2 Delta rho     ... (FP-const)

This is a *linear second-order parabolic PDE* with variable coefficients (b(x) enters the first-order and zeroth-order terms).

### 2.3 Channel-Labeled Decomposition

    partial_t rho =    -div(b rho)         +       div(D nabla rho)
                   |___________________|    |________________________|
                     Drift channel (T)        Diffusion channel (D)

    subject to:   rho >= 0,    integral rho dx = 1
                 |_________|   |___________________|
                  Positivity    Conservation (C)

    when b = -nabla V:
                   Gradient-flow structure (P)
                 |_________________________________|
                   Wasserstein gradient flow of F[rho]

### 2.4 The Gradient-Flow Sub-Architecture (b = -nabla V)

When the drift is the negative gradient of a potential V(x), the FP equation becomes:

    partial_t rho = div(rho nabla V) + div(D nabla rho) = div(rho (nabla V + D nabla log rho))

For D = sigma^2 I, this can be written as:

    partial_t rho = div(rho nabla (V + sigma^2 log rho))

This is the Wasserstein gradient flow of the *free energy*:

    F[rho] = integral rho V dx + sigma^2 integral rho log rho dx = <V>_rho + sigma^2 H[rho]

where H[rho] = integral rho log rho dx is the Boltzmann entropy (negative Shannon entropy). The free energy combines potential energy (<V>_rho) with entropic energy (sigma^2 H[rho]).

The unique stationary solution (equilibrium) is the *Gibbs–Boltzmann distribution*:

    rho_eq(x) = Z^{-1} exp(-V(x) / sigma^2)

where Z = integral exp(-V/sigma^2) dx is the partition function. This is the *global minimizer* of F[rho] subject to integral rho = 1, and the *universal attractor* of the gradient FP dynamics.

The dissipation identity:

    dF/dt = -integral rho |nabla(V + sigma^2 log rho)|^2 / sigma^2 dx <= 0

This is the FP analogue of the AC/CH/PME Lyapunov identities. It is exact, strictly negative except at equilibrium, and has finite total budget.

### 2.5 Boundary and Initial Conditions

**Initial condition:**

    rho(x, 0) = rho_0(x) >= 0,    integral rho_0 dx = 1

**Boundary conditions:**
- **No-flux (reflecting):** **J** . n = (b rho - D nabla rho) . n = 0 on partial Omega. Preserves total probability.
- **Absorbing:** rho = 0 on partial Omega. Probability is absorbed at the boundary (total probability decreases — extends beyond FP-7).
- **Periodic:** rho(x + L) = rho(x).
- **On R^d:** rho → 0 as |x| → infinity (decay at infinity).

### 2.6 Connection to Stochastic Differential Equations

The FP equation is the *deterministic shadow* of the SDE:

    dX_t = b(X_t) dt + sigma(X_t) dW_t

where W_t is a d-dimensional Brownian motion and D = (1/2) sigma sigma^T. The probability density rho(x, t) of X_t satisfies the FP equation (FP-I). Every SDE has a corresponding FP equation, and every FP equation corresponds to a family of SDEs (differing in the choice of sigma given D).

This SDE–FP correspondence is the structural bridge between the stochastic and deterministic frameworks. The FP equation is the *mean-field limit* of the stochastic process: it describes the average behavior of an ensemble of particles, each following the SDE independently.

---

## 3. Channel Identification

### Channel T: Transport (First-Order Drift)

    T(rho) = -div(b rho) = -b . nabla rho - (div b) rho

- **Role:** Transports probability along the drift field b. In the SDE interpretation, the drift is the deterministic part of the particle motion — the "expected velocity" at each point. The transport channel moves probability without spreading it: if D = 0, the FP equation reduces to the continuity equation partial_t rho + div(b rho) = 0, and rho is transported along the characteristics of b.
- **Locality:** Local. Depends on rho, nabla rho, and the prescribed field b(x) at each point.
- **Linearity:** Linear in rho (for prescribed b). The drift field b does not depend on rho — it is an external field.
- **Stability role:** *Depends on the drift structure:*
  - **Gradient drift** (b = -nabla V with V convex): stabilizing. The drift pushes rho toward the minimum of V, concentrating probability near the potential well.
  - **Divergence-free drift** (div b = 0): neutral. The drift preserves the L^2 norm of rho (volume-preserving transport). It rotates probability without concentrating or spreading it.
  - **Expanding drift** (div b > 0): destabilizing (locally). The drift dilutes rho.
  - **General drift:** mixed — may be stabilizing in some regions and destabilizing in others.
- **Scale action:** First-order in spatial derivatives. The transport rate is |b| / L at spatial scale L. Transport is scale-independent in the sense that it moves features at speed |b| regardless of their size — unlike diffusion, which is scale-dependent (rate ~ D/L^2).

### Channel D: Diffusion (Second-Order Smoothing)

    D(rho) = div(D nabla rho)

- **Role:** Spreads probability, smoothing concentration gradients. In the SDE interpretation, diffusion is the stochastic part — the random fluctuations (Brownian motion) that spread the particle's position.
- **Locality:** Local. Depends on rho, nabla rho, Delta rho, and the prescribed tensor D(x) at each point.
- **Linearity:** Linear in rho (for prescribed D).
- **Stability role:** Stabilizing (for positive definite D). The diffusion channel damps all non-constant modes, spreading probability uniformly. It is the *entropic* channel: it increases the entropy H[rho] = integral rho log rho dx (making it less negative, i.e., more disordered).
- **Scale action:** Second-order. Damping rate ~ D k^2 at wavenumber k. Small-scale features are smoothed fastest. The diffusion time scale is t_D ~ L^2 / D — the same as the linear heat equation and the non-degenerate RD class.

### Channel C: Conservation (Probability Preservation)

    C: integral rho(x, t) dx = 1    for all t >= 0

- **Role:** Structural constraint. The total probability is exactly 1 at all times. This is the *normalization* constraint of probability theory — more specific than the mass conservation of PME/CH/TFE (where the total mass can be any positive number M).
- **Locality:** Global constraint, locally enforced through the divergence form of the PDE.
- **Linearity:** Linear.
- **Stability role:** Constraining. The dynamics are confined to the *probability simplex* — the infinite-dimensional set of non-negative functions with unit integral.

### Channel P: Potential / Gradient-Flow Structure (b = -nabla V)

    P: F[rho] = integral rho V dx + sigma^2 integral rho log rho dx,    dF/dt <= 0

- **Role:** When the drift is a gradient field (b = -nabla V), the FP equation acquires a gradient-flow structure in the Wasserstein metric. The free energy F[rho] = <V>_rho + sigma^2 H[rho] is a Lyapunov functional. The dynamics descend the free-energy landscape toward the Gibbs–Boltzmann equilibrium.
- **Locality:** The free energy is a *global* functional, but the dynamics are local (the PDE is local).
- **Linearity:** The gradient-flow structure is *nonlinear* in rho (through the entropy term rho log rho), even though the PDE is linear.
- **Stability role:** Stabilizing (when present). The gradient-flow structure ensures monotone free-energy decay and convergence to the unique Gibbs–Boltzmann equilibrium.

**Key distinction:** Channel P exists *only for gradient drifts* (b = -nabla V). For non-gradient drifts, there is no Lyapunov functional, and the dynamics may exhibit more complex long-time behavior (rotating probability densities, non-convergent dynamics).

### Channel Summary Table

| Channel | Symbol | Term                    | Role                      | Locality | Linearity | Stability          | Scale Action    |
|---------|--------|-------------------------|---------------------------|----------|-----------|--------------------|-----------------|
| Transport   | T  | -div(b rho)            | Drift along b             | Local    | Linear    | b-dependent        | Rate ~ \|b\|/L |
| Diffusion   | D  | div(D nabla rho)       | Smoothing                 | Local    | Linear    | Stabilizing        | Rate ~ D k^2   |
| Conservation| C  | integral rho = 1       | Probability preservation  | Global*  | Linear    | Constraining       | All-scale       |
| Potential   | P  | F[rho], dF/dt <= 0    | Gradient flow (b=-nabla V)| Global** | Nonlinear | Stabilizing        | All-scale       |

*Enforced locally through divergence form.
**F is a global functional; the PDE is local.

---

## 4. Relation to AC, CH, PME, RD, NS, and ED

### 4.1 The Stochastic Corner of the PDE Atlas

The FP equation occupies a unique position: it is the *only* PDE in the PDE Atlas that is the deterministic description of a stochastic process. Every other architecture describes a deterministic physical system (fluid flow, phase separation, thin films, nonlinear diffusion). The FP equation describes a *probability* — the statistical behavior of an ensemble of stochastic particles.

This stochastic origin gives FP several features that no other architecture possesses:

- **Linearity:** The FP equation is *linear* in rho (for prescribed b and D). This makes it the only linear PDE in the Atlas (all others — NS, AC, CH, PME, TFE, RD — have nonlinear terms). The linearity arises because the evolution of a probability density under a linear (Markov) stochastic process is itself linear.

- **Probabilistic normalization:** The total integral is normalized to 1 (probability), not just conserved at an arbitrary value M (mass). This is a stronger structural constraint.

- **Drift + diffusion:** The combination of first-order transport and second-order diffusion is unique to FP. AC, CH, PME, and TFE have only diffusion (no drift). NS has advection, but it is nonlinear self-advection; FP has linear advection by an external prescribed field. RD has reaction + diffusion; FP has drift + diffusion.

### 4.2 FP vs. the Gradient-Flow Architectures

| Feature                    | AC            | CH            | PME           | TFE           | FP (b=-nabla V) |
|----------------------------|---------------|---------------|---------------|---------------|------------------|
| Conservation               | No            | Yes           | Yes           | Yes           | Yes (integral=1) |
| Gradient-flow metric       | L^2           | H^{-1}       | Wasserstein   | Weighted H^{-1}| Wasserstein     |
| PDE order                  | 2nd           | 4th           | 2nd (degen.)  | 4th (degen.)  | 2nd (non-degen.)|
| Drift channel              | No            | No            | No            | No            | **Yes** (first-order) |
| Reaction channel           | Yes (phi-phi^3)| Yes (via mu) | No            | No            | No               |
| Linearity                  | Nonlinear     | Nonlinear     | Nonlinear     | Nonlinear     | **Linear**       |
| Equilibrium                | phi = ±1      | Phase-sep.    | Barenblatt    | Flat film     | Gibbs–Boltzmann  |
| Free energy                | Ginzburg-Landau| Ginzburg-Landau| Entropy     | Surface energy| V + sigma^2 H   |

The gradient FP equation (b = -nabla V) is the *Wasserstein gradient flow* of the free energy F = <V> + sigma^2 H. This places it in the same structural class as the PME (which is also a Wasserstein gradient flow — of the Renyi entropy). The two architectures share the Wasserstein metric but differ in the functional being minimized: PME minimizes a purely entropic functional; FP minimizes a combined potential + entropic functional.

### 4.3 FP vs. NS

| Feature                    | Fokker–Planck         | Navier–Stokes              |
|----------------------------|-----------------------|----------------------------|
| State variable             | Scalar density rho    | Vector velocity **u**      |
| Linearity                  | Linear                | Nonlinear (advection)      |
| Drift / advection          | Linear (b rho)        | Nonlinear (u . nabla u)    |
| Diffusion                  | Linear (D Delta rho)  | Linear (nu Delta u)        |
| Conservation               | Probability (integral=1)| Mass + momentum           |
| Incompressibility          | No                    | Yes (div u = 0)            |
| Nonlocal channel           | No                    | Yes (pressure)             |
| Stochastic interpretation  | Yes (SDE)             | No (deterministic)         |

The deepest structural difference: NS advection is *self-advection* (the velocity field transports itself), producing the quadratic nonlinearity that drives turbulence. FP advection is *external advection* (the prescribed drift transports the density), keeping the equation linear. This linearity is the structural reason FP is analytically tractable — and why it has no turbulence analogue.

### 4.4 FP vs. RD

| Feature                    | Fokker–Planck         | Reaction–Diffusion          |
|----------------------------|-----------------------|-----------------------------|
| Drift channel              | Yes (first-order)     | No (except via spatial bias)|
| Reaction channel           | No                    | Yes (R(u))                  |
| Linearity                  | Linear                | Nonlinear (via R)           |
| Species                    | 1 (probability density)| n >= 1                     |
| Oscillations               | No (linear, monotone) | Permitted (nonlinear R)     |
| Patterns                   | No                    | Permitted (Turing)          |
| Chaos                      | No (for gradient drift)| Permitted                  |
| Lyapunov (gradient drift)  | Yes (free energy F)   | Generically no              |

FP and RD occupy complementary positions in the PDE Atlas: FP has drift but no reaction; RD has reaction but no drift (in the standard form). FP is linear; RD is nonlinear. FP preserves probability; RD can create/destroy mass. FP cannot pattern-form; RD can. The two architectures have *disjoint* dynamical repertoires beyond shared diffusive smoothing.

### 4.5 FP and ED: The Probability-Density Connection

The FP equation connects to the Event Density concept from the AD framework through the *density interpretation*: both ED and FP describe how a density (of events, of probability) distributes across a space. ED distributes prime-event density across the integer skyline; FP distributes probability density across Euclidean space. The structural analogy:

- ED: a static density on a discrete domain (Z), governed by arithmetic.
- FP: a dynamic density on a continuous domain (R^d), governed by drift + diffusion.

Both are *density architectures* — they describe how "stuff" (events, probability) is distributed. The FP equation is the *dynamical, continuous, stochastic* version of the density concept that ED embodies statically and arithmetically.

### 4.6 Positioning Table

| Feature                    | FP            | AC    | CH    | PME   | TFE   | NS    | RD          |
|----------------------------|---------------|-------|-------|-------|-------|-------|-------------|
| State variable             | Prob. density | Order param. | Order param. | Density | Film height | Velocity | Concentration |
| Linearity                  | **Linear**    | Nonlin.| Nonlin.| Nonlin.| Nonlin.| Nonlin.| Nonlin.    |
| Drift channel              | **Yes**       | No    | No    | No    | No    | Self-adv. | No       |
| Diffusion order            | 2nd           | 2nd   | 4th   | 2nd   | 4th   | 2nd   | 2nd         |
| Conservation               | Yes (=1)      | No    | Yes   | Yes   | Yes   | Yes   | Constitutive|
| Gradient-flow (b=-nabla V) | Wasserstein   | L^2   | H^{-1}| Wass. | Wt. H^{-1} | No | Gen. no |
| Equilibrium (gradient)     | Gibbs–Boltz.  | ±1    | Phase-sep. | Barenblatt | Flat film | — | Constitutive |
| Stochastic origin          | **SDE**       | No    | No    | No    | No    | No    | No          |
| Oscillations (non-gradient)| Possible*     | No    | No    | No    | No    | Yes   | Yes         |
| Blowup                     | No            | No    | No    | No    | n-dep.| 3D open| Constitutive|
| Locality                   | Fully local   | Local | Local | Local | Local | Nonlocal | Local    |

*For non-gradient drift, the probability density can rotate around a limit cycle of the drift flow, but this is linear rotation, not nonlinear oscillation.

---

*End of Architectural Specification. The Mode 1 (Axiom → Envelope) analysis will follow in the next file.*
