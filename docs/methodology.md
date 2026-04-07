# X5D Methodology: The Complete Process

> **Summary:** The complete, end-to-end X5D process in one document. Covers all six steps, the six evaluation criteria, the standard five-document output, and how to apply the X5D Framework to a new system.

---

## 1. Summary

The X5D methodology transforms a system into a standardized structural profile through six steps:

```
Step 1: Identify the Architecture
    ↓
Step 2: Derive the Envelope (Mode 1)
    ↓
Step 3: Identify Extremal Dynamics (Mode 2)
    ↓
Step 4: Construct the Constraint Surface (Mode 3)
    ↓
Step 5: Validate and Evaluate
    ↓
Step 6: Generalize and Extend
```

Each step builds on the previous one. Steps 1-4 are the core analysis. Step 5 is verification. Step 6 feeds back into the framework.

---

## 2. Step-by-Step

### Step 1: Identify the Architecture

**Input:** A system (PDE, dynamical system, geometric structure, arithmetic process, etc.)

**Process:**
- Identify the system's axioms (structural, constitutive, domain).
- Decompose into independent channels.
- Classify each channel by locality, linearity, stability role, and scale action.

**Output:** Axiom list + channel decomposition table.

See [`framework/methodology/process/step1_identify_multiplicative_structure.md`](../framework/methodology/process/step1_identify_multiplicative_structure.md) for full details.

### Step 2: Derive the Envelope (Mode 1)

**Input:** Axioms and channels from Step 1.

**Process:**
- Identify forbidden configurations (what the axioms exclude).
- Identify necessary configurations (what the axioms force).
- Derive envelope inequalities (conservation identities, dissipation identities, contraction inequalities, regularity bounds, threshold conditions).
- Assess envelope closure (closed, partially open, open).

**Output:** Forbidden/necessary configurations + envelope inequality table + closure assessment.

See [`framework/methodology/process/step2_extract_axes.md`](../framework/methodology/process/step2_extract_axes.md) for full details.

### Step 3: Identify Extremal Dynamics (Mode 2)

**Input:** Envelope from Step 2.

**Process:**
- Identify extremal behavior types (spreading, shock, soliton, concentration, extinction, etc.).
- Catalog universal inequalities.
- Identify attractor type(s).

**Output:** Extremal behavior catalog + universal inequality table + attractor identification.

See [`framework/methodology/process/step3_construct_skyline.md`](../framework/methodology/process/step3_construct_skyline.md) for full details.

### Step 4: Construct the Constraint Surface (Mode 3)

**Input:** Channels from Step 1, envelope from Step 2, extremal dynamics from Step 3.

**Process:**
- Define the channel space.
- Identify faces of the constraint surface.
- Assess closure (sealed vs. open faces).
- Classify the surface type (contracting, isoenergetic, entropy-resolved, geometrically dissipative, mass-stratified).
- Characterize dissipation geometry.
- Assign to a structural pole.

**Output:** Constraint-surface description + closure assessment + surface-type classification + pole assignment.

See [`framework/methodology/process/step4_distill_invariants.md`](../framework/methodology/process/step4_distill_invariants.md) for full details.

### Step 5: Validate and Evaluate

**Input:** Complete analysis from Steps 1-4.

**Process:**
- Evaluate against six X5D criteria (minimality, locality, determinism, generative sufficiency, envelope tightness, structural optimality).
- Build reproducibility harness.
- Cross-check against known domain-specific results.

**Output:** Six-criteria evaluation table + X5D score + reproducibility harness.

See [`framework/methodology/process/step5_validate.md`](../framework/methodology/process/step5_validate.md) for full details.

### Step 6: Generalize and Extend

**Input:** Complete evaluated distillation from Step 5.

**Process:**
- Compare with previously distilled systems.
- Identify transferable results.
- Propose taxonomy extensions (new channels, poles, surface types).
- Localize open problems to specific structural features.

**Output:** Comparison report + transferable results + taxonomy proposals + open-problem localization.

See [`framework/methodology/process/step6_generalize.md`](../framework/methodology/process/step6_generalize.md) for full details.

---

## 3. The Six Evaluation Criteria

| # | Criterion | Measures | PASS means |
|---|---|---|---|
| 1 | **Minimality** | Economy | Axioms are irreducible; zero non-minimal elements |
| 2 | **Locality** | Simplicity | All channels are local |
| 3 | **Determinism** | Predictability | Global well-posedness unconditionally |
| 4 | **Generative sufficiency** | Completeness | All phenomena derived from axioms |
| 5 | **Envelope tightness** | Sharpness | All bounds sharp, envelope fully closed |
| 6 | **Structural optimality** | Elegance | Zero anomalies, maximally economical |

**Scoring:** Each criterion receives PASS, CONDITIONAL, or FAIL. The X5D score is the count of PASSes (0-6).

---

## 4. The Standard Output

A complete X5D analysis produces four standard documents:

1. **Architectural Specification** — axioms, channels, structural commitments (Step 1)
2. **Mode 1: Envelope** — forbidden/necessary configurations, inequalities, closure (Step 2)
3. **Mode 2: Extremal Dynamics** — extremal behaviors, universal inequalities, attractors (Step 3)
4. **Mode 3: Constraint Surface** — geometry, faces, closure, dissipation, pole (Step 4)

Plus an evaluation document:

5. **Criteria and Verdict** — six-criteria assessment and X5D score (Step 5)

These five documents constitute a complete *atlas entry* — a standardized structural profile that can be compared with any other entry.

---

## 5. Applying X5D to a New System

To distill a new system:

1. Choose a system you want to analyze.
2. Follow Steps 1-6 in order.
3. Produce the five standard documents.
4. Submit to the appropriate X5D atlas (or create a new one).

The process is designed to be self-contained: everything needed is in [`framework/methodology/core/`](../framework/methodology/core/) (concepts) and [`framework/methodology/process/`](../framework/methodology/process/) (steps). The worked examples in [`examples/`](../examples/) demonstrate the methodology applied to real systems.
