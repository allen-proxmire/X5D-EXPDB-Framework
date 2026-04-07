# README: The EXPDB Skyline

## Overview

This folder contains the complete geometric reinterpretation of the  
**Exponent Database (EXPDB)** as a **five‑dimensional polyhedral flow**,  
analogous to the FS–EGS reinterpretation of the Erdős–Guy–Selfridge pipeline.

The central result is the **EXPDB Skyline**:  
a single 5D polytope whose projections and envelopes reproduce every analytic  
object in the EXPDB pipeline — exponent pairs, beta bounds, mu bounds,  
large value regions, zero density envelopes, and the prime gap exponent.

This is the **second major example** of the **Factor Skyline (FS)** framework.

---

## Contents

### `EXPDB-Skyline_A-Polyhedral-Reinterpretation.md`
A full research paper presenting:

- the EXPDB pipeline as a polyhedral computation engine  
- the master polytope \( \mathcal{P} \subset \mathbb{R}^5 \)  
- the projection/envelope ladder \( \mathbb{R}^5 \to \mathbb{R}^3 \to \mathbb{R}^1 \to \mathbb{R}^0 \)  
- the EXPDB Skyline invariant  
- the monotone contraction flow and fixed‑point theorem  
- the structural comparison with the FS–EGS reinterpretation  
- consequences, dualities, and future directions  

This paper is the authoritative description of the EXPDB Skyline.

---

### `invariant.md`
A concise, standalone definition of the **EXPDB Skyline invariant**:

- the master polytope  
- all derived objects as projections/envelopes  
- the Skyline tuple  
- the monotonicity theorem  
- the fixed‑point property  

This file mirrors the role of `invariant.md` in the FS–EGS folder.

---

## Relation to the Factor Skyline (FS)

The EXPDB Skyline is the second demonstration of the FS method:

1. **FS–EGS** — reinterpretation of the Erdős–Guy–Selfridge pipeline  
2. **EXPDB Skyline** — reinterpretation of the Exponent Database  
3. **(forthcoming)** ED Skyline — reinterpretation of the Erdős Discrepancy pipeline  

Together, these examples show that many analytic pipelines can be understood  
as **flows on rational polyhedral regions**, with:

- axioms → half‑spaces  
- intersection → master region  
- projection → lower‑dimensional shadows  
- envelope → boundary functions  
- scalar extraction → final bound  

The EXPDB Skyline extends this paradigm to analytic number theory.

---

## Status

This folder is complete and stable:

- full paper written  
- invariant extracted  
- structure aligned with FS–EGS  
- ready for citation, discussion, and outreach  

The next step is to open a GitHub Issue on the EXPDB repository presenting  
the Skyline reinterpretation.
