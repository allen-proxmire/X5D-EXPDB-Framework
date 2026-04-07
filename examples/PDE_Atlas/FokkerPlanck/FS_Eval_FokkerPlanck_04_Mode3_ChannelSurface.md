# AD Evaluation: Fokker–Planck Equation — Mode 3: Channels → Constraint Surface

Allen Proxmire

April 2026

---

## Overview

Mode 3 constructs the constraint surface of the FP architecture. The FP constraint surface is *the simplest fully closed surface* among all dynamical PDEs in the PDE Atlas. Its closure arises from *linearity* — the most economical closure mechanism available — rather than from the nonlinear mechanisms (maximum principle, degeneracy, fourth-order smoothing, entropy contraction) that the other architectures require. The FP surface has no open faces for *any* choice of constitutive parameters (b, D) — it is the only PDE in the Atlas whose closure is *unconditionally parameter-independent*.

We continue with:

    partial_t rho = -div(b rho) + div(D nabla rho),    rho >= 0,    integral rho = 1

---

## 1. Channel Decomposition

### Channel T: Transport (First-Order Drift)

    T(rho) = -div(b rho) = -b . nabla rho - (div b) rho

- **Locality:** Local. Depends on rho, nabla rho, and the prescribed field b(x) at each point.
- **Linearity:** Linear in rho. The drift b is prescribed (independent of rho). This is the *only first-order linear transport channel* in the PDE Atlas. NS has a first-order advection channel, but it is *nonlinear* (self-advection u . nabla u). AC/CH/PME/TFE/RD have no first-order channel at all.
- **Stability role:** b-dependent.
  - Confining drift (b = -nabla V, V convex): stabilizing — pushes rho toward the potential well.
  - Divergence-free drift (div b = 0): neutral — transports rho without concentrating or diluting.
  - Expanding drift (div b > 0): locally destabilizing — dilutes rho.
  - General: mixed. But crucially, the destabilization is *linear* — it cannot produce finite-time blowup, oscillations, or chaos. The worst a destabilizing linear drift can do is exponential growth of rho in some region, which is controlled by the conservation constraint (integral rho = 1) and the diffusion channel.
- **Scale action:** First-order in k. Transport moves mode k at rate |b| k. Scale-independent in the sense that all modes are advected at the same speed |b|, unlike diffusion which preferentially damps high-k modes.

### Channel D: Diffusion (Second-Order Smoothing)

    D(rho) = div(D nabla rho)

- **Locality:** Local. Second-order spatial derivatives at each point.
- **Linearity:** Linear in rho (for prescribed D(x)). The diffusion tensor D does not depend on rho.
- **Stability role:** Unconditionally stabilizing (for positive definite D). Damps all non-constant modes at rate D_min k^2. The stabilizing character is *independent of the drift* — the diffusion channel smooths regardless of what the transport channel does.
- **Scale action:** Second-order in k. Damping rate D k^2. High-frequency modes are damped fastest. This is the standard parabolic smoothing, identical in character to the diffusion channels of AC, PME, and RD (though those are often nonlinear in the state variable).

### Channel C: Conservation (Probability Preservation)

    C: integral rho(x, t) dx = 1    for all t >= 0

- **Locality:** Global constraint, locally enforced through the divergence form partial_t rho = -div(**J**).
- **Linearity:** Linear (the integral is a linear functional).
- **Stability role:** Constraining. Confines the dynamics to the *probability simplex* — the infinite-dimensional set {rho >= 0, integral rho = 1}. The conservation constraint prevents rho from "escaping" — the total probability is locked at 1, so any local increase must be compensated by a decrease elsewhere.
- **Scale action:** All-scale. The constraint couples the behavior of rho across all spatial scales.

### Channel P: Potential / Gradient-Flow Structure (b = -nabla V)

    P: partial_t rho = div(rho nabla(V + sigma^2 log rho))    [Wasserstein gradient flow of F]

    F[rho] = integral rho V dx + sigma^2 integral rho log rho dx

    dF/dt = -sigma^{-2} integral rho |nabla(V + sigma^2 log rho)|^2 dx <= 0

- **Locality:** The free energy F is a global functional, but the PDE (the gradient flow) is local.
- **Linearity:** The free energy F is *nonlinear* in rho (through the entropy term rho log rho), even though the PDE is linear. The gradient-flow structure introduces nonlinear *geometry* (the Wasserstein metric on the space of probability measures) without introducing nonlinear *dynamics*.
- **Stability role:** Stabilizing (when present). F is a strict Lyapunov functional with a unique minimizer (the Gibbs–Boltzmann distribution rho_eq). The gradient-flow structure guarantees monotone descent and exponential convergence.
- **Scale action:** All-scale. The free energy involves both the potential energy integral rho V dx (large-scale, governed by V) and the entropic energy sigma^2 integral rho log rho dx (all-scale, penalizing concentration).

**Channel P is conditional:** It exists only for gradient drifts (b = -nabla V). For non-gradient drifts, no Lyapunov functional is available, and the dynamics may circulate rather than converge. However, even without Channel P, the FP dynamics are *still linear*, *still well-posed*, and *still non-chaotic*. Channel P adds convergence guarantees but is not needed for closure.

### Channel Summary Table

| Channel | Symbol | Term                    | Locality | Linearity  | Stability       | Scale Action    |
|---------|--------|-------------------------|----------|------------|-----------------|-----------------|
| Transport   | T  | -div(b rho)            | Local    | Linear     | b-dependent     | Rate ~ \|b\| k |
| Diffusion   | D  | div(D nabla rho)       | Local    | Linear     | Stabilizing     | Rate ~ D k^2   |
| Conservation| C  | integral rho = 1       | Global*  | Linear     | Constraining    | All-scale       |
| Potential   | P  | F[rho], dF/dt <= 0    | Global** | Nonlinear*** | Stabilizing  | All-scale       |

*Locally enforced. **F is global; PDE is local. ***F is nonlinear in rho (entropy term); PDE is linear.

### Channel Count Comparison

| Architecture | Dynamical Channels | Constraint | Geometric | Gradient-flow | Total |
|-------------|-------------------|------------|-----------|---------------|-------|
| **FP**      | **2 (T, D)**      | **1 (C)**  | **0**     | **1 (P, cond.)**| **3+1** |
| PME         | 1 (D_nl)          | 1 (C)      | 1 (G)     | 1 (entropy)   | 3+1   |
| TFE         | 1 (D_4)           | 1 (C)      | 1 (G)     | 1 (E)         | 3+1   |
| AC          | 2 (R, S)          | 0           | 0         | 1 (F)         | 2+1   |
| CH          | 2 (R, S)          | 1 (D)      | 0         | 1 (F)         | 3+1   |
| NS          | 2 (A, V)          | 1 (C)      | 1 (P)    | 0             | 4+0   |

The FP has the *same total channel count* (3+1) as PME, TFE, and CH. But its channel *types* are unique: it is the only architecture with both a first-order transport channel and a second-order diffusion channel acting on the same field. All other architectures have either pure diffusion (AC, CH, PME, TFE) or reaction + diffusion (RD) or nonlinear advection + diffusion (NS).

---

## 2. Dissipation Geometry

### 2.1 The Free-Energy Functional (Gradient Drift)

For b = -nabla V with constant isotropic diffusion D = sigma^2 I:

    F[rho] = integral rho V dx + sigma^2 integral rho log rho dx

This is the sum of:
- **Potential energy:** integral rho V dx = <V>_rho. Measures the average potential energy of the particle ensemble. Minimized when rho concentrates at the minimum of V.
- **Entropic energy:** sigma^2 integral rho log rho dx = sigma^2 H[rho]. Measures the "disorder" of the distribution. Minimized when rho is as spread out as possible (maximum entropy = uniform distribution, if the domain is bounded).

The equilibrium rho_eq = Z^{-1} exp(-V/sigma^2) balances these two competing tendencies: potential energy drives concentration; entropy drives spreading. The balance point is the Gibbs–Boltzmann distribution.

### 2.2 The Dissipation Metric: Fisher Information

The dissipation rate is:

    dF/dt = -I[rho | rho_eq] / sigma^2

where:

    I[rho | rho_eq] = integral rho |nabla log(rho / rho_eq)|^2 dx

is the *Fisher information* of rho relative to rho_eq. The Fisher information measures the "roughness" of the density ratio rho/rho_eq — it is large when rho deviates sharply from equilibrium and zero when rho = rho_eq.

The Fisher information is the FP analogue of:
- AC: M ||mu||^2 (squared chemical potential, L^2 norm).
- CH: M ||nabla mu||^2 (squared chemical potential gradient, H^{-1} norm).
- PME: (4m/(m-1)) ||nabla(u^{(m+1)/2})||^2 (gradient of a power of u).
- TFE: integral h^n |nabla Delta h|^2 dx (weighted gradient of pressure).

Each architecture dissipates a different functional — the specific form is determined by the gradient-flow metric:

| Architecture | Gradient-flow metric | Dissipation functional           |
|-------------|---------------------|----------------------------------|
| AC          | L^2                 | ||mu||^2 = ||delta F / delta phi||^2 |
| CH          | H^{-1}             | ||nabla mu||^2                   |
| PME         | Wasserstein         | ||nabla(u^{(m+1)/2})||^2        |
| TFE         | Weighted H^{-1}     | integral h^n |nabla Delta h|^2   |
| **FP**      | **Wasserstein**     | **I[rho \| rho_eq] (Fisher info)**|

FP and PME share the Wasserstein metric but dissipate different functionals (Fisher information for FP, gradient-power norm for PME). The Fisher information is the *information-theoretic* dissipation functional — it measures the statistical distinguishability of rho from rho_eq, and its decay is the FP version of the H-theorem.

### 2.3 The Linear Dissipation Geometry

The FP dissipation geometry is *qualitatively different* from all other architectures because the PDE is linear:

- **All other architectures:** The dissipation functional is a *nonlinear* function of the state (mu depends nonlinearly on phi in AC/CH; the PME dissipation involves u^{(m+1)/2}). The dissipation landscape is curved — the dissipation rate depends nonlinearly on the distance from equilibrium.

- **FP:** The PDE is linear, so the *dynamics* are linear (even though the free energy F is nonlinear in rho). The dissipation rate I[rho | rho_eq] is a quadratic functional of the deviation rho - rho_eq when measured in the right coordinates (log(rho/rho_eq)). The dissipation landscape, viewed in logarithmic coordinates, is *quadratic* — the simplest possible dissipation geometry.

This quadratic structure is why the log-Sobolev inequality (H <= (1/(2 lambda)) I) and the Poincare inequality (||rho - rho_eq||^2 <= (1/lambda_1) I) produce *exponential* convergence: a quadratic Lyapunov functional with a quadratic dissipation rate gives Gronwall-type exponential decay. In nonlinear architectures, the dissipation is not quadratic, and the convergence is typically algebraic (power-law).

---

## 3. Constraint Surface Geometry

### 3.1 Three Geometric Regions

**Region A: Interior (rho > 0, strictly parabolic)**

Where rho is bounded away from zero, the FP equation is a *uniformly parabolic linear PDE* with smooth coefficients. The dynamics are:
- Real-analytic: rho is a real-analytic function of (x, t) for t > 0.
- Spectrally decomposable: rho can be expanded in eigenfunctions of the FP operator.
- Exponentially convergent (for confining gradient drift): each eigenmode decays at rate lambda_k.

The interior region is the *entire domain* for non-degenerate diffusion: since D > 0 everywhere, the equation is uniformly parabolic everywhere. There is no degenerate boundary layer (unlike PME/TFE) and no free boundary.

**Region B: Tails (rho small but positive)**

At large |x| (on R^d), rho is small but strictly positive (by the infinite-speed propagation property). For confining drift, the equilibrium tails decay as:

    rho_eq(x) ~ exp(-V(x) / sigma^2)    as |x| → infinity

Solutions rho(t) approach this tail behavior exponentially fast. The tails are *Gaussian-type* (for quadratic V) or *sub-Gaussian/super-Gaussian* (for sub-/super-quadratic V).

The tail region presents no structural difficulty: the solution is smooth, positive, and exponentially controlled.

**Region C: Equilibrium Basin (b = -nabla V confining)**

When V is confining and convex, the entire function space {rho >= 0, integral rho = 1} is a *single convex basin* of the free energy F. Every initial density rho_0 lies in this basin, and the dynamics flow monotonically toward the unique minimum rho_eq. There are no metastable states, no saddle points of F, and no energy barriers — the free-energy landscape is globally convex.

For non-convex V (with multiple local minima), the free-energy landscape has multiple basins, separated by saddle points. The dynamics still converge to rho_eq (the unique global minimum for sigma > 0), but the convergence may be slow (exponentially long trapping in metastable wells). This metastability is the *only source of slow dynamics* in the gradient FP equation.

### 3.2 Full Closure of the Constraint Surface

The FP constraint surface is *fully closed* for all choices of b and D (positive definite). The closure is established face by face:

**Positivity face: Closed.** The linear parabolic maximum principle ensures rho >= 0 for all time if rho_0 >= 0. No external mechanism (degeneracy, entropy, fourth-order smoothing) is needed — the linearity and parabolicity alone suffice.

**Mass face: Closed.** The divergence form of the PDE ensures integral rho = 1 for all time. Automatic from the conservation structure.

**Oscillatory face: Closed.** For gradient drift: the Lyapunov functional F forbids limit cycles. For non-gradient drift: the linearity of the PDE prevents nonlinear oscillations. Linear rotation of rho around a drift cycle is not a dynamical oscillation — it is a deterministic transport that preserves all norms.

**Chaotic face: Closed.** The PDE is linear. Linear semigroups cannot exhibit sensitive dependence on initial conditions. The solution operator is a bounded linear map — nearby initial data produce nearby solutions for all time.

**Blowup face: Closed.** Linear parabolic PDEs with smooth bounded coefficients have global smooth solutions. No nonlinear amplification mechanism exists. The L^{infinity} norm of rho is controlled by the maximum principle and the conservation constraint.

**Degeneracy face: N/A (no degeneracy).** D is positive definite everywhere. No free boundary, no compact support, no degenerate boundary layer. This face simply does not exist in the FP architecture.

**Nonlocal face: Closed (absent).** All channels are local. No Poisson equation, no Green's function, no integral constraint requiring a global solve.

### 3.3 Unconditional Parameter-Independence of Closure

The FP closure is *unconditionally parameter-independent*: it holds for *every* choice of b(x) and D(x) (with D positive definite), without any condition on the specific form, magnitude, or structure of the drift and diffusion fields.

This is unique in the Atlas:
- PME: closed for all m > 1 (parameter-independent within the PME class).
- TFE: closed for n >= 1 but open for 0 < n < 1 (parameter-dependent).
- RD: closure depends on the reaction kinetics (constitutive-dependent).
- NS: open in 3D regardless of parameters (architecturally dependent).

The FP closure is parameter-independent because the closure mechanism is *linearity itself* — and the PDE is linear for every choice of b and D. Linearity is not a constitutive property; it is a *structural* property of the FP class. Therefore, the closure holds structurally, not constitutively.

---

## 4. Anomalies and Open Faces

### 4.1 Zero Anomalies

The FP architecture has *zero* structural anomalies:

| Potential Anomaly              | FP Status                              |
|-------------------------------|----------------------------------------|
| Nonlocal channel              | Absent. All channels local.            |
| Destabilizing sub-channel     | Absent. Drift is linear; diffusion stabilizing. |
| Oscillatory face              | Closed. Linearity prevents nonlinear oscillation. |
| Chaotic face                  | Closed. Linear semigroup, no sensitive dependence. |
| Blowup face                   | Closed. Linear PDE, maximum principle. |
| Degeneracy face               | Absent. D > 0 everywhere.             |
| Positivity face               | Closed. Linear maximum principle.      |
| Pattern-formation face         | Absent. No reaction, single species.   |

**No anomaly of any type is present in the FP architecture.** This is the strongest anomaly-free verdict in the Atlas — not just "zero anomalies for specific parameters" (as in PME for m > 1 or TFE for n >= 1) but "zero anomalies for *all* parameters."

### 4.2 Comparison of Anomaly Profiles

| Architecture | Anomalies (count)  | Parameter-dependent? | Closure mechanism  |
|-------------|--------------------|-----------------------|-------------------|
| ED          | 0                  | N/A (static)          | Unique factorization |
| **FP**      | **0**              | **No (all parameters)** | **Linearity**   |
| PME         | 0                  | No (all m > 1)        | Degeneracy + entropy + L^1 + cons. |
| AC          | 0                  | No (all d <= 3)       | Max. principle + Lyapunov |
| CH          | 0                  | No (all d <= 3)       | 4th-order + Lyapunov |
| TFE         | 0 (n>=1) / 1 (n<1)| Yes (n-dependent)     | 4th-order + degeneracy + cons. |
| NS          | 2                  | No (architectural)    | Viscosity (insufficient 3D) |
| RD          | 0 (class) / 3+ (instances) | Yes (constitutive) | None universal |

The FP is one of only five architectures (ED, FP, PME, AC, CH) with *unconditionally zero anomalies*. Among these five, FP achieves its closure through the *simplest mechanism* (linearity), while the others require nonlinear structural features.

---

## 5. Channel Constraints

---

**C1. Linear Parabolicity**

    The FP equation is a linear second-order parabolic PDE with prescribed coefficients b(x), D(x).
    No nonlinear terms. Superposition principle holds.

*Scope: All FP systems.*

---

**C2. Drift–Diffusion Decomposition**

    partial_t rho = [-div(b rho)] + [div(D nabla rho)] = T(rho) + D(rho)

The evolution is the sum of a first-order transport and a second-order diffusion, each linear in rho.

*Scope: All FP systems.*

---

**C3. Positivity Preservation**

    rho_0 >= 0  =>  rho(t) >= 0    for all t >= 0

Linear parabolic maximum principle. Unconditional for all b, D (D positive definite).

*Scope: All FP systems.*

---

**C4. Probability Conservation**

    integral rho(x, t) dx = 1    for all t >= 0

Exact identity. Follows from divergence form + no-flux boundary conditions.

*Scope: All FP systems.*

---

**C5. Gaussian Smoothing**

    ||nabla^k rho(t)||_{L^2} <= C_k t^{-k/2} ||rho_0||_{L^2}    for t > 0

Instantaneous analytic regularization. Solutions become real-analytic for t > 0.

*Scope: All FP systems with smooth b, D.*

---

**C6. Entropy Dissipation (H-Theorem, Gradient Drift)**

    d/dt H[rho | rho_eq] = -I[rho | rho_eq] <= 0

The relative entropy decreases at rate equal to the Fisher information.

*Scope: Gradient drift (b = -nabla V) with confining V.*

---

**C7. Fisher-Information Dissipation**

    I[rho | rho_eq] = integral rho |nabla log(rho/rho_eq)|^2 dx = -dH/dt

The Fisher information is the dissipation rate of the relative entropy. It measures the statistical roughness of rho relative to equilibrium.

*Scope: Gradient drift with confining V.*

---

**C8. Exponential Convergence (Spectral Gap)**

    ||rho(t) - rho_eq||_{L^2(rho_eq^{-1})} <= exp(-lambda_1 t) ||rho_0 - rho_eq||_{L^2(rho_eq^{-1})}

Exponential L^2 convergence at the spectral gap rate lambda_1 > 0.

*Scope: Confining drift with spectral gap.*

---

**C9. Wasserstein Contractivity (Convex V)**

    W_2(rho_1(t), rho_2(t)) <= exp(-lambda t) W_2(rho_1(0), rho_2(0))

Exponential contraction in the Wasserstein-2 metric. The strongest stability property.

*Scope: b = -nabla V with Hess V >= lambda I, lambda > 0.*

---

**C10. No Oscillations**

    Gradient drift: dF/dt <= 0 => no limit cycles.
    Non-gradient drift: linearity => no nonlinear oscillations. Linear rotation only.

*Scope: All FP systems.*

---

**C11. No Blowup**

    ||rho(t)||_{L^{infinity}} bounded for all t > 0.

Linear parabolic PDEs with smooth bounded coefficients have global smooth solutions.

*Scope: All FP systems with smooth b, D.*

---

**C12. Unique Equilibrium (Confining Gradient Drift)**

    rho_eq = Z^{-1} exp(-V / sigma^2)    is the unique stationary probability density.

All solutions converge to rho_eq. The equilibrium is explicit, unique, and globally attracting.

*Scope: b = -nabla V with V confining.*

---

### Channel Constraint Summary

| Label | Constraint                        | Type              | Scope            |
|-------|-----------------------------------|-------------------|------------------|
| C1    | Linear parabolicity               | Structural        | All FP           |
| C2    | Drift-diffusion decomposition     | Structural        | All FP           |
| C3    | Positivity preservation           | Max. principle    | All FP           |
| C4    | Probability conservation          | Exact identity    | All FP           |
| C5    | Gaussian smoothing                | Analytic regular. | All FP (smooth b,D) |
| C6    | Entropy dissipation               | Exact identity    | Gradient drift   |
| C7    | Fisher-info dissipation           | Exact identity    | Gradient drift   |
| C8    | Exponential convergence           | Spectral          | Confining drift  |
| C9    | Wasserstein contractivity         | Contraction       | Convex V         |
| C10   | No oscillations                   | Linearity         | All FP           |
| C11   | No blowup                        | Linearity         | All FP           |
| C12   | Unique equilibrium                | Variational       | Confining V      |

**Six of twelve constraints (C1–C5, C10, C11) hold unconditionally for all FP systems.** The remaining six (C6–C9, C12) require gradient drift with confining potential — the sub-class with the richest structure.

---

## 6. Comparison with AC, CH, PME, TFE, RD, and NS

### 6.1 Closure Comparison

| Architecture | Surface Closure   | Mechanism                           | Parameter-Independent? |
|-------------|-------------------|-------------------------------------|------------------------|
| **FP**      | **Fully closed**  | **Linearity**                      | **Yes (all b, D)**     |
| PME         | Fully closed      | Degeneracy + entropy + L^1 + cons.  | Yes (all m > 1)        |
| AC          | Fully closed      | Max. principle + Lyapunov           | Yes (d <= 3)           |
| CH          | Fully closed      | 4th-order smooth. + Lyapunov        | Yes (d <= 3)           |
| TFE         | n-dependent       | 4th-order + degeneracy + cons.      | No (open for n < 1)    |
| NS          | Open (3D)         | Viscosity                           | No (arch. gap in 3D)   |
| RD          | Constitutive      | None universal                      | No (class-level only)  |

FP is the *only dynamical PDE* whose closure is unconditional across all constitutive parameters. (ED is also unconditionally closed, but it is static.) PME, AC, and CH are unconditionally closed within their respective parameter classes but have dimensional or parameter restrictions. TFE, NS, and RD have parameter-dependent or architecturally open surfaces.

### 6.2 Channel Structure Comparison

| Feature                    | FP          | AC    | CH    | PME   | TFE   | NS    | RD          |
|----------------------------|-------------|-------|-------|-------|-------|-------|-------------|
| Channel types              | T + D       | R + S | R + S + D | D_nl | D_4 | A + V | D + R       |
| First-order channel        | **T (drift)** | No | No    | No    | No    | A (self-adv.)| No       |
| Linearity                  | **Linear**  | NL    | NL    | NL    | NL    | NL    | NL          |
| Conservation               | Prob (=1)   | No    | Yes   | Yes   | Yes   | Yes   | Constitutive|
| Free boundary              | No          | No    | No    | Yes   | Yes   | No    | Constitutive|
| Gradient-flow              | Wass. (cond.)| L^2  | H^{-1}| Wass.| Wt.H^{-1}| No | Gen. no   |
| Closure mechanism          | Linearity   | Max.pr.| 4th-ord.| Degen.| 4th+degen.| Visc.| None univ.|

### 6.3 The Linearity Axis

The PDE Atlas can be organized along a *linearity axis*:

    FP (linear) ←──── AC/CH/PME/TFE (nonlinear, gradient flow) ←──── RD/NS (nonlinear, no Lyapunov)

Moving from left to right:
- **FP (linear):** Complete analytical tractability. Spectral decomposition. Superposition. No chaos, no patterns, no turbulence. The *simplest* dynamics.
- **AC/CH/PME/TFE (nonlinear gradient flow):** Monotone descent. No chaos, no oscillations, but complex geometry (interfaces, free boundaries, coarsening, spreading). *Intermediate* dynamics.
- **RD/NS (nonlinear, non-gradient):** Oscillations, patterns, chaos, turbulence possible. The *richest* dynamics but the *weakest* structural control.

FP is at the extreme left of this axis: maximum analytical control, minimum dynamical richness. RD/NS are at the right: minimum analytical control, maximum dynamical richness. The gradient-flow architectures sit in between, trading some dynamical richness for structural guarantees.

### 6.4 FP as the Stochastic Mirror of ED

The FP and ED architectures are structurally *parallel*:

| Feature                    | ED                         | FP                           |
|----------------------------|----------------------------|------------------------------|
| Domain                     | Discrete (integers)        | Continuous (R^d)             |
| State variable             | Event density              | Probability density          |
| Dynamics                   | Static (fixed structure)   | Dynamic (drift + diffusion)  |
| Attractor                  | Arithmetic distribution    | Gibbs–Boltzmann              |
| Generating mechanism       | Unique factorization       | SDE + Markov property        |
| Linearity                  | Linear (in distributional sense) | **Linear** (PDE)       |
| Locality                   | Fully local                | Fully local                  |
| Closure                    | Unconditional              | **Unconditional**            |
| Anomalies                  | 0                          | **0**                        |

Both architectures distribute a density across a space, both produce universal equilibrium distributions, both are fully local, both are unconditionally closed, and both are anomaly-free. The FP equation is the *dynamical, continuous, stochastic* realization of the density-distribution concept that ED embodies statically and arithmetically. Of all PDEs in the Atlas, FP is structurally closest to ED.

---

*End of Mode 3: Channels → Constraint Surface. The AD Criteria and Verdict will follow in the final file.*
