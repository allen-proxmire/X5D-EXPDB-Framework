# AD Evaluation: Thin-Film Equation — Architectural Specification

Allen Proxmire

April 2026

---

## 1. Implicit Axioms of the Thin-Film Architecture

The Thin-Film Equation (TFE) models the spreading of a thin viscous film on a solid substrate under the action of surface tension. It describes the evolution of the film height h(x, t) >= 0 through a fourth-order degenerate parabolic equation in conservation form. The TFE combines two structural features that appear separately in previously evaluated architectures: the *fourth-order smoothing* of Cahn–Hilliard and the *degenerate mobility* of the Porous Medium Equation. This combination produces an architecture that is simultaneously fourth-order (like CH), degenerate (like PME), conserved (like both), and equipped with a free boundary (like PME but not CH).

The TFE occupies a precise position in the architectural hierarchy: it is to Cahn–Hilliard what the Porous Medium Equation is to Allen–Cahn — the degenerate, free-boundary version of a conserved gradient-flow equation. Where CH has non-degenerate diffusion and diffuse interfaces, the TFE has degenerate diffusion and sharp interfaces. Where PME is second-order, the TFE is fourth-order. The TFE is the *fourth-order degenerate conserved* architecture — the intersection of CH-type and PME-type structural commitments.

### Axiom TFE-1: Continuum Hypothesis

The system is modeled by a scalar height field h(x, t) >= 0 defined at every point x in a domain Omega subset R^d (d = 1 or 2 for physically relevant films; d >= 1 in the mathematical theory) and every time t >= 0. The field h represents the local thickness of the film above the substrate. The continuum hypothesis suppresses the molecular structure of the liquid and treats the film as a smooth field — valid when the film thickness far exceeds the molecular scale (typically nanometers for simple liquids).

### Axiom TFE-2: Locality

All interactions are local: the time evolution of h at x depends only on h and its spatial derivatives at x, up to fourth order. There are no nonlocal operators, no integral constraints, and no elliptic enforcement mechanisms. The TFE is *fully local* at both formulation and solution levels — the same locality class as AC, CH, PME, and RD, and stronger than NS.

### Axiom TFE-3: Fourth-Order Degenerate Diffusion

The diffusion operator is a fourth-order operator with a degenerate mobility:

    partial_t h = -div(h^n nabla Delta h)

where:
- Delta h = nabla^2 h is the Laplacian of the height (related to the film's curvature and, through the Young–Laplace law, to the capillary pressure).
- nabla Delta h is the gradient of the capillary pressure — the driving force for the flow.
- h^n is the *mobility coefficient*, which degenerates at h = 0.
- The overall operator -div(h^n nabla Delta h) is a *fourth-order* degenerate parabolic operator in conservation form.

The fourth-order character arises from the physics: surface tension produces a capillary pressure proportional to -Delta h (the curvature of the free surface), and the flux is driven by the gradient of this pressure. The Navier–Stokes equations in the thin-film (lubrication) approximation reduce to this form, with the mobility h^n arising from integrating the velocity profile across the film thickness.

The degeneracy at h = 0 is the same structural feature as in PME: when the film thickness vanishes, the mobility vanishes, and the flux vanishes. This produces:
- Finite-speed propagation (the film edge advances at finite speed).
- Compact support (if the initial film has compact support, it remains compactly supported).
- Free-boundary formation (the contact line where h transitions from positive to zero is a free boundary).

The exponent n determines the specific mobility law:
- n = 1: linear mobility (Hele-Shaw cell, certain surface-tension-driven flows).
- n = 2: intermediate regime.
- n = 3: Navier–Stokes thin-film equation with no-slip boundary conditions (the physically most common case).
- n > 3: strong degeneracy (very slow spreading near the contact line).

### Axiom TFE-4: Conservation of Mass

The TFE is in conservation (divergence) form:

    partial_t h = -div(**J**),    **J** = h^n nabla Delta h

which implies, with no-flux boundary conditions:

    d/dt integral_Omega h(x, t) dx = 0

Total film volume (mass) is exactly conserved. The TFE can redistribute material but cannot create or destroy it. This is the same structural commitment as in CH and PME: conservation shapes the dynamics by forcing the film to spread (free boundary expands) rather than evaporate or condense.

### Axiom TFE-5: Euclidean Geometry

The equation is formulated on flat Euclidean R^d or bounded domains Omega subset R^d with the standard Laplacian. The substrate is flat. Curvature of the substrate, non-Euclidean geometry, and topographic effects are outside the standard TFE architecture (though they can be incorporated as extensions).

### Axiom TFE-6: Forward Parabolic Orientation

The TFE evolves forward in time. The fourth-order degenerate operator is *dissipative* (it decreases the surface energy) and well-posed in the forward direction. Backward evolution is ill-posed, as with all parabolic equations.

### Axiom TFE-7: No Reaction Term

The TFE is a *pure diffusion* equation — there is no reaction, no forcing, no external mass input. The dynamics are driven entirely by the fourth-order degenerate diffusion channel:

    partial_t h = -div(h^n nabla Delta h)    [no R, no f]

This is the same structural commitment as PME-7: the architecture isolates the effects of (fourth-order degenerate) diffusion by excluding all other dynamical channels. Extensions (evaporation, condensation, Marangoni effects, Van der Waals forces) add terms to the right-hand side but are outside the standard TFE.

### Axiom TFE-8: Constitutive Exponent n > 0

The mobility exponent n > 0 is a constitutive parameter selected by the specific physical system:

- n = 1: linear mobility. Hele-Shaw flow, certain idealized thin-film flows.
- n = 3: the Navier–Stokes thin-film equation (lubrication approximation with no-slip at the substrate).
- n → 0: approaches constant mobility (non-degenerate, CH-like behavior).
- n → infinity: extreme degeneracy (nearly frozen contact line).

The qualitative behavior depends on n:
- For n >= 1 (and especially n >= 3): the degeneracy is strong enough to produce *compactly supported* solutions with finite-speed propagation and a well-defined free boundary (contact line).
- For 0 < n < 1: the degeneracy is weak. Solutions may or may not have compact support depending on the dimension and the specific value of n.

The value n = 3 is the *physically canonical* case. The AD evaluation covers all n > 0 but focuses on the structurally rich regime n >= 1.

---

## 2. Canonical PDE in Architectural Form

### 2.1 The Thin-Film Equation

    partial_t h = -div(h^n nabla Delta h),    n > 0,    h >= 0          ... (TFE)

Equivalently, expanding the divergence:

    partial_t h = -nabla . (h^n nabla Delta h)
               = -h^n Delta^2 h - n h^{n-1} nabla h . nabla Delta h      ... (TFE-exp)

The expanded form reveals two sub-mechanisms within the single channel:
- -h^n Delta^2 h: the *biharmonic* term (fourth-order smoothing weighted by the mobility h^n).
- -n h^{n-1} nabla h . nabla Delta h: a *gradient-pressure coupling* term that modifies the smoothing near regions where h varies rapidly.

### 2.2 Flux Form and Pressure

The TFE can be written in flux form:

    partial_t h = -div(**J**),    **J** = h^n nabla p,    p = -Delta h

where p = -Delta h is the *capillary pressure* (proportional to the curvature of the free surface in the thin-film approximation). The flux is driven by pressure gradients, modulated by the mobility h^n. This is the *Darcy-type* structure: pressure gradient drives the flow, mobility depends on the state.

### 2.3 Channel-Labeled Decomposition

    partial_t h =    -div(h^n nabla Delta h)
                 |________________________________|
                   Fourth-order degenerate diffusion (D_4)

    subject to:   h >= 0,    integral h dx = const
                 |_______|   |___________________|
                  Positivity   Conservation (C)
                  constraint

    producing:    Contact line Gamma(t) = partial{h > 0}
                 |____________________________________________|
                   Geometric free boundary (G)

The TFE has the same structural simplicity as the PME: a single dynamical channel (fourth-order degenerate diffusion) with two constraints (positivity, conservation) and one emergent geometric feature (contact line / free boundary).

### 2.4 Gradient-Flow Structure

The TFE is a gradient flow of the *surface energy* (or Dirichlet energy of h):

    E[h] = (1/2) integral |nabla h|^2 dx

with respect to a *weighted H^{-1}* metric defined by the mobility h^n. The dissipation identity:

    dE/dt = -integral h^n |nabla Delta h|^2 dx <= 0

This is the TFE's Lyapunov identity: the surface energy decreases monotonically along every trajectory. The only stationary states have nabla Delta h = 0 wherever h > 0, which (combined with conservation) selects flat-film configurations h = const as the ultimate equilibria.

### 2.5 Self-Similar Solutions (Source-Type)

The TFE admits self-similar spreading solutions analogous to the Barenblatt profiles of the PME. For d = 1, the source-type solution with total mass M has the form:

    h(x, t) = t^{-alpha} H(x / t^{beta})

where:
- alpha = 1/(n + 4) is the decay exponent.
- beta = 1/(n + 4) is the spreading exponent.
- H(eta) is a compactly supported profile determined by an ODE.

The spreading rate is R(t) ~ t^{1/(n+4)} — fourth-order spreading (slower than the PME rate t^{1/(d(m-1)+2)} for comparable parameters because the fourth-order operator introduces a stronger scale dependence).

### 2.6 Boundary and Initial Conditions

**Initial condition:**

    h(x, 0) = h_0(x) >= 0,    h_0 in L^1(Omega)

**Boundary conditions (bounded domain):**
- No-flux: h^n nabla Delta h . n = 0 and nabla h . n = 0 on partial Omega.
- Periodic: on rectangular domains.

**Positivity constraint:** h >= 0 is the physical requirement that the film height is non-negative. Whether the PDE preserves positivity is a *structural question* that depends on the exponent n — see below.

---

## 3. Channel Identification

### Channel D_4: Fourth-Order Degenerate Diffusion

    D_4(h) = -div(h^n nabla Delta h)

- **Role:** The sole dynamical channel. Smooths the film surface by driving flow from regions of high capillary pressure (high curvature) to regions of low capillary pressure (low curvature). This is the fourth-order analogue of the PME's second-order nonlinear diffusion.
- **Locality:** Local. Involves h and its derivatives up to fourth order at each point.
- **Linearity:** Nonlinear. The mobility h^n makes the operator nonlinear in h. The fourth-order derivative structure (Delta^2) is linear, but the prefactor h^n introduces the nonlinearity.
- **Stability role:** Stabilizing. The surface energy E[h] = (1/2)||nabla h||^2 decreases monotonically:

      dE/dt = -integral h^n |nabla Delta h|^2 dx <= 0

  The dissipation is strict except at equilibrium (h = const or h = 0). The fourth-order smoothing damps modes at rate h^n k^4 — faster at high wavenumbers than the PME's h^{m-1} k^2.

- **Scale action:** Damping rate ~ h^n k^4 at density level h and wavenumber k. The fourth power k^4 provides *stronger* high-frequency damping than the PME's k^2. At the free boundary (h → 0), the damping rate degenerates to zero. The scale action is *doubly state-dependent*: it depends on both the local height h (through the mobility) and the wavenumber k (through the biharmonic).

### Channel C: Conservation

    C: d/dt integral h dx = 0

- **Role:** Mass-preserving structural constraint. Identical in character to PME's conservation channel and CH's conservation.
- **Locality:** Global constraint, locally enforced through divergence form.
- **Linearity:** Linear.
- **Stability role:** Constraining. Couples the decay of the maximum to the expansion of the support.

### Channel G: Geometric Free Boundary (Contact Line)

    G: Gamma(t) = partial{h(t) > 0}

- **Role:** The contact line where the film meets the dry substrate. The free boundary moves at a speed determined by the local height profile near the contact line. The contact-line dynamics are the TFE's most distinctive geometric feature — they encode the physics of wetting, dewetting, and spreading.
- **Locality:** Local (velocity determined by local height gradient at the contact line).
- **Linearity:** Nonlinear.
- **Stability role:** Neutral (geometric consequence, not an independent force).

**Contact-line subtlety:** For n >= 3 (the physically relevant Navier–Stokes case), the *contact-line velocity* involves a delicate balance: the fourth-order operator produces a *logarithmic correction* to the spreading rate near the contact line, and the classical no-slip boundary condition creates a *stress singularity* at the moving contact line. The TFE regularizes this singularity through the mobility degeneracy h^n, which suppresses the flux near h = 0. The exponent n = 3 is the *critical* case where the Navier–Stokes lubrication theory produces a logarithmic correction to Tanner's law for the contact angle.

### Channel M: Mobility Exponent n

    M: the constitutive exponent n > 0

- **Role:** Selects the strength of the degeneracy and the spreading dynamics. Larger n → stronger degeneracy → slower spreading → sharper contact angle.
- **Locality:** N/A (parameter).
- **Linearity:** N/A.
- **Stability role:** Parametric. All n > 0 produce qualitatively similar dynamics (spreading, surface-energy decay, free boundary), but the quantitative details (spreading rate, contact-line regularity, positivity preservation) depend on n.

### Channel Summary Table

| Channel | Symbol | Term / Feature              | Locality | Linearity  | Stability     | Scale Action                     |
|---------|--------|-----------------------------|----------|------------|---------------|----------------------------------|
| 4th-order diff. | D_4 | -div(h^n nabla Delta h) | Local    | Nonlinear  | Stabilizing   | Rate ~ h^n k^4                   |
| Conservation    | C   | integral h = const       | Global*  | Linear     | Constraining  | Couples all scales               |
| Free boundary   | G   | Contact line Gamma(t)    | Local    | Nonlinear  | Neutral       | Sets outer scale R(t) ~ t^{beta} |
| Exponent        | M   | n > 0                    | N/A      | N/A        | Parametric    | Sets alpha, beta                  |

*Enforced locally through divergence form.

---

## 4. Relation to AC, CH, PME, and RD

### 4.1 The Architectural Hierarchy

The TFE occupies a precise position in the hierarchy of gradient-flow PDEs evaluated in the PDE Atlas:

```
                    Non-conserved              Conserved
                    ────────────              ─────────
    Non-degenerate:   Allen–Cahn   ←→   Cahn–Hilliard
                       (2nd order)          (4th order)
                          ↓                     ↓
    Degenerate:      Porous Medium  ←→   Thin-Film Equation
                       (2nd order)          (4th order)
```

Each arrow represents a single structural step:
- Left → Right: *add conservation* (raises PDE order by 2, adds conserving Laplacian).
- Top → Bottom: *add degeneracy* (D → D(h), introduces free boundary and finite propagation).

The TFE is the *bottom-right corner*: the fourth-order degenerate conserved gradient-flow architecture. It inherits:
- Fourth-order character from CH (smoothing at rate k^4).
- Degeneracy from PME (mobility vanishes at h = 0, producing free boundaries).
- Conservation from both CH and PME (total mass preserved).
- Gradient-flow structure from all four corners (surface energy decreases monotonically).

### 4.2 TFE vs. Cahn–Hilliard

| Feature                    | Thin-Film Equation           | Cahn–Hilliard               |
|----------------------------|------------------------------|-----------------------------|
| PDE order                  | 4th                          | 4th                         |
| Diffusion type             | Degenerate (h^n)             | Non-degenerate              |
| Conservation               | Yes                          | Yes                         |
| Propagation speed          | Finite (for n >= 1)          | Infinite                    |
| Interface type             | Sharp (contact line)         | Diffuse (tanh profile)      |
| Phase separation           | No (single phase: liquid/dry)| Yes (two phases: +1/-1)     |
| Free energy                | E = (1/2)\|\|nabla h\|\|^2  | F = integral [f(phi) + (eps^2/2)\|\|nabla phi\|\|^2] |
| Reaction/double-well       | None                         | phi^3 - phi                 |
| Maximum principle          | Depends on n                 | No (4th order)              |
| Coarsening                 | Droplet coarsening           | Domain coarsening           |
| Gradient-flow metric       | Weighted H^{-1}              | H^{-1}                     |

The deepest structural difference: CH has a *double-well potential* (two preferred phases, phi = ±1) that drives phase separation, while TFE has *no potential landscape* — only the surface-energy gradient drives the dynamics. CH separates a mixture into phases; TFE spreads a film over a substrate.

### 4.3 TFE vs. PME

| Feature                    | Thin-Film Equation           | Porous Medium Equation      |
|----------------------------|------------------------------|-----------------------------|
| PDE order                  | 4th                          | 2nd                         |
| Diffusion type             | Degenerate (h^n)             | Degenerate (u^{m-1})       |
| Conservation               | Yes                          | Yes                         |
| Propagation speed          | Finite (n >= 1)              | Finite (m > 1)              |
| Free boundary              | Yes (contact line)           | Yes (support boundary)      |
| Free energy                | E = (1/2)\|\|nabla h\|\|^2  | Entropy functionals         |
| Smoothing order            | k^4                          | k^2                         |
| Self-similar exponent      | beta = 1/(n+4) [d=1]        | beta = 1/(d(m-1)+2)        |
| Maximum principle          | Depends on n                 | Yes (comparison principle)  |
| L^1 contraction            | Not in general               | Yes (unconditional)         |
| Attractor                  | Flat film (explicit)         | Barenblatt (explicit)       |

The TFE is the *fourth-order relative of the PME*. Both have degenerate diffusion, conservation, and free boundaries. The TFE's fourth-order character provides stronger smoothing (k^4 vs. k^2) but introduces complications: the maximum principle generally fails for fourth-order equations, the L^1 contraction is not guaranteed, and the positivity of solutions depends on the exponent n.

### 4.4 Positivity and the n-Dependence

A critical structural subtlety distinguishes the TFE from the PME: the *preservation of positivity* depends on the mobility exponent n.

- **n >= 1 (particularly n >= 3):** Solutions are expected to remain non-negative (h >= 0) for non-negative initial data. The degeneracy h^n is strong enough to prevent the fourth-order operator from driving h below zero. Rigorous proofs exist for n >= 1 in certain settings.
- **0 < n < 1:** The degeneracy may be too weak to prevent the fourth-order operator from producing negative values of h. Solutions can become *negative* — a physically meaningless state (negative film height). This is the *positivity crisis* of the TFE: the fourth-order operator, lacking a maximum principle, can overshoot h = 0 from above, producing unphysical negative heights.

The positivity question is the TFE's *single most delicate structural issue* — the analogue of the NS regularity problem, but for a different reason: not "does the solution remain smooth?" but "does the solution remain non-negative?" For n >= 1 (and especially n = 3, the physical case), the answer is expected to be yes, and partial results exist. For small n, the answer may be no without additional regularization (e.g., Van der Waals forces or slip conditions).

### 4.5 Positioning Table

| Feature                    | AC        | CH        | PME         | TFE               | RD          |
|----------------------------|-----------|-----------|-------------|--------------------|-------------|
| PDE order                  | 2nd       | 4th       | 2nd         | 4th                | 2nd         |
| Diffusion type             | Linear    | Non-degen.| Degenerate  | Degenerate         | Linear/nonlin.|
| Conservation               | No        | Yes       | Yes         | Yes                | Constitutive|
| Degeneracy                 | No        | No        | Yes (u^{m-1})| Yes (h^n)         | Constitutive|
| Free boundary              | No        | No        | Yes         | Yes (contact line) | Constitutive|
| Propagation speed          | Infinite  | Infinite  | Finite      | Finite (n>=1)      | Constitutive|
| Gradient flow              | Yes (L^2) | Yes (H^{-1})| Yes (Wass.)| Yes (weighted H^{-1})| Gen. no  |
| Reaction                   | phi-phi^3 | via mu    | None        | None               | R(u)        |
| Maximum principle          | Yes       | No        | Yes         | n-dependent        | Constitutive|
| Structural complexity      | Low       | Moderate  | Low         | Moderate           | Highest     |

---

*End of Architectural Specification. The Mode 1 (Axiom → Envelope) analysis will follow in the next file.*
