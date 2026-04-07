# AD Evaluation: Cahn–Hilliard Equation — Mode 2: PDE → Extremal Dynamics

Allen Proxmire

April 2026

---

## Overview

Mode 2 moves from the static envelope (Mode 1) to the dynamics — the time-evolution behavior that the CH PDE forces, permits, or forbids. Where Mode 1 asked "what does the architecture allow?", Mode 2 asks "what does the architecture *do*?"

The CH Mode 2 analysis reveals a qualitatively different dynamical landscape from Navier–Stokes. NS dynamics are dominated by the competition between advection (nonlinear, destabilizing in 3D) and viscosity (linear, stabilizing), with an unresolved outcome. CH dynamics are dominated by the competition between the double-well reaction (nonlinear, locally destabilizing) and the biharmonic surface-tension term (linear, globally stabilizing), with a *resolved* outcome: the biharmonic always wins asymptotically, the free energy always decreases, and the system always converges to equilibrium. The architectural drama of CH is not whether the system survives (it always does) but *how* it reaches equilibrium — through what sequence of spinodal decomposition, interface formation, coarsening, and metastable trapping.

Throughout, we work with:

    partial_t phi = M Delta mu,    mu = phi^3 - phi - epsilon^2 Delta phi
    F[phi] = integral [f(phi) + (epsilon^2/2)|nabla phi|^2] dx,    f(phi) = (1/4)(phi^2 - 1)^2

on a bounded domain Omega subset R^d (d = 1, 2, 3) with constant mobility M > 0 and no-flux boundary conditions.

---

## 1. Free-Energy Dissipation and Gradient Flow

### 1.1 Derivation of the Lyapunov Identity

Compute the time derivative of the free energy:

    dF/dt = integral_Omega [f'(phi) partial_t phi + epsilon^2 nabla phi . nabla(partial_t phi)] dx

Integrate the second term by parts (using nabla phi . n = 0 on partial Omega):

    dF/dt = integral_Omega [f'(phi) - epsilon^2 Delta phi] partial_t phi dx = integral_Omega mu partial_t phi dx

Substitute partial_t phi = M Delta mu:

    dF/dt = integral_Omega mu M Delta mu dx

Integrate by parts (using nabla mu . n = 0 on partial Omega):

    dF/dt = -M integral_Omega |nabla mu|^2 dx                    ... (Lyapunov Identity)

This is the *exact Lyapunov dissipation identity* of the CH architecture. It holds with equality — not as an inequality derived from estimates, but as an algebraic consequence of the gradient-flow structure.

### 1.2 Properties of the Dissipation Channel

The dissipation rate D(t) = M ||nabla mu||_{L^2}^2 has the following structural properties:

**Strict monotonicity:** D(t) >= 0, with D(t) = 0 if and only if nabla mu = 0 on Omega, i.e., mu = const. The only states with zero dissipation are thermodynamic equilibria. Every non-equilibrium state dissipates energy strictly.

**Integrability:**

    M integral_0^{infinity} ||nabla mu(s)||^2 ds = F[phi_0] - lim_{t→∞} F[phi(t)] <= F[phi_0]

The total dissipation over all time is finite and bounded by the initial free energy. The dissipation budget is *fixed at birth* and is spent monotonically. The system cannot borrow, regenerate, or supplement its dissipation budget.

**Instantaneous dissipation rate:** The rate D(t) is not monotone in general — it can increase or decrease depending on the phase of the dynamics. During spinodal decomposition, D(t) increases (as gradients of mu steepen). During late-stage coarsening, D(t) decreases (as the system approaches equilibrium). The free energy F(t) is monotone; the dissipation rate D(t) is not.

### 1.3 Contrast with Navier–Stokes

The NS energy identity is:

    dE/dt = -nu ||nabla **u**||^2 + (**f**, **u**)

Key differences:

| Feature                    | Cahn–Hilliard              | Navier–Stokes              |
|----------------------------|----------------------------|----------------------------|
| Energy identity type       | Exact equality             | Exact for smooth solutions; inequality for weak |
| Forcing channel            | None (autonomous)          | Present (**f**)            |
| Energy direction           | Strictly non-increasing    | Can increase (via forcing) |
| Lyapunov functional        | Yes (F)                    | No (E is not Lyapunov when forced) |
| Limit cycles / chaos       | Forbidden                  | Permitted (when forced)    |
| Anomalous dissipation      | Impossible (identity exact)| Possible (for weak solutions in 3D) |

The CH architecture is *thermodynamically closed* — no energy enters or leaves. The NS architecture is *thermodynamically open* when forced. This makes CH's energy analysis strictly simpler and strictly more powerful than NS's.

### 1.4 H^{-1} Gradient-Flow Structure

The Lyapunov identity can be rewritten to reveal the H^{-1} gradient-flow structure. Define the H^{-1} inner product:

    (f, g)_{H^{-1}} = integral_Omega nabla(-Delta)^{-1} f . nabla(-Delta)^{-1} g dx

where (-Delta)^{-1} is the inverse Laplacian with zero-mean constraint. Then the CH equation is:

    partial_t phi = -M grad_{H^{-1}} F[phi]

The dynamics descend the steepest direction of F in the H^{-1} metric. The H^{-1} metric is the natural metric for conserved dynamics: it measures distances by the *transport cost* of redistributing mass, not the pointwise difference. This is why the CH coarsening dynamics are slow at large scales — the H^{-1} distance between two configurations differing at scale L grows as L^2, making large-scale rearrangements expensive.

---

## 2. Chemical Potential Dynamics

### 2.1 Derivation and Structure of mu

The chemical potential is the variational derivative of F:

    mu = delta F / delta phi = f'(phi) - epsilon^2 Delta phi = phi^3 - phi - epsilon^2 Delta phi

This decomposes into two contributions with opposite characters:

**Destabilizing contribution (double-well):**

    mu_R = f'(phi) = phi^3 - phi

For |phi| < 1/sqrt(3) (the spinodal region where f''(phi) < 0), the response mu_R is *decreasing* in phi: an increase in phi produces a decrease in chemical potential, which drives further accumulation. This is the thermodynamic instability — the "upside-down" curvature of the double-well creates a negative effective diffusivity.

**Stabilizing contribution (surface tension):**

    mu_S = -epsilon^2 Delta phi

This term penalizes spatial curvature in phi. It opposes sharp gradients and favors smooth fields. In Fourier space, mu_S(k) = epsilon^2 k^2 hat{phi}(k) — a contribution that grows quadratically with wavenumber, stabilizing high-frequency modes.

### 2.2 Slave Variable Character

The chemical potential mu is *entirely determined* by phi at each point and each instant:

    mu(x, t) = phi(x,t)^3 - phi(x,t) - epsilon^2 Delta phi(x,t)

It has no independent evolution equation, no initial condition, and no freedom beyond what phi dictates. Contrast with NS, where the pressure p is also a slave variable, but one determined *nonlocally* by a Poisson equation over the entire domain. The CH chemical potential is determined *locally* — the value of mu at x depends only on phi and Delta phi at x.

This locality of the slave variable is the structural reason that the CH architecture has no nonlocal channel. The NS architecture's nonlocality enters entirely through the pressure-determination step (the Poisson solve). CH avoids this by having a chemical potential that is a *pointwise* function of phi and its derivatives.

### 2.3 Chemical Potential as the Driving Field

The flux is **J** = -M nabla mu. Chemical potential gradients drive the mass flux: material flows from regions of high mu to regions of low mu. At equilibrium, mu = const — the chemical potential is uniform, and no flux exists.

The chemical potential plays the role that pressure plays in NS: it is the field whose gradients drive the dynamics. But unlike NS pressure (which enforces a constraint and does no work), the CH chemical potential *does* work: it mediates the conversion of free energy into dissipation. The chemical potential is simultaneously the *force* (nabla mu drives the flux) and the *accounting variable* (||nabla mu||^2 measures the dissipation rate).

---

## 3. Extremal Behaviors

The extremal behaviors are the dynamical configurations at the boundary of what the PDE permits.

### 3.1 Spinodal Decomposition (Fastest-Growing Mode)

**Regime:** Early time, phi near the unstable state phi ≈ phi-bar with f''(phi-bar) < 0.

Linearize the CH equation around a uniform state phi = phi-bar + delta phi:

    partial_t (delta phi) = M Delta [f''(phi-bar) delta phi - epsilon^2 Delta(delta phi)]

In Fourier space, each mode hat{delta phi}(k) evolves as:

    d/dt hat{delta phi}(k) = sigma(k) hat{delta phi}(k)

where the growth rate is:

    sigma(k) = -M k^2 [f''(phi-bar) + epsilon^2 k^2]

For f''(phi-bar) < 0 (spinodal region):
- Modes with k^2 < |f''(phi-bar)| / epsilon^2 are *unstable* (sigma > 0).
- Modes with k^2 > |f''(phi-bar)| / epsilon^2 are *stable* (sigma < 0).
- The most unstable mode: k_max^2 = |f''(phi-bar)| / (2 epsilon^2), with maximum growth rate sigma_max = M f''(phi-bar)^2 / (4 epsilon^2).

**Extremal spinodal behavior:** The fastest possible initial growth rate occurs at the hilltop phi-bar = 0 of the standard double-well, where f''(0) = -1:

    sigma_max = M / (4 epsilon^2),    k_max = 1 / (epsilon sqrt(2))

This sets the *architectural speed limit* for phase separation: the initial concentration fluctuations grow exponentially at rate M / (4 epsilon^2), with characteristic wavelength 2 pi epsilon sqrt(2). The growth rate diverges as epsilon → 0, reflecting the fact that the flat double-well (no gradient penalty) has infinite growth rate at all scales.

### 3.2 Interface Formation

**Regime:** Intermediate time, after spinodal decomposition.

As the linearized modes grow and saturate, the solution develops a pattern of phase-separated domains with phi ≈ +1 and phi ≈ -1, separated by diffuse interfaces. The interface profile converges to the equilibrium solution:

    phi_interface(z) = tanh(z / (epsilon sqrt(2)))

where z is the signed distance from the interface. This profile is the unique minimizer of the one-dimensional free energy subject to the boundary conditions phi → ±1 at z → ±infinity.

**Extremal interface behavior:** The sharpest possible interface has width O(epsilon). The architecture cannot produce interfaces thinner than this — the gradient penalty forbids it (F4 from Mode 1). The tanh profile is an *attractor* of the local dynamics: any interface profile evolves toward it on a fast time scale O(epsilon^2 / M).

### 3.3 Coarsening Dynamics (Domain Growth)

**Regime:** Late time, after interfaces have formed.

Once a pattern of phase-separated domains exists, the system evolves by *coarsening* — larger domains grow at the expense of smaller ones. The driving force is the reduction of total interfacial energy (surface tension times total interface area). Mass conservation forces coarsening to proceed by diffusion of material through the bulk, from high-curvature (small) domains to low-curvature (large) domains.

The characteristic domain size L(t) grows in time. Two coarsening regimes exist:

**Regime A: Diffusion-limited coarsening (Lifshitz–Slyozov–Wagner)**

For constant mobility M, the rate-limiting step is bulk diffusion of phi between domains. The scaling argument:

- Driving force: Gibbs–Thomson effect gives a chemical potential difference delta mu ~ sigma / L ~ epsilon / L between domains of different curvature.
- Flux: J ~ M delta mu / L ~ M epsilon / L^2.
- Volume change rate: dV/dt ~ J * A ~ (M epsilon / L^2) * L^{d-1}.
- For d = 3: dL^3/dt ~ M epsilon / L^2 * L^2 = M epsilon, so L^3 ~ M epsilon t.

**Extremal coarsening rate (constant mobility):**

    L(t) ~ (M epsilon t)^{1/3}                                    ... (LSW law)

**Regime B: Surface-diffusion-limited coarsening (degenerate mobility)**

For M(phi) = 1 - phi^2 (vanishing at the pure phases), diffusion is restricted to the interface region of width O(epsilon). The effective bulk mobility is M_eff ~ M_0 epsilon / L, introducing an additional factor:

    L(t) ~ (M_0 epsilon^2 t)^{1/4}                                ... (surface diffusion law)

**Extremal coarsening rate (degenerate mobility):**

    L(t) ~ t^{1/4}

Both coarsening laws are *upper bounds* on the speed of domain growth. The Kohn–Otto rigorous bounds (Mode 1, E-Bound 7) confirm that coarsening cannot exceed these rates.

### 3.4 Metastability and Slow Manifold Dynamics

**Regime:** Late time, near (but not at) equilibrium.

The coarsening process is not continuous — it is punctuated by long *metastable plateaus* during which the solution sits near a local minimum of the free energy, followed by rapid *transition events* (droplet disappearance, domain merging) that reduce the number of interfaces.

**Metastable trapping:** A configuration with N interfaces is approximately stationary if all interfaces are widely separated (inter-interface distance >> epsilon). The free energy landscape near such a configuration has local minima separated by energy barriers. The CH gradient flow descends smoothly but can spend exponentially long times (in the inter-interface distance) near a local minimum before crossing the barrier to a lower-energy state.

**Exponential time scales:** For a 1D domain with two interfaces separated by distance L, the time to merge scales as:

    T_merge ~ exp(C L / epsilon)

This exponential dependence on L/epsilon is a *structural feature* of the CH architecture: the energy barrier between the N-interface and (N-2)-interface states grows linearly with L/epsilon, and the gradient flow crosses it at a rate exponential in the barrier height.

**The slow manifold:** The set of configurations with well-separated interfaces of width O(epsilon) forms an approximate *slow manifold* in the infinite-dimensional phase space. The fast dynamics (interface formation, local relaxation) drive the solution onto this manifold in time O(epsilon^2/M). The slow dynamics (coarsening, metastable transitions) then govern the long-time evolution *on* the manifold.

The slow manifold can be parameterized by the *interface positions* {x_1, ..., x_N}. The CH dynamics on the slow manifold reduce to an ODE system for the interface positions — a finite-dimensional reduction of the infinite-dimensional PDE. This reduction is the CH analogue of the NS global attractor: the architecture compresses its infinite-dimensional dynamics to a finite-dimensional core.

### 3.5 Absence of Finite-Time Blowup

**All regimes, all dimensions.**

The CH architecture has *no finite-time blowup channel*. The structural reasons:

1. **Lyapunov functional:** F[phi(t)] is bounded below and monotone decreasing, so it remains finite for all time.
2. **Energy controls H^1:** The bound ||nabla phi||_{L^2}^2 <= 2F[phi_0]/epsilon^2 gives uniform-in-time H^1 control.
3. **Fourth-order smoothing:** The biharmonic term -M epsilon^2 Delta^2 phi provides instantaneous regularization at rate k^4, overwhelming the cubic nonlinearity (which grows at rate k^2 in Fourier space) at high wavenumbers.
4. **Subcritical nonlinearity:** The cubic term phi^3 is subcritical relative to H^2(R^d) for d <= 3 — the Sobolev embedding H^2 hookrightarrow L^{infinity} holds in d <= 3, so H^2 control implies L^{infinity} control, and the bootstrap closes.

**Comparison with NS:** The NS architecture has a blowup channel in 3D because the advection nonlinearity (**u** . nabla)**u** is *critical* relative to the second-order viscous smoothing in the energy space. The CH architecture avoids this because the cubic nonlinearity f'(phi) is *subcritical* relative to the fourth-order biharmonic smoothing. The extra two orders of smoothing provide a decisive margin.

---

## 4. Universal Inequalities

The following inequalities hold for every admissible CH evolution.

---

**U1. Free-Energy Dissipation Identity**

    F[phi(t)] + M integral_0^t ||nabla mu(s)||^2 ds = F[phi_0]    for all t >= 0

Exact identity (not an inequality). The total energy accounting is closed with no gap.

**Structural role:** Primary accounting identity. Determines the total dissipation budget and guarantees convergence to equilibrium.

---

**U2. H^1 Control from Free Energy**

    ||nabla phi(t)||_{L^2}^2 <= 2 F[phi_0] / epsilon^2    for all t >= 0

The gradient energy term in F provides uniform-in-time control of the H^1 seminorm.

**Structural role:** First rung of the regularity bootstrap. Converts energy control into gradient control without any dimensional restriction.

---

**U3. L^{infinity} Control via Fourth-Order Smoothing**

For t > 0 (instantaneous regularization):

    ||phi(t)||_{L^{infinity}} <= C(F[phi_0], epsilon, M, Omega, t_0)    for all t >= t_0 > 0

The biharmonic smoothing provides H^2 regularity for t > 0, and Sobolev embedding (H^2 hookrightarrow L^{infinity} for d <= 3) gives L^{infinity} control.

**Structural role:** Closes the regularity bootstrap unconditionally. This is the inequality that makes the CH envelope closed in all dimensions — the fourth-order smoothing controls the nonlinearity.

**Note:** The bound depends on epsilon — it may degenerate as epsilon → 0 (the sharp-interface limit). The L^{infinity} bound is *not uniform in epsilon*.

---

**U4. Coarsening Rate Bounds (Kohn–Otto)**

For constant mobility:

    F[phi(t)] >= C t^{-1/3}    for t >> 1

For degenerate mobility M(phi) = 1 - phi^2:

    F[phi(t)] >= C t^{-1/4}    for t >> 1

These are *rigorous lower bounds* on the free energy (equivalently, upper bounds on the coarsening rate). The proofs use optimal transport arguments and interpolation inequalities.

**Structural role:** Constrain the long-time dynamics from above. Coarsening cannot be arbitrarily fast — the architecture imposes a speed limit on domain growth.

---

**U5. Chemical Potential Regularity**

For t > 0:

    ||mu(t)||_{H^1} <= C(F[phi_0], epsilon, M, Omega, t_0)    for all t >= t_0 > 0

The chemical potential inherits regularity from phi through the relation mu = f'(phi) - epsilon^2 Delta phi. Since phi in H^2 for t > 0, and f' is smooth, mu is in H^1 (at minimum). Higher regularity follows by bootstrapping.

**Structural role:** Ensures that the dissipation density M |nabla mu|^2 is integrable and that the flux **J** = -M nabla mu is well-defined.

---

**U6. Mass Conservation Constraint**

    integral_Omega phi(x, t) dx = integral_Omega phi_0(x) dx =: m |Omega|    for all t >= 0

where m = phi-bar is the conserved mean. This is an exact equality, not an inequality.

**Structural role:** Constrains the dynamics to a hyperplane in function space. The evolution of phi is confined to the affine subspace { phi : integral phi = m |Omega| }. This constraint interacts with the free energy to determine which equilibrium states are accessible: only those with the correct total mass.

---

**U7. Interface Width Lower Bound**

In the sharp-interface regime (well-separated phases with phi ≈ ±1):

    (Interface width) >= C epsilon

for a universal constant C > 0. Interfaces cannot be thinner than O(epsilon). This bound follows from the balance between the double-well driving (which favors sharp transitions) and the gradient penalty (which penalizes them).

More precisely: the energy per unit interface area satisfies

    sigma >= sigma_0 epsilon

where sigma_0 = 2 sqrt(2) / 3 is the optimal surface tension coefficient, with equality for the tanh profile. Any interface thinner than O(epsilon) would have surface tension strictly greater than sigma_0 epsilon and is dynamically unstable — it relaxes to the equilibrium width.

**Structural role:** Sets the *architectural resolution limit*. No structure finer than O(epsilon) can persist in the CH dynamics. This is the analogue of the NS Kolmogorov scale, but the CH scale is an *architectural constant* (set by epsilon), not a dynamical quantity (set by the flow state).

---

### Universal Inequality Summary

| Label | Inequality                          | Type            | Status        | Role                        |
|-------|--------------------------------------|-----------------|---------------|-----------------------------|
| U1    | Free-energy dissipation identity     | Exact equality  | Unconditional | Primary accounting          |
| U2    | H^1 control from energy             | Inequality      | Unconditional | Regularity (first rung)     |
| U3    | L^{infinity} via 4th-order smoothing| Inequality      | Unconditional | Regularity (closure)        |
| U4    | Coarsening rate bounds              | Lower bound on F| Unconditional | Coarsening speed limit      |
| U5    | Chemical potential regularity       | Inequality      | Unconditional | Dissipation well-definedness|
| U6    | Mass conservation                   | Exact equality  | Unconditional | State-space constraint      |
| U7    | Interface width lower bound         | Lower bound     | Unconditional | Architectural resolution    |

**All seven universal inequalities are unconditional.** None requires a dimensional restriction, a smallness condition, or a conditional regularity hypothesis. This is the CH architecture's defining feature at the Mode 2 level: every inequality closes, in every dimension, without qualification.

---

## 5. Attractors and Long-Time Behavior

### 5.1 Global Attractor (All Dimensions)

The CH equation on a bounded domain with no-flux boundary conditions possesses a *global attractor* A: a compact, connected, finite-dimensional invariant set in H^1(Omega) that attracts all trajectories.

**Existence proof sketch:**
1. The dissipation identity (U1) and energy lower bound (E3 from Mode 1) provide an *absorbing ball* in H^1: every trajectory enters the ball { ||nabla phi||_{L^2} <= R } for R^2 = 2F[phi_0]/epsilon^2 — but since F decreases, the ball with R^2 = 2F_max/epsilon^2 absorbs all trajectories regardless of initial data.
2. The fourth-order smoothing provides *compactness*: the solution operator maps H^1 to H^2 for t > 0, and the embedding H^2 hookrightarrow H^1 is compact on bounded domains.
3. Existence of the global attractor follows from the standard Ladyzhenskaya–Temam theory for dissipative semigroups.

**Dimension bound:** The Hausdorff dimension of A is bounded by:

    dim_H(A) <= C(epsilon, M, |Omega|, d)

The dimension depends on epsilon — as epsilon → 0, the attractor dimension grows (reflecting the increasing number of metastable states with many interfaces). The attractor in the sharp-interface limit is *high-dimensional* but still finite.

**Structure:** The attractor contains:
- All stationary solutions (equilibria with mu = const).
- All heteroclinic connections between equilibria (coarsening trajectories).
- The unstable manifolds of unstable equilibria (saddle points of F on the mass-constrained function space).

The attractor is the *complete diagram* of the long-time dynamics — every possible long-time behavior is represented on A.

**Comparison with NS:** The NS architecture has a global attractor only in 2D (unconditionally). In 3D, the existence of a classical attractor is conditional on regularity. The CH architecture has a global attractor *unconditionally* in all dimensions. This reflects the CH envelope's complete closure.

### 5.2 The Slow Manifold of Near-Equilibrium States

The global attractor has an internal hierarchy of time scales:

**Fast dynamics (t ~ epsilon^2 / M):** Relaxation of interface profiles to the equilibrium tanh shape. Internal adjustment of the diffuse interface. These dynamics are essentially *local* — each interface relaxes independently of the others.

**Intermediate dynamics (t ~ L^3 / (M epsilon) for constant mobility):** Coarsening by Ostwald ripening or coalescence. Smaller domains shrink and disappear; larger domains grow. The number of interfaces decreases. These dynamics are *global* — they involve diffusion of material across the bulk between distant interfaces.

**Slow dynamics (t ~ exp(C L / epsilon)):** Metastable transitions. Widely separated interfaces interact exponentially weakly. The system can spend exponentially long times near a metastable configuration before a transition event (interface annihilation, domain merging) occurs.

The slow manifold M_N of configurations with N well-separated interfaces is an N-dimensional (approximately) invariant manifold in the infinite-dimensional phase space. The CH dynamics on M_N are governed by an *effective ODE* for the interface positions:

    dx_i/dt = f_i(x_1, ..., x_N; epsilon, M)

where the right-hand side involves exponentially small interaction terms between neighboring interfaces. This is the CH architecture's version of dimensional reduction: the PDE compresses to an ODE on the slow manifold.

### 5.3 Coarsening Regimes

**Regime A: Spinodal decomposition (early time)**

Characterized by exponential growth of linear modes. The domain pattern emerges with a characteristic wavelength ~ epsilon. Free energy decreases rapidly as the system moves from the unstable homogeneous state to a phase-separated pattern. Duration: t ~ epsilon^2 / M (a few e-folding times of the fastest mode).

**Regime B: Interface sharpening (intermediate time)**

The initially sinusoidal concentration pattern sharpens into well-defined interfaces with the tanh profile. Bulk regions approach phi ≈ ±1. Free energy continues to decrease, mainly through reduction of the bulk free-energy contribution. Duration: t ~ epsilon^2 / M to t ~ (L_0)^3 / (M epsilon), where L_0 is the initial domain size.

**Regime C: Diffusion-limited coarsening (late time, constant mobility)**

Domain growth at rate L(t) ~ t^{1/3}. Free energy decays as F(t) ~ t^{-1/3} (in d = 3) or F(t) ~ t^{-(d-1)/3} (general d). The dynamics are self-similar: the domain size distribution, rescaled by L(t), approaches a universal form (the LSW distribution in the mean-field limit).

**Regime D: Surface-diffusion-limited coarsening (late time, degenerate mobility)**

Domain growth at rate L(t) ~ t^{1/4}. Slower than Regime C because the degenerate mobility restricts diffusion to the interfacial region. Free energy decays as F(t) ~ t^{-1/4} (in d = 3).

**Regime E: Metastable trapping (very late time)**

A small number of domains remain, widely separated. The coarsening rate slows exponentially as inter-domain distances grow. The system approaches a local minimum of F, separated from the global minimum by energy barriers that grow with L/epsilon. Final convergence to the global minimum (a single domain or two half-domains, depending on mass constraint) may take exponentially long time.

### 5.4 Exponential Convergence Near Equilibrium

Near a non-degenerate local minimum phi_* of F (on the mass-constrained function space), the linearized CH operator

    L_* = M Delta [f''(phi_*) - epsilon^2 Delta]

has a discrete spectrum with a spectral gap lambda_1 > 0 (the smallest nonzero eigenvalue, restricting to the mass-conserving subspace).

Solutions near phi_* satisfy:

    ||phi(t) - phi_*||_{H^1} <= C exp(-lambda_1 t)

The final approach to equilibrium is exponential, with rate determined by the curvature of F at the minimum and the domain geometry.

**Spectral gap dependence:** The gap lambda_1 depends on:
- The domain size |Omega| (larger domains have smaller gaps).
- The parameter epsilon (smaller epsilon produces a more complex energy landscape with smaller gaps near metastable states).
- The specific equilibrium phi_* (different stationary solutions have different spectral gaps).

The *global* spectral gap (across all equilibria) may be exponentially small in |Omega| / epsilon, reflecting the exponentially long metastable transitions discussed in Section 3.4.

---

## 6. Comparison with ED Mode 2

### 6.1 Static vs. Dynamical

**ED:** The FS/ED architecture is static. The integers do not evolve in time. The FS primitives describe the multiplicative structure of Z as a fixed geometric object. There is no PDE, no time derivative, no dynamics, and no dissipation. The "extremal behaviors" of ED are extremal properties of arithmetic functions (maxima and minima of prime gaps, extremal values of the divisor function, etc.) — not dynamical extrema.

**CH:** The CH architecture is dynamical. The order parameter phi(x, t) evolves under a fourth-order parabolic PDE. The dynamics are driven by the gradient flow of a free-energy functional. The extremal behaviors (spinodal decomposition, coarsening, metastability) are genuinely dynamical phenomena — they describe processes that unfold in time.

### 6.2 Lyapunov Structure vs. No Dissipation

**ED:** No dissipation, no Lyapunov functional, no energy landscape. The ED architecture has no concept of "energy" or "equilibrium" — the integers are not in any state that could be energetically favored or disfavored.

**CH:** The free-energy functional F[phi] is a Lyapunov functional that monotonically decreases along every trajectory. The CH architecture has a well-defined energy landscape with minima (equilibria), saddle points (metastable states), and a gradient-flow dynamics that descends this landscape. The Lyapunov structure is *exact* — it holds for all solutions with equality, not as an approximation.

### 6.3 Blowup Channels

**ED:** No blowup channel. Every ED quantity is finite for any finite argument. The integers are exactly defined and never blow up.

**CH:** No blowup channel. The Lyapunov structure (F bounded below, F decreasing) and the fourth-order smoothing (H^2 control in all dimensions) ensure global regularity. The CH architecture shares ED's property of *unconditional self-consistency* — both architectures survive their own dynamics (or, in ED's case, have no dynamics to survive).

### 6.4 Locality

**ED:** Fully local. Every FS primitive at integer n depends only on the factorization of n.

**CH:** Fully local. The chemical potential mu at x depends only on phi and Delta phi at x. There is no nonlocal channel — no Poisson equation, no Green's function, no instantaneous global coupling. CH shares ED's complete locality, in contrast to NS (which has the nonlocal pressure channel).

### 6.5 Attractor Structure

**ED:** The ED "attractor" is the arithmetic structure of Z itself — the unique, fixed, deterministic object defined by the axioms of arithmetic. There is no dynamics and no convergence; the attractor simply *is*.

**CH:** The CH attractor is a compact, finite-dimensional subset of function space containing all equilibria and their connecting orbits. Solutions converge to the attractor, with exponential rate near equilibria and algebraic rate during coarsening. The attractor is *dynamically realized* — solutions approach it over time.

### 6.6 Summary Table

| Feature                    | ED                   | CH                           |
|----------------------------|----------------------|------------------------------|
| Dynamics                   | None (static)        | Gradient-flow PDE            |
| Lyapunov functional        | No                   | Yes (F, exact identity)      |
| Blowup channel             | None                 | None                         |
| Locality                   | Fully local          | Fully local                  |
| Attractor                  | Fixed (arithmetic)   | Dynamic (finite-dim compact) |
| Dissipation                | None                 | Exact, monotone, finite budget|
| Extremal behavior          | Arithmetic extrema   | Spinodal, coarsening, metastability |
| Self-consistency           | Unconditional        | Unconditional                |
| Dimensional dependence     | None                 | None (closed in all d)       |

---

*End of Mode 2: PDE → Extremal Dynamics. Mode 3 (Channels → Constraint Surface) will follow in a subsequent file.*
