# AD Evaluation: Inviscid Burgers Equation — Mode 2: PDE → Extremal Dynamics

Allen Proxmire

April 2026

---

## Overview

Mode 2 moves from the static envelope to the dynamics. The Burgers dynamical landscape parallels HJ's — steepening, shock formation, variational continuation — but adds the *conservation-law dynamics* that HJ lacks: Rankine–Hugoniot shock propagation, shock interaction and merging, N-wave asymptotic decay, and the irreversible dissipation of kinetic energy at shocks. The conservation-law structure gives Burgers a richer dynamical program than HJ while maintaining the same closure properties.

Throughout:

    partial_t v + v partial_x v = 0    (equivalently partial_t v + partial_x(v^2/2) = 0)

on R with bounded initial data v_0.

---

## 1. Fundamental Time and Length Scales

### 1.1 Shock-Formation Time

    T* = -1 / min_x (v_0'(x))

The shock forms at the point of steepest negative slope. For data with v_0' >= 0 everywhere (monotonically increasing), T* = infinity (no shock). For generic data with a decreasing region, T* < infinity.

### 1.2 Characteristic Speed

Characteristics travel at speed v: dx/dt = v, with v constant along each characteristic. The maximum propagation speed is ||v_0||_{L^infinity}. The characteristic map x → x + v_0(x) t is *one-to-one* for t < T* and *folds* at t = T*.

### 1.3 Three Dynamical Regimes

**Regime (A): Smooth (t < T*)**

Characteristics do not cross. The solution is classical (C^1). The velocity profile steepens in regions where v_0 is decreasing: the gradient v_x grows as v_x(x, t) = v_0'(x_0) / (1 + t v_0'(x_0)), blowing up when 1 + t v_0'(x_0) = 0.

**Regime (B): Pre-Shock (t → T*)**

The gradient concentrates: v_x → -infinity at the point of maximum initial steepness. The velocity itself remains bounded. The characteristic map is about to fold.

**Regime (C): Post-Shock (t > T*)**

Shocks have formed. The entropy solution has discontinuities in v. Between shocks, the solution is smooth (classical). The shocks propagate at speed s = (v_L + v_R)/2 and interact when they collide (shock merging). The long-time behavior is dominated by *N-waves* — self-similar triangular profiles that decay as t^{-1/2}.

### 1.4 Contrast with HJ

| Feature                    | Burgers                           | HJ                              |
|----------------------------|-----------------------------------|----------------------------------|
| Pre-shock dynamics         | v steepens                        | nabla u steepens                 |
| Shock = discontinuity in   | v itself                          | nabla u (u has a kink)           |
| Post-shock dynamics        | Shock propagation + interaction   | Kink propagation                 |
| Long-time attractor        | N-wave (t^{-1/2} decay)          | Paraboloid (1/t decay)           |
| Mass conservation          | Yes (integral v = const)          | No                               |
| Shock speed                | s = (v_L + v_R)/2 (Rankine–Hugoniot) | N/A                         |
| Energy at shocks           | Dissipated (irreversible)         | N/A                              |

---

## 2. Extremal Behaviors

### E1. Finite-Time Shock Formation

For generic data with min(v_0') < 0:

    v_x(x*, T*) → -infinity    where x* is the shock location

The shock is a *genuine discontinuity*: v jumps from v_L to v_R with v_L > v_R. The shock is the extremal steepening event — the maximum gradient concentration the architecture can produce.

### E2. Rankine–Hugoniot Shock Propagation

After formation, the shock propagates at speed:

    s(t) = (v_L(t) + v_R(t)) / 2

The shock speed is the average of the left and right states. As the shock sweeps through the medium, it *absorbs* the intervening characteristics (which enter the shock from both sides), irreversibly merging them. The shock is a *moving information sink*.

### E3. Shock Interaction and Merging

When two shocks collide, they merge into a single shock. The merged shock has:
- Left state = left state of the leftmost original shock.
- Right state = right state of the rightmost original shock.
- Speed = average of the new left and right states.

The number of shocks is *non-increasing* over time: shocks can merge but not split. The dynamics monotonically simplify the shock structure — an irreversible topological simplification analogous to MCF's topological monotonicity.

### E4. N-Wave Asymptotic Decay

For compactly supported initial data with zero mean (integral v_0 = 0), the long-time behavior is the *N-wave*:

    v(x, t) ~ { x/t    for -sqrt(2At) < x < sqrt(2Bt)
               { 0      otherwise

where A and B are determined by the positive and negative parts of v_0. The N-wave has:
- Amplitude decaying as t^{-1/2}.
- Support expanding as t^{1/2}.
- Total variation decaying as t^{-1/2}.
- A single shock at the right edge (positive-to-zero transition) and a rarefaction at the left edge.

The N-wave is the *universal long-time attractor* for zero-mean compactly supported data — the Burgers analogue of the PME's Barenblatt profile and the FP's Gibbs–Boltzmann equilibrium. For nonzero mean, the attractor is a *shifted N-wave*.

### E5. Rarefaction Waves

When v_0 has a region of increasing slope (v_0 jumping from v_L to v_R with v_L < v_R — an expansion), the entropy solution produces a *rarefaction wave*:

    v(x, t) = x/t    for v_L < x/t < v_R

The rarefaction is a *smooth, self-similar expansion fan*. Unlike shocks (discontinuous, compressive, irreversible), rarefactions are smooth, expansive, and reversible. The rarefaction wave is the Burgers architecture's *only smooth nonlinear structure* — the counterpart of the shock.

### E6. L^1 and L^{infinity} Contraction

    ||v(t) - w(t)||_{L^1} <= ||v_0 - w_0||_{L^1}
    ||v(t) - w(t)||_{L^{infinity}} <= ||v_0 - w_0||_{L^{infinity}}

Simultaneous contraction in two norms. The L^1 contraction measures *total deviation*; the L^{infinity} contraction measures *maximum deviation*. Both are non-increasing. This double contraction is *unique to Burgers* (and scalar conservation laws generally) in the Atlas.

### E7. Energy Dissipation at Shocks

    dE/dt = -(1/12) sum_shocks (v_L - v_R)^3 * (shock speed factor)

Energy is dissipated *only* at shocks, at a rate proportional to the cube of the shock strength. Between shocks, energy is exactly conserved. The total energy integral v^2/2 dx is a *piecewise-conserved, globally-decreasing* quantity.

### E8. No Oscillations, No Chaos

The comparison principle and L^1 contraction forbid oscillations, limit cycles, and chaos. The dynamics are monotone (order-preserving) and contracting (distances decrease) — the structural opposite of chaotic dynamics.

---

## 3. Universal Inequalities

---

**U1. Comparison Principle**

    v_0 <= w_0  =>  v(t) <= w(t)    for all t >= 0

---

**U2. L^1 Contraction (Kruzkov)**

    ||v(t) - w(t)||_{L^1} <= ||v_0 - w_0||_{L^1}

---

**U3. L^{infinity} Contraction**

    ||v(t) - w(t)||_{L^{infinity}} <= ||v_0 - w_0||_{L^{infinity}}

---

**U4. Oleinik One-Sided Gradient Bound**

    partial_x v(x, t) <= 1/t    for all x, t > 0

Universal: independent of initial data.

---

**U5. Mass Conservation**

    integral v(x, t) dx = integral v_0(x) dx    for all t >= 0

---

**U6. Finite-Speed Propagation**

    Domain of dependence of (x, t) subset { y : |y - x| <= ||v_0||_{L^inf} t }

---

**U7. Energy Dissipation Inequality**

    d/dt integral v^2/2 dx <= 0

Non-increasing. Strict inequality at shock times.

---

**U8. Shock-Formation Time**

    T* = -1 / min_x v_0'(x)

Sharp estimate: achieved by data with the specified minimum slope.

---

**U9. Rankine–Hugoniot Shock Speed**

    s = (v_L + v_R) / 2    at every shock

Exact: not an approximation.

---

**U10. Total Variation Bound**

    TV(v(t)) <= TV(v_0)    for all t >= 0

The total variation (integral |v_x| dx) is non-increasing. Shocks reduce total variation by absorbing characteristics.

---

### Summary

| Label | Inequality                     | Type           | Status        | Role                    |
|-------|--------------------------------|----------------|---------------|-------------------------|
| U1    | Comparison principle           | Order          | Unconditional | Uniqueness              |
| U2    | L^1 contraction                | Contraction    | Unconditional | Strongest stability     |
| U3    | L^{infinity} contraction       | Contraction    | Unconditional | Sup-norm stability      |
| U4    | Oleinik bound                  | Universal      | t > 0         | Gradient control        |
| U5    | Mass conservation              | Exact identity | Unconditional | Fundamental invariant   |
| U6    | Finite-speed propagation       | Cone           | Unconditional | Hyperbolicity           |
| U7    | Energy dissipation             | Inequality     | Unconditional | Irreversibility         |
| U8    | Shock-formation time           | Sharp          | Generic data  | Singularity timing      |
| U9    | Rankine–Hugoniot               | Exact          | At shocks     | Shock propagation       |
| U10   | Total variation bound          | Bound          | Unconditional | Complexity control      |

---

## 4. Attractors and Long-Time Behavior

### 4.1 The N-Wave Attractor

For compactly supported data with integral v_0 = 0, the long-time attractor is the *N-wave* — a piecewise-linear profile with one shock and one rarefaction:

    v(x, t) ~ N(x, t; A, B) = { x/t    for -sqrt(2At) < x < sqrt(2Bt)
                                { 0      otherwise

with A = -min integral^x v_0 dy and B = max integral^x v_0 dy.

The N-wave is:
- **Self-similar:** N(x, t) = t^{-1/2} N_*(x / t^{1/2}).
- **Universal:** All compactly supported zero-mean data converge to it.
- **Explicit:** Given by a piecewise-linear formula.
- **Decaying:** Amplitude ~ t^{-1/2}, support ~ t^{1/2}.

For nonzero mean (integral v_0 = M ≠ 0), the attractor includes a constant-velocity component plus an N-wave correction.

### 4.2 Comparison with Other Attractors

| Architecture | Attractor             | Decay Rate     | Character        |
|-------------|------------------------|----------------|------------------|
| **Burgers** | **N-wave**            | **t^{-1/2}**   | **Conservation-law self-similar** |
| HJ          | Paraboloid            | t^{-1}         | Variational      |
| FP          | Gibbs–Boltzmann       | Exponential     | Statistical      |
| PME         | Barenblatt            | t^{-alpha}     | Diffusive        |
| MCF         | Sphere (extinction)   | (T*-t)^{1/2}   | Geometric        |
| AC          | phi = ±1              | Exponential     | Phase selection  |

The N-wave decay rate t^{-1/2} is the *conservation-law decay* — determined by the balance of mass conservation (which forbids faster decay) and shock dissipation (which drives the decay). The rate is *slower* than HJ's paraboloid decay (1/t) because Burgers conserves mass (which HJ does not). Conservation is a *constraint on decay*.

---

## 5. Comparison with HJ, NS, FP, AC/CH, PME/TFE, MCF

### 5.1 Burgers vs. HJ: Conservation Law Enrichment

Burgers adds to HJ: conservation form, L^1 contraction, mass conservation, Rankine–Hugoniot conditions, energy dissipation at shocks, total variation bounds, N-wave attractor. Burgers *inherits* from HJ: comparison principle, L^{infinity} contraction, Oleinik bound, finite speed, entropy/viscosity selection.

### 5.2 Burgers as the Scalar Core of NS

Burgers captures the *self-advection nonlinearity* of NS (v v_x ↔ u . nabla u) in its simplest form. The structural lessons from Burgers that transfer to NS:
- Self-advection produces steepening (in Burgers: shocks; in NS: vortex stretching).
- Without diffusion, singularities are certain (in Burgers: proven; in NS 3D: open).
- With diffusion, the question is whether smoothing beats steepening (in viscous Burgers: yes, always; in NS 3D: open).
- Conservation-law structure provides contraction (in Burgers: L^1 + L^{infinity}; in NS: partial, via energy inequality).

The gap between Burgers (completely understood) and NS (open regularity problem) is precisely the gap introduced by *vectorization + incompressibility + pressure*. Burgers isolates and resolves the scalar transport mechanism; NS wraps it in structural complexity that remains unresolved.

### 5.3 Summary Table

| Feature                    | Burgers      | HJ    | FP    | PME   | AC    | NS    | MCF   |
|----------------------------|-------------|-------|-------|-------|-------|-------|-------|
| Conservation law           | **Yes**     | No    | Yes   | Yes   | No    | Yes   | No    |
| Self-advection             | **v v_x**   | H(u_x)| b.nabla rho| No | No    | u.nabla u| No |
| L^1 contraction            | **Yes**     | No    | No    | **Yes**| No   | No    | No    |
| L^{infinity} contraction   | **Yes**     | **Yes**| No   | No    | No    | No    | No    |
| Mass conservation          | **Yes**     | No    | Yes   | Yes   | No    | Yes   | No    |
| Energy dissipation (shock) | **Yes**     | No    | N/A   | N/A   | N/A   | Open  | N/A   |
| Shock formation            | **Certain** | Certain| None | None  | None  | Open  | Certain|
| N-wave attractor           | **Yes**     | No    | No    | No    | No    | No    | No    |
| Parameters                 | **0**       | **0** | 2     | 1     | 3     | 2     | **0** |

Burgers is the *unique* architecture with: conservation-law structure + self-advection + L^1 contraction + L^{infinity} contraction + mass conservation + energy dissipation at shocks + N-wave attractor. It is the *richest hyperbolic* architecture in the Atlas.

---

*End of Mode 2: PDE → Extremal Dynamics. Mode 3 (Channels → Constraint Surface) will follow in the next file.*
