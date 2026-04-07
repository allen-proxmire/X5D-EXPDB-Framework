# AD Evaluation: Allen–Cahn Equation — Architectural Specification

Allen Proxmire

April 2026

---

## 1. Implicit Axioms of the Allen–Cahn Architecture

The Allen–Cahn (AC) equation models the evolution of a non-conserved order parameter toward equilibrium, driven by the descent of a free-energy functional. It shares its thermodynamic foundation — the same free energy, the same double-well potential, the same gradient penalty — with the Cahn–Hilliard equation, but makes a fundamentally different kinetic commitment: *the order parameter is not conserved*. This single architectural difference — the absence of the conserving Laplacian — changes the PDE from fourth-order to second-order, eliminates coarsening dynamics, introduces the possibility of a maximum principle, and produces a simpler but weaker architecture.

### Axiom AC-1: Continuum Hypothesis

The system is modeled as a continuous medium. The order parameter phi(x, t) is a smooth scalar field defined at every point x in the domain Omega and every time t >= 0. This axiom suppresses molecular discreteness and replaces it with a smooth field variable. It is the same commitment as CH-1 and NS-1: valid when the observation scale far exceeds the molecular scale, with no internal mechanism for detecting its own breakdown.

### Axiom AC-2: Locality

All interactions are local: the time evolution of phi at x depends only on phi and its spatial derivatives at x. The AC equation is a PDE with local differential operators — no integral kernels, no nonlocal coupling, no elliptic constraints. Like CH, and unlike NS, the AC architecture is *fully local* at both the formulation and solution levels. There is no analogue of the pressure Poisson equation.

### Axiom AC-3: Non-Conserved Order Parameter

The order parameter phi is *not* conserved:

    d/dt integral_Omega phi(x, t) dx ≠ 0    in general

This is the defining structural commitment of Allen–Cahn, and the single axiom that distinguishes it from Cahn–Hilliard. The dynamics are *not* in divergence form — the evolution equation is:

    partial_t phi = -M mu

not partial_t phi = div(M nabla mu). The architecture can create and destroy phi locally. A point where phi = 0.5 can evolve to phi = 1.0 without any compensating decrease elsewhere. Mass is not an accounting constraint.

**Consequences of non-conservation:**
- The PDE is second-order (not fourth-order). The evolution partial_t phi = -M mu = -M[f'(phi) - epsilon^2 Delta phi] involves at most the Laplacian, not the bilaplacian.
- The dynamics are *faster* than CH at large scales: AC relaxation scales as t ~ L^2 (second-order diffusion), while CH coarsening scales as t ~ L^4 (fourth-order diffusion).
- There is no Ostwald ripening or diffusion-limited coarsening — the architecture can annihilate interfaces directly by locally adjusting phi, without transporting mass through the bulk.
- The H^{-1} gradient-flow structure of CH is replaced by an L^2 gradient-flow structure in AC.

### Axiom AC-4: Gradient-Flow Structure

The AC equation is a gradient flow of the same free-energy functional F[phi] used by Cahn–Hilliard, but with respect to the *L^2 inner product* (not the H^{-1} inner product):

    partial_t phi = -M (delta F / delta phi) = -M mu

The gradient-flow structure guarantees:
- F[phi(t)] is monotone non-increasing: dF/dt <= 0.
- Stationary solutions satisfy mu = delta F / delta phi = 0 (not mu = const as in CH).
- The dynamics are dissipative: every trajectory descends the energy landscape.
- No limit cycles, no chaos, no recurrence to higher-energy states.

The L^2 gradient flow is the *simplest* gradient-flow structure for a scalar field: the steepest descent of F in the pointwise L^2 metric. It is simpler than the CH gradient flow (which uses the H^{-1} metric and is more expensive for large-scale rearrangements) but less physically constrained (because it does not enforce conservation).

### Axiom AC-5: Free-Energy Functional (Double-Well + Gradient Penalty)

The free energy takes the same Ginzburg–Landau form as in CH:

    F[phi] = integral_Omega [f(phi) + (epsilon^2 / 2) |nabla phi|^2] dx

with:
- f(phi) = (1/4)(phi^2 - 1)^2, the standard double-well potential with minima at phi = ±1.
- epsilon > 0, the interfacial width parameter.
- (epsilon^2/2)|nabla phi|^2, the gradient penalty encoding surface tension.

The free energy is *identical* to CH-5. The two architectures differ in their *kinetic* response to the same thermodynamic landscape, not in the landscape itself. AC and CH are the L^2 and H^{-1} gradient flows of the same functional F.

### Axiom AC-6: Chemical Potential Definition

The chemical potential is the variational derivative of F:

    mu = delta F / delta phi = f'(phi) - epsilon^2 Delta phi = phi^3 - phi - epsilon^2 Delta phi

This is *identical* to CH-6. The chemical potential is a locally determined slave variable — entirely fixed by phi and Delta phi at each point. No nonlocal solve is required.

Note: in the AC context, "chemical potential" is sometimes called the "variational derivative" or "functional derivative" rather than "chemical potential," because the non-conserved dynamics do not describe diffusion-driven chemical equilibration. The mathematical object is the same.

### Axiom AC-7: Mobility

The mobility M > 0 is a positive scalar (or function of phi) that sets the kinetic rate:

    partial_t phi = -M mu

For constant M = M_0 > 0, the equation becomes:

    partial_t phi = M_0 [phi - phi^3 + epsilon^2 Delta phi]

The mobility controls the speed of relaxation but not the equilibrium states (which satisfy mu = 0 regardless of M). As in CH, the mobility is a constitutive kinetic parameter.

**Differences from CH mobility:**
- In CH, M multiplies nabla mu inside a divergence: div(M nabla mu). Degenerate mobility M(phi) = 1 - phi^2 restricts dynamics to interfaces.
- In AC, M multiplies mu directly: -M mu. Degenerate mobility M(phi) = 1 - phi^2 suppresses dynamics near the pure phases but does not restrict them to interfaces, because there is no divergence structure.

### Axiom AC-8: Euclidean Geometry

The equation is formulated on flat Euclidean R^d or bounded domains Omega subset R^d (d = 1, 2, 3) with the standard Laplacian. The same geometric commitment as CH-8 and NS-8.

---

## 2. Canonical PDE in Architectural Form

### 2.1 Order Parameter Evolution

The Allen–Cahn equation in canonical form:

    partial_t phi = -M mu = -M [f'(phi) - epsilon^2 Delta phi]        ... (AC-I)

For constant M and the standard double-well:

    partial_t phi = M [phi - phi^3 + epsilon^2 Delta phi]               ... (AC-II)

Or equivalently:

    partial_t phi = M epsilon^2 Delta phi + M(phi - phi^3)              ... (AC-III)

### 2.2 Chemical Potential

    mu = f'(phi) - epsilon^2 Delta phi = phi^3 - phi - epsilon^2 Delta phi    ... (AC-IV)

### 2.3 Channel-Labeled Decomposition

    partial_t phi =    M epsilon^2 Delta phi     +     M(phi - phi^3)
                   |_______________________|    |_____________________|
                     Laplacian smoothing           Reaction (double-well)
                     (Channel S)                    (Channel R)

**Channel S** (Laplacian smoothing): The term M epsilon^2 Delta phi is a *second-order* linear diffusion operator. It smooths the order parameter, penalizes spatial gradients, and drives phi toward spatial uniformity. In Fourier space, it damps mode k at rate M epsilon^2 k^2.

**Channel R** (Reaction / double-well): The term M(phi - phi^3) is a *zeroth-order* nonlinear reaction term. It drives phi toward the wells of the double-well potential:
- For |phi| < 1: phi - phi^3 > 0 if phi > 0 and phi - phi^3 < 0 if phi < 0. The reaction pushes phi toward the nearest well (±1).
- For |phi| > 1: phi - phi^3 < 0 if phi > 1 and phi - phi^3 > 0 if phi < -1. The reaction pulls phi back toward ±1.

The AC equation is a *reaction-diffusion equation*: a second-order parabolic PDE with a nonlinear reaction term and a linear diffusion term. This places it in the classical reaction-diffusion family, alongside the Fisher–KPP equation, the Nagumo equation, and the bistable equation.

### 2.4 Boundary Conditions

Standard boundary conditions:

    nabla phi . n = 0    on partial Omega    (Neumann / no-flux)

or periodic, or Dirichlet. The Neumann condition is the natural (variational) boundary condition derived from the free energy.

Note: unlike CH, there is no second boundary condition on mu (because the PDE is second-order, not fourth-order). A single boundary condition suffices.

### 2.5 Initial Conditions

    phi(x, 0) = phi_0(x)

No constraint on the initial data (unlike NS, which requires div(**u**_0) = 0). Any sufficiently regular phi_0 is admissible.

---

## 3. Channel Identification

The Allen–Cahn architecture routes dynamics through four structural channels.

### Channel R: Reaction / Double-Well

    R(phi) = M(phi - phi^3)

- **Role:** Drives the order parameter toward the wells phi = ±1. This is the thermodynamic driving force — the tendency of the system to minimize the bulk free energy f(phi). In the spinodal region (|phi| < 1), R amplifies deviations from the unstable hilltop phi = 0. Near the wells (|phi| close to 1), R acts as a restoring force that stabilizes the equilibrium.
- **Locality:** Local. R depends only on phi at each point (algebraic function, no derivatives).
- **Linearity:** Nonlinear. Cubic in phi. This is the sole nonlinearity in the AC architecture.
- **Scaling:** R ~ M for phi = O(1). The reaction channel operates at a *fixed rate* independent of spatial scale — it does not involve spatial derivatives.

### Channel S: Surface Tension / Laplacian Smoothing

    S(phi) = M epsilon^2 Delta phi

- **Role:** Smooths the order parameter by penalizing spatial gradients. The Laplacian diffusion drives phi toward spatial uniformity and sets the interface width at O(epsilon). This is the *regularizing* channel that prevents infinitely sharp interfaces.
- **Locality:** Local. Depends on phi and its second spatial derivatives.
- **Linearity:** Linear. The Laplacian is a linear operator.
- **Scaling:** S ~ M epsilon^2 / L^2 for variations at length scale L. The smoothing rate grows as L^{-2} — small-scale features are smoothed faster. At the interface scale L ~ epsilon, the smoothing rate is M, matching the reaction rate. This balance sets the interface width.

### Channel G: Gradient-Flow Dissipation

    G: dF/dt = -M integral |mu|^2 dx <= 0

- **Role:** Structural property of the full evolution. The free energy F is a strict Lyapunov functional, decreasing at rate M ||mu||_{L^2}^2. The gradient-flow channel ensures thermodynamic consistency: the dynamics always reduce F, and the only stationary states have mu = 0 everywhere.
- **Locality:** The dissipation density M |mu|^2 is local.
- **Linearity:** Nonlinear (through mu's dependence on phi).
- **Scaling:** The dissipation rate scales as M times the square of the chemical potential deviation from zero.

**Comparison with CH gradient flow:** The CH dissipation rate is M ||nabla mu||_{L^2}^2 (involving gradients of mu), while the AC dissipation rate is M ||mu||_{L^2}^2 (involving mu itself). The CH rate measures how far mu is from being *spatially uniform*; the AC rate measures how far mu is from being *zero*. This reflects the different equilibrium conditions: CH equilibrium is mu = const; AC equilibrium is mu = 0.

### Channel M: Mobility

    M(phi): multiplicative kinetic prefactor

- **Role:** Controls the relaxation rate without affecting equilibrium states.
- **Locality:** Local.
- **Linearity:** Prescribed function, not an operator.
- **Scaling:** M sets the overall time scale.

### Channel Summary Table

| Channel | Symbol | Term                    | Role                     | Locality | Linearity   | Scaling             |
|---------|--------|-------------------------|--------------------------|----------|-------------|---------------------|
| Reaction    | R  | M(phi - phi^3)         | Drive toward wells       | Local    | Nonlinear   | Rate ~ M (scale-free)|
| Smoothing   | S  | M eps^2 Delta phi      | Interface regularization | Local    | Linear      | Rate ~ M eps^2/L^2  |
| Grad. flow  | G  | dF/dt = -M\|\|mu\|\|^2| Lyapunov dissipation     | Local    | Nonlinear   | All-scale decay      |
| Mobility    | M  | M(phi)                 | Kinetic rate control     | Local    | Prescribed  | Sets time scale      |

**Note:** The AC architecture has *four* channels, compared to CH's *five*. The missing channel is the *mass-conserving diffusion* channel D, which exists in CH because of the conserving Laplacian div(M nabla mu). In AC, the Laplacian appears inside the chemical potential (as part of S), not as an outer diffusion operator. The absence of channel D is the structural signature of non-conservation.

---

## 4. Contrast with Cahn–Hilliard

Allen–Cahn and Cahn–Hilliard share the same thermodynamic foundation but differ in their kinetic architecture. The contrasts are sharp and structurally consequential.

### 4.1 Conservation

**AC:** Non-conserved. d/dt integral phi dx ≠ 0 in general. The architecture can create and destroy phi locally.

**CH:** Conserved. d/dt integral phi dx = 0 exactly. The architecture can only redistribute phi.

This is the *single axiom* that separates the two architectures. All other structural differences (PDE order, smoothing power, coarsening behavior, channel count) are downstream consequences of this kinetic choice.

### 4.2 PDE Order

**AC:** Second-order parabolic. partial_t phi = M epsilon^2 Delta phi + M(phi - phi^3). The highest-order spatial operator is the Laplacian (Delta).

**CH:** Fourth-order parabolic. partial_t phi = -M epsilon^2 Delta^2 phi + M Delta(phi^3 - phi). The highest-order spatial operator is the bilaplacian (Delta^2).

The fourth-order character of CH arises from the conserving Laplacian acting on the chemical potential (which itself contains a Laplacian). AC, lacking the outer Laplacian, is two orders lower.

### 4.3 Smoothing Power

**AC:** Second-order smoothing. The Laplacian damps mode k at rate epsilon^2 k^2. This is sufficient to control the cubic nonlinearity in d <= 3 (by the same argument as the heat equation: the Laplacian is the standard parabolic regularizer, and the cubic is subcritical relative to H^1 in d <= 3).

**CH:** Fourth-order smoothing. The bilaplacian damps mode k at rate epsilon^2 k^4. This provides *stronger* regularization — two extra orders of smoothing — giving CH unconditional H^2 control and a wider regularity margin.

**Consequence:** Both AC and CH have global regularity in d <= 3, but for different reasons. AC achieves regularity through the *maximum principle* (available for second-order parabolic equations) combined with standard energy estimates. CH achieves regularity through *fourth-order smoothing* and Sobolev embedding. The AC regularity proof is simpler; the CH regularity is more robust.

### 4.4 Maximum Principle

**AC:** Satisfies a maximum principle. If |phi_0(x)| <= 1 for all x, then |phi(x, t)| <= 1 for all x, t. The reaction term M(phi - phi^3) is inward-pointing at phi = ±1 (it pushes phi back toward the interval [-1, 1]), and the Laplacian preserves the maximum principle for second-order parabolic equations.

**CH:** Does *not* satisfy a maximum principle. Fourth-order parabolic equations can overshoot the well values ±1 (E6 in the CH Mode 1 envelope).

This is a significant structural difference. The AC maximum principle provides L^{infinity} control for free — no Sobolev embedding needed. CH must work harder (using H^2 estimates and Sobolev embedding) to achieve the same L^{infinity} control.

### 4.5 Interface Dynamics

**AC:** Interfaces move by *mean curvature*. In the sharp-interface limit (epsilon → 0), the AC equation converges to the motion-by-mean-curvature flow:

    V_n = sigma kappa

where V_n is the normal velocity of the interface and kappa is the mean curvature. Interfaces shrink and disappear — curved interfaces move inward (toward their center of curvature) and eventually collapse. Total interface area decreases.

**CH:** Interfaces move by *surface diffusion* (for degenerate mobility) or by *Mullins–Sekerka dynamics* (for constant mobility). In the sharp-interface limit, the CH equation converges to:

    V_n = M Delta_s (sigma kappa)    [surface diffusion]
    V_n = M [nabla mu]_+^-           [Mullins–Sekerka]

where Delta_s is the surface Laplacian. Interfaces evolve to reduce total area while conserving total enclosed volume.

The key difference: AC interfaces can *vanish* (a shrinking circle disappears in finite time). CH interfaces can *merge* and *coarsen* but cannot vanish without transferring their mass elsewhere. This is the kinetic consequence of conservation.

### 4.6 Gradient-Flow Metric

**AC:** L^2 gradient flow. partial_t phi = -M grad_{L^2} F. The L^2 metric treats all spatial scales equally — large-scale and small-scale rearrangements cost the same.

**CH:** H^{-1} gradient flow. partial_t phi = -M grad_{H^{-1}} F. The H^{-1} metric makes large-scale rearrangements expensive (proportional to L^2), which is why CH coarsening is slow (t ~ L^4).

### 4.7 Channel Count

**AC:** Four channels (R, S, G, M). No mass-conserving diffusion channel.

**CH:** Five channels (R, S, D, G, M). The mass-conserving diffusion channel D is present.

### 4.8 Summary Table

| Feature                    | Allen–Cahn                | Cahn–Hilliard              |
|----------------------------|---------------------------|----------------------------|
| Conservation               | Non-conserved             | Conserved                  |
| PDE order                  | 2nd order                 | 4th order                  |
| Gradient-flow metric       | L^2                       | H^{-1}                    |
| Smoothing order            | k^2 (Laplacian)           | k^4 (bilaplacian)          |
| Maximum principle          | Yes (|phi| <= 1)          | No (overshoot possible)   |
| Sharp-interface limit      | Mean curvature flow       | Mullins–Sekerka / surface diff. |
| Interface fate             | Shrink and vanish         | Merge and coarsen          |
| Coarsening                 | None (interfaces vanish)  | Yes (L ~ t^{1/3} or t^{1/4}) |
| Channel count              | 4                         | 5                          |
| Dissipation rate           | M \|\|mu\|\|^2            | M \|\|nabla mu\|\|^2      |
| Equilibrium condition      | mu = 0                    | mu = const                 |
| Global regularity (d<=3)   | Yes                       | Yes                        |
| Blowup channel             | None (standard potential) | None                       |
| Lyapunov functional        | F (exact identity)        | F (exact identity)         |
| Locality                   | Fully local               | Fully local                |

---

*End of Architectural Specification. The Mode 1 (Axiom → Envelope) analysis will follow in the next file.*
