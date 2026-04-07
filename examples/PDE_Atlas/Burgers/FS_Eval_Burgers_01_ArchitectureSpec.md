# AD Evaluation: Inviscid Burgers Equation — Architectural Specification

Allen Proxmire

April 2026

---

## 1. Implicit Axioms of the Inviscid Burgers Architecture

The inviscid Burgers equation describes the evolution of a scalar velocity field v(x, t) under its own nonlinear self-advection. It is the *simplest nonlinear conservation law* — the minimal PDE in which a scalar field transports itself, producing shock waves from smooth initial data. Burgers occupies a precise structural position in the PDE Atlas: it is the *derivative of Hamilton–Jacobi* (v = partial_x u where u satisfies HJ), the *scalar ancestor of the Euler equations* (NS without viscosity, pressure, or incompressibility), and the *canonical model for shock formation* in hyperbolic conservation laws.

Where HJ evolves a *potential* u whose gradient steepens and develops kinks, Burgers evolves the *gradient itself* — the velocity v = nabla u — which steepens and develops *discontinuities* (shocks). The relationship is exact: every HJ gradient catastrophe corresponds to a Burgers shock, and every Burgers entropy solution corresponds to an HJ viscosity solution. The two architectures are *structurally dual* — related by a single derivative — and share the same closure mechanism (convexity + entropy/viscosity), the same singularity structure (certain finite-time blowup), and the same parameter-free character.

The Burgers equation adds one structural feature that HJ lacks: the *conservation-law structure*. Burgers is not just a first-order nonlinear PDE — it is a *conservation law* with a specific flux function f(v) = v^2/2. The conservation structure provides additional tools (Rankine–Hugoniot jump conditions, Oleinik entropy condition, L^1 contraction) that go beyond the HJ viscosity framework. Burgers is HJ *plus conservation*.

### Axiom BA-1: Field Hypothesis (Scalar Velocity)

The state variable is a scalar velocity field v(x, t) defined on R x [0, T) (primarily in one spatial dimension, though multi-dimensional extensions exist). Unlike HJ, where the state is a *potential* (an auxiliary quantity whose gradient is physical), the Burgers state v is *directly physical* — it represents velocity, speed, or a conserved density. The field v is the primary object; no gradient or potential is needed for the physical interpretation.

### Axiom BA-2: Locality

All interactions are local: the time evolution of v at x depends only on v(x, t) and partial_x v(x, t) at the same point. There are no nonlocal operators, no integral constraints, and no pressure-type coupling. The Burgers equation is *fully local* at the formulation level — the same locality class as HJ, AC, CH, PME, TFE, FP, MCF, and RD.

### Axiom BA-3: First-Order Nonlinear Conservation Law

The evolution is governed by a first-order conservation law:

    partial_t v + partial_x f(v) = 0

with flux function f(v) = v^2/2, giving:

    partial_t v + v partial_x v = 0                              ... (Burgers)

The equation is simultaneously:
- A *conservation law*: partial_t v + partial_x(v^2/2) = 0. The quantity v is conserved in integral form: d/dt integral v dx = 0 (for compactly supported solutions or appropriate boundary conditions).
- A *self-advection equation*: v transports itself at speed v. The velocity field is its own carrier — a nonlinear feedback loop in which the transported quantity determines its own transport speed.

The conservation-law structure is the *defining feature* that distinguishes Burgers from HJ. HJ (partial_t u + H(nabla u) = 0) is *not* a conservation law — it does not have the form partial_t u + partial_x(something) = 0 (because H(nabla u) is not the x-derivative of anything in general). Burgers inherits the conservation-law structure from being the *derivative* of HJ: differentiating partial_t u + (1/2)(partial_x u)^2 = 0 with respect to x and setting v = partial_x u gives partial_t v + v partial_x v = 0 = partial_t v + partial_x(v^2/2).

### Axiom BA-4: Convex Flux

The flux function f(v) = v^2/2 is *strictly convex*: f''(v) = 1 > 0. Convexity of the flux is the structural requirement for:
- Uniqueness of entropy solutions.
- The Oleinik entropy condition (one-sided slope bound).
- The L^1 contraction property.
- The connection to HJ via the Hopf–Lax formula.

Non-convex fluxes (e.g., the Buckley–Leverett flux f(v) = v^2/(v^2 + (1-v)^2)) produce qualitatively different shock structures (compound waves, undercompressive shocks) and require more refined entropy conditions. The convex-flux assumption is the Burgers analogue of HJ's convex-Hamiltonian assumption (HJ-4) — and indeed, f(v) = v^2/2 *is* the Legendre transform of H(p) = p^2/2.

### Axiom BA-5: Hyperbolic Orientation

The Burgers equation is *hyperbolic*: information propagates along *characteristics* at speed v. The characteristic equations are:

    dx/dt = v(x(t), t),    dv/dt = 0

Each characteristic carries a constant value of v, traveling at speed v. Fast regions (v large) outrun slow regions (v small), leading to characteristic crossing and shock formation.

The hyperbolic character is inherited from HJ: Burgers is the gradient of the HJ equation, and the gradient of a hyperbolic equation is hyperbolic. The propagation speed is *finite* (bounded by ||v_0||_{L^infinity}), and the domain of dependence is a cone — the same structural features as HJ.

### Axiom BA-6: No Diffusion

The inviscid Burgers equation has no second-order term — no viscosity, no diffusion, no smoothing:

    partial_t v + v partial_x v = 0    [no nu partial_x^2 v]

Adding viscosity gives the *viscous Burgers equation* partial_t v + v partial_x v = nu partial_{xx} v, which is parabolic, globally smooth, and has no shocks. The inviscid limit (nu → 0) produces the inviscid Burgers equation — with its shocks — as the limiting architecture.

The absence of diffusion is the structural commitment that produces shocks: without smoothing, the gradient steepening has no counterbalance, and discontinuities form in finite time. This is the same structural commitment as HJ-7 (no diffusion in HJ).

### Axiom BA-7: No Reaction

No source or sink terms. The equation is a *pure conservation law*: the only mechanism is nonlinear self-advection. Mass (integral v dx) is conserved. No creation, destruction, or external forcing.

### Axiom BA-8: Entropy/Viscosity-Solution Framework

Because classical solutions break down at shock time (v develops discontinuities), the architecture requires a weak-solution framework for global well-posedness. The standard framework is the *entropy solution* (Kruzkov, 1970):

A bounded measurable function v is an *entropy solution* if for every convex entropy eta(v) with entropy flux q(v) satisfying q'(v) = eta'(v) f'(v):

    partial_t eta(v) + partial_x q(v) <= 0    (in the distributional sense)

The entropy condition selects the unique physically admissible weak solution — the one obtained as the limit of vanishing-viscosity approximations: v = lim_{nu → 0} v^nu where partial_t v^nu + v^nu partial_x v^nu = nu partial_{xx} v^nu.

For the convex flux f(v) = v^2/2, the entropy solution satisfies:
- **Oleinik condition:** partial_x v <= 1/t (the one-sided slope bound — same as HJ's Oleinik bound).
- **Rankine–Hugoniot condition:** At a shock with left state v_L and right state v_R, the shock speed is s = (v_L + v_R)/2 = (f(v_L) - f(v_R))/(v_L - v_R).
- **Lax entropy condition:** v_L > s > v_R (characteristics enter the shock from both sides).

The entropy-solution framework is the Burgers analogue of HJ's viscosity-solution framework (HJ-8). Indeed, the two are *exactly equivalent*: v is an entropy solution of Burgers if and only if u = integral v dx is a viscosity solution of HJ. The two frameworks are related by a derivative.

---

## 2. Canonical PDE in Architectural Form

### 2.1 The Inviscid Burgers Equation

**Conservation form:**

    partial_t v + partial_x(v^2/2) = 0                            ... (BA-cons)

**Non-conservative (advective) form:**

    partial_t v + v partial_x v = 0                                ... (BA-adv)

The two forms are equivalent for smooth solutions but differ for discontinuous (shock) solutions. The *conservation form* is the correct weak formulation: it specifies the Rankine–Hugoniot jump condition at shocks. The advective form is undefined at shocks (v partial_x v is not defined when v is discontinuous).

### 2.2 Method of Characteristics

The characteristic equations:

    dx/dt = v,    dv/dt = 0

give straight-line characteristics x(t) = x_0 + v_0 t with v constant along each line:

    v(x_0 + v_0 t, t) = v_0 = v(x_0, 0)

The characteristics are *labeled* by their initial position x_0 and carry the initial velocity v_0 = v_0(x_0). When two characteristics with different velocities cross (which happens when v_0 is decreasing: v_0(x_1) > v_0(x_2) for x_1 < x_2), the classical solution becomes multi-valued → a *shock* forms.

### 2.3 Shock Formation

The shock time is:

    T* = -1 / min_x (partial_x v_0(x))    [minimum of the initial slope]

If v_0 has a region of negative slope (decreasing velocity), characteristics converge and a shock forms at time T*. The shock is a *discontinuity in v*: v jumps from v_L (left state) to v_R (right state) with v_L > v_R (the Lax entropy condition).

**Comparison with HJ:** The HJ shock time is T* = 1/max(-u_0''). Since v_0 = u_0', we have partial_x v_0 = u_0'', so min(partial_x v_0) = min(u_0'') = -max(-u_0''). Thus T*_Burgers = -1/min(v_0') = 1/max(-u_0'') = T*_HJ. The two equations develop singularities at the *same time* — confirming their duality.

### 2.4 Channel-Labeled Decomposition

    partial_t v + v partial_x v = 0

    =     partial_t v           +        v partial_x v
    |__________________|    |________________________|
      Time evolution          Self-advection (Transport T)

    producing:
      Gradient steepening → shock formation
    |___________________________________________________|
      Steepening channel (S)

    resolved by:
      Entropy-solution selection (Kruzkov)
    |______________________________________________|
      Entropy/Viscosity channel (V)

### 2.5 The Hopf–Cole–Lax Connection

For v = partial_x u where u satisfies HJ with H(p) = p^2/2:

    v(x, t) = (x - y*(x,t)) / t

where y*(x, t) = argmin_y { u_0(y) + |x-y|^2/(2t) } is the optimal point in the Hopf–Lax formula. The entropy solution of Burgers is obtained by *differentiating* the viscosity solution of HJ.

For the viscous case, the Cole–Hopf transform v = -2 nu partial_x(log phi) linearizes the viscous Burgers equation to the heat equation partial_t phi = nu partial_{xx} phi, providing an *exact analytical solution*.

---

## 3. Channel Identification

### Channel T: Transport (Self-Advection)

    T(v) = v partial_x v = partial_x(v^2/2)

- **Role:** The sole dynamical mechanism. The velocity field v advects itself: each "particle" of fluid moves at speed v, carrying its own velocity. This *self-referential transport* is the source of all dynamics — the velocity determines the speed, and the speed changes the velocity distribution by rearranging it spatially.
- **Locality:** Local. v partial_x v depends on v and partial_x v at each point.
- **Linearity:** Nonlinear. The product v partial_x v is quadratic in v. This is the same nonlinear self-advection as in the Euler/NS equations (u . nabla u), reduced to the scalar 1D case.
- **Stability role:** Destabilizing. Self-advection steepens the velocity profile: fast regions (large v) outrun slow regions (small v), compressing the profile and eventually forming a discontinuity. This is the *scalar analogue of vortex stretching* in NS — a nonlinear amplification mechanism that drives singularity formation.
- **Scale action:** First-order in k. The advection rate is proportional to v k (the velocity times the wavenumber). High-k modes are amplified faster than low-k modes — the gradient steepens at all scales simultaneously, but the smallest-scale steepening is fastest.

### Channel S: Steepening (Shock Formation)

    S: partial_x v → -infinity    at x = x_shock as t → T*

- **Role:** Emergent consequence of Channel T. The velocity gradient steepens without bound, forming a *shock* — a genuine discontinuity in v. The shock is a *dissipative structure* in the entropy sense: kinetic energy is lost at the shock (converted to "heat" in the vanishing-viscosity interpretation).
- **Locality:** Local trigger (the shock forms at a specific point). Global consequence (the shock propagates and interacts with other features).
- **Linearity:** Nonlinear.
- **Stability role:** Destabilizing (produces loss of smoothness). But *self-limiting*: the shock, once formed, *reduces* the total variation of v (shocks are compressive, bringing v_L and v_R closer together over time). The steepening phase is destabilizing; the post-shock phase is stabilizing.
- **Scale action:** Concentrates at scale zero. The shock is a *delta function* in the gradient: partial_x v has a singularity of the form v_L - v_R at the shock location. The steepening creates structure at the smallest possible scale (a point discontinuity).

### Channel V: Entropy/Viscosity (Solution Selection)

    V: v = entropy solution (Kruzkov framework)

- **Role:** Selects the unique physically admissible weak solution. The entropy condition ensures that:
  - Shocks are *compressive* (v_L > v_R) — characteristics enter the shock, not leave it.
  - Kinetic energy is *dissipated* at shocks — energy decreases across discontinuities.
  - The solution is the *vanishing-viscosity limit* — the physically relevant weak solution.
- **Locality:** Locally defined (entropy inequalities at each point) but globally consequent (uniqueness of the solution on the entire domain).
- **Linearity:** Nonlinear.
- **Stability role:** Stabilizing (in the selection sense). The entropy condition + L^1 contraction provide a complete well-posedness theory past shocks.
- **Scale action:** Operates at the shock scale (the infinitesimal width of the discontinuity).

### Channel Summary Table

| Channel | Symbol | Feature                       | Locality | Linearity   | Stability            | Scale Action           |
|---------|--------|-------------------------------|----------|-------------|----------------------|------------------------|
| Transport    | T | v partial_x v (self-advection)| Local    | Nonlinear   | Destabilizing        | Rate ~ v k (1st-order) |
| Steepening   | S | partial_x v → -infinity       | Local*   | Nonlinear   | Destab. → self-limiting | Concentrates at k → ∞ |
| Entropy      | V | Entropy-solution selection    | Local**  | Nonlinear   | Stabilizing (selection)| At shock scale         |

*Local trigger, global consequence. **Locally defined, globally consequent.

### Structural Comparison: Burgers vs. HJ

| Feature                    | Burgers                      | Hamilton–Jacobi              |
|----------------------------|------------------------------|------------------------------|
| State variable             | Velocity v                   | Potential u                  |
| Relationship               | v = partial_x u              | u = integral v dx            |
| PDE                        | partial_t v + v v_x = 0      | partial_t u + (u_x)^2/2 = 0 |
| Conservation law?          | **Yes** (partial_t v + partial_x(v^2/2) = 0) | No      |
| Singularity type           | v discontinuous (shock)      | nabla u discontinuous (kink) |
| Weak solution              | Entropy solution (Kruzkov)   | Viscosity solution (C-L)     |
| Contraction                | **L^1 contraction**          | L^{infinity} contraction     |
| Mass conservation          | **Yes** (integral v = const) | No                           |
| Energy dissipation at shock| **Yes** (irreversible)       | N/A (no energy concept)      |

The key structural additions of Burgers over HJ:
1. **Conservation-law structure:** Burgers has partial_t v + partial_x(v^2/2) = 0 → Rankine–Hugoniot jump conditions, shock speed formula, and the connection to fluid mechanics.
2. **L^1 contraction:** ||v_1(t) - v_2(t)||_{L^1} <= ||v_{1,0} - v_{2,0}||_{L^1} (Kruzkov). HJ has L^{infinity} contraction; Burgers has *both* L^1 and L^{infinity}.
3. **Mass conservation:** integral v dx = const. HJ has no conservation law.
4. **Energy dissipation at shocks:** The kinetic energy integral v^2/2 dx *decreases* across shocks (irreversible dissipation). HJ has no energy concept.

---

## 4. Relation to HJ, NS, FP, AC/CH, PME/TFE, MCF, and ED

### 4.1 Burgers as the Derivative of HJ

The exact relationship:

    v = partial_x u    where    partial_t u + (1/2)(partial_x u)^2 = 0    (HJ)

Differentiating HJ with respect to x:

    partial_t v + v partial_x v = 0    (Burgers)

Every HJ viscosity solution u produces a Burgers entropy solution v = partial_x u. Conversely, every Burgers entropy solution v produces an HJ viscosity solution u = integral v dx (up to a constant). The two architectures are *exactly dual* — one derivative apart.

This duality means:
- HJ kinks (nabla u discontinuous) = Burgers shocks (v discontinuous).
- HJ semiconcavity (D^2 u <= C/t) = Burgers Oleinik condition (v_x <= 1/t).
- HJ Hopf–Lax formula = Burgers Lax–Oleinik formula.
- HJ L^{infinity} contraction = Burgers L^{infinity} contraction.
- Burgers L^1 contraction *has no HJ analogue* (this is the structural addition).

### 4.2 Burgers as the Scalar Ancestor of Euler/NS

The inviscid Burgers equation is the *one-dimensional scalar* reduction of the Euler equations:

    Burgers (1D scalar):  partial_t v + v partial_x v = 0
    Euler (dD vector):    partial_t **u** + (**u** . nabla)**u** = -nabla p,  div **u** = 0

The passage from Burgers to Euler adds:
- *Vector character:* **u** in R^d instead of v in R.
- *Incompressibility:* div **u** = 0 (a constraint, not a dynamical equation).
- *Pressure:* -nabla p (the nonlocal Lagrange multiplier enforcing incompressibility).

These three additions transform the *completely understood* Burgers equation into the *largely unresolved* Euler/NS equations. The Burgers evaluation isolates the nonlinear self-advection mechanism — the one feature shared by Burgers and NS — and shows that self-advection alone is *completely tractable*. The difficulty of NS lies not in self-advection but in the *interaction of self-advection with incompressibility and pressure*.

Adding viscosity to Burgers gives the *viscous Burgers equation*:

    partial_t v + v partial_x v = nu partial_{xx} v

which is *exactly solvable* (via the Cole–Hopf transform) and globally smooth. Adding viscosity to Euler gives Navier–Stokes, which is *not* exactly solvable and has an open regularity problem in 3D. The contrast reveals that viscosity + scalar self-advection = tractable, while viscosity + vector self-advection + incompressibility + pressure = intractable (in 3D).

### 4.3 Burgers vs. FP: Conservation Law vs. Probability

Burgers and FP are both *scalar evolution equations*, but with opposite structural characters:

| Feature                    | Burgers                     | Fokker–Planck              |
|----------------------------|-----------------------------|----------------------------|
| PDE type                   | Hyperbolic (1st-order)      | Parabolic (2nd-order)      |
| Nonlinearity               | Quadratic self-advection    | None (linear)              |
| Diffusion                  | None                        | Linear (D Delta rho)       |
| Conservation               | Mass (integral v = const)   | Probability (integral rho = 1) |
| Singularity                | Certain (shocks)            | Impossible                 |
| Contraction                | L^1 + L^{infinity}          | Wasserstein + L^2          |
| Solution type              | Entropy (Kruzkov)           | Classical                  |
| Long-time limit            | N-wave decay                | Gibbs–Boltzmann            |

Burgers and FP are *conservation-law duals*: Burgers conserves mass through a nonlinear flux; FP conserves probability through a linear flux. Burgers develops shocks (information loss at discontinuities); FP develops equilibria (information loss through entropy production). Both lose information over time, but through opposite mechanisms.

### 4.4 Burgers vs. Diffusive Architectures

| Feature                    | Burgers           | AC/CH/PME/TFE        |
|----------------------------|--------------------|----------------------|
| Smoothing                  | None               | Yes (various orders) |
| Gradient behavior          | Steepening → shock | Smoothing → regularity |
| Conservation               | Yes (integral v)   | Variable             |
| Lyapunov functional        | No (energy decreases only at shocks) | Yes (F, E, H) |
| Singularity                | Certain (shock)    | None (global smooth) |
| Attractor                  | Self-similar N-wave| Barenblatt/flat/phase-sep. |

The diffusive architectures prevent shocks through smoothing. Burgers has no smoothing and develops shocks as a structural necessity. The architectures are *structurally complementary*: Burgers models the nonlinear transport that diffusion counteracts.

### 4.5 Burgers and ED: Characteristic Horizons

The Burgers characteristics — straight lines in (x, t) carrying constant velocity — define *characteristic horizons*: the boundaries of the domain of dependence for each spacetime point. These horizons are the dynamical analogue of the ED *sieve horizons* — the boundaries beyond which the prime structure is not yet revealed. Both define *information boundaries* that partition spacetime into known and unknown regions.

At a Burgers shock, characteristics converge and *information is destroyed* — the pre-shock state cannot be recovered from the post-shock state (irreversibility). At an ED sieve horizon, coverage eliminates composite integers and *information is lost* — the specific factorization of eliminated integers is absorbed into the sieve. Both are *one-way information boundaries*.

### 4.6 Positioning Table

| Feature                    | Burgers       | HJ         | NS         | FP        | AC/CH     | PME/TFE   | MCF       | RD        |
|----------------------------|-------------|------------|------------|-----------|-----------|-----------|-----------|-----------|
| PDE type                   | **Hyperbolic**| Hyperbolic | Mixed      | Parabolic | Parabolic | Parabolic | Parabolic | Parabolic |
| State variable             | **Velocity v**| Potential u| Velocity **u**| Density rho| Order param.| Density/height| Surface| Concentration|
| Conservation law           | **Yes**     | No         | Yes (mass+mom)| Yes (prob.)| Variable | Yes       | No        | Constitutive|
| Self-advection             | **v v_x**   | H(u_x)    | **u.nabla u**| b.nabla rho| No      | No        | No        | No        |
| Diffusion                  | **None**    | None       | nu Delta u | D Delta rho| Various  | Various   | Curvature | Various   |
| Shock formation            | **Certain** | Certain    | Open (3D)  | Impossible| Impossible| Impossible*| Certain  | Constitutive|
| L^1 contraction            | **Yes**     | No         | No         | No        | No        | **Yes** (PME)| No    | No        |
| L^{infinity} contraction   | **Yes**     | **Yes**    | No         | No        | No        | No        | No        | No        |
| Conservation of mass       | **Yes**     | No         | Yes        | Yes       | Variable  | Yes       | No        | Constitutive|
| Energy dissipation at shock| **Yes**     | No         | Open       | N/A       | N/A       | N/A       | N/A       | N/A       |
| Parameters                 | **0**       | **0**      | 2          | 2         | 3         | 1         | **0**     | Many      |
| Relation to HJ             | **Derivative**| Identity  | Generalization| No    | Sharp-int.limit of AC| No | Sharp-int.limit of AC| No |

*TFE: positivity failure possible for n < 1, not gradient blowup.

Burgers is the *unique conservation-law, self-advecting, shock-forming, mass-conserving, L^1-contracting* architecture in the Atlas. It is the derivative of HJ, the scalar ancestor of NS, and the simplest model for the phenomenon of shock formation in nonlinear wave propagation.

---

*End of Architectural Specification. The Mode 1 (Axiom → Envelope) analysis will follow in the next file.*
