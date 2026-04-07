# Architectural Distillation: Overview

> **Summary:** A comprehensive introduction to AD — what it is, where it came from, its core concepts, its six-step process, and how to get started.

---

## What Is AD?

Architectural Distillation (AD) is a general, reusable methodology for extracting structure from systems composed of interacting mechanisms. Given any such system — a PDE, a dynamical system, a geometric structure, an arithmetic process, a computational architecture — AD produces a standardized structural profile: a channel decomposition, an envelope of constraints, a constraint-surface geometry, a pole classification, and an evaluation against six structural criteria.

AD is not a mathematical theory. It does not prove theorems about specific systems. It is a *process* — a step-by-step methodology that any practitioner can apply to any system to produce a comparable structural profile.

---

## The Vision

The same structural phenomena appear across different mathematical domains: decomposition into irreducible components, competition between stabilizing and destabilizing mechanisms, existence of canonical forms, threshold conditions separating qualitative regimes. These are not domain-specific — they are *architectural universals* that appear whenever a system is composed of interacting channels.

AD provides the language and methodology to make these universals visible, comparable, and transferable. The ultimate vision is a *structural atlas of systems* — a comprehensive map of the architectural landscape, showing the poles, the connections, the hierarchies, and the apex structures that organize the space of possible dynamics.

---

## Core Concepts

| Concept | Description |
|---|---|
| **Channel** | An independent mechanism within a system — the atomic building block of an architecture |
| **Envelope** | The maximal set of constraints imposed by the system's axioms on all admissible states |
| **Constraint Surface** | The geometric object in channel space encoding all structural relationships |
| **Pole** | A qualitatively distinct region of architectural space where specific channel combinations dominate |
| **AD Criteria** | Six evaluation dimensions: minimality, locality, determinism, generative sufficiency, envelope tightness, structural optimality |

---

## The AD Process

AD follows a six-step process (see `ad_process/` for details):

1. **Identify the architecture** — axioms and channel decomposition
2. **Derive the envelope** (Mode 1) — forbidden configurations, necessary configurations, envelope inequalities
3. **Identify extremal dynamics** (Mode 2) — behaviors at structural limits
4. **Construct the constraint surface** (Mode 3) — channel-space geometry
5. **Validate and evaluate** — six-criteria assessment and reproducibility
6. **Generalize and extend** — cross-domain comparison and taxonomy extension

---

## Where AD Came From

AD was extracted from the Factor Skyline (FS) project, which applied architectural analysis to the multiplicative structure of the integers and then to 14 major nonlinear PDEs. The methodology proved so general — the same concepts (channels, envelopes, constraint surfaces, poles) applied with equal force to arithmetic, diffusion, fluid dynamics, and geometry — that it warranted separation into its own standalone framework.

FS remains a specific mathematical theory (definitions, proofs, invariants). AD is the upstream methodology that produced it and can produce comparable structural analyses for any domain.

---

## Who AD Is For

- **Mathematicians** who want to compare the structural properties of systems across domains.
- **Scientists** who want to understand why some models are structurally sound and others have open questions.
- **Engineers** who want to select the simplest architecture that generates required behavior.
- **Researchers** who want a systematic methodology for analyzing new systems.

---

## Getting Started

1. Read [`ad_core/01_principles.md`](../ad_core/01_principles.md) for the motivation and four pillars.
2. Read [`ad_core/02_pipeline.md`](../ad_core/02_pipeline.md) for the channel taxonomy.
3. Read [`ad_core/03_geometry.md`](../ad_core/03_geometry.md) for envelopes, constraint surfaces, and poles.
4. Walk through a worked example in [`ad_examples/example_PDE_Atlas/`](../ad_examples/example_PDE_Atlas/README.md).
5. Apply the six-step process in [`ad_process/`](../ad_process/step1_identify_multiplicative_structure.md) to your own system.

---

## See Also

- [AD Methodology](AD_methodology.md) — the complete process description with all six steps
- [AD FAQ](AD_FAQ.md) — answers to common questions about AD
