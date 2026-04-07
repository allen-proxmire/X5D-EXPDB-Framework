# AD Evaluation: Keller–Segel System — Mode 2: PDE → Extremal Dynamics

Allen Proxmire

April 2026

---

## Overview

Mode 2 moves from the static envelope to the dynamics. The KS dynamical landscape is *uniquely governed by a single scalar*: the total mass M = integral u dx determines everything — whether the solution spreads or concentrates, whether it exists globally or blows up, whether the free energy converges to a finite minimum or diverges to -infinity. No other architecture in the Atlas has its *entire dynamical program* controlled by a single conserved scalar. The NS has multiple parameters (Re, forcing); the NLS has sign and dimension; the TFE has the exponent n. The KS has *one number*: M, compared to one threshold: 8 pi.

The KS dynamics also demonstrate a phenomenon unique in the Atlas: *Lyapunov-driven blowup*. In every other architecture with a Lyapunov functional (FP, PME, AC, CH, TFE), the Lyapunov descent leads to *equilibrium* — a global minimum of the free energy. In the KS, the Lyapunov descent can lead to *singularity* — the free energy plunges to -infinity, dragging the density into a Dirac delta. The gradient flow does not prevent the singularity; it *causes* it.

Throughout:

    u_t = Delta u - div(u nabla v),    -Delta v = u

on R^2, with u >= 0, integral u = M.

---

## 1. Fundamental Time and Length Scales

### 1.1 Two Competing Time Scales

**Diffusive time scale:** The time for diffusion to spread a density concentration of scale L:

    t_diff ~ L^2

Standard second-order parabolic scaling. The diffusion spreads the cells, reducing concentration gradients. Identical to the FP and heat-equation time scale.

**Aggregation time scale:** The time for the chemotactic drift to concentrate cells at scale L:

    t_agg ~ L^2 / M

The chemoattractant potential v = (-Delta)^{-1} u has magnitude ~ M (from the Poisson equation with source of total mass M), so nabla v ~ M/L. The chemotactic flux is u nabla v ~ u M/L, and the time to concentrate a density of order u over a region of size L is t ~ L/(nabla v) ~ L^2/M. The aggregation time scale *decreases with increasing mass* — more cells produce a stronger signal, which drives faster concentration.

### 1.2 The Mass as the Universal Control Parameter

The ratio of the two time scales:

    rho = t_diff / t_agg = M

The ratio is *exactly the mass M* (in appropriate units where the diffusion coefficient and chemotactic sensitivity are normalized to 1). This is the *simplest possible competition parameter*: a single conserved scalar that determines the entire dynamics.

**rho < 8 pi (diffusion-dominated, subcritical mass):**

Diffusion wins. The cells spread faster than chemotaxis can concentrate them. The solution exists globally and converges to a smooth steady state. The free energy F is bounded below and decreases toward the unique minimizer.

This regime is the KS analogue of:
- FP with confining drift: diffusion + drift → Gibbs–Boltzmann equilibrium.
- PME: diffusion → Barenblatt self-similar spreading.
- AC: diffusion + reaction → phase selection and equilibrium.

The subcritical KS dynamics are *qualitatively diffusive* — the aggregation is a perturbation that modifies the equilibrium shape but does not change the qualitative behavior (global existence, steady-state convergence).

**rho = 8 pi (critical mass):**

The diffusion and aggregation are *exactly balanced*. The free energy F approaches 0 from above but never crosses. The second moment V(t) = integral |x|^2 u dx is constant (dV/dt = 0). The density evolves toward the *critical steady state* — a rescaled Cauchy distribution u_* = 8 pi lambda^2 / (lambda^2 + |x|^2)^2 — but the convergence may be slow (algebraic, not exponential).

The critical mass is the KS analogue of:
- NLS M_*: the ground-state soliton mass separating global from blowup.
- MCF: the extinction time T* where area → 0.

**rho > 8 pi (aggregation-dominated, supercritical mass):**

Aggregation wins. The chemotactic drift concentrates cells faster than diffusion can spread them. The free energy F → -infinity in finite time. The density u forms a Dirac delta at a single point (or multiple points). The blowup is *certain* and *driven by the Lyapunov descent*.

This regime has no analogue in any other gradient-flow architecture — FP, PME, AC, CH, and TFE all have bounded-below free energies and never blow up. The KS supercritical regime is the *only gradient-flow blowup* in the Atlas.

### 1.3 The Remarkable Simplicity

The KS competition parameter rho = M is:
- *Conserved* (M is an exact invariant).
- *Scalar* (one number, not a function or a vector).
- *Dimensionless* (in appropriate units).
- *Sharp* (the threshold 8 pi is exact, not approximate).

No other architecture has its dynamics controlled by such a simple parameter:
- NS: Re = UL/nu (depends on the solution, not conserved, not a sharp threshold).
- NLS: M = ||psi||_{L^2}^2 (conserved and sharp threshold, but the blowup also depends on energy H and variance V).
- TFE: n (constitutive, not conserved, continuous threshold).
- **KS: M (conserved, sharp threshold 8 pi, determines *everything*).**

---

## 2. Extremal Behaviors

### E1. Diffusive Spreading (Subcritical Mass, M < 8 pi)

For M < 8 pi, the solution spreads and converges to a smooth steady state:

    u(x, t) → u_eq(x)    as t → infinity

where u_eq is the unique minimizer of F[u] subject to integral u = M. The steady state u_eq is:
- Radially symmetric (for radial initial data; otherwise, after a transient).
- Smooth and bounded.
- Exponentially decaying at infinity.
- Determined by the nonlinear elliptic equation: u_eq = M exp(v_eq) / integral exp(v_eq), -Delta v_eq = u_eq.

The convergence is:
- Exponential for M << 8 pi (the free energy has a strong spectral gap at the minimizer).
- Algebraic as M → 8 pi (the spectral gap closes at the critical mass).

### E2. Aggregation-Driven Concentration (Supercritical Mass, M > 8 pi)

For M > 8 pi, the density concentrates at one or more points. The concentration mechanism:

1. The free energy F decreases (gradient-flow structure).
2. For M > 8 pi, F is unbounded below (the interaction energy dominates the entropy).
3. F → -infinity requires integral u v → +infinity, which requires u to concentrate.
4. The concentration is *self-reinforcing*: more concentration → stronger signal → faster drift → more concentration.

The concentration produces a profile that, near the blowup point x_0, looks like:

    u(x, t) ~ (1/lambda(t)^2) U_*((x - x_0)/lambda(t))

where lambda(t) → 0 as t → T*, and U_* is a universal profile (related to the Cauchy distribution).

### E3. Finite-Time Blowup (Mass → Dirac Delta)

At the blowup time T*:

    u(x, T*-) contains a component M_0 delta(x - x_0)

where M_0 >= 8 pi is the concentrated mass. The blowup is:
- *Finite-time:* T* < infinity (the second-moment identity gives T* <= V(0) / (4M(M/(8pi) - 1))).
- *Point-concentration:* The density becomes infinite at a single point x_0.
- *Delta-type:* The concentrated mass forms a genuine Dirac measure.
- *Irreversible:* The blowup cannot be reversed (the free energy has descended past the point of no return).

**Comparison with other blowup types:**

| Architecture | Blowup Type                | What Diverges        | What Concentrates    |
|-------------|----------------------------|----------------------|----------------------|
| NS (3D)    | Open (vorticity?)           | ||nabla u||?         | Vorticity?           |
| NLS (foc.) | Amplitude concentration     | ||nabla psi||        | |psi|^2              |
| HJ/Burgers | Gradient steepening         | ||D^2 u|| or ||u_x|| | Gradient             |
| MCF         | Curvature blowup           | ||A||                | Curvature            |
| **KS**      | **Mass concentration**     | **||u||_{L^inf}**    | **u itself (density)**|

The KS blowup is the *most physical*: the directly observable quantity (cell density) concentrates into a point mass. Every other blowup type concentrates a *derivative* of the observable (gradient, curvature, vorticity) rather than the observable itself.

### E4. Mass Quantization at Blowup

The concentrated mass at each blowup point satisfies:

    M_0 >= 8 pi    (minimum concentration quantum)

The mass 8 pi is the *smallest amount of mass that can concentrate* — it is the "quantum of concentration" for the KS system. If M = 8 pi + epsilon (slightly supercritical), *all* of the mass concentrates at one point (no residual). If M = 16 pi + epsilon, *two* blowup points can form, each absorbing at least 8 pi.

The mass quantization 8 pi parallels:
- NLS mass quantization M_* = ||Q||_{L^2}^2 (the minimum mass of a collapsing NLS solution).
- MCF genus quantization (topology simplifies by integer steps at singularities).
- ED prime quantization (the smallest "unit" of multiplicative structure is a single prime).

### E5. Multi-Center Aggregation

For large M (M >> 8 pi), the blowup can occur at *multiple points simultaneously*:

    u(x, T*) → sum_{j=1}^N M_j delta(x - x_j) + u_residual

where each M_j >= 8 pi and sum M_j + integral u_residual = M. The number of blowup points satisfies N <= M / (8 pi) (each absorbs at least 8 pi).

Multi-center blowup is the KS analogue of:
- Burgers multi-shock formation (multiple shocks from initial data with multiple decreasing regions).
- MCF multi-pinch (multiple neckpinches in a complex surface).

### E6. Global Existence + Convergence (M < 8 pi)

For M < 8 pi, the solution converges to the unique steady state:

    ||u(t) - u_eq||_{L^p} → 0    as t → infinity    for all p in [1, infinity)

The convergence rate is *exponential* for M << 8 pi (spectral gap of the linearized operator) and *algebraic* for M approaching 8 pi (gap closing).

### E7. Critical Mass Dynamics (M = 8 pi)

At the critical mass M = 8 pi, the dynamics are *borderline*:
- Global existence holds for most initial data.
- The solution converges to a steady state, but *slowly* (algebraic, not exponential).
- The second moment V(t) is constant (dV/dt = 0).
- The free energy F(t) → 0 from above.
- The critical steady state is the *optimizer* of the log-HLS inequality — the Cauchy profile.

### E8. Post-Blowup Continuation

After the blowup at T*, the evolution can be continued in a *measure-valued* sense:

    u(t) = u_regular(t) + sum_j M_j(t) delta(x - x_j(t))

where:
- u_regular is the smooth (non-concentrated) part of the density.
- The delta masses M_j persist and can *move* (drift according to the chemoattractant gradient).
- If the residual mass integral u_regular < 8 pi, no further blowup occurs.
- If the residual mass >= 8 pi, further concentration events are possible — a *blowup cascade*.

The post-blowup continuation is the KS analogue of:
- HJ/Burgers entropy solutions (continuation past shocks via weak solutions).
- MCF surgery (continuation past curvature singularities via surgery + level-set).

But the KS post-blowup is *less well-developed* theoretically than the HJ/Burgers or MCF continuations — the measure-valued framework is still an active area of research.

---

## 3. Universal Inequalities

---

**U1. Mass Conservation**

    integral u(x, t) dx = M    for all t in [0, T)

Exact identity.

---

**U2. Free-Energy Dissipation**

    dF/dt = -integral u |nabla(log u - v)|^2 dx <= 0

Exact identity. The free energy F = integral u log u - (1/2) integral u v decreases monotonically. The dissipation rate is a *nonlocal Fisher information* — the squared gradient of the effective potential log u - v, weighted by u.

---

**U3. Log-HLS Inequality (Sharp Constant)**

    (1/(4 pi)) integral integral u(x) log|x-y| u(y) dx dy <= (M/(8 pi)) integral u log u dx + C(M)

Sharp constant M/(8 pi). Equality for the Cauchy distribution at M = 8 pi. The *variational backbone* of the KS theory — determines the critical mass and the free-energy boundedness.

---

**U4. Second-Moment Identity**

    dV/dt = 4M(1 - M/(8 pi))    where V(t) = integral |x|^2 u dx

Exact for the parabolic–elliptic KS in R^2. The *virial identity* of the KS:
- M < 8 pi: V increases → spreading → no blowup.
- M = 8 pi: V constant → critical balance.
- M > 8 pi: V decreases → V → 0 in finite time → blowup.

Blowup time bound: T* <= V(0) / (4M(M/(8 pi) - 1)).

---

**U5. A Priori Bounds (M < 8 pi)**

For M < 8 pi:

    integral u(t) log u(t) dx <= C(M, F[u_0])    for all t

Uniform-in-time entropy bound → uniform L^p bounds for all p > 1 → global smooth solution.

---

**U6. Blowup Criterion (M > 8 pi)**

    M > 8 pi and V(0) < infinity    =>    T* < infinity (finite-time blowup)

The criterion is *sufficient and, in a sharp sense, necessary*: M > 8 pi is required for blowup, and finite second moment ensures the blowup happens in finite time (rather than infinite time).

---

**U7. Lower Bound on Blowup Rate**

    ||u(t)||_{L^{infinity}} >= C / (T* - t)    as t → T*

The blowup rate is at least 1/(T* - t) — the self-similar rate. The actual rate depends on the blowup type:
- Type I: ||u||_{L^inf} ~ C/(T* - t). Self-similar.
- Type II: ||u||_{L^inf} >> 1/(T* - t). Faster than self-similar.

---

**U8. Concentration–Compactness Near Blowup**

Near the blowup time T*, the density decomposes:

    u(t) → M_0 delta(x - x_0) + u_residual    weakly as t → T*

where M_0 >= 8 pi and u_residual is smooth with integral u_residual = M - M_0.

---

**U9. Mass Quantization**

    M_0 >= 8 pi    at each blowup point

The minimum quantum of concentrated mass is 8 pi. Multiple blowup points each absorb at least 8 pi. The total number of blowup points is at most M / (8 pi).

---

**U10. Global Existence (Subcritical Regime)**

    M < 8 pi    =>    u(t) exists globally and converges to the unique steady state u_eq

Unconditional for M < 8 pi. The solution remains smooth, bounded, and positive for all time.

---

### Universal Inequality Summary

| Label | Inequality                        | Type            | Status              | Role                        |
|-------|-----------------------------------|-----------------|---------------------|-----------------------------|
| U1    | Mass conservation                 | Exact identity  | All KS              | Primary invariant           |
| U2    | Free-energy dissipation           | Exact identity  | All KS              | Lyapunov structure          |
| U3    | Log-HLS inequality                | Sharp bound     | All KS              | Variational backbone        |
| U4    | Second-moment identity            | Exact identity  | R^2, P-E model     | Virial/blowup criterion    |
| U5    | A priori bounds (M < 8pi)        | Bound           | Subcritical          | Global control              |
| U6    | Blowup criterion (M > 8pi)       | Criterion       | Supercritical        | Singularity condition       |
| U7    | Blowup rate lower bound          | Lower bound     | Supercritical        | Rate control                |
| U8    | Concentration-compactness         | Decomposition   | Near blowup          | Profile characterization    |
| U9    | Mass quantization at 8 pi        | Quantization    | At blowup            | Minimum concentration unit  |
| U10   | Global existence (M < 8pi)       | Existence       | Subcritical          | Complete well-posedness     |

---

## 4. Attractors and Long-Time Behavior

### 4.1 Three Mass Regimes, Three Fates

**M < 8 pi: Steady-State Attractor**

Every solution converges to the unique radially symmetric steady state u_eq. The attractor is a *single point* in the function space — a fixed-point attractor. The convergence is exponential (for M << 8 pi) or algebraic (for M near 8 pi).

The subcritical KS attractor is structurally identical to:
- FP with confining potential: single Gibbs–Boltzmann equilibrium.
- PME: single Barenblatt profile.
- AC: uniform phase ±1.

**M = 8 pi: Critical Manifold**

The dynamics converge (slowly) to the critical steady state — the Cauchy profile u_* = 8 pi lambda^2 / (lambda^2 + |x|^2)^2. The attractor is a *one-parameter family* indexed by the scale lambda > 0 (and the center, if not fixed). The convergence is *algebraic* (slow).

**M > 8 pi: Blowup (No Classical Attractor)**

The solution blows up in finite time. There is no classical attractor — the dynamics terminate in a singularity. The "attractor" in the measure-valued sense is a *Dirac delta* (or sum of deltas) — the simplest possible measure.

### 4.2 The Mass-Bifurcated Attractor Structure

The KS is the *only architecture in the Atlas with a mass-bifurcated attractor*:

| Mass Regime    | Attractor                    | Type              |
|----------------|------------------------------|-------------------|
| M < 8 pi       | Smooth steady state u_eq     | Fixed point       |
| M = 8 pi       | Critical Cauchy profile      | Manifold          |
| M > 8 pi       | Dirac delta (blowup)         | Measure-valued    |

No other architecture has three qualitatively different attractor types controlled by a single conserved scalar:
- FP/PME/AC/CH/TFE: single attractor type (equilibrium/self-similar).
- HJ/Burgers: single regime (shock → N-wave).
- NLS: two regimes (defocusing → scattering; focusing → soliton/blowup) controlled by sign + dimension.
- KdV: single regime (soliton resolution).
- MCF: single regime (extinction).
- **KS: three regimes (steady state / critical / blowup) controlled by M vs. 8 pi.**

### 4.3 Comparison of Long-Time Behavior

| Architecture | Long-Time Behavior                    | Controlled By       | Attractor Type        |
|-------------|---------------------------------------|----------------------|-----------------------|
| **KS (M<8pi)** | **Convergence to steady state**   | **Mass M**          | **Fixed point**       |
| **KS (M>8pi)** | **Finite-time blowup → delta**   | **Mass M**          | **Dirac measure**     |
| FP          | Convergence to Gibbs–Boltzmann        | Drift potential V   | Fixed point           |
| PME         | Self-similar spreading (Barenblatt)   | Total mass M        | Self-similar          |
| KdV         | Soliton resolution                    | Scattering data     | Solitons + radiation  |
| NLS (def.)  | Scattering to linear flow             | Mass + energy       | Free Schrödinger     |
| NLS (foc.)  | Blowup (d >= 2) or soliton (d = 1)  | Mass M, sign, d     | Soliton / collapse   |
| HJ/Burgers  | Shock decay / N-wave                 | Initial data        | Entropy solution      |
| MCF         | Extinction (round sphere)             | Area                | Point (extinct)       |
| NS (2D)    | Compact attractor                     | Grashof number      | Unknown structure     |

---

## 5. Comparison with FP, PME, HJ, Burgers, NLS, KdV, NS, MCF, AC/CH, TFE, RD, and ED

### 5.1 KS as the Nonlocal Aggregation Pole

The KS introduces the *fifth structural pole* — aggregation — to the Atlas:

| Pole         | Mechanism                    | Singularity          | Nonlocal? |
|-------------|------------------------------|----------------------|-----------|
| Diffusive   | Smoothing                    | None                 | No*       |
| Hyperbolic  | Steepening                   | Shock/kink           | No        |
| Dispersive  | Oscillatory spreading        | Amplitude collapse   | No        |
| Geometric   | Curvature flow               | Curvature blowup     | No        |
| **Aggregation** | **Nonlocal self-attraction** | **Mass concentration** | **Yes** |

*NS has a nonlocal pressure channel but is primarily transport-driven. KS has nonlocal aggregation as the *primary* mechanism.

### 5.2 KS vs. NS: Opposite Nonlocal Roles

The KS and NS are the *only two nonlocal architectures* in the Atlas. Their nonlocal channels have *opposite dynamical roles*:

| Feature                    | KS                           | NS                          |
|----------------------------|------------------------------|-----------------------------|
| Nonlocal equation          | -Delta v = u                 | Delta p = source            |
| Nonlocal field role        | **Drives aggregation**       | **Enforces incompressibility** |
| Effect on density          | **Concentrates**             | **Prevents concentration**   |
| Blowup mechanism           | Mass concentration (delta)   | Vorticity blowup (open)     |
| Critical threshold          | 8 pi (exact, sharp)         | Open (unresolved)            |
| Free-energy structure      | **Drives blowup**           | N/A (no free energy for NS)  |

The KS and NS nonlocal channels are *structural duals*: the KS potential *attracts* (concentrates density), while the NS pressure *repels* (prevents concentration). If one imagines "flipping the sign" of the nonlocal interaction from repulsive to attractive, the NS pressure becomes the KS chemoattractant. This sign flip is the *structural transformation from incompressible fluid to chemotactic aggregation*.

### 5.3 KS vs. NLS: Two Concentration Architectures

The KS and the focusing NLS are the *two concentration architectures* in the Atlas — both produce blowup through self-focusing concentration. The structural comparison:

| Feature                    | KS                           | NLS (focusing)               |
|----------------------------|------------------------------|------------------------------|
| Concentration mechanism    | **Nonlocal** self-attraction | **Local** self-focusing       |
| Critical threshold (2D)    | M = 8 pi                    | M = M_* = ||Q||_{L^2}^2     |
| Blowup type                | Density delta                | Gradient blowup              |
| Mass at blowup point       | >= 8 pi (quantized)         | >= M_* (quantized)           |
| Free-energy structure      | F → -infinity (drives blowup)| H conserved (does not drive) |
| Gradient-flow structure    | **Yes** (Wasserstein)        | No (Hamiltonian)             |
| Reversibility              | No (irreversible)            | Yes (reversible)             |

Both architectures have *mass-threshold blowup* with *quantized concentration mass*. But the mechanisms are *opposite*: the KS blowup is driven by a *decreasing free energy* (irreversible), while the NLS blowup is driven by a *conserved energy* (reversible). The KS *descends* to blowup; the NLS *oscillates* into blowup. The KS free energy *causes* the singularity; the NLS energy merely *permits* it.

### 5.4 KS vs. PME/FP: Gradient Flow With and Without Blowup

The KS, PME, and FP are all *Wasserstein gradient flows*:

| Architecture | Free Energy F                    | Bounded Below? | Blowup? | Attractor       |
|-------------|----------------------------------|----------------|---------|-----------------|
| FP          | integral rho V + sigma^2 integral rho log rho | Yes     | No      | Gibbs–Boltzmann |
| PME         | integral u^m / (m-1)             | Yes            | No      | Barenblatt      |
| **KS**      | **integral u log u - (1/2) integral u v** | **M < 8pi: Yes; M > 8pi: No** | **M > 8pi: Yes** | **Steady state / delta** |

The KS demonstrates that *gradient-flow structure does not prevent blowup* — what matters is whether the free energy is *bounded below*. The FP and PME free energies are bounded below (convex, or at least coercive) → global existence. The KS free energy is bounded below only for M < 8 pi → global existence in the subcritical regime but blowup in the supercritical.

### 5.5 KS and ED: Concentration as Structural Event

The KS mass concentration — a finite amount of density collapsing to a point — is the dynamical analogue of the ED *activation event*: at each prime p^2, the coverage structure concentrates at a specific arithmetic location. Both represent *density concentration at a distinguished point*:

- ED: coverage activates at p^2 → the sieve concentrates its action at a discrete set of points.
- KS: cell mass concentrates at x_0 → the density collapses to a delta at a distinguished spatial point.

Both processes involve *self-reinforcing concentration* driven by *nonlocal interaction*: in ED, the multiplicative structure of Z creates nonlocal correlations between coverage at different primes; in KS, the chemoattractant creates nonlocal attraction between cells at different locations.

### 5.6 Summary Table

| Feature                    | KS               | NS       | NLS      | FP       | PME      | KdV      | Burgers  | MCF      |
|----------------------------|------------------|----------|----------|----------|----------|----------|----------|----------|
| Nonlocal channels          | **2**            | 1        | 0        | 0        | 0        | 0        | 0        | 0        |
| Nonlocality role           | **Aggregation**  | Constraint| N/A     | N/A      | N/A      | N/A      | N/A      | N/A      |
| Blowup type                | **Mass delta**   | Open     | Amplitude| None     | None     | None     | Gradient | Curvature|
| Critical threshold         | **M=8pi (exact)**| Open     | M_*      | N/A      | N/A      | N/A      | N/A      | N/A      |
| Gradient flow              | **Wasserstein**  | No       | No       | Wass.    | Wass.    | No       | No       | L^2      |
| F bounded below            | **M-dependent**  | N/A      | Indef.   | Yes      | Yes      | N/A      | N/A      | Yes      |
| Lyapunov drives blowup     | **Yes (M>8pi)**  | No       | No       | No       | No       | No       | No       | No       |
| Mass quantization          | **8pi**          | N/A      | M_*      | N/A      | N/A      | N/A      | N/A      | N/A      |
| Conservation laws          | 1 (mass)         | 2        | 3        | 1        | 1        | Infinite | 1        | 0        |
| Parameters                 | 1 (chi)          | 2        | 1(sign)  | 2        | 1(m)     | 0        | 0        | 0        |

KS is the *unique nonlocal-aggregating, mass-concentrating, Lyapunov-driven-blowup, mass-quantized, gradient-flow* architecture in the Atlas. It is structurally orthogonal to every other architecture: no other PDE has nonlocal self-attraction driving a gradient flow to mass-concentrating blowup past a sharp threshold.

---

*End of Mode 2: PDE → Extremal Dynamics. Mode 3 (Channels → Constraint Surface) will follow in a subsequent file.*
