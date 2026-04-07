# AD Pipeline: Channels as Building Blocks

> **Summary:** This document defines *channels* — the atomic building blocks of any architecture — and presents the taxonomy of channel types, their properties (locality, linearity, stability role, scale action), and how they combine through balance, competition, cooperation, and nullity.

---

## 1. What Is a Channel?

A *channel* is an independent mechanism within a system. It is the atomic unit of an architecture — the irreducible building block from which the system's behavior is constructed. Every qualitative feature of a system (smoothing, steepening, concentration, oscillation, convergence) can be traced to the interaction of specific channels.

A channel is characterized by four properties:

- **Locality:** Does the channel depend only on the state at each point (local), or does it couple distant points through a global operator (nonlocal)?
- **Linearity:** Is the channel linear in the state, quasilinear, or fully nonlinear?
- **Stability role:** Does the channel stabilize the dynamics (smooth, spread, damp), destabilize them (steepen, concentrate, amplify), or act as a neutral constraint?
- **Scale action:** How does the channel's effect depend on the spatial or structural scale? Does it act preferentially on fine scales or coarse scales?

---

## 2. Channel Types

Across analyzed systems, a finite number of fundamental channel types appear. Every system is a composition of channels drawn from this finite set. The known channel types include:

| Channel Type | Structural Role | Example Manifestations |
|---|---|---|
| **Diffusion** | Stabilizing — spreading through amplitude decay | Laplacian smoothing, nonlinear diffusion, biharmonic dissipation |
| **Dispersion** | Stabilizing — spreading through phase interference | Oscillatory spreading where components dephase without energy loss |
| **Transport** | Destabilizing — movement along gradients | Self-advection, Hamiltonian transport, nonlinear steepening |
| **Curvature** | Dual-natured — smooths at low values, concentrates at high | Geometric evolution driven by curvature of surfaces or metrics |
| **Aggregation** | Destabilizing — nonlocal self-attraction | Concentration driven by global potential fields |
| **Pressure** | Neutral — constraint enforcement | Nonlocal constraint maintaining structural conditions (e.g., incompressibility) |
| **Reaction** | Constitutive-dependent | Local, zeroth-order transformation (bistable, oscillatory, excitable) |
| **Conservation** | Neutral — quantity preservation | Divergence-form structure preserving total mass, energy, or probability |
| **Gauge** | Neutral — symmetry invariance | Phase rotation, diffeomorphism invariance, reparametrization freedom |

The finiteness of channel types is a structural feature: the space of possible architectures is finite-dimensional at the qualitative level, enabling a finite taxonomy.

---

## 3. Channel Properties

### 3.1 Locality

The locality axis is the sharpest structural divide. Most architectures are *fully local* — every channel depends only on the state and its derivatives at each point. Nonlocal channels (pressure, aggregation) introduce fundamentally different structural character. The *role* of nonlocality matters: a nonlocal constraint-enforcement mechanism behaves very differently from a nonlocal driving mechanism.

### 3.2 Stability Classification

Every channel has a stability role:

- **Unconditionally stabilizing:** Diffusion, dispersion, conservation
- **Unconditionally destabilizing:** Transport (steepening), aggregation (concentration)
- **Dual-natured:** Curvature (smooths at low values, concentrates at high values)
- **Constitutive-dependent:** Reaction (depends on specific form)
- **Neutral:** Pressure, gauge (structural constraints, not forces)

The *fundamental tension* of every system is the competition between its stabilizing and destabilizing channels. The outcome of this competition — whether stabilizing channels can control destabilizing ones — is the system's core structural question.

### 3.3 Universality

The same channel types appear across different domains. Diffusion appears in heat transfer, probability, and geometry. Transport appears in fluid mechanics, traffic flow, and conservation laws. Curvature appears in surface evolution and metric evolution. The channels are *domain-independent structural units*.

### 3.4 Independence

Each channel has a definite structural character that is independent of the other channels present. Diffusion stabilizes regardless of what reaction channel accompanies it. Transport destabilizes regardless of whether diffusion or dispersion provides the counterbalance. This independence is what makes the decomposition meaningful — the channels are genuinely atomic.

---

## 4. How Channels Combine

Channels do not act independently — they interact through several mechanisms:

**Balance.** Two opposing channels reach equilibrium at a specific scale, producing a coherent structure (e.g., solitons from the balance of transport and dispersion).

**Competition.** Two opposing channels compete across a range of scales, with the outcome determined by a control parameter (e.g., Reynolds number governing viscosity vs. advection).

**Cooperation.** Two channels with the same tendency reinforce each other (e.g., diffusion and conservation cooperating to produce self-similar spreading).

**Nullity.** A channel contributes nothing to a specific accounting despite being dynamically active (e.g., energy-neutral channels that drive nonlinear dynamics but do zero net work in the energy budget).

---

## 5. Why Channels Are Atomic

The channels are the irreducible building blocks of the AD framework because:

1. **Finiteness.** The number of qualitatively distinct channel types is finite, enabling a finite taxonomy of architectures.
2. **Universality.** The same channel types appear across different domains — they are domain-independent structural units.
3. **Independence.** Each channel has a definite structural character independent of the other channels, making the decomposition meaningful.

---

## See Also

- [AD Principles](01_principles.md) — why architectural distillation exists
- [AD Geometry: Envelopes, Constraint Surfaces, and Poles](03_geometry.md) — what channels produce when they interact
- [Step 1: Identify the System's Architecture](../ad_process/step1_identify_multiplicative_structure.md) — how to identify and decompose channels in practice
- [PDE Atlas](../ad_examples/example_PDE_Atlas/README.md) — 14 worked examples of channel decomposition
