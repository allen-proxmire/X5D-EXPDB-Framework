# X5D Framework FAQ

> **Summary:** Answers to the most common questions about the X5D Framework — what it is, what it is not, how it relates to the Factor Skyline, and how to get involved.

---

### What is the X5D Framework?

X5D is a general, reusable methodology for extracting structure from systems composed of interacting mechanisms. It produces standardized structural profiles — channel decompositions, envelopes, constraint surfaces, pole classifications, and evaluation scores — that enable comparison across domains.

---

### What is X5D *not*?

- X5D is **not a mathematical theory.** It does not prove theorems.
- X5D is **not a collection of proofs.** The proofs belong to the domain-specific theories that X5D analyzes.
- X5D is **not tied to any specific domain.** It applies to PDEs, arithmetic, geometry, dynamical systems, and more.
- X5D is **not a dumping ground** for artifacts from any specific project.

X5D is a *process* — a methodology that produces comparable structural analyses.

---

### How does X5D relate to the Factor Skyline (FS)?

FS is a mathematical theory about the multiplicative structure of the integers. X5D is the methodology that was used to build FS — and was then recognized as general enough to stand alone.

The relationship is:
- **X5D is upstream; FS is downstream.**
- X5D is the process; FS is one product.
- X5D is reusable; FS is specialized.
- FS is one *instance* of X5D applied to a specific system.

---

### Can I apply X5D to my own system?

Yes. X5D is designed to be applied by any practitioner to any system. Follow the six-step process in [`framework/methodology/process/`](../framework/methodology/process/), using the worked examples in [`examples/`](../examples/) as a guide.

---

### What systems has X5D been applied to?

The most developed application is the **PDE Atlas** — structural evaluations of 14 major nonlinear PDEs. The **Factor Skyline** is the originating application (arithmetic/multiplicative structure of integers). The headline X5D worked example is **X5D-EXPDB** — a polyhedral reinterpretation of the Tao–Trudgian–Yang Analytic Number Theory Exponent Database. Future applications to dynamical systems, geometric structures, and computational architectures are planned.

---

### What is a "channel" in X5D?

A channel is an independent mechanism within a system. It is characterized by four properties: locality, linearity, stability role, and scale action. Channels are the atomic building blocks of an architecture. See [`framework/methodology/core/02_pipeline.md`](../framework/methodology/core/02_pipeline.md) for the full taxonomy.

---

### What is an "envelope"?

The envelope is the maximal set of constraints that a system's axioms impose on all admissible states. It includes forbidden configurations, necessary configurations, and quantitative bounds. See [`framework/methodology/core/03_geometry.md`](../framework/methodology/core/03_geometry.md).

---

### What is a "constraint surface"?

The constraint surface is the geometric object in channel space that encodes all structural relationships among the channels. Its faces, closure, and geometry determine the system's qualitative behavior. See [`framework/methodology/core/03_geometry.md`](../framework/methodology/core/03_geometry.md).

---

### What is a "pole"?

A structural pole is a qualitatively distinct region of architectural space where specific channel combinations dominate. Systems near the same pole share qualitative features. Seven poles have been identified from the PDE Atlas. See [`framework/methodology/core/03_geometry.md`](../framework/methodology/core/03_geometry.md).

---

### What are the six X5D criteria?

1. **Minimality** — Are the axioms irreducible?
2. **Locality** — Are all channels local?
3. **Determinism** — Is the future determined?
4. **Generative sufficiency** — Does the theory explain all phenomena?
5. **Envelope tightness** — Are the bounds sharp?
6. **Structural optimality** — Is the architecture free of anomalies?

See [`framework/methodology/core/04_invariants.md`](../framework/methodology/core/04_invariants.md) for full details.

---

### What is an X5D score?

The X5D score is the count of criteria that receive a PASS verdict (0-6). It is a single-number summary of structural quality. A low score does not mean the system is unimportant — it means the system has unresolved structural features.

---

### How do I contribute a new example?

1. Apply the six-step X5D process to your system.
2. Produce the five standard analysis documents.
3. Submit the worked example to [`examples/`](../examples/).

See [`framework/methodology/core/05_examples_overview.md`](../framework/methodology/core/05_examples_overview.md) for guidelines.

---

### Where can I learn more?

- **Core concepts:** [`framework/methodology/core/`](../framework/methodology/core/)
- **Process steps:** [`framework/methodology/process/`](../framework/methodology/process/)
- **Worked examples:** [`examples/`](../examples/)
- **Overview:** [`docs/overview.md`](overview.md)
- **Full methodology:** [`docs/methodology.md`](methodology.md)
