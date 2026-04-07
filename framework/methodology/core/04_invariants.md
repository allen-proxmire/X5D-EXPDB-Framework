# AD Invariants: Evaluation Criteria

> **Summary:** This document defines the six criteria used to evaluate a distilled architecture: minimality, locality, determinism, generative sufficiency, envelope tightness, and structural optimality. Each criterion measures a distinct dimension of architectural quality, producing a standardized AD score from 0 to 6.

---

## 1. Purpose of Evaluation

After an architecture has been distilled — its channels identified, its envelope derived, its constraint surface constructed — it is evaluated against a set of structural criteria. These criteria measure the *quality* of the architecture as a structural object, independent of its physical importance or practical utility.

The evaluation produces a structural profile: a standardized assessment that can be compared with any other distilled system. The criteria are not pass/fail tests for the system's importance — they are measurements of its structural properties.

---

## 2. The Six Evaluation Criteria

### 2.1 Minimality

*Is this architecture the simplest it can be?*

An architecture is minimal if its axioms are irreducible — each axiom is independent (not derivable from the others), and each is necessary (removing it changes the qualitative architecture). Non-minimal elements include constitutive selections (choosing a specific form when a general class would work), domain restrictions (restricting to a specific setting when the system could be formulated more broadly), and redundant axioms (axioms that are consequences of others).

The strongest minimality belongs to architectures with zero adjustable parameters — the system is fully determined by its structural commitments alone.

### 2.2 Locality

*Is everything local?*

An architecture passes locality if every channel depends only on the state and its derivatives at each point. This is the strongest form of structural locality — no integral operators, no global solves, no coupling between distant points.

When nonlocal channels are present, their *role* matters. A nonlocal constraint-enforcement mechanism (structural inconvenience) is less consequential than a nonlocal driving mechanism (dynamical driver).

### 2.3 Determinism

*Is the future determined by the past?*

Do admissible trajectories exist globally in time, are they unique, and do they depend continuously on initial conditions? The answer varies across systems:

- **Unconditional global determinism:** Smooth or appropriate weak solutions exist for all time, are unique, and are continuously dependent on initial data.
- **Conditional/regime-dependent determinism:** Determinism holds in some regimes but not others — either singularities occur for some data, or the theory is essentially but not fully complete.
- **Open determinism:** Whether smooth solutions exist globally is unresolved.

### 2.4 Generative Sufficiency

*Does the architecture generate all its observed phenomena from the axioms?*

This measures completeness: does the theory account for everything the system does, or are there observed behaviors the theory cannot explain?

The strongest generative sufficiency belongs to architectures where every phenomenon is rigorously derived from the axioms with exact formulas. Most systems have small but nonzero generative gaps — specific features whose derivation is incomplete.

### 2.5 Envelope Tightness

*Are the bounds sharp, and is the envelope fully closed?*

A tight envelope has sharp inequalities (each bound is achieved by some admissible state) and a fully closed constraint surface (no open faces). The tightest envelopes belong to architectures whose theory is most complete — every bound saturated by a canonical profile.

An envelope is less tight when it has open faces, when some bounds are known to be suboptimal, or when closure is regime-dependent.

### 2.6 Structural Optimality

*Is the architecture free of anomalies, and is it the simplest system generating its dynamics?*

An anomaly is a structural feature that is both *necessary* (forced by the axioms) and *potentially destructive* (threatening self-consistency). Anomaly-free architectures are maximally economical — the simplest systems that generate their respective dynamics.

---

## 3. Why These Six

The six criteria capture the six fundamental dimensions of architectural quality:

| Criterion | Dimension |
|---|---|
| Minimality | Economy — is the architecture lean? |
| Locality | Simplicity — is it free of nonlocal entanglement? |
| Determinism | Predictability — is the future determined? |
| Generative sufficiency | Completeness — does the theory explain everything? |
| Envelope tightness | Sharpness — are the bounds optimal? |
| Structural optimality | Elegance — is it the best of its kind? |

Together, these measure the *structural soundness* of an architecture. An architecture can be practically important but structurally flawed. An architecture can be structurally perfect but practically simple. The criteria measure structural quality, not domain importance.

---

## 4. Scoring

Each criterion receives a verdict: **PASS**, **CONDITIONAL**, or **FAIL**.

- **PASS:** The criterion is satisfied unconditionally.
- **CONDITIONAL:** The criterion is satisfied in some regimes or under specific assumptions.
- **FAIL:** The criterion is not satisfied, or the answer is unknown.

The total number of PASSes is the architecture's *AD score*, ranging from 0 to 6. The score provides a single-number summary of structural quality, while the individual criterion verdicts provide the detailed profile.

---

## 5. Using the Evaluation

The evaluation is not a ranking of importance — it is a structural diagnostic. Systems with low scores are not "bad" — they may be the most physically important or mathematically deep. The evaluation reveals *where* the structural challenges lie: which criteria fail, which faces are open, which generative gaps remain.

This diagnostic function is the evaluation's primary value: it localizes difficulty to specific structural features, guiding research toward the precise mechanisms that need resolution.

---

## See Also

- [AD Geometry: Envelopes, Constraint Surfaces, and Poles](03_geometry.md) — the structures being evaluated
- [Step 5: Validate and Evaluate](../ad_process/step5_validate.md) — how to apply these criteria in practice
- [PDE Atlas](../ad_examples/example_PDE_Atlas/README.md) — 14 worked examples of criteria evaluation
