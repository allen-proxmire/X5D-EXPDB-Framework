# Step 4: Construct the Constraint Surface (Mode 3)

> **Summary:** Construct the constraint surface — the geometric object in channel space that encodes all structural relationships. Identify faces, assess closure, classify the surface type, characterize dissipation geometry, and assign the architecture to a structural pole.

---

## Overview

Step 4 constructs the *constraint surface* — the geometric object in channel space that encodes all structural relationships among the channels. This is the deepest layer of the AD analysis.

This corresponds to **Mode 3** of the AD analysis.

---

## 4.1 Define the Channel Space

Each channel identified in Step 1 has a level of activity. Together, these activity levels define a coordinate system — the *channel space*. The constraint surface is a geometric object within this space.

**How to define channel space:**

1. List all channels from Step 1.
2. For each channel, define a scalar measure of its activity (e.g., the magnitude of the corresponding term in the system's defining equations).
3. The channel space is the space of all possible activity combinations.

---

## 4.2 Identify Faces

The constraint surface has *faces* — codimension-1 boundaries corresponding to structural limits.

**How to identify faces:**

1. For each channel, consider what happens when that channel is pushed to its extreme (maximum activity, zero activity).
2. For each pair of channels, consider what happens when one dominates the other.
3. Each structural limit defines a face of the constraint surface.

---

## 4.3 Assess Closure

For each face, determine whether it is *sealed* or *open*:

- **Sealed:** A structural mechanism (conservation law, contraction property, monotone functional) prevents the dynamics from crossing this face. Identify the sealing mechanism.
- **Open:** No known mechanism prevents crossing. The dynamics might escape through this face.

The *closure* of the constraint surface is the primary structural diagnostic:
- **Fully closed:** All faces sealed — the architecture is structurally sound.
- **Partially open:** Some faces sealed, some open — regime-dependent behavior.
- **Open:** Critical faces unsealed — fundamental structural questions unresolved.

---

## 4.4 Classify the Surface Type

Determine which of the five surface types best describes the constraint surface:

1. **Contracting (Lyapunov):** Dynamics descend toward an attractor.
2. **Isoenergetic (Hamiltonian):** Dynamics circulate on conserved-quantity level sets.
3. **Entropy-resolved (hyperbolic):** Folds resolved by selection principle.
4. **Geometrically dissipative:** Contraction through geometric mechanism.
5. **Mass-stratified:** Topology depends on a conserved scalar.

Some architectures may exhibit mixed surface types or transitions between types depending on the regime.

---

## 4.5 Characterize Dissipation Geometry

Determine how energy, entropy, or free energy is distributed and consumed:

- **Volumetric:** Dissipated everywhere at a rate determined by local state.
- **Zero:** No energy lost (Hamiltonian).
- **Shock-concentrated:** Dissipated only at discontinuities.
- **Nonlocal:** Dissipation rate depends on global state.

---

## 4.6 Assign to a Pole

Based on the constraint-surface geometry, assign the architecture to a structural pole (or identify it as occupying a position between poles):

- Which channel combination dominates?
- Which surface type characterizes the dynamics?
- Which known pole does the architecture most closely resemble?

If the architecture does not fit any known pole, it may represent a new pole — document it as such.

---

## 4.7 Output of Step 4

- A definition of the channel space with coordinates.
- A list of faces with sealing mechanisms (or open status).
- A closure assessment.
- A surface-type classification.
- A dissipation-geometry characterization.
- A pole assignment.
- A narrative explaining the constraint-surface geometry and what it reveals about the architecture.

---

## 4.8 Checklist

- [ ] Channel space defined with activity measures
- [ ] All faces identified
- [ ] Each face assessed as sealed or open
- [ ] Sealing mechanisms identified for sealed faces
- [ ] Surface type classified
- [ ] Dissipation geometry characterized
- [ ] Pole assigned (or new pole documented)
- [ ] Narrative connecting geometry to architectural character

---

## See Also

- [AD Geometry: Envelopes, Constraint Surfaces, and Poles](../ad_core/03_geometry.md) — the full treatment of constraint surfaces and poles
- **Previous step:** [Step 3: Identify Extremal Dynamics](step3_construct_skyline.md)
- **Next step:** [Step 5: Validate and Evaluate](step5_validate.md)
- [PDE Atlas: Allen-Cahn Mode 3](../ad_examples/example_PDE_Atlas/AllenCahn/FS_Eval_AllenCahn_04_Mode3_ChannelSurface.md) — a worked example of constraint surface construction
