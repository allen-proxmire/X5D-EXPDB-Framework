# Computational Pipeline

This folder contains the runnable Python pipeline that drives the
empirical X5D-EXPDB analysis. It computes the zero-density envelope
\( A(\sigma) \), the energy envelope \( A^*(\sigma) \), the prime gap
exponent \( \theta \), the binding constraints, and the figures used in
[`../examples/expdb/analysis/`](../examples/expdb/analysis/).

The pipeline runs the upstream Tao–Trudgian–Yang EXPDB code (vendored in
`vendor/expdb/`) with a scipy-based replacement for `pycddlib` that
removes the C-extension build dependency.

## Layout

| Path | Purpose |
|---|---|
| `pipeline.py` | Full pipeline: \(A(\sigma)\), \(A^*(\sigma)\), \(\theta\), sensitivity |
| `gap_test_harness.py` | Systematic check of unexploited Guth–Maynard interactions |
| `sensitivity_map.py` | Fine-grained sensitivity computation |
| `plots/plot_A_envelope.py` | Figure 1 — zero-density envelope |
| `plots/plot_sensitivity_heatmap.py` | Figure 2 — sensitivity heat map |
| `plots/plot_alpha_sensitivity.py` | Figure 3 — \(\alpha\) sensitivity |
| `plots/plot_succession.py` | Figure 4 — succession of bottlenecks |
| `archive/` | Earlier pipeline iterations (kept for reference; do not use) |
| `vendor/expdb/` | Vendored clone of [teorth/expdb](https://github.com/teorth/expdb) |

## Requirements

- Python 3.10+
- `numpy`, `scipy`, `sympy`, `matplotlib`
- The vendored upstream package in `vendor/expdb/` (no installation
  needed; scripts add it to `sys.path` directly)

## Running

From the repository root:

```bash
python compute/pipeline.py
python compute/plots/plot_A_envelope.py
python compute/plots/plot_sensitivity_heatmap.py
python compute/plots/plot_alpha_sensitivity.py
python compute/plots/plot_succession.py
```

Plot scripts write their output PNGs to
`examples/expdb/analysis/figures/`.

## See Also

- [`../examples/expdb/`](../examples/expdb/) — the X5D-EXPDB
  reinterpretation that this pipeline supports.
- [`../examples/expdb/analysis/`](../examples/expdb/analysis/) — the
  empirical Guth–Maynard binding-constraint analysis that consumes the
  pipeline output.
- [`vendor/README.md`](vendor/README.md) — notes on the vendored
  upstream EXPDB clone.
