# AD Evaluation: Thin-Film Equation — Mode 1: Axiom → Envelope

Allen Proxmire

April 2026

---

## Overview

Mode 1 traces the path from the TFE axioms (TFE-1 through TFE-8) to the architectural envelope. The TFE envelope sits at a precise intermediate position in the PDE Atlas: tighter than the RD envelope (which has multiple open faces) and tighter than the NS envelope (which has an open enstrophy face in 3D), but less uniformly tight than the PME envelope (which is sealed by four independent mechanisms with no structural subtleties). The TFE envelope's distinctive feature is the *positivity question*: whether h remains non-negative depends on the mobility exponent n, producing an n-dependent closure that is unique in the Atlas.

Throughout:

    partial_t h = -div(h^n nabla Delta h),    n > 0,    h >= 0

on Omega subset R^d (d = 1, 2) with no-flux boundary conditions.

---

## 1. Forbidden Configurations

### F1. Negative Heights (Physical Regime)

**Axiom source:** TFE-1 (Continuum), TFE-3 (Degenerate Diffusion), TFE-8 (n > 0).

The film height h represents a physical thickness and must be non-negative. For the TFE, positivity preservation is a *structural question* that depends on n:

- **n >= 1 (strong degeneracy):** The mobility h^n vanishes fast enough at h = 0 to prevent the fourth-order operator from driving h below zero. Solutions with h_0 >= 0 satisfy h(t) >= 0 for all t > 0 (proven for n >= 1 in d = 1, and in various settings for higher d). **Negative heights forbidden.**

- **0 < n < 1 (weak degeneracy):** The mobility vanishes slowly, and the fourth-order operator — which lacks a maximum principle — can push h below zero. Solutions may develop *negative* excursions. **Negative heights may not be forbidden in this regime** without additional regularization.

The positivity distinction is the TFE's most important n-dependent structural feature. For the physical case n = 3, positivity is preserved — negative heights are forbidden. The AD evaluation treats the n >= 1 regime as the canonical (and physically relevant) architecture.

### F2. Nonlocal Diffusion

**Axiom source:** TFE-2 (Locality).

The operator -div(h^n nabla Delta h) involves only local derivatives up to fourth order. Nonlocal operators (fractional Laplacians, integral kernels, nonlocal pressure solves) are forbidden. The TFE is fully local — no Green's function, no Poisson equation, no integral constraint.

### F3. Second-Order Diffusion Only

**Axiom source:** TFE-3 (Fourth-Order Degenerate Diffusion).

The TFE is a *fourth-order* PDE. The highest-order term is the biharmonic Delta^2 h (weighted by h^n). Second-order diffusion alone (Delta(h^m), as in the PME) is outside the TFE architecture. The fourth-order character is structural — it arises from the physics of surface tension (capillary pressure p = -Delta h produces a fourth-order flux when composed with the Darcy law).

Removing the fourth-order term and replacing it with a second-order term would produce the PME ��� a different architecture occupying the bottom-left corner of the gradient-flow hierarchy.

### F4. Infinite-Speed Free-Boundary Motion (n >= 1)

**Axiom source:** TFE-3, TFE-8 (Degenerate Diffusion, n >= 1).

For n >= 1, the mobility degeneracy h^n is strong enough to enforce *finite-speed propagation*: if h_0 has compact support, then h(t) has compact support for all t > 0, and the contact line Gamma(t) = partial{h > 0} moves at finite speed.

The propagation speed of the contact line is bounded:

    R(t) <= C t^{beta},    beta = 1/(n + 2d)    [general scaling]

For d = 1: beta = 1/(n + 4) (from self-similar solutions).

Infinite-speed propagation — instantaneous influence at arbitrarily distant points — is forbidden in the n >= 1 regime. For 0 < n < 1, the degeneracy may be insufficient and the propagation speed may be infinite (solutions may have non-compact support even for compactly supported initial data).

### F5. Reaction Terms

**Axiom source:** TFE-7 (No Reaction).

The TFE is a pure fourth-order diffusion equation. Reaction terms R(h), source/sink terms, evaporation/condensation, Marangoni forcing, and Van der Waals interactions are all outside the standard TFE architecture. The dynamics are driven entirely by capillary-pressure-gradient-driven flow.

### F6. Forcing Terms

**Axiom source:** TFE-7 (No Reaction/Forcing).

External forces f(x, t) are forbidden. The TFE is autonomous — self-generated dynamics from initial data and the degenerate fourth-order diffusion.

### F7. Finite-Time Blowup (Physical Regime)

**Axiom source:** TFE-3, TFE-4, TFE-7.

In the physical regime (n >= 1), the TFE has no blowup mechanism:

1. **Mass conservation:** ||h(t)||_{L^1} = M for all t.
2. **Energy dissipation:** E[h(t)] = (1/2)||nabla h(t)||^2 decreases. Since E >= 0, it remains bounded.
3. **L^1 + energy control:** Combined mass and energy control gives uniform bounds on h in appropriate Sobolev spaces.
4. **No reaction to amplify:** Without a reaction term, there is no mechanism to concentrate mass faster than the fourth-order diffusion can spread it.

The fourth-order smoothing (k^4 damping) is *stronger* than the PME's second-order smoothing (k^2 damping) at controlling small-scale concentration. Blowup is structurally impossible in the physical regime because the architecture has no amplification mechanism — only smoothing and spreading.

### F8. Oscillations or Patterns

**Axiom source:** TFE-7 (No Reaction), TFE-3 (pure diffusion).

With no reaction channel, no coupling, and no forcing, the TFE cannot produce:
- Sustained oscillations (require reaction dynamics).
- Turing patterns (require n >= 2 species + reaction coupling).
- Traveling waves with selected speed (require bistable reaction).
- Spatiotemporal chaos (require oscillatory kinetics).

The TFE dynamics are monotone: the surface energy E decreases along every trajectory. No oscillation or complexity generation is possible.

### F9. Non-Conservation

**Axiom source:** TFE-4 (Conservation).

The divergence form partial_t h = -div(h^n nabla Delta h) with no-flux boundary conditions ensures:

    d/dt integral h dx = 0

Total film volume is exactly conserved. Mass creation (condensation) or destruction (evaporation) is forbidden.

### F10. Non-Degenerate Mobility

**Axiom source:** TFE-3, TFE-8 (Degenerate Diffusion, n > 0).

The mobility M(h) = h^n vanishes at h = 0 for all n > 0. Non-degenerate mobility (M = const > 0, corresponding to n = 0 or constant-coefficient fourth-order diffusion) is outside the standard TFE architecture. The degeneracy is structural: it produces the free boundary, the finite-speed propagation, and the contact-line geometry that define the TFE's identity.

Without degeneracy (n = 0), the equation becomes partial_t h = -Delta^2 h — the linear biharmonic equation, which has infinite propagation speed, no free boundary, and C^{infinity} smoothing. This is the CH analogue of the heat equation being the m = 1 limit of the PME.

### Summary of Forbidden Configurations

| Label | Forbidden Configuration                 | Excluding Axiom(s)     |
|-------|----------------------------------------|------------------------|
| F1    | Negative heights (n >= 1)              | TFE-1, TFE-3, TFE-8   |
| F2    | Nonlocal diffusion                     | TFE-2                  |
| F3    | Second-order diffusion only            | TFE-3                  |
| F4    | Infinite-speed propagation (n >= 1)    | TFE-3, TFE-8           |
| F5    | Reaction terms                         | TFE-7                  |
| F6    | Forcing terms                          | TFE-7                  |
| F7    | Finite-time blowup (physical regime)   | TFE-3, TFE-4, TFE-7   |
| F8    | Oscillations / patterns                | TFE-7                  |
| F9    | Non-conservation                       | TFE-4                  |
| F10   | Non-degenerate mobility                | TFE-3, TFE-8           |

---

## 2. Necessary Configurations

### N1. Fourth-Order Diffusion

**Source:** TFE-3.

The TFE is intrinsically fourth-order: the highest spatial derivative is Delta^2 h (the bilaplacian), arising from the composition of the capillary pressure p = -Delta h with the divergence of the Darcy flux div(h^n nabla p). In Fourier space, the damping rate of mode k is:

    sigma(k) ~ -h^n k^4    [leading order, for spatially uniform h]

The k^4 damping is *stronger* than the PME's k^2 at high wavenumbers and *weaker* at low wavenumbers. This fourth-order character is architecturally necessary — it cannot be reduced to second order without changing the physics (removing the capillary-pressure mechanism).

### N2. Degenerate Mobility

**Source:** TFE-3, TFE-8.

The mobility M(h) = h^n vanishes at h = 0 for all n > 0. This degeneracy is a permanent structural feature: every TFE solution has D_4 → 0 wherever h → 0. The degeneracy produces:
- Finite-speed propagation of the contact line (for n >= 1).
- Compact support preservation (for n >= 1).
- Sharp free boundary (contact line between wet and dry regions).

### N3. Mass Conservation

**Source:** TFE-4.

    integral h(x, t) dx = M    for all t >= 0

The total film volume is an exact invariant. This constraint couples the height decay to the support expansion: as the film thins (||h||_{L^{infinity}} decreases), the wetted area must expand to accommodate the conserved mass.

### N4. Free-Boundary (Contact Line) Formation

**Source:** TFE-3, TFE-8 (for n >= 1).

Every TFE solution with compactly supported initial data develops a contact line Gamma(t) = partial{h > 0}. The contact line is a *sharp* interface — h transitions from positive values to exactly zero (no exponentially small tails). The contact line is the TFE's signature geometric feature, analogous to the PME's free boundary but occurring at fourth order.

### N5. Finite-Speed Contact-Line Propagation

**Source:** TFE-3, TFE-8 (n >= 1).

The contact line moves at finite speed. For self-similar source-type solutions in d = 1:

    R(t) ~ t^{1/(n+4)}

The spreading exponent beta = 1/(n+4) is *smaller* than the PME exponent beta_PME = 1/(m+1) for comparable parameters — the fourth-order diffusion is intrinsically slower at large scales because it operates through pressure gradients (fourth derivative) rather than direct density gradients (second derivative).

### N6. Gradient-Flow Structure

**Source:** TFE-3, TFE-4.

The TFE is a gradient flow of the surface energy:

    E[h] = (1/2) integral |nabla h|^2 dx

with respect to the weighted H^{-1} metric defined by the mobility h^n. The gradient-flow structure guarantees:
- E[h(t)] is monotone non-increasing.
- Stationary solutions satisfy nabla Delta h = 0 wherever h > 0 (constant pressure, flat film).
- No limit cycles, no chaos, no recurrence.

### N7. Energy Dissipation Identity

**Source:** TFE-3, TFE-4, N6.

    dE/dt = -integral h^n |nabla Delta h|^2 dx <= 0

This is an *exact identity* (not an inequality) for smooth solutions. The dissipation rate is strictly negative except at equilibrium (nabla Delta h = 0 in {h > 0}). The identity is the TFE analogue of the Lyapunov identities in AC (dF/dt = -M||mu||^2), CH (dF/dt = -M||nabla mu||^2), and PME (dH/dt = -(4m/(m-1))||nabla(u^{(m+1)/2})||^2).

### N8. Self-Similar Spreading

**Source:** TFE-3, TFE-4, TFE-8.

For d = 1, the TFE admits source-type self-similar solutions:

    h(x, t) = t^{-alpha} H(x / t^{beta})

with alpha = 1/(n+4), beta = 1/(n+4). The profile H(eta) is a compactly supported function determined by a fourth-order ODE. Generic finite-mass solutions converge to the self-similar profile as t → infinity (analogous to the PME's Barenblatt convergence).

### N9. High-Frequency Smoothing

**Source:** TFE-3.

The fourth-order operator damps high-frequency modes at rate h^n k^4. For any h > 0, the damping at wavenumber k is *superlinear* in k^2 — stronger than the PME's k^2 damping. This provides:
- Instantaneous smoothing of the interior {h > 0} (solutions become C^{infinity} inside the support for t > 0).
- Control of the nonlinearity: the k^4 damping overwhelms any polynomial growth in the nonlinear terms at high wavenumbers.

### N10. No Oscillations, No Chaos

**Source:** TFE-7, N6 (gradient-flow structure).

The gradient-flow structure (N6) forbids:
- Limit cycles (E decreasing → no periodic orbits with E > E_{min}).
- Sustained oscillations (E monotone → no recurrence).
- Chaos (gradient flows are monotone → no sensitive dependence in the long-time limit).

The TFE dynamics are *monotonically simplifying*: the surface energy decreases, the film flattens, and the contact line expands, until the film reaches a flat equilibrium (h = M / |support|).

### Summary of Necessary Configurations

| Label | Necessary Configuration                     | Source               |
|-------|---------------------------------------------|----------------------|
| N1    | Fourth-order diffusion (k^4 damping)        | TFE-3                |
| N2    | Degenerate mobility (h^n, n > 0)            | TFE-3, TFE-8        |
| N3    | Mass conservation                           | TFE-4                |
| N4    | Contact-line formation                       | TFE-3, TFE-8        |
| N5    | Finite-speed propagation (n >= 1)            | TFE-3, TFE-8        |
| N6    | Gradient-flow structure                      | TFE-3, TFE-4        |
| N7    | Energy dissipation identity                  | TFE-3, TFE-4        |
| N8    | Self-similar spreading                       | TFE-3, TFE-4, TFE-8 |
| N9    | High-frequency smoothing (k^4)              | TFE-3                |
| N10   | No oscillations, no chaos                    | TFE-7, N6            |

---

## 3. Envelope Inequalities (E1–E10)

---

**E1. Energy Dissipation Identity**

    E[h(t)] + integral_0^t integral h^n |nabla Delta h|^2 dx ds = E[h_0]

Exact identity. The total surface energy at time t plus the cumulative dissipation equals the initial surface energy. No gap, no anomalous dissipation (for smooth or appropriate weak solutions).

---

**E2. Mass Conservation Identity**

    integral h(x, t) dx = M    for all t >= 0

Exact identity. The total film volume is invariant.

---

**E3. Fourth-Order Smoothing Estimate**

For the linear part (constant mobility, h = h_0 > 0):

    ||nabla^k h(t)||_{L^2} <= C_k t^{-k/4} ||h_0||_{L^2}    for t > 0, k >= 0

The fourth-order smoothing regularizes at rate t^{-k/4} — each derivative costs t^{-1/4} (compared to t^{-1/2} for second-order diffusion). The smoothing is *slower per derivative* than second-order diffusion but *applies to higher derivatives* — the net effect at high wavenumbers (k^4 damping) is stronger.

---

**E4. Finite-Speed Propagation Bound (n >= 1)**

For compactly supported initial data:

    supp(h(t)) subset B(0, R(t)),    R(t) <= C(n, d, M) t^{beta}

with beta = 1/(n + 2d) (general scaling) or beta = 1/(n+4) for d = 1 source-type solutions.

The contact line cannot advance faster than the self-similar rate. This is the TFE speed limit, analogous to the PME's Barenblatt speed limit.

---

**E5. Self-Similar Scaling Laws**

For d = 1:

    alpha = 1/(n + 4)    (height decay exponent)
    beta = 1/(n + 4)     (spreading exponent)
    alpha = beta          (mass conservation: alpha + beta = 2 beta in 1D requires alpha = beta)

For general d:

    alpha = d/(n + 2d)    (height decay)
    beta = 1/(n + 2d)     (spreading)
    alpha = d beta         (mass conservation coupling)

These exponents are architecturally determined by n and d alone.

---

**E6. Entropy/Energy Functional Inequalities**

The surface energy E = (1/2)||nabla h||^2 provides:

    ||nabla h(t)||_{L^2}^2 <= 2 E[h_0]    for all t >= 0

Higher-order entropy functionals (e.g., integral h^{alpha} dx for appropriate alpha) may also be dissipated, depending on n and d. For the specific entropy H = integral h log h dx (when well-defined):

    dH/dt <= 0    [under appropriate conditions]

The entropy structure is *richer* than a single Lyapunov functional but not as universal as the PME's (which dissipates *all* convex entropies).

---

**E7. Curvature Bounds from Energy**

The capillary pressure p = -Delta h satisfies:

    ||p||_{L^2}^2 = ||Delta h||_{L^2}^2

and through integration by parts:

    integral |Delta h|^2 dx <= C (||nabla h||_{L^2}^2 + boundary terms)

The energy E = (1/2)||nabla h||^2 provides an *indirect* bound on the curvature. Combined with the energy dissipation (E1), this gives uniform-in-time control of ||Delta h||_{L^2} under appropriate conditions.

---

**E8. No-Blowup Inequality (Physical Regime)**

For n >= 1 on bounded domains:

    ||h(t)||_{L^{infinity}} <= C(n, M, |Omega|, E[h_0])    for all t > 0

The L^{infinity} bound follows from:
1. Mass conservation (||h||_{L^1} = M).
2. Energy bound (||nabla h||_{L^2}^2 <= 2E[h_0]).
3. Sobolev/Gagliardo-Nirenberg interpolation: ||h||_{L^{infinity}} <= C ||h||_{L^1}^{theta} ||nabla h||_{L^2}^{1-theta} in appropriate dimensions.

Blowup is structurally impossible because the fourth-order smoothing + conservation + energy bound provide sufficient control.

---

**E9. Monotone Decay of Surface Energy**

    E[h(t_2)] <= E[h(t_1)]    for all t_2 >= t_1 >= 0

Follows directly from E1 (dE/dt <= 0). The surface energy is a strict Lyapunov functional. The film surface becomes monotonically flatter over time.

---

**E10. Positivity Conditions (n-Dependent)**

The preservation of h >= 0 depends on the mobility exponent n:

**n >= 1 (physical regime, including n = 3):**

    h_0 >= 0  =>  h(t) >= 0    for all t > 0

Positivity is preserved. The degeneracy h^n is strong enough to prevent the fourth-order operator from driving h below zero. The proof uses the *entropy method*: the functional integral h^{1-n} dx (or integral log h dx for n = 1) is controlled by the energy dissipation.

**0 < n < 1 (weak degeneracy):**

    h_0 >= 0  does NOT guarantee  h(t) >= 0

Positivity may fail. The fourth-order operator, lacking a maximum principle, can produce negative excursions of h. Physical regularization (Van der Waals forces, slip models) may be needed to restore positivity.

**Structural role:** E10 is the TFE's *n-dependent closure condition*. For n >= 1, it seals the positivity face of the envelope. For 0 < n < 1, it leaves the positivity face *open* — an n-dependent anomaly unique to the TFE among FS-evaluated architectures.

---

### Envelope Summary

The TFE envelope is defined by ten constraints (E1–E10) organized into three tiers:

**Tier 1 — Hard Constraints (exact, unconditional for all n > 0):**
- E1: Energy dissipation identity (exact).
- E2: Mass conservation (exact).
- E9: Monotone energy decay (Lyapunov).

**Tier 2 — Structural Properties (n >= 1 regime):**
- E3: Fourth-order smoothing estimate.
- E4: Finite-speed propagation bound.
- E5: Self-similar scaling laws.
- E8: No-blowup inequality.
- E10: Positivity preservation (n >= 1 only).

**Tier 3 — Supplementary Bounds:**
- E6: Entropy/energy functional inequalities.
- E7: Curvature bounds from energy.

**The n-dependent structure:** The TFE envelope has a *bifurcation* at n = 1:

- **n >= 1:** The envelope is *fully closed*. Positivity is preserved (E10), finite-speed propagation holds (E4), blowup is impossible (E8), and the gradient-flow structure seals all faces. The TFE is structurally analogous to the PME in this regime — fully closed, anomaly-free, with a universal self-similar attractor.

- **0 < n < 1:** The envelope has an *open positivity face*. Solutions can become negative, potentially invalidating the physical interpretation. The architecture requires regularization (additional physics) to close this face. This is structurally analogous to the NS 3D enstrophy gap — an open face where the architecture's self-consistency is not guaranteed by the axioms alone.

---

## 4. Central Architectural Finding

### 4.1 The TFE's Position in the PDE Atlas

The TFE envelope occupies a precise intermediate position:

| Architecture | Envelope Status          | Open Faces             | Sealing Mechanism              |
|-------------|--------------------------|------------------------|-------------------------------|
| ED          | Closed (static)          | 0                      | Unique factorization           |
| PME         | Closed (all d, m > 1)    | 0                      | Degeneracy + entropy + L^1 + cons. |
| AC          | Closed (all d <= 3)      | 0                      | Max. principle + Lyapunov      |
| CH          | Closed (all d <= 3)      | 0                      | 4th-order smooth. + Lyapunov   |
| **TFE**     | **Closed for n >= 1**    | **0 (n>=1); 1 (n<1)** | **Degeneracy + 4th-order + energy + cons.** |
| NS          | Open (3D)                | 1 (enstrophy)          | Viscosity (insufficient 3D)    |
| RD          | Constitutive             | 3+                     | None universal                 |

### 4.2 The Four Structural Ingredients

The TFE combines four structural ingredients, each inherited from a different ancestor:

1. **Fourth-order smoothing** (from CH): k^4 damping at high wavenumbers. Stronger than second-order but loses the maximum principle.

2. **Degenerate mobility** (from PME): h^n vanishing at h = 0. Produces finite-speed propagation and free boundaries.

3. **Conservation** (from CH and PME): integral h = M. Couples height decay to support expansion.

4. **Gradient-flow structure** (from all four corners of the hierarchy): E[h] decreases monotonically. Rules out oscillations and chaos.

The combination of (1) and (2) is the TFE's distinctive structural feature: fourth-order smoothing *plus* degeneracy. This combination produces:
- Stronger smoothing than PME at high wavenumbers (k^4 > k^2).
- Finite-speed propagation like PME (degeneracy at h = 0).
- No maximum principle (fourth-order equations lack it, unlike PME's second-order comparison principle).
- The positivity question (can h become negative?) — a new structural issue absent in both CH (which has no h = 0 degeneracy) and PME (which has a comparison principle).

### 4.3 One Channel, One Conservation Law, One Free Boundary

Like the PME, the TFE has a "1-1-1 structure" — but at fourth order:

- **One dynamical channel:** Fourth-order degenerate diffusion D_4.
- **One conservation law:** Mass (integral h = M).
- **One geometric feature:** The contact line (free boundary Gamma(t)).

The dynamics are: spread, smooth, flatten, converge to a flat-film equilibrium. The drama is in the *geometry* of the contact line — how it moves, what shape it takes, how fast it advances — rather than in the *dynamics* of the bulk (which is simply monotone fourth-order smoothing).

### 4.4 The Positivity Question as the TFE's Structural Frontier

The positivity question is the TFE's most important unresolved structural issue — its analogue of the NS regularity problem. The question:

    Does h_0 >= 0 guarantee h(t) >= 0 for all t > 0?

is answered *yes* for n >= 1 and *unresolved or negative* for 0 < n < 1. This n-dependent answer makes the TFE the only architecture in the PDE Atlas whose envelope closure depends on the value of a constitutive parameter in a qualitatively significant way. (The RD envelope also depends on constitutive choices, but the dependence is on the *functional form* of the kinetics, not on a single scalar parameter.)

For the physically relevant case n = 3, the positivity answer is yes — the TFE envelope is fully closed, and the architecture is structurally sound. For the mathematically interesting case 0 < n < 1, the architecture has an open positivity face that requires additional physics (regularization) to close.

---

*End of Mode 1: Axiom → Envelope. Mode 2 (PDE → Extremal Dynamics) will follow in a subsequent file.*
