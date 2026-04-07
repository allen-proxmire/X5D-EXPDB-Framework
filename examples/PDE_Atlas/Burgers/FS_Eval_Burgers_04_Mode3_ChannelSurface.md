# AD Evaluation: Inviscid Burgers Equation — Mode 3: Channels → Constraint Surface

Allen Proxmire

April 2026

---

## Overview

Mode 3 constructs the constraint surface of the Burgers architecture. The Burgers constraint surface is structurally parallel to the HJ surface — both are hyperbolic, both have a required singularity face (gradient blowup / shock), and both are sealed by convexity + entropy/viscosity. But the Burgers surface has *additional structural richness* from the conservation-law form: L^1 contraction, Rankine–Hugoniot jump conditions, shock-concentrated dissipation, and total variation decay. These conservation-law tools make the Burgers constraint surface the *most completely characterized hyperbolic surface* in the PDE Atlas.

The Burgers surface also introduces a new dissipation geometry — *shock-concentrated dissipation* — in which energy is dissipated only on a codimension-1 set (the shock locations), not distributed throughout the domain. This is qualitatively different from every parabolic architecture (where dissipation is volumetric) and from HJ (which has no dissipation at all).

We continue with:

    partial_t v + partial_x(v^2/2) = 0,    v entropy solution (Kruzkov)

---

## 1. Channel Decomposition

### Channel T: Transport (Nonlinear Self-Advection)

    T(v) = v partial_x v = partial_x(v^2/2)

- **Locality:** Local. v partial_x v depends on v and partial_x v at each point. No nonlocal coupling, no integral operators, no pressure equation.
- **Linearity:** Nonlinear. The product v partial_x v is quadratic in v — the simplest nonlinear self-interaction. This is the *scalar reduction* of the NS advection term **u** . nabla **u**: one spatial dimension, one velocity component, no incompressibility, no pressure.
- **Stability role:** Destabilizing. Self-advection steepens velocity profiles: fast regions overtake slow regions, compressing the profile until a shock forms. The steepening rate is proportional to -v_x — the steeper the negative slope, the faster the compression. This is the conservation-law analogue of HJ's gradient steepening, but expressed directly in the velocity field rather than in the potential.
- **Scale action:** First-order in wavenumber k. The advection rate is proportional to v k — linear in k, unlike parabolic damping (proportional to k^2). The first-order scaling amplifies high-k modes (steepening) rather than damping them (smoothing). This is the structural signature of hyperbolicity: first-order transport amplifies; second-order diffusion damps.

### Channel S: Steepening (Shock Formation)

    S: partial_x v → -infinity at x = x_shock as t → T*

- **Locality:** Local in trigger (the shock forms at the point of maximum initial negative slope). Global in consequence (the shock propagates and interacts with the entire solution).
- **Linearity:** Nonlinear. Shock formation is the nonlinear consequence of the self-advection feedback loop: steeper slopes → faster compression → steeper slopes → discontinuity.
- **Stability role:** Initially destabilizing (gradient blowup), then *self-limiting*. Once the shock forms, it *reduces* the total variation of v: the shock absorbs characteristics from both sides, merging them irreversibly. The post-shock dynamics are *simpler* (fewer features, lower total variation) than the pre-shock dynamics. The steepening channel is destructive in the short term but simplifying in the long term.
- **Scale action:** Concentrates at the smallest scales. The shock is a delta function in v_x — a structure of zero width. The steepening process creates structure at scale zero, which is then maintained by the entropy condition (the shock does not smooth out, because there is no diffusion).

### Channel V: Entropy (Solution Selection + L^1 Contraction)

    V: v = entropy solution satisfying Kruzkov's inequalities

- **Locality:** Locally defined (entropy inequalities at each point for each convex entropy eta). Globally consequent (uniqueness + stability of the entire solution).
- **Linearity:** Nonlinear. The entropy framework involves nonlinear operations (convex entropies, comparison with sub/super-solutions).
- **Stability role:** Stabilizing (in the well-posedness sense). Channel V provides:
  - **Uniqueness:** The entropy solution is the unique admissible weak solution.
  - **L^1 contraction:** ||v_1(t) - v_2(t)||_{L^1} <= ||v_{1,0} - v_{2,0}||_{L^1}.
  - **L^{infinity} contraction:** ||v_1(t) - v_2(t)||_{L^inf} <= ||v_{1,0} - v_{2,0}||_{L^inf}.
  - **Shock admissibility:** Compressive shocks only (v_L > v_R at each shock).
  - **Total variation control:** TV(v(t)) <= TV(v_0).

  Channel V is the Burgers closure mechanism — the structural tool that seals the constraint surface. It is strictly richer than HJ's viscosity channel (which provides L^{infinity} contraction and comparison but not L^1 contraction, mass conservation, or Rankine–Hugoniot conditions).

- **Scale action:** Operates at the shock scale. The entropy condition selects the correct weak solution at each discontinuity. Away from shocks, the entropy solution is classical and Channel V is inactive.

### Channel Summary Table

| Channel | Symbol | Feature                        | Locality | Linearity   | Stability              | Scale Action           |
|---------|--------|--------------------------------|----------|-------------|------------------------|------------------------|
| Transport    | T | v v_x (self-advection)        | Local    | Nonlinear   | Destabilizing          | Rate ~ v k (1st-order) |
| Steepening   | S | v_x → -infinity at T*        | Local*   | Nonlinear   | Destab. → self-limiting| Concentrates at k → ∞  |
| Entropy      | V | Kruzkov selection + L^1 contr.| Local**  | Nonlinear   | Stabilizing            | At shock scale          |

*Local trigger, global consequence. **Locally defined, globally consequent.

### Channel Count Comparison

| Architecture | Dynamical | Emergent Singular | Selection/Closure | Total |
|-------------|-----------|-------------------|-------------------|-------|
| **Burgers** | **1 (T)** | **1 (S)**         | **1 (V)**         | **3** |
| HJ          | 1 (T)     | 1 (S)             | 1 (V)             | 3     |
| MCF         | 1 (K)     | 1 (T_topology)    | 0 (area diss.)    | 3     |
| PME         | 1 (D_nl)  | 0                 | 0 (entropy + L^1) | 3+1   |
| FP          | 2 (T, D)  | 0                 | 0 (linearity)     | 3+1   |

Burgers, HJ, and MCF all have *three channels* — tied for fewest in the Atlas. All three include an emergent singularity channel and a closure/selection channel. The structural parallel:

- Burgers: transport → shock → entropy selection.
- HJ: transport → gradient blowup → viscosity selection.
- MCF: curvature → curvature blowup → area dissipation (+ surgery).

Three architectures, three singularity types, three closure mechanisms — but the same *three-channel minimal structure*.

---

## 2. Dissipation Geometry

### 2.1 The Absence of Volumetric Dissipation

Like HJ, the Burgers architecture has *no volumetric dissipation* — no diffusion, no Lyapunov functional that decreases continuously through a distributed mechanism. The kinetic energy E(t) = integral v^2/2 dx is *conserved between shocks* and *decreases only at shocks*.

This is qualitatively different from every parabolic architecture:

| Architecture | Dissipation Type         | Where Dissipation Occurs         |
|-------------|--------------------------|----------------------------------|
| FP          | Volumetric (entropic)    | Everywhere (Fisher information)  |
| AC/CH       | Volumetric (Lyapunov)    | Everywhere (||mu||^2 or ||nabla mu||^2) |
| PME         | Volumetric (entropy)     | Everywhere in {u > 0}           |
| TFE         | Volumetric (energy)      | Everywhere in {h > 0}           |
| MCF         | Volumetric (geometric)   | Everywhere on Gamma (integral H^2 dS) |
| NS          | Volumetric (viscous)     | Everywhere (nu ||nabla u||^2)    |
| HJ          | **None**                 | **Nowhere** (no dissipation at all) |
| **Burgers** | **Shock-concentrated**   | **Only at shocks** (codimension-1) |

### 2.2 Shock-Concentrated Dissipation

The Burgers energy identity:

    d/dt integral v^2/2 dx = -sum_{shocks} (1/12)(v_L - v_R)^3 * (correction factor)

Energy is dissipated *only* at shock locations — a set of measure zero in space (discrete points in 1D). Between shocks, energy is exactly conserved. The dissipation is:

- **Localized:** Concentrated on a codimension-1 set (points in 1D, curves in 2D).
- **Irreversible:** The energy lost at a shock cannot be recovered (entropy production).
- **Cubic in shock strength:** The dissipation rate at a shock is proportional to (v_L - v_R)^3 — strong shocks dissipate much more than weak shocks.
- **Spontaneous:** No external mechanism drives the dissipation — it is an *intrinsic consequence* of the nonlinear transport + entropy selection.

This shock-concentrated dissipation is a *new dissipation mode* in the PDE Atlas, distinct from both volumetric dissipation (parabolic architectures) and zero dissipation (HJ). Burgers demonstrates that *dissipation can occur without diffusion* — it arises from the entropy selection at discontinuities, not from a smoothing mechanism.

### 2.3 The Role of Convex Flux

The convex flux f(v) = v^2/2 induces the entire closure structure:

1. **Convexity → comparison principle:** v_0 <= w_0 implies v(t) <= w(t). Foundation of uniqueness.
2. **Convexity → L^1 contraction (Kruzkov):** ||v - w||_{L^1} non-increasing. The strongest stability property for scalar conservation laws.
3. **Convexity → L^{infinity} contraction:** ||v - w||_{L^inf} non-increasing. Inherited from HJ.
4. **Convexity → Oleinik entropy condition:** v_x <= 1/t. Universal one-sided gradient bound.
5. **Convexity → Rankine–Hugoniot:** Shock speed s = (v_L + v_R)/2 = f'((v_L + v_R)/2). Exact jump condition.
6. **Convexity → Lax entropy condition:** v_L > s > v_R. Compressive shocks only.
7. **Convexity → total variation decay:** TV(v(t)) <= TV(v_0). Complexity decreases.

All seven properties flow from the *single structural assumption* of convex flux. This is the Burgers analogue of the role that convexity of H plays in HJ — but the conservation-law structure provides *more* structural consequences (L^1 contraction, Rankine–Hugoniot, energy dissipation) than the HJ structure alone.

### 2.4 Comparison of Closure Mechanisms

| Architecture | Closure Type        | Key Ingredient              | Dissipation Mode       |
|-------------|---------------------|-----------------------------|------------------------|
| FP          | Linear              | Linearity of PDE            | Volumetric (entropic)  |
| AC/CH       | Dissipative         | Lyapunov + smoothing        | Volumetric (energy)    |
| PME         | Dissipative         | Degeneracy + entropy + L^1  | Volumetric (entropy)   |
| MCF         | Dissip.-geometric   | Area dissipation            | Volumetric (geometric) |
| HJ          | Variational         | Convexity + viscosity       | **None**               |
| **Burgers** | **Entropic-contractive** | **Convex flux + Kruzkov** | **Shock-concentrated** |
| NS          | Open (3D)           | Viscosity (insufficient?)   | Volumetric (viscous)   |

Burgers introduces the *fourth closure mode* in the Atlas (after linear, dissipative, and variational): **entropic-contractive closure** — achieved through the convex flux + Kruzkov entropy framework, with dissipation concentrated at shocks rather than distributed volumetrically.

---

## 3. Constraint Surface Geometry

### 3.1 Three Regions of the Constraint Surface

**Region A: Smooth (Classical Characteristics, t < T*)**

The entropy solution coincides with the classical solution. Characteristics carry constant velocity values along straight lines. The solution is C^1 (as smooth as the initial data). All estimates are classical.

**Properties:**
- v in C^1, determined by the characteristic map x = x_0 + v_0(x_0) t.
- v_x(x, t) = v_0'(x_0) / (1 + t v_0'(x_0)) — gradient evolves toward blowup.
- Energy exactly conserved: d/dt integral v^2/2 dx = 0 (no shocks yet).
- Mass exactly conserved: d/dt integral v dx = 0.

**Region B: Pre-Shock (Steepening, t → T*)**

The gradient concentrates: v_x → -infinity at the point of steepest negative initial slope. The velocity v remains bounded (||v||_{L^inf} <= ||v_0||_{L^inf}). The solution is still classical but approaching the breakdown threshold.

**Properties:**
- v remains bounded and continuous.
- v_x → -infinity at one point (the future shock location).
- The characteristic map is about to become multi-valued.
- T* = -1/min(v_0') is the exact shock time.

**Region C: Post-Shock (Entropy Solution, t > T*)**

The classical solution has broken down. The entropy solution provides the unique continuation:

**Properties:**
- v is bounded and measurable (BV — bounded variation).
- v has finitely many discontinuities (shocks) at each time.
- Between shocks, v is smooth (classical solution applies locally).
- Shocks propagate at Rankine–Hugoniot speed s = (v_L + v_R)/2.
- Shocks can merge (when two shocks collide) but not split.
- Energy is dissipated at each shock.
- Total variation TV(v) is non-increasing.
- The solution is unique (Kruzkov).

### 3.2 Assembly into a Single Constraint Surface

The three regions form a single constraint surface with a *one-way gate*:

    Region A (smooth) → Region B (pre-shock) → Region C (post-shock, permanent)

The gate at t = T* is irreversible: once a shock forms, it persists forever (there is no diffusion to smooth it). Additional shocks can form at later times (as other characteristic families cross), and existing shocks can merge. The number of shocks is *non-increasing* in time (monotone simplification).

**Comparison with HJ:** The HJ constraint surface has the same three-region structure (smooth → pre-singular → post-singular), but the HJ singularity is a *kink* (continuous u with discontinuous nabla u), while the Burgers singularity is a *shock* (discontinuous v). The Burgers shock is "one derivative lower" than the HJ kink — a direct consequence of the v = partial_x u relationship.

### 3.3 The Required Shock Face

The shock face is *required, not anomalous*:

- **Required:** For generic initial data with decreasing regions, characteristics *must* cross → a shock *must* form. This is a theorem (not a conjecture, not an open question).
- **Resolved:** The Kruzkov entropy framework provides unique continuation past the shock. The architecture is globally well-posed.
- **Permanent:** Shocks persist forever (no diffusion to smooth them). The solution remains in Region C for all t > T*.
- **Simplifying:** Each shock reduces the total variation of v. The post-shock solution is *simpler* than the pre-shock solution.

**Comparison with other singular faces:**

| Architecture | Singular Face           | Required? | Resolved? | Permanent? | Simplifying? |
|-------------|-------------------------|-----------|-----------|------------|--------------|
| NS (3D)    | Vorticity blowup        | Open      | Open      | Open       | Open         |
| MCF         | Curvature blowup        | Yes       | Yes (surgery)| No (restart)| Yes       |
| HJ          | Gradient blowup (kink)  | Yes       | Yes (viscosity)| Yes     | Yes (semiconcavity) |
| **Burgers** | **Velocity shock**      | **Yes**   | **Yes (entropy)** | **Yes** | **Yes (TV decay)** |
| FP/PME/AC/CH| None                   | N/A       | N/A       | N/A        | N/A          |

Burgers and HJ share the same structural profile: required, resolved, permanent, simplifying. The difference is the *level* of the singularity (velocity discontinuity vs. gradient discontinuity) and the *closure tools* (L^1 contraction + Rankine–Hugoniot for Burgers vs. L^{infinity} contraction + Hopf–Lax for HJ).

---

## 4. Anomalies and Open Faces

### 4.1 Sealed Faces

**Oscillatory face: Sealed.** The L^1 contraction (||v_1 - v_2||_{L^1} non-increasing) and comparison principle (order-preserving) together forbid limit cycles, sustained oscillations, and recurrence. The entropy semigroup is monotone and contracting — the structural opposite of oscillatory dynamics.

**Chaotic face: Sealed.** The L^1 contraction implies Lipschitz stability in L^1: nearby initial data produce nearby solutions for all time. No sensitive dependence on initial conditions. The L^{infinity} contraction provides the same in the sup norm. Double contraction in two norms is *maximally anti-chaotic*.

**Amplitude-blowup face: Sealed.** The L^{infinity} norm of v is non-increasing: ||v(t)||_{L^inf} <= ||v_0||_{L^inf}. The velocity itself never blows up — only the gradient v_x blows up (at shocks). The singularity is purely in the *regularity* (loss of differentiability), not in the *amplitude* (v remains bounded).

**Nonlocal face: Sealed (absent).** All channels are local. No pressure equation, no Green's function, no integral operator.

**Pattern-formation face: Sealed (absent).** One species, no reaction, no diffusion. No mechanism for spatial self-organization.

### 4.2 The Shock Face: Required and Resolved

The shock-formation face is the single structural face of the Burgers constraint surface. It is sealed by the *entropy channel V*:

- L^1 contraction: provides uniqueness and stability past shocks.
- Rankine–Hugoniot: provides exact shock speed (no ambiguity in shock propagation).
- Lax entropy condition: selects compressive shocks (no expansive discontinuities).
- Total variation decay: ensures that the solution simplifies over time.

The shock face is *not an anomaly* — it is a structural feature sealed by the strongest closure tools in the hyperbolic PDE theory.

### 4.3 Anomaly Count

| Face               | Status              |
|--------------------|---------------------|
| Oscillatory        | Sealed (L^1 contraction) |
| Chaotic            | Sealed (double contraction) |
| Amplitude-blowup   | Sealed (L^{infinity} bound) |
| Nonlocal           | Absent              |
| Pattern-formation  | Absent              |
| **Shock formation**| **Required, resolved by entropy + L^1** |

**Anomaly count: zero.** The shock is structural, not anomalous. The constraint surface is fully sealed.

### 4.4 Burgers as the Entropy-Contracted Architecture

The Burgers constraint surface is the *only* surface in the Atlas sealed by entropy + L^1 contraction. This combination is *strictly stronger* than any other hyperbolic closure:

- HJ: sealed by convexity + viscosity (L^{infinity} contraction, comparison, Hopf–Lax). *No L^1 contraction.*
- MCF: sealed by area dissipation + monotonicity formula. *No contraction in any function norm.*
- NS: *not sealed* (3D regularity open).

The L^1 contraction is the structural addition that conservation-law form provides beyond the HJ viscosity framework. It is the *strongest stability property* available for first-order nonlinear PDEs — and it is unique to conservation laws with convex flux.

---

## 5. Channel Constraints

---

**C1. Convex Flux**

    f(v) = v^2/2,    f''(v) = 1 > 0

Strict convexity. The structural requirement for comparison, L^1 contraction, and entropy uniqueness.

*Scope: All standard Burgers.*

---

**C2. First-Order Conservation Law**

    partial_t v + partial_x(v^2/2) = 0    [conservation form]
    partial_t v + v partial_x v = 0        [advective form]

No second-order terms. No diffusion. No reaction. Purely first-order nonlinear transport in conservation form.

*Scope: All Burgers.*

---

**C3. Finite-Speed Propagation**

    Domain of dependence of (x, t) subset { y : |y - x| <= ||v_0||_{L^inf} t }

Hyperbolic cone. Characteristics at speed v. Maximum speed = ||v_0||_{L^inf}.

*Scope: All Burgers with bounded data.*

---

**C4. L^1 Contraction (Kruzkov)**

    ||v_1(t) - v_2(t)||_{L^1} <= ||v_{1,0} - v_{2,0}||_{L^1}    for all t >= 0

The strongest stability property for scalar conservation laws. Implies uniqueness and continuous dependence.

*Scope: All entropy solutions with convex flux.*

---

**C5. L^{infinity} Contraction**

    ||v_1(t) - v_2(t)||_{L^{infinity}} <= ||v_{1,0} - v_{2,0}||_{L^{infinity}}

Sup-norm stability. Combined with C4: double contraction in two norms — unique in the Atlas.

*Scope: All entropy solutions with convex flux.*

---

**C6. Oleinik One-Sided Gradient Bound**

    partial_x v(x, t) <= 1/t    for all x, t > 0

Universal: independent of initial data. The positive slope decays as 1/t. Shocks (negative slope) can be arbitrarily steep.

*Scope: Entropy solutions, t > 0.*

---

**C7. Shock Formation**

    For generic data with min(v_0') < 0: T* = -1/min(v_0') < infinity

Gradient blowup is certain. The velocity develops a discontinuity at T*.

*Scope: Generic data with decreasing regions.*

---

**C8. Entropy Admissibility**

    For every convex eta: partial_t eta(v) + partial_x q(v) <= 0    (distributional)
    where q'(v) = eta'(v) f'(v)

The entropy condition selects the unique physically admissible weak solution — the vanishing-viscosity limit.

*Scope: All entropy solutions.*

---

**C9. Rankine–Hugoniot Jump Condition**

    At each shock: s = (v_L + v_R) / 2 = [f(v_L) - f(v_R)] / (v_L - v_R)

Exact shock speed. Not an approximation. The shock propagates at the average of the left and right states.

*Scope: All shocks in entropy solutions.*

---

**C10. Total Variation Decay**

    TV(v(t)) <= TV(v_0)    for all t >= 0

The total variation (integral |v_x| dx, counting shock jumps) is non-increasing. Each shock reduces TV by absorbing characteristics. The solution monotonically simplifies.

*Scope: All entropy solutions with BV data.*

---

**C11. No Oscillations**

    L^1 contraction (C4) + comparison principle => monotone, contracting dynamics
    => no limit cycles, no recurrence, no periodic orbits

*Scope: All Burgers.*

---

**C12. Mass Conservation + Energy Dissipation at Shocks**

    d/dt integral v dx = 0    (mass conserved exactly)
    d/dt integral v^2/2 dx <= 0    (energy dissipated at shocks only)

Mass is an exact invariant. Energy is a piecewise-conserved, globally-decreasing quantity. The architecture is *mass-conservative* and *energy-dissipative* — the two accounting identities are structurally decoupled (mass is exact; energy has an irreversible loss at shocks).

*Scope: All entropy solutions.*

---

### Channel Constraint Summary

| Label | Constraint                        | Type              | Scope            |
|-------|-----------------------------------|-------------------|------------------|
| C1    | Convex flux                       | Structural req.   | All standard BA  |
| C2    | First-order conservation law      | PDE structure     | All BA           |
| C3    | Finite-speed propagation          | Hyperbolic        | All BA           |
| C4    | L^1 contraction                   | Contraction       | Convex flux      |
| C5    | L^{infinity} contraction          | Contraction       | Convex flux      |
| C6    | Oleinik bound                     | Universal         | t > 0            |
| C7    | Shock formation                   | Singularity       | Generic data     |
| C8    | Entropy admissibility             | Selection         | All BA           |
| C9    | Rankine–Hugoniot                  | Jump condition    | At shocks        |
| C10   | Total variation decay             | Monotonicity      | BV data          |
| C11   | No oscillations                   | Contraction       | All BA           |
| C12   | Mass conservation + energy dissip.| Conservation + dissipation | All BA  |

All twelve constraints are unconditional for convex flux and bounded (or BV) initial data.

---

## 6. Comparison with AC, CH, PME, TFE, RD, NS, FP, MCF, and HJ

### 6.1 Closure Mechanism Comparison

| Architecture | Closure Type             | Key Tool                    | Dissipation Mode       |
|-------------|---------------------------|-----------------------------|------------------------|
| FP          | Linear                   | Linearity                   | Volumetric (entropic)  |
| AC/CH       | Dissipative              | Lyapunov + smoothing        | Volumetric (energy)    |
| PME         | Dissipative              | Degeneracy + entropy + L^1  | Volumetric (entropy)   |
| TFE         | Dissipative              | 4th-order + degeneracy      | Volumetric (energy)    |
| MCF         | Dissipative-geometric    | Area + Huisken monotonicity | Volumetric (geometric) |
| HJ          | Variational              | Convexity + viscosity       | **None**               |
| **Burgers** | **Entropic-contractive** | **Convex flux + Kruzkov L^1** | **Shock-concentrated** |
| NS          | Open (3D)                | Viscosity (insufficient?)   | Volumetric (viscous)   |
| RD          | Constitutive             | Constitutive-dependent      | Constitutive           |

### 6.2 Burgers vs. HJ: The Conservation-Law Addition

| Feature                    | Burgers                       | HJ                          |
|----------------------------|-------------------------------|-----------------------------|
| Singularity type           | Velocity discontinuity (shock)| Gradient discontinuity (kink)|
| Conservation law           | **Yes** (integral v = const)  | No                          |
| L^1 contraction            | **Yes** (Kruzkov)             | No                          |
| L^{infinity} contraction   | Yes                           | Yes                         |
| Shock speed formula        | **s = (v_L+v_R)/2 (R-H)**    | N/A                         |
| Energy dissipation         | **At shocks (irreversible)**  | None                        |
| Total variation decay      | **TV non-increasing**         | N/A                         |
| Mass conservation          | **Yes**                       | No                          |
| Closure mechanism          | Entropy + L^1 contraction     | Convexity + viscosity       |

Burgers adds *five structural features* over HJ (L^1 contraction, conservation, Rankine–Hugoniot, energy dissipation, TV decay) — all arising from the conservation-law form. The two architectures are one derivative apart (v = partial_x u) and share the same singularity time, the same comparison principle, and the same Oleinik bound.

### 6.3 Burgers as the Scalar Core of NS

The structural chain:

    Burgers → Euler → NS

- Burgers → Euler: add vector character + incompressibility + pressure.
- Euler → NS: add viscosity.

Burgers resolves the nonlinear self-advection completely (entropy solutions, L^1 contraction, exact shock conditions). NS cannot resolve it in 3D. The difference is the *structural additions* (vector + incompressibility + pressure) that Euler/NS impose on top of the Burgers self-advection. The open NS regularity problem lies *in these additions*, not in the self-advection itself.

### 6.4 The Dissipation Spectrum

The Atlas architectures span a *dissipation spectrum*:

    HJ (zero dissipation) → Burgers (shock-concentrated) → MCF (geometric-volumetric) → PME/TFE (nonlinear-volumetric) → AC/CH (linear-volumetric) → FP (linear-entropic)

Burgers sits *between* HJ (zero dissipation) and the parabolic architectures (volumetric dissipation). It demonstrates a *middle mode*: dissipation exists but is concentrated on a lower-dimensional set (shocks), not distributed through the volume. This shock-concentrated dissipation is the conservation-law contribution to the dissipation landscape — a mode that does not exist in any non-conservation-law architecture.

### 6.5 Summary Table

| Feature                    | Burgers      | HJ    | FP    | PME   | AC    | NS    | MCF   | RD    |
|----------------------------|-------------|-------|-------|-------|-------|-------|-------|-------|
| Conservation law           | **Yes**     | No    | Yes   | Yes   | No    | Yes   | No    | Const.|
| L^1 contraction            | **Yes**     | No    | No    | **Yes**| No   | No    | No    | No    |
| L^{inf} contraction        | **Yes**     | **Yes**| No   | No    | No    | No    | No    | No    |
| Shock-concentrated dissip. | **Yes**     | No    | No    | No    | No    | Open  | No    | No    |
| Rankine–Hugoniot           | **Yes**     | No    | N/A   | N/A   | N/A   | N/A   | N/A   | N/A   |
| Total variation decay      | **Yes**     | No    | No    | No    | No    | No    | No    | No    |
| Mass conservation          | **Yes**     | No    | Yes   | Yes   | No    | Yes   | No    | Const.|
| Parameters                 | **0**       | **0** | 2     | 1     | 3     | 2     | **0** | Many  |
| Anomalies                  | 0           | 0     | 0     | 0     | 0     | 2     | 0     | 0-3+  |

Burgers is the *unique* architecture with: conservation-law structure + double contraction (L^1 + L^{infinity}) + shock-concentrated dissipation + Rankine–Hugoniot + total variation decay. It is the *richest hyperbolic constraint surface* in the Atlas — HJ's closure plus the full conservation-law toolkit.

---

*End of Mode 3: Channels → Constraint Surface. The AD Criteria and Verdict will follow in the final file.*
