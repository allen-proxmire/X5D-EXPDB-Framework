# AD Evaluation: Thin-Film Equation — Mode 3: Channels → Constraint Surface

Allen Proxmire

April 2026

---

## Overview

Mode 3 constructs the constraint surface of the TFE architecture. The TFE constraint surface is the *most structurally nuanced* among the gradient-flow architectures: it inherits the fourth-order smoothing of CH's surface, the degenerate free-boundary geometry of PME's surface, and the conservation structure of both — but it adds a feature that neither ancestor possesses: an *n-dependent closure condition* on the positivity face. For n >= 1 (the physical regime), the surface is fully closed. For 0 < n < 1, the positivity face opens, producing the only *parameter-dependent anomaly* among the gradient-flow architectures in the PDE Atlas.

We continue with:

    partial_t h = -div(h^n nabla Delta h),    n > 0,    h >= 0

---

## 1. Channel Decomposition

### Channel D_4: Fourth-Order Diffusion

    D_4(h) = -div(h^n nabla Delta h)

- **Locality:** Local. Involves h and its spatial derivatives up to fourth order at each point.
- **Linearity:** Nonlinear. The mobility prefactor h^n makes the operator nonlinear. The fourth-order derivative structure (nabla Delta h) is linear in h, but the full operator h^n nabla Delta h is nonlinear through the mobility.
- **Stability role:** Stabilizing. The surface energy E = (1/2)||nabla h||^2 decreases monotonically:

      dE/dt = -integral h^n |nabla Delta h|^2 dx <= 0

  Strictly stabilizing except at equilibrium. The fourth-order character provides k^4 damping — the strongest parabolic smoothing in the PDE Atlas (shared with CH).

- **Scale action:** Doubly state-dependent:
  - *Wavenumber dependence:* Damping rate ~ k^4 (fourth-order). High-frequency modes are damped quadratically faster than in second-order equations (k^4 vs. k^2).
  - *Height dependence:* Damping rate ~ h^n. The damping degenerates at h = 0, freezing the dynamics at the contact line and in the dry region.
  - *Combined:* Effective damping rate ~ h^n k^4. This is the product of two factors — one from the PDE order, one from the degeneracy. No other architecture in the Atlas has this *multiplicative* two-factor scaling.

### Channel C: Conservation

    C: d/dt integral h dx = 0

- **Locality:** Global constraint, locally enforced through the divergence form -div(h^n nabla Delta h).
- **Linearity:** Linear (the integral is a linear functional).
- **Stability role:** Constraining. Couples height decay to support expansion: as ||h||_{L^{infinity}} decreases, the wetted area must increase to maintain constant mass.
- **Scale action:** All-scale coupling. The conservation constraint links the behavior of h across all spatial scales.

### Channel G: Geometric Free Boundary (Contact Line)

    G: Gamma(t) = partial{h(t) > 0}

- **Locality:** Local. The contact-line velocity depends on the local height profile near Gamma(t).
- **Linearity:** Nonlinear.
- **Stability role:** Neutral. The contact line is a geometric consequence of the degeneracy, not an independent dynamical agent. It delineates the wet/dry boundary without exerting independent force.
- **Scale action:** Sets the outer scale of the solution. The contact-line position R(t) ~ t^{beta} determines the extent of the support.

### Channel M: Mobility Exponent n

    M: h^n with n > 0

- **Locality:** N/A (parameter).
- **Linearity:** N/A.
- **Stability role:** Parametric. Selects the degeneracy strength, the spreading rate, and (crucially) whether positivity is preserved.
- **Scale action:** n determines the self-similar exponents alpha and beta, and the contact-angle behavior near Gamma(t). Larger n → stronger degeneracy → slower spreading → more regular contact line.

### Channel Summary Table

| Channel | Symbol | Term / Feature               | Locality | Linearity  | Stability     | Scale Action           |
|---------|--------|------------------------------|----------|------------|---------------|------------------------|
| 4th-order diff. | D_4 | -div(h^n nabla Delta h) | Local    | Nonlinear  | Stabilizing   | h^n k^4 (multiplicative)|
| Conservation    | C   | integral h = const        | Global*  | Linear     | Constraining  | All-scale coupling     |
| Contact line    | G   | Gamma(t) = partial{h>0}  | Local    | Nonlinear  | Neutral       | Outer scale R(t)       |
| Exponent        | M   | n > 0                     | N/A      | N/A        | Parametric    | Sets alpha, beta, positivity |

*Enforced locally through divergence form.

### Channel Count Comparison

| Architecture | Dynamical | Constraint | Geometric | Param. | Total |
|-------------|-----------|------------|-----------|--------|-------|
| PME         | 1 (D_nl)  | 1 (C)     | 1 (G)     | 1 (m)  | 4     |
| **TFE**     | **1 (D_4)**| **1 (C)** | **1 (G)** | **1 (n)**| **4** |
| AC          | 2 (R, S)  | 0          | 0         | 2      | 4     |
| CH          | 2 (R, S)  | 1 (D)     | 0         | 2      | 5     |
| NS          | 2 (A, V)  | 1 (C)     | 1 (P)    | 1      | 5     |

The TFE and PME have *identical channel counts* (4) and *identical channel types* (one dynamical, one constraint, one geometric, one parametric). The only difference is the *order* of the dynamical channel: fourth (TFE) vs. second (PME). This structural parallelism confirms the TFE's position as the fourth-order relative of the PME.

---

## 2. Dissipation Geometry

### 2.1 Gradient-Flow Structure

The TFE is a gradient flow of the surface energy:

    E[h] = (1/2) integral |nabla h|^2 dx

with respect to the *weighted H^{-1} metric* defined by the mobility h^n. Concretely, the dynamics satisfy:

    partial_t h = -grad_{H^{-1}_{h^n}} E[h]

where the weighted H^{-1} metric measures the "cost" of redistributing mass with a mobility that depends on the local height.

### 2.2 The Dissipation Functional

The dissipation rate is:

    D(t) = integral h^n |nabla Delta h|^2 dx

This is a *degenerate quadratic form* in the fourth derivative of h:

- **In the interior** ({h > 0}): h^n > 0 and the form is strictly positive definite. Full fourth-order dissipation.
- **At the contact line** (h → 0): h^n → 0 and the form degenerates. Dissipation is suppressed near the free boundary.
- **In the dry region** (h = 0): No contribution.

The dissipation functional is *spatially stratified* — full-rank in the interior, degenerate at the boundary, zero outside. This is identical in structure to the PME's dissipation (integral |nabla(u^{(m+1)/2})|^2 dx, which degenerates at u = 0) but at fourth order.

### 2.3 Comparison of Dissipation Geometries

| Architecture | Energy Functional                        | Dissipation Functional                    | Degeneracy |
|-------------|------------------------------------------|-------------------------------------------|------------|
| AC          | F = integral [f(phi) + (eps^2/2)\|nabla phi\|^2] | M \|\|mu\|\|^2                    | None       |
| CH          | F = integral [f(phi) + (eps^2/2)\|nabla phi\|^2] | M \|\|nabla mu\|\|^2             | None       |
| PME         | H = integral Phi(u) (entropy)            | (4m/(m-1)) \|\|nabla(u^{(m+1)/2})\|\|^2 | At u = 0   |
| **TFE**     | **E = (1/2)\|\|nabla h\|\|^2**          | **integral h^n \|nabla Delta h\|^2**     | **At h = 0**|

The TFE dissipation is the *fourth-order degenerate* analogue of the PME dissipation. Both degenerate at the zero state; both are strictly positive in the interior; both produce spatially stratified dissipation landscapes. The difference is the order: TFE dissipates the fourth derivative (nabla Delta h), while PME dissipates a fractional power of the first derivative (nabla(u^{(m+1)/2})).

### 2.4 The Hybrid Geometry

The TFE dissipation geometry combines two features that appear separately in the ancestors:

**From CH:** The energy E = (1/2)||nabla h||^2 is the *same* as CH's gradient energy (with epsilon = 1 and without the double-well bulk term f(phi)). The fourth-order structure of the dissipation (involving nabla Delta h) is inherited from CH.

**From PME:** The degeneracy h^n in the dissipation prefactor is inherited from PME. The spatial stratification (full dissipation in interior, zero at boundary) is the same structural feature as PME's degenerate entropy dissipation.

**Unique to TFE:** The *product* h^n |nabla Delta h|^2 combines fourth-order derivative structure with degenerate prefactor. This product is a *new mathematical object* — not reducible to either the CH dissipation (non-degenerate, fourth-order) or the PME dissipation (degenerate, second-order). The product structure is what produces the TFE's unique phenomena: contact-angle selection, fourth-order waiting times, and the positivity question.

---

## 3. Constraint Surface Geometry

### 3.1 Three Geometric Regions

The TFE constraint surface has the same three-region stratification as the PME, but at one higher order of regularity.

**Region A: Interior (h > 0, strictly fourth-order parabolic)**

- Mobility h^n > 0 (non-degenerate in the interior).
- Equation is uniformly fourth-order parabolic on compact subsets of {h > 0}.
- Solutions are C^{infinity}.
- All fourth-order parabolic estimates apply.
- The dissipation is full-rank.

**Constraint surface properties:** Smooth, closed, non-degenerate. All estimates unconditional.

**Region B: Contact Line (h → 0, degenerate fourth-order)**

- Mobility h^n → 0. The equation degenerates.
- Solutions are Holder continuous (C^{alpha}, alpha < 1) across Gamma(t).
- The contact-line velocity is determined by the capillary-pressure gradient.
- The fourth-order structure produces capillary-pressure singularities that are regularized by the degeneracy.
- Positivity of h across the contact line is *n-dependent*: preserved for n >= 1, potentially violated for 0 < n < 1.

**Constraint surface properties:** Degenerate but controlled for n >= 1. The surface narrows (effective dimension decreases) as h → 0. For n >= 1, the narrowing is *sufficient to prevent negative excursions*. For 0 < n < 1, it may be *insufficient*.

**Region C: Dry Region (h = 0 identically)**

- No dynamics. Mobility h^n = 0. The equation reduces to partial_t h = 0.
- Perfectly static until the contact line arrives.

**Constraint surface properties:** Trivially closed. Flat face with no dynamics.

### 3.2 The n-Dependent Closure

The three regions assemble into a constraint surface whose closure depends on n:

**n >= 1 (physical regime):**

The constraint surface is *fully closed*. The four sealing mechanisms:

1. **Fourth-order smoothing** seals the high-frequency face (k^4 damping prevents small-scale blowup).
2. **Degeneracy** seals the contact-line face (h^n → 0 prevents mass from leaking into the dry region faster than finite speed).
3. **Conservation** seals the mass face (integral h = M prevents escape to infinity).
4. **Gradient-flow monotonicity** seals the oscillation/chaos face (dE/dt <= 0 forbids limit cycles and recurrence).

Additionally, for n >= 1, the degeneracy is *strong enough* to seal the positivity face: the mobility vanishes fast enough at h = 0 to prevent the fourth-order operator from driving h below zero.

**0 < n < 1 (weak degeneracy):**

The constraint surface has an *open positivity face*. The four sealing mechanisms above still close the high-frequency, contact-line, mass, and oscillation faces. But the positivity face is *not sealed*: the weak degeneracy may be insufficient to prevent the fourth-order operator (which lacks a maximum principle) from producing negative values of h.

### 3.3 Comparison with PME and CH

| Feature                    | TFE (n >= 1)      | TFE (0 < n < 1)  | PME             | CH              |
|----------------------------|--------------------|-------------------|-----------------|-----------------|
| Surface closure            | Fully closed       | Open (positivity) | Fully closed    | Fully closed    |
| Sealing mechanisms         | 4                  | 3 (positivity open)| 4              | 2               |
| Positivity                 | Preserved          | May fail          | Preserved (comp.)| N/A             |
| Interior regularity        | C^{infinity}       | C^{infinity}      | C^{infinity}    | C^{infinity}    |
| Boundary regularity        | Holder             | Holder            | Holder          | C^{infinity}*   |
| Free boundary              | Yes                | Yes               | Yes             | No              |
| Max. principle              | No (4th order)     | No (4th order)    | Yes (comparison)| No (4th order)  |

*CH has no free boundary; "boundary" regularity is the interface profile regularity, which is smooth.

The key structural observation: the PME achieves closed positivity through the *comparison principle* (available for second-order scalar parabolic equations). The TFE cannot use the comparison principle (fourth-order equations do not have one). Instead, the TFE must seal the positivity face through the *entropy method* — controlling integral h^{1-n} dx or similar functionals that blow up when h approaches zero. This entropy method works for n >= 1 but may fail for 0 < n < 1.

---

## 4. Anomalies and Open Faces

### 4.1 The Single Structural Vulnerability: Positivity (0 < n < 1)

The TFE has *one* potential anomaly: the open positivity face for 0 < n < 1.

**Mechanism:** The fourth-order operator -div(h^n nabla Delta h) does not satisfy a maximum principle. For n >= 1, the strong degeneracy compensates — the mobility h^n vanishes fast enough to prevent the operator from driving h below zero. For 0 < n < 1, the weak degeneracy may be insufficient, and the fourth-order operator can produce *negative undershoot*: h temporarily drops below zero near the contact line before the degeneracy catches up.

**Physical significance:** Negative h is unphysical (negative film thickness). For 0 < n < 1, the TFE architecture may require *regularization* (Van der Waals forces, precursor films, slip models) to maintain physical validity.

**Comparison with other anomalies:**

| Architecture | Anomaly                    | Type           | Structural or Constitutive? |
|-------------|----------------------------|----------------|-----------------------------|
| NS (3D)    | Enstrophy gap              | Regularity     | Architectural               |
| RD          | Multiple open faces        | Constitutive   | Constitutive                |
| **TFE**     | **Positivity (0<n<1)**    | **Positivity** | **Parametric (n-dependent)**|

The TFE anomaly is *parametric*: it can be closed by choosing n >= 1. This is weaker than the NS anomaly (architectural, cannot be closed by parameter choice) and comparable to the RD anomalies (constitutive, can be closed by choosing appropriate kinetics).

### 4.2 Absence of All Other Anomalies

**No oscillatory face:** The gradient-flow structure (dE/dt <= 0) forbids limit cycles, sustained oscillations, and recurrence. The dynamics are monotonically smoothing.

**No Turing face:** Single species (n_species = 1), no reaction channel. Turing instability requires at least two species with differential diffusion and reaction coupling.

**No chaotic face:** Gradient flows are monotone systems. No sensitive dependence on initial conditions in the long-time limit.

**No blowup face (n >= 1):** Mass conservation + energy bounds + fourth-order smoothing prevent concentration of mass. ||h(t)||_{L^{infinity}} is bounded and decaying.

**No nonlocal face:** All channels are local. No Poisson equation, no Green's function, no integral operator.

### 4.3 Summary: TFE Anomaly Profile

| Face              | Status (n >= 1) | Status (0 < n < 1) |
|-------------------|-----------------|--------------------|
| Oscillatory       | Closed          | Closed             |
| Turing            | Closed          | Closed             |
| Chaotic           | Closed          | Closed             |
| Blowup            | Closed          | Closed             |
| Nonlocal          | Closed          | Closed             |
| **Positivity**    | **Closed**      | **Open**           |

For n >= 1: *zero* open faces. Fully closed, anomaly-free.
For 0 < n < 1: *one* open face (positivity). Parametrically anomalous.

---

## 5. Channel Constraints

---

**C1. Fourth-Order Parabolicity**

    The highest-order term is -h^n Delta^2 h, a fourth-order degenerate parabolic operator.
    Damping rate: h^n k^4 at wavenumber k and height h.

*Scope: All TFE solutions.*

---

**C2. Degenerate Mobility**

    M(h) = h^n,    n > 0,    M(0) = 0

The mobility vanishes at h = 0, producing finite-speed propagation and a free boundary.

*Scope: All TFE solutions.*

---

**C3. Finite-Speed Contact-Line Motion (n >= 1)**

    R(t) <= C t^{beta},    beta = 1/(n + 2d)

The contact line cannot advance faster than the self-similar rate.

*Scope: n >= 1, compactly supported initial data.*

---

**C4. Mass Conservation**

    integral h(x, t) dx = M    for all t >= 0

Exact conservation. Total film volume invariant.

*Scope: All TFE solutions (no-flux BC or R^d).*

---

**C5. Energy Dissipation**

    dE/dt = -integral h^n |nabla Delta h|^2 dx <= 0

Exact identity. Surface energy E = (1/2)||nabla h||^2 is a strict Lyapunov functional.

*Scope: All TFE solutions.*

---

**C6. Gradient-Flow Structure**

    partial_t h = -grad_{H^{-1}_{h^n}} E[h]

The TFE is a gradient flow of E with respect to the weighted H^{-1} metric. This forbids limit cycles, chaos, and sustained oscillations.

*Scope: All TFE solutions.*

---

**C7. Curvature-Controlled Smoothing**

    The capillary pressure p = -Delta h satisfies bounds derived from E:
    ||Delta h||_{L^2}^2 bounded by energy + boundary terms

Fourth-order smoothing provides curvature control beyond what second-order diffusion achieves.

*Scope: All TFE solutions, t > 0.*

---

**C8. Positivity Preservation (n >= 1)**

    h_0 >= 0  =>  h(t) >= 0    for all t > 0    [n >= 1]

The strong degeneracy prevents the fourth-order operator from driving h below zero.

*Scope: n >= 1. May fail for 0 < n < 1.*

---

**C9. No Oscillations**

    E[h(t)] monotone decreasing => no limit cycles, no recurrence

Gradient-flow monotonicity forbids all oscillatory dynamics.

*Scope: All TFE solutions.*

---

**C10. No Blowup (n >= 1)**

    ||h(t)||_{L^{infinity}} <= C(n, d, M, E[h_0])    for all t > 0

Mass conservation + energy bounds + interpolation prevent concentration.

*Scope: n >= 1.*

---

**C11. Self-Similar Scaling**

    alpha = d/(n + 2d),    beta = 1/(n + 2d),    alpha = d beta

Exponents uniquely determined by n and d.

*Scope: All TFE, all n > 0.*

---

**C12. Universal Convergence to Source-Type Attractor**

    h(t) → H_*(x / t^{beta}) t^{-alpha}    as t → infinity

for all finite-mass initial data. Universal, independent of initial-data shape.

*Scope: Finite-mass TFE solutions on R^d.*

---

### Channel Constraint Summary

| Label | Constraint                        | Type              | Scope            |
|-------|-----------------------------------|-------------------|------------------|
| C1    | Fourth-order parabolicity         | Structural        | All              |
| C2    | Degenerate mobility               | Structural        | All              |
| C3    | Finite-speed propagation          | Upper bound       | n >= 1           |
| C4    | Mass conservation                 | Exact identity    | All              |
| C5    | Energy dissipation                | Exact identity    | All              |
| C6    | Gradient-flow structure           | Structural        | All              |
| C7    | Curvature-controlled smoothing    | Estimate          | t > 0            |
| C8    | Positivity preservation           | n-dependent       | n >= 1           |
| C9    | No oscillations                   | Monotonicity      | All              |
| C10   | No blowup                        | Bound             | n >= 1           |
| C11   | Self-similar scaling              | Exact exponents   | All              |
| C12   | Universal convergence             | Attractor         | Finite mass      |

**Note:** Constraints C3, C8, and C10 are restricted to n >= 1. This is the *only* architecture in the PDE Atlas where channel constraints carry an explicit parameter restriction. In all other architectures, the constraints either hold universally (AC, CH, PME) or are constitutive-class-dependent (RD).

---

## 6. Comparison with AC, CH, PME, and RD

### 6.1 The 2×2 Hierarchy: Constraint Surface Comparison

|                    | Non-conserved        | Conserved              |
|--------------------|---------------------|------------------------|
| **Non-degenerate** | AC: closed, 4 ch.   | CH: closed, 5 ch.     |
| **Degenerate**     | PME: closed, 4 ch.  | **TFE: closed (n>=1), 4 ch.** |

All four corners of the hierarchy have *closed* constraint surfaces (for their canonical parameter regimes). The TFE is the only corner where the closure is *parameter-dependent* (requiring n >= 1). The other three corners are unconditionally closed.

### 6.2 Surface Closure Mechanisms

| Architecture | Positivity Mechanism     | Smoothing    | Conservation | Gradient Flow |
|-------------|--------------------------|-------------|--------------|---------------|
| AC          | Maximum principle        | k^2         | No           | Yes (L^2)     |
| CH          | N/A (no positivity req.) | k^4         | Yes          | Yes (H^{-1})  |
| PME         | Comparison principle     | u^{m-1} k^2| Yes          | Yes (Wass.)   |
| **TFE**     | **Entropy method (n>=1)**| **h^n k^4** | **Yes**      | **Yes (wt. H^{-1})** |
| NS          | N/A (vector system)      | k^2         | Yes (div-free)| No           |
| RD          | Constitutive             | k^2         | Constitutive | Constitutive  |

The TFE's positivity mechanism (entropy method) is *weaker* than the PME's (comparison principle) because the fourth-order character prevents the comparison principle from applying. This weakness is the structural origin of the n-dependent closure.

### 6.3 The n-Dependent Surface: Unique in the Atlas

The TFE is the *only* architecture in the PDE Atlas whose constraint surface has a *parametric bifurcation*:

- For n >= 1: fully closed. Zero open faces. Structurally equivalent to PME.
- For 0 < n < 1: one open face (positivity). One parametric anomaly.

No other architecture has this feature:
- AC, CH, PME: unconditionally closed for all admissible parameters.
- NS: open face in 3D, but this is a *dimensional* bifurcation (d = 2 vs. d = 3), not a *parametric* one.
- RD: constitutive-dependent closure, but the dependence is on the *functional form* of the kinetics, not on a single scalar parameter.

The TFE's parametric bifurcation at n = 1 is a *new structural phenomenon* in the PDE Atlas: a single scalar parameter determining whether the architecture is self-consistent (n >= 1) or has an open face (0 < n < 1). This makes the TFE a natural *test case* for understanding how structural soundness depends on constitutive parameters.

### 6.4 Bottom-Right Corner Assessment

The TFE, as the bottom-right corner of the 2×2 gradient-flow hierarchy, combines the maximum structural complexity:
- Fourth-order smoothing (from CH) — strongest in the Atlas.
- Degenerate mobility (from PME) — produces free boundary.
- Conservation (from CH and PME) — constrains the dynamics.
- Gradient-flow structure (from all four corners) — seals oscillation/chaos faces.

The cost of this complexity is the *positivity question*: the fourth-order character (from CH) *removes* the maximum principle, while the degeneracy (from PME) *requires* positivity for physical consistency. The tension between these two inherited features is the structural origin of the n-dependent closure — a tension that does not arise in any other corner of the hierarchy, because the other corners either have the maximum principle (AC, PME) or do not require positivity (CH).

---

*End of Mode 3: Channels → Constraint Surface. The AD Criteria and Verdict will follow in the final file.*
