# AD Evaluation: Fokker–Planck Equation — Mode 1: Axiom → Envelope

Allen Proxmire

April 2026

---

## Overview

Mode 1 traces the path from the FP axioms (FP-1 through FP-8) to the architectural envelope. The FP envelope is *fully closed* and qualitatively different from every other envelope in the PDE Atlas. Its closure arises not from nonlinear structural mechanisms (maximum principle, degenerate diffusion, fourth-order smoothing) but from a simpler and more fundamental property: *linearity*. The FP equation is linear in rho, and linear parabolic equations have complete, unconditional well-posedness theories. The FP envelope is sealed by the *linearity itself* — the most structurally economical closure mechanism in the Atlas.

Throughout:

    partial_t rho = -div(b rho) + div(D nabla rho),    rho >= 0,    integral rho dx = 1

on Omega subset R^d with no-flux boundary conditions and prescribed drift b(x) and diffusion D(x) (positive definite).

---

## 1. Forbidden Configurations

### F1. Negative Probability (Normalization Violation)

**Axiom source:** FP-1 (Probability Density), FP-4 (Conservation).

The total probability is exactly 1 at all times:

    integral rho(x, t) dx = 1    for all t >= 0

Negative total probability (integral rho < 0), super-unit probability (integral rho > 1), or any violation of the normalization constraint is forbidden. The divergence form of the PDE, combined with no-flux boundary conditions, preserves the integral of rho exactly. This is stronger than the mass conservation of PME/CH/TFE (which preserves integral u = M for arbitrary M > 0): FP preserves not just the total but its specific value 1.

Moreover, rho >= 0 pointwise is preserved by the PDE (see N4 below). Negative probability densities are forbidden — rho(x, t) < 0 at any point is axiomatically impossible for non-negative initial data.

### F2. Reaction Terms (Probability Creation/Destruction)

**Axiom source:** FP-7 (No Reaction).

The FP equation has no source or sink terms. Probability is neither created nor destroyed — it is only transported (by drift) and spread (by diffusion). Adding a reaction term R(rho) would break the probability interpretation: it would create or destroy probability mass, violating the normalization constraint.

Formally, the FP right-hand side is a pure divergence:

    partial_t rho = -div(**J**)

Any non-divergence contribution (a reaction term that is not a divergence of a flux) would violate conservation. Reaction terms are structurally forbidden.

### F3. Nonlocal Diffusion

**Axiom source:** FP-2 (Locality).

The diffusion operator div(D nabla rho) is local — it involves rho and its derivatives at each point. Nonlocal diffusion (fractional Laplacians, Levy-process-generated operators, integral kernels) is outside the standard FP architecture. The corresponding stochastic processes (Levy flights, jump processes) have different FP-type equations (fractional FP, integro-differential equations) that are different architectures.

### F4. Non-Conservative Drift

**Axiom source:** FP-4 (Conservation), FP-3 (Drift–Diffusion Structure).

The drift channel -div(b rho) is automatically in divergence form, preserving integral rho. A drift term of the form b . nabla rho (without the divergence structure) would not preserve mass in general. The FP architecture requires the drift to enter as -div(b rho), not as b . nabla rho. (The two differ by -(div b) rho, which is a zeroth-order term that creates/destroys probability unless div b = 0.)

More precisely: the FP drift preserves total probability *for any drift field b*, because -div(b rho) is a divergence. No structural condition on b is needed for conservation — the conservation is *built into the form* of the PDE, not dependent on the specific drift.

### F5. Finite-Time Blowup

**Axiom source:** FP-3 (Drift–Diffusion), FP-8 (prescribed b and D), linearity.

The FP equation is *linear* in rho with prescribed (rho-independent) coefficients b and D. Linear parabolic equations with smooth, bounded coefficients have global-in-time smooth solutions for all smooth initial data. There is no mechanism for blowup:

- The diffusion channel is stabilizing (damps all modes).
- The drift channel is linear (cannot amplify rho faster than exponentially in regions where div b < 0, but such growth is bounded by the Gronwall inequality).
- The L^1 norm (integral rho = 1) is conserved.
- The maximum principle for linear parabolic equations provides L^{infinity} control.

Blowup requires a *nonlinear amplification mechanism* — and the FP equation has none. The linearity is the structural reason blowup is impossible.

### F6. Oscillations and Chaos (in the Gradient-Drift Case)

**Axiom source:** FP-3, FP-8, linearity.

For the gradient FP equation (b = -nabla V), the free energy F[rho] = integral rho V dx + sigma^2 integral rho log rho dx is a strict Lyapunov functional (dF/dt <= 0). This rules out limit cycles, sustained oscillations, and chaos. The dynamics are monotonically dissipative: rho descends the free-energy landscape toward the unique Gibbs–Boltzmann equilibrium.

For *non-gradient* drift, the situation is more subtle. The probability density rho can exhibit *apparent rotation* (the mass of rho circulates around a limit cycle of the drift field b). However, this rotation is *not* a nonlinear oscillation — it is a linear transport phenomenon. The density rho does not oscillate in any norm; it merely circulates spatially. The L^2 or entropy distance to any fixed reference state may not decrease monotonically, but there is no sensitive dependence on initial conditions (the PDE is linear) and no chaotic attractor. The "oscillation" is deterministic linear rotation, not nonlinear dynamics.

### F7. Nonlinear Self-Advection

**Axiom source:** FP-8 (prescribed b, D).

The drift field b(x) does not depend on rho. There is no self-advection term rho . nabla rho or u . nabla u as in NS. The linearity of the drift channel is a structural commitment: the particles do not interact with each other through the density. Each particle follows the prescribed drift independently, and their collective behavior (rho) is the superposition.

Self-advection (density-dependent drift, b = b[rho]) would produce a *nonlinear* FP equation (the McKean–Vlasov equation or mean-field PDE), which is a different architecture outside the standard FP class.

### F8. Degenerate Diffusion (Standard FP)

**Axiom source:** FP-3 (Drift–Diffusion), FP-8 (D positive definite).

The standard FP architecture requires D(x) to be positive definite at every point. Degenerate diffusion (D with zero eigenvalues at some points, as in the PME or TFE) is outside the standard FP. When D degenerates, the FP equation becomes *hypoelliptic* rather than *elliptic*, and the regularity theory changes qualitatively. Degenerate FP equations (Kramers equation, kinetic FP) exist but are specialized sub-architectures.

The positive definiteness of D ensures uniform parabolicity: the FP equation is uniformly parabolic everywhere in the domain, with no frozen regions and no free boundaries.

### F9. Finite-Speed Propagation

**Axiom source:** FP-3 (non-degenerate diffusion).

The non-degenerate diffusion channel div(D nabla rho) has *infinite propagation speed*: a point perturbation of rho at x = 0, t = 0 is felt everywhere instantaneously (with exponentially small amplitude at large distances). The Gaussian heat kernel has support on all of R^d for any t > 0.

Finite-speed propagation (compact support preservation, free boundaries) requires *degenerate* diffusion (D → 0 at rho = 0 or at certain spatial locations). Since the standard FP has non-degenerate D, finite-speed propagation is forbidden. The probability density rho(x, t) > 0 for all x in Omega and all t > 0, regardless of the initial data's support.

### F10. Pattern Formation

**Axiom source:** FP-7 (No Reaction), FP-3 (Drift–Diffusion), linearity.

The FP equation cannot form spatial patterns:

- No Turing instability (requires n >= 2 species + reaction coupling).
- No reaction-driven patterning (no reaction channel).
- No nonlinear instability (the PDE is linear).
- No symmetry-breaking (the linear drift–diffusion cannot amplify spatially heterogeneous perturbations selectively — the diffusion channel damps *all* non-constant modes).

The only spatial structure in FP solutions is inherited from the drift field b(x) and the initial data — it is not self-generated. The equilibrium rho_eq(x) = Z^{-1} exp(-V/sigma^2) has spatial structure (concentrated near the minima of V), but this structure is *prescribed by the potential*, not generated by the dynamics.

### Summary of Forbidden Configurations

| Label | Forbidden Configuration              | Excluding Axiom(s)      |
|-------|--------------------------------------|-------------------------|
| F1    | Negative probability / normalization violation | FP-1, FP-4    |
| F2    | Reaction terms                       | FP-7                    |
| F3    | Nonlocal diffusion                   | FP-2                    |
| F4    | Non-conservative drift               | FP-4, FP-3              |
| F5    | Finite-time blowup                   | FP-3, FP-8, linearity   |
| F6    | Oscillations / chaos (gradient drift)| FP-3, FP-8, Lyapunov    |
| F7    | Nonlinear self-advection             | FP-8                    |
| F8    | Degenerate diffusion                 | FP-3, FP-8              |
| F9    | Finite-speed propagation             | FP-3 (non-degen. D)     |
| F10   | Pattern formation                    | FP-7, linearity         |

---

## 2. Necessary Configurations

### N1. Drift–Diffusion Decomposition

**Source:** FP-3.

Every FP evolution decomposes into a first-order drift contribution and a second-order diffusion contribution:

    partial_t rho = [-div(b rho)] + [div(D nabla rho)]
                    = T(rho) + D(rho)

This decomposition is *structural* — the two channels are always present and always separable. The drift channel transports probability; the diffusion channel spreads it. No FP evolution can avoid this two-channel structure.

### N2. Linear Parabolicity

**Source:** FP-3, FP-8.

The FP equation is a *linear* second-order parabolic PDE:

    partial_t rho = sum_i b_i(x) partial_i rho + [sum_i partial_i b_i(x)] rho + sum_{ij} D_{ij}(x) partial_i partial_j rho + lower-order terms

All coefficients (b_i, D_{ij}) are prescribed functions of x alone — they do not depend on rho. This linearity is a *necessary consequence* of the stochastic interpretation: the Markov property of the underlying SDE implies that the evolution of the probability density is linear (the superposition principle holds).

### N3. Mass Conservation (Probability Normalization)

**Source:** FP-4.

    integral rho(x, t) dx = 1    for all t >= 0

Exact conservation of total probability. Follows from the divergence form of the PDE and no-flux boundary conditions.

### N4. Positivity Preservation

**Source:** FP-1, FP-3 (maximum principle for linear parabolic equations).

If rho_0(x) >= 0, then rho(x, t) >= 0 for all x and all t > 0. The linear parabolic maximum principle guarantees that the minimum of rho is non-decreasing if the equation has no negative zeroth-order terms that could drive rho below zero. For the FP equation in conservation form, the comparison with the zero sub-solution gives positivity.

More precisely: the FP equation preserves the cone of non-negative functions. Combined with N3, this means rho(t) is a *probability density* for all t > 0 — non-negative and normalized.

### N5. Infinite-Speed Propagation

**Source:** FP-3, FP-8 (non-degenerate D).

For D positive definite, the fundamental solution of the FP equation is strictly positive for all (x, t) with t > 0. If rho_0 has compact support, then rho(t) > 0 everywhere for t > 0. Information propagates at infinite speed — every point feels the initial data instantaneously.

This is the *opposite* of the PME/TFE property (finite-speed propagation). The FP architecture has no free boundaries and no compact support preservation.

### N6. Gaussian Smoothing at Small Scales

**Source:** FP-3 (diffusion channel).

At small scales (high wavenumbers), the diffusion channel dominates the drift:

    |diffusion rate| / |drift rate| = D k^2 / (|b| k) = D k / |b| → infinity as k → infinity

The FP equation smooths at the *Gaussian rate* — mode k is damped at rate D k^2. At sufficiently small scales, the FP dynamics are indistinguishable from the heat equation. This Gaussian smoothing is instantaneous: rho becomes C^{infinity} for any t > 0, regardless of the initial data's regularity.

### N7. Exponential Convergence to Equilibrium (Confining Gradient Drift)

**Source:** FP-3, FP-8, gradient-flow structure.

For b = -nabla V with V confining (V(x) → infinity as |x| → infinity), the FP equation has a unique equilibrium:

    rho_eq = Z^{-1} exp(-V / sigma^2)

and every solution converges exponentially:

    ||rho(t) - rho_eq||_{L^2(rho_eq^{-1})} <= C exp(-lambda t) ||rho_0 - rho_eq||_{L^2(rho_eq^{-1})}

where lambda > 0 is the *spectral gap* of the FP operator (the smallest nonzero eigenvalue of the generator -div(b .) + div(D nabla .)). The spectral gap is determined by the potential V and the diffusion sigma^2.

### N8. Gibbs–Boltzmann Equilibrium (Gradient Drift)

**Source:** FP-3, FP-8 (b = -nabla V).

The unique stationary solution of the gradient FP equation is:

    rho_eq(x) = Z^{-1} exp(-V(x) / sigma^2),    Z = integral exp(-V / sigma^2) dx

This is the *Gibbs–Boltzmann distribution* — the central object of equilibrium statistical mechanics. It is the global minimizer of the free energy F[rho] = integral rho V dx + sigma^2 integral rho log rho dx subject to integral rho = 1. The Gibbs–Boltzmann distribution concentrates near the minima of V, with width proportional to sigma (the "temperature" parameter).

### N9. Entropy Dissipation (H-Theorem)

**Source:** FP-3, FP-8 (gradient drift).

The relative entropy (KL divergence) with respect to the equilibrium:

    H[rho | rho_eq] = integral rho log(rho / rho_eq) dx >= 0

satisfies:

    d/dt H[rho | rho_eq] = -I[rho | rho_eq] <= 0

where I[rho | rho_eq] = integral rho |nabla log(rho / rho_eq)|^2 dx is the *Fisher information*. This is the *H-theorem* of the FP equation — the exact analogue of Boltzmann's H-theorem for the Boltzmann equation, proving that the entropy monotonically decreases toward the equilibrium value.

The H-theorem is the FP's Lyapunov identity, analogous to:
- AC: dF/dt = -M ||mu||^2.
- CH: dF/dt = -M ||nabla mu||^2.
- PME: dH/dt = -(4m/(m-1)) ||nabla(u^{(m+1)/2})||^2.

### N10. Wasserstein Gradient-Flow Structure (Gradient Drift)

**Source:** FP-3, FP-8 (b = -nabla V).

The gradient FP equation is a gradient flow of the free energy F[rho] in the *Wasserstein-2 metric*:

    partial_t rho = -grad_{W_2} F[rho]

where W_2 is the 2-Wasserstein distance on the space of probability measures. This identification (due to Jordan–Kinderlehrer–Otto, 1998) places the FP equation in the same structural class as the PME (which is a Wasserstein gradient flow of the Renyi entropy).

The Wasserstein gradient-flow structure implies:
- The free energy F is a strict Lyapunov functional.
- The W_2 distance between any two solutions decreases in time (Wasserstein contractivity).
- The dynamics are the steepest descent of F in the optimal-transport metric.
- The equilibrium rho_eq minimizes F over all probability measures.

### Summary of Necessary Configurations

| Label | Necessary Configuration                     | Source                |
|-------|---------------------------------------------|-----------------------|
| N1    | Drift–diffusion decomposition               | FP-3                  |
| N2    | Linear parabolicity                         | FP-3, FP-8            |
| N3    | Probability conservation (integral = 1)     | FP-4                  |
| N4    | Positivity preservation                     | FP-1, FP-3            |
| N5    | Infinite-speed propagation                  | FP-3, FP-8            |
| N6    | Gaussian smoothing at small scales          | FP-3                  |
| N7    | Exponential convergence (confining drift)   | FP-3, FP-8, gradient  |
| N8    | Gibbs–Boltzmann equilibrium (gradient drift)| FP-3, FP-8            |
| N9    | Entropy dissipation (H-theorem)             | FP-3, FP-8, gradient  |
| N10   | Wasserstein gradient flow (gradient drift)  | FP-3, FP-8            |

---

## 3. Envelope Inequalities (E1–E10)

---

**E1. Mass Conservation Identity**

    integral rho(x, t) dx = 1    for all t >= 0

Exact identity. The most fundamental constraint: total probability is conserved.

---

**E2. Positivity Preservation**

    rho_0 >= 0  =>  rho(t) >= 0    for all t >= 0

The maximum principle for linear parabolic equations. Combined with E1, this ensures rho(t) is a valid probability density at all times.

---

**E3. Entropy Dissipation (H-Theorem, Gradient Drift)**

    d/dt H[rho | rho_eq] = -I[rho | rho_eq] <= 0

where H[rho | rho_eq] = integral rho log(rho/rho_eq) dx is the relative entropy and I is the Fisher information:

    I[rho | rho_eq] = integral rho |nabla log(rho/rho_eq)|^2 dx

The relative entropy decreases monotonically. The dissipation rate is the Fisher information — a *strictly positive* quadratic form that vanishes only at equilibrium (rho = rho_eq).

---

**E4. Fisher Information Identity**

    I[rho | rho_eq] = integral rho |nabla log(rho / rho_eq)|^2 dx = -d/dt H[rho | rho_eq]

The Fisher information is the *dissipation rate* of the relative entropy. It measures the "sharpness" of rho relative to rho_eq. As rho → rho_eq, the Fisher information → 0, and the entropy dissipation rate → 0.

The Fisher information also satisfies its own dissipation identity (de Bruijn's identity), producing a hierarchy of entropy-information-dissipation inequalities.

---

**E5. Log-Sobolev Inequality (Confining Potentials)**

For V strongly convex (Hess V >= kappa I, kappa > 0):

    H[rho | rho_eq] <= (1 / (2 kappa)) I[rho | rho_eq]

The log-Sobolev inequality (LSI) bounds the entropy by the Fisher information. Combined with E3:

    d/dt H <= -2 kappa H

giving *exponential* entropy decay:

    H[rho(t) | rho_eq] <= H[rho_0 | rho_eq] exp(-2 kappa t)

The log-Sobolev constant kappa is determined by the *convexity of V* — the stronger the potential confines the particles, the faster the convergence. For the Ornstein–Uhlenbeck process (V = |x|^2 / 2), kappa = 1, and the convergence rate is 2.

The LSI is the *strongest convergence estimate* in the FP envelope. It is stronger than the Poincare inequality (E6) and implies it.

---

**E6. Poincare Inequality (Spectral Gap)**

For V confining with rho_eq as equilibrium:

    Var_{rho_eq}(f) <= (1 / lambda_1) integral |nabla f|^2 rho_eq dx

where lambda_1 > 0 is the spectral gap of the FP operator and Var_{rho_eq}(f) = integral f^2 rho_eq dx - (integral f rho_eq dx)^2 is the variance under the equilibrium measure.

Applied to f = rho / rho_eq (the density ratio), the Poincare inequality gives:

    ||rho(t) - rho_eq||_{L^2(rho_eq^{-1})}^2 <= ||rho_0 - rho_eq||_{L^2(rho_eq^{-1})}^2 exp(-2 lambda_1 t)

Exponential convergence in the weighted L^2 norm at rate 2 lambda_1. The spectral gap lambda_1 is the smallest nonzero eigenvalue of the FP operator.

---

**E7. Exponential Convergence Rate**

Combining E5 and E6:

    H[rho(t) | rho_eq] <= H[rho_0 | rho_eq] exp(-2 kappa t)    [from LSI]
    ||rho(t) - rho_eq||_{L^2}^2 <= C exp(-2 lambda_1 t)          [from Poincare]
    W_2(rho(t), rho_eq) <= W_2(rho_0, rho_eq) exp(-kappa t)     [from Wasserstein contractivity]

The convergence is *exponential in all metrics* — entropy, L^2, and Wasserstein. The rates (2 kappa, 2 lambda_1, kappa) depend on the convexity of V and the diffusion constant sigma^2. For strongly convex V, the convergence is *unconditionally exponential* — no smallness condition, no conditional hypothesis.

---

**E8. Gaussian Smoothing Estimate**

For the pure diffusion part (b = 0):

    ||nabla^k rho(t)||_{L^2} <= C_k t^{-k/2} ||rho_0||_{L^2}    for t > 0, k >= 0

The same Gaussian smoothing as the heat equation: each derivative costs t^{-1/2}. For the full FP equation with drift, the smoothing is modified by the drift (which can concentrate probability), but the *high-frequency smoothing* is still Gaussian at leading order:

    Mode k damped at rate D k^2 + O(|b| k)    for large k

The diffusion dominates the drift at high wavenumbers.

---

**E9. Drift–Diffusion Energy Balance**

The L^2 norm of rho satisfies:

    d/dt ||rho||_{L^2}^2 = -2 integral (nabla rho)^T D (nabla rho) dx + integral (div b) rho^2 dx + boundary terms

The first term (diffusion) is negative definite (stabilizing). The second term (drift) can be positive or negative depending on div b:
- div b < 0 (compressing drift): concentrates rho, increases ||rho||_{L^2}.
- div b > 0 (expanding drift): dilutes rho, decreases ||rho||_{L^2}.
- div b = 0 (incompressible drift): preserves ||rho||_{L^2}.

For confining potentials (V convex, div b < 0 near infinity), the drift term is bounded, and the diffusion term dominates in the long run, driving rho toward the equilibrium.

---

**E10. Wasserstein Contractivity (Gradient Drift)**

For b = -nabla V with V lambda-convex (Hess V >= lambda I):

    W_2(rho_1(t), rho_2(t)) <= exp(-lambda t) W_2(rho_1(0), rho_2(0))

The Wasserstein-2 distance between any two FP solutions *contracts exponentially*. This is the strongest stability estimate for the gradient FP equation:

- **Stronger than L^1 contraction** (PME has L^1 contraction; FP has Wasserstein contraction, which implies L^1 contraction via the Wasserstein-L^1 inequality).
- **Stronger than entropy decay** (Wasserstein contractivity implies entropy decay via the Talagrand inequality).
- **Implies uniqueness of equilibrium** (if all solutions contract toward each other, they must converge to the same limit).

The Wasserstein contractivity is the FP's structural analogue of the PME's L^1 contraction — but in a *stronger metric* (Wasserstein vs. L^1).

---

### Envelope Summary

The FP envelope is defined by ten constraints organized into three tiers:

**Tier 1 — Universal (all FP systems, all drifts):**
- E1: Probability conservation (integral = 1, exact).
- E2: Positivity preservation (rho >= 0, unconditional).
- E8: Gaussian smoothing at high wavenumbers.
- E9: Drift–diffusion energy balance.

**Tier 2 — Gradient-Drift (b = -nabla V):**
- E3: Entropy dissipation (H-theorem, exact identity).
- E4: Fisher information as dissipation rate.
- E5: Log-Sobolev inequality (exponential entropy decay).
- E7: Exponential convergence in all metrics.
- E10: Wasserstein contractivity.

**Tier 3 — Spectral:**
- E6: Poincare / spectral gap (exponential L^2 convergence).

**All constraints are unconditional** within their scope (universal or gradient-drift). No constraint is open, conditional, or dimension-dependent. The FP envelope is *fully closed* for all d >= 1.

---

## 4. Central Architectural Finding

### 4.1 The FP Envelope in the Atlas

| Architecture | Envelope Status       | Closing Mechanism                         | Key Feature         |
|-------------|------------------------|-------------------------------------------|---------------------|
| ED          | Closed (static)        | Unique factorization                      | Static              |
| PME         | Closed (all d, m > 1)  | Degeneracy + entropy + L^1 + conservation | Self-similar        |
| AC          | Closed (d <= 3)        | Max. principle + Lyapunov                 | Mean curvature      |
| CH          | Closed (d <= 3)        | 4th-order smooth. + Lyapunov              | Coarsening          |
| TFE (n>=1)  | Closed                 | 4th-order + degeneracy + cons. + Lyapunov | Contact line        |
| **FP**      | **Closed (all d)**     | **Linearity + positivity + entropy**      | **Gibbs–Boltzmann** |
| NS          | Open (3D)              | Viscosity (insufficient)                  | Turbulence          |
| RD          | Constitutive           | None universal                            | Patterns/chaos      |

### 4.2 What Makes the FP Envelope Unique

The FP envelope is closed by the *simplest mechanism* in the Atlas: **linearity**. Every other closed architecture relies on nonlinear structural features for closure — maximum principles, degenerate diffusion, Lyapunov functionals derived from nonlinear free energies, fourth-order smoothing. The FP equation needs none of these because the PDE is *linear in rho*:

- **Existence and uniqueness:** Follow from the standard theory of linear parabolic equations. No nonlinear fixed-point argument, no energy estimates, no bootstrap.
- **Positivity:** Follows from the linear maximum principle (rho = 0 is a sub-solution).
- **Smoothness:** Follows from linear parabolic regularity (Schauder theory, hypoelliptic theory).
- **Convergence:** Follows from spectral theory of the linear operator (eigenvalue gap → exponential decay).

The linearity makes FP the *most analytically tractable* PDE in the Atlas. The complete spectral decomposition of the FP operator is available (at least in principle), giving exact solutions in terms of eigenfunction expansions.

### 4.3 The Stochastic Corner

The FP equation is the deterministic PDE that describes the statistical behavior of a stochastic process. This *stochastic origin* gives it structural features that no other architecture possesses:

- **Linearity** (from the Markov property of the SDE).
- **Probabilistic normalization** (integral rho = 1, from probability axioms).
- **Drift + diffusion** (from the SDE decomposition dX = b dt + sigma dW).
- **Gibbs–Boltzmann equilibrium** (from the fluctuation-dissipation theorem, connecting drift to diffusion through the potential).
- **Wasserstein gradient flow** (from optimal transport theory, connecting the PDE to the geometry of probability measures).

The FP equation is the *only* architecture in the Atlas where the PDE is *derived from a stochastic process* rather than from continuum mechanics or thermodynamics. This derivation route produces a qualitatively different architecture — one that is linear, probabilistic, and connected to information theory (entropy, Fisher information, mutual information) rather than to energy, momentum, and stress.

### 4.4 FP and ED: The Density Architectures

The FP equation and the Event Density framework share a deep structural parallel: both are *density architectures* — frameworks for describing how a density (of probability, of events) distributes across a space. The parallel:

- ED: distributes prime-event density across the integer skyline (discrete, static, arithmetic).
- FP: distributes probability density across Euclidean space (continuous, dynamic, stochastic).

Both produce *universal distributions* as their attractors:
- ED → PNT, Chebyshev, Mertens (the asymptotic distribution of primes).
- FP → Gibbs–Boltzmann (the equilibrium distribution of a stochastic particle).

Both are *fully local, fully closed, anomaly-free* architectures. The FP equation is the *dynamical, continuous, stochastic* realization of the density-distribution concept that ED embodies statically and arithmetically.

---

*End of Mode 1: Axiom → Envelope. Mode 2 (PDE → Extremal Dynamics) will follow in a subsequent file.*
