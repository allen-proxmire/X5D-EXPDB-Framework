# AD Evaluation: Hamilton–Jacobi Equation — Mode 2: PDE → Extremal Dynamics

Allen Proxmire

April 2026

---

## Overview

Mode 2 moves from the static envelope to the dynamics. The HJ dynamical landscape is *structurally inverted* relative to every parabolic architecture in the Atlas: where parabolic dynamics smooth, HJ dynamics steepen; where parabolic dynamics gain regularity, HJ dynamics lose it; where parabolic dynamics converge to equilibria, HJ dynamics develop shocks and then settle into a post-shock regime described by the Hopf–Lax variational formula. The HJ architecture demonstrates the *minimum dynamical content* that produces finite-time singularity from smooth data — one nonlinear first-order term, no diffusion, and the inevitable consequence of characteristic crossing.

Throughout:

    partial_t u + H(nabla u) = 0,    H(p) = |p|^2 / 2    (quadratic Hamiltonian)

on R^d, with Lipschitz initial data u_0. All solutions are viscosity solutions.

---

## 1. Fundamental Time and Length Scales

### 1.1 The Shock-Formation Time Scale

The HJ architecture has a single fundamental time scale: the *shock-formation time* T*, determined by the initial concavity of u_0.

For H(p) = |p|^2/2 in one dimension:

    T* = 1 / max_x (-u_0''(x))

In d dimensions, the shock-formation time is determined by the most negative eigenvalue of the Hessian D^2 u_0:

    T* = 1 / max_x (lambda_max(-D^2 u_0(x)))

where lambda_max(-D^2 u_0) is the largest eigenvalue of -D^2 u_0 (the maximum concavity). The shock forms at the point where the initial data is most concave.

**Comparison with other time scales:**

| Architecture | Fundamental Time Scale          | Set By                       |
|-------------|----------------------------------|------------------------------|
| **HJ**      | **T* = 1/max(-u_0'')**          | **Initial concavity**        |
| FP          | t_D = L^2/D, t_T = L/\|b\|     | Diffusion + drift parameters |
| PME         | t ~ L^2 / u^{m-1}               | Density + degeneracy         |
| AC          | t ~ 1/M (bulk), t ~ R^2/(M eps) (interface) | Mobility + epsilon |
| NS          | t ~ L^2/nu (viscous), t ~ L/U (advective) | Viscosity + velocity |
| MCF         | t ~ R^2                          | Curvature radius             |

The HJ time scale is unique: it depends on the *second derivative of the initial data*, not on any constitutive parameter (no epsilon, no nu, no D, no m). The HJ architecture has no constitutive parameters — the time scale is set entirely by the geometry of the initial condition. This is the temporal expression of the HJ's parameter-free character (shared with MCF).

### 1.2 Finite-Speed Propagation via Characteristics

The characteristic equations for H(p) = |p|^2/2:

    dx/dt = nabla u(x(0), 0) = p_0    (constant velocity along each characteristic)
    du/dt = |p_0|^2 / 2                 (quadratic growth of u along each characteristic)

Each characteristic is a *straight line* in the (x, t) plane:

    x(t) = x_0 + t nabla u_0(x_0)

The propagation speed is |nabla u_0(x_0)| — the initial gradient magnitude at the starting point. Information from (x_0, 0) reaches (x, t) if and only if x = x_0 + t nabla u_0(x_0).

**The domain of dependence** of (x, t) is:

    D(x, t) = { y : x = y + t nabla u_0(y) }

This is a single point (when characteristics are non-crossing) or multiple points (when characteristics have crossed — the post-shock regime). In the pre-shock regime, the solution is uniquely determined by tracing back a single characteristic; in the post-shock regime, the Hopf–Lax formula selects the *minimum-cost* path.

### 1.3 Three Dynamical Regimes

**Regime (A): Smooth (t < T*, before gradient blowup)**

The classical solution exists and is smooth. Characteristics do not cross. The solution is given by the classical method of characteristics:

    u(x, t) = u_0(x_0) + t |nabla u_0(x_0)|^2 / 2

where x_0 is the unique root of x = x_0 + t nabla u_0(x_0). The gradient nabla u(x, t) varies smoothly and *steepens* over time: concave regions of u become more concave, approaching a discontinuity.

**Properties in Regime A:**
- u is C^{infinity} (as smooth as u_0).
- The gradient evolves according to nabla u(x, t) = nabla u_0(x_0) (constant along characteristics, but the mapping x → x_0 contracts in concave regions, steepening the gradient in Eulerian coordinates).
- The solution is unique (classical).
- Energy-type quantities may increase or decrease — there is no Lyapunov monotonicity.

**Regime (B): Pre-Shock (t → T*, characteristics converging)**

As t approaches T*, the characteristics converge at a point (or a curve/surface in higher dimensions). The gradient steepens without bound:

    |nabla^2 u(x, t)| ~ 1/(T* - t)    as t → T*

The second derivative of u blows up at rate 1/(T* - t) — the standard self-similar blowup rate for first-order quasilinear equations. The gradient itself remains bounded (the Lipschitz norm is non-increasing, E2 from Mode 1), but its spatial variation becomes infinite.

**Properties in Regime B:**
- u remains Lipschitz (nabla u bounded in L^{infinity}).
- D^2 u blows up (the gradient becomes discontinuous at T*).
- The solution is still classical but is approaching the breakdown threshold.
- The blowup is *certain and predictable*: the time T* and the location x* are determined by the initial data.

**Regime (C): Post-Shock (t > T*, viscosity solution)**

After T*, the classical solution ceases to exist (nabla u has a jump discontinuity). The viscosity solution provides the unique continuation:

    u(x, t) = inf_y { u_0(y) + |x - y|^2 / (2t) }    (Hopf–Lax)

The viscosity solution is:
- Lipschitz continuous (u is continuous, nabla u has bounded L^{infinity} norm).
- Semiconcave (one-sided second-order control: D^2 u <= C/t in the distributional sense).
- *Not* C^1 at shock points (nabla u has jump discontinuities).
- Unique (by the comparison principle).

**Properties in Regime C:**
- The shock set { x : nabla u is discontinuous } is a lower-dimensional set (a curve in 2D, a surface in 3D) that evolves in time.
- Away from the shock set, u is smooth (classical solution applies between shocks).
- The shock set *grows* over time as more characteristics cross and new shocks form.
- In the long time limit (t → infinity), the solution simplifies: the Hopf–Lax formula produces an increasingly smooth (semiconcave) profile.

### 1.4 Contrast with Other Architectures

| Feature                    | HJ                        | FP/PME/TFE               | MCF                      | NS                       |
|----------------------------|---------------------------|---------------------------|---------------------------|--------------------------|
| Regime sequence            | Smooth → Pre-shock → Post-shock | Smooth → Equilibrium | Smooth → Singularity → Extinction | Smooth → ???(3D)  |
| Regularity trend           | *Decreases* (C^inf → Lip.)| *Increases* (→ C^inf)    | Decreases (→ curvature blowup)| Open (3D)          |
| Singularity mechanism      | Characteristic crossing   | None (smoothing prevents) | Curvature concentration   | Vortex stretching (open) |
| Post-singularity           | Viscosity solution (unique)| N/A (no singularity)    | Surgery/level-set (unique)| Open                     |
| Long-time behavior         | Hopf–Lax (variational)   | Equilibrium (PME: Barenblatt, FP: Gibbs)| Extinction | Attractor (2D) / open (3D)|

The HJ regime sequence is the *reverse* of the parabolic sequence: parabolic PDEs start rough and become smooth; HJ starts smooth and becomes rough. The singularity is in the *forward* direction for HJ and in the *backward* direction for parabolic PDEs (if one were to reverse time in a parabolic PDE, one would get the ill-posed backward heat equation — the parabolic analogue of HJ's forward singularity).

---

## 2. Extremal Behaviors

### E1. Finite-Time Gradient Blowup (Shock Formation)

For generic Lipschitz initial data u_0 with non-trivial concavity (D^2 u_0 has a negative eigenvalue somewhere):

    sup_x |D^2 u(x, t)| → infinity    as t → T*

The *second derivative* of u blows up in finite time. The first derivative (gradient) remains bounded — the Lipschitz constant is non-increasing (E2 from Mode 1). The solution u itself remains continuous and bounded. The singularity is *purely in the regularity*: the function u degrades from C^2 to merely Lipschitz, but its values and gradients remain finite.

**Comparison with other singularities:**
- MCF: curvature (second fundamental form) blows up → the *surface* becomes singular.
- NS (3D): vorticity might blow up → the *velocity gradients* become singular.
- HJ: D^2 u blows up → the *second derivatives* become singular, producing a gradient discontinuity.
- PME/AC/CH/FP: no singularity (smoothing prevents blowup).

### E2. Characteristic Crossing (Multi-Valued Classical Solution)

At the shock time T*, two (or more) characteristics arrive at the same point with different gradient values. The classical solution becomes *multi-valued*: two different values of nabla u are assigned to the same point. The multi-valuedness is the *geometric* manifestation of the shock.

In the (x, t, u) space, the graph of u develops a *fold* — a region where the graph turns over and becomes multi-sheeted. The viscosity solution resolves this by selecting the *lower sheet* (the minimum value), which corresponds to the infimum in the Hopf–Lax formula.

**Geometric interpretation:** The characteristics form a *caustic* — a curve (in 1+1 dimensions) or a surface (in higher dimensions) where characteristics cross. The caustic is the *envelope* of the family of characteristics. Inside the caustic, the classical solution is multi-valued; outside, it is single-valued.

### E3. Viscosity-Solution Selection (Unique Continuation)

The viscosity-solution framework resolves the multi-valuedness by selecting the *minimum-cost* branch:

    u(x, t) = inf_y { u_0(y) + |x - y|^2 / (2t) } = minimum over all paths

This selection is:
- **Unique:** For convex H, the viscosity solution is unique (comparison principle).
- **Physical:** The selected solution is the limit of vanishing-viscosity approximations (the solution that would survive infinitesimal diffusion).
- **Variational:** The selected solution minimizes the action integral along characteristics.
- **Entropic:** The selected solution satisfies the entropy condition (information loss at shocks).

### E4. Hopf–Lax Minimization as Variational Attractor

For large t, the Hopf–Lax formula:

    u(x, t) = inf_y { u_0(y) + |x - y|^2 / (2t) }

becomes dominated by the *global minimum* of u_0 plus a quadratic correction:

    u(x, t) ≈ min u_0 + |x - x_*|^2 / (2t)    as t → infinity

where x_* = argmin u_0. The solution converges to a *paraboloid* centered at the minimizer of u_0. This paraboloid is the long-time *variational attractor* of the HJ dynamics.

**Comparison with other attractors:**
- FP: Gibbs–Boltzmann rho_eq = Z^{-1} exp(-V/sigma^2) — an *exponential* profile determined by the potential.
- PME: Barenblatt B(x, t; M) — a *power-law* profile determined by the mass.
- MCF: Round sphere S^d — a *geometric* shape determined by the area.
- **HJ: Paraboloid u ~ |x - x_*|^2 / (2t)** — a *quadratic* profile determined by the minimum of u_0.

The HJ attractor is *variational*: it is the minimum-cost envelope, not a function-space equilibrium (FP, PME) or a geometric shape (MCF). It is the *simplest* attractor in the Atlas — a single paraboloid.

### E5. Semiconcavity (One-Sided Regularity)

For t > 0, the viscosity solution satisfies:

    D^2 u(x, t) <= (C / t) I    (in the distributional sense)

The Hessian of u is bounded from above (by C/t times the identity matrix). This is *one-sided*: u can be as convex as it wants (D^2 u can be large and positive) but cannot be too concave (D^2 u is bounded above). This one-sided control is the *maximum regularity* the HJ can provide — it is strictly weaker than the C^{infinity} smoothing of parabolic equations but strictly stronger than mere Lipschitz continuity.

**Physical meaning:** Semiconcavity means that the solution is "at most as curved as a paraboloid from above." The shocks (gradient discontinuities) are all *concave-type* — the gradient jumps downward, not upward. This is the geometric content of the entropy condition.

### E6. Finite-Speed Propagation (Hyperbolic Cone)

The domain of dependence of (x, t) is contained in the cone:

    { y : |y - x| <= C t }

where C = ||nabla u_0||_{L^{infinity}} is the maximum initial gradient. Information travels at speed at most C — the *maximum characteristic speed*.

The domain of *influence* of (y, 0) is the forward cone:

    { (x, t) : |x - y| <= C t }

These cones are *sharp*: for the quadratic Hamiltonian, the propagation speed is exactly |nabla u_0(y)| along the characteristic from y.

### E7. Oleinik One-Sided Gradient Bound

In one dimension, for H(p) = p^2/2:

    u_x(x, t) <= 1/t    for all x, for t > 0

This is a *universal* bound: it depends only on t, not on the initial data. It is the strongest one-sided estimate in the HJ theory:
- The positive part of nabla u decays universally as 1/t.
- The negative part of nabla u can be arbitrarily large (at shocks).
- The bound is *sharp*: it is achieved by the solution with u_0(x) = -|x|.

In d dimensions, the analogue is the semiconcavity estimate (E5): D^2 u <= C/t.

The Oleinik bound is the HJ's *substitute for parabolic smoothing*: it provides a universal, time-dependent regularization estimate without any diffusion. The regularity comes not from smoothing but from the *variational selection principle* — the Hopf–Lax infimum automatically selects the most regular (most concave) branch.

### E8. No Oscillations, No Chaos

The HJ dynamics are *monotone* (comparison principle: u_0 <= v_0 implies u(t) <= v(t)) and *contractive* (L^{infinity} contraction: ||u(t) - v(t)||_{L^inf} <= ||u_0 - v_0||_{L^inf}). These properties forbid:

- Limit cycles (the L^{infinity} distance between any two solutions is non-increasing — orbits cannot recur).
- Chaos (the L^{infinity} contraction gives Lipschitz stability — no sensitive dependence on initial conditions).
- Oscillations (the comparison principle implies order-preservation — the dynamics are monotone).

The HJ semigroup S_t is a *monotone L^{infinity}-contraction* — the same structural category as the PME semigroup (monotone L^1-contraction) but in a different metric. Both are fundamentally incompatible with oscillatory or chaotic behavior.

---

## 3. Universal Inequalities

---

**U1. Comparison Principle**

    u_0 <= v_0 (a.e.)  =>  u(t) <= v(t) (a.e.)    for all t >= 0

Order-preservation. The foundation of uniqueness and the structural backbone of the viscosity-solution theory.

---

**U2. L^{infinity} Contraction**

    ||u(t) - v(t)||_{L^{infinity}} <= ||u_0 - v_0||_{L^{infinity}}    for all t >= 0

The viscosity-solution semigroup is a contraction on L^{infinity}. Two solutions starting close remain close forever. Implies uniqueness and Lipschitz continuous dependence.

---

**U3. Lipschitz Propagation**

    ||nabla u(t)||_{L^{infinity}} <= ||nabla u_0||_{L^{infinity}}    for all t >= 0

The Lipschitz constant is non-increasing. The gradient magnitude (in the L^{infinity} sense) never exceeds its initial value. Shocks *decrease* the effective Lipschitz constant by clipping the steepest parts of the gradient.

---

**U4. Semiconcavity Estimate**

    D^2 u(x, t) <= (C / t) I    for t > 0    (distributional sense)

One-sided Hessian control. The solution becomes semiconcave instantaneously for t > 0, with semiconcavity constant improving as 1/t.

---

**U5. Finite-Speed Propagation Bound**

    u(x, t) depends only on u_0(y) with |y - x| <= ||nabla u_0||_{L^inf} t

Hyperbolic cone of dependence. Information travels at speed at most ||nabla u_0||_{L^{infinity}}.

---

**U6. Hopf–Lax Variational Inequality**

    u(x, t) = inf_y { u_0(y) + |x - y|^2 / (2t) }

The viscosity solution equals the infimal convolution of u_0 with the quadratic cost. This is simultaneously an *explicit formula* (giving the solution directly) and an *inequality* (u(x, t) <= u_0(y) + |x - y|^2/(2t) for every y, with equality for the optimal y).

---

**U7. Oleinik One-Sided Gradient Bound (1D)**

    partial_x u(x, t) <= 1/t    for all x, t > 0

Universal: independent of initial data. The positive gradient decays at rate 1/t. This is the sharpest universal regularization estimate for HJ — the first-order analogue of the parabolic smoothing estimate ||nabla u(t)|| <= C/sqrt(t).

---

**U8. Shock-Formation Time Estimate**

    T* = 1 / max_x lambda_max(-D^2 u_0(x))

The shock time is determined by the maximum initial concavity. Sharp: achieved by the solution whose initial Hessian is -alpha I at the concavity maximum.

---

**U9. Stability Under Sup-Convolution**

    u^epsilon = sup_y { u(y) - |x - y|^2 / (2 epsilon) } → u uniformly as epsilon → 0

The viscosity solution is stable under regularization by sup-convolution. This provides a regularization procedure: u^epsilon is semiconvex (C^{1,1}) and converges to u.

---

**U10. Entropy/Viscosity Admissibility**

    u = lim_{epsilon → 0} u^epsilon    where partial_t u^epsilon + H(nabla u^epsilon) = epsilon Delta u^epsilon

The viscosity solution is the unique limit of vanishing-viscosity approximations. This is the *defining* selection principle: among all possible weak solutions, the viscosity solution is the one that survives infinitesimal diffusion.

---

### Universal Inequality Summary

| Label | Inequality                        | Type            | Status        | Role                        |
|-------|-----------------------------------|-----------------|---------------|-----------------------------|
| U1    | Comparison principle              | Order           | Unconditional | Foundation of uniqueness     |
| U2    | L^{infinity} contraction          | Contraction     | Unconditional | Stability                   |
| U3    | Lipschitz propagation             | Bound           | Unconditional | Gradient control             |
| U4    | Semiconcavity                     | One-sided       | t > 0         | Maximum regularity           |
| U5    | Finite-speed propagation          | Cone            | Unconditional | Hyperbolicity                |
| U6    | Hopf–Lax formula                 | Variational     | Quadratic H   | Explicit solution            |
| U7    | Oleinik bound                     | Universal       | 1D, t > 0    | Sharpest regularization      |
| U8    | Shock-formation time              | Sharp estimate  | Generic data  | Singularity timing           |
| U9    | Sup-convolution stability         | Regularization  | Unconditional | Robustness                   |
| U10   | Vanishing-viscosity selection     | Limit           | Unconditional | Physical selection            |

**All ten inequalities are unconditional** for convex H and Lipschitz initial data. The HJ envelope is fully closed within the viscosity-solution framework.

---

## 4. Attractors and Long-Time Behavior

### 4.1 The Hopf–Lax Formula as Variational Attractor

For H(p) = |p|^2/2 on R^d with Lipschitz initial data u_0:

    u(x, t) = inf_y { u_0(y) + |x - y|^2 / (2t) }

As t → infinity, the infimum is dominated by the global minimizer y_* = argmin u_0:

    u(x, t) → min u_0 + |x - y_*|^2 / (2t)    [leading-order asymptotics]

The long-time profile is a *paraboloid* centered at the minimizer of u_0, with amplitude decaying as 1/t.

**Properties of the HJ attractor:**
- *Variational:* The attractor is the minimum of a cost functional, not an equilibrium of a differential equation.
- *Decaying:* u(x, t) → min u_0 as t → infinity (u approaches its global minimum value at every point).
- *Self-similar:* The profile u(x, t) - min u_0 has the scaling form t^{-1} Phi(x / sqrt(t)).
- *Universal:* The long-time asymptotics depend on u_0 only through its minimum value and the location of the minimizer — all other features of u_0 are forgotten.

### 4.2 Pre-Shock vs. Post-Shock Attractor Mechanisms

**Pre-shock (t < T*):** The dynamics are governed by *classical characteristics*. The "attractor" is the characteristic map itself: each point x at time t traces back to a unique initial point x_0 via x = x_0 + t nabla u_0(x_0). The solution is determined by point-to-point tracing — a purely *kinematic* mechanism.

**Post-shock (t > T*):** The dynamics are governed by the *Hopf–Lax minimization*. The attractor mechanism shifts from kinematic (characteristic tracing) to *variational* (cost minimization). The viscosity solution selects, at each point x, the *optimal initial point* y that minimizes u_0(y) + |x - y|^2/(2t). This variational selection is a *competition among characteristics*: multiple characteristics arrive at the same point, and the Hopf–Lax formula selects the one with the lowest total cost.

The transition from kinematic to variational is the *dynamical content of shock formation*: before the shock, each point has a unique predecessor; after the shock, each point has multiple predecessors, and the solution selects the optimal one.

### 4.3 Comparison with Other Attractors

| Architecture | Attractor Type           | Character       | Determined By        | Convergence |
|-------------|--------------------------|-----------------|----------------------|-------------|
| **HJ**      | **Paraboloid (1/t decay)**| **Variational** | **min(u_0), argmin** | **Algebraic (1/t)** |
| FP          | Gibbs–Boltzmann          | Statistical     | Potential V, sigma^2 | Exponential |
| PME         | Barenblatt profile       | Self-similar    | Total mass M         | Algebraic   |
| TFE         | Source-type profile      | Self-similar    | Total mass M         | Algebraic   |
| MCF         | Round sphere / shrinkers | Geometric       | Area/topology        | Algebraic   |
| AC          | phi = ±1                 | Functional      | Initial phase sign   | Exponential (bulk) |
| CH          | Phase-separated domains  | Functional      | Mass + topology      | Algebraic   |
| NS (2D)    | Compact attractor        | Dynamical       | Reynolds number      | Unknown     |
| RD          | Constitutive             | Constitutive    | Kinetics             | Constitutive|

The HJ attractor is unique in the Atlas:
- It is *variational* (a minimizer of a cost functional), not a fixed point of a flow or an equilibrium of a gradient flow.
- It *decays* (u → min u_0, approaching a constant), rather than converging to a nontrivial profile.
- It depends on only *two* features of the initial data (the minimum value and its location), making it the *most forgetful* attractor — it retains the least information about the initial conditions.

### 4.4 The HJ "Central Limit Theorem"

The HJ long-time asymptotics parallel the classical central limit theorem (CLT) and its nonlinear generalizations:

| Framework | Initial Data     | Long-Time Limit              | Mechanism           |
|-----------|------------------|------------------------------|---------------------|
| CLT (m=1) | Any dist. (finite var.) | Gaussian             | Linear diffusion    |
| PME (m>1) | Any L^1 density  | Barenblatt profile           | Nonlinear diffusion |
| **HJ**    | **Any Lipschitz** | **Paraboloid (Hopf–Lax)**   | **Nonlinear transport** |
| FP        | Any prob. density | Gibbs–Boltzmann              | Drift + diffusion   |

Each architecture has its own "CLT" — a universal long-time profile that all initial data converge to, forgetting their specific shape and retaining only a few global parameters (mass, minimum, variance, etc.). The HJ CLT is: *every Lipschitz potential converges to a paraboloid determined by the location and value of its global minimum*.

---

## 5. Comparison with AC, CH, PME, TFE, RD, NS, FP, and MCF

### 5.1 The Smoothing–Steepening Axis

The PDE Atlas architectures can be organized along a *smoothing–steepening axis*:

    FP (max smooth) → PME/TFE → AC/CH → MCF → NS → HJ (max steep)

**Smoothing pole (FP):** Linear diffusion. Gaussian smoothing. Analytic regularity. Exponential convergence to Gibbs–Boltzmann. No singularity. Maximum analytical control.

**Steepening pole (HJ):** No diffusion. Gradient steepening. Regularity loss. Algebraic convergence to paraboloid. Certain singularity (gradient shock). Minimal analytical structure (viscosity solutions).

Every architecture in between has some mix of smoothing and steepening:
- PME/TFE: Nonlinear diffusion (smoothing), but degenerate (free boundary — a mild geometric singularity).
- AC/CH: Diffusion + reaction (smoothing), with interfaces (a mild structural complexity).
- MCF: Curvature smoothing + certain singularity (the transition point).
- NS: Viscous smoothing + nonlinear advection (the competition is unresolved in 3D).

HJ is at the extreme: *pure steepening, zero smoothing*. It demonstrates what happens when the smoothing mechanism is entirely absent.

### 5.2 HJ vs. NS: The Same Nonlinearity, Different Outcomes

HJ and NS share the same nonlinear mechanism — first-order transport (H(nabla u) for HJ, (u . nabla)u for NS). The difference:

- HJ has *only* this mechanism (no diffusion, no pressure, no incompressibility).
- NS has this mechanism *plus* diffusion + pressure + incompressibility.

The result:
- HJ: singularity is *certain and completely understood* (viscosity solutions).
- NS: singularity is *open and not understood* (the Millennium Problem).

This comparison reveals that the difficulty of the NS regularity problem is not in the nonlinear transport *per se* (HJ handles it completely) but in the *interaction* of transport with pressure and incompressibility. The nonlocal pressure channel, which HJ lacks, is what makes NS intractable.

### 5.3 HJ vs. FP: Structural Duals

HJ and FP are *structural duals* — every feature of one is reversed in the other:

| Feature                    | HJ                        | FP                          |
|----------------------------|----------------------------|-----------------------------|
| PDE type                   | Hyperbolic (1st-order)     | Parabolic (2nd-order)       |
| Smoothing                  | None                       | Maximum (Gaussian)          |
| Regularity trend           | Decreasing (C^inf → Lip.) | Increasing (L^2 → analytic) |
| Propagation speed          | Finite (characteristics)   | Infinite (heat kernel)      |
| Singularity                | Certain (gradient shock)   | Impossible (linear)         |
| Lyapunov functional        | None (parabolic sense)    | Free energy F               |
| Solution concept           | Viscosity                  | Classical                   |
| Contraction metric         | L^{infinity}              | Wasserstein                 |
| Attractor                  | Paraboloid (variational)  | Gibbs–Boltzmann (statistical)|
| Linearity                  | Nonlinear                  | Linear                      |
| Closure mechanism          | Convexity + viscosity      | Linearity                   |

The duality is *complete*: there is no feature of FP that is not reversed in HJ, and vice versa. Together, FP and HJ define the *full range* of scalar PDE dynamics in the Atlas.

### 5.4 Summary Table

| Feature                    | HJ           | FP    | PME   | AC    | CH    | TFE   | MCF   | NS    | RD    |
|----------------------------|-------------|-------|-------|-------|-------|-------|-------|-------|-------|
| PDE order                  | **1st**     | 2nd   | 2nd   | 2nd   | 4th   | 4th   | 2nd   | 2nd   | 2nd   |
| Diffusion                  | **None**    | Linear| Degen.| Linear| Biharm.| Degen.biharm.| Curv.| Visc.| Linear|
| Smoothing                  | **None**    | Max.  | Medium| Medium| Strong| Strong| Geom. | Medium| Constitutive |
| Gradient behavior          | **Steepen** | Smooth| Smooth| Smooth| Smooth| Smooth| Smooth| Open  | Constitutive |
| Singularity                | **Certain** | None  | None  | None  | None  | n-dep | Certain| Open | Constitutive |
| Continuation               | **Viscosity**| N/A  | N/A   | N/A   | N/A   | N/A   | Level-set| Leray| N/A |
| Attractor                  | **Paraboloid**| Gibbs| Baren.| ±1   | Phase | Flat  | Sphere| Open  | Constitutive |
| Conservation               | No          | Yes   | Yes   | No    | Yes   | Yes   | No    | Yes   | Constitutive |
| Locality                   | Local       | Local | Local | Local | Local | Local | Local | Nonloc.| Local |
| Parameters                 | **0**       | 2     | 1     | 3     | 3     | 1     | **0** | 2     | Many  |

HJ is the *unique first-order, non-diffusive, steepening, certainly-singular, variationally-continued* architecture in the Atlas. It is the anti-diffusion pole, the reduced core of NS, the structural dual of FP, and the simplest PDE that produces finite-time singularity from smooth data.

---

*End of Mode 2: PDE → Extremal Dynamics. Mode 3 (Channels → Constraint Surface) will follow in a subsequent file.*
