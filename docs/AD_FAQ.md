# AD Frequently Asked Questions

> **Summary:** Answers to the most common questions about AD — what it is, what it is not, how it relates to the Factor Skyline, and how to get involved.

---

### What is Architectural Distillation (AD)?

AD is a general, reusable methodology for extracting structure from systems composed of interacting mechanisms. It produces standardized structural profiles — channel decompositions, envelopes, constraint surfaces, pole classifications, and evaluation scores — that enable comparison across domains.

---

### What is AD *not*?

- AD is **not a mathematical theory.** It does not prove theorems.
- AD is **not a collection of proofs.** The proofs belong to the domain-specific theories that AD analyzes.
- AD is **not tied to any specific domain.** It applies to PDEs, arithmetic, geometry, dynamical systems, and more.
- AD is **not a dumping ground** for artifacts from any specific project.

AD is a *process* — a methodology that produces comparable structural analyses.

---

### How does AD relate to the Factor Skyline (FS)?

FS is a mathematical theory about the multiplicative structure of the integers. AD is the methodology that was used to build FS — and was then recognized as general enough to stand alone.

The relationship is:
- **AD is upstream; FS is downstream.**
- AD is the process; FS is one product.
- AD is reusable; FS is specialized.
- FS is one *instance* of AD applied to a specific system.

---

### Can I apply AD to my own system?

Yes. AD is designed to be applied by any practitioner to any system. Follow the six-step process in `ad_process/`, using the worked examples in `ad_examples/` as a guide.

---

### What systems has AD been applied to?

The most developed application is the **PDE Atlas** — structural evaluations of 14 major nonlinear PDEs. The **Factor Skyline** is the originating application (arithmetic/multiplicative structure of integers). Future applications to dynamical systems, geometric structures, and computational architectures are planned.

---

### What is a "channel" in AD?

A channel is an independent mechanism within a system. It is characterized by four properties: locality, linearity, stability role, and scale action. Channels are the atomic building blocks of an architecture. See `ad_core/02_pipeline.md` for the full taxonomy.

---

### What is an "envelope"?

The envelope is the maximal set of constraints that a system's axioms impose on all admissible states. It includes forbidden configurations, necessary configurations, and quantitative bounds. See `ad_core/03_geometry.md`.

---

### What is a "constraint surface"?

The constraint surface is the geometric object in channel space that encodes all structural relationships among the channels. Its faces, closure, and geometry determine the system's qualitative behavior. See `ad_core/03_geometry.md`.

---

### What is a "pole"?

A structural pole is a qualitatively distinct region of architectural space where specific channel combinations dominate. Systems near the same pole share qualitative features. Seven poles have been identified from the PDE Atlas. See `ad_core/03_geometry.md`.

---

### What are the six AD criteria?

1. **Minimality** — Are the axioms irreducible?
2. **Locality** — Are all channels local?
3. **Determinism** — Is the future determined?
4. **Generative sufficiency** — Does the theory explain all phenomena?
5. **Envelope tightness** — Are the bounds sharp?
6. **Structural optimality** — Is the architecture free of anomalies?

See `ad_core/04_invariants.md` for full details.

---

### What is an AD score?

The AD score is the count of criteria that receive a PASS verdict (0-6). It is a single-number summary of structural quality. A low score does not mean the system is unimportant — it means the system has unresolved structural features.

---

### How do I contribute a new example?

1. Apply the six-step AD process to your system.
2. Produce the five standard analysis documents.
3. Submit the worked example to `ad_examples/`.

See `ad_core/05_examples_overview.md` for guidelines.

---

### Where can I learn more?

- **Core concepts:** `ad_core/`
- **Process steps:** `ad_process/`
- **Worked examples:** `ad_examples/`
- **Overview:** `docs/AD_overview.md`
- **Full methodology:** `docs/AD_methodology.md`
