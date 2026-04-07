# EXPDB 5D Polyhedral — The X5D Framework
[![DOI](https://zenodo.org/badge/1203337814.svg)](https://doi.org/10.5281/zenodo.19454867)

The **X5D framework** is an architectural language for describing dynamical
systems and analytic pipelines as compositions of channels, envelopes, and
constraint surfaces. This repository contains the framework specification
together with its first major worked example, **X5D-EXPDB**: a polyhedral
reinterpretation of the Tao–Trudgian–Yang Analytic Number Theory Exponent
Database (EXPDB) in which every analytic object computed by the EXPDB
pipeline arises as a projection or envelope of one master polytope
\( \mathcal{P} \subset \mathbb{R}^5 \).

The repository also includes a computational pipeline and an empirical
analysis applying X5D-EXPDB to the post–Guth–Maynard zero-density
landscape.

---

## Repository Map

```
.
├── README.md
├── LICENSE
├── .gitignore
│
├── framework/                       The X5D framework specification
│   ├── X5D_Framework.md
│   └── methodology/                 Architectural Distillation methodology
│       ├── core/                    Concept docs (principles, pipeline,
│       │                            geometry, invariants, examples overview)
│       └── process/                 Six-step AD process (step1 … step6)
│
├── docs/                            Methodology overview, FAQ, archived
│   ├── AD_overview.md               original AD README
│   ├── AD_methodology.md
│   ├── AD_FAQ.md
│   └── AD_original_README.md
│
├── examples/                        Worked examples
│   ├── README.md
│   ├── expdb/                       X5D-EXPDB (the headline example)
│   │   ├── README.md
│   │   ├── X5D_EXPDB_Reinterpretation.md
│   │   ├── invariant.md
│   │   ├── NEXT_STEPS.md
│   │   └── analysis/                Empirical Guth–Maynard analysis
│   │       ├── README.md
│   │       ├── GuthMaynard_BindingConstraints.md
│   │       ├── GuthMaynard_EXPDB_Analysis.md
│   │       ├── GuthMaynard_Pipeline_Report.txt
│   │       └── figures/
│   ├── example_PDE_Atlas/           14 PDEs evaluated by AD methodology
│   │   └── README.md
│   ├── example_EGS_Skyline/         Erdős–Guy–Selfridge skyline notes
│   └── FactorSkyline_Evaluation_EventDensity.md
│
└── compute/                         Computational pipeline
    ├── README.md
    ├── pipeline.py
    ├── gap_test_harness.py
    ├── sensitivity_map.py
    ├── plots/
    ├── archive/                     Earlier pipeline iterations
    │   └── README.md
    └── vendor/                      Vendored upstream
        ├── README.md
        └── expdb/                   Clone of teorth/expdb
```

---

## Entry Points

- **The framework**: [`framework/X5D_Framework.md`](framework/X5D_Framework.md)
  — the architectural language: channels, envelopes, constraint surfaces,
  six evaluation criteria, the seven structural poles.

- **The methodology**:
  [`framework/methodology/`](framework/methodology/) — the upstream
  Architectural Distillation methodology that the X5D framework
  instantiates: five concept docs in [`core/`](framework/methodology/core/)
  and the six-step AD process in [`process/`](framework/methodology/process/).
  See also [`docs/AD_overview.md`](docs/AD_overview.md) and
  [`docs/AD_methodology.md`](docs/AD_methodology.md).

- **The X5D-EXPDB reinterpretation**:
  [`examples/expdb/`](examples/expdb/) — the master polytope
  \( \mathcal{P} \subset \mathbb{R}^5 \), the projection/envelope ladder,
  the X5D invariant, the monotone contraction flow, and the fixed-point
  theorem.

- **Empirical analysis**:
  [`examples/expdb/analysis/`](examples/expdb/analysis/) — binding
  constraints and sensitivity after Guth–Maynard (2024).

- **The PDE Atlas**:
  [`examples/example_PDE_Atlas/`](examples/example_PDE_Atlas/) — 14 major
  nonlinear PDEs evaluated through the AD methodology (Allen–Cahn,
  Burgers, Cahn–Hilliard, Navier–Stokes, Ricci flow, …).

- **Computational pipeline**: [`compute/`](compute/) — runnable Python
  scripts that compute \( A(\sigma) \), \( A^*(\sigma) \), \( \theta \),
  and the figures.

---

## Status

Active research repository. The X5D framework is described in
`framework/X5D_Framework.md`, and the underlying Architectural
Distillation methodology lives in `framework/methodology/`. X5D-EXPDB
is the first complete worked example; the PDE Atlas (14 PDEs) provides
a second family of worked examples through the AD methodology.
Additional examples (Erdős discrepancy, expanded EGS skyline) are
in progress.
