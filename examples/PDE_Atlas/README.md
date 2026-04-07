# AD Example: The PDE Atlas

---

## Overview

The PDE Atlas is the first and most comprehensive example of Architectural Distillation applied to a family of systems. It contains structural evaluations of 14 major nonlinear partial differential equations of mathematical physics, all analyzed through the same AD methodology.

Each evaluation demonstrates the full AD process: axiom identification, channel decomposition, envelope derivation (Mode 1), extremal dynamics (Mode 2), constraint surface construction (Mode 3), and evaluation against the six AD criteria.

---

## Systems Evaluated

| System | Pole | Key Feature |
|---|---|---|
| **Allen-Cahn** | Diffusive | Non-conserved gradient flow, interface extinction |
| **Burgers** | Hyperbolic | Conservation-law closure, shock formation |
| **Cahn-Hilliard** | Diffusive | Conserved gradient flow, coarsening dynamics |
| **Fokker-Planck** | Diffusive | Linear drift-diffusion, Gibbs-Boltzmann equilibrium |
| **Hamilton-Jacobi** | Hyperbolic | Variational closure, Hopf-Lax formula |
| **Keller-Segel** | Aggregation | Nonlocal self-attraction, mass-concentrating blowup |
| **KdV** | Integrable | Bi-Hamiltonian, soliton resolution, exact solvability |
| **Mean Curvature Flow** | Geometric | Extrinsic curvature evolution, genus reduction |
| **NLS** | Dispersive | Complex-valued Hamiltonian, solitons/scattering |
| **Navier-Stokes** | Fluid | Nonlocal pressure, open 3D regularity |
| **Porous Medium** | Diffusive | Degenerate diffusion, finite-speed propagation |
| **Ricci Flow** | Geometric | Intrinsic curvature evolution, geometrization |
| **Reaction-Diffusion** | Diffusive | Pattern formation, Turing instability |
| **Thin Film** | Diffusive | Fourth-order degenerate, contact-line geometry |

---

## Evaluation Structure

Each system's evaluation follows a standardized five-document structure:

1. **`_01_ArchitectureSpec.md`** — Axiom identification and channel decomposition (AD Step 1)
2. **`_02_Mode1_Envelope.md`** — Envelope derivation: forbidden/necessary configurations, envelope inequalities (AD Step 2)
3. **`_03_Mode2_ExtremalDynamics.md`** — Extremal dynamics: behaviors at structural limits, universal inequalities, attractors (AD Step 3)
4. **`_04_Mode3_ChannelSurface.md`** — Constraint surface: channel-space geometry, faces, closure, dissipation geometry (AD Step 4)
5. **`_05_FS_Criteria_Verdict.md`** — Evaluation against the six AD criteria with scoring (AD Step 5)

---

## How to Read the Atlas

**To understand the AD process:** Read any single system's five documents in order. The Allen-Cahn or Burgers evaluations are good starting points — they are structurally simple and demonstrate the methodology clearly.

**To compare systems:** Read the `_01` documents side by side to compare axioms and channels. Read the `_04` documents to compare constraint-surface geometries. Read the `_05` documents to compare AD scores.

**To understand a pole:** Read the evaluations for all systems at the same pole (e.g., all diffusive-pole systems) to see what they share and where they differ.

---

## Provenance

These evaluations were originally developed within the Factor Skyline project and have been reframed as AD examples. The underlying mathematical analysis is preserved in full. The "FS" naming in file names reflects this provenance.

---

## See Also

- [AD Process Steps](../../framework/methodology/process/step1_identify_multiplicative_structure.md) — the six-step process each evaluation follows
- [AD Pipeline: Channels](../../framework/methodology/core/02_pipeline.md) — the channel taxonomy used in each decomposition
- [AD Geometry: Envelopes and Constraint Surfaces](../../framework/methodology/core/03_geometry.md) — the geometric concepts applied in Modes 1-3
- [AD Invariants: Evaluation Criteria](../../framework/methodology/core/04_invariants.md) — the six criteria used in each verdict
- [AD Methodology](../../docs/AD_methodology.md) — the complete process description
