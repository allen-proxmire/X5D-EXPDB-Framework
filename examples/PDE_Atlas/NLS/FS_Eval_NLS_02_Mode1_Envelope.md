# AD Evaluation: Nonlinear Schrödinger Equation — Mode 1: Axiom → Envelope

Allen Proxmire

April 2026

---

## Overview

Mode 1 traces the path from the NLS axioms (NLS-1 through NLS-10) to the architectural envelope. The NLS envelope is *structurally unprecedented* in the PDE Atlas: it is the first envelope sealed not by dissipation, not by entropy, not by convex variational structure, but by *conservation laws + dispersive estimates*. The NLS has three exact conservation laws (mass, energy, momentum) and a family of *Strichartz inequalities* that control the solution in space-time norms through the dispersive spreading of the linear flow. These tools — conservative rather than dissipative, oscillatory rather than monotone — provide a closure mechanism that is qualitatively new: **dispersive Hamiltonian closure**.

The NLS envelope also introduces the *focusing/defocusing dichotomy* as a structural bifurcation. Where NS has a 2D/3D dimensional bifurcation and TFE has an n-dependent parametric bifurcation, the NLS has a *sign bifurcation*: the sign of the nonlinearity (±|psi|^2 psi) determines whether the architecture is globally well-posed (defocusing) or admits finite-time blowup (focusing, d >= 2). The sign is a single bit of structural information — the most economical bifurcation parameter possible.

Throughout:

    i partial_t psi + Delta psi ± |psi|^2 psi = 0

on R^d, with psi : R^d x R → C. The + sign is defocusing; the - sign is focusing.

---

## 1. Forbidden Configurations

### F1. Diffusive Smoothing

**Axiom source:** NLS-3 (Dispersive Core), NLS-9 (No Diffusion).

The NLS time derivative is i partial_t psi — imaginary, not real. The linear propagator e^{it Delta} is a *unitary group* on L^2, not a contraction semigroup. It preserves the L^2 norm exactly and does not damp any mode:

    ||e^{it Delta} psi_0||_{L^2} = ||psi_0||_{L^2}    for all t

There is no smoothing in the parabolic sense: initial data in H^s remains in H^s — regularity is neither gained nor lost. The NLS does not convert rough data to smooth data (as the heat equation does). The Sobolev regularity of the solution is *exactly preserved*, not improved.

Diffusive smoothing — the instantaneous C^{infinity} regularization that every parabolic architecture provides — is axiomatically forbidden. The NLS is structurally incapable of smoothing.

### F2. Irreversible Decay

**Axiom source:** NLS-5 (Hamiltonian), NLS-9 (No Diffusion).

The NLS is time-reversible: if psi(x, t) solves NLS, then psi*(x, -t) also solves NLS. There is no preferred time direction, no arrow of time, no monotone quantity that distinguishes past from future.

Irreversible decay — a quantity that decreases monotonically and cannot increase — is forbidden. The NLS has no Lyapunov functional in the parabolic sense:
- Energy H is *conserved* (not decreasing).
- Mass M is *conserved* (not decreasing).
- No scalar functional exists that is monotonically decreasing along all trajectories.

The gradient-flow architectures (AC, CH, PME, TFE) all have Lyapunov functionals; the entropy-producing architectures (HJ, Burgers) have irreversible entropy production at shocks; the linear architecture (FP) has monotone entropy decay. The NLS has *none of these*. It is the only architecture in the Atlas where every trajectory is time-reversible.

### F3. Shock Formation (Burgers/HJ Type)

**Axiom source:** NLS-3 (Dispersive), NLS-8 (Cubic Nonlinearity).

The NLS is not a conservation law in the Burgers/HJ sense — it does not have the form partial_t v + partial_x f(v) = 0. The NLS nonlinearity is *algebraic* (|psi|^2 psi, no derivatives) rather than *transport-type* (v v_x, involving a derivative). The NLS cannot develop the *gradient steepening* that leads to Burgers shocks or HJ kinks.

When the focusing NLS does blow up (in d >= 2), the singularity is *concentration* (|psi| → infinity at a point) rather than *steepening* (nabla psi developing a discontinuity). The blowup mechanism is fundamentally different from the hyperbolic architectures: NLS concentrates amplitude; HJ/Burgers steepens gradients.

### F4. Finite-Speed Propagation

**Axiom source:** NLS-3 (Dispersive Core).

The free Schrödinger propagator e^{it Delta} has *infinite-speed propagation*: for any compactly supported psi_0, the solution e^{it Delta} psi_0 is nonzero everywhere for any t ≠ 0. The dispersive spreading is instantaneous — information reaches all of R^d immediately (though with rapidly decaying amplitude at large distances).

Finite-speed propagation — the characteristic-cone structure of HJ/Burgers, or the compact-support preservation of PME/TFE — is forbidden. The NLS is *non-hyperbolic*: it has infinite propagation speed (like the parabolic architectures) but without the diffusive decay that accompanies parabolic infinite speed.

### F5. Entropy Production

**Axiom source:** NLS-5 (Hamiltonian), NLS-9 (No Diffusion).

The NLS produces no entropy. The evolution is a symplectic flow on the phase space of (psi, psi*) — it preserves phase-space volume (Liouville's theorem) and produces no irreversibility. There is no second law, no H-theorem, no entropy functional that increases.

Entropy production — the irreversible creation of disorder, present in every dissipative architecture (FP, PME, AC/CH/TFE) and at shocks in hyperbolic architectures (HJ, Burgers) — is axiomatically forbidden.

### F6. Mass Loss

**Axiom source:** NLS-4 (Gauge Invariance), NLS-6 (Mass Conservation).

The L^2 norm ||psi(t)||_{L^2}^2 = M is exactly conserved. No mechanism in the NLS can create or destroy mass. The unitary evolution preserves the L^2 norm by construction — the operator i partial_t + Delta is skew-adjoint on L^2, and skew-adjoint operators generate isometries.

### F7. Energy Dissipation

**Axiom source:** NLS-5 (Hamiltonian).

The energy H[psi] = integral [|nabla psi|^2 ± (1/2)|psi|^4] dx is exactly conserved: dH/dt = 0. No mechanism can transfer energy from the wave field to "heat" or to an external reservoir. Energy dissipation is structurally impossible.

### F8. Nonlocal Forcing

**Axiom source:** NLS-2 (Locality), NLS-10 (No Reaction).

The NLS has no external potential V(x), no forcing term f(x,t), and no nonlocal coupling. The evolution is autonomous and fully local. Adding an external potential (i psi_t + Delta psi + V(x) psi ± |psi|^2 psi = 0) extends the architecture but is outside the canonical NLS.

### F9. Turing-Type Pattern Formation

**Axiom source:** NLS-1 (Complex Scalar), NLS-10 (No Reaction).

The NLS has one species (psi), no reaction terms, and no diffusion. Turing instability requires at least two species with differential diffusion and reaction coupling. Pattern-forming instabilities of the reaction-diffusion type are structurally absent.

The NLS *can* form patterns through *modulational instability* (a dispersive phenomenon), but these are qualitatively different from Turing patterns: they arise from the focusing nonlinearity destabilizing a constant-amplitude background, not from reaction-diffusion coupling.

### F10. Classical Parabolic Regularization

**Axiom source:** NLS-3, NLS-9.

The NLS does not gain regularity over time. Initial data in H^s(R^d) produces solutions in H^s(R^d) — the Sobolev index s is *preserved*, not improved. There is no instantaneous C^{infinity} regularization, no analytic regularization, no smoothing estimate of the form ||nabla^k psi(t)|| <= C t^{-k/2} ||psi_0|| (which would require decay, not conservation, of the L^2 norm).

The NLS solution at time t is *exactly as regular* as the initial data — no more, no less. This is the structural consequence of unitary evolution: the propagator is an isometry on H^s, not a contraction.

### Summary of Forbidden Configurations

| Label | Forbidden Configuration               | Excluding Axiom(s)        |
|-------|---------------------------------------|---------------------------|
| F1    | Diffusive smoothing                   | NLS-3, NLS-9              |
| F2    | Irreversible decay (Lyapunov)         | NLS-5, NLS-9              |
| F3    | Shock / gradient blowup               | NLS-3, NLS-8              |
| F4    | Finite-speed propagation              | NLS-3                     |
| F5    | Entropy production                    | NLS-5, NLS-9              |
| F6    | Mass loss                             | NLS-4, NLS-6              |
| F7    | Energy dissipation                    | NLS-5                     |
| F8    | Nonlocal forcing                      | NLS-2, NLS-10             |
| F9    | Turing-type patterns                  | NLS-1, NLS-10             |
| F10   | Parabolic regularization              | NLS-3, NLS-9              |

---

## 2. Necessary Configurations

### N1. Complex-Valued Field with U(1) Gauge Symmetry

**Source:** NLS-1, NLS-4.

The state psi is complex-valued, and the NLS is invariant under psi → e^{i theta} psi. The gauge symmetry generates mass conservation via Noether's theorem. The complex character couples the "amplitude" |psi| and "phase" arg(psi) into a single dynamical object that cannot be decomposed into independent real equations.

### N2. Dispersive Core (Free Schrödinger Propagator)

**Source:** NLS-3.

The linear part i psi_t + Delta psi = 0 generates the free Schrödinger group e^{it Delta}, which:
- Is unitary on L^2: preserves ||psi||_{L^2}.
- Has dispersive decay: ||e^{it Delta} f||_{L^{infinity}} <= C |t|^{-d/2} ||f||_{L^1}.
- Spreads wave packets: the variance integral |x|^2 |psi|^2 dx grows as t^2 for large t.
- Does not smooth: H^s regularity is preserved, not gained.

The dispersive decay ||psi(t)||_{L^{infinity}} ~ t^{-d/2} is the NLS analogue of the diffusive decay ||u(t)||_{L^{infinity}} ~ t^{-d/2} in the heat equation — both have the *same rate* — but the mechanism is different: the heat equation decays through energy dissipation; the Schrödinger equation decays through phase cancellation (interference of rapidly oscillating components). The L^{infinity} norm decreases not because energy is lost but because it is *spread* over an increasing volume.

### N3. Hamiltonian Structure

**Source:** NLS-5.

The NLS is a Hamiltonian PDE: i psi_t = delta H / delta psi*, with:

    H[psi] = integral [|nabla psi|^2 ± (1/2)|psi|^4] dx

The Hamiltonian structure implies:
- dH/dt = 0 (energy conservation).
- The flow is symplectic (preserves the symplectic form omega = Im integral delta psi* wedge delta psi dx).
- Time-reversibility: psi(t) ↔ psi*(-t).
- No attractors in the conventional sense (Hamiltonian flows preserve phase-space volume and cannot contract to lower-dimensional sets).

### N4. Mass Conservation

**Source:** NLS-4, NLS-6.

    M = ||psi(t)||_{L^2}^2 = ||psi_0||_{L^2}^2    for all t

Exact L^2 conservation. The mass M is the primary invariant — it is the *scaling-critical quantity* in d = 2 (for the cubic NLS) and controls the blowup/global existence threshold in the focusing case.

### N5. Momentum Conservation

**Source:** NLS-7.

    P = Im integral psi* nabla psi dx = const

Exact momentum conservation. The momentum P determines the center-of-mass velocity of the wave packet. It is the second Noether invariant (from translation invariance), after mass (from gauge invariance).

### N6. Focusing/Defocusing Dichotomy

**Source:** NLS-8.

The sign of the nonlinearity determines the qualitative dynamics:

**Defocusing (+):** H = integral [|nabla psi|^2 + (1/2)|psi|^4] dx >= 0. The energy is positive definite. Combined with mass conservation:

    ||nabla psi(t)||_{L^2}^2 <= H[psi_0]    for all t

This gives uniform-in-time H^1 control → global well-posedness in d <= 3 (subcritical or critical). No blowup possible.

**Focusing (-):** H = integral [|nabla psi|^2 - (1/2)|psi|^4] dx. The energy can be negative. The H^1 norm is *not* controlled by the energy alone — the kinetic and potential energies can exchange without bound. In d >= 2, this permits finite-time blowup: ||nabla psi(t)||_{L^2} → infinity at some T* < infinity.

The dichotomy is architecturally analogous to:
- NS: 2D (global regularity) vs. 3D (open). Parameter: dimension d.
- TFE: n >= 1 (positivity preserved) vs. n < 1 (open). Parameter: mobility exponent n.
- **NLS: defocusing (global) vs. focusing (blowup possible, d >= 2). Parameter: sign ±.**

### N7. Time-Reversibility

**Source:** NLS-5, NLS-9.

If psi(x, t) solves NLS, then psi*(x, -t) solves NLS. The dynamics have no intrinsic arrow of time. This is a *necessary consequence* of the Hamiltonian structure (conservative, symplectic, no dissipation).

Time-reversibility is *unique to NLS* in the Atlas. Every other architecture is either irreversible (parabolic: AC, CH, PME, TFE, FP dissipate energy; MCF decreases area) or entropy-producing (HJ, Burgers produce entropy at shocks). The NLS is the *only reversible PDE* in the Atlas.

### N8. Dispersive Spreading

**Source:** NLS-3.

For the linear flow, the L^{infinity} norm decays as t^{-d/2}:

    ||e^{it Delta} f||_{L^{infinity}} <= C |t|^{-d/2} ||f||_{L^1}

This *dispersive estimate* is the key analytical tool for the NLS. It controls the nonlinearity: the cubic term |psi|^2 psi is bounded by ||psi||_{L^{infinity}}^2 ||psi||_{L^2}, and if ||psi||_{L^{infinity}} decays as t^{-d/2}, the nonlinearity becomes *integrable in time* for d >= 2 — enabling the solution to *scatter* (approach a free solution as t → infinity).

### N9. Solitons and Standing Waves

**Source:** NLS-3, NLS-8 (focusing).

The focusing NLS admits *soliton* solutions — localized, shape-preserving traveling waves:

    psi(x, t) = e^{i omega t} Q(x)

where Q solves the *elliptic ground-state equation*:

    -Delta Q + omega Q - |Q|^2 Q = 0,    Q > 0

The ground state Q (unique up to symmetry for given omega) is the *critical object* for the focusing NLS: its mass M_* = ||Q||_{L^2}^2 is the *threshold mass* in d = 2 — blowup occurs if and only if M > M_* (the Weinstein sharp Gagliardo–Nirenberg inequality).

Solitons are *unique to the NLS* in the Atlas. No other architecture has localized, shape-preserving, non-decaying solutions. Solitons arise from the *exact balance* between dispersion (which spreads the wave packet) and focusing nonlinearity (which concentrates it). This balance is a *dispersive* phenomenon with no analogue in parabolic or hyperbolic architectures.

### N10. Criticality Structure

**Source:** NLS-3, NLS-8, scaling symmetry.

The cubic NLS has the scaling symmetry psi → lambda^{d/2} psi(lambda x, lambda^2 t), under which:

    ||psi_lambda||_{L^2} = ||psi||_{L^2}    [mass-preserving rescaling]

The *critical Sobolev space* is L^2 (in d = 2) — the space whose norm is invariant under the NLS scaling. The criticality structure:

- d = 1: **Subcritical.** The L^2 norm is *stronger* than needed for control. Global existence for all L^2 data (both focusing and defocusing). The 1D NLS is completely integrable (inverse scattering).
- d = 2: **L^2-critical.** The mass M = ||psi||_{L^2}^2 is the exact scaling-invariant quantity. Focusing blowup occurs iff M > M_* (ground-state mass). The threshold M_* is sharp.
- d = 3: **L^2-supercritical.** The mass is too weak to control the dynamics. Blowup can occur for arbitrarily small mass (large H^1 data). The energy H and additional profile information (variance, Morawetz quantities) are needed for global control.

### Summary of Necessary Configurations

| Label | Necessary Configuration                     | Source                |
|-------|---------------------------------------------|-----------------------|
| N1    | Complex field + U(1) gauge symmetry         | NLS-1, NLS-4          |
| N2    | Dispersive core (unitary, decay t^{-d/2})   | NLS-3                 |
| N3    | Hamiltonian structure (energy conserved)     | NLS-5                 |
| N4    | Mass conservation (L^2 norm)                | NLS-4, NLS-6          |
| N5    | Momentum conservation                       | NLS-7                 |
| N6    | Focusing/defocusing dichotomy               | NLS-8                 |
| N7    | Time-reversibility                          | NLS-5, NLS-9          |
| N8    | Dispersive spreading (t^{-d/2} linear decay)| NLS-3                 |
| N9    | Solitons (focusing, balance D vs. N)        | NLS-3, NLS-8          |
| N10   | Criticality (L^2-critical in d=2, cubic)    | NLS-3, NLS-8, scaling |

---

## 3. Envelope Inequalities (E1–E10)

---

**E1. Mass Conservation**

    ||psi(t)||_{L^2}^2 = ||psi_0||_{L^2}^2 = M    for all t

Exact identity. The L^2 norm is an exact invariant. This is the NLS's primary structural constraint — the analogue of integral v = const in Burgers and integral rho = 1 in FP. But the mechanism is different: Burgers conserves mass through flux divergence; FP through probability preservation; NLS through *unitary evolution* (the Schrödinger propagator is an isometry on L^2).

---

**E2. Energy Conservation**

    H[psi(t)] = integral [|nabla psi|^2 ± (1/2)|psi|^4] dx = H[psi_0]    for all t

Exact identity. The Hamiltonian is an exact invariant. This is the NLS's secondary constraint — the analogue of the Lyapunov identity dF/dt = -D in AC/CH/PME, but with a *crucial difference*: the NLS energy is *conserved* (dH/dt = 0), not *dissipated* (dF/dt <= 0). Conservation provides control (H bounds ||nabla psi||^2 in the defocusing case) but not monotonicity (H does not decrease toward a minimum).

---

**E3. Momentum Conservation**

    P[psi(t)] = Im integral psi* nabla psi dx = P[psi_0]    for all t

Exact identity. The third conservation law, from translational invariance.

---

**E4. Linear Dispersive Estimate**

    ||e^{it Delta} f||_{L^{infinity}} <= C |t|^{-d/2} ||f||_{L^1}

The free Schrödinger propagator maps L^1 to L^{infinity} with decay rate t^{-d/2}. This is the *fundamental dispersive estimate* — the NLS analogue of the heat-kernel bound ||e^{t Delta} f||_{L^{infinity}} <= (4 pi t)^{-d/2} ||f||_{L^1}. Both have the same rate t^{-d/2}, but the mechanisms differ: the heat kernel decays through energy dissipation; the Schrödinger kernel decays through phase cancellation.

The dispersive estimate is the *primary analytical tool* for controlling the nonlinear NLS. It is not a conservation law but a *spreading inequality* — it says that the L^{infinity} norm decreases (through spreading) even though the L^2 norm is conserved.

---

**E5. Strichartz Estimates**

For admissible pairs (q, r) satisfying 2/q + d/r = d/2:

    ||e^{it Delta} f||_{L^q_t L^r_x} <= C ||f||_{L^2}

and the inhomogeneous version:

    ||integral_0^t e^{i(t-s)Delta} F(s) ds||_{L^q_t L^r_x} <= C ||F||_{L^{q'}_t L^{r'}_x}

The Strichartz estimates control the solution in *mixed space-time norms* — they bound the L^q_t L^r_x norm by the L^2 norm of the initial data. These estimates are the *workhorse* of NLS well-posedness theory: they convert the dispersive decay (E4) into usable bounds for the nonlinear fixed-point argument.

The Strichartz estimates are the NLS analogue of the parabolic smoothing estimates (||nabla^k u(t)|| <= C t^{-k/2} ||u_0||) — both convert properties of the linear propagator into bounds on the nonlinear solution. But the Strichartz estimates are *weaker*: they control space-time integrals (not pointwise values) and require admissibility conditions on the exponents.

---

**E6. Local Well-Posedness in H^s**

For the cubic NLS on R^d with initial data psi_0 in H^s(R^d):

    s >= 0 (d = 1), s >= 0 (d = 2), s > 1/2 (d = 3)

there exists T > 0 and a unique solution psi in C([0, T]; H^s) with continuous dependence on psi_0. The local existence time T depends on ||psi_0||_{H^s}.

Local well-posedness is the *baseline* — it holds for both focusing and defocusing, in all dimensions, for sufficiently regular data. The NLS always has a short-time solution.

---

**E7. Global Well-Posedness (Defocusing)**

**Defocusing cubic NLS (+):**

- d = 1: Global in H^s for s >= 0 (complete integrability, inverse scattering).
- d = 2: Global in L^2 (mass + energy control + Gagliardo–Nirenberg).
- d = 3: Global in H^1 (energy + Morawetz estimates; the Colliander–Keel–Staffilani–Takaoka–Tao theorem for d = 3 energy-critical; for cubic d = 3 this is subcritical and follows from energy + Strichartz).

The defocusing case has *unconditional global well-posedness* in all physically relevant dimensions — the energy is positive definite and controls the H^1 norm, closing the bootstrap.

**Focusing cubic NLS (-):**

- d = 1: Global in L^2 (mass conservation alone suffices — the Gagliardo–Nirenberg inequality ||psi||_{L^4}^4 <= C ||psi||_{L^2}^2 ||nabla psi||_{L^2}^2 controls the nonlinearity with the available mass + energy).
- d = 2: Global iff M < M_* (mass below the ground-state threshold). Blowup iff M >= M_* (with additional conditions on the energy/variance).
- d = 3: Blowup possible for large data. Global existence for small H^1 data.

---

**E8. Blowup Criteria (Focusing, d >= 2)**

**Virial identity (Glassey):** Define the variance V(t) = integral |x|^2 |psi|^2 dx. Then:

    d^2 V/dt^2 = 8 H[psi] - (4d - 2d) integral |psi|^4 dx    [for cubic NLS]

For the focusing cubic NLS in d = 2:

    d^2 V/dt^2 = 8 H[psi]

If H < 0 (negative energy), then V''(t) = 8H < 0 → V(t) is concave → V(t) reaches zero in finite time → ||nabla psi(t)||_{L^2} → infinity (blowup). The virial identity provides a *sufficient condition for blowup*: negative energy implies finite-time singularity.

**Sharp threshold (d = 2, focusing):** Blowup occurs if and only if M > M_* = ||Q||_{L^2}^2 (Weinstein). The ground-state mass M_* is the *exact critical mass*. This is the sharpest blowup criterion in the Atlas — it identifies the *exact threshold* (not just a sufficient condition) for singularity formation.

---

**E9. Scattering (Defocusing)**

For the defocusing cubic NLS in d >= 3 (and in d = 2 with appropriate conditions):

    ||psi(t) - e^{it Delta} psi_+||_{H^1} → 0    as t → +infinity

for some asymptotic state psi_+ in H^1. The solution *scatters* — it approaches a *free solution* (solution of the linear Schrödinger equation) as t → infinity. The nonlinearity becomes negligible at large times because the dispersive spreading reduces ||psi||_{L^{infinity}} faster than the nonlinearity can act.

Scattering is the NLS's version of "convergence to equilibrium" — but the "equilibrium" is not a fixed point; it is a *free solution* (a linear dispersive wave). The solution does not settle down to a static state but rather approaches *linear dynamics* — the nonlinearity "turns off" asymptotically.

---

**E10. Critical Mass/Energy Thresholds**

**d = 2, focusing cubic NLS:**

    M < M_* = ||Q||_{L^2}^2    =>    global existence + scattering
    M = M_*                      =>    global existence (soliton is the unique optimizer)
    M > M_*                      =>    blowup possible (for appropriate energy/variance conditions)

The ground-state soliton Q is the *critical object*: it sits at the exact boundary between global existence and blowup. Its mass M_* is the *sharp threshold mass*. This is the most precise blowup/global-existence boundary in the entire PDE Atlas — sharper than the NS enstrophy gap (which is unresolved) and sharper than the TFE positivity boundary (which depends continuously on n).

**d = 3 and higher, focusing:**

The critical thresholds involve energy and other quantities (not just mass). The analysis uses the *concentration-compactness* machinery (Kenig–Merle) to identify the threshold between scattering and blowup.

---

### Envelope Summary

The NLS envelope is defined by ten constraints organized into three tiers:

**Tier 1 — Conservation Laws (exact, all NLS):**
- E1: Mass conservation (L^2 norm invariant).
- E2: Energy conservation (Hamiltonian invariant).
- E3: Momentum conservation.

**Tier 2 — Dispersive/Strichartz Control:**
- E4: Linear dispersive estimate (t^{-d/2} L^{infinity} decay).
- E5: Strichartz estimates (mixed space-time norms).
- E6: Local well-posedness in H^s.
- E9: Scattering (defocusing, d >= 3: solution → free linear flow).

**Tier 3 — Sign-Dependent (Focusing/Defocusing):**
- E7: Global well-posedness (defocusing: unconditional; focusing: conditional on mass/energy).
- E8: Blowup criteria (focusing, d >= 2: virial identity, negative energy).
- E10: Critical mass/energy thresholds (sharp, involving ground-state soliton).

### Closure Assessment

**Defocusing NLS (+):** The envelope is *fully closed*. The positive-definite energy (E2) controls the H^1 norm unconditionally. The Strichartz estimates (E5) provide the space-time control. Global well-posedness (E7) and scattering (E9) hold in all relevant dimensions. No blowup, no open questions. The defocusing envelope is as tight as the PME or FP envelope.

**Focusing NLS (-), d = 1:** The envelope is *fully closed*. Mass conservation alone suffices for global existence (the Gagliardo–Nirenberg inequality controls the nonlinearity). Complete integrability provides additional structure (inverse scattering, infinitely many conservation laws).

**Focusing NLS (-), d = 2:** The envelope is *closed at the sharp threshold*. The critical mass M_* provides an exact bifurcation: M < M_* → global; M > M_* → blowup possible. The threshold is *resolved* (not open, unlike NS 3D). The envelope has a *sharp boundary* rather than an *open face*.

**Focusing NLS (-), d >= 3:** The envelope is *partially open*. Blowup can occur for large data. The exact threshold between blowup and global existence depends on the energy, variance, and profile — the analysis is deep (Kenig–Merle concentration-compactness) but not fully resolved for all initial data. Some questions remain open (the complete classification of all blowup dynamics).

---

## 4. Central Architectural Finding

### 4.1 The Dispersive Hamiltonian Closure

The NLS envelope is sealed by a *new closure mode* — **dispersive Hamiltonian closure** — that is qualitatively different from every previous mode:

| Closure Mode              | Representative | Key Tools                        | Dissipation? |
|---------------------------|----------------|----------------------------------|-------------|
| Linear                    | FP             | Linearity + spectral theory      | Yes (entropic) |
| Dissipative               | PME            | Lyapunov + smoothing + contraction| Yes (entropy/energy) |
| Variational               | HJ             | Convexity + viscosity + Hopf–Lax | No (variational) |
| Entropic-contractive      | Burgers        | Convex flux + Kruzkov + L^1      | Yes (at shocks) |
| Geometric-dissipative     | MCF            | Area dissipation + Huisken monotonicity | Yes (geometric) |
| **Dispersive Hamiltonian**| **NLS**        | **Conservation laws + Strichartz + dispersive decay** | **No (conservative)** |

The NLS closure mode is *conservative*: it uses conservation laws (mass, energy, momentum) and *dispersive estimates* (Strichartz, linear decay) rather than dissipation or entropy. The solution is controlled not by tracking what *decreases* but by tracking what is *preserved* and what *spreads*.

### 4.2 The Focusing/Defocusing Dichotomy

The NLS is the *third* architecture with a structural bifurcation in the Atlas:

| Architecture | Bifurcation Parameter | Closed Side              | Open/Singular Side          |
|-------------|------------------------|--------------------------|------------------------------|
| NS          | Dimension d            | d = 2 (global regularity)| d = 3 (open)                |
| TFE         | Exponent n             | n >= 1 (positivity)      | n < 1 (positivity may fail) |
| **NLS**     | **Sign ±**             | **Defocusing (+): global**| **Focusing (-): blowup (d>=2)** |

The NLS bifurcation is the *most economical*: a single bit (sign ±) determines whether the architecture is globally well-posed or admits singularities. The NS bifurcation requires changing the dimension (d = 2 vs. 3); the TFE bifurcation requires varying a continuous parameter (n). The NLS bifurcation requires only *flipping a sign*.

### 4.3 NLS as the Dispersive Pole

The NLS completes the *three-pole structure* of the PDE Atlas:

    Diffusive pole: FP / PME / AC / CH / TFE    (smoothing, decay, Lyapunov)
    Hyperbolic pole: HJ / Burgers                (steepening, shocks, entropy)
    Dispersive pole: NLS                          (spreading, oscillation, Hamiltonian)

Each pole has its own:
- *Propagation mechanism:* diffusion (amplitude decay) / transport (characteristic flow) / dispersion (phase interference).
- *Closure mode:* Lyapunov dissipation / convex variational / dispersive Hamiltonian.
- *Singularity type:* none (diffusive) / shock/kink (hyperbolic) / concentration (dispersive).
- *Time direction:* irreversible (diffusive) / entropy-producing (hyperbolic) / *reversible* (dispersive).

The NLS is the *only representative* of the dispersive pole — the only architecture in the Atlas whose dynamics are governed by oscillatory spreading rather than monotone decay or gradient compression. Its inclusion completes the structural triangle of PDE dynamics.

### 4.4 Envelope Comparison

| Architecture | Envelope Status          | Closure Mode                | Singularity            |
|-------------|--------------------------|------------------------------|------------------------|
| ED          | Closed (static)          | Arithmetic                   | None                   |
| FP          | Closed (all params)      | Linear                       | None                   |
| PME         | Closed (all m > 1)       | Dissipative                  | None                   |
| HJ          | Closed (viscosity)       | Variational                  | Gradient kink (certain)|
| Burgers     | Closed (entropy)         | Entropic-contractive         | Shock (certain)        |
| AC          | Closed (d <= 3)          | Dissipative                  | None                   |
| CH          | Closed (d <= 3)          | Dissipative                  | None                   |
| TFE (n>=1)  | Closed                   | Dissipative                  | None                   |
| MCF         | Closed + req. singularity| Geometric-dissipative        | Curvature (certain)    |
| **NLS (def.)**| **Closed**             | **Dispersive Hamiltonian**   | **None**               |
| **NLS (foc., d=1)**| **Closed**        | **Dispersive Hamiltonian**   | **None**               |
| **NLS (foc., d=2)**| **Sharp threshold** | **Dispersive Hamiltonian**   | **Concentration (above M_*)** |
| **NLS (foc., d>=3)**| **Partially open** | **Dispersive Hamiltonian**   | **Concentration (large data)** |
| NS (3D)    | Open                     | Viscous (insufficient)       | Open                   |
| RD          | Constitutive             | Constitutive                 | Constitutive           |

---

*End of Mode 1: Axiom → Envelope. Mode 2 (PDE → Extremal Dynamics) will follow in a subsequent file.*
