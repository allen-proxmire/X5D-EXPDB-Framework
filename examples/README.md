# Worked Examples

This folder collects worked examples of the X5D framework and the
underlying Architectural Distillation (AD) methodology — concrete
analytic, geometric, or algorithmic systems analyzed as flows on
rational polyhedral regions, channel decompositions, and constraint
surfaces.

## X5D reinterpretations

- **[expdb/](expdb/) — X5D-EXPDB**
  The X5D reinterpretation of the Tao–Trudgian–Yang Analytic Number
  Theory Exponent Database. A single 5D rational polytope
  \( \mathcal{P} \subset \mathbb{R}^5 \) whose projections and envelopes
  reproduce every analytic object in the EXPDB pipeline. Includes the
  full paper, the invariant, project notes, and an empirical
  Guth–Maynard binding-constraint analysis.

## AD evaluations

These examples apply the Architectural Distillation methodology
(`../framework/methodology/`) to families of systems. They use the
shared AD vocabulary — channels, envelopes, constraint surfaces,
poles, and the six AD criteria.

- **[example_PDE_Atlas/](example_PDE_Atlas/) — The PDE Atlas**
  Structural evaluations of 14 major nonlinear partial differential
  equations: Allen–Cahn, Burgers, Cahn–Hilliard, Fokker–Planck,
  Hamilton–Jacobi, KdV, Keller–Segel, Mean Curvature Flow, NLS,
  Navier–Stokes, Porous Medium, Ricci flow, Reaction–Diffusion, and
  Thin Film. Each evaluation follows the same five-document structure
  (architecture spec, envelope, extremal dynamics, channel surface,
  criteria verdict). See [`example_PDE_Atlas/README.md`](example_PDE_Atlas/README.md).

- **[example_EGS_Skyline/](example_EGS_Skyline/) — Erdős–Guy–Selfridge**
  Notes on the factorial-decomposition skyline view of the
  Erdős–Guy–Selfridge problem.

- **[FactorSkyline_Evaluation_EventDensity.md](FactorSkyline_Evaluation_EventDensity.md)**
  Standalone Factor Skyline evaluation of the Event Density framework.

## In progress

- **X5D-ED** — X5D reinterpretation of the Erdős discrepancy pipeline.
- **Expanded X5D-EGS** — full X5D treatment of Erdős–Guy–Selfridge
  beyond the current AD-style notes.

Each X5D example follows the same pattern: a master polytope, a
projection/envelope ladder, an X5D signature, and a monotone
contraction flow with a fixed-point theorem.
