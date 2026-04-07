# AD Evaluation: Hamilton–Jacobi Equation — Mode 3: Channels → Constraint Surface

Allen Proxmire

April 2026

---

## Overview

Mode 3 constructs the constraint surface of the HJ architecture. The HJ constraint surface introduces a *new structural category* in the PDE Atlas: a surface sealed not by smoothing (as in every parabolic architecture) but by *convexity and viscosity* — two structural features that have no counterpart in any diffusion-based closure. The result is an architecture that is fully closed (existence, uniqueness, stability of global solutions) despite having *certain gradient singularities* and *no dissipation mechanism*. The HJ closure is the *minimalist closure* — the fewest structural resources that can produce a complete well-posedness theory for a nonlinear PDE with singularities.

We continue with:

    partial_t u + H(nabla u) = 0,    H convex,    u viscosity solution

---

## 1. Channel Decomposition

### Channel T: Transport (First-Order Nonlinear)

    T(u) = H(nabla u)

- **Locality:** Local. H(nabla u) depends on nabla u at each point — no nonlocal coupling, no integral operators, no bulk-field interaction.
- **Linearity:** Nonlinear. H is a nonlinear function of p = nabla u. For H(p) = |p|^2/2, the nonlinearity is quadratic in nabla u. This is a *first-order* nonlinearity (acting on first spatial derivatives), unlike AC/CH (zeroth-order reaction nonlinearity) or NS (first-order self-advection nonlinearity on a vector field).
- **Stability role:** Destabilizing. The nonlinear transport steepens gradients: regions of high |nabla u| propagate faster than regions of low |nabla u|, causing the gradient profile to fold over and develop discontinuities. This is the *anti-diffusion* mechanism — the structural opposite of the Laplacian smoothing in parabolic architectures.
- **Scale action:** First-order in wavenumber k. The transport rate grows linearly with k (compared to k^2 damping in second-order diffusion and k^4 damping in fourth-order diffusion). The first-order growth is sufficient to produce finite-time gradient blowup but insufficient to blow up the function u itself (which remains Lipschitz). The scale action is: *amplify gradients, preserve amplitudes*.

### Channel S: Steepening (Gradient Blowup)

    S: ||D^2 u(t)||_{L^{infinity}} → infinity    as t → T*

- **Locality:** Local in origin (the steepening occurs where characteristics converge — a local geometric event). Global in consequence (the gradient discontinuity at the shock affects the global solution structure).
- **Linearity:** Nonlinear (emerges from the nonlinear feedback in Channel T).
- **Stability role:** Destabilizing (produces loss of regularity). Channel S is the *emergent consequence* of Channel T — not a separate PDE term but the inevitable dynamical outcome of nonlinear first-order transport without smoothing.
- **Scale action:** Concentrates at the smallest scales. The gradient profile sharpens: the characteristic width of the steepening region decreases as (T* - t)^{1/2}, reaching zero at the shock time. The steepening is a *scale-zero singularity* — it creates a structure of zero width (a gradient discontinuity).

### Channel V: Viscosity (Solution Selection)

    V: u = viscosity solution of partial_t u + H(nabla u) = 0

- **Locality:** The viscosity-solution concept is *locally defined* (comparison with test functions at each point) but *globally consequent* (the selection principle determines the unique global solution).
- **Linearity:** Nonlinear. The viscosity-solution concept involves sup/inf operations (subsolutions and supersolutions), not linear operations. The comparison principle is a *nonlinear* structural tool.
- **Stability role:** Stabilizing (in the sense of well-posedness). Channel V selects the unique entropy-admissible weak solution, providing existence, uniqueness, and stability past the gradient blowup. It is the HJ's *closure mechanism* — the structural tool that seals the constraint surface.
- **Scale action:** Operates at the shock scale. The viscosity selection resolves the multi-valuedness at gradient discontinuities — it chooses the correct branch at each shock point. Away from shocks, the viscosity solution coincides with the classical solution (Channel V is inactive in smooth regions).

### Channel Summary Table

| Channel | Symbol | Feature                       | Locality    | Linearity   | Stability         | Scale Action           |
|---------|--------|-------------------------------|-------------|-------------|-------------------|------------------------|
| Transport    | T | H(nabla u) = 0               | Local       | Nonlinear   | Destabilizing     | Rate ~ k (1st-order)  |
| Steepening   | S | D^2 u → infinity at T*       | Local*      | Nonlinear   | Destabilizing     | Concentrates at k → ∞ |
| Viscosity    | V | Viscosity-solution selection  | Local**     | Nonlinear   | Stabilizing       | Operates at shocks     |

*Local trigger, global consequence. **Locally defined, globally consequent.

### Channel Count and Structural Comparison

| Architecture | Dynamical | Emergent Singular | Selection/Closure | Total |
|-------------|-----------|-------------------|-------------------|-------|
| **HJ**      | **1 (T)** | **1 (S)**         | **1 (V)**         | **3** |
| MCF         | 1 (K)     | 1 (T_topology)    | 0 (area dissipation)| 3   |
| PME         | 1 (D_nl)  | 0                 | 0 (entropy + L^1) | 3+1  |
| FP          | 2 (T, D)  | 0                 | 0 (linearity)     | 3+1  |
| AC          | 2 (R, S)  | 0                 | 0 (max. pr. + Lyap.)| 2+2 |

HJ and MCF both have *three channels* and both include an *emergent singularity channel*. But the singularity mechanisms are structurally different:
- MCF: curvature blowup (second-order, geometric, completes the area-minimization program).
- HJ: gradient blowup (first-order, kinematic, resolves characteristic crossing).

And the closure mechanisms are different:
- MCF: area dissipation (Lyapunov functional, parabolic smoothing).
- HJ: viscosity selection (comparison principle, convex duality). No dissipation at all.

---

## 2. Dissipation Geometry

### 2.1 The Absence of Classical Dissipation

The HJ architecture has *no classical dissipation mechanism*:

- **No Lyapunov functional:** There is no functional Phi[u] with dPhi/dt <= 0. The HJ equation does not dissipate any "energy" — it transports and steepens without losing or gaining any integral quantity.
- **No entropy production:** Unlike conservation laws (which produce entropy at shocks), the HJ equation in its potential form does not have a natural entropy functional.
- **No gradient decay:** The gradient |nabla u| is non-increasing in L^{infinity} (U3 from Mode 1) but *not* in L^2 or any other integrated norm (the gradient can concentrate at shocks, maintaining or increasing the L^2 norm).

**This is unique in the Atlas.** Every other architecture has at least one dissipation mechanism:

| Architecture | Dissipation Mechanism              | Functional                        |
|-------------|-------------------------------------|-----------------------------------|
| AC          | Energy dissipation: dF/dt = -M\|\|mu\|\|^2 | Ginzburg–Landau F         |
| CH          | Energy dissipation: dF/dt = -M\|\|nabla mu\|\|^2 | Ginzburg–Landau F  |
| PME         | Entropy dissipation: dH/dt <= 0    | All convex entropies              |
| TFE         | Energy dissipation: dE/dt <= 0     | Surface energy E                  |
| FP          | Entropy dissipation: dH/dt = -I   | Relative entropy H                |
| MCF         | Area dissipation: dA/dt = -integral H^2 | Area A                     |
| NS          | Energy dissipation: dE/dt = -epsilon + P_f | Kinetic energy E         |
| **HJ**      | **None**                           | **None**                          |

### 2.2 Variational Closure Instead of Dissipative Closure

The HJ architecture compensates for the absence of dissipation through a *variational closure*: the Hopf–Lax formula provides a *global variational representation* of the solution that serves the same structural role as the Lyapunov functional in parabolic architectures.

**The Hopf–Lax formula as a "variational Lyapunov":**

    u(x, t) = inf_y { u_0(y) + |x - y|^2 / (2t) }

This formula:
- **Determines the solution uniquely** (like a Lyapunov functional determines the equilibrium).
- **Is monotone in a structural sense:** the infimum operation selects the *minimum-cost* branch, enforcing a variational form of "descent."
- **Is stable under perturbation:** small changes in u_0 produce small changes in u(t) (L^{infinity} contraction).
- **Forgets initial complexity:** as t → infinity, the solution converges to a paraboloid determined by min(u_0) alone.

The Hopf–Lax formula is *not* a Lyapunov functional (it is not a scalar that decreases in time), but it serves the *same structural purpose*: it provides existence, uniqueness, and stability. The closure is *variational* (cost minimization) rather than *dissipative* (energy decrease).

### 2.3 The Role of Convexity

The convexity of H(p) is the structural feature that enables the variational closure:

1. **Convexity → Comparison principle:** If u_0 <= v_0, then the viscosity solutions satisfy u(t) <= v(t). This is the *foundation of uniqueness*. It follows from the convexity of H through the doubling-variables technique of Crandall–Lions.

2. **Convexity → L^{infinity} contraction:** ||u(t) - v(t)||_{L^inf} <= ||u_0 - v_0||_{L^inf}. The solution map is a contraction — nearby initial data produce nearby solutions. This follows from the comparison principle.

3. **Convexity → Semiconcavity:** D^2 u <= C/t. The solution acquires one-sided second-order regularity for t > 0. This follows from the convexity of H through the structure of the Hopf–Lax formula (the infimum of a family of paraboloids is semiconcave).

4. **Convexity → Hopf–Lax representation:** The explicit variational formula u = inf{u_0 + cost} holds specifically for convex H (through the Legendre transform L = H^*).

Convexity plays the role in HJ that *positive definiteness of the diffusion operator* plays in parabolic architectures: it is the *structural assumption* that makes the closure mechanism work. Parabolic closure requires D > 0; HJ closure requires H convex.

### 2.4 Comparison of Closure Mechanisms

| Architecture | Closure Type        | Structural Ingredient    | Mechanism                    |
|-------------|---------------------|--------------------------|------------------------------|
| FP          | Linear              | Linearity of PDE         | Linear parabolic theory      |
| AC          | Dissipative         | Max. principle + Lyapunov| Energy decrease + L^inf bound|
| CH          | Dissipative         | 4th-order smooth + Lyapunov | H^2 control + Sobolev    |
| PME         | Dissipative         | Degeneracy + entropy + L^1 | Four-mechanism cooperation |
| TFE         | Dissipative         | 4th-order + degeneracy + cons.| Four-mechanism cooperation|
| MCF         | Dissipative-geometric| Area dissipation + convexity | Huisken monotonicity     |
| NS          | **Open** (3D)       | Viscosity (insufficient?) | Enstrophy gap (unresolved)  |
| **HJ**      | **Variational**     | **Convexity of H + viscosity**| **Comparison + Hopf–Lax** |

HJ is the *only* architecture whose closure is variational rather than dissipative. It demonstrates that *dissipation is not necessary for closure* — convex duality and viscosity-solution selection can do the same job.

---

## 3. Constraint Surface Geometry

### 3.1 Three Regions of the Constraint Surface

**Region A: Smooth (Classical Characteristics, t < T*)**

The solution is classical (C^{infinity} if u_0 is smooth). Characteristics do not cross. The constraint surface is *non-degenerate*: the classical PDE theory applies, and all estimates are unconditional. The dynamics are *reversible in principle* (the characteristic ODE is time-reversible) — no information is lost.

**Properties:**
- u in C^{infinity}(R^d x (0, T*)).
- nabla u evolves along characteristics: nabla u(x(t), t) = nabla u_0(x_0) (constant along each characteristic).
- The solution is uniquely determined by characteristic tracing.
- No selection principle needed — the classical solution is the viscosity solution.

**Region B: Pre-Shock (Characteristics Converging, t → T*)**

Characteristics converge but have not yet crossed. The gradient D^2 u grows without bound:

    ||D^2 u(t)||_{L^{infinity}} ~ C / (T* - t)

The solution remains classical but is approaching the regularity threshold. The constraint surface *narrows* as the second-derivative norm approaches infinity.

**Properties:**
- u remains C^1 (nabla u continuous but rapidly steepening).
- D^2 u → infinity at the convergence point (the future shock location).
- The classical and viscosity solutions still coincide.
- The Lipschitz constant ||nabla u||_{L^{infinity}} is non-increasing (E2).

**Region C: Post-Shock (Viscosity Solution, t > T*)**

The classical solution has broken down (nabla u has jump discontinuities at shocks). The viscosity solution provides the unique continuation:

    u(x, t) = inf_y { u_0(y) + |x - y|^2 / (2t) }

**Properties:**
- u is Lipschitz continuous (not C^1 at shocks).
- u is semiconcave (D^2 u <= C/t in the distributional sense).
- nabla u has jump discontinuities across the *shock set* Sigma_t (a lower-dimensional set).
- Away from Sigma_t, the classical solution applies.
- The solution is unique (comparison principle + viscosity framework).

### 3.2 Assembly into a Single Constraint Surface

The three regions form a *single constraint surface* with the following structure:

    Region A (smooth) → Region B (pre-shock) → Region C (post-shock)

The flow is one-directional: the dynamics move from A through B to C, never backward. Once a shock forms, it persists — shocks do not heal (because there is no diffusion to smooth them). The constraint surface has a *one-way gate* at t = T*: solutions pass through the gate (from smooth to non-smooth) and cannot return.

**Comparison with MCF:** MCF also has a one-way gate (from smooth to singular at curvature blowup). But the mechanisms and continuations differ:
- MCF: curvature blowup → surgery/level-set → smooth restart. The surface *passes through* the singularity and re-enters the smooth regime.
- HJ: gradient blowup → viscosity solution → permanent non-smoothness. The solution *crosses the gate* and stays in Region C forever. Shocks accumulate over time — the solution never returns to Region A.

### 3.3 The Required Regularity-Loss Face

The constraint surface includes a *required regularity-loss face*: the transition from C^1 to Lipschitz at the shock time T*. This face is:

- **Required:** For generic initial data, gradient blowup *must* occur (characteristics cross).
- **Structural:** The regularity loss is a consequence of the axioms (first-order nonlinear transport without diffusion), not a failure of the architecture.
- **Resolved:** The viscosity-solution framework provides unique continuation past the regularity loss. The architecture is well-posed globally — it just operates at lower regularity after the shock.
- **Permanent:** Unlike MCF (where the singularity is a discrete event followed by smooth restart), HJ's regularity loss is *permanent* — once the gradient becomes discontinuous, it stays discontinuous.

**Comparison with other singular faces:**

| Architecture | Singular Face            | Required? | Resolved? | Permanent?        |
|-------------|--------------------------|-----------|-----------|-------------------|
| NS (3D)    | Enstrophy blowup         | Open      | Open      | Open              |
| MCF         | Curvature blowup         | Yes       | Yes (surgery)| No (smooth restart) |
| **HJ**      | **Gradient blowup**     | **Yes**   | **Yes (viscosity)**| **Yes (permanent)** |
| TFE (n<1)  | Positivity failure       | Parametric| Open      | Open              |
| RD          | Blowup (super-linear)    | Constitutive| Constitutive | Constitutive  |

HJ is the only architecture with a *required, resolved, permanent* singular face. The gradient blowup definitely occurs, the viscosity framework definitely continues past it, and the solution definitely remains non-smooth forever after.

---

## 4. Anomalies and Open Faces

### 4.1 Sealed Faces

**Oscillatory face: Sealed.** The comparison principle (U1) provides order-preservation: u_0 <= v_0 implies u(t) <= v(t). Order-preserving dynamics cannot oscillate. The L^{infinity} contraction (U2) provides distance control: ||u(t) - v(t)||_{L^inf} <= ||u_0 - v_0||_{L^inf}. Non-expanding dynamics cannot exhibit limit cycles.

**Chaotic face: Sealed.** The L^{infinity} contraction implies Lipschitz stability: nearby initial data produce nearby solutions for all time. No sensitive dependence on initial conditions. The HJ semigroup S_t is a *non-expansive monotone map* — the structural opposite of a chaotic dynamical system.

**Amplitude-blowup face: Sealed.** The function u remains Lipschitz continuous for all time (the Lipschitz constant is non-increasing). Neither u nor nabla u blows up in L^{infinity}. The singularity is *purely in the regularity* (D^2 u blows up) — not in the amplitude. This is the weakest type of singularity: the solution remains bounded and continuous; only its second derivatives become infinite.

**Nonlocal face: Sealed (absent).** All channels are local. No Poisson equation, no Green's function, no integral operator. The HJ architecture is fully local at the formulation level.

**Pattern-formation face: Sealed (absent).** One species, no reaction, no diffusion. No mechanism for spatial pattern self-organization.

### 4.2 The Gradient-Blowup Face: Required and Resolved

The gradient-blowup face (transition from C^1 to Lipschitz) is the single structural face of the HJ constraint surface. It is:

- **Required:** Characteristics cross for generic data → gradient must become discontinuous.
- **Resolved:** Viscosity solutions provide the unique continuation.
- **Not anomalous:** The blowup is a structural consequence of the axioms (first-order + nonlinear + no diffusion), not a defect. Every PDE with these three properties *must* develop gradient shocks — it is a theorem, not a conjecture.

The gradient-blowup face is sealed by the *viscosity channel V*: the comparison principle, L^{infinity} contraction, and Hopf–Lax formula together provide complete control of the post-shock solution. The face is "open" in the regularity sense (the solution loses smoothness) but "closed" in the well-posedness sense (the solution exists, is unique, and is stable).

### 4.3 Anomaly Count

| Face               | Status              |
|--------------------|---------------------|
| Oscillatory        | Sealed (comparison principle) |
| Chaotic            | Sealed (L^{infinity} contraction) |
| Amplitude-blowup   | Sealed (Lipschitz propagation) |
| Nonlocal           | Absent              |
| Pattern-formation  | Absent              |
| **Gradient blowup**| **Required, resolved by viscosity** |

**Anomaly count: zero** (in the standard FS sense). The gradient blowup is not an anomaly — it is a required structural feature resolved by the viscosity framework. The constraint surface is *closed* with respect to all anomalous faces and *includes* the gradient-blowup face as a resolved structural transition.

---

## 5. Channel Constraints

---

**C1. Convex Hamiltonian**

    H : R^d → R is convex, with H(p)/|p| → infinity as |p| → infinity

Convexity is the structural requirement for the comparison principle, the Hopf–Lax formula, and the uniqueness of viscosity solutions. It is the *single axiom* on which the entire closure rests.

*Scope: All standard HJ.*

---

**C2. First-Order Transport Law**

    partial_t u + H(nabla u) = 0    [no Delta u, no higher-order terms]

The PDE is purely first-order in space. No diffusion, no dispersion, no reaction.

*Scope: All HJ.*

---

**C3. Finite-Speed Propagation**

    Domain of dependence of (x, t) subset { y : |y - x| <= C t }

Information propagates at speed at most C = ||nabla u_0||_{L^{infinity}} |H''|_{max}. Hyperbolic cone of dependence.

*Scope: All HJ with bounded initial gradient.*

---

**C4. Comparison Principle**

    u_0 <= v_0 (a.e.)  =>  u(t) <= v(t) (a.e.)    for all t >= 0

Order-preservation for viscosity sub- and super-solutions. The foundation of uniqueness.

*Scope: All HJ with convex H.*

---

**C5. L^{infinity} Contraction**

    ||u(t) - v(t)||_{L^{infinity}} <= ||u_0 - v_0||_{L^{infinity}}

The viscosity-solution semigroup is non-expansive in L^{infinity}. Stability and continuous dependence.

*Scope: All HJ with convex H.*

---

**C6. Semiconcavity**

    D^2 u(x, t) <= (C / t) I    for t > 0    (distributional)

One-sided second-order control. The maximum regularity the HJ can provide. Follows from the Hopf–Lax structure and the convexity of H.

*Scope: All HJ with convex H, t > 0.*

---

**C7. Shock Formation (Gradient Blowup)**

    For generic Lipschitz u_0: there exists T* < infinity such that ||D^2 u(t)||_{L^inf} → infinity as t → T*

Gradient blowup is certain for generic data. The shock-formation time T* is determined by the initial concavity.

*Scope: Generic Lipschitz initial data with non-trivial concavity.*

---

**C8. Viscosity-Solution Admissibility**

    u = lim_{epsilon → 0} u^epsilon    where partial_t u^epsilon + H(nabla u^epsilon) = epsilon Delta u^epsilon

The viscosity solution is the unique vanishing-viscosity limit. This selects the entropy-admissible weak solution.

*Scope: All HJ with convex H.*

---

**C9. Stability Under Sup-Convolution**

    u^delta(x) = sup_y { u(y) - |x - y|^2 / (2 delta) } → u uniformly as delta → 0

The viscosity solution is stable under regularization. Sup-convolution provides C^{1,1} approximations.

*Scope: All HJ viscosity solutions.*

---

**C10. No Oscillations**

    Comparison principle (C4) + L^{infinity} contraction (C5) => monotone, non-expansive dynamics
    => no limit cycles, no recurrence, no periodic orbits

*Scope: All HJ.*

---

**C11. No Chaos**

    L^{infinity} contraction => Lipschitz stability => no sensitive dependence on initial conditions

*Scope: All HJ.*

---

**C12. Hopf–Lax Variational Representation**

    u(x, t) = inf_y { u_0(y) + t L((x - y) / t) }    where L = H^* (Legendre transform)

Explicit variational formula for the viscosity solution. Connects HJ to optimal transport and calculus of variations.

*Scope: HJ with convex H on R^d.*

---

### Channel Constraint Summary

| Label | Constraint                        | Type              | Scope            |
|-------|-----------------------------------|-------------------|------------------|
| C1    | Convex Hamiltonian                | Structural req.   | All standard HJ  |
| C2    | First-order transport             | PDE structure     | All HJ           |
| C3    | Finite-speed propagation          | Hyperbolic        | All HJ           |
| C4    | Comparison principle              | Order             | Convex H         |
| C5    | L^{infinity} contraction          | Stability         | Convex H         |
| C6    | Semiconcavity                     | One-sided reg.    | Convex H, t > 0  |
| C7    | Shock formation                   | Singularity       | Generic data     |
| C8    | Viscosity admissibility           | Selection         | All HJ           |
| C9    | Sup-convolution stability         | Robustness        | All viscosity sol.|
| C10   | No oscillations                   | Monotonicity      | All HJ           |
| C11   | No chaos                          | Contraction       | All HJ           |
| C12   | Hopf–Lax formula                 | Variational       | Convex H on R^d  |

**All twelve constraints are unconditional** for convex H and Lipschitz initial data. No dimensional restriction, no conditional hypothesis, no parameter conditions beyond the structural requirement of convexity.

---

## 6. Comparison with AC, CH, PME, TFE, RD, NS, FP, and MCF

### 6.1 Closure Mechanism Comparison

| Architecture | Closure Type        | Key Ingredient              | Singularity?    | Result            |
|-------------|---------------------|-----------------------------|-----------------|-------------------|
| FP          | Linear              | Linearity                   | None            | Complete (global C^{infinity}) |
| AC          | Dissipative         | Max. principle + Lyapunov   | None            | Complete (global C^{infinity}) |
| CH          | Dissipative         | 4th-order + Lyapunov        | None            | Complete (global C^{infinity}) |
| PME         | Dissipative         | Degeneracy + entropy + L^1  | None            | Complete (Holder at boundary)  |
| TFE (n>=1)  | Dissipative        | 4th-order + degeneracy      | None            | Complete (Holder at contact)   |
| MCF         | Dissip.-geometric   | Area + Huisken monotonicity | Curvature blowup| Requires extension (surgery)   |
| **HJ**      | **Variational**     | **Convexity + viscosity**   | **Gradient blowup** | **Complete (Lipschitz + semiconcave)** |
| NS (3D)    | Open                | Viscosity (insufficient?)   | Open            | Incomplete                      |
| RD          | Constitutive        | Constitutive-dependent      | Constitutive    | Class-dependent                 |

### 6.2 The Smoothing–Steepening Spectrum at Mode 3

Organizing the Atlas by the *character of the constraint surface*:

**Fully smooth (no singularity, global C^{infinity}):**
FP, AC, CH — diffusion + smoothing eliminates all singular faces.

**Smooth interior, degenerate boundary (Holder at free boundary, no topology change):**
PME, TFE — degenerate diffusion creates a free boundary but no classical singularity.

**Smooth until singularity, then continuation (singularity is structural):**
MCF — curvature blowup is required; surgery/level-set continues. Smooth restart after singularity.
**HJ** — gradient blowup is required; viscosity solutions continue. *No* smooth restart — permanent non-smoothness.

**Open (singularity status unresolved):**
NS (3D) — the regularity question is the Millennium Problem.

**Constitutive (depends on specific kinetics):**
RD — ranges from globally smooth to blowup depending on reaction terms.

HJ and MCF occupy the *same structural tier* (singularity required, continuation exists) but differ in the *permanence* of the singularity: MCF's curvature blowup is a *discrete event* (the surface re-enters the smooth regime after surgery), while HJ's gradient blowup is a *permanent transition* (the solution never returns to C^1).

### 6.3 The Unique HJ Position: Variational Closure Without Dissipation

HJ is the *only* architecture in the Atlas whose constraint surface is sealed by a *variational* mechanism (Hopf–Lax + comparison) rather than a *dissipative* mechanism (Lyapunov functional + smoothing). This reveals a fundamental structural insight:

**Dissipation is sufficient but not necessary for closure.** Every parabolic architecture uses dissipation to close its constraint surface. HJ shows that an alternative exists: *convex variational structure* can close a constraint surface without any dissipation at all. The closure comes from the *convex geometry of the Hamiltonian* and the *minimization structure of the Hopf–Lax formula*, not from any energy decrease.

This insight positions HJ as the *structural complement* of the parabolic architectures: where they control dynamics through energy decrease, HJ controls dynamics through cost minimization. The two approaches are dual (in the Legendre-transform sense) — and together, they exhaust the two fundamental modes of PDE closure.

### 6.4 Summary

| Feature                    | HJ           | FP    | PME   | AC    | CH    | TFE   | MCF   | NS    | RD    |
|----------------------------|-------------|-------|-------|-------|-------|-------|-------|-------|-------|
| Closure type               | **Variational** | Linear | Dissipative | Dissipative | Dissipative | Dissipative | Dissip.-geom. | Open | Constitutive |
| Singularity                | **Required** | None  | None  | None  | None  | n-dep | Required | Open | Constitutive |
| Post-singularity           | **Viscosity** | N/A  | N/A   | N/A   | N/A   | N/A   | Surgery | Leray | N/A |
| Permanence of singularity  | **Permanent**| N/A   | N/A   | N/A   | N/A   | N/A   | Discrete| Open  | Constitutive |
| Dissipation functional     | **None**     | Free energy | Entropy | Ginzburg-Landau | Ginzburg-Landau | Surface energy | Area | Kinetic energy | N/A |
| Contraction metric         | **L^{infinity}**| Wasserstein | L^1 | N/A | N/A | N/A | N/A | N/A | N/A |
| Parameters                 | **0**        | 2     | 1     | 3     | 3     | 1     | **0** | 2     | Many  |
| Anomalies                  | 0            | 0     | 0     | 0     | 0     | 0-1   | 0     | 2     | 0-3+  |

HJ is the *unique variational, non-dissipative, certainly-singular, permanently-non-smooth* architecture in the Atlas — the structural dual of the parabolic wing, sealed by convexity and viscosity rather than by smoothing and Lyapunov monotonicity.

---

*End of Mode 3: Channels → Constraint Surface. The AD Criteria and Verdict will follow in the final file.*
