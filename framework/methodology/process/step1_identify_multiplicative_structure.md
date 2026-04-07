# Step 1: Identify the System's Architecture

> **Summary:** Identify the system's axioms (structural, constitutive, domain) and decompose it into independent channels, each classified by locality, linearity, stability role, and scale action. This step produces the foundation on which all subsequent analysis builds.

---

## Overview

The first step of Architectural Distillation is to identify the system's structural commitments — the axioms that define what the system is and what it can do. This step produces two outputs: a list of axioms and a channel decomposition.

---

## 1.1 Identify the Axioms

Every system rests on a set of structural commitments — assumptions, constraints, and constitutive laws that define its architecture. These axioms are not always stated explicitly; part of the distillation process is making them visible.

**Types of axioms:**

- **Structural axioms:** The fundamental mathematical commitments (continuity, locality, conservation, symmetry, unique factorization, total order).
- **Constitutive axioms:** Specific choices within a structural class (a particular potential, a particular mobility, a particular metric).
- **Domain axioms:** Restrictions on the setting (Euclidean space, compact manifold, periodic boundary, finite set).

**How to identify axioms:**

1. Write down the system's defining equations or rules.
2. For each term, ask: *What structural commitment does this term represent?*
3. For each constraint, ask: *Is this forced by the structure, or is it a choice?*
4. Separate structural axioms (irreducible) from constitutive axioms (replaceable).

The goal is a *minimal* axiom set — each axiom independent, each necessary, none redundant.

---

## 1.2 Decompose into Channels

Once the axioms are identified, decompose the system into its independent mechanisms — the channels.

**How to decompose:**

1. Identify each independent mechanism that drives the system's behavior.
2. Classify each channel by its four properties: locality, linearity, stability role, and scale action.
3. Verify independence: each channel should have a definite structural character that is independent of the other channels.
4. Verify completeness: the channels together should account for all terms in the system's defining equations or rules.

**Output of Step 1:**

- A numbered list of axioms, classified as structural, constitutive, or domain.
- A channel decomposition table listing each channel, its type, and its four properties.
- A brief narrative explaining the architecture's structural commitments.

---

## 1.3 Checklist

- [ ] All axioms identified and classified
- [ ] Structural vs. constitutive axioms distinguished
- [ ] Channel decomposition complete
- [ ] Each channel classified by locality, linearity, stability role, scale action
- [ ] Independence and completeness verified
- [ ] Narrative written explaining the architecture

---

## See Also

- [AD Pipeline: Channels as Building Blocks](../ad_core/02_pipeline.md) — the full channel taxonomy and properties
- [AD Principles](../ad_core/01_principles.md) — why architectural decomposition matters
- **Next step:** [Step 2: Derive the Envelope](step2_extract_axes.md)
- [PDE Atlas: Allen-Cahn Architectural Specification](../ad_examples/example_PDE_Atlas/AllenCahn/FS_Eval_AllenCahn_01_ArchitectureSpec.md) — a worked example of Step 1
