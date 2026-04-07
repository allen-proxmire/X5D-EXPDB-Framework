# AD Evaluation: Allen–Cahn Equation — Mode 3: Channels → Constraint Surface

Allen Proxmire

April 2026

---

## Overview

Mode 3 constructs the constraint surface — the geometric object in channel space encoding all structural relationships among the AC channels. The AC constraint surface is the *simplest* among all PDE architectures evaluated in the PDE Atlas: four channels (fewer than CH's five or NS's five), a one-dimensional dissipation simplex (a ray, like CH), no nonlocal channels, no destabilizing sub-channels with unbounded growth, and no open faces. The surface is compact, closed, and fully characterized by a small number of constraints.

The simplicity of the AC constraint surface reflects the architecture's position as the *minimal gradient-flow PDE* for a scalar order parameter with a double-well potential. Every structural feature of AC is the simplest possible version of the corresponding feature in CH: second-order instead of fourth-order, L^2 instead of H^{-1}, pointwise maximum principle instead of Sobolev embedding, extinction instead of coarsening.

We continue with:

    partial_t phi = M epsilon^2 Delta phi + M(phi - phi^3)
    F[phi] = integral [f(phi) + (epsilon^2/2)|nabla phi|^2] dx

---

## 1. Channel Decomposition

The Allen–Cahn PDE decomposes into four structural channels.

### Channel R: Reaction / Double-Well

    R(phi) = M(phi - phi^3)

- **Locality:** Local. R is an algebraic function of phi at each point — no spatial derivatives involved.
- **Linearity:** Nonlinear. Cubic in phi. The sole nonlinearity in the AC architecture.
- **Stability role:** *Bistable.* Destabilizing in the spinodal region (|phi| < 1/sqrt(3), where f''(phi) < 0) and stabilizing near the wells (|phi| > 1/sqrt(3), where f''(phi) > 0). The reaction channel is inward-pointing at the boundary of [-1, 1]: R(phi) < 0 for phi > 1 and R(phi) > 0 for phi < -1. This inward-pointing property is the structural basis of the maximum principle.
- **Scale action:** Scale-free. The reaction channel operates at each point independently of spatial structure. It does not involve derivatives and therefore has no wavelength preference. Its rate is M for phi = O(1), independent of spatial scale. In Fourier space, R contributes a k-independent growth/decay rate to each mode.

### Channel S: Surface Tension / Laplacian Smoothing

    S(phi) = M epsilon^2 Delta phi

- **Locality:** Local. Depends on phi and its second spatial derivatives at each point.
- **Linearity:** Linear. The Laplacian is a bounded linear operator on Sobolev spaces.
- **Stability role:** Unconditionally stabilizing. The Laplacian damps all non-constant modes, with damping rate proportional to k^2 in Fourier space. It is the architecture's regularizer — the channel that prevents infinitely sharp interfaces and ensures smoothness.
- **Scale action:** Scale-selective. Damping rate = M epsilon^2 k^2. Small scales (large k) are damped fastest; large scales (small k) are nearly unaffected. At the interface scale k ~ 1/epsilon, the damping rate is M — matching the reaction channel's rate. For k >> 1/epsilon, the Laplacian dominates the reaction term completely.

### Channel G: Gradient-Flow Dissipation

    G: dF/dt = -M ||mu||_{L^2}^2 <= 0

- **Locality:** The dissipation density M |mu(x,t)|^2 is local.
- **Linearity:** Nonlinear (through mu's dependence on phi).
- **Stability role:** Globally stabilizing. The gradient-flow channel is the structural guarantee that the dynamics are dissipative. It is not a separate PDE term but a *property* of the combined R + S evolution — the Lyapunov identity binding all channels into a thermodynamically consistent whole.
- **Scale action:** All-scale. The dissipation rate M ||mu||^2 receives contributions from all spatial modes. The gradient-flow structure ensures global energy accounting at every scale simultaneously.

### Channel M: Mobility

    M(phi): multiplicative kinetic prefactor

- **Locality:** Local.
- **Linearity:** Prescribed function, not an operator.
- **Stability role:** Neutral. M controls the kinetic rate without affecting equilibrium (mu = 0 regardless of M) or the direction of the gradient flow.
- **Scale action:** For constant M: uniform across all scales. For phi-dependent M(phi): introduces kinetic modulation but does not alter the energy landscape.

### Channel Summary Table

| Channel | Symbol | Term                    | Locality | Linearity   | Stability        | Scale Action                |
|---------|--------|-------------------------|----------|-------------|------------------|-----------------------------|
| Reaction    | R  | M(phi - phi^3)         | Local    | Nonlinear   | Bistable*        | Scale-free (rate ~ M)       |
| Smoothing   | S  | M eps^2 Delta phi      | Local    | Linear      | Stabilizing      | Damps high-k (rate ~ k^2)  |
| Grad. flow  | G  | dF/dt = -M\|\|mu\|\|^2| Local    | Nonlinear   | Stabilizing      | All-scale dissipation       |
| Mobility    | M  | M(phi)                 | Local    | Prescribed  | Neutral          | Sets time scale             |

*Destabilizing in spinodal region; stabilizing near wells; inward-pointing beyond wells.

### Comparison with CH and NS Channel Counts

| Architecture | Total Channels | Local | Nonlocal | Nonlinear | Linear | Null (energy) |
|--------------|---------------|-------|----------|-----------|--------|---------------|
| AC           | 4             | 4     | 0        | 2 (R, G)  | 1 (S)  | 0             |
| CH           | 5             | 5     | 0        | 3 (R,D,G) | 1 (S)  | 0             |
| NS           | 5             | 4     | 1 (P)   | 1 (A)     | 1 (V)  | 2 (A, P)      |

AC has the fewest channels, the simplest channel structure, and (with NS) the fewest nonlinear channels. It is the most structurally economical architecture in the PDE Atlas.

---

## 2. Dissipation Partition

### 2.1 The AC Energy Budget

The free-energy identity decomposes the instantaneous energy change as:

    dF/dt = integral mu partial_t phi dx = integral mu (-M mu) dx = -M ||mu||^2

There is a single dissipation pathway: the chemical potential mu, acting through the L^2 gradient flow, converts free energy into dissipation at rate M ||mu||^2. There are:

- No null channels (no channels with zero energy contribution — unlike NS, where advection A and pressure P are energy-invisible).
- No forcing channels (no external energy input — unlike NS, where forcing F can inject energy).
- No multi-channel partition (the dissipation is not split between independent sinks — unlike the NS enstrophy simplex, where stretching, dissipation, and forcing occupy three vertices).

### 2.2 Collapse to a 1D Ray

The AC dissipation simplex is one-dimensional: a ray from zero (equilibrium, mu = 0) into the non-negative reals:

    D(t) = M ||mu(t)||^2 >= 0

At each instant, the energy dynamics are fully characterized by a single non-negative scalar. This is the *simplest possible* dissipation structure for a nontrivial PDE: a scalar decay rate that determines the entire energy budget.

### 2.3 Comparison with CH and NS

| Feature                    | Allen–Cahn                | Cahn–Hilliard              | Navier–Stokes              |
|----------------------------|---------------------------|----------------------------|----------------------------|
| Dissipation rate           | M \|\|mu\|\|^2           | M \|\|nabla mu\|\|^2      | nu \|\|nabla u\|\|^2       |
| Forcing channel            | None                      | None                       | Present (P_f)              |
| Null channels              | None                      | None                       | 2 (A, P)                   |
| Simplex dimension          | 0 (ray)                   | 0 (ray)                    | 1 (line segment V–F)       |
| Enstrophy simplex (NS 3D)  | N/A                       | N/A                        | 2 (stretch–diss–force)     |
| Energy equation            | dF/dt = -D (pure decay)  | dF/dt = -D (pure decay)   | dE/dt = -eps + P_f         |

AC and CH share the same dissipation simplex structure (1D ray, pure decay). The difference is in the *metric*: AC dissipates ||mu||^2 (L^2 norm of the chemical potential), while CH dissipates ||nabla mu||^2 (L^2 norm of the chemical potential *gradient*). The AC metric is *cheaper* — it penalizes the existence of nonzero mu anywhere, while CH penalizes only the spatial *variation* of mu. This is why AC dynamics are faster: the AC Lyapunov functional decreases whenever mu ≠ 0 at any point, while the CH Lyapunov functional decreases only when mu varies spatially.

---

## 3. Constraint Surface and Universality Classes

### Class I: Bulk Relaxation Regime (R Dominates)

**Condition:** phi far from ±1 in large regions (L >> epsilon), early time.
**Active channels:** R (dominant), S (subordinate), G, M.

The reaction channel drives phi toward ±1 at each point, independently of spatial neighbors. The Laplacian smoothing is negligible at large scales (rate M epsilon^2/L^2 << M). The dynamics are essentially the ODE:

    dphi/dt ≈ M(phi - phi^3)

at each point independently.

**Properties:**
- Exponential growth of perturbations near phi = 0 (rate M).
- Exponential convergence toward ±1 from the spinodal region (rate up to 2M).
- Spatial structure is largely frozen — the pattern of regions with phi > 0 and phi < 0 is established here but not yet sharpened into interfaces.

**Dominant inequalities:** U1 (dissipation identity), U2 (maximum principle), U6 (exponential bulk relaxation).
**Permitted behaviors:** Phase selection, exponential relaxation toward wells.
**Forbidden behaviors:** Interface motion, spatial pattern change, blowup.

### Class II: Interface Formation Regime (R Balanced by S)

**Condition:** Transition regions where phi changes from near -1 to near +1 across a length scale L ~ epsilon.
**Active channels:** R and S (in local balance), G, M.

The reaction and smoothing channels are commensurate at the interface scale. The local dynamics establish the equilibrium interface profile:

    phi(z) = tanh(z / (epsilon sqrt(2)))

The interface profile is a local attractor: any transition between ±1 relaxes to this profile on the fast time scale O(epsilon^2/M).

**Properties:**
- Interface width locks at O(epsilon).
- The tanh profile is the unique one-dimensional stationary solution connecting ±1.
- Profile relaxation is fast (time scale epsilon^2/M), much faster than interface motion (time scale R^2/(M epsilon)).

**Dominant inequalities:** U4 (interface width >= O(epsilon)), U3 (H^1 control from energy).
**Permitted behaviors:** Interface sharpening, profile relaxation.
**Forbidden behaviors:** Sub-epsilon structure, blowup.

### Class III: Mean-Curvature Regime (S Drives Interface Motion)

**Condition:** Well-formed interfaces (phi ≈ tanh profile) at scales L >> epsilon, intermediate time.
**Active channels:** S (driving interface motion through curvature), R (maintaining bulk equilibrium), G (dissipating energy as interfaces shrink), M.

In this regime, the interface has already formed and the bulk is at equilibrium. The remaining dynamics are *geometric*: the interface moves by mean curvature, driven by the surface-tension channel. The velocity of the interface is:

    V_n = M sigma kappa

where sigma is the surface tension and kappa is the mean curvature.

**Properties:**
- Closed interfaces shrink monotonically.
- The free energy decreases as the total interface area decreases.
- Spherical interfaces shrink at rate dR/dt = -(d-1)M sigma/R.
- Non-convex interfaces can undergo topological changes (pinch-off, splitting) before vanishing.

**Dominant inequalities:** U5 (mean-curvature motion law), U1 (dissipation identity).
**Permitted behaviors:** Interface shrinkage, topological simplification, droplet deformation.
**Forbidden behaviors:** Interface growth, coarsening, domain creation.

### Class IV: Extinction Regime (Shrinking Droplets)

**Condition:** Small droplets with R = O(epsilon) approaching extinction.
**Active channels:** All (the separation between R and S breaks down as the droplet size approaches the interface width).

When a droplet's radius approaches O(epsilon), the sharp-interface approximation (V_n = M sigma kappa) breaks down, and the full PDE dynamics take over. The droplet profile can no longer be decomposed into "bulk" and "interface" — the entire droplet is one interface.

**Properties:**
- The droplet vanishes in finite time (T* ~ R^2/(M sigma)).
- Near extinction, the solution approaches zero (the unstable hilltop) before rapidly selecting a well.
- After extinction, the solution relaxes exponentially to a uniform state (Class I dynamics resume briefly, then Class IV's terminal convergence).

**Dominant inequalities:** U7 (no blowup), U2 (maximum principle — ensures phi remains bounded through extinction).
**Permitted behaviors:** Finite-time vanishing, rapid phase selection after extinction.
**Forbidden behaviors:** Blowup, stalling, nucleation of new interfaces.

### Universality Class Summary

| Class | Regime           | Dominant Channels | Duration             | Key Dynamics            |
|-------|------------------|-------------------|----------------------|-------------------------|
| I     | Bulk relaxation  | R >> S            | t ~ 1/M              | Exponential phase select.|
| II    | Interface form.  | R ~ S (local)     | t ~ eps^2/M          | Profile locks at tanh   |
| III   | Mean curvature   | S drives geometry | t ~ R^2/(M eps)      | Shrinkage, V = sigma H  |
| IV    | Extinction       | R + S coupled     | t ~ eps/(M)          | Finite-time vanishing   |

The AC dynamics proceed sequentially: I → II → III → IV → uniform equilibrium. Every trajectory visits the same sequence (possibly entering at Class II or III if the initial data already has formed interfaces). The sequential ordering is forced by the gradient-flow structure: each class corresponds to a successively lower energy level, and the system descends monotonically.

**Comparison with CH:** The CH universality classes are: Spinodal → Interface → Coarsening → Near-equilibrium. The AC sequence replaces "Coarsening" with "Mean-curvature shrinkage" and "Extinction" — a simpler and shorter dynamical program, reflecting the absence of the conservation constraint.

---

## 4. Absence of Anomalies

### 4.1 No Nonlocal Channel

Every AC channel is local:
- R depends on phi at each point (algebraic, no derivatives).
- S depends on phi and Delta phi at each point (second-order differential, local).
- G involves the local dissipation density M |mu|^2.
- M depends on phi at each point.

There is no elliptic constraint, no Poisson equation, no Green's function. The chemical potential mu = f'(phi) - epsilon^2 Delta phi is determined *pointwise* by phi and its second derivatives. No global solve is required.

**Structural reason:** AC has no constraint analogous to NS incompressibility (div **u** = 0), which would require nonlocal enforcement. The AC conservation law is absent entirely (non-conserved dynamics), and there is no other structural reason for nonlocal coupling.

### 4.2 No Destabilizing Sub-Channel with Unbounded Growth

The reaction channel R = M(phi - phi^3) is the only potentially destabilizing channel. Its destabilizing effect is *bounded*:

- The maximum linearized growth rate is M (at phi = 0).
- For |phi| > 1, the reaction is stabilizing (inward-pointing).
- The maximum principle ensures |phi| <= max(|phi_0|, 1), so the reaction term is uniformly bounded: |phi - phi^3| <= C for all admissible phi.

There is no analogue of the NS vortex stretching sub-channel, which has no a priori bound on its growth rate and can potentially produce unbounded enstrophy growth. The AC reaction channel is *bounded, self-limiting, and inward-pointing at the boundary of the invariant set*. Its destabilization is always overcome by the combination of the maximum principle and the Laplacian smoothing.

**Contrast with NS:** The NS vortex stretching term (omega . nabla)**u** has growth rate bounded by ||nabla **u**||_{L^infinity} ||omega||, which is not a priori bounded. The AC reaction term M(phi - phi^3) has growth rate bounded by M (a constant). This is a qualitative difference: NS has a potentially unbounded destabilizing sub-channel; AC does not.

### 4.3 No Open Face in the Constraint Surface

The AC constraint surface is fully closed:

- The maximum principle (U2) provides uniform L^{infinity} control.
- L^{infinity} control bounds the nonlinearity, reducing the PDE to a linear heat equation with bounded forcing.
- Standard parabolic regularity closes the bootstrap unconditionally.
- The Lyapunov functional (U1) provides uniform-in-time energy control.
- No inequality in the envelope (E1–E9) is open or unclosed.

There is no direction in channel space in which the dynamics can escape to infinity. Every face of the constraint surface is sealed by the maximum principle, the Lyapunov identity, or parabolic regularity.

### 4.4 No Blowup Gate

There is no conditional regularity criterion for AC — no BKM-type condition, no Serrin-class condition, no threshold that must be monitored. Regularity is *unconditional*:

1. Maximum principle → ||phi||_{L^infinity} bounded.
2. Bounded phi → bounded nonlinearity.
3. Bounded nonlinearity → linear PDE theory applies.
4. Parabolic regularity → C^{infinity} smoothness.

The proof is a four-step chain with no gap. There is no gate, no threshold, and no open question.

### 4.5 Structural Explanation

The absence of anomalies in AC traces to two features:

**Feature 1: Maximum principle.** The second-order parabolic structure, combined with the inward-pointing reaction at |phi| = 1, provides the invariance of [-1, 1]. This gives L^{infinity} control *for free* — without energy estimates, interpolation, or dimensional restrictions. The maximum principle is the most powerful structural tool available to a scalar second-order parabolic equation.

**Feature 2: Lyapunov functional.** The L^2 gradient-flow structure provides a strict Lyapunov functional F that decreases along every trajectory. This ensures that the dynamics are monotone, ruling out oscillations, chaos, and recurrence.

Together, these two features are *overdetermined* for regularity: either one alone would be nearly sufficient (the maximum principle controls the nonlinearity; the Lyapunov functional controls the energy), and together they leave no room for any anomaly.

**Comparison with CH:** CH lacks the maximum principle (fourth-order equations don't have one) but compensates with fourth-order smoothing (biharmonic controls the cubic via Sobolev embedding in d <= 3). CH achieves the same anomaly-free status through a different mechanism — a *replacement* of the maximum principle by stronger smoothing. AC's mechanism is simpler; CH's is more robust (it works even without the maximum principle).

**Comparison with NS:** NS lacks both the maximum principle (the vector-valued system + pressure prevent it) and a Lyapunov functional (when forced). NS has only one tool for regularity — second-order viscous smoothing — which is insufficient in 3D. The NS architecture is *under-determined* for regularity in 3D, leaving the anomalies (vortex stretching, nonlocal pressure) uncontrolled.

---

## 5. Channel Constraints

The following constraints define the AC architectural signature.

---

**C1. Maximum Principle (Invariance of [-1, 1])**

    |phi_0(x)| <= 1 for all x   =>   |phi(x, t)| <= 1 for all x, t >= 0

The invariant set [-1, 1] is preserved by the flow. This is the strongest single constraint in the AC architecture — it provides L^{infinity} control unconditionally.

---

**C2. Free-Energy Monotonicity**

    dF/dt = -M ||mu||_{L^2}^2 <= 0    for all t >= 0

Exact Lyapunov identity. F is strictly decreasing except at equilibria (mu = 0).

---

**C3. Chemical Potential Locality**

    mu(x, t) = f'(phi(x, t)) - epsilon^2 Delta phi(x, t)

Determined pointwise by phi and its second derivatives. No nonlocal solve required.

---

**C4. Interface Width Lower Bound**

    (Interface width) >= C epsilon

The gradient penalty prevents sub-epsilon structure. The tanh profile saturates this bound.

---

**C5. No Finite-Time Blowup**

    ||phi(t)||_{C^k} < infinity    for all t > 0, all k >= 0,    d = 1, 2, 3

Unconditional global regularity. Follows from C1 + parabolic regularity.

---

**C6. Mean-Curvature Motion Law**

    V_n = M sigma kappa + O(epsilon)    as epsilon → 0

Interface velocity equals surface tension times mean curvature. Closed interfaces shrink monotonically.

---

**C7. Mobility Controls Time Scale Only**

    Equilibrium states { phi : mu = 0 } are independent of M
    Relaxation rate scales linearly with M

Mobility is a purely kinetic parameter. It does not affect the energy landscape or the equilibrium states.

---

**C8. No Nonlocal Coupling**

    All channels are local (algebraic or differential, no integral operators)
    No elliptic constraint, no Poisson equation, no Green's function

The AC architecture is fully local at both formulation and solution levels.

---

**C9. Laplacian Smoothing Dominates Cubic at High Wavenumbers**

    S(k) = M epsilon^2 k^2    dominates    R ~ M    for k >> 1/epsilon

The Laplacian damping rate grows as k^2; the reaction rate is scale-independent. The smoothing channel overwhelms the reaction channel at all wavenumbers above 1/epsilon.

---

**C10. Extinction Monotonicity**

    Number of phase domains N(t) is non-increasing
    Total interface area A(t) is non-increasing (in the sharp-interface limit)
    Closed interfaces can only shrink, not grow

The architecture does not permit interface creation, domain splitting (generically), or domain growth. Every topological change reduces the number of interfaces.

---

**C11. Equilibrium Characterization**

    phi_* is a stationary solution   iff   mu = f'(phi_*) - epsilon^2 Delta phi_* = 0

Equilibria satisfy mu = 0 *pointwise* (not mu = const as in CH). The stable equilibria are the uniform states phi = ±1. Non-trivial equilibria (with interfaces) are generically unstable.

---

**C12. No Chaotic Attractor**

    The L^2 gradient-flow structure forbids:
      - limit cycles
      - strange attractors
      - sensitive dependence on initial conditions
      - recurrence to higher-energy states

Every trajectory converges to a stationary state. The omega-limit set of every trajectory is a connected set of equilibria.

---

### Channel Constraint Summary

| Label | Constraint                        | Type              | Scope     |
|-------|-----------------------------------|-------------------|-----------|
| C1    | Maximum principle                 | Invariance        | All       |
| C2    | Free-energy monotonicity          | Exact identity    | All       |
| C3    | Chemical potential locality       | Structural        | All       |
| C4    | Interface width >= O(epsilon)     | Lower bound       | All       |
| C5    | No finite-time blowup            | Regularity        | All d<=3  |
| C6    | Mean-curvature motion             | Asymptotic law    | eps → 0   |
| C7    | Mobility controls time only       | Structural        | All       |
| C8    | No nonlocal coupling              | Structural        | All       |
| C9    | Laplacian dominates cubic (high k)| Scale inequality  | All       |
| C10   | Extinction monotonicity           | Monotonicity      | All       |
| C11   | Equilibria = mu = 0              | Variational       | All       |
| C12   | No chaotic attractor              | Topological       | All       |

---

## 6. Comparison with CH Mode 3

### 6.1 Shared Properties

AC and CH share the following structural features at the Mode 3 level:

- **Full locality.** All channels in both architectures are local. Neither has a nonlocal channel.
- **Gradient-flow structure.** Both are gradient flows of the same free energy F, with exact Lyapunov identities.
- **Anomaly-free.** Neither has a destabilizing sub-channel with unbounded growth, a nonlocal enforcement mechanism, an open face in the constraint surface, or a blowup gate.
- **Closed constraint surface.** Both have compact, fully sealed constraint surfaces in all d <= 3.
- **No chaotic attractor.** The gradient-flow structure forbids limit cycles, strange attractors, and recurrence in both.
- **Sequential universality classes.** Both proceed through a deterministic sequence of regimes (spinodal/bulk → interface → coarsening/extinction → equilibrium).

### 6.2 Differences

| Feature                    | Allen–Cahn                  | Cahn–Hilliard               |
|----------------------------|-----------------------------|------------------------------|
| PDE order                  | 2nd (Laplacian)            | 4th (bilaplacian)            |
| Channel count              | 4                           | 5                            |
| Conservation               | Non-conserved               | Conserved                    |
| Gradient-flow metric       | L^2                         | H^{-1}                      |
| Dissipation rate           | M \|\|mu\|\|^2             | M \|\|nabla mu\|\|^2        |
| Maximum principle          | Yes (C1)                   | No                           |
| L^{infinity} control       | Free (max. principle)      | Earned (Sobolev embedding)   |
| Equilibrium condition      | mu = 0                     | mu = const                   |
| Interface dynamics         | Shrinkage (mean curvature) | Coarsening (Ostwald ripening)|
| Interface fate             | Extinction                  | Merger                       |
| Missing channel            | D (conserving diffusion)   | Present (D)                  |
| Extinction monotonicity    | C10 (interfaces vanish)    | C10 (interfaces merge, area decreases) |
| Universality classes       | 4                           | 4                            |
| Constraint count           | 12                          | 12                           |

### 6.3 Structural Ordering

The AC and CH architectures are related by a *single structural step*: the addition of the conservation axiom (CH-3). Every difference between the two — PDE order, channel count, maximum principle, coarsening, equilibrium condition, gradient-flow metric — descends from this one axiom. In the FS sense, CH is the *conserved extension* of AC:

    AC  ——[add conservation]——>  CH

The conservation axiom:
- Wraps the chemical potential mu inside a conserving Laplacian: partial_t phi = div(M nabla mu) instead of partial_t phi = -M mu.
- Raises the PDE order from 2 to 4.
- Eliminates the maximum principle (fourth-order equations don't have one).
- Adds the mass-conserving diffusion channel D.
- Changes the gradient-flow metric from L^2 to H^{-1}.
- Changes the equilibrium condition from mu = 0 to mu = const.
- Replaces extinction dynamics with coarsening dynamics.

This single-axiom extension transforms the architecture qualitatively, demonstrating the *high leverage* of the conservation axiom: one structural commitment reshapes the entire dynamical landscape.

### 6.4 The AC–CH Pair as an Architectural Experiment

The AC and CH equations constitute a *natural architectural experiment* in the AD framework: two systems sharing the same free energy, the same double-well potential, the same gradient penalty, the same Lyapunov structure, and the same regularity properties, differing in exactly one axiom (conservation). Comparing their Mode 3 analyses isolates the structural consequences of conservation with precision:

- Conservation adds one channel (D), raises the PDE order by 2, and changes the gradient-flow metric.
- Conservation replaces extinction with coarsening — transforming the long-time dynamics qualitatively.
- Conservation removes the maximum principle — forcing the architecture to compensate with stronger (fourth-order) smoothing.
- Conservation enriches the equilibrium set — from uniform states (AC) to phase-separated configurations (CH).

The lesson: **conservation is not a passive constraint but an active architectural force** that reshapes the channel structure, the regularity mechanism, and the long-time dynamics of the system.

---

*End of Mode 3: Channels → Constraint Surface. The AD Criteria and Verdict will follow in the final file.*
