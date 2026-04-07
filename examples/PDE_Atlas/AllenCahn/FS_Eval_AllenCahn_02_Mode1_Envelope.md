# AD Evaluation: Allen–Cahn Equation — Mode 1: Axiom → Envelope

Allen Proxmire

April 2026

---

## Overview

Mode 1 traces the path from the Allen–Cahn axioms (AC-1 through AC-8) to the architectural envelope. The AC envelope is *fully closed* in all dimensions d <= 3, like the CH envelope, but with a different structural mechanism: where CH relies on fourth-order smoothing, AC relies on the *maximum principle* — a feature available to second-order parabolic equations but not to fourth-order ones. The maximum principle gives AC a structural advantage (automatic L^{infinity} control) that CH must earn through Sobolev embedding. In exchange, AC sacrifices mass conservation, which eliminates the coarsening dynamics that make CH physically rich.

Throughout, we work with the Allen–Cahn equation on a bounded domain Omega subset R^d (d = 1, 2, 3) with constant mobility M > 0:

    partial_t phi = M epsilon^2 Delta phi + M(phi - phi^3)
    nabla phi . n = 0  on partial Omega
    phi(x, 0) = phi_0(x)

The free energy is F[phi] = integral [f(phi) + (epsilon^2/2)|nabla phi|^2] dx with f(phi) = (1/4)(phi^2 - 1)^2.

---

## 1. Forbidden Configurations

### F1. Maximum Principle Violation

**Axiom source:** AC-2 (Locality), AC-5 (Free Energy), AC-7 (Mobility), second-order parabolic structure.

If |phi_0(x)| <= 1 for all x in Omega, then |phi(x, t)| <= 1 for all x and all t > 0. The standard double-well reaction term R(phi) = M(phi - phi^3) is *inward-pointing* at the boundary of [-1, 1]:

- At phi = +1: R(1) = M(1 - 1) = 0, and for phi > 1, R(phi) = M(phi - phi^3) < 0 (pushes phi back below 1).
- At phi = -1: R(-1) = 0, and for phi < -1, R(phi) > 0 (pushes phi back above -1).

The Laplacian term M epsilon^2 Delta phi preserves the maximum principle for second-order parabolic equations (by the classical maximum principle of Protter–Weinberger). The combination — second-order linear diffusion plus an inward-pointing reaction at the boundary of a convex set — yields:

    |phi_0| <= 1  =>  |phi(t)| <= 1    for all t > 0

States with |phi(x, t)| > 1 are forbidden for initial data in [-1, 1]. This is a *structural feature* that CH lacks — fourth-order parabolic equations do not satisfy a maximum principle, and CH solutions can overshoot ±1.

**Note:** For initial data with |phi_0| > 1 at some points, the reaction term still pulls phi back toward [-1, 1], and the maximum of |phi| is non-increasing in time. The invariance of [-1, 1] is the strongest statement.

### F2. Free-Energy Increasing Dynamics

**Axiom source:** AC-4 (Gradient-Flow Structure).

Any evolution along which F[phi(t)] increases is forbidden. The L^2 gradient-flow structure guarantees:

    dF/dt = -M integral |mu|^2 dx <= 0

This is an exact identity. The free energy is a strict Lyapunov functional: it decreases along every non-stationary trajectory. Oscillatory dynamics, limit cycles, and recurrence to higher-energy states are all axiomatically impossible. The AC architecture is *monotonically dissipative*.

### F3. Mass Conservation

**Axiom source:** AC-3 (Non-Conserved Order Parameter).

The total order parameter is *not* conserved in general:

    d/dt integral phi dx = integral partial_t phi dx = M integral (phi - phi^3 + epsilon^2 Delta phi) dx
                         = M integral (phi - phi^3) dx + M epsilon^2 integral Delta phi dx
                         = M integral (phi - phi^3) dx    [by Neumann BC]

The integral M integral(phi - phi^3) dx is nonzero in general. In particular:
- If phi is predominantly positive but not at +1, the total mass increases (the reaction pushes phi toward +1).
- If phi is predominantly negative, the total mass decreases.

Mass conservation (d/dt integral phi = 0) occurs *only* for the special case where the spatial average of phi - phi^3 vanishes — a non-generic condition. **Mass conservation is forbidden as a structural property.** The architecture cannot guarantee it and does not attempt to enforce it.

### F4. Nonlocal Chemical Potentials

**Axiom source:** AC-2 (Locality), AC-6 (Chemical Potential Definition).

The chemical potential mu = f'(phi) - epsilon^2 Delta phi is determined *locally* by phi and Delta phi at each point. Nonlocal chemical potentials — those depending on phi values at distant points, or determined by a global elliptic equation — are forbidden. There is no Poisson equation, no Green's function, no integral operator in the AC architecture.

### F5. Sub-Epsilon Interface Structure

**Axiom source:** AC-5 (Free Energy).

The gradient penalty (epsilon^2/2)|nabla phi|^2 sets a minimum interface width at O(epsilon). The equilibrium interface profile is phi(z) = tanh(z/(epsilon sqrt(2))), with width proportional to epsilon. Interfaces thinner than O(epsilon) carry excess gradient energy and are dynamically unstable — the Laplacian smoothing channel relaxes them to the equilibrium width on time scale O(epsilon^2/M).

### F6. Non-Standard Double-Well Potentials

**Axiom source:** AC-5 (Free Energy).

The architecture commits to f(phi) = (1/4)(phi^2 - 1)^2. Multi-well potentials (three or more minima), asymmetric potentials (wells at unequal depths), and potentials without the phi → -phi symmetry are outside the standard AC architecture. The double-well structure with equal-depth minima at ±1 is a constitutive selection.

### F7. Anisotropic Gradient Penalties

**Axiom source:** AC-5 + AC-8 (Free Energy + Euclidean Geometry).

The gradient penalty (epsilon^2/2)|nabla phi|^2 treats all spatial directions equally. Anisotropic penalties (direction-dependent epsilon) are forbidden under the standard axioms.

### F8. Non-Variational Forcing

**Axiom source:** AC-4 (Gradient-Flow Structure).

The AC equation is an *autonomous* gradient flow with no external forcing. The dynamics are entirely self-generated — driven by the descent of F, with no external energy input. Adding a forcing term g(x, t) to the right-hand side (partial_t phi = -M mu + g) would break the gradient-flow structure unless g is itself the gradient of some functional. Non-variational forcing is forbidden.

### Summary of Forbidden Configurations

| Label | Forbidden Configuration              | Excluding Axiom(s)     |
|-------|--------------------------------------|------------------------|
| F1    | \|phi\| > 1 (for \|phi_0\| <= 1)    | AC-2, AC-5, AC-7      |
| F2    | Free-energy increase                 | AC-4                   |
| F3    | Mass conservation (as structural law)| AC-3                   |
| F4    | Nonlocal chemical potentials         | AC-2, AC-6             |
| F5    | Sub-epsilon interface structure      | AC-5                   |
| F6    | Non-standard double-well potentials  | AC-5                   |
| F7    | Anisotropic gradient penalty         | AC-5, AC-8             |
| F8    | Non-variational forcing              | AC-4                   |

---

## 2. Necessary Configurations

### N1. Exact Lyapunov Dissipation Identity

**Source:** AC-4, AC-5, AC-6.

Compute:

    dF/dt = integral [f'(phi) partial_t phi + epsilon^2 nabla phi . nabla(partial_t phi)] dx

Integrate by parts (using nabla phi . n = 0):

    dF/dt = integral [f'(phi) - epsilon^2 Delta phi] partial_t phi dx = integral mu partial_t phi dx

Substitute partial_t phi = -M mu:

    dF/dt = -M integral |mu|^2 dx = -M ||mu||_{L^2}^2              ... (AC Lyapunov Identity)

This is an exact identity for all solutions. The dissipation rate is M ||mu||^2, vanishing if and only if mu = 0 everywhere (equilibrium).

**Integrated form:**

    F[phi(t)] + M integral_0^t ||mu(s)||^2 ds = F[phi_0]

The total dissipation budget is fixed at birth.

### N2. Maximum Principle (Invariance of [-1, 1])

**Source:** AC-2, AC-3, AC-5, AC-7 (second-order parabolic structure + inward-pointing reaction).

For initial data phi_0 with |phi_0(x)| <= 1:

    |phi(x, t)| <= 1    for all x in Omega, t >= 0

This is the *strongest* L^{infinity} bound available in the AC architecture, and it is obtained *for free* — without energy estimates, Sobolev embedding, or bootstrapping. The maximum principle is a structural gift of the second-order parabolic character.

More generally, for arbitrary initial data:

    max |phi(x, t)| <= max(max |phi_0|, 1)

The L^{infinity} norm is non-increasing once it enters [-1, 1], and if it starts outside, the reaction term pulls it back.

### N3. Interface Motion by Mean Curvature

**Source:** AC-2, AC-3, AC-4, AC-5 (combined).

In the sharp-interface limit epsilon → 0, the AC equation converges (in an appropriate sense) to the *motion by mean curvature* flow:

    V_n = M sigma kappa

where:
- V_n is the normal velocity of the interface (positive for outward motion)
- sigma = (2 sqrt(2)/3) epsilon is the surface tension
- kappa is the mean curvature (positive for convex surfaces)

A convex interface (kappa > 0) has V_n > 0 if the convention is that normal points inward — the interface moves *inward*, shrinking. A sphere of radius R shrinks as:

    dR/dt = -(d-1) M sigma / R

In d = 2: R^2(t) = R_0^2 - 2 M sigma t, so the circle vanishes at time T* = R_0^2 / (2 M sigma).
In d = 3: R^2(t) = R_0^2 - 4 M sigma t, vanishing at T* = R_0^2 / (4 M sigma).

**Interface annihilation is architecturally necessary:** any closed interface in AC must shrink and vanish in finite time (in the sharp-interface limit). There is no mechanism to sustain a curved interface — the non-conserved dynamics allow the enclosed phase to simply disappear. This is in stark contrast to CH, where mass conservation prevents interface annihilation (the enclosed phase must be transferred elsewhere).

### N4. Exponential Relaxation in Bulk Regions

**Source:** AC-4, AC-5.

In regions where phi is close to one of the wells (say phi ≈ 1 - delta with delta small), the linearized AC equation gives:

    partial_t (delta) ≈ -M f''(1) delta + M epsilon^2 Delta(delta) = -2M delta + M epsilon^2 Delta(delta)

Since f''(1) = 2 > 0, the uniform part relaxes exponentially:

    delta(t) ~ delta(0) exp(-2M t)

The order parameter approaches the well exponentially fast in bulk regions, with rate 2M (independent of epsilon and the domain size). The time scale for bulk relaxation is O(1/M) — much faster than the interface dynamics (which operate on time scale O(R^2 / (M sigma)) ~ O(R^2 / (M epsilon))).

### N5. Interface Width O(epsilon)

**Source:** AC-5.

The equilibrium (stationary) interface profile in one dimension is:

    phi_eq(z) = tanh(z / (epsilon sqrt(2)))

This profile satisfies mu = f'(phi) - epsilon^2 phi'' = 0 and has width proportional to epsilon. The interface width is set by the balance between the reaction channel (driving phi toward ±1, favoring sharp transitions) and the smoothing channel (penalizing gradients, favoring smooth transitions). The equilibrium width is the unique scale at which these two forces balance.

### N6. Metastability of Well-Separated Droplets

**Source:** AC-3, AC-4, AC-5.

A spherical droplet of one phase embedded in the other is *metastable* for the AC equation: it is not a stationary solution (it shrinks by mean curvature, N3), but the shrinking rate is slow for large droplets:

    dR/dt ~ -M epsilon / R

The lifetime of a droplet of radius R is T* ~ R^2 / (M epsilon), which is large for R >> epsilon. During this time, the droplet sits near a local minimum of F (the energy landscape has a well at each topologically distinct configuration), and the dynamics are confined to a slow manifold parameterized by the droplet radius.

For *multiple* well-separated droplets, the interactions are exponentially weak: the interaction between two droplets separated by distance L decays as exp(-C L / epsilon). The droplets evolve nearly independently, each shrinking by its own mean curvature, until they become small enough to vanish rapidly.

### N7. Global Regularity in d <= 3

**Source:** All axioms combined.

The AC equation has *unconditional global regularity* in dimensions d = 1, 2, 3:

- The maximum principle (N2) provides L^{infinity} control: ||phi(t)||_{L^infinity} <= max(||phi_0||_{L^infinity}, 1).
- L^{infinity} control bounds the nonlinear term: |phi - phi^3| <= C(1 + |phi|^3) <= C for |phi| <= max(||phi_0||_{L^infinity}, 1).
- The PDE becomes a linear heat equation with a bounded source: partial_t phi = M epsilon^2 Delta phi + g(x, t) where ||g||_{L^infinity} <= C.
- Standard parabolic regularity theory gives phi in C^{infinity}(Omega x (0, infinity)).

The regularity proof is *simpler* than the CH proof (which requires H^2 estimates and Sobolev embedding) because the maximum principle short-circuits the bootstrap. This is the structural advantage of second-order over fourth-order parabolic equations.

### N8. Absence of Finite-Time Blowup

**Source:** N2 + N7.

There is no finite-time blowup mechanism in the AC architecture:

- L^{infinity} is controlled by the maximum principle (no concentration of phi).
- The free energy is bounded below and monotone decreasing (no energy accumulation).
- The second-order smoothing controls the cubic nonlinearity (the Laplacian is sufficient in d <= 3).
- No conditional regularity criterion is needed — regularity is unconditional.

### Summary of Necessary Configurations

| Label | Necessary Configuration              | Forcing Axiom(s)        |
|-------|--------------------------------------|-------------------------|
| N1    | Exact Lyapunov identity              | AC-4, AC-5, AC-6       |
| N2    | Maximum principle (\|phi\| <= 1)     | AC-2, AC-5, AC-7       |
| N3    | Interface motion by mean curvature   | AC-2, AC-3, AC-4, AC-5 |
| N4    | Exponential bulk relaxation          | AC-4, AC-5              |
| N5    | Interface width O(epsilon)           | AC-5                    |
| N6    | Metastability of droplets            | AC-3, AC-4, AC-5       |
| N7    | Global regularity (d <= 3)           | All                     |
| N8    | No finite-time blowup               | N2, N7                  |

---

## 3. Envelope Inequalities (E1–E9)

---

**E1. Free-Energy Dissipation Identity (Exact)**

    F[phi(t)] + M integral_0^t ||mu(s)||_{L^2}^2 ds = F[phi_0]

Exact identity for all solutions. Total free energy at time t plus total dissipation over [0, t] equals initial free energy. No gap, no anomalous dissipation.

---

**E2. H^1 Control from Free Energy**

    (epsilon^2 / 2) ||nabla phi(t)||_{L^2}^2 <= F[phi(t)] <= F[phi_0]

Therefore:

    ||nabla phi(t)||_{L^2}^2 <= 2 F[phi_0] / epsilon^2    for all t >= 0

The free energy controls the H^1 seminorm uniformly in time. This bound is unconditional and dimension-independent.

---

**E3. Maximum Principle Bound**

    ||phi(t)||_{L^infinity} <= max(||phi_0||_{L^infinity}, 1)    for all t >= 0

For initial data in [-1, 1]:

    -1 <= phi(x, t) <= 1    for all x, t

This is the *strongest* envelope bound in the AC architecture — it provides L^{infinity} control *for free*, without any estimate. No other architecture in the PDE Atlas (NS, CH) has a comparable bound at this level of generality.

---

**E4. Interface Width Lower Bound**

    (Interface width) >= C epsilon

for a universal constant C > 0. Interfaces cannot be thinner than O(epsilon). The equilibrium profile phi = tanh(z/(epsilon sqrt(2))) achieves this bound.

---

**E5. Global Regularity (All d <= 3)**

    phi(t) in C^{infinity}(Omega)    for all t > 0,    d = 1, 2, 3

The envelope is *fully closed* in every spatial dimension. No regularity gap, no blowup channel, no conditional hypotheses. The maximum principle + standard parabolic regularity closes the bootstrap unconditionally.

---

**E6. Mean-Curvature Motion Law (Sharp-Interface Limit)**

In the limit epsilon → 0, the AC dynamics converge to motion by mean curvature:

    V_n = M sigma kappa,    sigma = (2 sqrt(2) / 3) epsilon

For a sphere of radius R:

    R(t) = sqrt(R_0^2 - 2(d-1) M sigma t)

vanishing at time T* = R_0^2 / (2(d-1) M sigma). This is the asymptotic envelope law governing interface dynamics at scales L >> epsilon.

---

**E7. Exponential Bulk Relaxation**

In regions where phi is close to a well (phi ≈ ±1 ∓ delta):

    |delta(x, t)| <= C exp(-2M t) ||delta_0||_{L^infinity}    [to leading order]

The bulk relaxation rate is 2M = M f''(±1), independent of epsilon and the domain size. Bulk relaxation is the *fastest* process in the AC architecture; interface dynamics operate on a slower time scale.

---

**E8. Reaction-Diffusion Balance Inequality**

The competition between the reaction channel R and the smoothing channel S determines the dynamics at each scale:

    At scale L:   R ~ M,    S ~ M epsilon^2 / L^2

    R dominates S when L >> epsilon  (reaction-dominated: bulk relaxation)
    S dominates R when L << epsilon  (diffusion-dominated: sub-interface smoothing)
    R ~ S when L ~ epsilon           (balance: interface width)

This balance defines the *architectural resolution scale* epsilon: the unique length at which the two channels are commensurate. Below epsilon, the smoothing channel controls; above epsilon, the reaction channel controls.

In Fourier space, the linearized growth rate around phi = 0 is:

    sigma(k) = M(1 - epsilon^2 k^2)

- Unstable modes: k < 1/epsilon (sigma > 0). The reaction drives phase separation.
- Stable modes: k > 1/epsilon (sigma < 0). The smoothing damps short-wavelength perturbations.
- Most unstable mode: k = 0 (sigma_max = M). Unlike CH, the most unstable mode in AC is the *uniform* mode (k = 0) — the fastest instability is homogeneous phase selection, not spatially modulated spinodal decomposition.

---

**E9. No Blowup Channel**

The second-order Laplacian smoothing dominates the cubic nonlinearity in d <= 3:

- The maximum principle bounds ||phi||_{L^infinity} unconditionally.
- Once ||phi||_{L^infinity} is bounded, the nonlinearity phi - phi^3 is bounded.
- The PDE reduces to a linear heat equation with bounded forcing.
- Parabolic regularity gives C^{infinity} smoothness.

There is no blowup gate, no conditional regularity criterion, and no dimensional restriction (within d <= 3). The envelope is sealed.

---

### Envelope Summary

The AC architectural envelope is defined by nine constraints (E1–E9) organized into three tiers:

**Tier 1 — Hard Constraints (exact identities and sharp bounds):**
- E1: Free-energy dissipation identity (exact).
- E2: H^1 control from energy (unconditional).
- E3: Maximum principle (sharp, for free).

**Tier 2 — Global Structure (unconditional, all dimensions):**
- E4: Interface width >= O(epsilon).
- E5: Global regularity (d <= 3, closed envelope).
- E8: Reaction-diffusion balance (sets architectural resolution).
- E9: No blowup channel.

**Tier 3 — Asymptotic Behavior:**
- E6: Mean-curvature motion law (sharp-interface limit).
- E7: Exponential bulk relaxation (rate 2M).

---

## 4. Central Architectural Finding

The AC Mode 1 envelope is *fully closed in all dimensions d <= 3*, with no open face, no regularity gap, and no blowup channel. This matches the CH envelope's closure but achieves it through a different and simpler mechanism.

### AC vs. CH Envelope Comparison

| Feature                    | Allen–Cahn                  | Cahn–Hilliard               |
|----------------------------|-----------------------------|-----------------------------|
| Envelope closure           | Closed (all d <= 3)        | Closed (all d <= 3)         |
| Closing mechanism          | Maximum principle (E3)     | Fourth-order smoothing (E5) |
| L^{infinity} control       | Free (maximum principle)   | Earned (Sobolev embedding)  |
| Energy identity            | dF/dt = -M\|\|mu\|\|^2    | dF/dt = -M\|\|nabla mu\|\|^2 |
| Mass conservation          | No (F3: forbidden)         | Yes (C1: enforced)          |
| Interface fate             | Shrink and vanish (E6)     | Merge and coarsen           |
| Open faces                 | None                       | None                        |
| Blowup channel             | None                       | None                        |
| PDE order                  | 2nd                        | 4th                         |
| Maximum principle          | Yes                        | No                          |

### Structural Assessment

The AC architecture is *simpler but less constrained* than CH:

- **Simpler:** Second-order (not fourth-order), fewer channels (four vs. five), simpler regularity proof (maximum principle vs. Sobolev embedding), simpler energy identity (||mu||^2 vs. ||nabla mu||^2).
- **Less constrained:** No mass conservation (the architecture allows phi to be created and destroyed), no coarsening dynamics (interfaces vanish rather than merge), no H^{-1} gradient-flow structure (the L^2 metric does not penalize large-scale rearrangements).

The AC architecture is the *minimal gradient-flow PDE* for a scalar order parameter with a double-well potential: it is the simplest dynamics that descend the Ginzburg–Landau free energy. CH is the *conserved* variant — richer, more constrained, more physical for phase-separation applications, but structurally more complex.

Both architectures achieve the same FS envelope verdict: fully closed, no anomalies, no blowup channel. The AC architecture achieves this with fewer structural resources, making it the *most structurally economical* PDE architecture in the PDE Atlas.

---

*End of Mode 1: Axiom → Envelope. Mode 2 (PDE → Extremal Dynamics) will follow in a subsequent file.*
