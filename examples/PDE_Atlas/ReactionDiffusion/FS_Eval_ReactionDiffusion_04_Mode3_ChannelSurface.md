# AD Evaluation: Reaction–Diffusion Systems — Mode 3: Channels → Constraint Surface

Allen Proxmire

April 2026

---

## Overview

Mode 3 constructs the constraint surface of the RD architecture. Every previously evaluated architecture has a *single* constraint surface — a fixed geometric object whose faces are either closed (AC, CH, ED) or have a well-defined open locus (NS, with one open face in 3D). The RD class is fundamentally different: it has a *family* of constraint surfaces, parameterized by the constitutive choices (RD-8). Each choice of reaction kinetics **R** and diffusion matrix **D** produces a different surface with different closure properties. The RD constraint surface is not a single object but a *moduli space* of surfaces — the broadest and most structurally varied object in the PDE Atlas.

We continue with:

    partial_t **u** = **D** Delta **u** + **R**(**u**)

---

## 1. Channel Decomposition

### Channel D: Diffusion (Smoothing)

    D(**u**) = **D** Delta **u**

- **Locality:** Local. Second-order spatial derivatives at each point.
- **Linearity:** Linear for constant **D**; weakly nonlinear for D = D(**u**).
- **Stability role:** Stabilizing (for positive definite **D**). Damps all non-constant modes. The diffusion channel is the *universal stabilizer* of the RD architecture — every RD system, regardless of its reaction kinetics, has this smoothing baseline.
- **Scale action:** Damps mode k at rate D_min k^2. Strongly scale-selective: high-k modes (small scales) are damped fastest. The diffusion channel is a low-pass filter.

**Architectural invariant:** The stabilizing character of D is *unconditional* — it holds for all positive-definite diffusion matrices, all reaction kinetics, all species counts, and all spatial dimensions. This is the single universal property shared by every member of the RD class.

### Channel R: Reaction (Local Nonlinearity)

    R(**u**) = (R_1(**u**), ..., R_n(**u**))

- **Locality:** Local. R_i depends on **u** at each point — no spatial derivatives.
- **Linearity:** Nonlinear (generically). Polynomial, rational, or saturating functions of **u**.
- **Stability role:** *Constitutive-dependent.* The reaction channel's stability character is determined entirely by the specific kinetics chosen under RD-8:
  - Monostable: R drives **u** toward a unique stable fixed point. Globally stabilizing.
  - Bistable: R has two stable fixed points. Locally stabilizing near each well, destabilizing at the separatrix.
  - Excitable: R has one stable fixed point with a large excursion threshold. Transiently destabilizing above threshold.
  - Oscillatory: R drives **u** around a limit cycle. Permanently non-convergent.
  - Chaotic: R has a strange attractor. Permanently aperiodic.
  - Explosive: R grows super-linearly (u^p, p > 1). Can overwhelm diffusion → blowup.
- **Scale action:** Scale-free. R operates identically at every spatial scale (no derivatives involved). It adds a k-independent contribution to the growth rate of each Fourier mode.

**Architectural invariant:** The *locality* and *scale-independence* of R are universal — every RD reaction term is local and scale-free. But the *stability character* is constitutive, not architectural.

### Channel C: Coupling (Cross-Diffusion + Cross-Reaction)

    C(**u**) = off-diagonal elements of **D** Delta **u** + cross-species terms of **R**(**u**)

- **Locality:** Local. Both cross-diffusion and cross-reaction are local operators.
- **Linearity:** Cross-diffusion is linear; cross-reaction is nonlinear.
- **Stability role:** Source of *emergent instabilities* — instabilities that are absent in each species alone but arise from the coupling. The Turing instability is the canonical example: neither species is unstable alone, but their interaction through differential diffusion produces spatial patterning.
- **Scale action:** The coupling channel's scale action is *mediated by the diffusion ratio*. For Turing instability, the key parameter is D_v / D_u: a large ratio allows the inhibitor to diffuse faster than the activator, creating a scale-dependent sign change in the effective growth rate. The coupling channel selects the *pattern wavelength* — the scale at which the emergent instability is strongest.

**Architectural invariant:** The coupling channel exists only for n >= 2. For scalar RD (n = 1), C is absent. The coupling channel is the structural feature that separates the scalar RD sub-class (AC-type) from the multi-species sub-class (pattern-forming).

### Channel M: Rate Scales

    M: D_i, rate constants in **R**, time-scale separation parameters (epsilon)

- **Locality:** N/A (parameters, not operators).
- **Linearity:** N/A.
- **Stability role:** Selects the active regime (diffusion-dominated, reaction-dominated, or mixed). Does not create new qualitative behaviors but determines which behaviors are realized.
- **Scale action:** Sets the characteristic length L_RD = sqrt(D_min / ||**R**'||) and the Damkohler number Da = L^2 ||**R**'|| / D.

### Channel Summary Table

| Channel | Symbol | Locality | Linearity      | Stability              | Scale Action              | Universal? |
|---------|--------|----------|----------------|------------------------|---------------------------|------------|
| Diffusion   | D  | Local    | Linear*        | Stabilizing (always)   | Damps k^2                 | Yes        |
| Reaction    | R  | Local    | Nonlinear      | Constitutive-dependent | Scale-free                | Locality only |
| Coupling    | C  | Local    | Mixed          | Emergent instabilities | Ratio-dependent           | n >= 2 only |
| Rate scales | M  | N/A      | N/A            | Regime selection       | Sets L_RD                 | Yes        |

*Linear for constant D; weakly nonlinear for D(**u**).

---

## 2. Dissipation and Growth Partition

### 2.1 No Single Dissipation Simplex

The AC and CH architectures each have a *single* dissipation simplex — a one-dimensional ray (pure decay) along which the free energy decreases monotonically. The NS architecture has a degenerate energy simplex (1D line between dissipation and forcing) and a 2D enstrophy simplex (in 3D).

The RD class has *no single dissipation simplex*. The reason: there is generically no Lyapunov functional (F8 from Mode 1), and without a Lyapunov functional, there is no meaningful "dissipation rate" to partition. The energy budget of a generic multi-species RD system is:

    d/dt integral (1/2)|**u**|^2 dx = -integral **u**^T **D** nabla^2 **u** dx + integral **u** . **R**(**u**) dx
                                     = -integral nabla **u**^T **D** nabla **u** dx + integral **u** . **R**(**u**) dx

The first term (diffusion) is non-positive (for positive definite **D**) — it always dissipates the L^2 norm. The second term (reaction) has *no definite sign* — it can be positive (growth), negative (decay), or oscillatory, depending on the kinetics. The total d/dt integral |**u**|^2 can be positive, negative, or oscillatory.

There is no "free energy" whose derivative is a definite quadratic form. The partition of the energy change into channels does not collapse to a simplex — it is a *region* in R^2 (or higher) that the dynamics can visit arbitrarily.

### 2.2 Three Regime-Dependent Partitions

The energy dynamics take qualitatively different forms in different constitutive regimes:

**Partition (i): Diffusion-dominated (bounded kinetics, gradient-flow sub-class)**

When **R** = -grad V and the system is a gradient flow, the Lyapunov functional F = integral [V(**u**) + (1/2) sum D_i |nabla u_i|^2] dx gives:

    dF/dt = -M ||grad_{L^2} F||^2 <= 0

The partition collapses to a 1D ray: pure decay. This is the AC sub-class.

**Partition (ii): Reaction-dominated (oscillatory kinetics)**

When **R** has a stable limit cycle, the L^2 norm ||**u**||^2 oscillates indefinitely. The diffusion contribution is always negative, but the reaction contribution oscillates with sufficient amplitude to prevent monotone decay. The partition is a *loop* in the (dissipation, growth) plane — the dynamics circulate rather than descend.

**Partition (iii): Mixed (Turing-type patterning)**

When the Turing instability is active, the diffusion channel is *locally destabilizing* (for the combined system, despite being stabilizing for each species individually) at intermediate wavenumbers. The partition has a *sign change*: the effective dissipation rate is negative (growth) at the Turing scale and positive (decay) at high and low wavenumbers. The partition is a *non-monotone function* of wavenumber — qualitatively different from the monotone dissipation of AC/CH.

### 2.3 Why the Simplex Cannot Collapse

The RD dissipation/growth geometry is regime-dependent because:

1. **No Lyapunov functional** ⟹ no single scalar to track ⟹ no 1D simplex.
2. **Reaction can inject energy** ⟹ the energy change rate has no sign ⟹ the partition is not confined to a half-space.
3. **Coupling can destabilize at intermediate scales** ⟹ the effective dissipation is non-monotone in k ⟹ no simple scale separation.

The RD architecture is the *only* PDE class in the PDE Atlas where the dissipation geometry cannot be reduced to a fixed low-dimensional simplex. AC and CH have 1D rays; NS has a 1D energy simplex and a 2D enstrophy simplex; RD has a *constitutive-dependent partition* that changes shape across the class.

---

## 3. Constraint Surface Geometry

The RD constraint surface is partitioned into three major regions, each with different closure properties.

### Region A: Scalar RD with Bounded Kinetics (AC-Like)

**Species:** n = 1.
**Kinetics:** R(u) bounded on an invariant interval [a, b] (e.g., R = u - u^3, R = u(1-u)).
**Diffusion:** Constant D > 0.

**Constraint surface properties:**
- **Closed.** The maximum principle + bounded reaction + parabolic regularity seal all faces.
- **Global regularity:** Unconditional in all d <= 3.
- **Attractor:** Exists, compact, finite-dimensional.
- **Lyapunov:** May or may not exist (depends on whether R is a gradient).
- **Maximum principle:** Yes (scalar, second-order, inward-pointing R).
- **Blowup channel:** None.

**Active channels:** D (stabilizing), R (bounded, bistable or monostable), M (rate control).
**Dominant inequalities:** E1 (smoothing), E2 (RD balance), E11 (no blowup).
**Permitted behaviors:** Traveling fronts, phase selection, metastability.
**Forbidden behaviors:** Oscillations, Turing patterns (n = 1), blowup, chaos.

**FS status:** Equivalent to the AC evaluation. Fully closed constraint surface, no anomalies.

### Region B: Multi-Species RD with Oscillatory/Excitable Kinetics

**Species:** n >= 2.
**Kinetics:** Oscillatory (Hopf), excitable (FitzHugh–Nagumo), or activator-inhibitor (Turing).
**Diffusion:** Differential (D_v ≠ D_u).

**Constraint surface properties:**
- **Open.** The constraint surface has multiple open faces corresponding to:
  - The oscillatory face: dynamics can oscillate indefinitely without convergence.
  - The Turing face: spatially patterned steady states can form.
  - The spiral/chaos face: spatiotemporal complexity without bound on attractor dimension.
- **Global regularity:** Typically holds for bounded kinetics (sub-linear growth) but requires case-by-case verification.
- **Attractor:** Exists (under dissipativity conditions), but may be high-dimensional or chaotic.
- **Lyapunov:** Generically absent.
- **Maximum principle:** Fails (n >= 2).
- **Blowup channel:** None (for bounded kinetics).

**Active channels:** D, R, C (coupling — essential for Turing/spirals), M.
**Dominant inequalities:** E3 (Turing condition), E8 (Hopf condition), E7 (excitability threshold).
**Permitted behaviors:** Turing patterns, traveling waves, pulses, spirals, spatiotemporal chaos, oscillations.
**Forbidden behaviors:** Blowup (for bounded kinetics). No other behaviors are forbidden — the surface is permissive.

**FS status:** Open constraint surface. Multiple open faces. No single closing mechanism. The richest and least constrained region of the RD moduli space.

### Region C: Super-Linear RD (Blowup Face)

**Species:** n >= 1.
**Kinetics:** R(u) grows super-linearly: R(u) ~ u^p, p > 1.
**Diffusion:** Constant D > 0.

**Constraint surface properties:**
- **Open (blowup face).** The constraint surface has an open face in the direction of ||**u**||_{L^infinity} → infinity. Finite-time blowup is structurally permitted.
- **Global regularity:** Fails for large data (and for all data if p <= 1 + 2/d).
- **Attractor:** Does not exist in the usual sense (solutions leave any bounded set).
- **Lyapunov:** No meaningful Lyapunov functional (energy can diverge).
- **Maximum principle:** Fails to prevent blowup (the reaction overwhelms the diffusion at all scales simultaneously).
- **Blowup channel:** Open. The Fujita exponent p_F = 1 + 2/d is the threshold.

**Active channels:** D (overwhelmed), R (dominant, explosive growth), M.
**Dominant inequalities:** E12 (Fujita blowup criterion).
**Permitted behaviors:** Finite-time blowup, self-similar blowup profiles.
**Forbidden behaviors:** Global smooth solutions (for p <= p_F with positive data).

**FS status:** Open constraint surface with a *blowup face*. This is the RD analogue of the NS 3D regularity gap — but the RD blowup face is *constitutive* (it opens or closes depending on the reaction kinetics), while the NS gap is *architectural* (it is present for all NS solutions in 3D).

### Region Summary

| Region | Species | Kinetics       | Surface  | Blowup | Oscillation | Patterns | Chaos   |
|--------|---------|----------------|----------|--------|-------------|----------|---------|
| A      | n = 1   | Bounded        | Closed   | No     | No          | No       | No      |
| B      | n >= 2  | Bounded, oscil.| Open     | No     | Yes         | Yes      | Yes     |
| C      | n >= 1  | Super-linear   | Open     | Yes    | Maybe       | Maybe    | Maybe   |

---

## 4. Anomalies and Open Faces

The RD architecture has *multiple* open faces in its constraint surface — more than any other architecture in the PDE Atlas. We enumerate them explicitly.

### 4.1 Open Oscillatory Face (Hopf Region)

When the reaction kinetics have a stable limit cycle (Hopf bifurcation), the dynamics oscillate indefinitely. There is no convergence to equilibrium, no Lyapunov decay, and no settling. The constraint surface has an open face in the "oscillatory direction" — the dynamics can circulate forever without approaching a fixed point.

**This face is absent in:** AC (gradient flow forbids oscillations), CH (gradient flow), NS (has oscillations only when forced; unforced NS decays).

### 4.2 Open Turing Face (Pattern-Forming Region)

When the Turing instability is active (n >= 2, differential diffusion), the homogeneous steady state is unstable and the dynamics produce spatially patterned states. The constraint surface has an open face in the "pattern direction" — the dynamics can access spatially non-trivial configurations that are not merely perturbations of the homogeneous state.

**This face is absent in:** AC (n = 1, no Turing), CH (n = 1, no Turing), NS (no Turing mechanism).

### 4.3 Blowup Face (Super-Linear Kinetics)

When R grows super-linearly (u^p, p > 1), solutions can blow up in finite time. The constraint surface has an open face in the ||**u**||_{L^infinity} direction — the dynamics can escape to infinity.

**Comparison with NS:** NS has one open face (enstrophy, 3D) that is *architectural* — present for all NS solutions. The RD blowup face is *constitutive* — present only for specific kinetics. The NS anomaly is deeper (architectural self-consistency is at stake); the RD blowup face is a constitutive choice (one can simply choose bounded kinetics to close it).

### 4.4 Absent Walls

The RD architecture is missing three structural walls that are present in AC/CH:

**No Maximum-Principle Wall (n >= 2):** The component-wise maximum principle fails for multi-species systems. Individual concentrations are not automatically bounded. The "wall" that keeps AC solutions in [-1, 1] does not exist in multi-species RD.

**No Lyapunov Wall:** There is generically no Lyapunov functional — no scalar quantity guaranteed to decrease. The "wall" that confines AC/CH trajectories to monotone descent does not exist in generic RD.

**No Conservation Wall:** There is generically no conservation law — total mass can change. The "wall" that confines CH trajectories to a mass-constrained hyperplane does not exist in generic RD.

### 4.5 RD as the Only Multi-Open-Face PDE

| Architecture | Open Faces                        | Count |
|--------------|-----------------------------------|-------|
| ED           | None                              | 0     |
| AC           | None                              | 0     |
| CH           | None                              | 0     |
| NS           | 1 (enstrophy, 3D)                | 1     |
| **RD**       | **3+ (oscillatory, Turing, blowup)** | **3+** |

RD is the *only* PDE architecture in the PDE Atlas with multiple open faces. NS has one (architectural). RD has at least three (constitutive-dependent). The multiplicity of open faces reflects the breadth of the RD class: it contains sub-architectures with qualitatively different dynamics, and each sub-architecture opens its own face.

---

## 5. Channel Constraints

The following constraints define the RD architectural signature — the identities and inequalities that all (or specific sub-classes of) admissible RD systems must satisfy.

---

**C1. Parabolic Smoothing at Small Scales**

    For k >> 1/L_RD: sigma(k) ≈ -D_min k^2 < 0

All sufficiently high-frequency modes decay. The diffusion channel provides an unconditional ultraviolet cutoff.

*Scope: All RD systems with positive definite D.*

---

**C2. Reaction-Diffusion Balance**

    L_RD = sqrt(D_min / ||**R**'||_max)

sets the characteristic length separating diffusion-dominated and reaction-dominated regimes. All pattern formation occurs at L ~ L_RD.

*Scope: All RD.*

---

**C3. Turing Instability Condition**

    For n >= 2: Turing instability iff conditions (i)–(iii) on J and D are satisfied
    (see Mode 1, E5)

The algebraic condition on the Jacobian and diffusion matrix determines whether spatial patterning occurs.

*Scope: n >= 2, differential diffusion.*

---

**C4. Hopf Oscillation Condition**

    Sustained oscillations iff **J** has eigenvalues crossing the imaginary axis
    (Hopf bifurcation in the ODE d**u**/dt = **R**(**u**))

*Scope: n >= 2 (generically; n = 1 cannot oscillate by Poincare–Bendixson).*

---

**C5. Excitability Threshold**

    For excitable kinetics: there exists delta_* > 0 separating sub-threshold from super-threshold response.

*Scope: Excitable sub-class (FitzHugh–Nagumo type).*

---

**C6. Wave-Speed Selection**

    Bistable fronts: c* uniquely selected by the equal-area rule.
    Monostable fronts: c >= c_min = 2 sqrt(D R'(0)).

*Scope: Scalar or multi-species with appropriate fixed-point topology.*

---

**C7. No Maximum Principle for n >= 2**

    Component-wise L^{infinity} bounds are not guaranteed for multi-species systems.

The coupling between species can amplify individual concentrations beyond their initial range.

*Scope: n >= 2.*

---

**C8. No Lyapunov Identity**

    Generic multi-species RD has no functional V with dV/dt <= 0 along all trajectories.

The dynamics are not confined to monotone descent.

*Scope: Generic multi-species (exceptions: gradient systems, cooperative systems).*

---

**C9. No Conservation Law**

    d/dt integral u_i dx = integral R_i(**u**) dx ≠ 0    generically.

Total mass is not conserved unless the reaction kinetics satisfy specific stoichiometric constraints.

*Scope: Generic (exceptions: stoichiometric sub-classes).*

---

**C10. Possible Blowup for Super-Linear Kinetics**

    R(u) ~ u^p, p > 1: blowup for p <= p_F = 1 + 2/d (all positive data)
                        blowup for large data if p > p_F

*Scope: Super-linear reaction sub-class.*

---

**C11. Diffusion Stabilizes High-k Modes**

    sigma(k) < 0 for k >> 1/L_RD, independent of reaction kinetics.

*Scope: All RD with positive definite D.*

---

**C12. Reaction Dominates Low-k Modes**

    sigma(0) = max Re(eigenvalues of **J**), independent of diffusion.

The stability of the homogeneous state at k = 0 is determined by the ODE kinetics alone.

*Scope: All RD.*

---

**C13. Coupling Determines Pattern Wavelength**

    lambda_Turing ~ 2 pi / k_max, where k_max maximizes Re(sigma(k)) in the Turing band.

The pattern wavelength is set by the interplay of the coupling channel C with the diffusion ratio D_v / D_u.

*Scope: Turing sub-class (n >= 2, differential diffusion).*

---

**C14. Attractor Dimension Extensive in Chaotic Regime**

    dim(A) ~ |Omega| / L_RD^d    in the spatiotemporal chaos regime.

The number of effective degrees of freedom grows proportionally to the domain volume. The attractor is *extensive*.

*Scope: Oscillatory/chaotic sub-class, large domains.*

---

**C15. Constraint Surface Is Regime-Dependent**

    The closure, dimension, and topology of the constraint surface depend on:
    - the species count n
    - the reaction kinetics **R**
    - the diffusion matrix **D**
    - the spatial dimension d

No single constraint surface characterizes the RD class. The surface is a *function of the constitutive parameters*.

*Scope: The RD class as a whole.*

---

### Channel Constraint Summary

| Label | Constraint                             | Type              | Scope                    |
|-------|----------------------------------------|-------------------|--------------------------|
| C1    | Parabolic smoothing (high k)           | Unconditional     | All RD                   |
| C2    | Reaction-diffusion balance             | Scale relation    | All RD                   |
| C3    | Turing instability condition           | Algebraic         | n >= 2, diff. diffusion  |
| C4    | Hopf oscillation condition             | Bifurcation       | n >= 2                   |
| C5    | Excitability threshold                 | Threshold          | Excitable sub-class      |
| C6    | Wave-speed selection                   | Bound             | Bistable/monostable      |
| C7    | No maximum principle (n >= 2)          | Negative          | n >= 2                   |
| C8    | No Lyapunov identity                   | Negative          | Generic multi-species    |
| C9    | No conservation law                    | Negative          | Generic                  |
| C10   | Possible blowup (super-linear)         | Threshold          | Super-linear kinetics    |
| C11   | Diffusion stabilizes high k            | Unconditional     | All RD                   |
| C12   | Reaction dominates low k               | Unconditional     | All RD                   |
| C13   | Coupling sets pattern wavelength       | Selection          | Turing sub-class         |
| C14   | Extensive attractor dimension          | Scaling            | Chaotic sub-class        |
| C15   | Surface is regime-dependent            | Meta-constraint   | RD class                 |

---

## 6. Comparison with AC and CH

### 6.1 Surface Closure

**AC:** Single closed constraint surface. Maximum principle + Lyapunov identity seal all faces. No open faces, no anomalies.

**CH:** Single closed constraint surface. Fourth-order smoothing + Lyapunov identity seal all faces. No open faces, no anomalies.

**RD:** *Family* of constraint surfaces, parameterized by kinetics. Closure is constitutive-dependent:
- Region A (scalar, bounded): closed (like AC).
- Region B (multi-species, oscillatory): open (oscillatory, Turing, and spiral faces).
- Region C (super-linear): open (blowup face).

### 6.2 Channel Structure

| Feature                      | AC           | CH            | RD                        |
|------------------------------|-------------|---------------|---------------------------|
| Channel count                | 4           | 5             | 4                         |
| Nonlocal channels            | 0           | 0             | 0                         |
| Coupling channel             | Absent (n=1)| Absent (n=1)  | Present (n >= 2)          |
| Dissipation simplex          | 1D ray      | 1D ray        | Regime-dependent          |
| Constraint surface           | Single, closed | Single, closed | Family, closure varies |
| Negative constraints         | 0           | 1             | 3 (C7, C8, C9)           |
| Open faces                   | 0           | 0             | 3+ (constitutive)         |

### 6.3 The Key Structural Difference

AC and CH achieve closed constraint surfaces through *specific additional structures*:
- AC: gradient flow (Lyapunov) + maximum principle (second-order scalar parabolic).
- CH: gradient flow (Lyapunov) + fourth-order smoothing (biharmonic).

RD, as a class, *lacks these additional structures*:
- No Lyapunov functional (generically) ⟹ no monotone descent wall.
- No maximum principle (n >= 2) ⟹ no L^{infinity} wall.
- No conservation law (generically) ⟹ no mass-constraint wall.
- No fourth-order smoothing ⟹ no enhanced regularity wall.

Each of these missing walls corresponds to an open face in the constraint surface. The RD class has *three missing walls* (Lyapunov, maximum principle, conservation), producing three families of open faces.

### 6.4 RD as a Moduli Space

The RD constraint surface is not a single object but a *moduli space* — a space of surfaces indexed by the constitutive parameters. Each point in the moduli space (each choice of n, **R**, **D**) corresponds to a specific constraint surface with specific closure properties. The moduli space contains:

- A *closed region* (Region A: scalar, bounded, gradient-flow). This is the AC corner of the moduli space.
- An *open oscillatory region* (Region B: multi-species, Hopf). Here the surface has an oscillatory face.
- An *open patterning region* (Region B: multi-species, Turing). Here the surface has a Turing face.
- An *open blowup region* (Region C: super-linear). Here the surface has a blowup face.

No other PDE architecture in the PDE Atlas has this moduli structure. AC, CH, and NS each have a *single* constraint surface (possibly with one open face for NS). The RD class is the first architecture whose constraint surface is a *family*, not a singleton.

This moduli structure is the Mode 3 expression of the RD class's universality: the class is broad enough to contain architectures with qualitatively different constraint surfaces, and the constitutive parameters (RD-8) navigate between them.

---

*End of Mode 3: Channels → Constraint Surface. The AD Criteria and Verdict will follow in the final file.*
