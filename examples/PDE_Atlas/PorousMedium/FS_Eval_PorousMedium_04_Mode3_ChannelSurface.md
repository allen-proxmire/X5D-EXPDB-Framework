# AD Evaluation: Porous Medium Equation — Mode 3: Channels → Constraint Surface

Allen Proxmire

April 2026

---

## Overview

Mode 3 constructs the constraint surface of the PME architecture. The PME constraint surface is the *simplest closed surface* in the PDE Atlas: it has the fewest channels, the fewest faces, and the most uniform closure properties of any nontrivial PDE. Its geometry is dominated by a single structural feature — the *degeneracy boundary* at u = 0 — which simultaneously produces the architecture's most distinctive property (finite-speed propagation) and its most challenging analytical feature (limited regularity at the free boundary). The surface is fully closed, with no open faces of any kind.

We continue with:

    partial_t u = Delta(u^m),    m > 1,    u >= 0

---

## 1. Channel Decomposition

### Channel D_nl: Nonlinear Diffusion

    D_nl(u) = Delta(u^m) = div(m u^{m-1} nabla u)

- **Locality:** Local. Depends on u, nabla u, and Delta u at each point. No integral operators, no nonlocal coupling.
- **Linearity:** Nonlinear. The diffusion coefficient D(u) = m u^{m-1} depends on the solution itself. This is the sole nonlinearity in the PME architecture — and since there are no other channels, it is the *only* operator in the PDE.
- **Stability role:** Unconditionally stabilizing. D_nl decreases all convex entropies, contracts L^1 distances between solutions, and preserves the ordering of solutions. It is the most thoroughly stabilizing channel in the PDE Atlas: there is no direction in function space in which D_nl amplifies, concentrates, or destabilizes.
- **Scale action:** State-dependent and scale-dependent.
  - At density U and scale L: damping rate ~ m U^{m-1} / L^2.
  - High-k modes in regions with U > 0: strongly damped (rate grows as k^2 U^{m-1}).
  - Low-k modes: weakly damped (large-scale rearrangements are slow).
  - At u = 0: damping rate = 0. The vacuum is frozen — no diffusion occurs.

  The scale action has a *multiplicative structure*: the spatial scale L enters as L^{-2} (standard parabolic) and the density scale U enters as U^{m-1} (degenerate). The two factors are independent, producing a two-parameter family of damping rates indexed by (U, L).

### Channel C: Conservation

    C: d/dt integral u dx = 0

- **Locality:** The constraint is global (integral over the domain), but its *enforcement* is local — it follows automatically from the divergence form of the PDE and the no-flux boundary conditions. No nonlocal solve is required.
- **Linearity:** Linear. The integral functional is linear in u.
- **Stability role:** Constraining. Conservation restricts the dynamics to the hyperplane {integral u = M} in function space. It does not directly stabilize or destabilize but constrains the geometry of the flow: the mass must spread (free boundary expands) rather than concentrate (blowup is impossible because spreading + conservation prevents it).
- **Scale action:** Conservation couples all scales: the integral constraint links the behavior of u at every spatial scale. A decrease in the maximum (large-scale) must be compensated by an increase in the support radius (also large-scale). Conservation is a *global accounting constraint* that operates across all scales simultaneously.

### Channel G: Geometric Spreading (Free Boundary)

    G: Gamma(t) = partial{u(t) > 0},    V_n = -(m/(m-1)) partial_n(u^{m-1})

- **Locality:** The free boundary is a *local* geometric feature: its velocity at each point depends on the density gradient at that point. However, the *position* of Gamma(t) depends on the global mass distribution (through conservation).
- **Linearity:** Nonlinear. The free-boundary velocity depends nonlinearly on the density profile near the interface.
- **Stability role:** Neutral. The free boundary is a geometric consequence of the degeneracy — it delineates the boundary between the active region (u > 0, where diffusion operates) and the frozen region (u = 0, where nothing happens). It does not exert an independent dynamical force; it is a *slave* to the density gradient.
- **Scale action:** The free boundary moves at speed V_n ~ t^{beta-1} (decelerating). It sets the *outer scale* of the solution — the maximum extent of the support. All dynamics are confined within the free boundary; outside it, u = 0 identically.

### Channel M: Exponent m

    M: the constitutive exponent m > 1

- **Locality:** N/A (parameter).
- **Linearity:** N/A.
- **Stability role:** Parametric. Larger m produces stronger degeneracy (slower spreading, slower propagation, thicker Barenblatt profiles). All m > 1 are qualitatively equivalent.
- **Scale action:** m sets the self-similar exponents alpha = d/(d(m-1)+2) and beta = 1/(d(m-1)+2), which determine the rate of decay and spreading. Larger m → smaller beta → slower spreading.

### Channel Summary Table

| Channel | Symbol | Term / Feature        | Locality    | Linearity   | Stability       | Scale Action                    |
|---------|--------|-----------------------|-------------|-------------|-----------------|--------------------------------|
| Nonlin. diffusion | D_nl | Delta(u^m)   | Local       | Nonlinear   | Stabilizing     | Rate ~ U^{m-1} k^2             |
| Conservation      | C    | integral u = M| Global*     | Linear      | Constraining    | Couples all scales              |
| Geom. spreading   | G    | Gamma(t), V_n | Local       | Nonlinear   | Neutral (slave) | Sets outer scale R(t) ~ t^beta |
| Exponent          | M    | m > 1         | N/A         | N/A         | Parametric      | Sets alpha, beta                |

*Enforced locally through divergence form.

**Channel count comparison:**

| Architecture | Dynamical Channels | Constraint Channels | Geometric Features | Total |
|--------------|-------------------|--------------------|--------------------|-------|
| PME          | 1 (D_nl)          | 1 (C)              | 1 (G)              | 3+1   |
| AC           | 2 (R, S)          | 0                  | 0                  | 2+2   |
| CH           | 2 (R, S)          | 1 (D)              | 0                  | 3+2   |
| NS           | 2 (A, V)          | 1 (C incompat.)    | 1 (P nonlocal)     | 4+1   |
| RD           | 2 (D, R)          | 0                  | 0                  | 2+2   |

The PME has the *fewest dynamical channels* (one) and the *fewest total channels* of any nontrivial PDE in the Atlas.

---

## 2. Dissipation Geometry

### 2.1 Monotone Decay of All Convex Entropies

The PME dissipation geometry is defined by a single structural property: for every convex function Phi : [0, infinity) → R with Phi(0) = 0:

    d/dt integral Phi(u(x, t)) dx <= 0

This is not a single Lyapunov functional (as in AC, where F[phi] decreases) but an *infinite family* of Lyapunov functionals — one for each convex Phi. The PME dissipates *every* convex entropy simultaneously.

Specific instances:
- Phi(u) = u^p (p > 1): d/dt ||u||_{L^p}^p <= 0.
- Phi(u) = u log u: d/dt integral u log u dx <= 0 (Boltzmann entropy).
- Phi(u) = u^m/(m-1): d/dt H(u) = -(4m/(m-1)) ||nabla(u^{(m+1)/2})||^2 <= 0 (specific dissipation identity).

The dissipation is *strict* for non-constant u: equality holds only for u = const (which, combined with mass conservation, means u = M/|Omega| on bounded domains or u → 0 on R^d).

### 2.2 Geometry of the Dissipation

The dissipation "geometry" of the PME is *ultra-simple*:

**In the interior** (u > 0): The equation is strictly parabolic with diffusion coefficient D(u) = m u^{m-1} > 0. The entropy dissipation rate is strictly positive. All modes are damped. The dissipation is a *full-rank quadratic form* in the gradient of u^{(m+1)/2}.

**At the free boundary** (u = 0): The diffusion coefficient degenerates to zero. The entropy dissipation rate approaches zero. The dynamics slow down and eventually freeze. The dissipation is *degenerate* — it has a *null direction* at u = 0 (the direction of zero density).

**In the vacuum** (u = 0 identically): No dissipation occurs. The region is frozen.

This produces a *spatially stratified dissipation geometry*: full-rank parabolic dissipation in the interior, degenerating to zero at the free boundary, and identically zero in the vacuum. The stratification is controlled by a single scalar — the density u — rather than by the spatial dimension or the wavenumber.

### 2.3 Comparison with Other Architectures

| Architecture | Dissipation Geometry                               | Dimension | Degeneracy            |
|-------------|----------------------------------------------------|-----------|-----------------------|
| AC          | 1D ray: dF/dt = -M\|\|mu\|\|^2                   | 0-simplex | None (non-degenerate) |
| CH          | 1D ray: dF/dt = -M\|\|nabla mu\|\|^2             | 0-simplex | None (non-degenerate) |
| PME         | 1D ray with degenerate boundary: dH/dt <= 0       | 0-simplex | Degenerate at u = 0   |
| NS          | 1D energy + 2D enstrophy (3D)                     | 0 + 2     | None                  |
| RD          | Regime-dependent (ray, loop, or non-monotone)      | Variable  | Constitutive          |

The PME dissipation is topologically a 1D ray (like AC and CH) but has an additional structural feature: *spatial degeneracy*. The dissipation rate is a function of position (through u(x,t)), not just a global scalar. This degeneracy is the Mode 3 signature of the free-boundary property: the dissipation shuts off at the interface because the dynamics shut off there.

---

## 3. Constraint Surface Geometry

### 3.1 Three Geometric Regions

The PME constraint surface has a natural stratification into three regions, corresponding to the three geometric regimes identified in Mode 2.

**Region A: Interior (u > 0, strictly parabolic)**

- The diffusion coefficient D(u) = m u^{m-1} > 0.
- The equation is uniformly parabolic on compact subsets of {u > 0}.
- Solutions are C^{infinity}.
- All entropy dissipation estimates hold with strict inequality.
- Standard parabolic theory applies.

**Constraint surface properties:** Fully closed, non-degenerate, smooth. All estimates are unconditional. No open faces.

**Region B: Free Boundary (u = 0 from the positive side, degenerate parabolic)**

- The diffusion coefficient degenerates: D(u) → 0 as u → 0.
- Solutions are Holder continuous (C^{alpha} for some alpha < 1) but typically not C^1.
- The free-boundary velocity is determined by the Darcy law V_n = -(m/(m-1)) partial_n(u^{m-1}).
- Waiting-time phenomena can occur.

**Constraint surface properties:** Closed but *degenerate*. The constraint surface narrows at the free boundary — the effective dimension of the admissible dynamics decreases as the equation becomes less parabolic. The degeneracy is *controlled*: the Holder regularity exponent and the free-boundary regularity have been established (Caffarelli–Friedman, Caffarelli–Vazquez–Wolanski), and no pathology occurs.

**Region C: Vacuum (u = 0 identically)**

- No dynamics. D(u) = 0. The PDE reduces to partial_t u = 0.
- The vacuum is perfectly static until the free boundary reaches it.

**Constraint surface properties:** Trivially closed. The vacuum region contributes a *flat face* to the constraint surface — a face where nothing happens.

### 3.2 The Single Closed Constraint Surface

The three regions fit together into a *single closed constraint surface*:

- Region A (interior) is the *smooth interior* of the surface.
- Region B (free boundary) is the *degenerate edge* of the surface — a lower-dimensional boundary where the surface narrows.
- Region C (vacuum) is the *flat exterior* — outside the surface entirely.

The surface is closed because:

1. **Degeneracy seals the u = 0 boundary.** The diffusion shuts off at u = 0, preventing the solution from leaking into the vacuum. The free boundary is an *impermeable wall* from the inside — mass cannot cross it faster than the Darcy velocity allows.

2. **Entropy dissipation prevents interior escape.** Inside {u > 0}, all convex entropies decrease. The solution cannot concentrate (which would increase L^p norms) or oscillate (which would increase the entropy). The only permitted motion is *smoothing and spreading*.

3. **L^1 contraction prevents separation.** Two solutions starting close together remain close forever. No instability can drive solutions apart.

4. **Mass conservation prevents escape to infinity.** The total mass is fixed. The solution cannot dump mass to infinity or create mass from nothing.

These four mechanisms — degeneracy, entropy, contraction, conservation — seal the surface from every direction. There is no direction in the function space in which the PME dynamics can escape.

### 3.3 Why PME Has No Open Faces

**No oscillatory face:** The PME has no reaction channel, no coupling, and no mechanism for oscillation. All convex entropies are monotone decreasing. The dynamics are *irreversibly smoothing*. Oscillations require a non-monotone energy landscape; the PME has a *strictly monotone* entropy landscape.

**No Turing face:** Turing patterns require at least two species (n >= 2) with differential diffusion. The PME has one species (n = 1) and no reaction. Spatial patterning is structurally impossible.

**No blowup face:** The L^{infinity} norm of u *decays* as t^{-alpha}. The combination of mass conservation (fixed total mass) and spreading (support expands) forces the maximum to decrease. There is no mechanism for concentration or blowup.

**No nonlocal face:** All PME channels are local. There is no elliptic constraint, no Poisson equation, no pressure channel. The architecture is fully local at both formulation and solution levels.

**No chaotic face:** The L^1 contraction property ensures Lipschitz stability — no sensitive dependence on initial conditions. The dynamics are *contractive*, not chaotic.

---

## 4. Anomalies and Open Faces

### 4.1 Explicit Absence of All Anomalies

We verify the absence of each type of anomaly that appears elsewhere in the PDE Atlas:

| Anomaly Type                  | NS Status           | RD Status           | PME Status         |
|-------------------------------|---------------------|---------------------|---------------------|
| Nonlocal channel              | Yes (pressure)      | No                  | **No**              |
| Destabilizing sub-channel     | Yes (vortex stretch) | Constitutive       | **No**              |
| Open oscillatory face         | When forced         | Multi-species       | **No**              |
| Open Turing face              | No                  | n >= 2              | **No**              |
| Open blowup face              | 3D (open)           | Super-linear R      | **No**              |
| Missing Lyapunov wall         | When forced         | Generic             | **No** (entropy)    |
| Missing max. principle wall   | Yes (vector system) | n >= 2              | **No** (comparison) |
| Missing conservation wall     | N/A                 | Generic             | **No** (conserved)  |

The PME has *zero* anomalies. Every potential anomaly is either structurally absent (nonlocal channel, destabilizing sub-channel, Turing face) or sealed by a specific mechanism (blowup sealed by decay, oscillation sealed by entropy, chaos sealed by contraction).

### 4.2 PME Among the Fully Closed Architectures

Only three PDE architectures in the PDE Atlas have *fully closed* constraint surfaces with no open faces:

| Architecture | Constraint Surface | Closing Mechanisms                         |
|-------------|-------------------|--------------------------------------------|
| AC          | Closed            | Maximum principle + Lyapunov (F)           |
| CH          | Closed            | Fourth-order smoothing + Lyapunov (F)      |
| **PME**     | **Closed**        | **Degeneracy + entropy + L^1 contraction + conservation** |

The PME achieves closure through a *different and richer* set of mechanisms than AC or CH. AC relies on the maximum principle (specific to scalar second-order parabolic equations). CH relies on fourth-order smoothing (specific to biharmonic equations). The PME relies on *four* independent mechanisms — any one of which provides partial closure, and which together provide complete closure. This makes the PME closure *more robust* than AC's or CH's: it does not depend on a single structural feature but on a web of reinforcing properties.

---

## 5. Channel Constraints

---

**C1. Degenerate Parabolicity**

    D(u) = m u^{m-1} >= 0,    with D(0) = 0 for m > 1

The diffusion degenerates at u = 0. The equation is parabolic where u > 0 and degenerate where u = 0. This degeneracy is the structural origin of finite-speed propagation and free boundaries.

*Scope: All PME solutions, all m > 1.*

---

**C2. Finite-Speed Propagation**

    supp(u(t)) subset B(0, R(t)),    R(t) <= C t^{beta},    beta = 1/(d(m-1)+2)

No information propagates faster than the Barenblatt rate. Compact support is preserved.

*Scope: All compactly supported initial data.*

---

**C3. Free-Boundary Velocity Law**

    V_n = -(m/(m-1)) partial_n(u^{m-1})    at smooth points of Gamma(t)
    V_n >= 0    (free boundary only advances)

The free-boundary velocity is slaved to the pressure gradient. The interface is irreversible — it only expands.

*Scope: All PME solutions with compact support.*

---

**C4. Mass Conservation**

    integral u(x, t) dx = M    for all t >= 0

Exact conservation. The total mass M is an invariant and the sole parameter of the Barenblatt attractor.

*Scope: All PME solutions (with no-flux BC or on R^d).*

---

**C5. Entropy Dissipation**

    d/dt integral Phi(u) dx <= 0    for all convex Phi with Phi(0) = 0

All convex entropies are monotone decreasing. The specific dissipation identity:

    dH/dt = -(4m/(m-1)) ||nabla(u^{(m+1)/2})||^2

where H = integral u^m/(m-1) dx.

*Scope: All PME solutions.*

---

**C6. L^1 Contraction**

    ||u(t) - v(t)||_{L^1} <= ||u_0 - v_0||_{L^1}    for all t >= 0

The strongest stability property in the PDE Atlas. Implies uniqueness, continuous dependence, and convergence.

*Scope: All pairs of PME solutions.*

---

**C7. Comparison Principle**

    u_0 <= v_0  =>  u(t) <= v(t)    for all t >= 0

The ordering of solutions is preserved. Provides upper and lower bounds by comparison with Barenblatt profiles.

*Scope: All pairs of PME solutions.*

---

**C8. Positivity Preservation**

    u_0 >= 0  =>  u(t) >= 0    for all t >= 0

Non-negative initial data remains non-negative. The vacuum state u = 0 is an *impermeable floor* — the dynamics cannot drive u below zero.

*Scope: All PME solutions.*

---

**C9. No Oscillations**

    All convex entropy functionals are monotone decreasing (C5)
    L^1 distances are non-increasing (C6)
    ⟹ No limit cycles, no recurrence, no oscillatory dynamics

*Scope: All PME solutions.*

---

**C10. No Blowup**

    ||u(t)||_{L^{infinity}} <= C M^{2beta} t^{-alpha} → 0    as t → infinity

The L^{infinity} norm decays algebraically. Blowup is structurally impossible.

*Scope: All PME solutions with finite mass.*

---

**C11. Barenblatt Scaling**

    alpha = d/(d(m-1)+2),    beta = 1/(d(m-1)+2),    alpha = d beta

The self-similar exponents are uniquely determined by m and d. They are architectural constants.

*Scope: All PME, all m > 1, all d >= 1.*

---

**C12. Universal Convergence to Barenblatt**

    u(t) → B(t; M)    as t → infinity    for all u_0 in L^1, u_0 >= 0, integral u_0 = M

Universal convergence to the Barenblatt profile. All initial-data dependence (beyond total mass) is forgotten.

*Scope: All finite-mass PME solutions on R^d.*

---

### Channel Constraint Summary

| Label | Constraint                        | Type              | Scope            |
|-------|-----------------------------------|-------------------|------------------|
| C1    | Degenerate parabolicity           | Structural        | All m > 1        |
| C2    | Finite-speed propagation          | Upper bound       | Compact support  |
| C3    | Free-boundary velocity law        | Slaved            | Compact support  |
| C4    | Mass conservation                 | Exact identity    | All              |
| C5    | Entropy dissipation               | Monotonicity      | All              |
| C6    | L^1 contraction                   | Contraction       | All              |
| C7    | Comparison principle              | Order preservation| All              |
| C8    | Positivity preservation           | Invariance        | All              |
| C9    | No oscillations                   | Monotonicity      | All              |
| C10   | No blowup                        | Decay bound       | All finite mass  |
| C11   | Barenblatt scaling                | Exact exponents   | All              |
| C12   | Universal convergence             | Attractor         | All finite mass  |

**All twelve constraints are unconditional** — no dimensional restrictions, no conditional hypotheses, no constitutive sub-class restrictions. This is the most uniform set of channel constraints in the PDE Atlas.

---

## 6. Comparison with AC, CH, and RD

### 6.1 Surface Closure Across the Atlas

| Architecture | Surface Status | Open Faces | Closing Mechanisms                         | Channels |
|-------------|----------------|------------|-------------------------------------------|----------|
| PME         | Closed         | 0          | Degeneracy + entropy + contraction + cons. | 3+1      |
| AC          | Closed         | 0          | Maximum principle + Lyapunov               | 4        |
| CH          | Closed         | 0          | Fourth-order smoothing + Lyapunov          | 5        |
| NS          | Open (3D)      | 1          | Viscosity (insufficient 3D)                | 5        |
| RD          | Constitutive   | 3+         | None universal                             | 4        |

### 6.2 Structural Comparison

| Feature                    | PME             | AC              | CH              | RD              |
|----------------------------|-----------------|-----------------|-----------------|-----------------|
| Interface type             | Sharp (free bdy)| Diffuse (tanh)  | Diffuse (tanh)  | Constitutive    |
| Propagation speed          | Finite          | Infinite        | Infinite        | Constitutive    |
| Conservation               | Yes             | No              | Yes             | Constitutive    |
| Reaction channel           | None            | Yes (cubic)     | Yes (via mu)    | Yes (arbitrary) |
| Gradient flow              | Yes (Wasserstein)| Yes (L^2)      | Yes (H^{-1})   | Generically no  |
| Lyapunov structure         | All conv. entropies| Single F     | Single F        | Generically none|
| Attractor                  | Barenblatt      | phi = ±1        | Phase-separated | Constitutive    |
| L^1 contraction            | Yes             | No*             | No*             | No*             |
| Waiting time               | Yes             | No              | No              | No              |
| Anomalies                  | 0               | 0               | 0               | 0 (class level) |

*AC, CH, and RD do not have the L^1 contraction property in general (it is specific to scalar conservation laws and degenerate parabolic equations).

### 6.3 The PME's Unique Structural Position

The PME occupies a unique position in the PDE Atlas: it is the *simplest PDE with nontrivial geometry*. Its one dynamical channel (nonlinear diffusion) produces one geometric feature (free boundary), one attractor (Barenblatt), and one asymptotic behavior (self-similar spreading). No other architecture achieves this level of structural economy.

The PME's constraint surface is closed by *four independent mechanisms* — more than any other closed architecture. AC uses two (maximum principle + Lyapunov), CH uses two (fourth-order smoothing + Lyapunov). The PME uses four (degeneracy + entropy + contraction + conservation). This makes the PME closure the *most robust* in the Atlas: removing any one mechanism still leaves the others to provide partial closure, and the closure degrades gracefully rather than failing catastrophically.

The PME's distinctive features — finite-speed propagation, sharp interfaces, waiting times, degenerate regularity at the free boundary — have no counterpart in any other FS-evaluated architecture. These features are all consequences of the *single structural commitment* to degenerate diffusion (PME-3, PME-8), demonstrating the high leverage of the degeneracy axiom: one structural choice produces an entire suite of novel geometric and dynamical properties.

---

*End of Mode 3: Channels → Constraint Surface. The AD Criteria and Verdict will follow in the final file.*
