# AD Evaluation: Cahn–Hilliard Equation — Architectural Specification

Allen Proxmire

April 2026

---

## 1. Implicit Axioms of the Cahn–Hilliard Architecture

The Cahn–Hilliard (CH) equation models the phase separation of a binary mixture through the evolution of a conserved order parameter. Like Navier–Stokes, its PDE formulation rests on a set of implicit architectural axioms — commitments that are not derived from deeper principles but are chosen as the foundation of the dynamical system. Each axiom defines a structural boundary where the architecture commits to a specific representation.

### Axiom CH-1: Continuum Hypothesis

The system is modeled as a continuous medium. The order parameter phi(x, t), representing the local concentration difference between two phases (or the local composition), is assumed to be a well-defined smooth field at every point x in the domain Omega and every time t >= 0. This axiom suppresses the molecular discreteness of the mixture and replaces it with a smooth scalar field. The continuum hypothesis is valid when the observation length scale L far exceeds the molecular interaction scale, but the equation carries no internal mechanism for detecting when this assumption breaks down.

### Axiom CH-2: Locality

All interactions are local in the following sense: the time evolution of phi at a point x depends only on phi, the chemical potential mu, and their spatial derivatives at x. The CH equation is a PDE — a differential, not integral, description. There is no action at a distance in the governing equation itself. This is the same *differential locality* as Navier–Stokes: physics is encoded in local differential operators.

Note: unlike NS, the CH architecture has no nonlocal enforcement channel. The chemical potential mu is defined pointwise from phi and its derivatives — there is no elliptic constraint analogous to the pressure Poisson equation. CH is *fully local* at both the formulation and solution levels.

### Axiom CH-3: Conserved Order Parameter

The order parameter phi is globally conserved:

    d/dt integral_Omega phi(x, t) dx = 0

This is the defining structural commitment of the Cahn–Hilliard equation and the feature that distinguishes it from the Allen–Cahn equation (which has the same free energy but a non-conserved order parameter). Conservation forces the dynamics to take the form of a *divergence of a flux*:

    partial_t phi = -div(**J**)

for some flux **J**. The architecture cannot create or destroy phi — it can only redistribute it. This conservation law is exact, not approximate, and holds for all time.

### Axiom CH-4: Gradient-Flow Structure

The CH equation is a *gradient flow* of a free-energy functional F[phi] with respect to the H^{-1} inner product. Concretely, the dynamics are dissipative and driven by the tendency to decrease F:

    partial_t phi = div(M nabla mu),    mu = delta F / delta phi

where mu is the chemical potential (the variational derivative of F with respect to phi) and M is the mobility. The gradient-flow structure guarantees:

- F[phi(t)] is monotone non-increasing in time (for M >= 0).
- The dynamics are dissipative: the system evolves toward local minima of F.
- Stationary solutions satisfy mu = const (uniform chemical potential, thermodynamic equilibrium).

This is the deepest structural axiom of the CH architecture: the PDE is not an arbitrary evolution equation but is *derived* from a variational principle. The free energy F is the *generating object* from which the entire dynamics descend.

### Axiom CH-5: Free-Energy Functional (Double-Well + Gradient Penalty)

The free energy is assumed to take the Ginzburg–Landau form:

    F[phi] = integral_Omega [ f(phi) + (epsilon^2 / 2) |nabla phi|^2 ] dx

where:
- f(phi) is the *bulk free-energy density*, a double-well potential with two minima at phi = +/- 1 (or more generally at the two equilibrium phases). The standard choice is f(phi) = (1/4)(phi^2 - 1)^2.
- epsilon > 0 is the *interfacial width parameter*, controlling the thickness of the diffuse interface between phases.
- (epsilon^2 / 2)|nabla phi|^2 is the *gradient penalty*, penalizing sharp spatial gradients and favoring smooth transitions between phases.

This axiom selects a specific class of free energies. The double-well structure encodes *bistability* (two preferred phases), and the gradient penalty encodes *surface tension* (energetic cost of interfaces). The parameter epsilon sets the intrinsic length scale of the architecture — the width of the diffuse interface.

**Non-minimality note:** The double-well form of f(phi) is a modeling choice. Other potentials (logarithmic, Flory–Huggins, multi-well) are used in specific physical contexts. The gradient penalty is the leading-order term in a gradient expansion of the non-local free energy; higher-order gradient terms (|Delta phi|^2, etc.) are sometimes included. Axiom CH-5 selects the simplest nontrivial member of a family of possible free energies.

### Axiom CH-6: Chemical Potential Definition

The chemical potential mu is defined as the first variational derivative of F with respect to phi:

    mu = delta F / delta phi = f'(phi) - epsilon^2 Delta phi

For the standard double-well f(phi) = (1/4)(phi^2 - 1)^2:

    mu = phi^3 - phi - epsilon^2 Delta phi

The chemical potential is a *derived quantity*, not an independent field: it is entirely determined by phi and its spatial derivatives at each point. This is analogous to the NS pressure being determined by the velocity field, but with a crucial difference: mu is determined *locally* (by phi and Delta phi at each point), whereas the NS pressure is determined *nonlocally* (by the Poisson equation over the entire domain).

### Axiom CH-7: Mobility

The flux is driven by the gradient of the chemical potential, with proportionality constant M (the mobility):

    **J** = -M nabla mu

The mobility M may be:
- Constant: M = M_0 > 0. The simplest case, and the one most commonly analyzed.
- Concentration-dependent: M = M(phi). Physical models often use M(phi) = 1 - phi^2 (degenerate mobility, vanishing at the pure phases) or other positive functions.
- Tensor-valued: M_ij (anisotropic mobility). Rarely used; breaks the isotropy implicit in the standard CH.

The choice of mobility is a *constitutive axiom*, analogous to the Newtonian constitutive law (NS-3) in Navier–Stokes. It specifies how the system responds to chemical potential gradients. The constant-mobility case is the analogue of constant viscosity.

**Structural role:** The mobility M controls the *rate* of phase separation but not the *equilibrium* — the stationary solutions (mu = const) are independent of M. The mobility is the architecture's *kinetic* parameter, while the free energy F is the *thermodynamic* parameter.

### Axiom CH-8: Euclidean Geometry

The equation is formulated on flat Euclidean space R^d or on bounded domains Omega subset R^d (d = 1, 2, 3) with the standard Laplacian. The metric is flat. Curvature effects, flows on manifolds, and non-Euclidean geometries are outside the architecture.

---

## 2. Canonical PDE in Architectural Form

### 2.1 Order Parameter Evolution

The Cahn–Hilliard equation in its canonical form:

    partial_t phi = div(M nabla mu)                                ... (CH-I)

For constant mobility M:

    partial_t phi = M Delta mu                                     ... (CH-II)

### 2.2 Chemical Potential

    mu = f'(phi) - epsilon^2 Delta phi                             ... (CH-III)

For the standard double-well f(phi) = (1/4)(phi^2 - 1)^2:

    mu = phi^3 - phi - epsilon^2 Delta phi                         ... (CH-IV)

### 2.3 Combined Fourth-Order Form

Substituting (CH-IV) into (CH-II) with M = const:

    partial_t phi = M Delta [phi^3 - phi - epsilon^2 Delta phi]

    = M Delta(phi^3 - phi) - M epsilon^2 Delta^2 phi              ... (CH-V)

This is a *fourth-order* parabolic PDE. The highest-order term -M epsilon^2 Delta^2 phi (the biharmonic term) provides the dominant regularization. The equation is fourth-order because the free energy contains |nabla phi|^2 (second derivatives in F lead to fourth derivatives in the evolution via the double variational derivative).

### 2.4 Channel-Labeled Decomposition

We decompose (CH-V) into its structural channels:

    partial_t phi =    M Delta(phi^3 - phi)      -    M epsilon^2 Delta^2 phi
                   |________________________|    |__________________________|
                     Reaction-diffusion            Surface-tension diffusion
                     (double-well channel)          (gradient-penalty channel)

Or equivalently, at the flux level:

    **J** = -M nabla mu = -M nabla [f'(phi)] + M epsilon^2 nabla(Delta phi)
          |___________________|   |__________________________|
            Chemical flux           Capillary flux
            (toward equilibrium)     (against sharp gradients)

### 2.5 Boundary Conditions

Standard boundary conditions for CH on a bounded domain Omega:

**Natural (variational) boundary conditions:**

    nabla phi . **n** = 0    on partial Omega    (no-flux of phi)
    nabla mu . **n** = 0     on partial Omega    (no-flux of chemical potential)

These enforce:
- Conservation of total phi (no flux through the boundary).
- No contact-angle constraint (90-degree contact angle by default).

**Alternative boundary conditions:**
- Periodic boundary conditions (on rectangular domains).
- Dirichlet conditions on phi or mu (non-variational, break conservation if imposed on phi).
- Dynamic contact-angle conditions (extend the architecture to include wall-fluid interactions).

### 2.6 Initial Conditions

    phi(x, 0) = phi_0(x)

The initial data phi_0 must be sufficiently regular (e.g., phi_0 in H^2(Omega)) for the classical solution theory. Unlike NS, there is no constraint on the initial data analogous to div(**u**_0) = 0 — the conservation law d/dt integral phi dx = 0 is automatically preserved by the PDE, not imposed as an initial constraint.

---

## 3. Channel Identification

The Cahn–Hilliard architecture routes dynamics through five identifiable structural channels. Each channel has a distinct mathematical character, physical role, and scaling behavior.

### Channel D: Mass-Conserving Diffusion

    D(phi) = M Delta mu = -div(M nabla mu)    [in conservation form]

- **Role:** Redistributes the order parameter phi across space, driven by gradients in the chemical potential mu. This is the *transport* mechanism of the CH architecture — it moves material from regions of high chemical potential to regions of low chemical potential, conserving total mass.
- **Locality:** Local. The flux **J** = -M nabla mu depends on phi and its derivatives at each point.
- **Linearity:** Nonlinear (through the dependence of mu on phi). The flux is a nonlinear function of phi, though it is linear in nabla mu for constant M.
- **Scaling:** If phi ~ O(1), length ~ L, then the diffusive flux scales as J ~ M / L for the reaction part and J ~ M epsilon^2 / L^3 for the capillary part. The overall time scale is t ~ L^4 / (M epsilon^2) — fourth-order diffusion, much slower than second-order diffusion at large scales.

### Channel R: Double-Well Reaction Landscape

    R(phi) = M Delta [f'(phi)] = M Delta [phi^3 - phi]

- **Role:** Drives phase separation by amplifying concentration differences. The double-well potential f(phi) has two minima (at phi = +/- 1), creating a thermodynamic preference for phase-pure states. The reaction channel *destabilizes* the homogeneous state: perturbations near phi = 0 (the unstable hilltop of the double-well) grow, pushing the system toward phi = +1 or phi = -1.
- **Locality:** Local. f'(phi) is an algebraic function of phi at each point.
- **Linearity:** Nonlinear. The reaction term f'(phi) = phi^3 - phi is cubic in phi. This is the sole source of nonlinearity in the CH architecture.
- **Scaling:** R ~ M / L^2 for concentration variations of O(1) over length L.

**Structural role in the energy budget:** The reaction channel tends to *decrease* the bulk free energy integral f(phi) dx by driving phi toward the wells. It is the *thermodynamic driving force* for phase separation.

### Channel S: Surface-Tension / Gradient-Penalty Channel

    S(phi) = -M epsilon^2 Delta^2 phi

- **Role:** Penalizes sharp spatial gradients in phi, favoring smooth interfaces between phases. The gradient penalty (epsilon^2/2)|nabla phi|^2 in the free energy produces a fourth-order (biharmonic) diffusion term that regularizes the solution, prevents infinitely sharp interfaces, and sets the interfacial width at O(epsilon).
- **Locality:** Local. The biharmonic operator Delta^2 involves only derivatives at each point (up to fourth order).
- **Linearity:** Linear. The surface-tension channel is a linear operator on phi.
- **Scaling:** S ~ M epsilon^2 / L^4. This term dominates at small scales (large L^{-4}) and is subdominant at large scales.

**Structural role in the energy budget:** The surface-tension channel tends to *increase* the bulk free energy (by smoothing interfaces, which reduces gradient energy but may push phi away from the wells) and acts as the *regularizing* counterpart to the destabilizing reaction channel.

### Channel G: Gradient-Flow / Energy Dissipation

    G: dF/dt = -integral M |nabla mu|^2 dx <= 0

- **Role:** This is not a separate term in the PDE but a *structural property* of the full evolution: the CH equation is a gradient flow of F with respect to the H^{-1} metric. The free energy F[phi(t)] is monotone non-increasing. The dissipation rate is integral M |nabla mu|^2 dx, which vanishes only when mu = const (equilibrium).
- **Locality:** The dissipation density M |nabla mu|^2 is local.
- **Linearity:** Nonlinear (through the dependence of mu on phi).
- **Scaling:** The dissipation rate scales as M / L^2 times the squared chemical-potential gradient.

**Structural role:** The gradient-flow channel is the *architectural guarantee of thermodynamic consistency*. It ensures that the dynamics are dissipative, that the system evolves toward equilibrium, and that no perpetual oscillation or energy creation is possible. This is the CH analogue of the NS energy inequality — but stronger, because the CH dissipation identity is *exact* (not merely an inequality), holds for all solutions (not just smooth ones in a suitable sense), and involves a Lyapunov functional (F) rather than just a norm.

### Channel M: Mobility

    M(phi): controls the kinetic rate of the flux **J** = -M nabla mu

- **Role:** The mobility M sets the rate at which the system responds to chemical-potential gradients. It is a *kinetic* parameter that controls the speed of phase separation without affecting the equilibrium states.
- **Locality:** Local (M depends on phi at each point, for concentration-dependent mobility).
- **Linearity:** M is a prescribed function (possibly constant, possibly phi-dependent), not an operator. It modulates the linear and nonlinear channels multiplicatively.
- **Scaling:** M sets the overall time scale. Doubling M halves the time to equilibrium.

**Degenerate mobility:** If M(phi) = 1 - phi^2 (vanishing at the pure phases), the flux vanishes in regions of pure phase. This introduces a *kinetic constraint* — phase-pure regions are frozen, and dynamics occur only at interfaces. Degenerate mobility is the CH analogue of a contact-line condition: it physically encodes the fact that diffusion requires the presence of both species.

### Channel Summary Table

| Channel | Symbol | Term in PDE                   | Role                       | Locality | Linearity   | Scale Action                |
|---------|--------|-------------------------------|----------------------------|----------|-------------|-----------------------------|
| Diffusion   | D | M Delta mu                | Mass redistribution        | Local    | Nonlinear   | Fourth-order (t ~ L^4)     |
| Reaction    | R | M Delta[f'(phi)]          | Phase separation driving   | Local    | Nonlinear   | Destabilizes at large L     |
| Surface-ten.| S | -M eps^2 Delta^2 phi      | Interface regularization   | Local    | Linear      | Stabilizes at small L       |
| Gradient-flow | G | dF/dt <= 0              | Lyapunov dissipation       | Local    | Nonlinear   | Monotone energy decrease    |
| Mobility    | M | M(phi)                    | Kinetic rate control       | Local    | Prescribed  | Sets time scale             |

---

## 4. Contrast with Event Density (ED) Architecture

The Cahn–Hilliard and Event Density architectures occupy fundamentally different positions in the space of mathematical structures. The key contrasts are:

### 4.1 Gradient-Flow PDE vs. Static Multiplicative Ontology

The CH equation is a *dynamical system* — a fourth-order parabolic PDE that evolves a field phi(x, t) in time. Its architecture is *variational*: the entire dynamics are derived from a single functional F[phi] through the gradient-flow mechanism. Time, space, and energy are all structural variables.

The FS/ED architecture is *static*: the integers do not evolve. The FS primitives (width, height, activation, coverage, escape) describe the multiplicative structure of Z as a fixed geometric object. There is no time variable, no PDE, no evolution. The "dynamics" of the ED framework are evaluations of sums and densities over expanding domains — they measure a pre-existing structure, not a process.

### 4.2 Variational Structure vs. No Variational Structure

CH possesses a free-energy functional F[phi] from which the entire PDE is derived by variational differentiation. This functional is the *generating object* of the architecture: the chemical potential, the flux, the dissipation rate, and the equilibrium conditions all descend from F. The existence of F guarantees thermodynamic consistency, monotone dissipation, and a well-defined notion of "distance to equilibrium."

ED has no variational structure. The FS primitives are defined combinatorially (by factorization), not variationally (by extremizing a functional). There is no free energy, no Lagrangian, no action principle. The laws of the ED architecture (PNT, Mertens, Chebyshev conservation) are *identities and asymptotics* of arithmetic functions, not Euler–Lagrange equations of a functional.

### 4.3 Conservation Law vs. No Conservation Law

CH has a conserved quantity: the total order parameter integral phi dx is exactly preserved by the dynamics. This conservation law shapes the entire architecture — it forces the evolution into divergence form, requires the chemical potential to mediate the dynamics, and prevents the system from reaching the global energy minimum by direct relaxation (it must redistribute phi, not create or destroy it).

ED has no conservation law in the dynamical sense. The Chebyshev conservation law (sum log p / p = log x + O(1)) is an asymptotic identity, not a dynamical constraint. It describes how arithmetic mass is distributed across the skyline, but it does not constrain an evolution — there is no evolution to constrain.

### 4.4 Full Locality vs. Full Locality

Both CH and ED are *fully local* architectures — a contrast with Navier–Stokes, which has the nonlocal pressure channel.

- **CH:** All channels (D, R, S, G, M) depend only on phi and its derivatives at each point. The chemical potential mu = f'(phi) - epsilon^2 Delta phi is determined locally. There is no elliptic constraint, no Poisson equation, no Green's function coupling distant points.

- **ED:** All primitives (width, height, activation, coverage, escape) at integer n depend only on the factorization of n. No integer's FS structure depends on any other integer's structure.

The shared locality distinguishes both CH and ED from NS. In the NS architecture, the pressure Poisson equation introduces irreducible nonlocality; neither CH nor ED has an analogous mechanism. This makes CH a *closer architectural relative of ED* than NS is, despite the fact that CH is a PDE and ED is a number-theoretic structure.

### 4.5 Summary Table

| Feature                     | Cahn–Hilliard              | Event Density (ED)           |
|-----------------------------|----------------------------|------------------------------|
| Type                        | Gradient-flow PDE          | Static multiplicative ontology|
| Domain                      | Continuous (R^d)           | Discrete (Z)                 |
| Time evolution              | Yes (parabolic, 4th order) | No (static)                  |
| Variational structure       | Yes (F[phi])               | No                           |
| Conservation law            | Yes (integral phi)         | No (Chebyshev is asymptotic) |
| Locality                    | Fully local                | Fully local                  |
| Nonlinear channel           | Reaction (f'(phi))         | None (linear primitives)     |
| Lyapunov functional         | Yes (F decreasing)         | No                           |
| Blowup channel              | None                       | None                         |
| Equilibrium / attractor     | Energy minimizers           | Arithmetic structure itself   |

---

*End of Architectural Specification. The Mode 1 (Axiom → Envelope) analysis will follow in the next file.*
