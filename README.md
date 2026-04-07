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
│   └── X5D_Framework.md
│
├── examples/                        Worked examples of the X5D framework
│   ├── README.md
│   └── expdb/                       X5D-EXPDB
│       ├── README.md
│       ├── X5D_EXPDB_Reinterpretation.md
│       ├── invariant.md
│       ├── NEXT_STEPS.md
│       └── analysis/                Empirical Guth–Maynard analysis
│           ├── README.md
│           ├── GuthMaynard_BindingConstraints.md
│           ├── GuthMaynard_EXPDB_Analysis.md
│           ├── GuthMaynard_Pipeline_Report.txt
│           └── figures/
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

- **The X5D-EXPDB reinterpretation**:
  [`examples/expdb/`](examples/expdb/) — the master polytope
  \( \mathcal{P} \subset \mathbb{R}^5 \), the projection/envelope ladder,
  the X5D invariant, the monotone contraction flow, and the fixed-point
  theorem.

- **Empirical analysis**:
  [`examples/expdb/analysis/`](examples/expdb/analysis/) — binding
  constraints and sensitivity after Guth–Maynard (2024).

- **Computational pipeline**: [`compute/`](compute/) — runnable Python
  scripts that compute \( A(\sigma) \), \( A^*(\sigma) \), \( \theta \),
  and the figures.

---

## Status

Active research repository. The X5D framework is described in
`framework/X5D_Framework.md`. X5D-EXPDB is the first complete worked
example. Additional examples (Erdős–Guy–Selfridge, Erdős discrepancy)
are forthcoming.
