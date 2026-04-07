# AD Evaluation: Inviscid Burgers Equation — Mode 1: Axiom → Envelope

Allen Proxmire

April 2026

---

## Overview

Mode 1 traces the path from the Burgers axioms (BA-1 through BA-8) to the architectural envelope. The Burgers envelope is structurally parallel to the HJ envelope — both are hyperbolic, both develop certain singularities, and both are sealed by convexity + entropy/viscosity. But the Burgers envelope has one structural feature that HJ lacks: the *conservation-law structure*, which provides L^1 contraction, mass conservation, Rankine–Hugoniot jump conditions, and energy dissipation at shocks. These additional tools make the Burgers envelope *richer* than the HJ envelope while maintaining the same closure level.

Throughout:

    partial_t v + partial_x(v^2/2) = 0,    v entropy solution (Kruzkov)

on R with bounded measurable initial data v_0.

---

## 1. Forbidden Configurations

### F1. Diffusion

**Axiom source:** BA-6 (No Diffusion).

No second-order term. No nu partial_{xx} v. The architecture is purely first-order — adding even infinitesimal viscosity converts Burgers to the viscous Burgers equation (globally smooth, exactly solvable via Cole–Hopf), a qualitatively different architecture.

### F2. Reaction Terms

**Axiom source:** BA-7 (No Reaction).

No source/sink terms. The evolution is pure self-advection + conservation. The mass integral v dx is preserved exactly.

### F3. Nonlocal Coupling

**Axiom source:** BA-2 (Locality).

No pressure equation, no Green's function, no integral operators. The velocity at each point evolves based solely on local information (v and v_x at that point). Fully local at formulation level.

### F4. Infinite-Speed Propagation

**Axiom source:** BA-5 (Hyperbolic).

Information propagates along characteristics at speed v — finite for bounded v. The domain of dependence is a finite cone. Infinite-speed propagation is structurally forbidden.

### F5. Persistent Smoothness (Generic Data)

**Axiom source:** BA-3, BA-5, BA-6.

For generic initial data with a region of negative slope (v_0'(x) < 0 somewhere), the classical solution breaks down in finite time T* = -1/min(v_0'). The velocity v develops a discontinuity (shock). Persistent global smoothness is forbidden for generic data.

### F6. Oscillations and Chaos

**Axiom source:** BA-3, BA-6.

The entropy solution satisfies the comparison principle (v_0 <= w_0 implies v(t) <= w(t)) and the L^1 contraction (||v - w||_{L^1} non-increasing). Monotone contracting semigroups cannot oscillate or exhibit chaos.

### F7. Pattern Formation

**Axiom source:** BA-3, BA-7.

One species, no reaction, no diffusion, no coupling. No mechanism for spatial self-organization.

### F8. Non-Convex Flux (Standard Theory)

**Axiom source:** BA-4 (Convex Flux).

The flux f(v) = v^2/2 is strictly convex (f'' = 1 > 0). Non-convex fluxes produce compound waves and require more refined entropy conditions. The standard Burgers theory assumes convexity.

### F9. Energy Conservation Across Shocks

**Axiom source:** BA-3, BA-8.

The kinetic energy integral (v^2/2) dx is *not* conserved — it *decreases* across shocks. The entropy condition requires energy dissipation at discontinuities. Energy conservation across shocks is forbidden; the architecture is *irreversible* at shocks.

### F10. Classical Continuation Past Shocks

**Axiom source:** BA-3, BA-5, BA-8.

Once v develops a discontinuity, the classical PDE v_t + v v_x = 0 is not defined at the shock (v_x is a delta function). The architecture requires the entropy-solution framework for global continuation. Classical solutions cannot persist past shock time.

### Summary of Forbidden Configurations

| Label | Forbidden Configuration                | Excluding Axiom(s)    |
|-------|----------------------------------------|-----------------------|
| F1    | Diffusion                              | BA-6                  |
| F2    | Reaction terms                         | BA-7                  |
| F3    | Nonlocal coupling                      | BA-2                  |
| F4    | Infinite-speed propagation             | BA-5                  |
| F5    | Persistent smoothness (generic)        | BA-3, BA-5, BA-6      |
| F6    | Oscillations / chaos                   | BA-3, BA-6            |
| F7    | Pattern formation                      | BA-3, BA-7            |
| F8    | Non-convex flux                        | BA-4                  |
| F9    | Energy conservation across shocks      | BA-3, BA-8            |
| F10   | Classical continuation past shocks     | BA-3, BA-5, BA-8      |

---

## 2. Necessary Configurations

### N1. First-Order Nonlinear Self-Advection

**Source:** BA-3.

The evolution is partial_t v + v partial_x v = 0 — a scalar field advecting itself at its own speed. This is the simplest *nonlinear feedback* in PDE theory: the transported quantity determines its own transport velocity.

### N2. Conservation-Law Structure

**Source:** BA-3.

The PDE has the conservation form partial_t v + partial_x(v^2/2) = 0. This implies:
- Mass conservation: d/dt integral v dx = 0 (for compactly supported v or periodic BC).
- Rankine–Hugoniot jump condition at shocks: shock speed s = (v_L + v_R)/2.
- Well-defined weak formulation: the conservation form specifies the correct integral equation for discontinuous solutions.

### N3. Finite-Speed Propagation

**Source:** BA-3, BA-5.

Characteristics travel at speed v. Information from (x_0, 0) reaches (x, t) only if x = x_0 + v_0(x_0) t. The maximum propagation speed is ||v_0||_{L^infinity}.

### N4. Gradient Steepening and Shock Formation

**Source:** BA-3, BA-5, BA-6.

For initial data with v_0'(x) < 0 somewhere: shock forms at time T* = -1/min(v_0'). The velocity gradient v_x → -infinity at the shock point, and v itself develops a jump discontinuity. Shock formation is *certain* for generic data.

### N5. Entropy-Solution Framework

**Source:** BA-8.

The Kruzkov entropy solution provides:
- Existence for all bounded initial data.
- Uniqueness among entropy solutions.
- Stability: L^1 contraction.
- Physical admissibility: vanishing-viscosity limit.

### N6. L^1 Contraction

**Source:** BA-3, BA-4, BA-8.

For any two entropy solutions v, w:

    ||v(t) - w(t)||_{L^1} <= ||v_0 - w_0||_{L^1}    for all t >= 0

This is the *Kruzkov contraction theorem* — the strongest stability property for scalar conservation laws. It implies uniqueness, continuous dependence, and asymptotic convergence. The L^1 contraction is the Burgers analogue of the PME's L^1 contraction and is *not available* for the HJ equation (which has L^{infinity} contraction instead).

### N7. L^{infinity} Contraction

**Source:** BA-3, BA-4, BA-8.

    ||v(t) - w(t)||_{L^{infinity}} <= ||v_0 - w_0||_{L^{infinity}}    for all t >= 0

Burgers has *both* L^1 and L^{infinity} contraction — the only architecture in the Atlas with contractions in two different norms simultaneously.

### N8. Oleinik One-Sided Gradient Bound

**Source:** BA-3, BA-4, BA-8.

For the entropy solution:

    partial_x v(x, t) <= 1/t    for all x, for all t > 0

This is a *universal* bound — independent of initial data. The positive part of the gradient decays as 1/t. The negative part can be arbitrarily large (at shocks). This is the same bound as HJ's semiconcavity estimate, expressed at the velocity level.

### N9. Mass Conservation

**Source:** BA-3.

    d/dt integral v(x, t) dx = 0

Total "mass" (integral of v) is exactly conserved. This is a *stronger structural property* than what HJ has (HJ has no conservation law). Mass conservation constrains the long-time asymptotics and the interaction between shocks.

### N10. Energy Dissipation at Shocks

**Source:** BA-3, BA-8.

The kinetic energy E(t) = integral v^2/2 dx satisfies:

    dE/dt <= 0    (inequality, not equality)

Energy is *dissipated* at shocks: the jump from v_L to v_R (with v_L > v_R) produces an irreversible energy loss proportional to (v_L - v_R)^3. Between shocks, energy is conserved. The energy dissipation at shocks is the *entropic irreversibility* of the Burgers architecture — the mechanism by which information is lost at discontinuities.

### Summary of Necessary Configurations

| Label | Necessary Configuration                    | Source              |
|-------|--------------------------------------------|---------------------|
| N1    | First-order self-advection                 | BA-3                |
| N2    | Conservation-law structure                 | BA-3                |
| N3    | Finite-speed propagation                   | BA-3, BA-5          |
| N4    | Shock formation (certain for generic data) | BA-3, BA-5, BA-6    |
| N5    | Entropy-solution framework                 | BA-8                |
| N6    | L^1 contraction (Kruzkov)                  | BA-3, BA-4, BA-8    |
| N7    | L^{infinity} contraction                   | BA-3, BA-4, BA-8    |
| N8    | Oleinik one-sided gradient bound (1/t)     | BA-3, BA-4, BA-8    |
| N9    | Mass conservation                          | BA-3                |
| N10   | Energy dissipation at shocks               | BA-3, BA-8          |

---

## 3. Envelope Inequalities (E1–E10)

---

**E1. Comparison Principle**

    v_0 <= w_0 (a.e.)  =>  v(t) <= w(t) (a.e.)    for all t >= 0

Order-preservation for entropy solutions. Foundation of uniqueness.

---

**E2. L^1 Contraction**

    ||v(t) - w(t)||_{L^1} <= ||v_0 - w_0||_{L^1}    for all t >= 0

The strongest stability estimate. Implies uniqueness, continuous dependence, and asymptotic convergence. *Unique to conservation laws* — HJ has L^{infinity} contraction but not L^1.

---

**E3. L^{infinity} Contraction**

    ||v(t) - w(t)||_{L^{infinity}} <= ||v_0 - w_0||_{L^{infinity}}    for all t >= 0

Sup-norm stability. Combined with E2, Burgers contracts in *two norms simultaneously* — the only architecture in the Atlas with this property.

---

**E4. Oleinik One-Sided Gradient Bound**

    partial_x v(x, t) <= 1/t    for all x, t > 0

Universal: independent of initial data. The positive slope decays as 1/t. Shocks (negative slope) can be arbitrarily steep. This is the conservation-law analogue of HJ's semiconcavity.

---

**E5. Mass Conservation**

    integral v(x, t) dx = integral v_0(x) dx    for all t >= 0

Exact conservation. Burgers is a *mass-preserving* architecture — the only hyperbolic architecture in the Atlas with an exact conservation law.

---

**E6. Finite-Speed Propagation Bound**

    v(x, t) depends only on v_0(y) with |y - x| <= ||v_0||_{L^{infinity}} t

Hyperbolic cone of dependence. Speed bounded by the maximum initial velocity.

---

**E7. Shock-Formation Time**

    T* = -1 / min_x (partial_x v_0(x))

Sharp: achieved by initial data with the specified minimum slope. The shock forms at the point of steepest negative slope.

---

**E8. Energy Dissipation Inequality**

    d/dt integral v^2/2 dx <= 0

Energy is non-increasing. Equality holds between shocks; strict inequality at shocks. The dissipation rate at a shock with jump [v_L, v_R] is proportional to (v_L - v_R)^3 / 12.

---

**E9. Rankine–Hugoniot Jump Condition**

At a shock with left state v_L, right state v_R, and shock speed s:

    s = (v_L + v_R) / 2 = [f(v_L) - f(v_R)] / (v_L - v_R)

The shock speed is the *average* of the left and right velocities. This is exact — not an approximation.

---

**E10. Lax Entropy Condition**

At every shock:

    v_L > s > v_R

Characteristics enter the shock from both sides (compressive shock). Expansive shocks (v_L < v_R) are forbidden — they would violate the entropy condition and are replaced by *rarefaction waves* (smooth, continuous expansion fans).

---

### Envelope Summary

**Tier 1 — Structural Framework:**
- E1: Comparison principle (uniqueness foundation).
- E2: L^1 contraction (strongest stability).
- E3: L^{infinity} contraction (sup-norm stability).
- E5: Mass conservation (exact).

**Tier 2 — Regularity and Propagation:**
- E4: Oleinik bound (universal 1/t gradient control).
- E6: Finite-speed propagation (hyperbolic cone).
- E8: Energy dissipation (non-increasing, irreversible at shocks).

**Tier 3 — Shock Structure:**
- E7: Shock-formation time (sharp).
- E9: Rankine–Hugoniot (exact shock speed).
- E10: Lax entropy condition (compressive shocks only).

All constraints are unconditional for convex flux and bounded initial data. The envelope is *fully closed* within the entropy-solution framework.

---

## 4. Central Architectural Finding

The Burgers envelope is the *conservation-law-enriched version* of the HJ envelope. It inherits all of HJ's closure properties (comparison, L^{infinity} contraction, Oleinik bound, finite speed, variational structure) and adds the conservation-law structure (L^1 contraction, mass conservation, Rankine–Hugoniot, energy dissipation).

### Burgers vs. HJ Envelope Comparison

| Feature                        | Burgers                    | HJ                          |
|--------------------------------|----------------------------|-----------------------------|
| Comparison principle           | Yes (E1)                   | Yes                         |
| L^1 contraction                | **Yes (E2)**               | No                          |
| L^{infinity} contraction       | Yes (E3)                   | Yes                         |
| Oleinik bound                  | Yes (E4)                   | Yes (semiconcavity)         |
| Mass conservation              | **Yes (E5)**               | No                          |
| Finite speed                   | Yes (E6)                   | Yes                         |
| Shock-formation time           | Yes (E7)                   | Yes (same T*)               |
| Energy dissipation at shocks   | **Yes (E8)**               | No (no energy concept)      |
| Rankine–Hugoniot               | **Yes (E9)**               | No (no conservation form)   |
| Lax entropy condition          | **Yes (E10)**              | Yes (viscosity condition)   |

Burgers has *four additional envelope inequalities* (E2, E5, E8, E9) that HJ lacks — all arising from the conservation-law structure. The conservation form partial_t v + partial_x(v^2/2) = 0 provides structural tools (L^1 contraction, jump conditions, energy balance) that the non-conservation HJ equation partial_t u + (1/2)(u_x)^2 = 0 does not have.

The Burgers envelope is therefore the *richest hyperbolic envelope* in the Atlas: it has all of HJ's closure properties plus the conservation-law additions. It is the *complete* hyperbolic-conservation-law envelope — the maximum structural content achievable by a first-order scalar conservation law with convex flux.

---

*End of Mode 1: Axiom → Envelope. Mode 2 (PDE → Extremal Dynamics) will follow in the next file.*
