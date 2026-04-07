# AD Evaluation: Fokker–Planck Equation — Mode 2: PDE → Extremal Dynamics

Allen Proxmire

April 2026

---

## Overview

Mode 2 moves from the static envelope to the dynamics. The FP dynamical landscape is *qualitatively simpler* than every other PDE in the Atlas — simpler even than the PME (which has free-boundary geometry and self-similar spreading) and the AC (which has interface dynamics and metastability). The FP dynamics reduce to a single program: *spread, drift, converge to equilibrium*. There is no interface motion, no free boundary, no pattern formation, no phase separation, no turbulence, and (for gradient drift) no non-convergent behavior. The simplicity arises from *linearity*: the FP equation is the only linear PDE in the Atlas, and linearity eliminates every mechanism for dynamical complexity.

Throughout:

    partial_t rho = -div(b rho) + div(D nabla rho)

on R^d or bounded Omega, with rho >= 0, integral rho = 1, prescribed b(x) and D(x) positive definite.

---

## 1. Fundamental Time and Length Scales

### 1.1 Two Characteristic Time Scales

The FP equation has two independent time scales at spatial scale L:

**Diffusion time scale:**

    t_D = L^2 / D

The time for diffusion to homogenize a perturbation of scale L. Second-order parabolic: scales as L^2. This is the same scaling as the linear heat equation, the PME (with D replaced by u^{m-1} D), and the diffusion channel of RD.

**Drift (transport) time scale:**

    t_T = L / |b|

The time for the drift to transport probability a distance L. First-order: scales as L. This is *faster* than diffusion at large scales (L >> D/|b|) and *slower* at small scales (L << D/|b|).

**The Peclet number:**

    Pe = t_D / t_T = L |b| / D

measures the relative importance of drift to diffusion at scale L:
- Pe >> 1: drift-dominated (large scales, strong drift, weak diffusion).
- Pe << 1: diffusion-dominated (small scales, weak drift, strong diffusion).
- Pe ~ 1: balanced (the characteristic length L_* = D / |b| where drift and diffusion are commensurate).

### 1.2 Three Geometric Regimes

**Regime (A): Free Diffusion (b = 0)**

No drift. The FP equation reduces to the heat equation:

    partial_t rho = div(D nabla rho) = D Delta rho    (for constant isotropic D)

Dynamics: Gaussian spreading. The density rho(t) approaches a Gaussian with variance growing as 2Dt. On R^d, the solution for a point mass initial datum is:

    rho(x, t) = (4 pi D t)^{-d/2} exp(-|x|^2 / (4Dt))

On bounded domains: exponential convergence to the uniform distribution rho_eq = 1/|Omega| at rate lambda_1 (the first nonzero eigenvalue of -D Delta with Neumann conditions).

This is the *simplest FP regime*: pure smoothing, no concentration, monotone approach to uniformity.

**Regime (B): Confining Gradient Drift (b = -nabla V, V convex)**

The drift pushes probability toward the minimum of V. The diffusion spreads it. The competition produces a unique equilibrium — the Gibbs–Boltzmann distribution:

    rho_eq = Z^{-1} exp(-V / sigma^2)

The dynamics are *exponentially convergent* to rho_eq. The convergence rate is determined by the convexity of V:

- Strongly convex V (Hess V >= kappa I, kappa > 0): convergence at rate kappa in the Wasserstein metric, 2 kappa in entropy.
- Weakly convex V: slower convergence, potentially algebraic for non-uniformly convex potentials.
- Harmonic V (V = |x|^2 / 2): the *Ornstein–Uhlenbeck process*, with explicit Gaussian equilibrium rho_eq = (2 pi sigma^2)^{-d/2} exp(-|x|^2 / (2 sigma^2)) and spectral gap lambda_1 = 1.

This is the *canonical FP regime*: drift concentrates, diffusion spreads, and the balance produces an explicit exponentially attracting equilibrium.

**Regime (C): Non-Confining or Non-Gradient Drift**

When V is not confining (V does not grow at infinity), or when b is not a gradient field:

- *Non-confining gradient drift:* rho may spread to infinity (no equilibrium). The long-time behavior is diffusive spreading, modulated by the drift.
- *Non-gradient drift:* the probability density may circulate along the flow lines of b. If b has closed orbits (e.g., a rotation field), rho circulates indefinitely without settling to a fixed equilibrium. However, this circulation is *linear* — it is deterministic rotation, not nonlinear oscillation or chaos.
- *Mixing drift:* If b is a mixing (ergodic) vector field, the combination of drift and diffusion can produce faster-than-diffusive convergence to equilibrium (enhanced diffusion).

### 1.3 Contrast with Other Architectures

| Feature                    | FP                      | PME/TFE                | RD                     | NS                    |
|----------------------------|-------------------------|------------------------|------------------------|-----------------------|
| Time scale (diffusion)     | L^2 / D (constant D)   | L^2 / u^{m-1} or L^4 / h^n | L^2 / D          | L^2 / nu              |
| Time scale (transport)     | L / \|b\| (drift)      | None (no drift)        | None (no drift*)       | L / \|u\| (advection)|
| Peclet number              | Pe = L\|b\|/D           | N/A                    | Da = L^2\|\|R'\|\|/D  | Re = L\|u\|/nu        |
| Linearity                  | **Linear**              | Nonlinear              | Nonlinear              | Nonlinear             |
| Propagation speed          | Infinite                | Finite                 | Constitutive           | Infinite              |
| Equilibrium (confining)    | Gibbs–Boltzmann         | Barenblatt / flat film | Constitutive           | None (decays to 0)    |

*Standard RD has no first-order drift. Some extensions (chemotaxis, convection-RD) add drift terms.

The FP architecture's *linearity* is the deepest structural distinction: the Peclet number Pe controls which regime dominates, but the *dynamics within each regime are linear*. No nonlinear amplification, no self-interaction, no turbulence.

---

## 2. Extremal Behaviors

### E1. Gaussian Spreading Under Pure Diffusion

For b = 0, D = sigma^2 I on R^d, with initial datum rho_0 = delta(x):

    rho(x, t) = (4 pi sigma^2 t)^{-d/2} exp(-|x|^2 / (4 sigma^2 t))

The Gaussian is the *extremal spreading profile* — the fundamental solution of the heat equation. Key properties:
- Variance: Var(X_t) = 2 sigma^2 t (grows linearly).
- Maximum: ||rho(t)||_{L^{infinity}} = (4 pi sigma^2 t)^{-d/2} (decays algebraically).
- Support: all of R^d for any t > 0 (infinite-speed propagation).
- Entropy: H[rho(t)] = (d/2) log(4 pi e sigma^2 t) (grows logarithmically — the density becomes increasingly disordered).

This is the *simplest extremal behavior* in the PDE Atlas: a single explicit formula describing the density for all time. No other architecture has such a clean closed-form fundamental solution.

### E2. Drift-Dominated Transport

When Pe >> 1 (strong drift, weak diffusion), the dynamics are approximately:

    partial_t rho ≈ -div(b rho)

This is the *continuity equation* — rho is transported along the characteristics of b without spreading. The density rho(t) is approximately the push-forward of rho_0 along the flow map of b:

    rho(Phi_t(x), t) det(nabla Phi_t(x)) = rho_0(x)

where Phi_t is the flow of b (dPhi/dt = b(Phi)). In this regime, the probability density moves as a "rigid" object along the drift field, with diffusion providing only a small correction (a slowly growing Gaussian blur around the transported density).

### E3. Exponential Convergence to Gibbs–Boltzmann (Confining Gradient Drift)

For b = -nabla V with V lambda-convex (Hess V >= lambda I, lambda > 0):

    H[rho(t) | rho_eq] <= exp(-2 lambda t) H[rho_0 | rho_eq]

The relative entropy decays *exponentially*. The convergence is:
- *Unconditional:* No smallness condition on rho_0.
- *Dimension-independent:* The rate 2 lambda does not depend on d.
- *Metric-universal:* Convergence holds in entropy, L^2, L^1, and Wasserstein simultaneously.

The Gibbs–Boltzmann equilibrium rho_eq = Z^{-1} exp(-V/sigma^2) is the unique global attractor. The exponential rate 2 lambda is the *fastest convergence rate* of any gradient-flow architecture in the Atlas:
- PME: algebraic decay (t^{-gamma}).
- AC: exponential in bulk (rate 2M), but interface dynamics are algebraic.
- CH: algebraic coarsening (t^{-1/3}).
- TFE: algebraic spreading (t^{-alpha}).

FP with convex potential is the *fastest-converging* architecture in the Atlas.

### E4. Spectral-Gap-Controlled Relaxation

The FP operator L = -div(b .) + div(D nabla .) on L^2(rho_eq^{-1}) is self-adjoint (for gradient drift) with discrete spectrum:

    0 = lambda_0 < lambda_1 <= lambda_2 <= ...

The eigenvalue lambda_0 = 0 corresponds to the equilibrium rho_eq. The spectral gap lambda_1 > 0 controls the asymptotic convergence rate:

    ||rho(t) - rho_eq||_{L^2(rho_eq^{-1})} <= exp(-lambda_1 t) ||rho_0 - rho_eq||_{L^2(rho_eq^{-1})}

For the Ornstein–Uhlenbeck process (V = |x|^2/2, sigma^2 = 1): lambda_k = k, so lambda_1 = 1. The eigenvalues are exactly the natural numbers — the most explicit spectrum in the Atlas.

The spectral decomposition provides *complete analytical control* over the dynamics: every solution can be expanded in eigenfunctions, and the time evolution is an exponentially decaying sum. This level of analytical control is *unique to the linear FP equation* — no nonlinear PDE in the Atlas admits a comparable spectral decomposition.

### E5. Entropy Decay with Explicit Rate (Log-Sobolev)

Under the log-Sobolev inequality (valid for lambda-convex V):

    d/dt H[rho | rho_eq] = -I[rho | rho_eq] <= -2 lambda H[rho | rho_eq]

giving:

    H[rho(t) | rho_eq] <= exp(-2 lambda t) H[rho_0 | rho_eq]

The entropy decay rate 2 lambda is *twice the spectral gap* — the log-Sobolev inequality gives a *stronger* convergence rate than the spectral gap alone. This is the content of the Bakry–Emery theory: for uniformly convex potentials, the entropy contracts at twice the L^2 rate.

### E6. Instantaneous Analytic Regularization

The FP equation with non-degenerate D provides *instantaneous* analytic regularization: for any t > 0, the solution rho(t) is a real-analytic function (not just C^{infinity} but analytic — representable by a convergent power series at every point).

This is the *strongest regularity* of any PDE in the Atlas:
- AC, CH: C^{infinity} for t > 0 (smooth but not necessarily analytic at the free boundary for degenerate variants).
- PME, TFE: C^{infinity} in the interior, Holder at the free boundary.
- NS: C^{infinity} in 2D; open in 3D.
- RD: constitutive.
- **FP: real-analytic for all t > 0, everywhere in the domain.**

The analytic regularization is a consequence of the *linearity + non-degeneracy*: the FP heat kernel is a Gaussian (analytic), and convolution with an analytic kernel produces an analytic function.

### E7. Infinite-Speed Propagation

The non-degenerate diffusion ensures that rho(x, t) > 0 for all x and all t > 0, regardless of the support of rho_0. A point mass at x = 0 instantly becomes a strictly positive density on all of R^d.

This is the structural opposite of PME/TFE (finite speed, compact support). The FP architecture has no free boundaries, no contact lines, and no compact-support preservation. The "information front" is the entire domain from t = 0+.

### E8. Absence of Oscillations and Chaos

The FP dynamics are *incapable* of oscillation or chaos:

**Gradient drift (b = -nabla V):** The free energy F[rho] is a strict Lyapunov functional. Monotone descent forbids limit cycles, periodic orbits, and recurrence.

**Non-gradient drift:** The PDE is linear. Two solutions rho_1, rho_2 satisfy rho_1 - rho_2 = linear combination of eigenfunctions of the FP operator (or generalized eigenfunctions for non-self-adjoint cases). The difference decays or oscillates in a *linear, non-chaotic* way. There is no sensitive dependence on initial conditions because the solution operator is a *linear* semigroup — the image of two nearby initial data stays nearby (linearly bounded separation).

For non-gradient drifts with rotational structure, the probability density can *rotate* in space (circulate along the drift's flow lines), but this rotation is *linear* — it is deterministic transport, not nonlinear oscillation. The "oscillation" in the spatial distribution of rho is the same as the rotation of a rigid body — perfectly predictable, with no chaos.

---

## 3. Universal Inequalities

---

**U1. Mass Conservation**

    integral rho(x, t) dx = 1    for all t >= 0

Exact identity. Total probability invariant.

---

**U2. Positivity Preservation**

    rho_0 >= 0  =>  rho(t) >= 0    for all t >= 0

Linear parabolic maximum principle. Combined with U1: rho is a probability density for all time.

---

**U3. Gaussian Smoothing Estimate**

    ||nabla^k rho(t)||_{L^2} <= C_k t^{-k/2} ||rho_0||_{L^2}    for t > 0

Second-order parabolic smoothing: each derivative costs t^{-1/2}. For the full FP equation with drift, the estimate is modified by the drift (exponential factors from the transport), but the high-frequency behavior is still Gaussian.

---

**U4. Entropy Dissipation Identity (Gradient Drift)**

    d/dt H[rho | rho_eq] = -I[rho | rho_eq]

where H = integral rho log(rho/rho_eq) dx and I = integral rho |nabla log(rho/rho_eq)|^2 dx. Exact identity — the dissipation rate is the Fisher information.

---

**U5. Log-Sobolev Inequality (Lambda-Convex V)**

    H[rho | rho_eq] <= (1/(2 lambda)) I[rho | rho_eq]

Bounds entropy by Fisher information. Implies exponential entropy decay at rate 2 lambda.

---

**U6. Exponential Entropy Decay**

    H[rho(t) | rho_eq] <= exp(-2 lambda t) H[rho_0 | rho_eq]

Follows from U4 + U5 by Gronwall. The strongest convergence estimate for confining potentials.

---

**U7. Poincare / Spectral-Gap Inequality**

    Var_{rho_eq}(f) <= (1/lambda_1) integral |nabla f|^2 rho_eq dx

Implies L^2 convergence at rate lambda_1:

    ||rho(t) - rho_eq||_{L^2(rho_eq^{-1})}^2 <= exp(-2 lambda_1 t) ||rho_0 - rho_eq||_{L^2(rho_eq^{-1})}^2

---

**U8. Wasserstein Contractivity (Lambda-Convex V)**

    W_2(rho_1(t), rho_2(t)) <= exp(-lambda t) W_2(rho_1(0), rho_2(0))

Exponential contraction in the Wasserstein-2 metric. The strongest stability estimate: implies uniqueness, continuous dependence, and convergence.

---

**U9. Drift–Diffusion Energy Balance**

    d/dt integral |x|^2 rho dx = 2 integral (b . x) rho dx + 2 tr(D)

For confining drift (b . x <= -lambda |x|^2 + C):

    integral |x|^2 rho(t) dx <= exp(-2 lambda t) integral |x|^2 rho_0 dx + C/lambda

The second moment is bounded and converges to a finite value. This provides spatial confinement: the probability mass does not escape to infinity.

---

**U10. Higher Moment Bounds (Confining Drift)**

For V growing polynomially (V(x) >= c |x|^{2k} for large |x|):

    integral |x|^{2k} rho(t) dx <= C(k, V, sigma^2)    for all t >= t_0 > 0

All polynomial moments are bounded under confining drift. This provides *tail control*: the probability density decays at least as fast as exp(-c |x|^{2k} / sigma^2) at infinity, matching the equilibrium's tail behavior.

---

### Universal Inequality Summary

| Label | Inequality                        | Type           | Status              | Role                         |
|-------|-----------------------------------|----------------|---------------------|------------------------------|
| U1    | Mass conservation                 | Exact equality | All FP              | Fundamental invariant        |
| U2    | Positivity                        | Max. principle | All FP              | Probability validity         |
| U3    | Gaussian smoothing                | Estimate       | All FP, t > 0       | High-k regularization        |
| U4    | Entropy dissipation               | Exact identity | Gradient drift      | H-theorem                    |
| U5    | Log-Sobolev                       | Inequality     | Lambda-convex V     | Entropy-Fisher bridge        |
| U6    | Exponential entropy decay         | Decay bound    | Lambda-convex V     | Convergence rate             |
| U7    | Poincare/spectral gap             | Inequality     | Confining drift     | L^2 convergence              |
| U8    | Wasserstein contractivity         | Contraction    | Lambda-convex V     | Strongest stability          |
| U9    | Drift-diffusion energy balance    | Identity       | All FP              | Moment control               |
| U10   | Higher moment bounds              | Bound          | Confining drift     | Tail control                 |

**Seven of ten inequalities are unconditional** (U1, U2, U3, U9 for all FP; U4, U5, U6, U7, U8, U10 for confining gradient drift). The remaining three (U5, U6, U8) require lambda-convexity — the *strongest* form of confining drift.

---

## 4. Attractors and Long-Time Behavior

### 4.1 The Gibbs–Boltzmann Equilibrium

For confining gradient drift b = -nabla V on R^d:

    rho_eq(x) = Z^{-1} exp(-V(x) / sigma^2),    Z = integral exp(-V / sigma^2) dx

Properties of rho_eq:
- Unique: the only probability density satisfying the stationarity condition.
- Global minimizer: minimizes F[rho] = integral rho V dx + sigma^2 integral rho log rho dx over all probability densities.
- Explicit: given in closed form for any V (up to the normalizing constant Z).
- Concentrates near minima of V: rho_eq is largest where V is smallest.
- Width proportional to sigma: the "temperature" sigma^2 determines the spread of rho_eq around the potential wells.

### 4.2 Convergence Mechanisms (Three Levels)

The FP convergence theory has a *hierarchical* structure — three levels of increasingly powerful estimates:

**Level 1: Spectral gap (Poincare)**

    ||rho(t) - rho_eq||_{L^2(rho_eq^{-1})} <= exp(-lambda_1 t) ||rho_0 - rho_eq||

L^2 convergence at rate lambda_1. The weakest but most widely applicable estimate. Requires only a spectral gap (which exists for any confining potential on a bounded domain).

**Level 2: Log-Sobolev**

    H[rho(t) | rho_eq] <= exp(-2 lambda t) H[rho_0 | rho_eq]

Entropy convergence at rate 2 lambda. Stronger than Level 1 (implies it via Csiszar–Kullback–Pinsker). Requires lambda-convexity of V.

**Level 3: Wasserstein contractivity**

    W_2(rho_1(t), rho_2(t)) <= exp(-lambda t) W_2(rho_1(0), rho_2(0))

Wasserstein convergence at rate lambda. The strongest — implies both Level 1 and Level 2 (via Talagrand and Otto–Villani inequalities). Requires lambda-convexity of V.

This three-level hierarchy is *unique to FP* in the Atlas. No other architecture has three nested convergence mechanisms at three different metric levels (L^2, entropy, Wasserstein). The hierarchy reflects the rich interplay between probability theory (entropy), functional analysis (spectral gap), and optimal transport (Wasserstein) that converges at the FP equation.

### 4.3 Comparison with Other Architectures' Attractors

| Architecture | Attractor                    | Convergence Rate    | Mechanism             | Explicit?  |
|-------------|------------------------------|---------------------|-----------------------|------------|
| **FP**      | **Gibbs–Boltzmann**         | **Exponential**     | **Spectral + LSI + Wass.**| **Yes** |
| PME         | Barenblatt profile           | Algebraic (t^{-gamma})| Entropy + L^1 contraction | Yes     |
| TFE         | Source-type profile          | Algebraic            | Energy + degeneracy    | ODE-defined|
| AC          | phi = ±1 (uniform)          | Exponential (bulk)   | Max. principle + Lyapunov| Trivial   |
| CH          | Phase-separated domains     | Algebraic (coarsening)| Lyapunov + H^{-1}    | Implicit   |
| NS (2D)    | Compact attractor           | Dissipation-dependent| Viscosity              | Not explicit|
| RD          | Constitutive (full zoo)     | Constitutive         | Constitutive           | Constitutive|

The FP attractor is the *most completely characterized* attractor in the Atlas:
- **Explicit formula:** rho_eq = Z^{-1} exp(-V/sigma^2). No ODE to solve (unlike PME's Barenblatt profile), no implicit characterization (unlike CH's phase-separated states).
- **Exponential convergence:** Faster than all nonlinear architectures' algebraic convergence.
- **Three convergence metrics:** L^2, entropy, and Wasserstein — all exponential, all with explicit rates.
- **Dimension-independent rate:** The Bakry–Emery rate 2 lambda does not depend on d.

### 4.4 The Simplest Attractor in the Atlas

The FP attractor for confining gradient drift is a *single explicit function*:

    rho_eq(x) = Z^{-1} exp(-V(x) / sigma^2)

This is simpler than every other attractor:
- PME's Barenblatt: an explicit formula, but with a compact-support cutoff and a nonlinear exponent 1/(m-1).
- AC's phi = ±1: trivial (constant), but the approach involves complex interface dynamics.
- CH's phase-separated states: implicit (determined by the variational principle, mass constraint, and domain geometry).
- NS's attractor: not explicitly known.
- RD's attractors: constitutive-dependent, ranging from fixed points to strange attractors.

The FP equilibrium is the *Gibbs–Boltzmann distribution* — the central object of equilibrium statistical mechanics, the maximum-entropy distribution subject to an energy constraint, and the unique probability density that balances potential-energy minimization against entropic spreading. Its explicit, canonical form is the structural signature of the FP architecture's stochastic origin.

---

## 5. Comparison with AC, CH, PME, TFE, RD, and NS

### 5.1 The Linearity Divide

The deepest structural divide in the PDE Atlas separates the *linear* FP equation from all *nonlinear* architectures:

| Property                     | FP (linear)                    | All others (nonlinear)          |
|------------------------------|--------------------------------|----------------------------------|
| Superposition                | Holds                          | Fails                            |
| Spectral decomposition       | Complete (eigenfunction expansion)| Not available (generically)   |
| Closed-form solutions        | Available (for b = -nabla V)  | Rare (special cases only)        |
| Sensitive dependence         | Impossible (linear semigroup)  | Possible (NS, RD)               |
| Turbulence                   | Impossible                     | Possible (NS)                    |
| Pattern formation            | Impossible                     | Possible (RD, Turing)           |
| Chaos                        | Impossible                     | Possible (RD, NS)               |
| Analytical tractability      | Complete                       | Partial to minimal               |

The linearity of FP makes it the *most analytically tractable* PDE in the Atlas — every question about the dynamics can, in principle, be answered by spectral methods. This tractability comes at a cost: the FP equation cannot generate any of the complex nonlinear phenomena (turbulence, patterns, chaos, phase separation) that make the other architectures physically rich.

### 5.2 The Drift Channel: Unique to FP

The FP equation is the only architecture with a *linear first-order drift* channel:

| Architecture | First-order channel     | Character                          |
|-------------|-------------------------|------------------------------------|
| FP          | -div(b rho)             | Linear, external, prescribed       |
| NS          | (u . nabla)u            | Nonlinear, self-advecting          |
| AC/CH/PME/TFE | None                 | Pure diffusion (no drift)          |
| RD          | None (standard)         | Reaction + diffusion               |

The FP drift is *external* (b prescribed, independent of rho) and *linear* (entering the PDE linearly). The NS advection is *self-referential* (u advects itself) and *nonlinear* (quadratic in u). This distinction is why FP is tractable and NS is not: self-advection creates feedback loops; external advection does not.

### 5.3 The Stochastic Origin: Unique to FP

The FP equation is the *only* PDE in the Atlas derived from a stochastic process:

    SDE: dX_t = b(X_t) dt + sigma dW_t    →    FP: partial_t rho = -div(b rho) + sigma^2 Delta rho

This stochastic derivation gives FP structural features absent in all other architectures:
- **Probabilistic normalization** (integral rho = 1, not integral rho = M for arbitrary M).
- **Fluctuation-dissipation relation** (the drift b and diffusion D are connected through the equilibrium rho_eq = exp(-V/sigma^2) when b = -nabla V).
- **Information-theoretic structure** (entropy, Fisher information, mutual information are natural functionals for FP but not for AC/CH/PME/NS).
- **Optimal transport** (the Wasserstein gradient-flow interpretation connects FP to the geometry of probability measures).

### 5.4 FP and ED: The Density-Distribution Parallel

FP and ED are the two *density architectures* in the Atlas — frameworks for distributing a density across a space:

| Feature                    | FP                              | ED                              |
|----------------------------|---------------------------------|---------------------------------|
| Domain                     | Continuous (R^d)                | Discrete (Z)                    |
| Density type               | Probability                     | Event (prime) density           |
| Dynamics                   | Drift + diffusion (PDE)        | Static (arithmetic)             |
| Attractor                  | Gibbs–Boltzmann exp(-V/sigma^2)| PNT / Chebyshev distribution    |
| Mechanism                  | Stochastic (SDE)                | Arithmetic (factorization)      |
| Linearity                  | Linear                          | Linear (in a distributional sense)|
| Locality                   | Fully local                     | Fully local                     |
| Envelope                   | Fully closed                    | Fully closed                    |

Both architectures produce *universal distributions* as their attractors — the Gibbs–Boltzmann distribution for FP, the prime distribution (PNT, Mertens, Chebyshev) for ED. Both are fully local, fully closed, and anomaly-free. The FP equation is the closest PDE in the Atlas to ED's density-distribution concept: a framework for tracking how a density evolves toward its natural equilibrium.

### 5.5 Summary Table

| Feature                    | FP          | AC    | CH    | PME   | TFE   | NS    | RD          |
|----------------------------|-------------|-------|-------|-------|-------|-------|-------------|
| Linearity                  | **Linear**  | NL    | NL    | NL    | NL    | NL    | NL          |
| Drift channel              | **Yes**     | No    | No    | No    | No    | Self-adv. | No       |
| Diffusion order            | 2nd         | 2nd   | 4th   | 2nd   | 4th   | 2nd   | 2nd         |
| Conservation               | Prob (=1)   | No    | Yes   | Yes   | Yes   | Yes   | Constitutive|
| Gradient-flow (b=-nabla V) | Wasserstein | L^2   | H^{-1}| Wass. | Wt.H^{-1}| No | Gen. no   |
| Equilibrium                | Gibbs–Boltz.| ±1    | Phase | Baren.| Flat  | —     | Constitutive|
| Convergence rate           | Exponential | Exp.(bulk)| Alg. | Alg. | Alg.  | —    | Constitutive|
| Stochastic origin          | **SDE**     | No    | No    | No    | No    | No    | No          |
| Blowup                     | No          | No    | No    | No    | n-dep.| 3D?   | Constitutive|
| Analytical tractability    | **Complete**| High  | Mod.  | High  | Mod.  | Low   | Constitutive|

The FP equation is the *stochastic, linear corner* of the PDE Atlas: the simplest architecture with both drift and diffusion, the most analytically tractable PDE, and the closest classical PDE to ED's static density-distribution framework.

---

*End of Mode 2: PDE → Extremal Dynamics. Mode 3 (Channels → Constraint Surface) will follow in a subsequent file.*
