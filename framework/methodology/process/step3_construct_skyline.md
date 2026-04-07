# Step 3: Identify Extremal Dynamics (Mode 2)

> **Summary:** Identify the behaviors at the boundary of the envelope — the extremal dynamics that reveal the architecture's true character. Catalog universal inequalities and identify attractor types.

---

## Overview

Step 3 identifies the *extremal dynamics* of the architecture — the behaviors at the boundary of the envelope. These are the most extreme states the architecture can reach, revealing the system's true structural character.

This corresponds to **Mode 2** of the AD analysis.

---

## 3.1 What Extremal Means

The extremal dynamics are not the generic or typical behaviors (which may be uninteresting — most trajectories eventually settle down) but the *limiting* behaviors that reveal the architecture's character. If the envelope is a box, the extremal dynamics are what happens when the system pushes against the walls.

Does it bounce back (stable equilibrium)? Does it break through (singularity)? Does it slide along the wall (propagation)? Does it settle into a corner (coherent structure formation)?

---

## 3.2 Identify Extremal Behavior Types

Survey the architecture for each type of extremal behavior. The known types include:

| Type | Description |
|---|---|
| **Diffusive spreading** | Amplitude decays, support expands, density approaches universal profile |
| **Shock formation** | Gradients steepen to discontinuity, resolved by selection principle |
| **Soliton formation** | Opposing channels reach balance, producing localized shape-preserving structures |
| **Scattering** | Nonlinear solution approaches a free linear solution as time grows |
| **Amplitude concentration** | Solution concentrates at a point — amplitude grows without bound |
| **Mass concentration** | Density collapses into a singular measure |
| **Interface dynamics** | Diffuse boundaries move according to geometric laws |
| **Curvature blowup** | Curvature grows without bound at a point |
| **Topology change** | Singularity changes the connectivity of the domain |
| **Extinction** | The state variable ceases to exist |

Not every architecture exhibits all types. The relevant types depend on the channels present and the pole the system occupies.

---

## 3.3 Catalog Universal Inequalities

Identify the architecture's universal inequalities — quantitative bounds that hold for every admissible trajectory. These are the inviolable structural constraints. Classify them:

- **Conservation laws** (exact): quantities preserved for all time.
- **Contraction properties** (monotone): distances between trajectories decrease.
- **Dispersive/smoothing estimates** (decay): amplitudes decrease over time.
- **Monotone functionals** (Lyapunov): the system moves in a definite direction.
- **Threshold conditions** (bifurcation): precise boundaries between qualitative regimes.

---

## 3.4 Identify Attractors

Determine the long-time state to which generic trajectories converge. Known attractor types:

| Attractor Type | Description |
|---|---|
| **Fixed-point** | Single steady state |
| **Self-similar** | One-parameter family of profiles |
| **Soliton resolution** | Decomposition into persistent coherent structures plus dispersing radiation |
| **Scattering** | Approach to a free linear solution |
| **Geometric** | Convergence to canonical geometric forms |
| **Singular** | Singularity as the terminal state |

---

## 3.5 Output of Step 3

- A list of extremal behavior types exhibited by the architecture.
- A table of universal inequalities, classified by type.
- An identification of the attractor type(s).
- A narrative explaining *why* the extremal dynamics take the form they do — tracing each behavior to the competition or cooperation of specific channels.

---

## 3.6 Checklist

- [ ] All relevant extremal behavior types identified
- [ ] Universal inequalities cataloged and classified
- [ ] Attractor type(s) identified
- [ ] Each extremal behavior traced to channel interactions
- [ ] Narrative connecting extremal dynamics to architectural structure

---

## See Also

- [AD Geometry: Envelopes, Constraint Surfaces, and Poles](../ad_core/03_geometry.md) — the conceptual foundations
- **Previous step:** [Step 2: Derive the Envelope](step2_extract_axes.md)
- **Next step:** [Step 4: Construct the Constraint Surface](step4_distill_invariants.md)
- [PDE Atlas: Allen-Cahn Mode 2](../ad_examples/example_PDE_Atlas/AllenCahn/FS_Eval_AllenCahn_03_Mode2_ExtremalDynamics.md) — a worked example of extremal dynamics identification
