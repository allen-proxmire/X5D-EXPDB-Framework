# AD Evaluation: Reaction–Diffusion Systems — Architectural Specification

Allen Proxmire

April 2026

---

## 1. Implicit Axioms of the Reaction–Diffusion Architecture

A reaction–diffusion (RD) system models the spatiotemporal evolution of one or more concentration fields through the interplay of local reactions (creation, destruction, transformation) and spatial diffusion (spreading). RD systems are the broadest class of second-order parabolic PDEs with local nonlinearities — the universality class for pattern formation, traveling waves, fronts, and spatially organized structure in chemistry, biology, ecology, and materials science.

Unlike the previous AD evaluations (NS, CH, AC), which analyzed *specific* PDEs with fixed constitutive forms, the RD evaluation targets an *architectural class* — the family of all systems of the form partial_t **u** = **D** Delta **u** + **R**(**u**). The axioms therefore specify the structural commitments shared by all members of the class, not the constitutive details of any particular member.

### Axiom RD-1: Continuum Hypothesis

The system is modeled as a collection of continuous scalar fields **u**(x, t) = (u_1(x, t), ..., u_n(x, t)), where each u_i represents the concentration (or activity, or density) of the i-th species. The fields are defined at every point x in a domain Omega subset R^d (d = 1, 2, 3) and every time t >= 0. The molecular discreteness of matter is suppressed. This is the same commitment as in NS, CH, and AC: the continuum hypothesis is the entry ticket to the PDE paradigm.

### Axiom RD-2: Locality

All interactions are local: the time derivative partial_t u_i at point x depends only on **u**(x, t), nabla **u**(x, t), and Delta **u**(x, t) at the same point x. There is no action at a distance, no integral operators, and no nonlocal constraints. The RD architecture is *fully local* at both the formulation and solution levels — the same locality class as AC and CH, and stronger locality than NS (which has the nonlocal pressure channel).

RD-2 is the most restrictive structural axiom after the continuum hypothesis: it confines the architecture to differential operators and algebraic nonlinearities, excluding integral equations (Boltzmann), fractional diffusion, and nonlocal reaction terms.

### Axiom RD-3: Diffusion Structure

Each species diffuses in space through a second-order elliptic operator. The canonical form is:

    (Diffusion)_i = sum_j D_{ij} Delta u_j

where **D** = (D_{ij}) is the *diffusion matrix*. The diffusion structure may be:

- **Diagonal:** D_{ij} = d_i delta_{ij}. Each species diffuses independently. This is the standard case.
- **Coupled (cross-diffusion):** D_{ij} ≠ 0 for i ≠ j. The diffusion of species i depends on the gradient of species j. Cross-diffusion can produce qualitatively new phenomena (e.g., pattern formation even without Turing-type reaction instabilities).
- **Nonlinear:** D_{ij} = D_{ij}(**u**). The diffusion coefficients depend on the concentrations. This includes porous-medium-type diffusion (D ~ u^m), degenerate diffusion (D → 0 as u → 0), and density-dependent diffusion.
- **Scalar (single species):** n = 1, D is a positive scalar. This is the AC case with appropriate reaction terms.

The diffusion matrix must satisfy an *ellipticity condition* to ensure well-posedness: D must be positive semi-definite (for degenerate systems) or positive definite (for uniformly parabolic systems). Negative diffusion coefficients produce ill-posed (backward-heat-type) equations and are outside the standard RD architecture.

### Axiom RD-4: Reaction Terms

Each species has a local reaction term R_i(**u**) that depends only on the concentrations **u** = (u_1, ..., u_n) at each point — no spatial derivatives:

    (Reaction)_i = R_i(u_1, ..., u_n)

The reaction terms encode:
- **Growth and decay:** R_i > 0 produces species i; R_i < 0 consumes it.
- **Coupling:** R_i depends on u_j (j ≠ i), encoding interactions between species (activation, inhibition, predation, cooperation).
- **Nonlinearity:** R_i is typically a nonlinear function of **u** — polynomial, rational, saturating, or threshold-type. The nonlinearity is the source of the rich pattern-forming behavior of RD systems.

The reaction terms are *local* (no derivatives of **u**) and *algebraic* (determined at each point by the current concentrations). They are the RD analogue of the double-well reaction in AC, but far more general: there is no requirement that R derive from a free-energy functional, no gradient-flow constraint, and no variational structure.

**Key distinction from AC/CH:** In AC, the reaction term R(phi) = phi - phi^3 is the negative gradient of a double-well potential, and the entire dynamics are a gradient flow of F. In general RD, the reaction **R**(**u**) is *arbitrary* — it need not be a gradient of any functional. This means:

- General RD systems may lack a Lyapunov functional.
- General RD systems may exhibit limit cycles, chaos, and sustained oscillations.
- General RD systems are *not* thermodynamically constrained.

### Axiom RD-5: Euclidean Geometry

The equations are formulated on flat Euclidean R^d or on bounded domains Omega subset R^d with the standard Laplacian. The same geometric commitment as in NS, CH, and AC.

### Axiom RD-6: Boundary Conditions

The system is equipped with boundary conditions on partial Omega that are *local* — they involve **u** and its normal derivative at boundary points, not global integrals or nonlocal constraints. Standard choices:

- **Neumann (no-flux):** nabla u_i . n = 0. No material enters or leaves through the boundary. This is the natural condition for closed systems and the most common in biological/chemical applications.
- **Dirichlet:** u_i = g_i on partial Omega. Prescribed concentration at the boundary. Used for reservoirs or externally maintained conditions.
- **Periodic:** u_i(x + L) = u_i(x). The domain is a torus.
- **Robin (mixed):** alpha u_i + beta nabla u_i . n = gamma. Linear combination of Dirichlet and Neumann.

The boundary conditions are part of the architecture — they shape the solution space and can qualitatively change the dynamics (e.g., Neumann boundary conditions permit spatially non-uniform steady states that Dirichlet conditions may forbid).

### Axiom RD-7: Time Orientation (Forward Parabolic Evolution)

The system evolves *forward* in time under a parabolic (dissipative) structure. The diffusion operator provides second-order smoothing that makes the equation well-posed in the forward direction and ill-posed in the backward direction. This is a structural commitment to irreversibility: the RD architecture has a preferred time direction determined by the sign of the diffusion coefficients.

Time-reversal (D → -D) produces a backward heat equation, which is catastrophically ill-posed. The RD architecture is *irreversible by construction* — it distinguishes past from future through the parabolic structure.

### Axiom RD-8: Constitutive Choices

The specific reaction kinetics R_i(**u**) and diffusion coefficients D_{ij} are *constitutive selections* — chosen to model a particular physical, chemical, or biological system. The RD architecture does not specify these; it specifies only the *form* of the equations (partial_t **u** = **D** Delta **u** + **R**(**u**)). The constitutive choices determine:

- The number of species n.
- The specific nonlinearities in **R**.
- The diffusion rates in **D**.
- Whether the system has conservation laws, Lyapunov functionals, maximum principles, or none of these.

This axiom makes explicit that the RD architecture is a *class*, not a single system. The AD evaluation targets the structural properties shared by *all* members of the class, with specific constitutive choices treated as parameters that select particular sub-architectures.

---

## 2. Canonical PDE in Architectural Form

### 2.1 General Vector-Valued System

The canonical RD system for n species on a domain Omega subset R^d:

    partial_t u_i = sum_j D_{ij} Delta u_j + R_i(u_1, ..., u_n),    i = 1, ..., n    ... (RD-I)

In vector notation:

    partial_t **u** = **D** Delta **u** + **R**(**u**)                                    ... (RD-II)

where **u** : Omega x [0, T) → R^n, **D** is an n x n diffusion matrix, and **R** : R^n → R^n is the reaction vector.

### 2.2 Scalar Case (n = 1)

    partial_t u = D Delta u + R(u)                                                         ... (RD-III)

This includes:
- **Allen–Cahn:** D = M epsilon^2, R(u) = M(u - u^3). Gradient flow of a double-well free energy.
- **Fisher–KPP:** D = d, R(u) = r u(1 - u). Logistic growth + diffusion.
- **Nagumo / Bistable:** D = d, R(u) = u(1 - u)(u - a). Bistable reaction.
- **Heat equation:** D = d, R = 0. Pure diffusion, no reaction.

### 2.3 Two-Species Systems (n = 2)

    partial_t u = D_u Delta u + f(u, v)
    partial_t v = D_v Delta v + g(u, v)                                                     ... (RD-IV)

Classical examples:
- **FitzHugh–Nagumo:** f(u,v) = u - u^3 - v, g(u,v) = epsilon(u - gamma v). Excitable dynamics, traveling pulses.
- **Turing (activator–inhibitor):** f = a u - b v + nonlinear, g = c u - d v + nonlinear, with D_v >> D_u. Pattern formation via diffusion-driven instability.
- **Lotka–Volterra:** f = u(alpha - beta v), g = v(-gamma + delta u). Predator-prey oscillations.
- **Brusselator:** f = A - (B+1)u + u^2 v, g = Bu - u^2 v. Chemical oscillations.
- **Gray–Scott:** f = -uv^2 + F(1-u), g = uv^2 - (F+k)v. Self-replicating spots.

### 2.4 Channel-Labeled Decomposition

    partial_t **u** =    **D** Delta **u**    +    **R**(**u**)
                     |___________________|    |_______________|
                       Diffusion channel        Reaction channel
                       (Channel D)               (Channel R)

For cross-diffusion systems, the diffusion channel decomposes further:

    **D** Delta **u** =    diag(D_{ii}) Delta **u**    +    off-diag(D_{ij}) Delta **u**
                        |_________________________|    |______________________________|
                          Self-diffusion                 Cross-diffusion
                          (Channel D_self)                (Channel D_cross)

For multi-species reactions, the reaction channel decomposes:

    R_i(**u**) =    R_i(u_i)    +    [R_i(**u**) - R_i(u_i)]
                |____________|    |___________________________|
                 Self-reaction      Cross-reaction (coupling)
                 (Channel R_self)    (Channel R_cross)

### 2.5 Boundary and Initial Conditions

    **u**(x, 0) = **u**_0(x)
    Boundary conditions on partial Omega (species-by-species, local)

No constraint on initial data (unlike NS, which requires div(**u**_0) = 0, or CH, which implicitly requires finite F[phi_0]). Any sufficiently regular **u**_0 with u_i >= 0 (for concentration fields) is admissible.

---

## 3. Channel Identification

The RD architecture routes dynamics through four structural channels.

### Channel D: Diffusion (Smoothing)

    D(**u**) = **D** Delta **u**

- **Role:** Spreads each species spatially, smoothing concentration gradients. The diffusion channel is the regularizing mechanism of the RD architecture — it provides second-order parabolic smoothing that prevents infinitely sharp features and ensures (under appropriate conditions) that solutions remain smooth.
- **Locality:** Local. The Laplacian Delta u_i involves second spatial derivatives at each point.
- **Linearity:** Linear (for constant D) or weakly nonlinear (for concentration-dependent D(**u**)). The diffusion channel is the linear backbone of the RD architecture.
- **Stability role:** Stabilizing (for positive definite D). The Laplacian damps all non-constant modes, with damping rate D k^2 in Fourier space. The diffusion channel suppresses short-wavelength perturbations and is the architecture's primary smoothing mechanism.
- **Scaling:** Damping rate ~ D / L^2 at spatial scale L. Small-scale features are damped fastest. The diffusion time scale is t_D ~ L^2 / D.

**Subtlety — Turing instability:** Even though the diffusion channel is stabilizing for each species individually, the *combination* of diffusion with reaction coupling can be destabilizing. In a two-species system with D_v >> D_u, the fast diffusion of the inhibitor v can outpace the slow diffusion of the activator u, destabilizing a homogeneous state that would be stable without diffusion. This is the Turing mechanism: *diffusion-driven instability*. The instability is not in the diffusion channel alone but in the *interaction* of diffusion rates with reaction coupling.

### Channel R: Reaction (Local Nonlinearity)

    R(**u**) = (R_1(**u**), ..., R_n(**u**))

- **Role:** The reaction channel encodes all local, non-spatial interactions: growth, decay, transformation, activation, inhibition, cooperation, competition. It is the source of all qualitative complexity in RD dynamics — oscillations, excitability, bistability, multistability, chaos — because it is the only nonlinear channel.
- **Locality:** Local. R_i depends only on **u** at each point — no spatial derivatives.
- **Linearity:** Nonlinear (generically). The reaction terms are typically polynomial, rational, or piecewise functions of **u**. This is the sole nonlinear channel in the standard RD architecture.
- **Stability role:** *Depends on the specific kinetics.* The reaction channel can be:
  - Stabilizing (convergent to a fixed point): e.g., R(u) = -u (exponential decay).
  - Destabilizing (divergent from a fixed point): e.g., R(u) = u (exponential growth).
  - Bistable (two stable fixed points): e.g., R(u) = u(1-u)(u-a) (Nagumo).
  - Oscillatory (limit cycles in the ODE): e.g., FitzHugh–Nagumo, Brusselator.
  - Excitable (threshold-mediated firing): e.g., FitzHugh–Nagumo near the rest state.
  - Chaotic (sensitive dependence in the ODE): e.g., three-species systems with appropriate kinetics.

  The stability character of R is a *constitutive property* determined by the specific kinetics, not an architectural property of the RD class.

- **Scaling:** Scale-free. The reaction terms do not involve spatial derivatives, so they operate at the same rate regardless of spatial scale. The reaction time scale is t_R ~ 1 / ||R'||, determined by the Jacobian of R at the operating point.

### Channel C: Coupling (Cross-Diffusion and Cross-Reaction)

    C(**u**) = off-diagonal diffusion + cross-species reaction terms

- **Role:** Mediates interactions between species. Cross-reaction (R_i depends on u_j) couples the species dynamically. Cross-diffusion (D_{ij} ≠ 0 for i ≠ j) couples them spatially. The coupling channel is responsible for all multi-species phenomena: Turing patterns, predator-prey waves, chemical oscillations, and excitable media.
- **Locality:** Local. Both cross-reaction and cross-diffusion are local operators.
- **Linearity:** Cross-diffusion is linear (for constant D); cross-reaction is nonlinear (generically).
- **Stability role:** The coupling channel is the source of *emergent instabilities* — instabilities that are absent in each species alone but arise from the interaction. The Turing instability is the paradigmatic example: neither activator nor inhibitor is unstable alone, but their coupling through diffusion and reaction produces spatial pattern formation.
- **Scaling:** Cross-reaction is scale-free (like self-reaction). Cross-diffusion scales as D / L^2 (like self-diffusion). The *ratio* of diffusion coefficients D_v / D_u is the key parameter for Turing instability — it must exceed a threshold determined by the reaction kinetics.

### Channel M: Rate Scales (Mobility / Kinetic Parameters)

    M: the diffusion coefficients D_i, reaction rate constants, time-scale ratios

- **Role:** Sets the absolute and relative rates of diffusion and reaction. The rate scales determine which channel dominates at each spatial and temporal scale, and whether the system is in a diffusion-dominated, reaction-dominated, or balanced regime.
- **Locality:** N/A (parameters, not spatial operators).
- **Linearity:** N/A (parameters).
- **Stability role:** The rate scales determine the *architecture of instabilities*: the Turing instability requires D_v / D_u > threshold; excitable dynamics require epsilon << 1 (time-scale separation); oscillatory patterns require specific parameter ranges. The rate scales do not change the qualitative architecture (the form of the PDE) but they select which dynamical behaviors are realized.
- **Scaling:** Sets the fundamental time scales t_D = L^2 / D and t_R = 1 / ||R'||. The ratio t_D / t_R = D / (L^2 ||R'||) determines whether the system is diffusion-limited (t_D >> t_R) or reaction-limited (t_R >> t_D).

### Channel Summary Table

| Channel | Symbol | Term                       | Role                        | Locality | Linearity      | Stability          | Scaling                |
|---------|--------|----------------------------|-----------------------------|----------|----------------|--------------------|-----------------------|
| Diffusion   | D  | **D** Delta **u**         | Smoothing                   | Local    | Linear*        | Stabilizing        | Rate ~ D/L^2          |
| Reaction    | R  | **R**(**u**)              | Local growth/decay/coupling | Local    | Nonlinear      | Constitutive       | Rate ~ \|\|R'\|\|     |
| Coupling    | C  | Cross-D + cross-R         | Species interaction         | Local    | Mixed          | Emergent instab.   | Ratio-dependent       |
| Rate scales | M  | D_i, rate constants       | Time-scale control          | N/A      | N/A            | Selects behavior   | Sets t_D, t_R         |

*Linear for constant D; weakly nonlinear for D = D(**u**).

---

## 4. Relation to AC and CH

The RD architecture is the *broadest second-order parabolic class* evaluated in the PDE Atlas. AC and CH are special members or relatives of this class, positioned by their additional structural commitments.

### 4.1 Allen–Cahn as a Special RD System

Allen–Cahn is a *single-species RD system* (n = 1) with specific additional structure:

    partial_t phi = M epsilon^2 Delta phi + M(phi - phi^3)

This is RD-III with D = M epsilon^2 and R(phi) = M(phi - phi^3). AC inherits all RD structural properties (second-order parabolic, local, reaction-diffusion balance) and adds:

- **Gradient-flow structure:** The reaction term R(phi) = -M f'(phi) is the negative gradient of a double-well potential. This makes AC a gradient flow of F[phi], which is *not* a property of general RD systems.
- **Maximum principle:** The reaction is inward-pointing at |phi| = 1, preserving the invariant set [-1, 1]. General RD systems may or may not have invariant sets.
- **Lyapunov functional:** F[phi] decreases monotonically. General RD systems may lack any Lyapunov functional.

AC is the *most structured* single-species RD system: it has everything a general RD system has, plus gradient-flow + maximum principle + Lyapunov. Every property of AC that makes it anomaly-free (in the AD evaluation) traces to these additional structures.

### 4.2 Cahn–Hilliard as a Non-Standard Relative

Cahn–Hilliard is *not* a standard RD system:

    partial_t phi = M Delta [phi^3 - phi - epsilon^2 Delta phi]

This is *fourth-order* (bilaplacian), while RD systems are second-order (Laplacian). CH shares the same free energy as AC but uses the H^{-1} gradient-flow metric (conserved dynamics) instead of the L^2 metric (non-conserved dynamics). CH is related to RD through the limiting hierarchy:

    RD (second-order, non-conserved) → AC (second-order, gradient flow)
    CH (fourth-order, conserved, gradient flow) → sharp-interface limits of both

CH is the *conserved extension* of AC, obtained by wrapping the chemical potential inside a conserving Laplacian. This raises the PDE order from 2 to 4 and places CH outside the standard RD class.

### 4.3 What General RD Systems May Lack

General RD systems, unlike AC, may lack:

- **Lyapunov functional:** Most RD systems have no known free energy or entropy functional that decreases along trajectories. Without a Lyapunov functional, the dynamics can exhibit oscillations, limit cycles, chaos, and non-convergent behavior. The Lotka–Volterra, Brusselator, and FitzHugh–Nagumo systems all lack global Lyapunov functionals.

- **Maximum principle:** The scalar maximum principle holds for single-species RD systems with appropriate reaction terms (R inward-pointing at the boundary of an invariant set). For multi-species systems (n >= 2), the *component-wise* maximum principle generally fails — the coupling between species can drive individual concentrations outside their natural range. Invariant-region theory (Chueh–Conley–Smoller) provides partial substitutes, but these require specific structural conditions on **R** and **D**.

- **Conservation laws:** General RD systems do not conserve total mass. Individual species may be produced or consumed by the reaction terms. Conservation (sum_i u_i = const, or integral u_i dx = const) requires specific structural constraints on R (e.g., R_1 + R_2 = 0 for a two-species conversion reaction). When present, conservation adds structure analogous to CH-3.

- **Gradient-flow structure:** The gradient flow of a free energy requires R = -grad_u F for some functional F. This is a severe restriction on the reaction kinetics — most multi-species RD systems are not gradient flows. Non-gradient systems can exhibit phenomena forbidden in gradient flows: oscillations, traveling waves, spiral waves, and spatiotemporal chaos.

### 4.4 RD as the Universality Class for Pattern Formation

RD systems are the canonical architecture for *spatial pattern formation*:

- **Turing patterns:** Stationary periodic structures (spots, stripes, labyrinths) arising from diffusion-driven instability in activator-inhibitor systems.
- **Traveling waves:** Fronts, pulses, and wave trains propagating through excitable or bistable media.
- **Spiral waves:** Rotating spiral patterns in two-dimensional excitable media (e.g., Belousov–Zhabotinsky reaction, cardiac tissue).
- **Spatiotemporal chaos:** Irregular, aperiodic dynamics with sensitive dependence on initial conditions.
- **Self-replicating spots:** Localized structures that divide and multiply (Gray–Scott model).

None of these phenomena occur in the gradient-flow architectures (AC, CH), which are confined to monotone energy descent. The full RD class — without gradient-flow constraints — is the architectural home of oscillatory, excitable, and chaotic spatiotemporal dynamics.

### 4.5 Positioning Table

| Feature                    | General RD              | Allen–Cahn             | Cahn–Hilliard          |
|----------------------------|-------------------------|------------------------|------------------------|
| PDE order                  | 2nd                     | 2nd                    | 4th                    |
| Species count              | n >= 1                  | n = 1                  | n = 1                  |
| Gradient-flow structure    | Generally no            | Yes (L^2)              | Yes (H^{-1})           |
| Lyapunov functional        | Generally no            | Yes (F)                | Yes (F)                |
| Maximum principle          | Conditional (n=1 only)  | Yes                    | No                     |
| Conservation laws          | Generally no            | No                     | Yes                    |
| Oscillations / limit cycles| Permitted               | Forbidden              | Forbidden              |
| Chaos                      | Permitted               | Forbidden              | Forbidden              |
| Turing patterns            | Permitted (n >= 2)      | Forbidden (n = 1)      | Forbidden (n = 1)      |
| Traveling waves            | Permitted               | Permitted (fronts)     | Not standard           |
| Spiral waves               | Permitted (n >= 2)      | Forbidden              | Forbidden              |
| Blowup channel             | Possible (constitutive) | None                   | None                   |
| Locality                   | Fully local             | Fully local            | Fully local            |

---

*End of Architectural Specification. The Mode 1 (Axiom → Envelope) analysis will follow in the next file.*
