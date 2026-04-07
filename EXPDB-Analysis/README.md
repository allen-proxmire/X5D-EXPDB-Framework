# EXPDB Binding Constraint Analysis After Guth-Maynard (2024)

This folder contains a structural analysis of the [Analytic Number Theory Exponent Database](https://teorth.github.io/expdb/) (EXPDB) pipeline after incorporating the Guth-Maynard large value estimate.

## Papers

- **[GuthMaynard_BindingConstraints.md](GuthMaynard_BindingConstraints.md)** - The main paper. Identifies the cusp at sigma = 7/10 where Ingham (1940) and Guth-Maynard (2024) meet at A = 30/13, performs sensitivity analysis (d(theta)/d(||A||) = 169/900), maps the succession of bottlenecks, and shows that the EXPDB pipeline has fully exploited the GM result for theta_PNTALL = 17/30.

- **[GuthMaynard_EXPDB_Analysis.md](GuthMaynard_EXPDB_Analysis.md)** - Background analysis describing how GM fits into the EXPDB polyhedral framework.

- **[GuthMaynard_Pipeline_Report.txt](GuthMaynard_Pipeline_Report.txt)** - Raw pipeline output.

## Figures

| Figure | Description |
|--------|-------------|
| [A_sigma_envelope.png](A_sigma_envelope.png) | Zero-density envelope A(sigma) with binding constraints colored by source |
| [sensitivity_heatmap.png](sensitivity_heatmap.png) | Sensitivity heat map showing the cone of nonzero d(theta)/dA(sigma) |
| [alpha_sensitivity.png](alpha_sensitivity.png) | Partial derivatives of alpha(sigma) with respect to A and B = A* |
| [succession_bottlenecks.png](succession_bottlenecks.png) | Succession of bottlenecks as the cusp is progressively lowered |

## Code

The computational pipeline is in [`../../compute/`](../../compute/):

| Script | Purpose |
|--------|---------|
| `expdb_full_pipeline.py` | Full pipeline: A(sigma), A*(sigma), theta, sensitivity |
| `gap_test_harness.py` | Systematic check of unexploited GM interactions |
| `sensitivity_map.py` | Fine-grained sensitivity computation |
| `plot_A_envelope.py` | Figure 1 |
| `plot_sensitivity_heatmap.py` | Figure 2 |
| `plot_alpha_sensitivity.py` | Figure 3 |
| `plot_succession.py` | Figure 4 |
| `expdb/` | Clone of [teorth/expdb](https://github.com/teorth/expdb) with scipy-based cdd replacement |

## Key Results

- **theta_PNTALL = 17/30**, binding at sigma* = 7/10 (cusp of Ingham and GM)
- **Sensitivity:** d(theta)/d(||A||) = 169/900. An epsilon-improvement needs to hold on an interval of width ~0.563*epsilon around sigma = 0.70
- **Cusp slopes** are exactly symmetric: +/-300/169
- **Bottleneck** is purely in A(sigma) for theta_PNTALL; A*(sigma) only enters at the GAPSQUARE level
- **Pipeline completeness verified:** no unexploited transformation chain changes ||A|| = 30/13
- **One bug found:** stale hardcoded exponent pairs in `bourgain_ep_to_zd` (reported to EXPDB maintainers)
