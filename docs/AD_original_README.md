# Architectural Distillation of Multiplicative Processes (AD)

Architectural Distillation (AD) is a general, reusable methodology for extracting structure from systems composed of interacting mechanisms. Given any such system — a partial differential equation, a dynamical system, a geometric structure, an arithmetic process, a computational architecture — AD produces a standardized structural profile: a channel decomposition, an envelope of constraints, a constraint-surface geometry, a pole classification, and an evaluation against six structural criteria. AD is not tied to any specific mathematical domain. It is a reproducible, extensible framework that can be applied step-by-step to new systems by any practitioner.

---

## The Four Pillars

| Pillar | Description |
|---|---|
| **Generalizable** | AD applies to any system that can be decomposed into interacting mechanisms. It is a methodology, not a theory. |
| **Architectural** | AD identifies channels, envelopes, constraint surfaces, invariants, and poles. It analyzes structure, not solutions. |
| **Reproducible** | AD is a step-by-step process that produces consistent, testable outputs. Two practitioners analyzing the same system arrive at the same profile. |
| **Extensible** | AD grows as new systems are analyzed. New channel types, poles, and surface types extend the taxonomy without revising the core. |

---

## What AD Is Not

- AD is **not** a mathematical theory. It does not prove theorems.
- AD is **not** a collection of proofs. Proofs belong to the domain-specific theories AD analyzes.
- AD is **not** tied to the Factor Skyline or any specific domain.
- AD is **not** a dumping ground for artifacts from any project.

AD is a clean, standalone methodological framework.

---

## Relationship to the Factor Skyline

AD was extracted from the [Factor Skyline](https://github.com/allen-proxmire/factor-skyline) (FS) project. FS is a mathematical theory about the multiplicative structure of the integers. AD is the upstream methodology that was used to build FS and was then recognized as general enough to stand on its own. FS is one *instance* of AD; the PDE Atlas is another.

---

## Getting Started

1. **Understand the concepts:** Start with [`ad_core/01_principles.md`](ad_core/01_principles.md) for motivation, then [`ad_core/02_pipeline.md`](ad_core/02_pipeline.md) for the channel taxonomy, and [`ad_core/03_geometry.md`](ad_core/03_geometry.md) for envelopes, constraint surfaces, and poles.

2. **Follow the process:** The six-step AD process is documented in [`ad_process/`](ad_process/), from identifying the architecture through generalization.

3. **Study an example:** The [PDE Atlas](ad_examples/example_PDE_Atlas/) contains 14 complete worked examples showing AD applied to major nonlinear PDEs.

4. **Apply it yourself:** Use the process steps and examples as templates to distill your own system.

---

## Repo Structure

| Directory | Purpose |
|---|---|
| [`ad_core/`](ad_core/) | Core concepts: principles, channel taxonomy, geometry (envelopes, constraint surfaces, poles), evaluation criteria, and examples overview |
| [`ad_process/`](ad_process/) | The six-step AD process: identify architecture, derive envelope, identify extremal dynamics, construct constraint surface, validate, generalize |
| [`ad_examples/`](ad_examples/) | Worked examples of AD applied to real systems, including the PDE Atlas (14 evaluations) |
| [`docs/`](docs/) | Overview, full methodology description, and FAQ |
| `LICENSE` | License file |

---

## Examples

### The PDE Atlas

14 nonlinear PDEs evaluated through the full AD process, covering seven structural poles: diffusive, hyperbolic, dispersive, geometric, aggregation, fluid, and integrable. See [`ad_examples/example_PDE_Atlas/`](ad_examples/example_PDE_Atlas/).

### The Factor Skyline

The originating example — AD applied to the multiplicative structure of the integers. See the [Factor Skyline repository](https://github.com/allen-proxmire/factor-skyline).

---

## Contributing

Contributions are welcome. The most valuable contribution is a new worked example — a system distilled through the full AD process.

**To contribute a new example:**
1. Read the [AD Process Steps](ad_process/step1_identify_multiplicative_structure.md) and the [PDE Atlas](ad_examples/example_PDE_Atlas/README.md) for reference.
2. Apply the six-step process in [`ad_process/`](ad_process/) to your system.
3. Produce the five standard documents (Architectural Specification, Mode 1, Mode 2, Mode 3, Criteria Verdict).
4. Submit to `ad_examples/` via pull request.

**Other contributions:** Improvements to documentation, corrections to existing content, and proposals for new channel types, poles, or surface types are also welcome. Please open an issue to discuss before submitting large changes.

See [`ad_core/05_examples_overview.md`](ad_core/05_examples_overview.md) for detailed guidelines.
