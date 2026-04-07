# AD Examples Overview

> **Summary:** This document surveys the current examples of AD in action — the PDE Atlas (14 nonlinear PDEs), the Factor Skyline (arithmetic structure) — and outlines potential future applications to dynamical systems, geometric structures, computational architectures, and stochastic systems.

---

## 1. The Idea of an Atlas

An atlas is a collection of maps — each map showing a different region, but all drawn in the same projection, with the same symbols, the same scale, the same legend. You can compare any two maps because they speak the same visual language.

An AD atlas is a collection of structural profiles — each profile describing a different system, but all analyzed through the same AD methodology, with the same concepts (channels, envelopes, constraint surfaces, poles), the same criteria (minimality, locality, determinism, generative sufficiency, envelope tightness, structural optimality), and the same scoring. You can compare any two systems because they speak the same structural language.

---

## 2. Current Examples

### 2.1 The PDE Atlas

The first and most developed AD atlas covers the major nonlinear partial differential equations of mathematical physics. Sixteen systems have been evaluated, covering all seven known structural poles:

- **Diffusive pole:** Fokker-Planck, porous medium, thin-film, Allen-Cahn, Cahn-Hilliard, reaction-diffusion
- **Hyperbolic pole:** Hamilton-Jacobi, Burgers
- **Dispersive pole:** Nonlinear Schrodinger, Korteweg-de Vries
- **Geometric pole:** Mean curvature flow, Ricci flow
- **Aggregation pole:** Keller-Segel
- **Fluid pole:** Navier-Stokes
- **Integrable apex:** KdV

Each PDE evaluation follows a standardized 4-step process:
1. **Architectural Specification** — axioms, channel decomposition, structural commitments
2. **Mode 1: Envelope Derivation** — forbidden configurations, necessary configurations, envelope inequalities
3. **Mode 2: Extremal Dynamics** — behaviors at structural limits, universal inequalities, attractors
4. **Mode 3: Constraint Surface** — channel-space geometry, faces, closure, dissipation geometry

Followed by evaluation against the six AD criteria.

See `ad_examples/example_PDE_Atlas/` for the full worked examples.

### 2.2 The Factor Skyline (Arithmetic Architecture)

The Factor Skyline is the originating example of AD. It applies the distillation process to the multiplicative structure of the integers, where each integer is represented as a column of width lpf(n) (least prime factor) and height n/lpf(n). The AD primitives (width, height, activation, coverage, escape) are the "channels" of the arithmetic structure, and classical results (prime number theorem, Mertens' theorem, Chebyshev conservation law) emerge as "envelope inequalities."

The arithmetic skyline is a *static architecture* — the integers do not evolve in time. But it shares deep structural parallels with the dynamical PDE architectures, reflecting the universality of architectural structure.

See the [Factor Skyline repository](https://github.com/allen-proxmire/factor-skyline) for details.

---

## 3. Potential Future Examples

AD is designed to extend to new domains. The following are candidates for future atlas entries:

### 3.1 Dynamical Systems
Finite-dimensional dynamical systems where channels are the components of the vector field: linear terms (eigenvalue structure), nonlinear terms (bifurcation structure), coupling terms (network topology). Poles include gradient, Hamiltonian, dissipative-chaotic, and integrable.

### 3.2 Geometric Structures
Riemannian manifolds, symplectic manifolds, and algebraic varieties viewed as static architectures whose channels are curvature components and whose envelope is the set of geometric constraints (Einstein condition, Kahler condition, Calabi-Yau condition).

### 3.3 Computational Architectures
Neural network architectures where layer types (convolutional, recurrent, attention, normalization) are channels; the representable functions are the envelope; the loss landscape is the constraint surface.

### 3.4 Stochastic Systems
Stochastic PDEs where noise channels (additive, multiplicative, space-time) join the existing deterministic channels, connecting to regularity structures and paracontrolled distributions.

---

## 4. How to Contribute a New Example

To add a new system to an AD atlas:

1. Follow the six-step AD process (see `ad_process/`).
2. Produce the four standard analysis documents (Architectural Specification, Mode 1, Mode 2, Mode 3).
3. Evaluate against the six AD criteria.
4. Submit the worked example to `ad_examples/`.

The AD framework is designed so that any practitioner can apply it to a new system and produce a standardized structural profile.

---

## See Also

- [AD Process Steps](../ad_process/step1_identify_multiplicative_structure.md) — the six-step process for distilling a new system
- [PDE Atlas](../ad_examples/example_PDE_Atlas/README.md) — the full set of PDE worked examples
- [AD Methodology](../docs/AD_methodology.md) — the complete process description
