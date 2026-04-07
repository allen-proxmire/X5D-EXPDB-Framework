# Step 5: Validate and Evaluate

> **Summary:** Evaluate the distilled architecture against the six AD criteria (minimality, locality, determinism, generative sufficiency, envelope tightness, structural optimality), build a reproducibility harness, and cross-check against known domain-specific results.

---

## Overview

Step 5 validates the distillation by evaluating the architecture against the six AD criteria and verifying the results through a reproducibility harness. This step ensures that the distillation is correct, complete, and independently verifiable.

---

## 5.1 Evaluate Against the Six Criteria

Apply each of the six AD evaluation criteria to the distilled architecture:

| Criterion | Question | Verdict |
|---|---|---|
| **Minimality** | Are the axioms irreducible? | PASS / CONDITIONAL / FAIL |
| **Locality** | Are all channels local? | PASS / CONDITIONAL / FAIL |
| **Determinism** | Is the future determined by the past? | PASS / CONDITIONAL / FAIL |
| **Generative sufficiency** | Does the architecture generate all observed phenomena? | PASS / CONDITIONAL / FAIL |
| **Envelope tightness** | Are the bounds sharp and the envelope closed? | PASS / CONDITIONAL / FAIL |
| **Structural optimality** | Is it free of anomalies and maximally economical? | PASS / CONDITIONAL / FAIL |

For each criterion, provide:
- The verdict (PASS, CONDITIONAL, or FAIL).
- A brief justification citing specific structural features.
- If CONDITIONAL or FAIL, identify the specific structural feature responsible.

Compute the AD score (total PASSes, 0–6).

---

## 5.2 Build a Reproducibility Harness

A reproducibility harness ensures that every numerical or structural claim in the distillation can be independently verified. The harness should follow these principles:

### Design Principles

- **Deterministic seeding:** All random processes use fixed seeds, guaranteeing identical output across runs, machines, and platforms.
- **Timestamped outputs:** Each run creates a new output directory named with the current timestamp. Old runs are never overwritten or deleted.
- **Structured output:** Each verification produces a structured output file (JSON or equivalent) containing computed results, expected values, and pass/fail status.
- **Single entry point:** A single script runs all verifications in sequence and produces a summary report.
- **Isolation:** Each verification is independent — failure of one does not prevent others from running.

### Harness Structure

A typical reproducibility harness contains:

```
reproducibility/
  run_all.py           # Entry point — runs all verifications
  scripts/             # Core computational scripts
  tables/              # Individual verification scripts (one per claim)
  tables/output/       # Timestamped output directories
  utils/               # Shared utility modules
  notebooks/           # Interactive exploration and visualization
  README.md            # Documentation of the harness
```

### What to Verify

- Every envelope inequality (is the bound correct? is it sharp?).
- Every conservation identity (does the quantity remain constant?).
- Every threshold condition (does the bifurcation occur at the stated value?).
- Every attractor identification (do generic trajectories converge to the stated form?).
- Every channel classification (does each channel behave as described?).

---

## 5.3 Cross-Check with Known Results

Verify that the distillation is consistent with established domain-specific results:

- Do the envelope inequalities match known theorems?
- Does the pole assignment match the system's known qualitative behavior?
- Are there known results that the distillation fails to capture?

Any discrepancy should be investigated and resolved before finalizing the distillation.

---

## 5.4 Output of Step 5

- A completed evaluation table with all six criterion verdicts and justifications.
- An AD score (0–6).
- A reproducibility harness (or documentation of how to build one for this system).
- A cross-check report against known domain-specific results.

---

## 5.5 Checklist

- [ ] All six criteria evaluated with verdicts and justifications
- [ ] AD score computed
- [ ] Reproducibility harness designed or implemented
- [ ] All numerical/structural claims independently verifiable
- [ ] Cross-check against known results completed
- [ ] Any discrepancies investigated and resolved

---

## See Also

- [AD Invariants: Evaluation Criteria](../ad_core/04_invariants.md) — the full treatment of the six criteria
- **Previous step:** [Step 4: Construct the Constraint Surface](step4_distill_invariants.md)
- **Next step:** [Step 6: Generalize and Extend](step6_generalize.md)
- [PDE Atlas: Allen-Cahn AD Criteria](../ad_examples/example_PDE_Atlas/AllenCahn/FS_Eval_AllenCahn_05_FS_Criteria_Verdict.md) — a worked example of criteria evaluation
