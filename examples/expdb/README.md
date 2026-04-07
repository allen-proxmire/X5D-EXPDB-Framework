# X5D-EXPDB

## Overview

This folder contains the **X5D reinterpretation of EXPDB** — the
Tao–Trudgian–Yang Analytic Number Theory Exponent Database — as a
five‑dimensional polyhedral flow.

The central result, **X5D-EXPDB**, is a single 5D polytope
\( \mathcal{P} \subset \mathbb{R}^5 \) whose projections and envelopes
reproduce every analytic object in the EXPDB pipeline — exponent pairs,
beta bounds, mu bounds, large value regions, zero density envelopes, and
the prime gap exponent.

This is the first major worked example of the **X5D framework**.

---

## Contents

### `X5D_EXPDB_Reinterpretation.md`

A full research paper presenting:

- the EXPDB pipeline as a polyhedral computation engine
- the master polytope \( \mathcal{P} \subset \mathbb{R}^5 \)
- the projection/envelope ladder \( \mathbb{R}^5 \to \mathbb{R}^3 \to \mathbb{R}^1 \to \mathbb{R}^0 \)
- the X5D-EXPDB invariant
- the monotone contraction flow and fixed‑point theorem
- consequences, dualities, and future directions

This paper is the authoritative description of X5D-EXPDB.

### `invariant.md`

A concise, standalone definition of the **X5D-EXPDB invariant**:

- the master polytope
- all derived objects as projections/envelopes
- the X5D signature
- the monotonicity theorem
- the fixed‑point property

### `analysis/`

Empirical analysis of the EXPDB pipeline after incorporating the
Guth–Maynard (2024) large value estimate. Establishes the binding cusp
at \( \sigma^* = 7/10 \) and the prime-gap exponent
\( \theta_{\mathrm{PNTALL}} = 17/30 \). See `analysis/README.md`.

### `NEXT_STEPS.md`

Project notes on extending the binding-constraint analysis.

---

## Relation to the X5D Framework

X5D-EXPDB is the first major worked example of the X5D framework
(see `../../framework/X5D_Framework.md`). It demonstrates that an
analytic pipeline can be understood as a **flow on a rational polyhedral
region**, with:

- axioms → half‑spaces
- intersection → master region
- projection → lower‑dimensional shadows
- envelope → boundary functions
- scalar extraction → final bound

X5D-EXPDB extends this paradigm to analytic number theory.

---

## Computational Pipeline

The computational pipeline that generates the data and figures lives in
`../../compute/`. See `../../compute/README.md` for details.
