# The EXPDB Skyline Invariant

## Definition (Master Polytope)

Let \( \mathcal{P} \subset \mathbb{R}^5 \) be the polyhedral region with
coordinates \( (\sigma, \tau, \rho, \rho^\*, s) \), defined as:



\[
\mathcal{P}
= \bigcap_{H \in \mathcal{H}_0} C(H) \;\cap\; \mathcal{B},
\]



where:

- \( \mathcal{H}_0 \) is the initial literature hypothesis set,
- \( C(H) \) is the finite family of rational half‑spaces generated from \(H\)
  (via EP → LVER, LV → LVER, ZLV → LVER, raise‑to‑power, etc.),
- \( \mathcal{B} \) is the global bounding box imposed by EXPDB’s truncation
  constants.

All half‑spaces have rational coefficients, so \( \mathcal{P} \) is a rational
polytope (possibly represented as a disjoint union of convex pieces).

---

## Definition (Derived Objects)

Every object computed by EXPDB is a projection, section, envelope, or scalar
extraction of \( \mathcal{P} \). In particular:

- **Large Value Region**  
  

\[
  \mathrm{LV} = \pi_{\sigma,\tau,\rho}(\mathcal{P})
  \]



- **Zeta Large Value Region**  
  

\[
  \mathrm{ZLV} = \pi_{\sigma,\tau,\rho}(\mathcal{P}) \cap \{\tau \ge 2\}
  \]



- **Energy Region**  
  

\[
  \mathrm{EN} = \pi_{\sigma,\tau,\rho^\*}(\mathcal{P})
  \]



- **Zero Density Envelope**  
  

\[
  A(\sigma)
  = \sup_{(\tau,\rho) \in \mathrm{LV}} \frac{\rho}{\tau}
  \]



- **Zero Density Energy Envelope**  
  

\[
  A^\*(\sigma)
  = \frac{1}{1-\sigma}
    \sup_{(\tau,\rho^\*) \in \mathrm{EN}} \frac{\rho^\*}{\tau}
  \]



- **Prime Gap Bound**  
  

\[
  \theta
  = \sup_{\sigma \in [1/2,1)} \max\{\alpha(\sigma), \beta(\sigma)\},
  \]


  where \( \alpha, \beta \) are the standard rational expressions in
  \( A(\sigma) \) and \( A^\*(\sigma) \).

Exponent pairs, beta bounds, and mu bounds arise through classical dualities
and linear images of the same structure.

---

## Definition (EXPDB Skyline)

The **EXPDB Skyline** associated to a hypothesis set \( \mathcal{H}_0 \) is:



\[
\Sigma(\mathcal{H}_0)
=
\bigl(
\partial\mathrm{EP},\;
\beta^\*,\;
\mu^\*,\;
\partial\mathrm{LV},\;
\partial\mathrm{ZLV},\;
\partial\mathcal{P},\;
A,\;
A^\*,\;
\theta
\bigr),
\]



where each component is the boundary, envelope, or hull derived from
\( \mathcal{P} \) via the operations above.

---

## The Skyline Invariant

**Theorem (Skyline Invariant).**  
If \( \mathcal{H}_1 \subseteq \mathcal{H}_2 \), then:



\[
\Sigma(\mathcal{H}_2) \;\preceq\; \Sigma(\mathcal{H}_1)
\]



in the product order (every component becomes tighter).  
Equivalently:

- adding axioms adds half‑spaces,
- half‑spaces shrink \( \mathcal{P} \),
- shrinking \( \mathcal{P} \) tightens all projections and envelopes.

Thus the Skyline is a **monotone invariant** of the hypothesis set.

---

## Fixed Point Property

Let \( \Phi \) be the EXPDB update operator (EP expansion, beta envelope,
mu hull, LV/ZLV/LVER intersection, ZD/ZDE envelopes, prime gap extraction).

Then:

- \( \Phi \) is monotone on the EXPDB state lattice,
- \( \Phi(\Omega) \preceq \Omega \) for all reachable states,
- the descending chain \( \Omega, \Phi(\Omega), \Phi^2(\Omega), \ldots \)
  stabilizes in finitely many steps.

The limit state is exactly the Skyline \( \Sigma(\mathcal{H}_0) \).

---

## Summary

The EXPDB Skyline is the complete geometric signature of the EXPDB pipeline:
a single 5‑dimensional polytope \( \mathcal{P} \) whose shadows and envelopes
produce every analytic bound in the system, and whose refinement under added
axioms is monotone and convergent.
