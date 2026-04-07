# AD Evaluation: Cahn–Hilliard Equation — Mode 3: Channels → Constraint Surface

Allen Proxmire

April 2026

---

## Overview

Mode 3 constructs the *constraint surface* — the geometric object in channel space encoding all structural relationships among the CH channels. Where Mode 1 identified the envelope and Mode 2 the extremal dynamics, Mode 3 asks: *what is the shape of the space in which the channels operate?*

The CH constraint surface is qualitatively different from the NS constraint surface. The NS surface has a degenerate energy simplex (two null channels), an open enstrophy face in 3D, and a nonlocal channel. The CH surface has a non-degenerate but *one-dimensional* dissipation simplex (pure decay along a single ray), no open faces, and no nonlocal channels. The CH constraint surface is *compact and closed* — a feature it shares with the ED architecture but achieves through dynamical (gradient-flow) rather than static (combinatorial) mechanisms.

We continue with the canonical CH system:

    partial_t phi = M Delta mu,    mu = phi^3 - phi - epsilon^2 Delta phi
    F[phi] = integral [f(phi) + (epsilon^2/2)|nabla phi|^2] dx

---

## 1. Channel Decomposition

The Cahn–Hilliard PDE decomposes into five structural channels.

### Channel R: Reaction / Double-Well Destabilization

    R(phi) = M Delta[f'(phi)] = M Delta[phi^3 - phi]

- **Locality:** Local. Depends on phi and its second derivatives at each point (through the Laplacian of the algebraic function f'(phi)).
- **Linearity:** Nonlinear. The reaction term f'(phi) = phi^3 - phi is cubic in phi. This is the *sole source* of nonlinearity in the CH architecture.
- **Stability role:** Destabilizing at intermediate concentrations, stabilizing near the wells.
  - In the *spinodal region* (|phi| < 1/sqrt(3), where f''(phi) < 0): the effective diffusivity is negative. Concentration fluctuations are amplified — the reaction channel drives phase separation.
  - In the *metastable/stable region* (|phi| > 1/sqrt(3), where f''(phi) > 0): the effective diffusivity is positive. The reaction channel stabilizes the local concentration.
- **Scale action:** Scale-independent in its algebraic part. The Laplacian introduces a factor k^2, so the destabilizing effect grows with wavenumber as k^2 for k < k_c = 1/epsilon. The reaction channel is most dangerous at intermediate scales.

### Channel S: Surface Tension / Biharmonic Regularization

    S(phi) = -M epsilon^2 Delta^2 phi

- **Locality:** Local. The biharmonic operator Delta^2 involves fourth-order spatial derivatives at each point.
- **Linearity:** Linear. S is a bounded linear operator on appropriate Sobolev spaces.
- **Stability role:** Unconditionally stabilizing. The biharmonic term damps all modes, with damping rate proportional to k^4 in Fourier space. It is the architecture's *ultimate regularizer* — it controls the cubic nonlinearity in all dimensions d <= 3.
- **Scale action:** Strongly scale-selective. Damping rate = M epsilon^2 k^4. The surface-tension channel preferentially removes small-scale (high-k) structure and has negligible effect at large scales (small k). At wavenumber k = 1/epsilon, the damping rate is M/epsilon^2 — matching the reaction channel's maximum growth rate. For k >> 1/epsilon, the biharmonic dominates overwhelmingly.

### Channel D: Mass-Conserving Diffusion

    D(phi) = M Delta mu = -div(M nabla mu)

- **Locality:** Local (the divergence-form flux depends on nabla mu at each point).
- **Linearity:** Nonlinear (through the dependence of mu on phi).
- **Stability role:** Neutral. The diffusion channel is the *transport mechanism* — it redistributes phi in response to chemical potential gradients. It is neither inherently stabilizing nor destabilizing; its effect depends on the sign and magnitude of nabla mu, which is determined by the combined action of R and S.
- **Scale action:** Fourth-order overall (the double Laplacian structure gives scaling t ~ L^4). The diffusion channel slows down at large scales, making large-scale rearrangements expensive in the H^{-1} metric.

Strictly, D is the *composite* channel: D = R + S. We list it separately because the conservation-form structure (divergence of a flux) is an independent architectural feature — it is possible to have the same R and S channels without conservation (Allen–Cahn), and the conservation constraint fundamentally changes the dynamics.

### Channel G: Gradient-Flow Dissipation

    G: dF/dt = -M ||nabla mu||^2

- **Locality:** The dissipation density M |nabla mu|^2 is local.
- **Linearity:** Nonlinear (through mu's dependence on phi).
- **Stability role:** Stabilizing (globally). The gradient-flow structure guarantees that F decreases monotonically. G is not a separate term in the PDE but a *structural property* of the entire evolution — the Lyapunov identity that binds all other channels into a dissipative whole.
- **Scale action:** All-scale. The dissipation rate M ||nabla mu||^2 receives contributions from all wavenumbers. The gradient-flow structure ensures that the total energy budget is closed at every scale simultaneously.

### Channel M: Mobility

    M(phi): multiplicative prefactor in the flux **J** = -M nabla mu

- **Locality:** Local (M depends on phi at each point for concentration-dependent mobility).
- **Linearity:** Prescribed function, not an operator. M modulates the other channels multiplicatively.
- **Stability role:** Neutral. Mobility controls the *rate* of dynamics without affecting the equilibrium states or the direction of the gradient flow. It cannot create or destroy energy. For degenerate mobility M(phi) = 1 - phi^2, it introduces a kinetic constraint (freezing pure-phase regions) but does not alter the energy landscape.
- **Scale action:** For constant M: uniform across all scales. For degenerate M: introduces scale dependence by restricting dynamics to interfacial regions of width O(epsilon), effectively modifying the coarsening exponent from 1/3 to 1/4.

### Channel Summary Table

| Channel | Symbol | Term                        | Locality | Linearity   | Stability        | Scale Action           |
|---------|--------|-----------------------------|----------|-------------|------------------|------------------------|
| Reaction    | R  | M Delta[f'(phi)]           | Local    | Nonlinear   | Destabilizing*   | Amplifies k < 1/eps    |
| Surface ten.| S  | -M eps^2 Delta^2 phi       | Local    | Linear      | Stabilizing      | Damps k >> 1/eps (k^4) |
| Diffusion   | D  | M Delta mu = R + S          | Local    | Nonlinear   | Neutral (transport)| t ~ L^4 overall       |
| Grad. flow  | G  | dF/dt = -M\|\|nabla mu\|\|^2 | Local | Nonlinear   | Stabilizing      | All-scale dissipation  |
| Mobility    | M  | M(phi)                      | Local    | Prescribed  | Neutral          | Rate control           |

*Destabilizing only in the spinodal region (f''(phi) < 0); stabilizing in the metastable/stable regions.

---

## 2. Dissipation Partition

### 2.1 The CH Dissipation Simplex

The free-energy budget of the CH architecture is:

    dF/dt = W_R + W_S

where:
- W_R = integral mu_R partial_t phi dx, with mu_R = f'(phi), is the work done by the reaction channel.
- W_S = integral mu_S partial_t phi dx, with mu_S = -epsilon^2 Delta phi, is the work done by the surface-tension channel.

The total:

    dF/dt = integral mu partial_t phi dx = -M ||nabla mu||^2 <= 0

Critically, unlike NS, we cannot decompose the dissipation rate into independent channel contributions that vanish separately. The reaction and surface-tension channels contribute to the *chemical potential* mu = mu_R + mu_S, and the dissipation rate ||nabla mu||^2 is the squared gradient of their *sum*. The dissipation is a function of the combined channel output, not a sum of independent channel dissipations.

### 2.2 Collapse to a 1D Ray

The CH dissipation simplex is *one-dimensional*: a ray from zero (equilibrium) into the non-negative reals. At each instant, the dissipation rate is a single non-negative number:

    D(t) = M ||nabla mu(t)||^2 >= 0

There are no null channels (channels with zero energy contribution), no forcing channels (channels with positive energy contribution), and no separate dissipation channels. The entire energy budget is:

    dF/dt = -D(t) <= 0

This is a *one-parameter* accounting: know D(t) and you know everything about the energy dynamics. The CH dissipation simplex is a ray, not a simplex of any higher dimension.

### 2.3 Contrast with NS

| Feature                    | Cahn–Hilliard           | Navier–Stokes                  |
|----------------------------|-------------------------|--------------------------------|
| Energy channels            | R + S (combined)        | A, V, P, F (separate)          |
| Null channels              | None                    | A, P (both energy-null)        |
| Forcing channel            | None                    | F (energy source)              |
| Dissipation channels       | One (combined mu flow)  | One (viscosity V)              |
| Energy equation type       | dF/dt = -D (pure decay) | dE/dt = -eps + P_f (balance)   |
| Simplex dimension          | 0-simplex (ray)         | 1-simplex (line segment V–F)   |
| Enstrophy simplex (3D NS) | N/A                     | 2-simplex (stretch–diss–force) |

The CH architecture's energy accounting is *maximally simple*: a single scalar decay rate fully characterizes the instantaneous energy dynamics. NS has a richer (and in 3D, more dangerous) accounting structure because its energy simplex is at least one-dimensional and its enstrophy simplex is two-dimensional.

### 2.4 Contrast with ED

The ED dissipation partition (coverage–escape–activation) is a *fully populated 2-simplex*: three channels each carry a positive fraction of the arithmetic mass, and the partition has a nontrivial interior. The CH dissipation simplex collapses to a ray. ED's richer partition structure reflects the combinatorial complexity of prime factorization; CH's simpler structure reflects the thermodynamic monotonicity of gradient-flow dynamics.

---

## 3. Constraint Surface and Universality Classes

The CH constraint surface is parameterized by the relative activity levels of the channels R and S, mediated by the diffusion channel D. Different regions of this surface correspond to qualitatively different dynamical regimes.

### Class I: Spinodal Regime (R Dominates S)

**Condition:** phi near the unstable state (f''(phi) < 0), early time.
**Active channels:** R (dominant), S (subordinate), D, G, M.

In this regime, the reaction channel's negative effective diffusivity overwhelms the surface-tension channel's biharmonic damping for modes with k < k_c = |f''(phi)|^{1/2} / epsilon. The system is *linearly unstable* and undergoes spinodal decomposition.

**Properties:**
- Exponential growth of unstable Fourier modes.
- Fastest-growing mode at k_max = k_c / sqrt(2).
- Growth rate sigma_max = M f''(phi)^2 / (4 epsilon^2).
- The gradient-flow structure (G) ensures that F decreases even as the solution departs from homogeneity — the spinodal decomposition *reduces* free energy by allowing the system to access the lower-energy phase-separated states.

**Dominant inequalities:** U1 (dissipation identity), U6 (mass conservation), U8 (spinodal band from Mode 1 envelope).
**Permitted extremal behaviors:** Spinodal decomposition, pattern formation.
**Forbidden extremal behaviors:** Blowup, energy increase, mass creation/destruction.

### Class II: Interface Regime (R Balanced by S)

**Condition:** phi transitioning between ±1 across a diffuse interface of width O(epsilon).
**Active channels:** R and S (in local balance), D (transporting material across the interface), G (dissipating), M.

In this regime, the reaction and surface-tension channels are in *local equilibrium* within each interface. The interface profile is (approximately) the stationary solution of the one-dimensional problem:

    0 = f'(phi) - epsilon^2 phi'' => phi(z) = tanh(z / (epsilon sqrt(2)))

The interface width is O(epsilon), set by the R–S balance. Deviations from the equilibrium profile are corrected on the fast time scale O(epsilon^2 / M).

**Properties:**
- Interfaces are sharp on scale O(epsilon), smooth on scales << epsilon.
- The interface profile is a local attractor of the dynamics.
- Surface tension sigma = (2 sqrt(2)/3) epsilon is the energy per unit interface area.
- The chemical potential is approximately the Gibbs–Thomson relation: mu ≈ sigma kappa, where kappa is the interface mean curvature.

**Dominant inequalities:** U7 (interface width >= O(epsilon)), U2 (H^1 control from energy).
**Permitted extremal behaviors:** Interface formation, profile relaxation.
**Forbidden extremal behaviors:** Sub-epsilon interface structure, blowup.

### Class III: Coarsening Regime (D + S Dominate)

**Condition:** Well-separated phase domains with phi ≈ ±1 in the bulk, interfaces of width O(epsilon), late time.
**Active channels:** D (dominant — bulk diffusion drives coarsening), S (subordinate — maintains interface structure), R (nearly saturated in the bulk), G (slowly dissipating), M.

In this regime, the reaction channel has done its work: the bulk is nearly phase-pure. The dynamics are governed by the *slow diffusion* of material between domains of different sizes, driven by curvature differences (Gibbs–Thomson effect). The surface-tension channel maintains the interface structure but does not drive the bulk dynamics.

**Properties:**
- Domain size L(t) grows as t^{1/3} (constant mobility) or t^{1/4} (degenerate mobility).
- Free energy decays as F(t) ~ sigma * A(t), where A(t) is the total interface area.
- The number of domains decreases over time (topological simplification).
- Self-similar coarsening statistics (the domain size distribution, rescaled by L(t), approaches a universal form).

**Dominant inequalities:** U4 (coarsening rate bounds), U1 (dissipation identity), U6 (mass conservation).
**Permitted extremal behaviors:** Ostwald ripening, coalescence, domain annihilation.
**Forbidden extremal behaviors:** Domain creation, energy increase, faster-than-t^{1/3} coarsening.

### Class IV: Near-Equilibrium Regime (Linearized Gradient Flow)

**Condition:** phi close to a non-degenerate local minimum phi_* of F (subject to mass constraint).
**Active channels:** All channels linearized around phi_*.

In this regime, the dynamics are governed by the linearized CH operator:

    partial_t (delta phi) = M Delta [f''(phi_*)(delta phi) - epsilon^2 Delta(delta phi)]

This is a linear fourth-order parabolic equation with exponential decay at rate lambda_1 (the spectral gap of the linearized operator).

**Properties:**
- Exponential convergence: ||phi(t) - phi_*||_{H^1} <= C exp(-lambda_1 t).
- The spectral gap lambda_1 depends on the domain geometry, epsilon, and the specific equilibrium phi_*.
- All nonlinear effects are perturbative — the dynamics are essentially linear.
- The free energy decreases exponentially: F[phi(t)] - F[phi_*] <= C exp(-2 lambda_1 t).

**Dominant inequalities:** U1, U9 (exponential convergence from Mode 1 envelope).
**Permitted extremal behaviors:** Exponential relaxation.
**Forbidden extremal behaviors:** All nonlinear phenomena (spinodal, coarsening, metastability).

### Universality Class Summary

| Class | Regime           | Dominant Channels | Duration          | Key Scaling          |
|-------|------------------|-------------------|-------------------|----------------------|
| I     | Spinodal         | R >> S            | t ~ eps^2/M       | Exponential growth   |
| II    | Interface        | R ~ S (local)     | t ~ eps^2/M       | Profile relaxation   |
| III   | Coarsening       | D + S             | t ~ L^3/(M eps)   | L ~ t^{1/3}          |
| IV    | Near-equilibrium | Linearized all    | t → infinity       | exp(-lambda_1 t)     |

The CH dynamics proceed *sequentially* through these classes: I → II → III → IV. Every trajectory visits the same sequence (possibly skipping Class I if the initial data is already phase-separated). This sequential ordering is itself an architectural constraint — the gradient-flow structure ensures that the system descends through the energy landscape in a specific order, with each class corresponding to a distinct energy level.

---

## 4. Absence of Anomalies

The NS Mode 3 analysis identified two structural anomalies: the nonlocal pressure channel and the destabilizing vortex stretching sub-channel. The CH architecture has *neither*.

### 4.1 No Nonlocal Channel

Every CH channel is local: the reaction, surface-tension, diffusion, gradient-flow, and mobility channels all depend on phi and its derivatives at each point. There is no elliptic constraint, no Poisson equation, and no Green's function coupling distant points.

The chemical potential mu = f'(phi) - epsilon^2 Delta phi is determined pointwise. Unlike the NS pressure (which requires solving Delta p = -partial_i partial_j(u_i u_j) over the entire domain), the CH chemical potential requires no global solve — it is an *explicit local formula*.

**Why CH avoids nonlocality:** The CH architecture has no incompressibility constraint in the NS sense. The conservation law (integral phi = const) is enforced *automatically* by the divergence-form structure of the PDE, not by a global constraint that requires a Lagrange multiplier. The conservation law is a *consequence* of the local flux structure, not an *imposed* constraint requiring nonlocal enforcement.

### 4.2 No Destabilizing Sub-Channel Analogous to Vortex Stretching

The NS advection channel decomposes into A_transport (neutral) and A_stretch (destabilizing in 3D). The CH reaction channel R is destabilizing in the spinodal region, but it is *not* an anomaly in the NS sense because:

1. **The destabilization is bounded.** The reaction channel's maximum destabilizing effect is sigma_max = M/(4 epsilon^2), which is *finite and architecturally determined*. The NS vortex stretching has no a priori bound on its growth rate.

2. **The stabilizing channel dominates asymptotically.** The surface-tension channel S damps at rate k^4, which eventually overwhelms R's growth at rate k^2 for all k > k_c. In NS, the vortex stretching rate can potentially grow faster than viscous damping with no known saturation mechanism.

3. **The Lyapunov functional closes the loop.** Even though R is locally destabilizing, the global free-energy identity dF/dt = -M||nabla mu||^2 <= 0 ensures that the *combined* effect of R and S is always dissipative. There is no analogue of this in the NS enstrophy budget, where the stretching term has no definite sign relative to the total enstrophy.

4. **No dimensional dependence.** The CH reaction channel R has the same character in d = 1, 2, 3 — there is no analogue of the 2D/3D bifurcation caused by vortex stretching. The biharmonic controls the cubic in all dimensions.

### 4.3 No Open Face in the Constraint Surface

The NS constraint surface has an open face in 3D: the enstrophy inequality does not close, leaving a gap through which the dynamics might escape. The CH constraint surface has *no open face*:

- The energy inequality is an *exact identity* (no gap).
- The H^1 bound is unconditional (no dimensional restriction).
- The H^2 bound (and hence L^{infinity} bound) follows from fourth-order smoothing in all d <= 3.
- The regularity bootstrap closes without qualification.

Every face of the CH constraint surface is *sealed*. There is no direction in channel space in which the dynamics can escape.

### 4.4 No Blowup Gate

The NS architecture has a blowup gate: the BKM criterion (integral ||omega||_{L^infinity} dt = infinity) is the threshold whose violation signals finite-time blowup. The CH architecture has *no blowup gate* because:

- The free energy F is bounded below and monotone decreasing, so it remains finite for all time.
- F controls ||nabla phi||_{L^2} (uniformly in time).
- Fourth-order smoothing gives ||phi||_{H^2} control for t > 0.
- Sobolev embedding (H^2 hookrightarrow L^{infinity} for d <= 3) gives L^{infinity} control.
- The L^{infinity} bound closes the nonlinearity: |f'(phi)| <= C(1 + |phi|^3) is controlled.

No quantity needs to be monitored for potential divergence. There is no conditional regularity criterion because regularity is *unconditional*.

### 4.5 Structural Explanation

The absence of anomalies in the CH architecture traces to two structural features acting in concert:

**Feature 1: Fourth-order smoothing.** The biharmonic operator -epsilon^2 Delta^2 damps at rate k^4, which is *supercritical* relative to the cubic nonlinearity in d <= 3. This means the smoothing channel always wins at high wavenumbers, preventing the concentration of energy at small scales. In NS, the Laplacian damps at rate k^2, which is only *critical* in d = 2 and *subcritical* in d = 3 — the viscous smoothing may not win at high wavenumbers in 3D.

**Feature 2: Lyapunov structure.** The gradient-flow structure provides a strict Lyapunov functional F that decreases along every trajectory. This global constraint binds all channels into a cooperative dissipative structure: even though R is locally destabilizing, the combined effect of all channels is always energy-decreasing. NS has no Lyapunov functional (when forced), and even unforced NS has energy as a Lyapunov functional but lacks enstrophy as a Lyapunov functional in 3D.

Together, these two features seal the constraint surface: fourth-order smoothing prevents small-scale blowup, and the Lyapunov functional prevents large-scale energy growth. There is nowhere for the dynamics to escape.

---

## 5. Channel Constraints

The following constraints define the CH architectural signature — the identities and inequalities that all admissible channel states must satisfy.

---

**C1. Mass Conservation**

    integral_Omega phi(x, t) dx = integral_Omega phi_0(x) dx    for all t >= 0

The total order parameter is an exact invariant. The evolution is confined to a hyperplane in function space.

---

**C2. Free-Energy Monotonicity**

    dF/dt = -M ||nabla mu||^2 <= 0    for all t >= 0

The free energy is a strict Lyapunov functional. This is an *exact identity*, not an inequality.

---

**C3. Chemical Potential Locality**

    mu(x, t) = f'(phi(x, t)) - epsilon^2 Delta phi(x, t)

The chemical potential is determined locally — by phi and its second derivatives at each point. No nonlocal solve is required. This is the structural basis for CH's full locality.

---

**C4. Interface Width Lower Bound**

    (Interface width) >= C epsilon    for all admissible solutions

No structure finer than O(epsilon) can persist. The gradient penalty prevents sub-epsilon features.

---

**C5. No Finite-Time Blowup**

    ||phi(t)||_{H^2} < infinity    for all t > 0,    d = 1, 2, 3

The fourth-order smoothing provides instantaneous H^2 regularization. Global smooth solutions exist unconditionally.

---

**C6. Spinodal Band Selection**

    Unstable modes:  0 < k < k_c,    k_c = |f''(phi)|^{1/2} / epsilon
    Stable modes:    k > k_c
    Most unstable:   k_max = k_c / sqrt(2)

The spinodal instability band is determined architecturally by the double-well curvature f''(phi) and the interfacial parameter epsilon. The architecture selects its own instability wavelength.

---

**C7. Mobility Controls Time Scale Only**

    Equilibrium states { phi : mu = const } are independent of M
    Time to equilibrium scales as 1/M

The mobility is a purely kinetic parameter. It controls *when* the system arrives at equilibrium, not *where*.

---

**C8. No Nonlocal Coupling**

    All channel interactions are local (pointwise or via local derivatives)
    No elliptic constraint, no Poisson equation, no Green's function

The CH architecture is fully local at both the formulation and solution levels.

---

**C9. Fourth-Order Smoothing Dominates Cubic Nonlinearity**

    S(k) = M epsilon^2 k^4    dominates    R(k) ~ M k^2    for k >> 1/epsilon

The biharmonic damping rate grows as k^4; the reaction amplification grows at most as k^2. The surface-tension channel overwhelms the reaction channel at all wavenumbers above k_c. This dominance is the structural mechanism that closes the regularity bootstrap.

---

**C10. Coarsening Monotonicity**

    Total interface area A(t) is non-increasing in the coarsening regime
    Number of phase domains N(t) is non-increasing (for generic initial data)

Coarsening is a one-way process: domains merge and interfaces disappear but are not created. This follows from the gradient-flow structure (creating new interfaces would increase F).

---

**C11. Equilibrium Characterization**

    phi_* is a stationary solution   iff   mu = delta F / delta phi |_{phi_*} = const on Omega

Every equilibrium has uniform chemical potential. The equilibrium states are completely characterized by the variational condition delta F = lambda delta(integral phi) (Lagrange multiplier for the mass constraint).

---

**C12. No Chaotic Attractor**

    The gradient-flow structure forbids:
      - limit cycles
      - strange attractors
      - sensitive dependence on initial conditions (in the chaotic sense)
      - recurrence to higher-energy states

Every trajectory converges to a stationary state (a local minimum of F on the mass-constrained function space). The omega-limit set of every trajectory is a connected component of the set of equilibria.

---

### Channel Constraint Summary

| Label | Constraint                              | Type               | Scope     |
|-------|-----------------------------------------|--------------------|-----------|
| C1    | Mass conservation                       | Exact equality     | All       |
| C2    | Free-energy monotonicity                | Exact identity     | All       |
| C3    | Chemical potential locality             | Structural         | All       |
| C4    | Interface width >= O(epsilon)           | Lower bound        | All       |
| C5    | No finite-time blowup                  | Regularity         | All d<=3  |
| C6    | Spinodal band selection                 | Architectural      | Spinodal  |
| C7    | Mobility controls time scale only       | Structural         | All       |
| C8    | No nonlocal coupling                    | Structural         | All       |
| C9    | 4th-order dominates cubic               | Scale inequality    | All       |
| C10   | Coarsening monotonicity                 | Monotonicity        | Coarsening|
| C11   | Equilibria = constant mu                | Variational         | All       |
| C12   | No chaotic attractor                    | Topological         | All       |

---

## 6. Comparison with ED Mode 3

### 6.1 Locality

**ED:** Fully local. Every FS primitive at integer n depends only on the factorization of n. No integer's structure influences any other's.

**CH:** Fully local. Every channel depends on phi and its derivatives at each point. No nonlocal solve, no Green's function, no elliptic constraint.

Both architectures achieve the strongest form of FS locality. This is in contrast to NS, where the pressure channel introduces irreducible nonlocality. CH and ED occupy the same locality class.

### 6.2 Blowup Channels

**ED:** None. All ED quantities are finite for any finite argument. The architecture is unconditionally self-consistent.

**CH:** None. The fourth-order smoothing and Lyapunov structure guarantee global regularity in all dimensions d <= 3. The architecture is unconditionally self-consistent.

Both architectures pass the blowup criterion unconditionally. NS fails it in 3D (open blowup channel via vortex stretching).

### 6.3 Constraint Surface Closure

**ED:** Closed. All faces of the ED constraint surface are compact. Every ED inequality is tight, every identity is exact, and no quantity can escape to infinity.

**CH:** Closed. All faces of the CH constraint surface are sealed. The Lyapunov identity, H^1 bound, H^2 bound, and L^{infinity} bound form a closed chain of estimates with no open face. No quantity can escape to infinity.

Both architectures have *compact, closed* constraint surfaces. NS has an open face in 3D (the enstrophy gap).

### 6.4 Dynamics vs. Statics

**ED:** Static. The integers are fixed; the FS primitives describe a permanent structure. There is no time, no evolution, and no dynamics. The constraint surface is a *geometric object* (the skyline) that exists once and for all.

**CH:** Dynamic. The order parameter evolves in time under a gradient-flow PDE. The constraint surface is a *phase portrait* through which trajectories flow. But the gradient-flow structure imposes a strong ordering on the dynamics: every trajectory descends monotonically through the energy landscape toward a local minimum. The dynamics are *ordered* — no recurrence, no chaos, no oscillation.

The CH dynamics are the *closest to statics* that a nontrivial PDE can achieve: monotone, ordered, convergent. The gradient-flow structure converts the dynamical constraint surface into something approaching a static one — the energy landscape is fixed, and the dynamics are simply the descent through it.

### 6.5 Variational Structure

**ED:** No variational structure. The FS primitives are defined combinatorially, not variationally. There is no free energy, no action, no extremal principle.

**CH:** Entirely variational. The PDE is derived from a single functional F[phi] by taking the variational derivative and composing with the conserving Laplacian. Every structural feature of CH descends from F: the chemical potential, the flux, the dissipation rate, the equilibrium conditions, the interface profile, the surface tension.

This is the deepest architectural difference between ED and CH. ED's structure is *arithmetically generated* (from unique factorization). CH's structure is *variationally generated* (from a free-energy functional). Both generation mechanisms produce fully self-consistent architectures, but through completely different mechanisms.

### 6.6 CH as the Closest PDE Analogue to ED

Among all PDE architectures evaluated in the PDE Atlas, Cahn–Hilliard is the *closest analogue to ED*:

| Property                    | ED               | CH                 | NS                 |
|-----------------------------|------------------|--------------------|--------------------|
| Locality                    | Fully local      | Fully local        | Nonlocal (pressure)|
| Blowup channel              | None             | None               | A_stretch (3D)     |
| Constraint surface          | Closed           | Closed             | Open face (3D)     |
| Self-consistency            | Unconditional    | Unconditional      | Open (3D)          |
| Dimensional dependence      | None             | None (d <= 3)      | Critical (2D vs 3D)|
| Anomalies                   | None             | None               | Two (pressure, stretching) |
| Regularity                  | N/A (static)     | Unconditional      | 2D: yes; 3D: open  |
| Attractor                   | Static (Z)       | Compact, finite-dim| 2D: yes; 3D: open  |

CH matches ED on every FS-evaluable criterion except the fundamental static/dynamic distinction. It is a dynamical system that achieves the structural self-consistency of a static one — a *gradient-flow statics*.

---

*End of Mode 3: Channels → Constraint Surface. The AD Criteria and Verdict will follow in the final file.*
