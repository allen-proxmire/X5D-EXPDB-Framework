# AD Geometry: Envelopes, Constraint Surfaces, and Poles

> **Summary:** This document defines the three geometric objects at the heart of AD: *envelopes* (the boundary of the structurally possible), *constraint surfaces* (the geometric encoding of channel interactions), and *poles* (the qualitatively distinct regions of architectural space). It also introduces architectural maps as visualization tools.

---

## 1. Systems as Architectures

The central idea of Architectural Distillation is that every system composed of interacting mechanisms is an *architecture* — a structured composition of channels, conservation laws, symmetries, and constraints. The architecture determines what the system can do (its dynamical repertoire), what it cannot do (its forbidden configurations), and how it behaves at its structural limits (its extremal dynamics).

An architecture is not a solution — it is the structural framework that generates all possible trajectories. An architecture is not an equation — it is the structural content that persists regardless of how the system is represented. Two different-looking systems can have the same architecture, and two similar-looking systems can have different architectures.

---

## 2. Envelopes

### 2.1 What an Envelope Is

An *envelope* is the maximal set of constraints that a system's axioms impose on all admissible states and evolutions. It is the boundary of the structurally possible — everything inside is consistent with the axioms; everything outside violates at least one.

The envelope is not a single number or inequality. It is a *system* of constraints that together define the boundary of the architecture's repertoire. Some constraints are equalities (conservation laws — exact, inviolable), some are one-sided inequalities (energy bounds — can decrease but not increase), and some are conditional (regularity criteria — valid as long as a specific quantity stays bounded).

The power of the envelope is that it applies to *every* admissible trajectory, not just specific initial conditions or parameter values. The envelope is *architectural* — it holds because of the structure, not because of any particular instance.

### 2.2 Deriving the Envelope

The envelope is derived through three steps:

**Step 1: Forbidden configurations.** What the system *cannot* do. These are states or behaviors that violate the axioms. Each forbidden configuration is traceable to a specific axiom — a specific structural commitment that excludes the behavior. The forbidden configurations define the *exterior* of the envelope.

**Step 2: Necessary configurations.** What the system *must* do — structures forced into existence by the axioms. The necessary configurations define the *interior structure* of the envelope.

**Step 3: Envelope inequalities.** The quantitative bounds that define the precise boundary. These come in several types:

- **Conservation identities:** Exact equalities for all admissible trajectories.
- **Dissipation identities:** Rates of energy or entropy decrease.
- **Contraction inequalities:** Bounds on how far apart two trajectories can be.
- **Regularity bounds:** Estimates on derivatives or smoothness.
- **Threshold conditions:** Precise boundaries between qualitative regimes (e.g., global existence vs. singularity formation).

### 2.3 Closed and Open Envelopes

An envelope is *closed* if every face of the constraint surface is sealed — the dynamics cannot escape in any direction. A closed envelope means the architecture is structurally sound: globally well-posed, predictable, controllable.

An envelope is *open* if one or more faces are unsealed — the dynamics might escape through an uncontrolled direction. Open envelopes indicate structurally challenging architectures where qualitative behavior may be unresolved.

The *degree* of openness matters. Some open faces are *sharp* (the exact threshold is known and the behavior at the boundary is characterized), while others are *unresolved* (neither the threshold nor the boundary behavior is determined).

---

## 3. Constraint Surfaces

### 3.1 What a Constraint Surface Is

The constraint surface is the *deepest structural object* in the AD analysis. It is the geometric object in channel space that encodes *all* structural relationships among the channels — not just individual channel properties (which the envelope captures) and extremal behaviors, but the *full geometry of how channels interact*.

Each channel has a level of activity. The set of all possible channel-activity states, subject to the system's structural constraints, forms a geometric object — the constraint surface. It is the phase portrait of the architecture.

### 3.2 Faces and Closure

The constraint surface has *faces* — codimension-1 boundaries that the dynamics can potentially approach. Each face corresponds to a structural limit — a direction in which a channel is pushed to its extreme.

A face is *sealed* if a structural mechanism prevents the dynamics from crossing it. A face is *open* if no known mechanism prevents crossing. The *closure* of the constraint surface — whether all faces are sealed — is the primary structural diagnostic.

### 3.3 Surface Types

Five qualitatively distinct constraint-surface geometries have been identified:

**Contracting (Lyapunov).** The surface contracts over time — the dynamics descend a Lyapunov functional toward an attractor. Produces convergence to equilibrium. The hallmark of diffusion-dominated architectures.

**Isoenergetic (Hamiltonian).** The surface has fixed dimension — the dynamics circulate on a level set of conserved quantities without contracting or expanding. Produces solitons, quasi-periodic orbits, and scattering. The hallmark of dispersion-dominated architectures.

**Entropy-resolved (hyperbolic).** The surface develops folds that are resolved by an entropy/viscosity selection principle. Introduces irreversibility — information is lost at discontinuities, and the surface simplifies over time. The hallmark of transport-dominated architectures.

**Geometrically dissipative.** The surface contracts through a geometric mechanism (area decrease, curvature decrease) rather than a scalar Lyapunov functional. Produces curvature singularities required for topological programs. The hallmark of curvature-dominated architectures.

**Mass-stratified.** The surface's topology depends on a conserved scalar. Below a threshold, the surface is contracting; above the threshold, the surface has an open face. The hallmark of aggregation-dominated architectures.

### 3.4 Dissipation Geometry

The dissipation geometry describes how energy, entropy, or free energy is distributed and consumed across the channels:

- **Volumetric dissipation:** Energy dissipated everywhere, at a rate determined by the local state.
- **Zero dissipation:** No energy lost — Hamiltonian structure preserves energy exactly.
- **Shock-concentrated dissipation:** Energy dissipated only at discontinuities — a set of measure zero.
- **Nonlocal dissipation:** Dissipation rate at each point depends on the global state.

The dissipation geometry determines the *direction* of dynamics on the constraint surface.

### 3.5 Why Geometry Is the Deepest Layer

The constraint surface captures all structural relationships simultaneously. Its closure, dimensionality, and singularity structure determine the system's qualitative character more completely than any individual inequality or extremal behavior.

The constraint surface is where the *poles* become visible. Systems at the same pole have qualitatively similar constraint-surface geometries. The constraint-surface geometry is the defining structural feature of each pole.

---

## 4. Poles

### 4.1 What a Pole Is

A *structural pole* is a qualitatively distinct region of the architectural space where specific channel combinations dominate. Systems near the same pole share qualitative features — they have the same type of smoothing, the same type of singularity, the same type of long-time behavior.

### 4.2 Known Poles

From the analysis of dynamical systems (primarily PDEs), seven poles have been identified:

| Pole | Dominant Channel | Characteristic Behavior |
|---|---|---|
| **Diffusive** | Parabolic smoothing | Smooth, spread, converge to equilibria |
| **Hyperbolic** | First-order transport | Steepen, form shocks |
| **Dispersive** | Oscillatory spreading | Oscillate, form solitons, conserve energy |
| **Geometric** | Curvature-driven evolution | Smooth geometrically, develop curvature singularities |
| **Aggregation** | Nonlocal self-attraction | Concentrate mass |
| **Fluid** | Multi-channel with nonlocal pressure | Complex dynamics with open regularity |
| **Integrable** | Maximum structural resources | Infinite conservation laws, exact solvability |

Poles are not rigid categories — they are *tendencies*. A system can have features of multiple poles. But the dominant pole determines the qualitative character.

### 4.3 Why the Taxonomy Is Finite

The taxonomy has a finite number of poles because the number of qualitatively distinct channel compositions is finite. There are approximately nine channel types, and they combine in a finite number of qualitatively distinct ways. This finiteness means the space of possible system dynamics is *bounded* — there are not infinitely many qualitatively different types of behavior, but a finite number of poles, each with a characteristic signature.

### 4.4 Apex Architectures

An *apex architecture* is a system that achieves the deepest structural results within its pole. Apex architectures have the most complete theory, the sharpest bounds, and the richest structural resources. They serve as the reference points against which other systems at the same pole are compared.

---

## 5. Architectural Maps

An *architectural map* is a visual representation of the dependency structure within a distilled system. It shows the relationships between axioms, channels, envelope inequalities, and constraint-surface faces — making the architecture's logical structure visible at a glance.

Architectural maps serve three purposes:
1. **Navigation:** They show how results depend on each other.
2. **Diagnosis:** They reveal where open questions and unresolved faces are located.
3. **Comparison:** They enable side-by-side structural comparison of different systems.

---

## See Also

- [AD Pipeline: Channels as Building Blocks](02_pipeline.md) — the channel taxonomy underlying these geometric structures
- [AD Invariants: Evaluation Criteria](04_invariants.md) — how to evaluate the resulting architecture
- [Step 2: Derive the Envelope](../ad_process/step2_extract_axes.md) — the process for deriving envelopes
- [Step 3: Identify Extremal Dynamics](../ad_process/step3_construct_skyline.md) — the process for identifying extremal behaviors
- [Step 4: Construct the Constraint Surface](../ad_process/step4_distill_invariants.md) — the process for constructing constraint surfaces
