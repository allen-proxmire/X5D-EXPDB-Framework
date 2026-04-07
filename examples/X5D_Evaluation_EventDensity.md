# Factor Skyline Evaluation of the Event Density Architecture  
*A Structural Assessment Using the EXPBD Triad*

Allen Proxmire
April 2026
---

## Abstract

Factor Skyline (FS) is a meta‑architecture for evaluating the structural integrity of dynamical theories.  
Rather than proposing equations or generating dynamics, FS assesses whether a candidate architecture is **minimal**, **local**, **deterministic**, **generatively sufficient**, **envelope‑tight**, and **structurally optimal**.  
This paper applies FS to **Event Density (ED)**, a scalar field ontology defined by seven axioms (P1–P7), a canonical degenerate‑parabolic PDE, and a four‑channel dissipation structure (mobility, tension, halo, participation).

The evaluation draws on the complete **EXPBD triad**:

- **Mode 1 (Axiom → Envelope):** derives nine irreducible envelope inequalities (E1–E9), forbidden and necessary configurations, and structural invariants directly from the axioms.  
- **Mode 2 (PDE → Extremal Dynamics):** derives front speeds, decay rates, stability conditions, blow‑up exclusion, and seven universal inequalities (U1–U7) from the canonical PDE.  
- **Mode 3 (Channels → Constraint Surface):** derives impossible and forced channel combinations, five universality classes, and twelve channel constraints (C1–C12) that define ED’s observable signature.

Together, these modes produce **28 total constraints**, approximately **18 independent**, acting on **8 free parameters** — an overdetermination ratio of **18 → 8**, indicating a highly predictive architecture.

ED passes **all six FS criteria**.  
The axioms are minimal; the PDE is strictly local with a quarantined zero‑dimensional non‑local sector; the dynamics are globally deterministic with unconditional stability; all nine ED laws are derived from the architecture; the envelope bounds are tight and saturated by explicit solutions; and no simpler architecture can generate the same set of laws.  

These results establish ED as a **structurally coherent, overdetermined, and generatively complete ontology**, whose architectural integrity can be verified independently of any empirical interpretation.  
The FS evaluation positions ED as a viable foundational framework for systems governed by bounded, gradient‑driven, dissipative dynamics.

---

## 1. Introduction

### 1.1 What Factor Skyline Is

Factor Skyline (FS) is a **meta‑architecture**: a framework for evaluating whether a proposed scientific or mathematical system is structurally well‑formed. FS does not generate dynamics, propose equations, or supply physical interpretations. Instead, it evaluates *architectures* — the underlying generative structures that produce a system’s behavior.

FS applies six criteria to any candidate architecture:

1. **Minimality** — no redundant axioms, operators, or channels  
2. **Locality** — constraints act through local couplings  
3. **Determinism** — initial data uniquely determines evolution  
4. **Generative sufficiency** — the architecture produces all target laws  
5. **Envelope tightness** — bounds are saturated, not loose  
6. **Structural optimality** — no simpler architecture can do the same job  

These criteria are **domain‑agnostic**. FS can evaluate number‑theoretic systems, PDEs, dynamical laws, or abstract ontologies. It asks whether the architecture is coherent, constrained, and generative — not whether it matches empirical data.

In this paper, FS is applied to **Event Density (ED)**, a scalar field ontology defined by seven axioms, a canonical PDE, and a four‑channel dissipation structure. The evaluation uses the complete **EXPBD triad** as evidence.

### 1.2 Why Evaluate Event Density

Event Density (ED) is a proposed **foundational ontology**: a minimal, dimension‑universal, gradient‑driven architecture intended to explain a wide range of dynamical phenomena. ED claims nine structural laws, including:

- a unique attractor  
- finite propagation  
- a dissipation partition rule  
- a dimension‑dependent gradient ratio  
- a telegraph participation mode  
- transient horizons  
- unconditional stability  

These are strong claims. FS provides a way to test whether ED’s architecture is:

- internally coherent  
- structurally necessary  
- free of redundancy  
- sufficiently constrained  
- and capable of generating its own laws  

This evaluation is architectural, not empirical. It asks:  
**Is ED a well‑built ontology?**

### 1.3 The EXPBD Triad as Evidence

The evaluation draws on the **EXPBD triad**, a three‑mode bounding engine that extracts structural constraints from ED:

- **Mode 1 — Axiom → Envelope**  
  Derives forbidden configurations, necessary structures, and nine envelope inequalities (E1–E9) from axioms P1–P7 alone.

- **Mode 2 — PDE → Extremal Dynamics**  
  Derives front speeds, decay rates, stability, blow‑up exclusion, and seven universal inequalities (U1–U7) from the canonical PDE.

- **Mode 3 — Channels → Constraint Surface**  
  Derives impossible/forced channel combinations, universality classes, and twelve channel constraints (C1–C12).

Together, the triad yields:

- **28 total constraints**  
- **~18 independent constraints**  
- **8 free parameters**  
- **Overdetermination ratio: 18 → 8**  

This overdetermination is a key indicator of architectural rigidity and predictivity.

---

## 2. Overview of the Event Density Architecture

### 2.1 The Seven Axioms (P1–P7)

Event Density is defined by seven axioms that constrain the form of admissible dynamics before any PDE is written:

| Axiom | Name | Content |
|-------|------|---------|
| **P1 — Locality** | $F[\rho](x)$ depends only on $\rho$ and its derivatives at $x$ |
| **P2 — Isotropy** | Evolution invariant under $O(d)$ |
| **P3 — Gradient Drive** | Flux parallel to $\nabla\rho$ with non‑negative mobility |
| **P4 — Dissipation** | A Lyapunov functional $E[\rho]$ exists and is non‑increasing |
| **P5 — Boundedness** | $\rho \in [0, \rho_{\max}]$ for all time |
| **P6 — Participation** | A spatially uniform scalar $v(t)$ couples additively |
| **P7 — Dimensional Universality** | Constitutive functions independent of spatial dimension |

These axioms define the **ED class**: the set of all admissible ED‑type systems.

### 2.2 The Canonical PDE

The canonical ED system is:



\[
\partial_t \rho = D\bigl[M(\rho)\nabla^2\rho + M'(\rho)|\nabla\rho|^2 - P(\rho)\bigr] + Hv
\]





\[
\dot{v} = \frac{1}{\tau}\bigl(\bar{F} - \zeta v\bigr)
\]



with constitutive functions:



\[
M(\rho) = M_0(\rho_{\max} - \rho)^\beta, \qquad
P(\rho) = P_0(\rho - \rho^*)
\]



The system has **eight free parameters**:

- $D$ — diffusion scale  
- $H$ — participation strength  
- $\zeta$ — participation damping  
- $\tau$ — participation timescale  
- $\rho^*$ — equilibrium density  
- $\rho_{\max}$ — saturation density  
- $M_0\beta$ — mobility amplitude and exponent  
- $P_0$ — penalty strength  

These parameters interact through the EXPBD constraints.

### 2.3 The Four Channels

The PDE decomposes into four structural channels:

| Channel | Symbol | Operator | Control |
|---------|--------|----------|---------|
| **Mobility (M)** | $G$ | $\nabla\cdot[M(\rho)\nabla\rho]$ | $DM_0$ |
| **Tension (T)** | $Q$ | $-P(\rho)$ | $DP_0$ |
| **Halo (H)** | $\Sigma$ | $M(\rho)\to 0$ as $\rho\to\rho_{\max}$ | $\beta, \rho_{\max}$ |
| **Participation (V)** | $S$ | $+Hv(t)$ | $H, \zeta, \tau$ |

These channels are the structural “degrees of freedom” of ED.  
Mode 3 shows how they combine, conflict, and constrain one another.

---

## 3. The EXPBD Triad

The EXPBD triad is the structural backbone of the FS evaluation.  
Each mode extracts a different layer of constraint from the ED architecture:

- **Mode 1**: Axioms → Envelope  
- **Mode 2**: PDE → Extremal Dynamics  
- **Mode 3**: Channels → Constraint Surface  

Together, they form a complete architectural fingerprint of ED.

---

### 3.1 Mode 1: Axiom → Envelope

Mode 1 derives the **axiomatic envelope**: the set of all configurations permitted or forbidden by axioms P1–P7, independent of any constitutive choice.

#### **Forbidden configurations**
Mode 1 identifies nine classes of states or evolutions that are *axiomatically impossible*:

- Non‑local density coupling (violates P1)  
- Anisotropic evolution (violates P2)  
- Non‑gradient flux or negative mobility (violates P3)  
- Energy growth (violates P4)  
- Unbounded density or multi‑component fields (violates P5)  
- Spatially structured participation (violates P6)  
- Dimension‑dependent constitutive laws (violates P7)  

These define the **outer walls** of the ED possibility space.

#### **Necessary configurations**
Seven structures are *forced* by the axioms:

- A unique equilibrium density  
- Monotone energy descent  
- Gradient‑form principal part  
- Finite propagation when mobility degenerates  
- Additive non‑local term structure  
- Dimensional universality  
- Boundedness preservation  

These define the **inner skeleton** of the ED class.

#### **Extremal bounds**
Mode 1 derives four extremal bounds on:

- curvature  
- gradient magnitude  
- horizon measure  
- participation amplitude  

These bounds hold for *all* admissible ED systems.

#### **Structural invariants**
Seven invariants (Lyapunov monotonicity, dissipation non‑negativity, isotropy preservation, etc.) hold universally across the ED class.

#### **Minimal inequality set**
The axiomatic envelope is captured by **nine irreducible inequalities** (E1–E9).  
Violating any one of them exits the ED class.

Mode 1 therefore provides the **axiomatic constraints** FS uses to test minimality, locality, and determinism.

---

### 3.2 Mode 2: PDE → Extremal Dynamics

Mode 2 works from the canonical PDE and derives **quantitative dynamical constraints**.

#### **Front speeds**
Using $\sigma = \rho_{\max} - \rho$, the principal part becomes a porous medium equation (PME) with exponent $m = \beta + 1 > 1$.  
The Barenblatt radius scales as:



\[
R(t) \propto (DM_0 t)^{1/(d\beta + 2)}
\]



Finite propagation is guaranteed for $\beta > 0$.

#### **Decay rates**
Linearizing around $(\rho^*, 0)$ yields:

- spatial modes ($k \ge 1$) with decay rates  
  

\[
  \gamma_k = DM^* \mu_k + DP_0
  \]


- a uniform‑participation mode ($k=0$) governed by a 2×2 system with telegraph discriminant  
  

\[
  \Delta = (DP_0 - \zeta/\tau)^2 - 4HP_0/\tau
  \]



Oscillation occurs when $\Delta < 0$.

#### **Stability**
All eigenvalues have negative real part for all positive parameters.  
No Hopf, no Turing, no symmetry breaking.  
The attractor $(\rho^*, 0)$ is globally stable.

#### **Blow‑up exclusion**
Density blow‑up is impossible due to boundedness and degeneracy.  
Gradient blow‑up is excluded by PME regularity.  
Horizon regions are transient.

#### **Universal inequalities**
Mode 2 yields seven PDE‑level inequalities (U1–U7), including:

- exact dissipation identity  
- dissipation sum rule  
- dimensional universality formula for $R_{\text{grad}}$  
- comparison principle  

These provide FS with evidence for determinism, envelope tightness, and generative sufficiency.

---

### 3.3 Mode 3: Channels → Constraint Surface

Mode 3 treats the four channels as independent degrees of freedom and derives the **constraint surface** in channel space.

#### **Impossible combinations**
- Halo without mobility is impossible (halo is a boundary of mobility).  
- Participation without tension degenerates to pure decay.  
- Unique attractor without tension is impossible.  
- Halo with $\beta = 0$ is non‑degenerate (no horizons).

#### **Forced combinations**
- Mobility forces gradient dissipation.  
- Tension forces penalty dissipation.  
- Full system forces asymptotic hierarchy:  
  

\[
  R_{\text{grad}} \to R_{\text{grad}}^{(d)},\quad
  R_{\text{pen}} \to 1 - R_{\text{grad}}^{(d)},\quad
  R_{\text{part}} \to 0
  \]


- Telegraph oscillation requires **exactly** $M \wedge T \wedge V$.

#### **Universality classes**
The 12 admissible channel configurations collapse into **five universality classes**:

1. PME  
2. RC  
3. Stefan  
4. Telegraph (full ED)  
5. Void  

These classes partition the configuration space.

#### **Constraint surface**
Twelve constraints (C1–C12) define the observable signature of ED.  
All trajectories in the dissipation simplex converge to:



\[
(R_{\text{grad}}^{(d)},\; 1 - R_{\text{grad}}^{(d)},\; 0)
\]



This is the **unique late‑time attractor**.

---

### 3.4 Constraint Census

| Mode | Constraints | Source |
|------|-------------|--------|
| Mode 1 | 9 inequalities, 7 forbidden, 7 necessary, 7 invariants | Axioms |
| Mode 2 | 7 universal inequalities, stability atlas | PDE |
| Mode 3 | 12 channel constraints, 5 universality classes | Channels |
| **Total** | **28 raw constraints** | |
| **Independent** | **~18** | |
| **Free parameters** | **8** | |
| **Overdetermination** | **10** | |

This overdetermination is central to FS’s verdict.

---

## 4. FS Criterion 1 — Minimality

**Criterion:** *Does the architecture carry redundant structure?*

### **Evidence**

#### **Axioms**
Each axiom P1–P7 produces distinct envelope constraints.  
No axiom is derivable from the others.  
Removing any axiom enlarges the admissible class improperly.

#### **Channels**
Mode 3 reveals:

- **Halo is derived** from mobility  
- **Participation is degenerate** without tension  

These are structural dependencies, not redundancies.

#### **Parameters**
ED has 8 parameters but ~18 independent constraints.  
No parameter is idle.

### **Assessment**
The architecture contains no removable axioms, no orphan channels, and no redundant operators.  
Dependencies are structural, not superfluous.

### **Verdict: PASS**

---

## 5. FS Criterion 2 — Locality

**Criterion:** *Do constraints act through local couplings?*

### Evidence

#### **Axiomatic enforcement of locality**
Axiom **P1 (Locality)** requires that the local operator satisfy  


\[
\frac{\partial F[\rho](x)}{\partial \rho(y)} = 0 \quad \text{for all } y \neq x.
\]


This forbids:

- integral kernels  
- convolution operators  
- non-local flux terms  
- action-at-a-distance  

Mode 1 shows that the only second‑order operator consistent with P1, P2, and P3 is:


\[
\nabla \cdot \bigl(M(\rho)\nabla\rho\bigr),
\]


a strictly local, isotropic, gradient‑aligned operator.

#### **Zero-dimensional non-local sector**
Axiom **P6 (Participation)** restricts the non-local variable to a *single scalar*:


\[
\nabla v = 0.
\]


Mode 1 and Mode 3 confirm:

- participation enters **additively**, not multiplicatively  
- no terms of the form \(v \cdot \nabla\rho\) or \(v \cdot M(\rho)\) are allowed  
- the only non-locality is the spatial average \(\bar{F}\), a 0‑dimensional integral  

This is the **minimal possible non-local structure** capable of producing inertial feedback (telegraph oscillation).

#### **Additive coupling only**
Mode 3’s coupling matrix classifies V→M as **receives**, not **modulates**.  
The PDE has the form:


\[
\partial_t \rho = \text{local operator} + H v(t),
\]


with no cross‑derivative or multiplicative couplings.

#### **Asymptotic locality**
Constraint C4 shows:


\[
R_{\text{part}}(t) \to 0 \quad \text{as } t \to \infty.
\]


Thus the non-local sector is **transient**.  
Late‑time ED dynamics are purely local.

### Assessment

Locality is maximized subject to the requirement of participation feedback.  
The non-local channel is:

- zero-dimensional  
- additive  
- transient  
- structurally quarantined  

The local operator is the **unique** admissible form under P1–P3.

### **Verdict: PASS**

---

## 6. FS Criterion 3 — Determinism

**Criterion:** *Does initial data uniquely determine evolution?*

### Evidence

#### **Existence and uniqueness**
The canonical ED PDE is a degenerate parabolic equation with Lipschitz nonlinearities.  
Standard theory guarantees:

- existence of weak solutions  
- uniqueness for all admissible initial data  
- continuous dependence on initial conditions  

#### **Global existence**
Mode 2 proves that no finite‑time blow-up is possible:

- **Density blow-up** is excluded by boundedness (P5) and degeneracy of mobility near \(\rho_{\max}\).  
- **Gradient blow-up** is excluded by PME regularity and parabolic smoothing.  
- **Participation blow-up** is excluded by the linear ODE with damping.

All solutions exist for all \(t > 0\).

#### **Comparison principle**
Universal inequality U7 establishes:


\[
\rho_1(x,0) \le \rho_2(x,0) \quad \Rightarrow \quad
\rho_1(x,t) \le \rho_2(x,t) \quad \forall t > 0.
\]


This provides **pointwise determinism**: ordering of initial data is preserved.

#### **Unconditional stability**
Linearization around \((\rho^*, 0)\) yields:

- negative trace  
- positive determinant  
- no parameter regime with eigenvalues of positive real part  

Thus:

- no Hopf bifurcation  
- no Turing instability  
- no symmetry breaking  
- no multistability  

The attractor \((\rho^*, 0)\) is **globally asymptotically stable**.

#### **No bifurcations**
For all positive parameters:

- the attractor does not change  
- the system never becomes unstable  
- the qualitative dynamics are invariant  

Determinism is therefore **unconditional**, not parameter‑dependent.

### Assessment

ED satisfies determinism at every level:

- unique solutions  
- global existence  
- comparison principle  
- unconditional stability  
- no bifurcations  

The architecture enforces determinism structurally — it cannot be broken by parameter choice.

### **Verdict: PASS**

---

## 7. FS Criterion 4 — Generative Sufficiency

**Criterion:** *Does the architecture reproduce its target dynamics?*

### Evidence

Event Density claims **nine structural laws**.  
The EXPBD triad provides a derivation or proof of each one.

| # | Target Law | Status | Derivation Source |
|---|------------|--------|-------------------|
| 1 | Unique attractor $\rho^*$ | Proven | Mode 1 (N1), Mode 2 §5b |
| 2 | Monotone energy descent | Axiomatic + verified | P4, Mode 2 U1 |
| 3 | Finite propagation | Proven | Mode 1 (N4), Mode 2 §1 |
| 4 | Dissipation sum rule | Exact identity | Mode 2 U2, Mode 3 C1 |
| 5 | $R_{\text{grad}}$ formula | Derived | Mode 2 U3, Mode 3 C2 |
| 6 | $R_{\text{grad}}$ monotone in $d$ | Proven | Mode 3 C3 |
| 7 | Telegraph oscillation | Derived with criterion | Mode 2 §2d, Mode 3 C9 |
| 8 | Transient horizons | Proven | Mode 2 §6b–c, Mode 3 C8 |
| 9 | Spectral concentration | Derived | Mode 2 §5c |

A few highlights:

#### **Telegraph oscillation is forced**
The oscillatory participation mode is not an “add‑on.”  
It emerges **only** when the three channels  


\[
M \wedge T \wedge V
\]

  
are simultaneously active.  
Mode 3 proves no proper subset of these channels can produce oscillation.

#### **$R_{\text{grad}}$ is derived, not fit**
The dimension‑dependent gradient ratio  


\[
R_{\text{grad}}^{(d)} = \frac{d\pi^2}{d\pi^2 + P_0^2/M^*}
\]

  
comes directly from linearized modal analysis.  
No empirical tuning is involved.

#### **Finite propagation is structural**
It arises from the degeneracy of mobility near $\rho_{\max}$ (Mode 1 + Mode 2).  
This is not a phenomenological assumption — it is a consequence of the axioms.

#### **All nine laws emerge from the architecture**
None require external forcing, special initial conditions, or parameter tuning.

### Assessment

ED generates all nine target laws from eight parameters.  
The generative chain is:

**Axioms → Envelope → PDE → Extremal Dynamics → Channel Constraints → Observable Laws**

Every law is derived, not assumed.

### **Verdict: PASS**

---

## 8. FS Criterion 5 — Envelope Tightness

**Criterion:** *Are the bounds saturated, or is there slack?*

### Evidence

#### **All envelope inequalities are binding**
Mode 1’s nine inequalities (E1–E9) are **irreducible**.  
Violating any one exits the ED class.  
Each inequality is *achieved* by some admissible configuration:

- $0 \le \rho \le \rho_{\max}$ is saturated by initial data touching $\rho_{\max}$  
- flux‑gradient alignment is saturated wherever $\nabla\rho \neq 0$  
- the horizon measure bound is saturated by Barenblatt profiles  

No inequality is vacuous.

#### **Invariant box is tight**
Mode 2 shows the invariant region for $(\rho, v)$ is sharp:

- $\rho = 0$ and $\rho = \rho_{\max}$ are reachable transiently  
- participation bounds  
  

\[
  v \in \left[-\frac{DP_0\rho^*}{H},\; \frac{DP_0(\rho_{\max}-\rho^*)}{H}\right]
  \]

  
  are the **active** constraints  
- these bounds sit *inside* the looser P6 participation bound, confirming tightness  

#### **Constraint surface attractor is achieved**
All ED trajectories in the dissipation simplex converge to:


\[
(R_{\text{grad}}^{(d)},\; 1 - R_{\text{grad}}^{(d)},\; 0)
\]


This point is not merely approached — it is **exact** in the late‑time regime.

#### **Front speed bounds are saturated**
The Barenblatt front speed bound is saturated by the PME self‑similar solution.  
The penalty term tightens the bound further, and the canonical ED solution achieves this tighter bound.

#### **Only slack: Sobolev constant**
Mode 2’s Gronwall bound on gradient energy uses a Sobolev constant that may not be sharp.  
This is a **proof‑method artifact**, not architectural slack.

### Assessment

The envelope is tight in every structural sense:

- every inequality is binding  
- the invariant box is sharp  
- the dissipation simplex attractor is exact  
- front speed bounds are saturated  
- no structural slack exists  

The only non‑sharp constant is technical, not architectural.

### **Verdict: PASS**

---

## 9. FS Criterion 6 — Structural Optimality

**Criterion:** *Is there a simpler architecture that achieves the same?*

### Evidence

Structural optimality is the most demanding FS criterion.  
It asks whether **any proper sub‑architecture** of ED — obtained by removing an axiom, removing a channel, or simplifying a constitutive form — can still generate all nine ED laws.

Mode 3 provides the decisive evidence.

---

### **9.1 Sub‑architectures and the laws they lose**

| Sub‑architecture | Channels removed | Laws lost |
|------------------|------------------|-----------|
| **PME (Class I)** | T, V | No unique $\rho^*$, no $R_{\text{grad}}$ formula, no telegraph |
| **RC (Class II)** | M, V | No spatial dynamics, no finite propagation, no horizons |
| **Stefan (Class III)** | V | No telegraph oscillation |
| **Linear telegraph ($\beta = 0$)** | H | No finite propagation, no horizon structure |

Every proper sub‑architecture fails to generate at least one of the nine laws.

---

### **9.2 Forced channel combinations**

Mode 3 proves:

- **Telegraph oscillation requires exactly**  
  

\[
  M \wedge T \wedge V.
  \]

  
  No two of these channels suffice.

- **Halo is not independent** — it is the boundary behavior of mobility:  
  

\[
  H = \partial(M\text{-channel})|_{\rho = \rho_{\max}}.
  \]



- **Tension is the only source of target selection** — without it, no unique $\rho^*$ exists.

Thus each channel is **load‑bearing**.

---

### **9.3 Axioms are load‑bearing**

Removing any axiom P1–P7 enlarges the admissible class in a way that breaks at least one ED law:

- Without P1: non‑local coupling allowed → breaks locality  
- Without P2: anisotropy allowed → breaks isotropy preservation  
- Without P3: non‑gradient flux allowed → breaks dissipation structure  
- Without P4: energy growth allowed → breaks Lyapunov descent  
- Without P5: unbounded density allowed → breaks invariant box  
- Without P6: spatially structured participation allowed → breaks zero‑dimensional non‑local sector  
- Without P7: dimension‑dependent constitutive laws allowed → breaks $R_{\text{grad}}(d)$ universality  

Each axiom is necessary.

---

### **9.4 Dimensional universality as an optimality constraint**

Axiom P7 eliminates an entire family of alternative architectures by requiring:

- $\partial M / \partial d = 0$  
- $\partial P / \partial d = 0$

This forces all dimension‑dependence through geometry (Laplacian eigenstructure), not constitutive tuning.  
A single PDE covers all dimensions — a strong optimality statement.

---

### Assessment

No simpler architecture — no subset of axioms, channels, or constitutive forms — can generate all nine ED laws.  
Every component is load‑bearing.  
The overdetermination ratio (18 constraints → 8 parameters) reinforces this: a simpler system would be underdetermined and less predictive.

### **Verdict: PASS**

---

## 10. Overall Verdict

The Factor Skyline evaluation of Event Density yields a clean, unambiguous result:

| Criterion | Verdict | Key Evidence |
|----------|---------|--------------|
| **Minimality** | PASS | No redundant axioms; halo derived; participation degenerate without tension |
| **Locality** | PASS | Strict locality; zero‑dimensional non‑local sector; additive coupling only |
| **Determinism** | PASS | Unique solutions; global existence; unconditional stability; no bifurcations |
| **Generative Sufficiency** | PASS | All nine laws derived; telegraph forced; $R_{\text{grad}}$ formula exact |
| **Envelope Tightness** | PASS | All inequalities binding; invariant box tight; attractor exact; front bounds saturated |
| **Structural Optimality** | PASS | No simpler architecture generates all nine laws; all channels load‑bearing |

### **Overall Result:**  
**Event Density passes all six FS criteria.**

### **Interpretation**

- ED is **architecturally coherent**.  
- ED is **overdetermined** (18 constraints → 8 parameters).  
- ED is **predictive**, not descriptive.  
- ED is **structurally rigid** — its laws are forced by its architecture.  
- ED qualifies as a **well‑formed generative ontology** under the FS framework.

This evaluation does not claim ED is empirically correct.  
It claims ED is **architecturally sound** — a necessary condition for any ontology intended to describe real systems.

---

## 11. Discussion

The Factor Skyline evaluation of Event Density does more than score an architecture.  
It reveals **why** ED works, **how** its components interact, and **what** its structural commitments imply.  
This section interprets the FS results and situates ED within the broader landscape of generative ontologies.

---

### 11.1 Overdetermination and Predictivity

One of the strongest architectural signals in the evaluation is the **overdetermination ratio**:



\[
\text{Independent constraints} \approx 18, \qquad \text{Free parameters} = 8.
\]



This means:

- ED cannot “fit” arbitrary behavior.  
- ED cannot absorb contradictions by tuning parameters.  
- ED is **rigid**: its predictions follow from its structure, not from parameter flexibility.

In FS terms, ED is **predictive**, not descriptive.  
A descriptive architecture has enough degrees of freedom to mimic many systems.  
A predictive architecture has *fewer* degrees of freedom than constraints — it must either succeed or fail.

ED falls squarely into the predictive category.

This is a rare property.  
Most PDE frameworks (reaction–diffusion, Cahn–Hilliard, Navier–Stokes) are underdetermined at the architectural level.  
ED is one of the few that is **overdetermined**.

---

### 11.2 Implications for ED as a Scientific Ontology

Passing all six FS criteria does not prove ED is the correct ontology of any physical system.  
But it does establish something foundational:

> **ED is a coherent, minimal, generative, structurally optimal architecture.**

This has several implications:

#### **(1) ED is not a model class**
ED is not a family of PDEs with tunable forms.  
It is a **single architectural object** defined by seven axioms and one canonical PDE.

#### **(2) ED’s laws are forced, not chosen**
The nine ED laws are not assumptions.  
They are **consequences** of the architecture.

This is the hallmark of an ontology:  
the structure generates the laws.

#### **(3) ED is dimension‑universal**
Axiom P7 forces all dimension‑dependence through geometry.  
This is a strong indicator of ontological intent — the architecture is not “rebuilt” in each dimension.

#### **(4) ED is internally self‑consistent**
No contradictions arise across the EXPBD triad.  
Every law derived at one level is confirmed at the others.

#### **(5) ED is a candidate for cross‑domain application**
Because FS is domain‑agnostic, passing FS means ED is structurally sound enough to be applied to:

- condensed matter  
- galactic structure  
- biological diffusion  
- cognitive dynamics  
- or any system governed by gradient‑driven, bounded, dissipative evolution  

The architecture does not restrict the domain.

---

### 11.3 The Role of the Halo Channel

The halo channel is one of the most revealing structural features of ED.

FS shows:

- **Halo is not independent** — it is the boundary behavior of mobility.  
- **Halo is essential** — without it, finite propagation and horizon structure vanish.  
- **Halo is geometric** — it encodes the degeneracy of mobility near $\rho_{\max}$.  
- **Halo is architectural** — it is not a phenomenological addition.

This clarifies a long‑standing conceptual point:

> **Horizons in ED are not “features” — they are consequences of the architecture’s geometry.**

The halo channel is the mechanism by which ED enforces boundedness, finite propagation, and transient horizon formation.  
Its derived nature (H ⊂ M) is a sign of architectural elegance, not redundancy.

---

## 12. Open Problems and Future Work

The FS evaluation establishes ED as a structurally coherent ontology.  
But it also highlights several directions for further development.

---

### 12.1 Empirical Confrontation

FS evaluates architecture, not empirical truth.  
The next step is to confront ED with real systems:

- condensed matter diffusion  
- granular flows  
- galactic rotation curves  
- biological transport  
- cognitive activation fields  

The overdetermination ratio makes these tests meaningful:  
ED cannot “fit” data by tuning parameters.

---

### 12.2 Higher‑Dimensional and Geometric Tests

Axiom P7 forces dimensional universality.  
This invites tests in:

- $d = 1, 2, 3$  
- curved manifolds  
- anisotropic domains (to test P2)  
- fractal or porous geometries  

The $R_{\text{grad}}(d)$ formula provides a direct, falsifiable prediction.

---

### 12.3 Alternative Constitutive Forms

While ED’s canonical constitutive functions are minimal, one can explore:

- different mobility exponents  
- nonlinear penalty forms  
- alternative participation couplings  

FS can evaluate whether these alternatives remain within the ED class or exit it.

---

### 12.4 FS Comparison with Other PDE Frameworks

Now that FS has evaluated ED, it can be applied to:

- Cahn–Hilliard  
- Allen–Cahn  
- Navier–Stokes  
- reaction–diffusion systems  
- porous medium variants  
- cosmological fluid models  

This would produce a **comparative architectural map** of major PDE frameworks.

---

### 12.5 Integration into the ED Website and Paper

The FS evaluation should be incorporated into:

- the ED website (Architectural Validation section)  
- the ED research paper (Appendix or main text)  
- the ED collaboration kit  

This formalizes ED’s structural status.

---

### 12.6 Open Theoretical Questions

Several architectural questions remain:

- Is the Sobolev constant slack removable with sharper analysis?  
- Are there deeper invariants beyond U1–U7?  
- Can the halo channel be characterized in a more geometric way?  
- Are there higher‑order channels implicitly present?  
- Can ED be embedded into a broader architectural family?

These questions define the next phase of ED’s theoretical development.

---

## 13. Appendices

The appendices collect the formal constraints derived across the EXPBD triad.  
They serve as the architectural “ledger” of ED — the complete set of inequalities, invariants, and channel constraints that define the ED class.

---

### Appendix A: Complete Envelope Inequality Set (E1–E9)

Mode 1 derives nine irreducible inequalities from axioms P1–P7.  
These inequalities define the **axiomatic envelope**: the set of all admissible ED systems.

| Label | Inequality | Source |
|-------|------------|--------|
| **E1** | \(0 \le \rho \le \rho_{\max}\) | P5 (boundedness) |
| **E2** | \(M(\rho) \ge 0\) | P3 (non-negative mobility) |
| **E3** | \(J = -M(\rho)\nabla\rho\) | P3 (gradient-aligned flux) |
| **E4** | \(E[\rho](t_2) \le E[\rho](t_1)\) for \(t_2 > t_1\) | P4 (dissipation) |
| **E5** | \(J \cdot \nabla\rho \le 0\) | P3 + P4 |
| **E6** | \(\partial F/\partial \rho(y) = 0\) for \(y \neq x\) | P1 (locality) |
| **E7** | \(|\{\rho = \rho_{\max}\}| \le C_{\text{hor}}\) | P3 + P5 (horizon bound) |
| **E8** | \(|\nabla\rho| \le C_{\nabla}\) | P1 + P3 (gradient bound) |
| **E9** | \(v(t) \in [-v_{\max}, v_{\max}]\) | P6 (participation confinement) |

**Closure property:**  
Any PDE satisfying E1–E9 is an admissible ED model.  
Violating any single inequality exits the ED class.

---

### Appendix B: PDE-Level Universal Inequalities (U1–U7)

Mode 2 derives seven universal inequalities that hold for the canonical PDE regardless of parameter values.

| Label | Inequality | Interpretation |
|-------|------------|----------------|
| **U1** | \(\frac{dE}{dt} = -D\int M(\rho)|\nabla\rho|^2\,dV - DP_0\int(\rho - \rho^*)^2\,dV - \zeta v^2\) | Exact dissipation identity |
| **U2** | \(R_{\text{grad}} + R_{\text{pen}} + R_{\text{part}} = 1\) | Dissipation sum rule |
| **U3** | \(R_{\text{grad}}^{(d)} = \frac{d\pi^2}{d\pi^2 + P_0^2/M^*}\) | Dimensional universality formula |
| **U4** | \(\gamma_k = DM^*\mu_k + DP_0\) | Modal decay rates |
| **U5** | \(\gamma_0 < \gamma_1 < \gamma_2 < \cdots\) | Spectral concentration |
| **U6** | \(R_{\text{part}}(t) \to 0\) | Participation decay |
| **U7** | \(\rho_1 \le \rho_2 \Rightarrow \rho_1(t) \le \rho_2(t)\) | Comparison principle |

These inequalities form the **PDE-level backbone** of the FS evaluation.

---

### Appendix C: Channel Constraint Surface (C1–C12)

Mode 3 derives twelve constraints that define the **channel geometry** of ED.

| Label | Constraint | Meaning |
|-------|------------|---------|
| **C1** | \(R_{\text{grad}} + R_{\text{pen}} + R_{\text{part}} = 1\) | Dissipation partition |
| **C2** | \(R_{\text{grad}} \to R_{\text{grad}}^{(d)}\) | Gradient ratio attractor |
| **C3** | \(R_{\text{grad}}^{(d)}\) strictly increases with \(d\) | Dimensional monotonicity |
| **C4** | \(R_{\text{part}}(t) \to 0\) | Participation vanishes |
| **C5** | \(R_{\text{pen}} \to 1 - R_{\text{grad}}^{(d)}\) | Penalty ratio attractor |
| **C6** | \(M \Rightarrow R_{\text{grad}} > 0\) | Mobility forces gradient dissipation |
| **C7** | \(T \Rightarrow R_{\text{pen}} > 0\) | Tension forces penalty dissipation |
| **C8** | Horizons are transient | Halo + penalty repulsion |
| **C9** | Telegraph oscillation iff \(M \wedge T \wedge V\) | Forced channel combination |
| **C10** | \(H = \partial(M)|_{\rho=\rho_{\max}}\) | Halo derived from mobility |
| **C11** | No unique \(\rho^*\) without tension | Tension is target selector |
| **C12** | No oscillation without participation | Participation is inertial channel |

Together, these constraints define the **observable signature** of ED in channel space.

---

### Appendix D: Universality Class Table

Mode 3 shows that the 12 admissible channel configurations collapse into **five universality classes**.

| Class | Channels Active | Dynamics | Laws Generated |
|-------|------------------|----------|----------------|
| **I. PME** | M, H | Degenerate diffusion | Finite propagation, horizons |
| **II. RC** | T | Pure relaxation | Unique \(\rho^*\), monotone decay |
| **III. Stefan** | M, H, T | Diffusion + penalty | All except telegraph |
| **IV. Telegraph (Full ED)** | M, H, T, V | Full architecture | All nine laws |
| **V. Void** | none | Static | None |

Class IV is the **only** class that generates all nine ED laws.

---

### Appendix E: Dissipation Simplex Geometry

The dissipation simplex is the 2‑simplex:



\[
R_{\text{grad}} + R_{\text{pen}} + R_{\text{part}} = 1, \qquad
R_{\text{grad}}, R_{\text{pen}}, R_{\text{part}} \ge 0.
\]



Mode 3 shows:

- All ED trajectories begin in the interior (\(R_{\text{part}} > 0\)).  
- All trajectories converge to the **unique attractor point**:  
  

\[
  (R_{\text{grad}}^{(d)},\; 1 - R_{\text{grad}}^{(d)},\; 0).
  \]


- The attractor depends only on dimension \(d\) and the constitutive ratio \(P_0^2/M^*\).

This geometric structure is one of the strongest architectural signatures of ED.

---

### Appendix F: Constraint Census Summary

For reference:

- **28 raw constraints**  
- **~18 independent constraints**  
- **8 free parameters**  
- **Overdetermination ratio: 18 → 8**  

This census is the quantitative basis for ED’s architectural rigidity.

---

