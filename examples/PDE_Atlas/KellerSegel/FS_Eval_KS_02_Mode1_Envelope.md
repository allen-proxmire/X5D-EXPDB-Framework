# AD Evaluation: Keller–Segel System — Mode 1: Axiom → Envelope

Allen Proxmire

April 2026

---

## Overview

Mode 1 traces the path from the KS axioms (KS-1 through KS-10) to the architectural envelope. The KS envelope is *structurally unique* in the PDE Atlas: it is the first envelope whose closure or openness is determined by a *nonlocal, scale-critical competition* between two opposing forces — entropy (diffusion, spreading) and aggregation (chemotactic drift, concentration). The competition is mediated by a nonlocal potential (the chemoattractant v), and its outcome is controlled by a single invariant: the total mass M = integral u dx. The mass M determines *everything*: whether the free energy is bounded below (M < 8 pi) or unbounded below (M > 8 pi), whether the solution exists globally or blows up, and whether the constraint surface is closed or has an open blowup face.

The KS envelope introduces the concept of *energy-landscape-controlled blowup*: the free energy F[u] is a Lyapunov functional (dF/dt <= 0, always), but the energy *landscape* changes qualitatively at the critical mass M = 8 pi. Below 8 pi, the landscape has a global minimum (the diffusion-dominated equilibrium); above 8 pi, the landscape has no lower bound (the aggregation-dominated free fall to -infinity, which is the blowup). The KS is the *only architecture in the Atlas where the Lyapunov structure itself drives the singularity* — the free energy decreases monotonically *toward* the blowup.

Throughout:

    u_t = Delta u - div(u nabla v),    -Delta v = u

on R^2, with u >= 0, integral u = M.

---

## 1. Forbidden Configurations

### F1. Hamiltonian Reversibility

**Axiom source:** KS-10 (No Hamiltonian Structure), KS-5 (Free Energy Dissipation).

The KS system is *dissipative*: the free energy F[u] decreases monotonically (dF/dt <= 0). The dynamics have a preferred time direction — forward in time corresponds to free-energy descent. Time-reversibility is forbidden: the system cannot "climb back up" the energy landscape.

This places the KS on the *opposite side* from NLS and KdV (which are Hamiltonian and time-reversible) and on the *same side* as FP, PME, and AC/CH (which are dissipative gradient flows). But the KS dissipation has a twist: unlike FP/PME/AC/CH (where the free energy is bounded below and drives convergence to equilibrium), the KS free energy can decrease to -infinity (for M > 8 pi), driving the system to singularity rather than equilibrium.

### F2. Shock Formation (Burgers/HJ Type)

**Axiom source:** KS-3 (Diffusion), KS-4 (Chemotactic Drift Structure).

The KS does not have the first-order self-advection (u u_x) that produces Burgers shocks. The chemotactic drift -div(u nabla v) is a first-order *advection by an external field* (nabla v), not self-advection. The diffusion Delta u prevents gradient steepening even in the advection. The KS blowup is *concentration* (u → infinity at a point) not *steepening* (nabla u → discontinuity).

### F3. Oscillatory Dispersion

**Axiom source:** KS-3 (Real Diffusion), KS-10.

The KS time derivative is u_t (real), not i u_t (imaginary). The diffusion is Delta u (real, dissipative), not -i Delta u (imaginary, dispersive). There is no dispersion, no oscillatory spreading, no Schrödinger-type dynamics. The KS is *purely diffusive-aggregative*.

### F4. Finite-Speed Propagation

**Axiom source:** KS-3 (Non-Degenerate Diffusion), KS-7 (Nonlocal Aggregation).

The diffusion Delta u has infinite propagation speed (the heat kernel has support on all of R^2 for any t > 0). The nonlocal potential v = (-Delta)^{-1} u couples all points instantaneously. The KS has *doubly infinite* propagation speed — through both the diffusion and the nonlocal potential. Finite-speed propagation (compact support preservation, free boundaries) is forbidden.

### F5. Entropy Increase

**Axiom source:** KS-5 (Free Energy), Wasserstein gradient-flow structure.

The free-energy dissipation identity:

    dF/dt = -integral u |nabla(log u - v)|^2 dx <= 0

The free energy F is non-increasing. The *entropy* integral u log u dx can increase or decrease (it is not separately monotone), but the *free energy* F = integral u log u - (1/2) integral u v is monotonically non-increasing. The entropy-potential combination F is the correct Lyapunov functional — it always decreases.

### F6. Mass Loss

**Axiom source:** KS-6 (Mass Conservation).

    d/dt integral u dx = 0

Total mass M is exactly conserved. The divergence-form structure + no-flux conditions ensure no mass enters or leaves.

### F7. Global Regularity for All Masses

**Axiom source:** KS-8 (Blowup Mechanism), KS-9 (Critical Mass).

In 2D, the KS blows up for M > 8 pi. Global regularity for *all* masses is forbidden — the architecture's destabilizing channel (aggregation) can overwhelm the stabilizing channel (diffusion) when the mass is sufficiently large. This is the *structural openness* of the KS envelope: the constraint surface has an open blowup face for M > 8 pi.

### F8. Full Locality

**Axiom source:** KS-7 (Nonlocal Aggregation).

The aggregation channel is *nonlocal*: the drift velocity nabla v at x depends on u(y) for all y through the Green's function of -Delta. The KS is *not* fully local — it has a nonlocal channel (the chemoattractant potential), similar to NS (which has the nonlocal pressure). Full locality is forbidden.

### F9. Soliton Formation

**Axiom source:** KS-3, KS-4, KS-10.

The KS has no Hamiltonian structure, no dispersion, and no balance between dispersion and nonlinearity. The dynamics are *purely diffusive-aggregative* — there is no mechanism for the formation of shape-preserving traveling waves (solitons). The KS can form *steady states* (for M < 8 pi) but not *traveling coherent structures* in the soliton sense.

### F10. Integrability

**Axiom source:** KS-7 (Nonlocal), KS-10 (No Hamiltonian).

The KS has no Lax pair, no bi-Hamiltonian structure, no inverse scattering transform, and no infinite hierarchy of conservation laws. The system has *one* conservation law (mass) and *one* Lyapunov functional (free energy), but no infinite structural hierarchy. The KS is *not integrable* — it is a *dissipative, nonlocal, finite-invariant* system.

### Summary of Forbidden Configurations

| Label | Forbidden Configuration               | Excluding Axiom(s)        |
|-------|---------------------------------------|---------------------------|
| F1    | Hamiltonian reversibility             | KS-5, KS-10              |
| F2    | Shock formation                       | KS-3, KS-4               |
| F3    | Oscillatory dispersion                | KS-3, KS-10              |
| F4    | Finite-speed propagation              | KS-3, KS-7               |
| F5    | Entropy (free-energy) increase        | KS-5                     |
| F6    | Mass loss                             | KS-6                     |
| F7    | Global regularity for all masses      | KS-8, KS-9               |
| F8    | Full locality                         | KS-7                     |
| F9    | Soliton formation                     | KS-3, KS-10              |
| F10   | Integrability                         | KS-7, KS-10              |

---

## 2. Necessary Configurations

### N1. Non-Negative Density

**Source:** KS-1.

u(x, t) >= 0 for all x, t (as long as the smooth solution exists). The non-negativity is preserved by the PDE: u = 0 is a sub-solution of u_t = Delta u - div(u nabla v), and the maximum principle for the advection-diffusion equation preserves non-negativity.

### N2. Nonlocal Chemoattractant

**Source:** KS-2, KS-5, KS-7.

The chemoattractant v is determined by the Poisson equation -Delta v = u:

    v(x) = -(1/(2 pi)) integral log|x - y| u(y) dy    [2D Newtonian potential]

This is a *nonlocal integral* of u — the chemoattractant at x depends on the cell density *everywhere*. The nonlocal coupling is the structural origin of the aggregation mechanism.

### N3. Diffusion (Stabilizing)

**Source:** KS-3.

The diffusion Delta u spreads the cell density at rate k^2 in Fourier space. It is the *stabilizing channel* — the mechanism that opposes concentration and prevents blowup when the mass is subcritical.

### N4. Aggregation (Destabilizing)

**Source:** KS-4, KS-7.

The chemotactic drift -div(u nabla v) = -div(u nabla(-Delta)^{-1} u) concentrates the cell density. The aggregation is:
- Nonlocal (mediated by the Green's function).
- Quadratic in u (the drift is nabla v = nabla(-Delta)^{-1} u, and the flux is u times nabla v — a product of u with an integral of u).
- Self-reinforcing (more cells → more signal → more drift → more cells).

### N5. Free-Energy Functional

**Source:** KS-5, KS-10.

    F[u] = integral u log u dx - (1/2) integral u v dx
         = integral u log u dx + (1/(4 pi)) integral integral u(x) log|x - y| u(y) dx dy

The free energy is the difference of:
- Entropy: integral u log u dx (favors spreading; increases as u spreads).
- Interaction energy: -(1/2) integral u v dx = (1/(4 pi)) integral integral u(x) log|x - y| u(y) dx dy (favors aggregation; decreases as u concentrates).

The competition between these two terms is the *fundamental energetic tension* of the KS architecture.

### N6. Wasserstein Gradient-Flow Structure

**Source:** KS-5, KS-10.

The KS equation is the Wasserstein-2 gradient flow of F[u]:

    u_t = div(u nabla(delta F / delta u)) = div(u nabla(log u - v))

This is the same gradient-flow structure as FP and PME — the dynamics descend the free-energy landscape in the optimal-transport metric. The descent rate is:

    dF/dt = -integral u |nabla(log u - v)|^2 dx = -D(t) <= 0

where D(t) is the *dissipation rate* (the Fisher-type information with respect to the "effective potential" log u - v).

### N7. Critical Mass M_c = 8 pi (2D)

**Source:** KS-9.

The sharp threshold mass for the 2D parabolic–elliptic KS:

    M_c = 8 pi

Below M_c: the entropy term dominates the interaction term in F → F is bounded below → global existence.
Above M_c: the interaction term dominates → F is unbounded below → blowup.
At M_c: the logarithmic Hardy–Littlewood–Sobolev inequality is *saturated* — the critical case.

The value 8 pi is the *best constant in the log-HLS inequality*:

    integral integral u(x) log|x - y| u(y) dx dy <= (M / (4 pi)) integral u log u dx + C(M)

with equality at M = 8 pi for the optimal profile (a rescaled Cauchy distribution u_* = 8 pi lambda^2 / (lambda^2 + |x|^2)^2).

### N8. Global Existence for M < 8 pi

**Source:** KS-9, N5, N7.

For M < 8 pi: the free energy F is bounded below by the log-HLS inequality:

    F[u] >= (1 - M/(8 pi)) integral u log u dx + C(M) > -infinity

The bounded-below free energy + mass conservation + dissipation provides uniform-in-time bounds on integral u log u (and hence on the L^p norms of u for p > 1). The solution exists globally and converges to the unique stationary solution (a radially symmetric profile).

### N9. Blowup for M > 8 pi

**Source:** KS-8, KS-9.

For M > 8 pi: the free energy F is unbounded below. The dynamics descend the free-energy landscape toward -infinity, which requires the density u to concentrate at a point — forming a Dirac delta.

The blowup mechanism:
1. F[u] decreases monotonically (gradient flow).
2. F is unbounded below (interaction energy dominates entropy for M > 8 pi).
3. F → -infinity requires integral u v → +infinity, which requires u to concentrate.
4. Concentration → Dirac delta → ||u||_{L^{infinity}} → infinity → blowup.

The blowup is *driven by the free-energy descent*. The Lyapunov structure, which in FP/PME *prevents* singularity, in KS *drives* it — because the energy landscape has no floor.

### N10. Logarithmic Hardy–Littlewood–Sobolev Inequality

**Source:** KS-9, variational analysis.

The sharp inequality:

    (1/(4 pi)) integral integral u(x) log|x - y| u(y) dx dy <= (M/(8 pi)) integral u log u dx + C(M)

with equality iff u is a rescaled Cauchy distribution. This inequality is the *variational backbone* of the KS theory:
- It determines the critical mass (M_c = 8 pi).
- It bounds the free energy from below (for M < 8 pi).
- Its optimizer is the critical profile (the steady state at M = 8 pi).
- Its failure (for M > 8 pi) is the *algebraic cause* of blowup.

### Summary of Necessary Configurations

| Label | Necessary Configuration                     | Source               |
|-------|---------------------------------------------|----------------------|
| N1    | Non-negative density u >= 0                 | KS-1                 |
| N2    | Nonlocal chemoattractant v = (-Delta)^{-1} u| KS-2, KS-5, KS-7   |
| N3    | Diffusion Delta u (stabilizing)             | KS-3                 |
| N4    | Aggregation -div(u nabla v) (destabilizing) | KS-4, KS-7          |
| N5    | Free energy F = integral u log u - (1/2) integral u v | KS-5, KS-10 |
| N6    | Wasserstein gradient-flow structure          | KS-5, KS-10         |
| N7    | Critical mass M_c = 8 pi                    | KS-9                 |
| N8    | Global existence for M < 8 pi               | KS-9, N5, N7        |
| N9    | Blowup for M > 8 pi                         | KS-8, KS-9          |
| N10   | Log-HLS inequality (sharp constant)         | KS-9                 |

---

## 3. Envelope Inequalities (E1–E10)

---

**E1. Mass Conservation**

    integral u(x, t) dx = M    for all t in [0, T)

Exact identity. The total cell mass is preserved.

---

**E2. Free-Energy Dissipation**

    dF/dt = -integral u |nabla(log u - v)|^2 dx <= 0

Exact identity. The free energy F = integral u log u - (1/2) integral u v decreases monotonically. The dissipation rate is D(t) = integral u |nabla(log u - v)|^2 dx — a *nonlocal Fisher information* (the standard Fisher information involves nabla log u; the KS version involves nabla(log u - v), coupling the entropy gradient to the chemoattractant gradient).

---

**E3. Log-HLS Inequality (Sharp Constant 8 pi)**

    (1/(4 pi)) integral integral u(x) log|x - y| u(y) dx dy <= (M/(8 pi)) integral u log u dx + C(M)

The *sharp* inequality with best constant M/(8 pi). Equality holds for the Cauchy distribution at M = 8 pi. This inequality is the *variational foundation* of the entire KS theory — it is the single estimate from which both global existence (M < 8 pi) and blowup (M > 8 pi) follow.

---

**E4. Entropy–Potential Competition**

For M < 8 pi:

    F[u] = integral u log u - (1/2) integral u v >= (1 - M/(8 pi)) integral u log u + C(M) > -infinity

The entropy term integral u log u dominates the potential term (1/2) integral u v. The free energy is bounded below. This is the *subcritical energy bound* — the structural guarantee of global existence.

For M > 8 pi:

    inf_u F[u] = -infinity

The potential term dominates. The free energy has no lower bound. The dynamics can descend to -infinity in finite time — this is the *supercritical energy unboundedness* that drives blowup.

---

**E5. A Priori Bounds for M < 8 pi**

For M < 8 pi, the free-energy bound (E4) provides:

    integral u log u dx <= C(M, F[u_0])    for all t

which, combined with mass conservation and interpolation, gives:

    ||u(t)||_{L^p} <= C(p, M, F[u_0])    for all 1 < p < infinity, all t

Uniform-in-time L^p bounds. The solution remains bounded in every L^p space and exists globally.

---

**E6. Second-Moment Identity (Virial-Type)**

Define V(t) = integral |x|^2 u(x, t) dx (the second moment of the density). Then:

    dV/dt = 4M - M^2 / (2 pi) = 4M(1 - M/(8 pi))

This is *exact* for the parabolic–elliptic KS in R^2 with the Newtonian potential.

For M < 8 pi: dV/dt > 0 → V(t) increases → the density spreads → no concentration → no blowup.
For M = 8 pi: dV/dt = 0 → V(t) is constant → critical balance.
For M > 8 pi: dV/dt < 0 → V(t) decreases → the density concentrates → V reaches 0 in finite time → *blowup*.

The blowup time is bounded by:

    T* <= V(0) / |dV/dt| = V(0) / (M(M/(8 pi) - 1) * (8 pi / M)) = 2 pi V(0) / (M^2/(8 pi) - M)

The second-moment identity is the KS analogue of the NLS virial identity (which gives d^2V/dt^2 = 8H for the focusing NLS). Both provide *exact conditions for blowup* through the concavity of a variance-type quantity.

---

**E7. Blowup Criterion for M > 8 pi**

**Sufficient condition for blowup:**

    M > 8 pi    and    u_0 has finite second moment

Then T* < infinity: the solution blows up in finite time.

**Necessary condition for blowup (in 2D):**

    M >= 8 pi    (blowup requires at least critical mass)

For M < 8 pi: no blowup is possible (global existence guaranteed by E4 and E5).

The mass M = 8 pi is the *exact threshold*: the sharpest blowup/global-existence boundary in the Atlas for a nonlocal PDE.

---

**E8. Lower Bound on Blowup Rate**

Near the blowup time T*, the maximum of u satisfies:

    ||u(t)||_{L^{infinity}} >= C / (T* - t)

The blowup rate is *at least* 1/(T* - t) — the *self-similar* rate. The exact blowup rate depends on the blowup profile:

- *Type I (self-similar):* ||u(t)||_{L^{infinity}} ~ C / (T* - t). The density concentrates at the self-similar rate.
- *Type II (faster-than-self-similar):* ||u(t)||_{L^{infinity}} >> 1/(T* - t). The concentration is faster than self-similar.

The classification of blowup types (Type I vs. Type II) for the KS is an active area of research — partially resolved for radial data (Raphaël–Schweyer).

---

**E9. Global Existence in Subcritical Regime**

For M < 8 pi on R^2 (or M < 8 pi / |Omega| on bounded domains with appropriate normalization):

    u(t) in C([0, infinity); L^1 ∩ L^{infinity}(R^2))

Global smooth solutions exist for all time. The solution converges to the unique stationary state:

    u_eq(x) = M * exp(v_eq(x)) / integral exp(v_eq) dx

where v_eq solves the nonlinear elliptic equation -Delta v_eq = M exp(v_eq) / integral exp(v_eq) dx — a *mean-field equation* whose solution is a radially decreasing profile.

---

**E10. Concentration–Compactness Decomposition Near Blowup**

Near the blowup time T*, the density decomposes into:

    u(x, t) → M_0 delta(x - x_0) + u_residual(x, T*)

where:
- M_0 >= 8 pi is the concentrated mass (at least the critical mass concentrates at the blowup point).
- x_0 is the blowup location.
- u_residual is the residual density (smooth, with total mass M - M_0).

The decomposition is *quantized*: the concentrated mass is always at least 8 pi. This *mass quantization* is the KS analogue of the NLS mass quantization (the concentrated profile has mass at least M_*). It reflects the *critical mass being the minimum unit of concentration*.

After blowup, the evolution can be continued (in a measure-valued sense): the delta mass persists as a point mass, and the residual density continues to evolve. If M - M_0 < 8 pi, the residual solution is globally regular. If M - M_0 >= 8 pi, further concentration events can occur — producing a *cascade of blowup events*, each absorbing at least 8 pi of mass.

---

### Envelope Summary

**Tier 1 — Exact Identities (all KS):**
- E1: Mass conservation (integral u = M, exact).
- E2: Free-energy dissipation (dF/dt = -D <= 0, exact).
- E6: Second-moment identity (dV/dt = 4M(1 - M/(8 pi)), exact in 2D).

**Tier 2 — Variational Control (subcritical M < 8 pi):**
- E3: Log-HLS inequality (sharp constant 8 pi).
- E4: Entropy-potential competition (F bounded below for M < 8 pi).
- E5: A priori L^p bounds (uniform in time for M < 8 pi).
- E9: Global existence and convergence to steady state.

**Tier 3 — Blowup Structure (supercritical M > 8 pi):**
- E7: Blowup criterion (M > 8 pi → finite-time blowup).
- E8: Blowup rate lower bound (at least 1/(T* - t)).
- E10: Concentration-compactness (mass quantization at 8 pi).

### Closure Assessment

**M < 8 pi (subcritical):** The envelope is *fully closed*. The log-HLS inequality bounds the free energy from below, providing uniform L^p estimates for all time. The solution exists globally and converges to a steady state. No open faces.

**M = 8 pi (critical):** The envelope is *marginally closed*. Global existence holds (the critical mass does not blow up for most initial data), but the estimates are *borderline* — the free energy touches zero from above, and the second moment is constant.

**M > 8 pi (supercritical):** The envelope has an *open blowup face*. The free energy is unbounded below, the second moment decreases to zero in finite time, and the density concentrates into a Dirac delta. The blowup is well-characterized (rate, profile, mass quantization) but *certain* — it is a structural feature, not an open question.

The KS envelope is therefore *mass-bifurcated*:

    M < 8 pi:  Fully closed (global existence, steady state)
    M = 8 pi:  Marginally closed (critical, threshold)
    M > 8 pi:  Open blowup face (certain, well-characterized)

---

## 4. Central Architectural Finding

### 4.1 The KS Envelope: Mass-Controlled Bifurcation

The KS envelope is *entirely controlled by a single scalar invariant*: the total mass M. Every structural property — global existence, blowup, free-energy boundedness, steady-state convergence — is determined by the value of M relative to the threshold 8 pi.

This is the *sharpest bifurcation* of any nonlocal PDE in the Atlas:
- NS (3D): the bifurcation parameter (dimension d) is *discrete* and the threshold is *open* (regularity unresolved).
- TFE: the bifurcation parameter (exponent n) is *continuous* and the threshold is *sharp* (n = 1).
- NLS (focusing): the bifurcation parameter (mass M) is *continuous* and the threshold is *sharp* (M = M_*).
- **KS: the bifurcation parameter (mass M) is *continuous* and the threshold is *sharp* (M = 8 pi), with the *additional feature* that the threshold is the best constant of a fundamental functional inequality (log-HLS).**

The KS threshold M = 8 pi is the *most deeply characterized* threshold in the Atlas: it is simultaneously:
- The best constant in the log-HLS inequality.
- The boundary of free-energy boundedness.
- The mass of the critical steady state.
- The zero of the second-moment evolution rate dV/dt = 4M(1 - M/(8 pi)).
- The minimum unit of mass that can concentrate in blowup.

Five independent characterizations of the same threshold — more than any other architecture.

### 4.2 KS as the Aggregation Pole

The KS establishes the *fifth structural pole* of the Atlas:

| Pole         | Representative | Mechanism                    | Singularity Type       |
|-------------|----------------|------------------------------|------------------------|
| Diffusive   | FP/PME         | Smoothing → equilibrium      | None                   |
| Hyperbolic  | HJ/Burgers     | Steepening → shocks          | Gradient/velocity      |
| Dispersive  | NLS/KdV        | Oscillatory → solitons       | Amplitude (focusing)   |
| Geometric   | MCF            | Curvature → extinction       | Curvature              |
| **Aggregation** | **KS**     | **Nonlocal attraction → mass concentration** | **Density (delta)** |

The aggregation pole is *unique*: no other pole has nonlocal attraction as its primary mechanism, mass concentration as its singularity type, or a gradient-flow structure that *drives* (rather than prevents) the singularity. The KS is the *only architecture whose Lyapunov structure is complicit in the blowup*.

### 4.3 The Free-Energy Landscape as the Governing Object

The KS architecture demonstrates a principle that is new in the Atlas: *the free-energy landscape, not just the free-energy value, determines the dynamics*.

In FP/PME/AC/CH: the free energy F is bounded below → F decreases → solution converges to the minimum of F. The *value* of F controls the dynamics.

In KS: the free energy F may or may not be bounded below (depending on M). When F is bounded below (M < 8 pi), the dynamics converge to the minimum — the standard gradient-flow behavior. When F is *not* bounded below (M > 8 pi), the dynamics descend toward -infinity — the free-energy *landscape itself* has a hole, and the solution falls through it. The *topology of the landscape* (bounded vs. unbounded) controls the dynamics, not just the current value of F.

This landscape-topology principle is the KS's deepest structural contribution: it shows that *gradient-flow structure alone does not prevent singularity* — the *shape of the energy landscape* is what matters. The FP/PME energy landscapes are *convex and bounded below* (preventing singularity). The KS energy landscape is *non-convex and unbounded below for large mass* (permitting and driving singularity).

### 4.4 Envelope Comparison

| Architecture | Envelope Status         | Critical Threshold   | Blowup Type          | Driven By       |
|-------------|--------------------------|---------------------|----------------------|-----------------|
| FP          | Closed (all params)      | None                | None                 | N/A             |
| PME         | Closed (all m > 1)       | None                | None                 | N/A             |
| KdV         | Closed (integrable)      | None                | None                 | N/A             |
| HJ/Burgers  | Closed (entropy)        | None (shock always) | Gradient/velocity    | Transport       |
| MCF         | Closed + req. singularity| None (always extinct)| Curvature            | Area dissipation|
| NLS (foc.)  | Sharp threshold (d=2)   | M_* = \|\|Q\|\|^2  | Amplitude            | Self-focusing   |
| TFE         | n-dependent             | n = 1               | Positivity           | 4th-order + degen.|
| NS (3D)    | Open                     | Open                | Open                 | Open            |
| **KS (2D)** | **Mass-bifurcated**     | **M = 8 pi (exact)**| **Mass concentration**| **Free-energy landscape** |

---

*End of Mode 1: Axiom → Envelope. Mode 2 (PDE → Extremal Dynamics) will follow in a subsequent file.*
