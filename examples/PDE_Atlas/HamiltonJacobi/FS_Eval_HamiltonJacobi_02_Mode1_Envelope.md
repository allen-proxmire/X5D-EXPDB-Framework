# AD Evaluation: Hamilton–Jacobi Equation — Mode 1: Axiom → Envelope

Allen Proxmire

April 2026

---

## Overview

Mode 1 traces the path from the HJ axioms (HJ-1 through HJ-8) to the architectural envelope. The HJ envelope is *qualitatively different* from every other envelope in the PDE Atlas: it is sealed not by diffusion, not by curvature, not by fourth-order smoothing, and not by linearity, but by *convexity of the Hamiltonian* combined with the *viscosity-solution framework*. These two structural features — one from the PDE (convexity) and one from the solution concept (viscosity) — together provide existence, uniqueness, and stability of global solutions, even though classical solutions break down in finite time.

The HJ envelope is the *anti-diffusion envelope*: where every other architecture controls its dynamics through some form of smoothing (parabolic, geometric, or linear), the HJ architecture controls its dynamics through *convex duality* and *selection principles*. The result is an envelope that is fully closed — but closed by completely different mechanisms than any other architecture.

Throughout:

    partial_t u + H(nabla u) = 0,    H convex,    u viscosity solution

on R^d with Lipschitz initial data u_0.

---

## 1. Forbidden Configurations

### F1. Diffusion

**Axiom source:** HJ-7 (No Diffusion).

The HJ equation has no second-order term. There is no Delta u, no div(D nabla u), no biharmonic Delta^2 u, and no degenerate diffusion u^{m-1} Delta u. The architecture is *purely first-order* in space. Adding any diffusion term, no matter how small, converts the HJ equation to a *viscous HJ equation* (partial_t u + H(nabla u) = epsilon Delta u), which is parabolic and globally smooth — a qualitatively different architecture.

The absence of diffusion is the most consequential structural commitment in the HJ architecture: it is what produces gradient steepening, shock formation, and the need for viscosity solutions. Every other architecture in the Atlas has diffusion; HJ alone lacks it.

### F2. Reaction Terms

**Axiom source:** HJ-7 (No Reaction).

No source/sink terms R(u) appear. The HJ equation is a *pure transport* equation: the value of u at each point changes only because of the nonlinear transport H(nabla u), not because of local creation or destruction. Adding reaction terms would produce a Hamilton–Jacobi–Bellman equation with running cost — a different architecture used in stochastic control.

### F3. Nonlocal Velocity Laws

**Axiom source:** HJ-2 (Locality), HJ-3 (H(nabla u)).

The Hamiltonian H depends only on nabla u at each point — not on u at distant points, not on integrals of u, and not on a nonlocal solve (no Poisson equation, no pressure). The HJ architecture is fully local at the formulation level. The velocity of a characteristic at (x, t) is nabla_p H(nabla u(x, t)) — determined entirely by the local gradient.

### F4. Infinite-Speed Propagation

**Axiom source:** HJ-6 (Hyperbolic, Characteristics).

The HJ equation propagates information at *finite speed* along characteristics. The propagation speed is |nabla_p H(nabla u)| — bounded for bounded nabla u. A perturbation at (x_0, 0) influences u(x, t) only within a cone |x - x_0| <= C t, where C depends on the Lipschitz constant of u_0 and the growth of H.

Infinite-speed propagation — instantaneous influence at arbitrarily distant points — is structurally forbidden. This is the *opposite* of FP, AC, CH (all of which have infinite propagation speed through their non-degenerate diffusion channels) and the *same* as PME/TFE (which have finite speed through degenerate diffusion). But the mechanism is different: PME/TFE have finite speed because diffusion degenerates at u = 0; HJ has finite speed because the equation is *hyperbolic* (first-order, characteristics).

### F5. Persistent Smoothness (for Generic Initial Data)

**Axiom source:** HJ-3, HJ-6, HJ-7.

For generic smooth initial data u_0 with non-trivial curvature in nabla u_0, the classical (smooth) solution breaks down in finite time. The gradient nabla u develops a discontinuity — a *shock* in the gradient, or equivalently a *kink* in u (a point where u is continuous but not differentiable).

Persistent global smoothness — u remaining C^1 for all time — is forbidden for generic initial data. The only initial data for which the solution remains smooth forever are those whose gradient is *monotone* (in 1D) or satisfies restrictive convexity conditions (in higher dimensions) that prevent characteristics from crossing.

### F6. Oscillations and Chaos

**Axiom source:** HJ-3 (first-order), HJ-7 (no diffusion, no reaction).

The HJ equation has no mechanism for oscillation or chaos:
- No reaction channel (which would be needed for limit cycles in the ODE sense).
- No dispersive terms (which would be needed for wave-type oscillations).
- No second-order structure (which would be needed for pattern formation).
- The comparison principle (E1 below) provides monotonicity: if u_0 <= v_0, then u(t) <= v(t). Monotone dynamics cannot oscillate.

The dynamics are *one-directional*: gradients steepen until they shock, and the viscosity solution selects the unique continuation. There is no mechanism for the solution to "bounce back" or revisit previous states.

### F7. Pattern Formation

**Axiom source:** HJ-3 (first-order), HJ-7 (no reaction).

Pattern formation requires instability mechanisms (Turing, Hopf, etc.) that involve at least two species or a reaction-diffusion balance. HJ has one species (u), no reaction, and no diffusion. Spatial patterns cannot self-organize under HJ dynamics — the solution simply transports and steepens.

### F8. Bulk Dissipation (Parabolic Lyapunov)

**Axiom source:** HJ-7 (no diffusion).

Every parabolic architecture in the Atlas has a Lyapunov functional that decreases through a *dissipation mechanism* involving gradients (||nabla u||^2, ||nabla mu||^2, integral H^2 dS, etc.). HJ has no dissipation mechanism — there is no diffusion to dissipate energy. The total "energy" integral H(nabla u) dx is *not* a Lyapunov functional — it is not monotone in general.

The HJ architecture has *no Lyapunov functional in the parabolic sense*. It does have *variational structure* (the Hopf–Lax formula, connection to optimal transport) and *comparison structure* (the comparison principle), which serve as substitute structural controls. But the parabolic-Lyapunov paradigm does not apply.

### F9. Non-Convex Hamiltonians (for Standard Uniqueness)

**Axiom source:** HJ-4 (Convex Hamiltonian).

The standard viscosity-solution theory requires H to be convex in p for the *comparison principle* (E1) to hold, which is the foundation of uniqueness. For non-convex H, the comparison principle can fail, leading to non-uniqueness of viscosity solutions or the need for additional selection criteria (e.g., Ishii's definition for non-convex H, which is more complex).

The convexity restriction is a *structural requirement for well-posedness*, not merely a simplifying assumption. Without it, the HJ architecture loses its primary closure mechanism.

### F10. Classical Continuation Past Gradient Blowup

**Axiom source:** HJ-3, HJ-6, HJ-8.

Once nabla u develops a discontinuity (shock), the classical PDE partial_t u + H(nabla u) = 0 is no longer meaningful at the shock location (nabla u is not defined). Classical solutions cannot continue past the shock time T*. The architecture *requires* the viscosity-solution framework (HJ-8) for continuation.

Any claim of classical (smooth) solutions for all time is forbidden for generic initial data. The HJ architecture is *designed* to break down classically and *designed* to continue through viscosity solutions.

### Summary of Forbidden Configurations

| Label | Forbidden Configuration                     | Excluding Axiom(s)      |
|-------|---------------------------------------------|-------------------------|
| F1    | Diffusion (any second-order term)           | HJ-7                   |
| F2    | Reaction terms                              | HJ-7                   |
| F3    | Nonlocal velocity laws                      | HJ-2, HJ-3             |
| F4    | Infinite-speed propagation                  | HJ-6                   |
| F5    | Persistent smoothness (generic data)        | HJ-3, HJ-6, HJ-7      |
| F6    | Oscillations / chaos                        | HJ-3, HJ-7             |
| F7    | Pattern formation                           | HJ-3, HJ-7             |
| F8    | Parabolic Lyapunov dissipation              | HJ-7                   |
| F9    | Non-convex Hamiltonians (standard theory)   | HJ-4                   |
| F10   | Classical continuation past blowup          | HJ-3, HJ-6, HJ-8      |

---

## 2. Necessary Configurations

### N1. First-Order Nonlinear Transport

**Source:** HJ-3.

The evolution is governed by the first-order law partial_t u + H(nabla u) = 0. The Hamiltonian H acts on the gradient nabla u, producing a *nonlinear transport* — the speed of characteristics depends on the gradient itself. This is the sole dynamical mechanism.

### N2. Finite-Speed Propagation via Characteristics

**Source:** HJ-3, HJ-6.

Information propagates along characteristics — curves (x(t), t) satisfying dx/dt = nabla_p H(nabla u). The propagation speed is |nabla_p H(p)| for gradient value p. For H(p) = |p|^2/2, the speed is |p| = |nabla u| — the speed equals the gradient magnitude. Information cannot travel faster than the maximum characteristic speed.

The domain of dependence of a point (x, t) is the set of points (y, 0) that can influence u(x, t) through characteristics. This set is bounded, confirming finite-speed propagation.

### N3. Gradient Steepening and Shock Formation

**Source:** HJ-3, HJ-6, HJ-7.

For generic initial data, characteristics converge in finite time. At the convergence time T*, the gradient nabla u becomes multi-valued (the classical solution ceases to exist) and the viscosity solution develops a kink (a point of non-differentiability). In the Burgers picture (v = nabla u), this is a *shock* — a discontinuity in the velocity.

**Shock-formation time estimate:** For H(p) = |p|^2/2 in 1D with initial data u_0:

    T* = 1 / max(-u_0''(x))    [where u_0 is concave]

If u_0 is strictly concave somewhere (u_0'' < 0 at some point), then T* < infinity and the gradient must blow up. The shock-formation time is *inversely proportional to the maximum initial concavity*.

### N4. Viscosity-Solution Framework

**Source:** HJ-8.

The viscosity-solution concept (Crandall–Lions, 1983) provides the unique global continuation past gradient blowup. Key properties:

- **Existence:** For any Lipschitz u_0, a viscosity solution exists for all t >= 0.
- **Uniqueness:** For convex H, the viscosity solution is unique (comparison principle).
- **Stability:** If u_n → u uniformly and each u_n is a viscosity solution of an approximating problem, then u is the viscosity solution.
- **Consistency:** Where u is smooth, the viscosity solution satisfies the PDE classically.
- **Vanishing-viscosity limit:** u = lim_{epsilon → 0} u^epsilon, where u^epsilon solves the viscous approximation.

### N5. Comparison Principle

**Source:** HJ-3, HJ-4 (convex H), HJ-8.

If u and v are viscosity sub- and super-solutions respectively, and u(x, 0) <= v(x, 0), then:

    u(x, t) <= v(x, t)    for all x, t >= 0

The comparison principle is the *foundation of uniqueness* for viscosity solutions. It follows from the convexity of H and the definition of viscosity sub/super-solutions. It is the HJ analogue of the maximum principle for parabolic equations — but operating in a different framework (viscosity instead of classical).

### N6. Hopf–Lax Variational Formula

**Source:** HJ-3, HJ-4, HJ-5.

For H(p) = L^*(p) where L^* is the Legendre transform of a convex Lagrangian L:

    u(x, t) = inf_y { u_0(y) + t L((x - y)/t) }

For H(p) = |p|^2/2: L(v) = |v|^2/2 and:

    u(x, t) = inf_y { u_0(y) + |x - y|^2 / (2t) }

The Hopf–Lax formula gives the viscosity solution *explicitly* as an infimal convolution. It connects HJ to optimal transport: u(x, t) is the optimal cost of reaching x at time t from any starting point y, with transport cost L((x-y)/t) and terminal value u_0(y).

### N7. Semiconcavity (Lipschitz Regularization)

**Source:** HJ-3, HJ-4, N6.

For convex H, the viscosity solution becomes *semiconcave* for t > 0:

    u(x + h, t) + u(x - h, t) - 2u(x, t) <= C |h|^2 / t

for a constant C depending on H. Semiconcavity is a *one-sided regularity*: the solution is "at most" as curved as a paraboloid from above. This is the HJ analogue of parabolic smoothing — but weaker: parabolic equations make solutions C^{infinity}, while the HJ makes solutions merely semiconcave (with possible kinks from below).

The semiconcavity estimate is the *maximum regularity* the HJ architecture can provide. The solution is Lipschitz continuous and semiconcave, but generically *not* C^1 (the gradient has jump discontinuities at shocks).

### N8. Entropy/Viscosity Selection

**Source:** HJ-4, HJ-8.

Among the many possible weak solutions of the HJ equation, the viscosity solution is the unique one that satisfies the *entropy condition*: it is the limit of the vanishing-viscosity approximation u^epsilon. Physically, the viscosity solution selects the solution that would survive the addition of infinitesimal diffusion — the *thermodynamically consistent* solution.

In the Burgers picture, the entropy condition corresponds to the Oleinik entropy condition for conservation laws: shocks must satisfy the Lax–Oleinik admissibility criterion (characteristics enter the shock from both sides).

### N9. Nonlinear Semigroup Structure

**Source:** HJ-3, HJ-8.

The viscosity-solution map S_t : u_0 → u(t) forms a *nonlinear semigroup*:

    S_{t+s} = S_t circ S_s    for all t, s >= 0
    S_0 = identity

The semigroup S_t is:
- Order-preserving: u_0 <= v_0 implies S_t u_0 <= S_t v_0 (comparison principle).
- L^{infinity}-contractive: ||S_t u_0 - S_t v_0||_{L^{infinity}} <= ||u_0 - v_0||_{L^{infinity}}.
- Lipschitz-preserving: if u_0 is Lipschitz with constant L, then S_t u_0 is Lipschitz with constant <= L.

The semigroup structure is the HJ analogue of the heat semigroup (for FP) and the L^1 contraction semigroup (for PME). It provides the global-in-time solution theory without any diffusion or smoothing.

### N10. Certain Singularity Formation

**Source:** HJ-3, HJ-6, HJ-7.

For generic Lipschitz initial data u_0 (specifically, for u_0 that is not globally convex), the classical solution develops a gradient discontinuity in finite time T* < infinity. This is *certain* — not open (as in NS), not constitutive (as in RD), and not required-for-a-purpose (as in MCF), but simply *inevitable* for generic data.

The singularity is a *gradient shock*: u remains continuous (and even Lipschitz) but nabla u develops a jump. The viscosity solution continues uniquely past the shock, selecting the entropy-admissible weak solution.

### Summary of Necessary Configurations

| Label | Necessary Configuration                     | Source               |
|-------|---------------------------------------------|----------------------|
| N1    | First-order nonlinear transport             | HJ-3                 |
| N2    | Finite-speed propagation (characteristics)  | HJ-3, HJ-6          |
| N3    | Gradient steepening → shock formation       | HJ-3, HJ-6, HJ-7   |
| N4    | Viscosity-solution framework                | HJ-8                 |
| N5    | Comparison principle (from convexity)       | HJ-3, HJ-4, HJ-8   |
| N6    | Hopf–Lax variational formula               | HJ-3, HJ-4, HJ-5   |
| N7    | Semiconcavity (one-sided regularity)        | HJ-3, HJ-4          |
| N8    | Entropy/viscosity selection                 | HJ-4, HJ-8          |
| N9    | Nonlinear semigroup structure               | HJ-3, HJ-8          |
| N10   | Certain singularity (gradient blowup)       | HJ-3, HJ-6, HJ-7   |

---

## 3. Envelope Inequalities (E1–E10)

---

**E1. Comparison Principle**

    u_0 <= v_0  =>  u(t) <= v(t)    for all t >= 0    (viscosity solutions)

The ordering of initial data is preserved for all time. This is the *foundational inequality* of the HJ envelope — it replaces the Lyapunov functional that parabolic architectures use. The comparison principle is the *structural backbone* of the viscosity-solution theory.

---

**E2. Lipschitz Bound Propagation**

    ||nabla u(t)||_{L^{infinity}} <= ||nabla u_0||_{L^{infinity}}

The Lipschitz constant of u does not increase in time. This is a *Lipschitz contraction* — the maximum slope of u is non-increasing. For the viscosity solution, the gradient can *decrease* (through shock formation, which "clips" the steep parts of the gradient) but never increase.

This bound ensures that u(t) remains Lipschitz for all time — even though nabla u develops discontinuities, the *Lipschitz constant* (the L^{infinity} norm of nabla u) does not blow up. The singularity is a *regularity loss* (from C^1 to Lipschitz), not an *amplitude blowup* (the Lipschitz constant stays bounded).

---

**E3. Semiconcavity Estimate**

    u(x + h, t) + u(x - h, t) - 2u(x, t) <= C |h|^2 / t    for t > 0

The solution becomes semiconcave for t > 0 — its second-order behavior is controlled from above. The constant C depends on the Hamiltonian H. The semiconcavity estimate is the HJ analogue of the parabolic smoothing estimate (||nabla^k u(t)|| <= C t^{-k/2} for the heat equation), but it is *one-sided* (controls concavity only, not convexity) and *weaker* (semiconcavity is between Lipschitz and C^{1,1}, not C^{infinity}).

---

**E4. Finite-Speed Propagation Bound**

For H(p) with |nabla_p H(p)| <= C(1 + |p|):

    u(x, t) depends only on u_0(y) with |y - x| <= C(1 + ||nabla u_0||_{L^{infinity}}) t

The domain of dependence is a *cone* in spacetime with opening angle determined by the maximum characteristic speed. Information cannot propagate faster than the maximum of |nabla_p H(nabla u)|.

---

**E5. Hopf–Lax Variational Inequality**

    u(x, t) = inf_y { u_0(y) + t L((x-y)/t) }    for H(p) = L^*(p)

The viscosity solution is characterized as the *infimum* over all "paths" connecting (y, 0) to (x, t) with Lagrangian cost L. This variational representation:
- Gives the solution explicitly (no PDE solving needed).
- Proves existence (the infimum is attained for nice L).
- Proves the comparison principle (infimum over a larger set is smaller).
- Connects HJ to optimal transport and calculus of variations.

---

**E6. Oleinik One-Sided Gradient Bound (1D)**

In one dimension, for H(p) = p^2/2:

    partial_x u(x, t) <= 1/t    for t > 0    (in the viscosity sense)

This is the *Oleinik entropy condition* expressed for HJ: the gradient from the right is bounded above by 1/t. The gradient can be arbitrarily negative (from shocks) but cannot be too positive. This one-sided bound is the *sharpest regularization* the HJ provides — it is a *universal* bound depending only on t, not on the initial data.

In the Burgers picture (v = u_x), this becomes v(x, t) <= 1/t — the velocity cannot exceed 1/t regardless of the initial velocity. This is the *universal decay estimate* for the gradient of viscosity solutions.

---

**E7. Shock-Formation Time Estimate**

For H(p) = |p|^2/2 in 1D:

    T* = 1 / max_x (-u_0''(x))    (where u_0 has negative second derivative)

More generally: the shock-formation time is determined by the *initial concavity*. If u_0 is globally convex, T* = infinity (no shock). If u_0 has a concave region, T* < infinity and the first shock forms at the point of maximum concavity.

For d > 1: the shock-formation time depends on the eigenvalues of the Hessian D^2 u_0. The first shock forms where the most negative eigenvalue of D^2 u_0 is largest in magnitude.

---

**E8. Entropy/Viscosity Admissibility**

The viscosity solution satisfies the *entropy condition*: at every point of non-differentiability (shock), the Lax–Oleinik admissibility criterion holds:

    H(p_-) >= (H(p_+) - H(p_-)) / (p_+ - p_-) * (p - p_-) + H(p_-)    for p between p_- and p_+

where p_- and p_+ are the left and right limits of nabla u at the shock. This ensures that *characteristics enter the shock from both sides* (the shock is compressive, not expansive).

The entropy condition is the HJ analogue of the Second Law of thermodynamics: it selects the physically correct weak solution by requiring that information is *lost* (not gained) at shocks.

---

**E9. Stability Under Sup-Convolution**

If u^epsilon(x) = sup_y { u(y) - |x-y|^2 / (2 epsilon) } is the sup-convolution of u, then:

    u^epsilon → u    uniformly as epsilon → 0

and u^epsilon is semiconvex (and thus C^{1,1}). The viscosity-solution theory is *stable under regularization*: smoothing u by sup-convolution produces an approximate solution that converges to the viscosity solution.

This stability is the HJ analogue of the stability of parabolic solutions under mollification. It ensures that the viscosity solution is *robust* — small perturbations of the initial data or the equation produce small changes in the solution.

---

**E10. L^{infinity} Contraction (Crandall–Lions Semigroup)**

    ||u(t) - v(t)||_{L^{infinity}} <= ||u_0 - v_0||_{L^{infinity}}    for all t >= 0

The viscosity-solution semigroup is a *contraction on L^{infinity}*. Two solutions that start close (in the sup norm) remain close forever. This is the *strongest stability estimate* for HJ — it provides Lipschitz continuous dependence on initial data in the L^{infinity} norm.

Comparison with other contractions:
- PME: L^1 contraction (||u - v||_{L^1} non-increasing).
- FP: Wasserstein contraction (W_2(rho_1, rho_2) exponentially decreasing).
- **HJ: L^{infinity} contraction** (||u - v||_{L^{infinity}} non-increasing).

Each architecture contracts in its *natural metric*: PME in L^1 (mass metric), FP in Wasserstein (transport metric), HJ in L^{infinity} (potential metric). The L^{infinity} contraction is the natural one for HJ because u is a *potential* — its maximum deviation from another potential is the relevant distance.

---

### Envelope Summary

The HJ envelope is defined by ten constraints organized into three tiers:

**Tier 1 — Structural Framework (convexity + viscosity):**
- E1: Comparison principle (foundation of uniqueness).
- E5: Hopf–Lax variational formula (explicit solution representation).
- E8: Entropy/viscosity admissibility (physical selection principle).
- E10: L^{infinity} contraction (strongest stability).

**Tier 2 — Regularity and Propagation:**
- E2: Lipschitz bound propagation (gradient stays bounded in L^{infinity}).
- E3: Semiconcavity (one-sided second-order control).
- E4: Finite-speed propagation (characteristic cone).
- E6: Oleinik one-sided gradient bound (universal: <= 1/t in 1D).

**Tier 3 — Singularity and Formation:**
- E7: Shock-formation time (determined by initial concavity).
- E9: Stability under sup-convolution (robustness of viscosity solutions).

**All constraints hold unconditionally** for convex H and Lipschitz initial data. No dimensional restriction, no parameter condition, no conditional hypothesis. The HJ envelope is *fully closed* within the viscosity-solution framework.

---

## 4. Central Architectural Finding

### 4.1 The HJ Closure Mechanism: Convexity + Viscosity

Every previous architecture in the Atlas seals its envelope through *smoothing*:

| Architecture | Smoothing Mechanism              | Closure Tool               |
|-------------|----------------------------------|-----------------------------|
| AC          | Laplacian + max. principle       | L^{infinity} control        |
| CH          | Bilaplacian                      | H^2 control + Sobolev       |
| PME         | Degenerate Laplacian             | L^1 contraction + entropy   |
| TFE         | Degenerate bilaplacian           | Energy + degeneracy + cons. |
| FP          | Laplacian                        | Linearity                   |
| MCF         | Curvature flow                   | Area dissipation            |

The HJ architecture has *no smoothing mechanism*. It seals its envelope through a completely different pair of tools:

1. **Convexity of H:** Provides the comparison principle (E1), which is the foundation of uniqueness. Convexity replaces the maximum principle / Lyapunov functional of parabolic architectures.

2. **Viscosity-solution framework:** Provides existence, stability, and the entropy selection (E8). The viscosity concept replaces the classical PDE solution concept, extending well-posedness past gradient blowup.

Together, convexity + viscosity provide:
- Existence (Hopf–Lax formula, E5).
- Uniqueness (comparison principle, E1).
- Stability (L^{infinity} contraction, E10).
- Selection (entropy admissibility, E8).

This is a *complete well-posedness theory* — existence, uniqueness, and stability — achieved without any smoothing. The HJ architecture demonstrates that *smoothing is not necessary for closure*: convex duality and selection principles can do the same job.

### 4.2 The Anti-Diffusion Pole

The HJ architecture is the *anti-diffusion pole* of the PDE Atlas:

| Feature                | Diffusive Architectures        | HJ (Anti-Diffusive)          |
|------------------------|-------------------------------|------------------------------|
| Second-order term      | Present (smoothing)           | Absent                       |
| Gradient behavior      | Smoothing (||nabla u|| decreases)| Steepening (nabla u shocks) |
| Classical regularity   | Improves over time             | Degrades over time           |
| Singularity            | Prevented by smoothing        | Certain (gradient blowup)    |
| Lyapunov functional    | Present (energy/entropy)      | Absent (parabolic sense)     |
| Closure mechanism      | Smoothing + Lyapunov          | Convexity + viscosity        |
| Contraction metric     | L^1, L^2, Wasserstein         | L^{infinity}                 |
| Propagation speed      | Infinite (parabolic)          | Finite (hyperbolic)          |

Every diffusive property is *reversed* in HJ. The two poles — FP (maximum diffusion, linear, smooth, infinite speed) and HJ (zero diffusion, nonlinear, steepening, finite speed) — bracket the entire range of scalar PDE dynamics.

### 4.3 HJ as the Nonlinear Transport Core

The HJ equation is the *reduced nonlinear core* of the Euler/NS architecture:

    HJ: partial_t u + H(nabla u) = 0    [scalar, first-order, no diffusion]
    Burgers: partial_t v + v . nabla v = 0    [vector, first-order, no diffusion]
    Euler: partial_t u + u . nabla u = -nabla p, div u = 0    [vector, first-order, incompressible]
    NS: partial_t u + u . nabla u = -nabla p + nu Delta u, div u = 0    [+ viscosity]

Each step from HJ to NS adds structural complexity (vector, incompressibility, pressure, viscosity). The HJ equation is what remains when all of these additions are stripped away — the *irreducible nonlinear transport*.

The fact that HJ is *closed* (through convexity + viscosity) while NS is *open* (the 3D regularity problem) shows that the difficulty of NS does not lie in the nonlinear transport itself (which HJ handles completely) but in the *interaction of transport with incompressibility and pressure* — the additional structural features that NS adds beyond HJ.

### 4.4 HJ Envelope in the Atlas

| Architecture | Envelope Status          | Closure Mechanism                | Singularity        |
|-------------|--------------------------|----------------------------------|--------------------|
| ED          | Closed (static)          | Unique factorization             | None               |
| FP          | Closed (all params)      | Linearity                        | None               |
| PME         | Closed (all m > 1)       | Degeneracy + entropy + L^1 + cons.| None             |
| AC          | Closed (d <= 3)          | Max. principle + Lyapunov        | None               |
| CH          | Closed (d <= 3)          | 4th-order + Lyapunov             | None               |
| TFE (n>=1)  | Closed                   | 4th-order + degeneracy + cons.   | None               |
| MCF         | Closed + required sing.  | Area dissipation + convexity     | Required (curvature)|
| **HJ**      | **Closed (viscosity)**   | **Convexity + viscosity**        | **Certain (gradient)** |
| NS (3D)    | Open                     | Viscosity (insufficient)         | Open                |
| RD          | Constitutive             | None universal                   | Constitutive        |

HJ is the *only hyperbolic architecture* with a fully closed envelope. It achieves closure through a mechanism (convexity + viscosity) that is *entirely different* from every parabolic architecture. The closure is complete: existence, uniqueness, stability, and continuation past singularity — all established within the viscosity-solution framework.

---

*End of Mode 1: Axiom → Envelope. Mode 2 (PDE → Extremal Dynamics) will follow in a subsequent file.*
