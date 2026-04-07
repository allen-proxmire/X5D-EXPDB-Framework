# Step 2: Derive the Envelope (Mode 1)

> **Summary:** Derive the complete envelope of structural constraints: forbidden configurations (what the system cannot do), necessary configurations (what it must do), and envelope inequalities (the quantitative bounds). Assess whether the envelope is closed or open.

---

## Overview

Step 2 derives the *envelope* of the architecture — the complete catalog of structural constraints that the system's axioms impose on all admissible states and evolutions. The envelope defines the boundary of the structurally possible.

This corresponds to **Mode 1** of the AD analysis.

---

## 2.1 Identify Forbidden Configurations

Determine what the architecture *cannot* do. For each axiom identified in Step 1, ask: *What states or behaviors does this axiom exclude?*

**Examples of forbidden configurations:**
- A conservation axiom forbids net creation or destruction of the conserved quantity.
- A locality axiom forbids coupling between distant points.
- A gradient-flow structure forbids energy increase.
- A unique factorization axiom forbids ambiguous decompositions.

Each forbidden configuration should be traced to a specific axiom. The forbidden configurations collectively define the *exterior* of the envelope — the region the system can never access.

---

## 2.2 Identify Necessary Configurations

Determine what the architecture *must* do — structures forced into existence by the axioms.

**Examples of necessary configurations:**
- A conservation law forces the total quantity to remain constant.
- A bi-Hamiltonian structure forces infinitely many conserved quantities.
- A degeneracy in the mechanism forces finite-speed propagation.
- A symmetry structure forces conservation laws (via Noether's theorem).

The necessary configurations define the *interior structure* of the envelope — the features that every admissible trajectory must exhibit.

---

## 2.3 Derive Envelope Inequalities

Derive the quantitative bounds that define the precise boundary of the envelope. Classify each inequality:

| Type | Description | Tightness |
|---|---|---|
| **Conservation identity** | Exact equality for all trajectories | Exact |
| **Dissipation identity** | Rate of energy/entropy decrease | Exact for smooth solutions |
| **Contraction inequality** | Bound on distance between trajectories | Sharp if saturated by some state |
| **Regularity bound** | Estimate on derivatives or smoothness | Sharp or suboptimal |
| **Threshold condition** | Boundary between qualitative regimes | Sharp if exact value known |

---

## 2.4 Assess Envelope Closure

Determine whether the envelope is *closed* (all faces sealed) or *open* (one or more faces unsealed).

For each face of the constraint surface:
- Identify the structural mechanism that seals it (if any).
- If no sealing mechanism is known, classify the face as open.
- Assess the *degree* of openness: sharp (threshold known) vs. unresolved (threshold unknown).

---

## 2.5 Output of Step 2

- A list of forbidden configurations, each traced to a specific axiom.
- A list of necessary configurations, each traced to a specific axiom.
- A table of envelope inequalities, classified by type and tightness.
- An assessment of envelope closure: closed, partially open, or open.
- A count of total constraints (typically 9–12 for well-analyzed systems).

---

## 2.6 Checklist

- [ ] All forbidden configurations identified and traced to axioms
- [ ] All necessary configurations identified and traced to axioms
- [ ] Envelope inequalities derived and classified
- [ ] Each inequality assessed for sharpness
- [ ] Envelope closure assessed (closed/partially open/open)
- [ ] Total constraint count documented

---

## See Also

- [AD Geometry: Envelopes, Constraint Surfaces, and Poles](../ad_core/03_geometry.md) — the conceptual foundations of envelopes
- **Previous step:** [Step 1: Identify the System's Architecture](step1_identify_multiplicative_structure.md)
- **Next step:** [Step 3: Identify Extremal Dynamics](step3_construct_skyline.md)
- [PDE Atlas: Allen-Cahn Mode 1](../ad_examples/example_PDE_Atlas/AllenCahn/FS_Eval_AllenCahn_02_Mode1_Envelope.md) — a worked example of envelope derivation
