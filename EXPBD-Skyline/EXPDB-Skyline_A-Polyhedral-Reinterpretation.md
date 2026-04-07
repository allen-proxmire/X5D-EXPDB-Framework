# The EXPDB Skyline: A Polyhedral Reinterpretation of the Exponent Database as a Five-Dimensional Geometric Flow

---

## 1. Introduction

### 1.1 The Exponent Database

The Analytic Number Theory Exponent Database (EXPDB) is a computational
system, initiated by Tao, Trudgian, and Yang [TTY25], that mechanizes the
derivation of bounds on exponents arising throughout analytic number theory.
It records, in both human-readable and executable form, a corpus of
literature results — exponent pairs, bounds on exponential sum growth rates,
large value estimates, zero density estimates, additive energy estimates, and
others — together with the network of transformations that relate them.
Given an input set of axioms drawn from the published literature, EXPDB
applies a cascade of transformations and produces, as output, the tightest
bounds derivable from those axioms.

The system is implemented as approximately 10,700 lines of Python, organized
into 24 modules.  Its core data structure is the *Hypothesis* object: a typed
mathematical assertion carrying a data payload, a human-readable proof, a
bibliographic reference, and a dependency set linking it to the hypotheses
from which it was derived.  The system supports ten hypothesis types:

> Upper bound on beta, Exponent pair, Exponent pair transform, Upper bound
> on mu, Large value estimate, Zeta large value estimate, Zero density
> estimate, Zero density energy estimate, Large value energy region, Large
> value energy region transform.

Each type has its own geometric representation — points, affine functions,
polytopes, regions, rational functions — and its own family of
transformations.  The full pipeline chains these transformations across types,
from exponent pairs and literature bounds at the top to prime gap estimates
at the bottom.

The architecture of EXPDB is procedural: derivation routines call
transformation functions in a prescribed sequence, accumulating new
hypotheses in a mutable set.  The present paper proposes an alternative
perspective.  We argue that the entire pipeline operates, at every stage, on
projections and envelopes of a single geometric object — a five-dimensional
polyhedral region — and that this reinterpretation clarifies the system's
convergence behavior, its information-theoretic structure, and its points of
contact with other geometric frameworks in number theory.


### 1.2 The Geometric Thesis

The central claim of this paper is:

> **Thesis.**  There exists a convex polytope $\mathcal{P} \subset \mathbb{R}^5$,
> defined as the intersection of finitely many rational half-spaces, such that
> every object computed by the EXPDB pipeline — exponent pair hulls, beta
> envelopes, mu hulls, large value regions, zeta large value regions, zero
> density estimates, zero density energy estimates, and prime gap bounds —
> arises as a projection, section, envelope, or scalar extraction of
> $\mathcal{P}$.

The five coordinates of the ambient space are $(\sigma, \tau, \rho, \rho^*, s)$,
corresponding to the variables that parameterize the *large value energy
region* (LVER), the highest-dimensional object in the EXPDB type system.
Concretely, $\mathcal{P}$ is the feasible set of all five-tuples
$(\sigma, \tau, \rho, \rho^*, s)$ that are simultaneously consistent with every
constraint derivable from the input hypotheses.  The system already computes
$\mathcal{P}$ — it is the output of the function `compute_best_lver` in the
module `additive_energy.py` — but it has not previously been identified as
the single object from which all other objects descend.

The claim is not merely that $\mathcal{P}$ exists in a formal sense.  It is
that the specific computational operations performed by EXPDB — the convex
hull of exponent pairs, the lower envelope of beta bounds, the intersection
of large value regions, the supremum of $\rho/\tau$ over polytope edges —
are all instances of three generic operations applied to $\mathcal{P}$:

1. **Projection**: dropping coordinates to obtain a lower-dimensional
   shadow.  The large value region is $\pi_{\sigma,\tau,\rho}(\mathcal{P})$;
   the energy region is $\pi_{\sigma,\tau,\rho^*}(\mathcal{P})$.

2. **Rational supremum**: computing $\sup_\tau\{\rho/\tau\}$ over a
   projected region, which extracts a piecewise-rational function of $\sigma$
   from a three-dimensional polyhedral shadow.

3. **Lower envelope**: taking the pointwise minimum over a family of such
   functions, yielding the tightest bound as a function of $\sigma$.

Every bound that EXPDB produces can be written as a composition of these
three operations.  The full derivation chain, from literature axioms to prime
gap bounds, is a sequence

$$
\mathcal{P} \;\subset\; \mathbb{R}^5
\;\;\xrightarrow{\;\pi\;}\;\;
R \;\subset\; \mathbb{R}^3
\;\;\xrightarrow{\;\sup\rho/\tau\;}\;\;
f(\sigma) \;\in\; \mathrm{Rat}([{\tfrac{1}{2}},1])
\;\;\xrightarrow{\;\inf\;}\;\;
f^*(\sigma)
\;\;\xrightarrow{\;\sup_\sigma\;}\;\;
\theta \;\in\; \mathbb{R}
$$

that descends the *dimension ladder* $\mathbb{R}^5 \to \mathbb{R}^3 \to
\mathbb{R}^1 \to \mathbb{R}^0$.  We call the collection of boundary
functions obtained at each stage the *EXPDB Skyline*, and we show that the
Skyline is a monotone invariant of a contraction flow on a product lattice.


### 1.3 Why a Geometric Reinterpretation?

The procedural description of EXPDB — "apply transform A, then transform B,
then take the intersection, then project" — is operationally complete but
leaves several structural questions unanswered.

**Convergence.**  The pipeline contains two feedback loops (exponent pairs
$\leftrightarrow$ beta bounds, and LVER $\to$ LV $\to$ LVER).  Why do these
loops terminate, and what is the limiting object?  The polyhedral
reinterpretation answers this directly: the loops correspond to alternating
projections and liftings of $\mathcal{P}$, and they converge because
$\mathcal{P}$ is a fixed point of the composition.

**Information loss.**  The pipeline produces bounds of decreasing
dimensionality: five-dimensional regions, three-dimensional regions,
one-dimensional functions, and finally a single scalar.  How much
information is lost at each stage?  The Skyline framework makes this
precise: each projection discards exactly those constraints that involve the
dropped coordinates, and the loss is irreversible (the three-dimensional
shadow does not determine $\mathcal{P}$).

**Duality.**  The exponent pair hull and the beta envelope are related by a
classical projective duality (point $\leftrightarrow$ tangent line), but
this duality has not been connected to the higher-dimensional polyhedral
structure.  The Skyline framework embeds this duality into a
section-projection adjunction between $\mathbb{R}^2$ and $\mathbb{R}^5$.

**Optimality.**  Given a fixed set of literature axioms, is the EXPDB
pipeline extracting the tightest bounds possible, or is there slack?  The
polyhedral framework gives a precise answer: the bounds are optimal *among
those derivable from the available half-spaces defining $\mathcal{P}$*.
Improving the bounds requires either adding new half-spaces (new literature
results) or changing the coordinate system (new auxiliary variables).

**Comparison with other frameworks.**  The Factor Skyline project [ET]
performs an analogous geometric reinterpretation for multiplicative number
theory.  A unified description of both Skylines — as monotone flows on
rational polyhedra — requires the kind of coordinate-free geometric language
that the present paper develops.


### 1.4 Scope and Limitations

We emphasize what this paper does and does not do.

We *do* provide a complete structural analysis of the EXPDB codebase,
identifying every module, transformation, and data flow.  We *do* define the
master polytope $\mathcal{P}$ and show that all EXPDB objects are derived
from it.  We *do* formalize the Skyline as a monotone invariant and prove
its convergence.  We *do* classify the transformations by their geometric
type (linear, affine, nonlinear; convexity-preserving or not;
monotone or not) and identify dualities, envelopes, and fixed points.

We do *not* engage with the underlying mathematics of analytic number theory.
The reader need not know what an exponent pair "means" or why zero density
estimates are useful.  Our analysis is purely geometric and computational:
we treat EXPDB as a pipeline of polyhedral operations on rational data, and
we characterize its behavior in those terms.  All references to coordinates
$(\sigma, \tau, \rho, \rho^*, s)$ should be understood as abstract parameters
of a five-dimensional ambient space, not as the analytic quantities they
represent in number theory.

We also do *not* propose modifications to EXPDB.  Our reinterpretation is
descriptive, not prescriptive.  We identify several points where the
existing pipeline might benefit from the polyhedral perspective (automated
$\tau_0$ selection, higher-dimensional lifting, Huxley subdivision), but we
leave these as directions for future work.


### 1.5 Relation to Prior Work

The EXPDB system itself is described in [TTY25], which also establishes
several new results obtained through the database.  The computational
infrastructure relies on `pycddlib` [F] for exact rational polytope
arithmetic (H-representation, V-representation, vertex enumeration via the
double description method) and `sympy` [MSP+17] for symbolic manipulation
of rational functions.  The system interfaces with Lean 4 for formal
verification of selected bounds, though this aspect is not part of the
present analysis.

The idea of reinterpreting a derivation system as geometry on a polyhedral
object has precedents in several areas.  In optimization, the feasible set
of a linear program is a polytope whose vertices correspond to basic
feasible solutions; the simplex method traverses the edge graph of this
polytope.  In tropical geometry, valuations of algebraic varieties produce
polyhedral complexes whose combinatorics encode algebraic information.  In
the theory of Newton polytopes, the exponents of a multivariate polynomial
form a polytope whose faces control the polynomial's asymptotic behavior.

The closest precedent within number theory is the Factor Skyline framework
[ET], which reinterprets multiplicative number theory bounds as projections
of a polyhedral region.  We compare the two frameworks in Section 9.


### 1.6 Outline

The remainder of the paper is organized as follows.

**Section 2** (not included in this draft) will provide notation and
conventions for polyhedral geometry over the rationals.

**Section 3** describes the EXPDB pipeline as a computational system:
its type system, transformation catalog, orchestration layer, and data
representations.

**Section 4** defines the master polytope $\mathcal{P} \subset \mathbb{R}^5$
and establishes its properties (rationality, convexity, monotone dependence
on axioms).

**Section 5** shows that every EXPDB object — EP hulls, beta envelopes, mu
hulls, LV regions, ZLV regions, ZD envelopes, ZDE envelopes, and prime gap
bounds — is a projection, section, or envelope of $\mathcal{P}$, and
describes the specific operation in each case.

**Section 6** defines the EXPDB Skyline formally, proves it is a monotone
invariant of the pipeline, and establishes convergence to a fixed point.

**Section 7** develops consequences: the dimension ladder, the duality web,
the flow structure, and the fixed-point hierarchy.

**Section 8** compares the EXPDB Skyline with the Factor Skyline.

**Section 9** discusses future directions, including algorithmic
improvements, formal verification opportunities, and open questions.

**Appendix A** provides a complete mapping from code modules and functions
to the geometric operations described in the paper, enabling readers to
trace every claim back to the source code.

## 2. Preliminaries: Polyhedral Geometry over the Rationals

This section fixes notation and collects the definitions from polyhedral
geometry and piecewise-function theory that are needed in the sequel.  All
objects are defined over the rational field $\mathbb{Q}$; this reflects the
exact-arithmetic design of EXPDB, which uses the `pycddlib` library with
`number_type="fraction"` throughout.  No floating-point approximation
enters any intermediate computation.


### 2.1 Polytopes

**Definition 2.1** (Half-space).
A *rational half-space* in $\mathbb{R}^d$ is a set of the form
$$
H^+ = \bigl\{ x \in \mathbb{R}^d : a_0 + a_1 x_1 + \cdots + a_d x_d \ge 0 \bigr\}
$$
where $a_0, a_1, \ldots, a_d \in \mathbb{Q}$.  We encode $H^+$ as the row
vector $(a_0, a_1, \ldots, a_d) \in \mathbb{Q}^{d+1}$.  The *bounding
hyperplane* of $H^+$ is $\partial H^+ = \{x : a_0 + a^T x = 0\}$.

**Definition 2.2** (H-polytope).
An *H-polytope* $P \subset \mathbb{R}^d$ is the intersection of finitely
many rational half-spaces:
$$
P = \bigcap_{i=1}^{m} H_i^+
= \bigl\{ x \in \mathbb{R}^d : A x + b \ge 0 \bigr\}
$$
where $A \in \mathbb{Q}^{m \times d}$, $b \in \mathbb{Q}^m$, and the
inequality is interpreted componentwise.  We call the list of row vectors
$(b_i, A_{i,1}, \ldots, A_{i,d})$ the *H-representation* of $P$.

In EXPDB, H-polytopes are the fundamental geometric primitive.  The class
`Polytope` stores the H-representation as a `cdd.Matrix` with
`rep_type = INEQUALITY`.  Rows belonging to the matrix's `lin_set` are
interpreted as *equalities* rather than inequalities, enabling the
representation of affine subspaces.

**Definition 2.3** (V-polytope).
A *V-polytope* is the convex hull of a finite set of rational points
$v_1, \ldots, v_n \in \mathbb{Q}^d$:
$$
P = \mathrm{conv}(v_1, \ldots, v_n)
= \Bigl\{ \sum_{i=1}^{n} \lambda_i v_i :
\lambda_i \ge 0,\; \sum_{i=1}^{n} \lambda_i = 1 \Bigr\}.
$$
The *vertices* of $P$ are the extreme points of this representation.

The double description method [MRTT53, F] converts between H- and
V-representations.  EXPDB uses `pycddlib` for this conversion; the
V-representation is computed lazily (method `compute_V_rep`) and cached.

**Definition 2.4** (Bounding box).
A *$d$-dimensional box* (or *hyperrectangle*) is a polytope of the form
$$
B = [l_1, u_1] \times [l_2, u_2] \times \cdots \times [l_d, u_d]
$$
with $l_i, u_i \in \mathbb{Q}$.  Its H-representation consists of $2d$
half-spaces.  In EXPDB, boxes are constructed by `Polytope.rect`.

**Convention.** Throughout this paper, all polytopes are bounded (i.e., they
are genuine polytopes rather than unbounded polyhedra).  This is guaranteed
in EXPDB by the bounding box $B$ imposed by the truncation constants in
`Constants` (specifically, `TAU_UPPER_LIMIT` and `LV_DEFAULT_UPPER_BOUND`).


### 2.2 Operations on Polytopes

We record the polytope operations used in EXPDB, together with their
algebraic and order-theoretic properties.

**Intersection.**
Given polytopes $P_1, \ldots, P_k \subset \mathbb{R}^d$, their intersection
is
$$
P_1 \cap \cdots \cap P_k
= \bigl\{ x \in \mathbb{R}^d : x \in P_i \text{ for all } i \bigr\}.
$$
In H-representation this is trivial: concatenate the constraint rows of all
$P_i$.  Intersection is the *meet* in the inclusion lattice of convex bodies:
$P_1 \cap P_2 \subseteq P_i$ for each $i$.  It is associative, commutative,
idempotent, and monotone: if $P_1 \subseteq P_1'$, then
$P_1 \cap P_2 \subseteq P_1' \cap P_2$.

In EXPDB: `Polytope.intersection(polys)` concatenates H-representations and
optionally canonicalizes.

**Set difference.**
Given polytopes $P, Q \subset \mathbb{R}^d$, the set difference
$P \setminus Q$ is generally *not* convex.  EXPDB decomposes it into a
disjoint union of polytopes as follows.  Let $Q$ be defined by constraints
$c_1, \ldots, c_m \ge 0$.  Then
$$
P \setminus Q
= \bigcup_{j=1}^{m}\,
P \;\cap\; \bigl(\neg c_j\bigr)
\;\cap\; c_1 \;\cap\; \cdots \;\cap\; c_{j-1}
$$
where $\neg c_j$ denotes the complementary half-space $\{x : -c_j(x) \ge 0\}$.
The pieces are pairwise disjoint by construction.

In EXPDB: `Polytope.set_minus(other)`.

**Scaling.**
Given a polytope $P \subset \mathbb{R}^d$ and a vector of rational scale
factors $\lambda = (\lambda_1, \ldots, \lambda_d) \in \mathbb{Q}^d_{>0}$,
the *coordinatewise scaling* of $P$ is
$$
\Lambda(P) = \bigl\{(\lambda_1 x_1, \ldots, \lambda_d x_d) :
(x_1, \ldots, x_d) \in P\bigr\}.
$$
In H-representation, this is achieved by dividing the $i$-th column of $A$
by $\lambda_i$.  Scaling is a linear automorphism of $\mathbb{R}^d$ and
preserves convexity.

In EXPDB: `Polytope.scale_all(factors)`.

**Projection.**
Given a polytope $P \subset \mathbb{R}^d$ and a subset of coordinate
indices $S \subseteq \{1, \ldots, d\}$, the *projection* of $P$ onto $S$ is
$$
\pi_S(P) = \bigl\{ (x_i)_{i \in S} : x \in P \bigr\}
\;\subset\; \mathbb{R}^{|S|}.
$$
Projection is the image of $P$ under the coordinate-erasing linear map.  It
preserves convexity (the image of a convex set under a linear map is convex)
and is monotone in the inclusion order: $P \subseteq Q$ implies
$\pi_S(P) \subseteq \pi_S(Q)$.

EXPDB computes projections via the V-representation: enumerate the vertices
of $P$, drop the coordinates not in $S$, then reconstruct the H-representation
of the projected vertex set using `Polytope.from_V_rep`.  This requires $P$
to be bounded (guaranteed by the bounding box convention).

In EXPDB: `Polytope.project(dims)`.

**Lifting.**
Given a polytope $P \subset \mathbb{R}^d$, a target dimension $n > d$, and
a specification of how the existing $d$ coordinates embed into the $n$
coordinates (together with bounding intervals for the new coordinates), the
*lifting* of $P$ is the Cartesian product
$$
\mathrm{lift}(P) = P' \times [l_{d+1}, u_{d+1}] \times \cdots \times [l_n, u_n]
\;\subset\; \mathbb{R}^n
$$
where $P'$ is $P$ re-embedded into the appropriate coordinate subspace of
$\mathbb{R}^n$.  Lifting preserves convexity (a Cartesian product of convex
sets is convex).  It is the *right adjoint* of projection in the following
sense: for any $Q \subset \mathbb{R}^n$,
$$
\pi_S(Q) \subseteq P
\quad\Longleftrightarrow\quad
Q \subseteq \mathrm{lift}(P)
$$
when the new coordinates in $\mathrm{lift}(P)$ are unconstrained (i.e.,
$[l_i, u_i]$ is taken sufficiently large).

In EXPDB: `Polytope.lift(var)` and `Region.lift(var)`.

**Containment and emptiness.**
EXPDB tests whether a polytope is empty by solving a linear program (LP)
with an arbitrary objective function over the H-representation.  If the LP
is feasible, the polytope is non-empty.  To test emptiness *excluding the
boundary* (strict feasibility), it solves an augmented LP that maximizes a
slack variable $\varepsilon$ subject to all constraints being satisfied with
margin $\varepsilon$.

In EXPDB: `Polytope.is_empty(include_boundary)`.

Subset testing $P \subseteq Q$ is implemented by verifying, for each
constraint $c$ of $Q$, that the minimum of $c$ over $P$ (an LP) is
non-negative.

In EXPDB: `Polytope.is_subset_of(other)`.


### 2.3 Regions

A polytope is convex by definition.  Many feasible sets arising in EXPDB are
*not* convex — they are unions, intersections, or complements of polytopes.
The `Region` class provides a recursive data structure for representing
arbitrary boolean combinations of polytopes.

**Definition 2.5** (Region).
A *region* $R \subset \mathbb{R}^d$ is defined inductively:
- **Atom**: A polytope $P$ (type `POLYTOPE`).
- **Complement**: $\mathbb{R}^d \setminus R'$ for a region $R'$ (type
  `COMPLEMENT`).
- **Union**: $R_1 \cup \cdots \cup R_k$ for regions $R_1, \ldots, R_k$
  (type `UNION`).
- **Disjoint union**: $R_1 \sqcup \cdots \sqcup R_k$ where the $R_i$ have
  pairwise disjoint interiors (type `DISJOINT_UNION`).
- **Intersection**: $R_1 \cap \cdots \cap R_k$ (type `INTERSECT`).

The type `DISJOINT_UNION` is semantically identical to `UNION` but carries
the additional invariant that the pieces have disjoint interiors.  This
invariant is exploited algorithmically: the disjoint decomposition
(`as_disjoint_union`) enables vertex enumeration and projection on each
piece independently.

**Canonical form.**  Every region can be converted to a disjoint union of
polytopes via the method `as_disjoint_union`, which recursively distributes
intersections over unions using the identity
$$
A \cap (B_1 \cup \cdots \cup B_n)
= (A \cap B_1) \cup \cdots \cup (A \cap B_n)
$$
and discards empty pieces.  The resulting disjoint union is not unique (it
depends on the order of processing), but it represents the same subset of
$\mathbb{R}^d$.  A subsequent simplification pass (`simplify`) attempts to
merge adjacent polytopes using `Polytope.try_union`, which tests whether the
union of two polytopes is itself convex [BCBM01].

All region operations — `contains`, `is_subset_of`, `substitute`,
`scale_all`, `project`, `lift` — are defined recursively, distributing over
the tree structure and delegating to `Polytope` methods at the leaves.


### 2.4 Affine and Piecewise-Affine Functions

**Definition 2.6** (Affine function on an interval).
A *1D affine function* is a triple $(m, c, I)$ representing
$f(x) = mx + c$ on the interval $I = [a, b] \subset \mathbb{R}$, with
$m, c \in \mathbb{Q}$ and $a, b \in \mathbb{Q}$.

In EXPDB: the class `Affine(m, c, domain)`.

**Definition 2.7** (Multidimensional affine function on a polytope).
A *$d$-dimensional affine function* is a pair $(a, P)$ where
$a = (a_0, a_1, \ldots, a_d) \in \mathbb{Q}^{d+1}$ and $P$ is a polytope
in $\mathbb{R}^d$, representing $f(x) = a_0 + a_1 x_1 + \cdots + a_d x_d$
for $x \in P$.

In EXPDB: the class `Affine2(a, domain)`.

**Definition 2.8** (Piecewise-affine function).
A *piecewise-affine function* is a finite collection
$\{(a^{(j)}, P_j)\}_{j=1}^{k}$ of affine functions on polytope domains,
where the polytopes $P_j$ have pairwise disjoint interiors and their union
covers the domain of definition.  The function is
$$
f(x) = a^{(j)}_0 + \sum_{i=1}^{d} a^{(j)}_i x_i
\qquad\text{for } x \in P_j.
$$

In EXPDB: the class `Piecewise(pieces)`, where each piece is an `Affine2`.

**Lower envelope.**  Given a collection $\{f_j\}$ of affine functions on a
common 1D domain, their *lower envelope* is $f^*(x) = \min_j f_j(x)$.  The
lower envelope of $n$ affine functions on $\mathbb{R}$ is a concave
piecewise-affine function with at most $n - 1$ breakpoints.  Breakpoints
occur at the intersection points of consecutive pairs of affine functions in
the envelope.

In EXPDB, the lower envelope is computed by `Affine.min_with`, which:
(i) collects all pairwise intersection points of the affine pieces,
(ii) sorts them to obtain a partition of the domain into subintervals,
(iii) on each subinterval, selects the piece with the smallest value at the
midpoint.

**Upper envelope.**  The *upper envelope* $f^*(x) = \max_j f_j(x)$ is
defined analogously and is a convex piecewise-affine function.

In EXPDB: `Affine.max_with`.

**Minimum of multidimensional affine functions.**
The class `Affine2` supports a `min_with` operation: given two affine
functions $f, g$ on polytope domains $P_f, P_g \subset \mathbb{R}^d$, compute
$\min(f, g)$ on $P_f \cap P_g$.  This is a piecewise-affine function on at
most two polytope pieces, obtained by splitting $P_f \cap P_g$ along the
hyperplane $\{f = g\}$.  The operation is the polytope-domain analogue of the
1D envelope computation.


### 2.5 Rational Functions and Their Envelopes

**Definition 2.9** (Univariate rational function).
A *rational function* over $\mathbb{Q}$ is a quotient $r(x) = p(x)/q(x)$
of two polynomials $p, q \in \mathbb{Q}[x]$, $q \not\equiv 0$.

In EXPDB: the class `RationalFunction`, which stores the numerator and
denominator as `sympy` symbolic expressions and supports exact arithmetic
(addition, multiplication, division, root-finding, and critical-point
computation).

**Definition 2.10** (Piecewise-rational function).
A *piecewise-rational function* on an interval $I \subset \mathbb{R}$ is a
finite collection $\{(r_j, I_j)\}_{j=1}^{k}$ where each $r_j$ is a
rational function and the intervals $I_j$ partition $I$.

**Lower envelope of rational functions.**
Given a family $\{(r_j, I_j)\}$ of rational functions on (possibly
overlapping) intervals, the *lower envelope* is the piecewise-rational
function
$$
r^*(x) = \min\bigl\{ r_j(x) : x \in I_j \bigr\}.
$$
The breakpoints of $r^*$ occur at the real roots of the polynomials
$p_i(x) q_j(x) - p_j(x) q_i(x)$, which are algebraic numbers computable by
`sympy.solve`.  Between consecutive breakpoints, the dominant function is
determined by evaluation at a single rational test point.

In EXPDB: `RationalFunction.min` (and `RationalFunction.max` for the upper
envelope).  The implementation proceeds iteratively: starting from a trivial
bound, each new rational curve is merged into the current envelope by
computing algebraic intersection points, partitioning into subintervals, and
selecting the dominant function on each.

**Remark 2.11** (Origin of rational functions in the pipeline).
Rational functions arise in EXPDB from the *supremum of a ratio* operation
(Section 2.6).  All input constraints are affine (half-spaces with rational
coefficients), so no rational functions appear at the polytope level.  The
transition from affine to rational occurs precisely when one computes
$\sup_\tau\{\rho/\tau\}$ along polytope edges: if $\rho(\sigma)$ and
$\tau(\sigma)$ are both affine in $\sigma$ along an edge, their ratio is a
degree-$(1,1)$ rational function.


### 2.6 The Rational Supremum Operator

The key non-trivial operation that connects the polyhedral stages of EXPDB
(dimensions 3 and 5) to the function-theoretic stages (dimension 1) is the
*rational supremum*.  We define it abstractly here; its role in the pipeline
is detailed in Section 5.

**Definition 2.12** (Rational supremum).
Let $R \subset \mathbb{R}^3$ be a bounded region with coordinates
$(\sigma, \tau, \rho)$, represented as a finite disjoint union of polytopes
$R = \bigsqcup_{j} P_j$.  The *rational supremum of $\rho/\tau$ over $R$*
is the function
$$
\Phi(\sigma)
= \sup\bigl\{ \rho / \tau : (\sigma, \tau, \rho) \in R,\; \tau > 0 \bigr\}
$$
defined for $\sigma$ in the projection $\pi_\sigma(R)$.

**Proposition 2.13.**
$\Phi(\sigma)$ is a piecewise-rational function of $\sigma$ with rational
breakpoints.

*Proof sketch.*
The supremum of $\rho/\tau$ over a convex polytope $P_j$ is attained at a
vertex or along an edge of $P_j$ (as a linear-fractional function over a
polytope, by the generalization of the simplex-vertex optimality theorem to
linear-fractional programs).  Along each edge of $P_j$, the coordinates
$\tau$ and $\rho$ are affine functions of $\sigma$:
$$
\tau(\sigma) = a\sigma + b, \qquad \rho(\sigma) = c\sigma + d,
$$
so $\rho/\tau = (c\sigma + d)/(a\sigma + b)$ is a rational function of
degree at most $(1, 1)$.  The supremum over finitely many such functions is
piecewise-rational, with breakpoints at the (algebraic, hence rational over
$\mathbb{Q}$ since the coefficients are rational and the intersection of two
degree-$(1,1)$ rational functions reduces to a linear equation) intersection
points.
$\square$

**Algorithm** (as implemented in `compute_sup_rho_on_tau`).
1. For each polytope $P_j$ in the disjoint decomposition, enumerate all edges
   via the vertex adjacency structure of the V-representation.
2. For each edge with vertices $v_1 = (\sigma_1, \tau_1, \rho_1)$ and
   $v_2 = (\sigma_2, \tau_2, \rho_2)$ with $\sigma_1 \ne \sigma_2$:
   - Parameterize $\tau(\sigma)$ and $\rho(\sigma)$ as affine functions
     interpolating the two vertices.
   - Compute $r(\sigma) = \rho(\sigma)/\tau(\sigma)$ as a `RationalFunction`.
   - Record $(r, [\min(\sigma_1, \sigma_2),\, \max(\sigma_1, \sigma_2)])$.
3. Compute the upper envelope of all recorded rational functions via
   `RationalFunction.max`.

The output is a piecewise-rational function $\Phi(\sigma)$ on a partition
of the $\sigma$ domain.


### 2.7 Convex Hulls

**Definition 2.14** (Convex hull of a point set).
Given a finite set $S = \{p_1, \ldots, p_n\} \subset \mathbb{Q}^d$, the
*convex hull* $\mathrm{conv}(S)$ is the smallest convex set containing $S$.
The *vertices* of $\mathrm{conv}(S)$ are the points $p_i$ that are extreme
(not expressible as convex combinations of other points in $S$).

For $d = 2$, EXPDB computes convex hulls using `scipy.spatial.ConvexHull`
(which implements the Quickhull algorithm [BDH96]).  This returns the vertices
in counterclockwise order, enabling efficient edge enumeration and tangent-line
extraction.  For $d \ge 3$, vertex enumeration via `pycddlib` is used instead.

**Remark 2.15** (Duality for 2D hulls).
In two dimensions, the convex hull of a point set is dual to the lower
envelope of a family of lines.  Specifically, given points
$(k_i, l_i) \in \mathbb{R}^2$, define the family of lines
$\beta_i(\alpha) = (l_i - k_i)\alpha + k_i$.  The lower envelope
$\beta^*(\alpha) = \min_i \beta_i(\alpha)$ is a concave piecewise-affine
function whose breakpoints correspond to edges of $\mathrm{conv}(S)$, and
whose affine pieces correspond to vertices of $\mathrm{conv}(S)$.  This is
a special case of Legendre--Fenchel duality restricted to finite point
sets and affine functions.  The duality is exact and information-preserving:
the hull can be recovered from the envelope and vice versa.

This duality is the geometric basis of the EP $\leftrightarrow$ Beta
correspondence in EXPDB (Section 5).


### 2.8 Order-Theoretic Framework

We conclude the preliminaries by setting up the lattice-theoretic language
used to state the convergence results in Section 6.

**Definition 2.16** (Inclusion lattice of regions).
Let $\mathcal{R}^d$ denote the set of all bounded regions in $\mathbb{R}^d$
(finite boolean combinations of rational polytopes), ordered by reverse
inclusion: $R_1 \preceq R_2$ iff $R_1 \subseteq R_2$.  Under this ordering,
$\preceq$ means "tighter" (a smaller feasible region is a stronger
constraint).  The meet is intersection: $R_1 \wedge R_2 = R_1 \cap R_2$.

**Definition 2.17** (Pointwise lattice of functions).
Let $\mathcal{F}(I)$ denote the set of piecewise-rational functions on an
interval $I$, ordered pointwise: $f \preceq g$ iff $f(\sigma) \le g(\sigma)$
for all $\sigma \in I$.  Under this ordering, $\preceq$ means "tighter" (a
smaller function value is a stronger bound).  The meet is the pointwise
minimum: $(f \wedge g)(\sigma) = \min(f(\sigma), g(\sigma))$.

**Definition 2.18** (Product lattice).
The *EXPDB state lattice* is the product
$$
\mathcal{L}
= \mathcal{H}^2 \times \mathcal{F}^{\downarrow} \times \mathcal{H}^2
\times \mathcal{R}^3 \times \mathcal{R}^3 \times \mathcal{R}^5
\times \mathcal{F}^{\downarrow} \times \mathcal{F}^{\downarrow}
\times \mathbb{R}^{\downarrow}
$$
where $\mathcal{H}^2$ denotes the lattice of 2D convex hulls ordered by
hull containment (larger hull = more information = tighter, so the order is
$H_1 \preceq H_2$ iff $H_1 \supseteq H_2$), $\mathcal{F}^{\downarrow}$
denotes piecewise functions ordered by $\le$ (smaller = tighter),
$\mathcal{R}^d$ denotes $d$-dimensional regions ordered by $\subseteq$
(smaller = tighter), and $\mathbb{R}^{\downarrow}$ denotes the reals with
the standard order (smaller = tighter).  The components correspond,
respectively, to: EP hull, Beta envelope, Mu hull, LV region, ZLV region,
LVER, ZD estimate, ZDE estimate, and the prime gap bound $\theta$.

The product order is componentwise: a state $\Omega_1 \preceq \Omega_2$
iff every component of $\Omega_1$ is at least as tight as the corresponding
component of $\Omega_2$.

**Definition 2.19** (Monotone operator).
A map $\Phi: \mathcal{L} \to \mathcal{L}$ is *monotone* if
$\Omega_1 \preceq \Omega_2$ implies $\Phi(\Omega_1) \preceq \Phi(\Omega_2)$.
It is a *contraction* (or *refinement*) if $\Phi(\Omega) \preceq \Omega$ for
all reachable states $\Omega$.

A monotone contraction on a lattice with descending chain condition
converges: the sequence $\Omega, \Phi(\Omega), \Phi^2(\Omega), \ldots$ is
(componentwise) non-increasing and must stabilize in finitely many steps.
This is the abstract basis for the convergence of the EXPDB pipeline
(Section 6).

## 3. The EXPDB Pipeline

This section describes the computational architecture of EXPDB in
structural terms: the type system, the transformation catalog, the data
representations, and the orchestration layer.  The goal is to make the
pipeline legible as a sequence of geometric operations, preparing the ground
for the identification of the master polytope in Section 4.  All code
references point to files under `blueprint/src/python/` in the EXPDB
repository.


### 3.1 The Hypothesis Object

The atomic unit of the pipeline is the *Hypothesis* — a Python object
(`hypotheses.py`, class `Hypothesis`) representing a single mathematical
assertion together with its provenance.  A Hypothesis carries five primary
attributes:

| Attribute | Type | Role |
|-----------|------|------|
| `name` | string | Short identifier, e.g. "Ingham (1940) zero density estimate" |
| `hypothesis_type` | string | One of ten type tags (see below) |
| `data` | domain-specific object | The geometric payload (point, function, region, etc.) |
| `proof` | string | Human-readable proof or literature citation |
| `reference` | `Reference` | Bibliographic source with author, year, and title |

In addition, each Hypothesis carries a mutable `dependencies` attribute — a
set of other Hypothesis objects from which it was derived.  A literature
result has $\mathsf{dependencies} = \emptyset$; a derived result records the
hypotheses it was produced from.  The transitive closure of the dependency
relation forms a directed acyclic graph (DAG) rooted at the derived
hypothesis, with literature results as leaves.  This DAG constitutes a
machine-readable proof.

Three metrics are defined on the proof DAG:

- `proof_complexity()`: the total number of nodes (Hypothesis objects) in the
  dependency tree, counting multiplicities.
- `proof_depth()`: the height of the dependency tree.
- `proof_date()`: the maximum publication year among all leaf dependencies.

These metrics enable proof selection: when multiple derivations of the same
result exist, the system can choose the proof that minimizes complexity,
depth, or recency.  This selection is controlled by the
`Proof_Optimization_Method` enum in `constants.py`.


### 3.2 The Type System

Each Hypothesis carries a `hypothesis_type` string drawn from a fixed
vocabulary of ten types.  These types partition the space of mathematical
assertions by the *geometric character* of their data payload.  We list them
here together with the payload class, the ambient space, and the shape of
the data:

| Type tag | Payload class | Ambient space | Shape |
|----------|--------------|---------------|-------|
| `"Upper bound on beta"` | `Bound_beta` | $\mathbb{R}^1$ (function on $\alpha$) | Affine segment: $\beta(\alpha) \le m\alpha + c$ on an interval |
| `"Exponent pair"` | `Exp_pair` | $\mathbb{R}^2$ | Point $(k, l)$ |
| `"Exponent pair transform"` | `Transform` | — | Map $\mathsf{EP} \to \mathsf{EP}$ |
| `"Exponent pair to beta bound transform"` | `Transform` | — | Map $\mathsf{EP} \to \mathsf{list[Beta]}$ |
| `"Upper bound on mu"` | `Bound_mu` | $\mathbb{R}^2$ | Point $(\sigma, \mu)$ |
| `"Large value estimate"` | `Large\_Value\_Estimate$ | $\mathbb{R}^3$ | Region in $(\sigma, \tau, \rho)$ |
| `"Zeta large value estimate"` | `Large\_Value\_Estimate$ | $\mathbb{R}^3$ | Region in $(\sigma, \tau, \rho)$ with $\tau \ge 2$ |
| `"Large value energy region"` | `Large\_Value\_Energy\_Region$ | $\mathbb{R}^5$ | Region in $(\sigma, \tau, \rho, \rho^*, s)$ |
| `"Large value energy region transform"` | `Transform` | — | Map $\mathsf{LVER} \to \mathsf{LVER}$ |
| `"Zero density estimate"` | `Zero\_Density\_Estimate$ | $\mathbb{R}^1$ (function on $\sigma$) | Rational function on interval: $A(\sigma) \le r(\sigma)$ |
| `"Zero density energy estimate"` | `Zero\_Density\_Energy\_Estimate$ | $\mathbb{R}^1$ (function on $\sigma$) | Rational function on interval: $A^*(\sigma) \le r(\sigma)$ |

The transform types are *higher-order*: their payload is a callable that
maps one Hypothesis to another (or to a list of others).  They are stored as
Hypothesis objects in the same `Hypothesis_Set`, enabling the system to
reason about which transforms are available and to record their use in the
dependency DAG.


### 3.3 The Hypothesis Set

A `Hypothesis_Set` (`hypotheses.py`, class `Hypothesis_Set`) is a mutable
collection of Hypothesis objects, serving as the pipeline's working memory.
Its interface provides:

- **Insertion**: `add_hypothesis(h)` and `add_hypotheses(hs)`, which add
  individual or batch hypotheses and invalidate cached derived data.
- **Filtering**: `list_hypotheses(hypothesis_type, year)`, which returns all
  hypotheses matching a type and optionally a publication-year cutoff.
- **Search**: `find_hypothesis(hypothesis_type, data, name, keywords, year)`,
  which returns the first hypothesis matching all specified criteria.
- **Caching**: A `data` dictionary and `data_valid` flag, used to store
  expensive derived quantities (e.g., convex hulls) that can be reused across
  multiple queries.  Insertion of a new hypothesis sets `data_valid = False`,
  forcing recomputation on the next access.

The set semantics (Python `set` of Hypothesis objects) ensure that identical
hypotheses are not duplicated.  However, hypotheses are compared by object
identity, not by data equality, so distinct Hypothesis objects with
identical data payloads may coexist.


### 3.4 The Axiom Layer: `literature.py`

The module `literature.py` (1,439 lines) defines the *axiom set* — the
collection of hypotheses drawn directly from the published literature.  It
executes at import time, populating a module-level `Hypothesis_Set` called
`literature`.

The structure of the module is sequential.  It proceeds through the
hypothesis types in the following order:

1. **Beta bounds** (§§ lines 33–360): Approximately 20 results, from
   Watt (1989) through Trudgian–Yang (2024).  Each is an affine bound
   $\beta(\alpha) \le m\alpha + c$ on a subinterval of $[0, 1/2]$,
   constructed as a `Bound_beta(Affine(...))` and inserted via
   `bbeta.add_beta_bound(literature, bounds, ref)`.

2. **Exponent pairs** (§§ lines 361–506): Literature exponent pairs
   (individual points $(k, l)$), inserted via
   `ep.literature_exp_pair(k, l, ref)`.

3. **Exponent pair transforms** (§§ lines 507–598): The four classical
   transforms — van der Corput A and B, Sargos C, and Sargos D — each
   defined as a `Transform` object wrapping a Python function, inserted as
   hypotheses of type `"Exponent pair transform"` or
   `"Exponent pair to beta bound transform"`.

4. **Mu bounds** (§§ lines 601–743): Literature bounds on $\mu(\sigma)$,
   each a point $(\sigma, \mu)$, inserted via
   `literature_bound_mu(sigma, mu, ref)`.

5. **Large value estimates** (§§ lines 744–902): Each is a list of affine
   upper bounds on $\rho$ as a function of $(\sigma, \tau)$, converted to a
   `Region` in $\mathbb{R}^3$ by `lv.convert_bounds`.

6. **Large value energy regions** (§§ lines 903–1147): Direct constraints on
   $(\sigma, \tau, \rho, \rho^*, s) \in \mathbb{R}^5$, constructed as
   `Region` objects and wrapped in `Large_Value_Energy_Region`.

7. **Zero density estimates** (§§ lines 1148–1416): Each is a rational
   function $A(\sigma) \le r(\sigma)$ on an interval, inserted via
   `zd.add_zero_density(literature, expr, interval, ref)`.

8. **Zero density energy estimates** (§§ lines 1416–end): Each is
   $A^*(\sigma) \le r(\sigma)$ on an interval.

After all insertions, the `literature` object contains the complete axiom
set.  Because the module executes at import time, any module that imports
from `literature.py` receives the fully populated set as a side effect.


### 3.5 The Transformation Catalog

The pipeline derives new hypotheses from existing ones via transformations.
Each transformation has a well-defined geometric character.  We catalog them
here by input and output type, grouping by the stage of the pipeline in
which they appear.  The geometric details of each transformation were
analyzed in our prior work; here we record only the signature, location, and
a one-line geometric description.

**Within the EP stage** (exponent pairs $\to$ exponent pairs):

| Name | Function | Geometric action |
|------|----------|-----------------|
| A-process | `literature.py:A_transform_function` | Rational contraction $(k,l) \mapsto (k/(2k+2),\, 1/2 + l/(2k+2))$ |
| B-process | `literature.py:B_transform_function` | Affine involution $(k,l) \mapsto (l - 1/2,\, k + 1/2)$ |
| C-process | `literature.py:C_transform_function` | Rational contraction toward $(0, 11/12)$ |
| Iterative expansion | `exponent_pair.py:compute_exp_pairs` | Repeated application of A, B, C with convex hull pruning |

**Cross-type: EP $\to$ Beta**:

| Name | Function | Geometric action |
|------|----------|-----------------|
| EP to beta | `bound_beta.py:exponent_pairs_to_beta_bounds` | Each point $(k,l) \mapsto$ affine function $(l{-}k)\alpha + k$ (tangent line) |
| D-process | `literature.py:D_transform_function` | EP $\to$ piecewise-affine beta bound (Sargos) |

**Within the Beta stage** (beta bounds $\to$ beta bounds):

| Name | Function | Geometric action |
|------|----------|-----------------|
| VdC-$\beta$ iteration | `bound_beta.py:apply_van_der_corput_process_for_beta` | Self-improvement via symmetric extension and recombination |
| Best beta | `bound_beta.py:compute_best_beta_bounds` | Lower envelope via iterated `Affine.min_with` |

**Cross-type: Beta $\to$ EP** (the return direction of the feedback loop):

| Name | Function | Geometric action |
|------|----------|-----------------|
| Beta to EP | `exponent_pair.py:beta_bounds_to_exponent_pairs` | Convex hull of epigraph; each edge $\to$ tangent-line EP |

**Cross-type: EP $\to$ Mu, Beta $\to$ Mu**:

| Name | Function | Geometric action |
|------|----------|-----------------|
| EP to mu | `bound_mu.py:exponent_pair_to_mu_bound` | Linear map $(k,l) \mapsto (l{-}k, k)$ |
| Functional equation | `bound_mu.py:apply_functional_equation` | Involution $(\sigma, \mu) \mapsto (1{-}\sigma,\, \mu{+}\sigma{-}1/2)$ |
| Mu convexity | `bound_mu.py:apply_mu_convexity` | Convex combination of two mu points |
| Beta to mu | `bound_mu.py:beta_bounds_to_mu_bounds` | Piecewise-affine evaluation of dual bound |

**Into the 3D stage** (various $\to$ LV / ZLV):

| Name | Function | Geometric action |
|------|----------|-----------------|
| LV combine | `large_values.py:combine_large_value_estimates` | Intersection of $\mathbb{R}^3$ regions |
| LV raise-to-power | `large_values.py:raise_to_power_hypothesis` | Diagonal scaling $(\sigma,\tau,\rho) \mapsto (\sigma, k\tau, k\rho)$ |
| Bourgain optimization | `large_values.py:optimize_bourgain_large_value_estimate` | LP-based parameter optimization over constraint triples |
| LV $\to$ ZLV | `zeta_large_values.py:lv_to_zlv` | Restriction to $\tau \ge 2$ |
| Beta $\to$ ZLV | `zeta_large_values.py:beta_to_zlv` | Each affine bound $\to$ zero-set halfspace in $\mathbb{R}^3$ |
| Mu $\to$ ZLV | `zeta_large_values.py:mu_to_zlv` | Each point $\to$ zero-set halfspace in $\mathbb{R}^3$ |

**Into the 5D stage** (various $\to$ LVER):

| Name | Function | Geometric action |
|------|----------|-----------------|
| EP $\to$ LVER | `additive_energy.py:ep_to_lver` | Each EP generates 9 halfspace constraints in $\mathbb{R}^5$ |
| LV $\to$ LVER | `additive_energy.py:lv_to_lver` | Cartesian product lift $\mathbb{R}^3 \to \mathbb{R}^5$ |
| LVER raise-to-power | `additive_energy.py:get_raise_to_power_hypothesis` | Diagonal scaling by $(1, k, k, k, k)$ |
| LVER intersection | `additive_energy.py:compute_best_lver` | Meet in the $\mathbb{R}^5$ region lattice |

**Descending: 5D $\to$ 3D $\to$ 1D $\to$ 0D**:

| Name | Function | Geometric action |
|------|----------|-----------------|
| LVER $\to$ LV | `additive_energy.py:lver_to_lv` | Projection $\pi_{\sigma,\tau,\rho}$ |
| LVER $\to$ energy | `additive_energy.py:lver_to_energy` | Projection $\pi_{\sigma,\tau,\rho^*}$ |
| LV/ZLV $\to$ ZD | `zero_density_estimate.py:lv_zlv_to_zd` | Rational supremum $\sup_\tau(\rho/\tau)$ + lower envelope |
| LVER $\to$ ZD | `zero_density_estimate.py:lver_to_zd` | Projection then rational supremum |
| LVER $\to$ ZDE | `zero_density_energy_estimate.py:lver_to_energy_bound` | Projection onto $(\sigma,\tau,\rho^*)$, then $\sup(\rho^*/\tau)/(1{-}\sigma)$ |
| Best ZD | `zero_density_estimate.py:best_zero_density_estimate` | Lower envelope via `RationalFunction.min` |
| Best ZDE | `zero_density_energy_estimate.py:compute_best_energy_bound` | Lower envelope via `RationalFunction.min` |
| ZD + ZDE $\to$ $\theta$ | `prime_gap.py:compute_gap2` | $\sup_\sigma \max(\alpha(\sigma), \beta(\sigma))$ |


### 3.6 Data Representations

Every hypothesis type has a specific geometric representation.  We list the
mapping from type to representation, emphasizing the data structures from
Section 2 that each type instantiates.

| Hypothesis type | Representation | Implements |
|----------------|----------------|-----------|
| Exponent pair | `Exp_pair(k, l)` | Point in $\mathbb{Q}^2$ (Def. 2.14) |
| Upper bound on beta | `Bound_beta(Affine(m, c, I))` | Affine function on interval (Def. 2.6) |
| Upper bound on mu | `Bound_mu(sigma, mu)` | Point in $\mathbb{Q}^2$ (Def. 2.14) |
| Large value estimate | `Large_Value_Estimate(Region)` | Region in $\mathbb{Q}^3$ (Def. 2.5) |
| Zeta large value estimate | `Large_Value_Estimate(Region)` | Region in $\mathbb{Q}^3$ with $\tau \ge 2$ (Def. 2.5) |
| Large value energy region | `Large_Value_Energy_Region(Region)` | Region in $\mathbb{Q}^5$ (Def. 2.5) |
| Additive energy estimate | `Additive_Energy_Estimate(Region)` | Region in $\mathbb{Q}^3$ (projected from $\mathbb{R}^5$) |
| Zero density estimate | `Zero_Density_Estimate(expr, I)` | Rational function on interval (Def. 2.9–2.10) |
| Zero density energy est. | `Zero_Density_Energy_Estimate(expr, I)` | Rational function on interval (Def. 2.9–2.10) |
| Transform types | `Transform(name, func)` | Higher-order: callable $\mathsf{Hyp} \to \mathsf{Hyp}$ |

The Zero Density and Zero Density Energy classes use *lazy evaluation*: the
string expression `expr` is stored at construction time; parsing into a
`RationalFunction` object (via `sympy`) is deferred until the first
evaluation call.  This avoids unnecessary symbolic computation for hypotheses
that are superseded before they are ever evaluated.


### 3.7 The Orchestration Layer

The derivation pipeline is driven by two modules: `derived.py` (1,384 lines)
and `examples.py` (620 lines).  The former contains all derivation routines
used to establish new results; the latter provides demonstration scripts.

The top-level entry point is `derived.py:prove_all()`, whose call graph
(with most routines commented out in the current codebase) activates the
pipeline stages in order:

```
prove_all()
├── prove_exponent_pairs()           # EP stage
├── prove_all_large_value_estimates() # LV stage  [commented out]
├── prove_all_zero_density_estimates() # ZD stage  [commented out]
├── prove_all_zero_density_energy_estimates() # ZDE stage  [commented out]
└── prove_prime_gap2()               # θ stage   [commented out]
```

Each `prove_*` routine follows a common pattern:

1. **Select axioms**: construct a fresh `Hypothesis_Set`, populate it with
   relevant literature hypotheses by calling
   `literature.list_hypotheses(hypothesis_type=...)` or
   `literature.find_hypothesis(keywords=...)`.
2. **Expand**: apply transforms to generate derived hypotheses, inserting
   them into the set.  This may involve iterative loops (e.g.,
   `compute_exp_pairs` with a `search_depth` parameter).
3. **Optimize**: call a `best_*` or `compute_best_*` function to extract the
   tightest bound from the accumulated hypotheses.
4. **Report**: print the result and optionally display the proof tree via
   `recursively_list_proofs()`.

The most complex orchestration occurs in the ZD and ZDE stages, where the
`prove_zero_density` function (called with varying hypothesis sets and
$\tau_0$ parameters) constructs local `Hypothesis_Set` objects, computes
large value regions over specified $(\sigma, \tau)$ domains, and extracts
zero density estimates via the rational supremum operator.  Each such call
is self-contained: it builds its own polytope, projects it, and extracts the
envelope.


### 3.8 Truncation and Boundedness

The pipeline uses six constants (defined in `constants.py`) that serve as
global termination guarantees and geometric bounding parameters:

| Constant | Value | Role |
|----------|-------|------|
| `BETA_TRUNCATION` | 20 | Maximum iterations for beta bound derivation |
| `EXP_PAIR_TRUNCATION` | 20 | Maximum iterations for exponent pair expansion |
| `LARGE_VALUES_TRUNCATION` | 20 | Maximum number of large value terms in a series |
| `ALPHA_UPPER_LIMIT` | 100 | Upper bound on the $\alpha$ parameter |
| `TAU_UPPER_LIMIT` | $10^6$ | Upper bound on $\tau$ (ensures polytopes are bounded) |
| `LV_DEFAULT_UPPER_BOUND` | $10^6$ | Upper bound on $\rho$, $\rho^*$, $s$ (ensures polytopes are bounded) |

The first three constants control iteration depth and guarantee termination
of the feedback loops.  The last three define the bounding box
$$
B = [{\tfrac{1}{2}}, 1] \times [0, 10^6] \times [0, 10^6]^3
\;\subset\; \mathbb{R}^5
$$
within which the master polytope $\mathcal{P}$ (Section 4) is constructed.
The bounding box ensures that all polytopes are bounded, enabling
V-representation computation and projection via vertex enumeration.


### 3.9 Summary: The Pipeline as Geometry

We can now restate the EXPDB pipeline in purely geometric terms.

The axiom layer (`literature.py`) populates the pipeline with an initial
collection of geometric objects: points in $\mathbb{R}^2$ (exponent pairs,
mu bounds), affine segments on intervals (beta bounds), polyhedral regions
in $\mathbb{R}^3$ (large value estimates, zeta large value estimates),
polyhedral regions in $\mathbb{R}^5$ (large value energy regions), and
rational functions on intervals (zero density estimates, zero density energy
estimates).

The transformation layer applies three families of operations:
- **Hull and envelope** (convex hull of points, lower envelope of affine or
  rational functions) — selecting the tightest bound from a collection.
- **Intersection** (meet in the region lattice) — combining constraints.
- **Projection and lifting** (coordinate erasure and Cartesian product) —
  moving between ambient spaces of different dimensions.

The orchestration layer sequences these operations in a particular order,
threading the results through the type system.  The claim of Section 4 is
that this entire sequence can be understood as the progressive construction
and then progressive dissection of a single polytope
$\mathcal{P} \subset \mathbb{R}^5$.

## 4. The Master Polyhedral Region $\mathcal{P} \subset \mathbb{R}^5$

This section defines the central geometric object of the paper.  We show
that the EXPDB pipeline constructs a single bounded region
$\mathcal{P} \subset \mathbb{R}^5$ — the intersection of all available
constraints in the five-dimensional parameter space — and that every object
computed by the pipeline (Sections 5–6) is a derived quantity of
$\mathcal{P}$.


### 4.1 The Ambient Space

The five-dimensional ambient space $\mathbb{R}^5$ is coordinated by the
tuple $(\sigma, \tau, \rho, \rho^*, s)$.  We assign each coordinate an
abstract label and a role in the pipeline:

| Index | Symbol | Role in the pipeline |
|-------|--------|---------------------|
| 0 | $\sigma$ | Primary parameter; all 1D output functions are functions of $\sigma$ |
| 1 | $\tau$ | Scale parameter; the supremum operator integrates over $\tau$ |
| 2 | $\rho$ | Value exponent; projects to the LV region |
| 3 | $\rho^*$ | Energy exponent; projects to the energy/LV* region |
| 4 | $s$ | Auxiliary parameter; eliminated by projection in all output stages |

These labels are abstract geometric coordinates.  Their interpretation in
analytic number theory is irrelevant to the structural analysis; what matters
is which coordinates are preserved, projected, or ratioed at each stage of
the pipeline.


### 4.2 The Bounding Box

All polytopes in EXPDB are constructed within a bounding box that
ensures boundedness and finiteness of vertex sets.  The box is defined by
the default constraints in `Large_Value_Energy_Region.default_constraints()`
(`additive_energy.py`, lines 51–72) together with the constants in
`constants.py`:

$$
\mathcal{B} =
\bigl[\tfrac{1}{2},\, 1\bigr]
\times \bigl[0,\, T\bigr]
\times \bigl[0,\, M\bigr]
\times \bigl[0,\, M\bigr]
\times \bigl[0,\, M\bigr]
\;\subset\; \mathbb{R}^5
$$

where $T = \mathtt{TAU\_UPPER\_LIMIT} = 10^6$ and
$M = \mathtt{LV\_DEFAULT\_UPPER\_BOUND} = 10^6$.

The box $\mathcal{B}$ is itself a polytope with $2 \times 5 = 10$
half-space constraints.  It serves as the initial feasible region: before
any literature hypotheses are applied, the set of admissible five-tuples is
exactly $\mathcal{B}$.


### 4.3 Sources of Constraints

The master region $\mathcal{P}$ is obtained by intersecting $\mathcal{B}$
with half-spaces derived from four sources.  Each source generates
constraints in $\mathbb{R}^5$ by one of three mechanisms: direct constraint,
lifting, or parametric construction.

#### 4.3.1 Direct LVER constraints (literature)

Several literature results directly constrain the five-tuple
$(\sigma, \tau, \rho, \rho^*, s)$.  These appear in `literature.py` as calls
to `add_lver_*` functions that construct `Region` objects in $\mathbb{R}^5$.

Each such result takes the form of a set of affine inequalities
$$
c_0 + c_1 \sigma + c_2 \tau + c_3 \rho + c_4 \rho^* + c_5 s \;\ge\; 0
$$
with $c_i \in \mathbb{Q}$.  These are packaged as the sub-level set of a
pointwise maximum of affine functions — that is, the set
$\{x : \max_j \ell_j(x) \le 0\}$ for affine functions $\ell_j$ — and
represented via `Region.from_union_of_halfplanes` as a disjoint union of
convex polytopes (see Section 2.3).

**Example.**  The Heath-Brown (1979) large value energy region imposes three
constraints of the form $s \le f_i(\rho, \tau)$ where each $f_i$ is affine.
The feasible set is
$$
\{(\sigma,\tau,\rho,\rho^*,s) \in \mathcal{B}
: s \le \min(2 + \rho,\; 1 + 2\rho,\; 1 + \tfrac{1}{2}\tau + \tfrac{5}{4}\rho)\}.
$$
The minimum of three affine functions is concave, so its sub-level set is
convex.  However, the `from_union_of_halfplanes` constructor represents the
*complement* of the super-level set of the *maximum* of the affine functions,
producing a disjoint union of (up to) three polytopes.

There are approximately 15–20 such direct LVER hypotheses in the current
literature set, arising from the work of Heath-Brown, Ivić, and
Guth–Maynard.  Each contributes between 3 and 9 half-space constraints to
$\mathcal{P}$.


#### 4.3.2 Lifted LV constraints

Each large value estimate in the literature constrains the triple
$(\sigma, \tau, \rho)$, defining a region
$R_{\mathrm{LV}} \subset \mathbb{R}^3$.  This is lifted to
$\mathbb{R}^5$ by the operation
$$
\mathrm{lift}(R_{\mathrm{LV}})
= R_{\mathrm{LV}} \times [0, M] \times [0, M]
\;\subset\; \mathbb{R}^5,
$$
which adds no constraints on $\rho^*$ or $s$ beyond the bounding box.
Formally, the lift maps each half-space $a_0 + a_1\sigma + a_2\tau +
a_3\rho \ge 0$ to the half-space
$a_0 + a_1\sigma + a_2\tau + a_3\rho + 0 \cdot \rho^* + 0 \cdot s \ge 0$
in $\mathbb{R}^5$.

In EXPDB: `lv_to_lver(hypotheses, zeta=False)` in `additive_energy.py`
(lines 243–296) applies `Region.lift([0, 1, 2, (0, M), (0, M)])` to each
LV region.

Similarly, each zeta large value estimate (with the additional constraint
$\tau \ge 2$) is lifted by `lv_to_lver(hypotheses, zeta=True)`.


#### 4.3.3 Lifted ZLV constraints from Beta and Mu

Beta bounds and mu bounds do not directly constrain the five-tuple.
Instead, they first generate constraints in the $(\sigma, \tau, \rho)$ space
(the ZLV region) via the constructions `beta_to_zlv` and `mu_to_zlv`
(Section 3.5), and these are then lifted to $\mathbb{R}^5$ by the same
mechanism as Section 4.3.2.

Each beta bound $\beta(\alpha) \le m\alpha + c$ on $[\alpha_0, \alpha_1]$
generates the half-space $\sigma - c\tau - m \ge 0$ in $\mathbb{R}^3$ (on
the subregion $\tau \in [1/\alpha_1, 1/\alpha_0]$), which forces $\rho = 0$
when the half-space is active.  This half-space lifts to
$\sigma - c\tau - m + 0 \cdot \rho + 0 \cdot \rho^* + 0 \cdot s \ge 0$
in $\mathbb{R}^5$.

Each mu bound $\mu(\sigma_0) \le \mu_0$ generates the half-space
$\sigma - \sigma_0 - \mu_0 \tau \ge 0$ in $\mathbb{R}^3$, with the same
lifting.


#### 4.3.4 EP-derived LVER constraints

Each exponent pair $(k, l)$ generates constraints in $\mathbb{R}^5$ via
`ep_to_lver` (`additive_energy.py`, lines 204–243).  The construction
proceeds as follows:

1. Define two families of affine forms on
   $(\sigma, \tau, \rho, \rho^*, s)$: a "first maximum" of 3 terms and a
   "second maximum" of 3 terms, whose coefficients are rational functions
   of $(k, l)$.

2. For each of the $3 \times 3 = 9$ pairs (one from each family), compute
   a combined affine constraint $c_0 + c_1\sigma + c_2\tau + c_3\rho +
   c_4\rho^* + c_5 s \ge 0$.

3. Package the 9 constraints as a `Region.from_union_of_halfplanes`
   object — a disjoint union of up to 9 polytopes in $\mathbb{R}^5$.

The coefficients of the constraints are rational in $(k, l)$ (specifically,
they involve the terms $(k + l)/(1 + 2k + 2l)$ and
$(2 + 3k + 4l)/(1 + 2k + 2l)$).  For each fixed EP, the constraint
coefficients are rational numbers.


#### 4.3.5 Raise-to-power constraints

The raise-to-power transform (`get_raise_to_power_hypothesis`,
`additive_energy.py`, lines 169–188) generates new LVER hypotheses by
scaling: given an existing LVER region $R$ and an integer $k \ge 2$, the
transform produces the region
$$
\Lambda_k(R) = \{(\sigma, k\tau, k\rho, k\rho^*, ks) :
(\sigma, \tau, \rho, \rho^*, s) \in R\}
$$
via `Region.scale_all([1, k, k, k, k])`.  In H-representation, this
divides columns 1–4 by $k$.  The result is a rescaled copy of $R$ that
covers a larger range of $\tau$ values.

In the current codebase, raise-to-power is applied for $k \in \{2, 3, 4\}$
(and occasionally up to $k = 5$).  Each application of the transform to each
existing LVER hypothesis produces one new LVER hypothesis.  These are
intersected together with all other LVER constraints in
`compute_best_lver`.


### 4.4 Construction of $\mathcal{P}$

**Definition 4.1** (Master region).
Let $\mathcal{H}$ be a hypothesis set containing hypotheses of types
"Large value energy region," "Large value energy region transform,"
"Large value estimate," "Zeta large value estimate," "Exponent pair,"
"Upper bound on beta," and "Upper bound on mu."  Let
$\mathcal{D} \subset \mathbb{R}^2$ be a region in $(\sigma, \tau)$-space
(the *domain of interest*).  The *master region*
$\mathcal{P} = \mathcal{P}(\mathcal{H}, \mathcal{D})$ is defined by the
following procedure:

**Step 1** (Collect LVER hypotheses).
Let $\mathcal{L}_0$ be the set of all hypotheses in $\mathcal{H}$ of type
"Large value energy region."

**Step 2** (Apply transforms).
Let $\mathcal{T}$ be the set of all hypotheses in $\mathcal{H}$ of type
"Large value energy region transform" (i.e., the raise-to-power
transforms for $k = 2, 3, \ldots$).  Expand:
$$
\mathcal{L}_1 = \mathcal{L}_0
\;\cup\; \bigl\{ T(R) : T \in \mathcal{T},\; R \in \mathcal{L}_0 \bigr\}.
$$

**Step 3** (Add lifted LV and ZLV constraints).
Lift all large value estimates to $\mathbb{R}^5$:
$$
\mathcal{L}_2 = \mathcal{L}_1
\;\cup\; \bigl\{ \mathrm{lift}(R) : R \text{ is an LV or ZLV region in } \mathcal{H}\bigr\}.
$$

**Step 4** (Lift the domain).
Let $D \subset \mathbb{R}^5$ be the lift of $\mathcal{D}$ to
$\mathbb{R}^5$:
$$
D = \mathcal{D} \times [0, M]^3 \;\subset\; \mathbb{R}^5.
$$

**Step 5** (Intersect).
$$
\mathcal{P}
= D \;\cap\; \bigcap_{R \in \mathcal{L}_2} R.
$$

This is exactly the computation performed by `compute_best_lver`:

```python
E = Region(Region_Type.INTERSECT, [domain] + [lver.data.region for lver in lvers])
E1 = E.as_disjoint_union(verbose=debug)
```

The result is a `Region` of type `DISJOINT_UNION` — a finite collection of
convex polytopes with pairwise disjoint interiors whose union is
$\mathcal{P}$.


### 4.5 Properties of $\mathcal{P}$

We establish several structural properties of $\mathcal{P}$ that are
consequences of the construction.

**Proposition 4.2** (Rationality).
Every vertex of every polytope in the disjoint decomposition of
$\mathcal{P}$ has rational coordinates.

*Proof.*
Each half-space contributing to $\mathcal{P}$ has coefficients in
$\mathbb{Q}$ (the EP parameters $k, l$ are rational; all constants
in `Constants` are rational; all literature bounds have rational
coefficients).  The vertices of a polytope defined by rational half-spaces
are rational (they are solutions of systems of linear equations with
rational coefficients).  The disjoint decomposition preserves this property,
since it only adds complementary half-spaces (negations of existing rational
constraints).
$\square$

**Proposition 4.3** (Boundedness).
$\mathcal{P}$ is bounded: it is contained in the box $\mathcal{B}$.

*Proof.*
The domain $D$ (Step 4) is contained in $\mathcal{B}$, and the intersection
in Step 5 can only shrink the region.
$\square$

**Proposition 4.4** (Non-convexity of the region; convexity of the pieces).
$\mathcal{P}$ is generally *not* convex as a region.  However, its disjoint
decomposition $\mathcal{P} = \bigsqcup_j P_j$ consists of convex polytopes
$P_j$.

*Proof.*
Individual LVER constraints are represented as disjoint unions of polytopes
(via `from_union_of_halfplanes`), which are not convex in general.  The
intersection of such regions, computed by the distributive law
(Section 2.3), is itself a disjoint union of convex polytopes.  Each piece
$P_j$ in the final decomposition is an intersection of finitely many
half-spaces, hence convex.
$\square$

**Remark 4.5** (Convex relaxation).
The convex hull $\mathrm{conv}(\mathcal{P})$ is a single convex polytope
that contains $\mathcal{P}$ and shares its projection onto each
coordinate subspace (since the projection of a union equals the union of the
projections, and the projection of a convex hull contains the convex hull of
the projections).  However, EXPDB does not compute or use
$\mathrm{conv}(\mathcal{P})$; it works directly with the disjoint
decomposition.  The non-convexity of $\mathcal{P}$ is essential: the
individual pieces carry dependency-tracking labels (polytope labels
propagated through `track_dependencies=True`) that identify which input
hypotheses contributed to each piece, enabling the construction of proof
trees.

**Proposition 4.6** (Monotonicity in the hypothesis set).
If $\mathcal{H}_1 \subseteq \mathcal{H}_2$ (as hypothesis sets), then
$$
\mathcal{P}(\mathcal{H}_2, \mathcal{D})
\;\subseteq\;
\mathcal{P}(\mathcal{H}_1, \mathcal{D}).
$$

*Proof.*
$\mathcal{H}_2$ contains all constraints of $\mathcal{H}_1$ plus
additional ones.  The intersection in Step 5 includes all half-spaces from
$\mathcal{H}_1$ and also the additional half-spaces from
$\mathcal{H}_2 \setminus \mathcal{H}_1$.  Adding constraints can only
shrink the intersection.
$\square$

**Proposition 4.7** (Dependence on domain).
If $\mathcal{D}_1 \subseteq \mathcal{D}_2$, then
$\mathcal{P}(\mathcal{H}, \mathcal{D}_1) \subseteq
\mathcal{P}(\mathcal{H}, \mathcal{D}_2)$.

*Proof.*
The domain lift $D_1 \subseteq D_2$ in Step 4, and intersection is
monotone.
$\square$


### 4.6 Dimension of $\mathcal{P}$

The master region $\mathcal{P}$ lives in $\mathbb{R}^5$ but its effective
dimension depends on the constraints.

**Proposition 4.8.**
For any non-trivial hypothesis set and any domain $\mathcal{D}$ with
non-empty interior, $\mathcal{P}$ is generically five-dimensional: at least
one polytope $P_j$ in its disjoint decomposition is full-dimensional in
$\mathbb{R}^5$.

*Proof sketch.*
The bounding box $\mathcal{B}$ is full-dimensional.  Literature constraints
are strict inequalities (they define open half-spaces whose closures are the
constraint half-spaces).  For a generic point in the interior of
$\mathcal{B}$, all constraints are satisfied with strict inequality, so a
neighborhood of that point lies in $\mathcal{P}$.
$\square$

However, specific sections of $\mathcal{P}$ (obtained by fixing some
coordinates) may have lower dimension.  In particular, the section at a
fixed $(\sigma, \tau)$ pair is a polytope in $\mathbb{R}^3$ (in coordinates
$(\rho, \rho^*, s)$), and its dimension may be 3, 2, 1, or 0 depending on
the tightness of the constraints at that $(\sigma, \tau)$ value.


### 4.7 The Three Faces of $\mathcal{P}$

The master region $\mathcal{P}$ has three natural "faces" — boundary
surfaces that correspond to the three types of downstream bounds:

1. **The $\rho$-boundary**: the upper boundary of $\mathcal{P}$ in the
   $\rho$ direction (for fixed $\sigma, \tau$).  This boundary, when
   projected onto $(\sigma, \tau, \rho)$, gives the LV region
   (Section 5.2).  The zero density estimate $A(\sigma)$ is extracted from
   this boundary by the rational supremum operator.

2. **The $\rho^*$-boundary**: the upper boundary in the $\rho^*$ direction
   (for fixed $\sigma, \tau$).  When projected onto
   $(\sigma, \tau, \rho^*)$, this gives the energy region (Section 5.4).
   The zero density energy estimate $A^*(\sigma)$ is extracted from this
   boundary.

3. **The $s$-boundary**: the upper boundary in the $s$ direction.  This
   boundary is not directly visible in the final output (since $s$ is
   eliminated by projection at every output stage), but it constrains the
   $\rho$ and $\rho^*$ boundaries indirectly through the joint constraints
   involving $s$.

The interplay between these three boundaries is the source of the pipeline's
power: constraints that involve $s$ (e.g., the Heath-Brown relations
$s \le f(\rho, \tau)$) couple the $\rho$-boundary and the
$\rho^*$-boundary, so that improvements in energy estimates ($\rho^*$)
can tighten value estimates ($\rho$) and vice versa.  This coupling is
visible only in the five-dimensional picture; it is lost when the pipeline
is described in terms of separate 3D regions.


### 4.8 $\mathcal{P}$ as the Unique Central Object

We can now state the sense in which $\mathcal{P}$ is the unique central
object of the EXPDB pipeline.

**Theorem 4.9** (Universality of $\mathcal{P}$).
Let $\mathcal{H}$ be a hypothesis set and $\mathcal{D}$ a domain.  Every
output of the EXPDB pipeline — the LV region, the ZLV region, the energy
region, the zero density estimate $A(\sigma)$, the zero density energy
estimate $A^*(\sigma)$, and the prime gap bound $\theta$ — is uniquely
determined by $\mathcal{P}(\mathcal{H}, \mathcal{D})$.  Specifically:

$$
\begin{aligned}
R_{\mathrm{LV}} &= \pi_{\sigma,\tau,\rho}(\mathcal{P}) \\[4pt]
R_{\mathrm{energy}} &= \pi_{\sigma,\tau,\rho^*}(\mathcal{P}) \\[4pt]
A(\sigma)
  &= \inf\nolimits_{\text{methods}}\,
     \sup\nolimits_\tau\bigl\{
       \rho/\tau : (\sigma,\tau,\rho) \in \pi_{\sigma,\tau,\rho}(\mathcal{P})
     \bigr\} \\[4pt]
A^*(\sigma)
  &= \inf\nolimits_{\text{methods}}\,
     \frac{1}{1 - \sigma}\,
     \sup\nolimits_\tau\bigl\{
       \rho^*/\tau : (\sigma,\tau,\rho^*) \in \pi_{\sigma,\tau,\rho^*}(\mathcal{P})
     \bigr\} \\[4pt]
\theta
  &= \sup\nolimits_\sigma\,
     \max\bigl(\alpha(\sigma;\, A, A^*),\;
               \beta(\sigma;\, A, A^*)\bigr)
\end{aligned}
$$

where $\alpha$ and $\beta$ are the rational functions of $A$ and $A^*$
defined in `prime_gap.py:compute_gap2`, and $\inf_{\text{methods}}$
denotes the lower envelope over all derivation methods (Sections 5.6–5.7).

*Proof.*
Each equation corresponds to a specific code path in the pipeline
(detailed in Section 5).  The first two are direct projections.  The third
and fourth compose projection with the rational supremum operator
(Definition 2.12) and the lower envelope operator.  The fifth composes
the preceding two with the scalar extraction in `compute_gap2`.  Each step
depends only on $\mathcal{P}$ (and the fixed functions $\alpha, \beta$
defined in the prime gap module).
$\square$

The converse is not true: $\mathcal{P}$ cannot be recovered from its
projections alone (Remark 5.10 in Section 5).  Information flows strictly
downward in the dimension ladder.


### 4.9 Comparison with a Single Convex Polytope

It is natural to ask whether $\mathcal{P}$ could be replaced by its convex
hull $\mathrm{conv}(\mathcal{P})$, which would be a single convex polytope.

The answer is: *for the purpose of computing projections and rational
suprema, yes* — the projection of a union equals the union of the
projections, which is contained in (and for convex projection, equals) the
projection of the convex hull.  Since projection and the rational supremum
are both insensitive to the decomposition into pieces, the final numerical
bounds $A(\sigma)$, $A^*(\sigma)$, and $\theta$ would be identical whether
computed from $\mathcal{P}$ or from $\mathrm{conv}(\mathcal{P})$.

However, the decomposition into pieces is essential for two reasons:

1. **Proof tracking.**  Each piece in the disjoint decomposition carries a
   label (via `polytope.dependencies`) recording which input hypotheses
   contributed to its construction.  These labels propagate through the
   distributive-law intersection algorithm and are used to construct the
   dependency DAG — the machine-readable proof.  The convex hull destroys
   this labeling.

2. **Computational efficiency.**  The disjoint decomposition enables
   piece-by-piece vertex enumeration and projection.  Computing the convex
   hull of the entire union would require merging all vertices, which may be
   more expensive than processing the pieces independently.

For the purposes of this paper, we work with $\mathcal{P}$ as a region
(disjoint union of convex polytopes) rather than as a single convex body.
The reader who prefers a single convex object may mentally replace
$\mathcal{P}$ with $\mathrm{conv}(\mathcal{P})$ wherever projections and
envelopes are discussed, with the understanding that proof tracking is lost.

## 5. Projections and Envelopes

This section demonstrates that every output of the EXPDB pipeline is a
derived quantity of the master region $\mathcal{P} \subset \mathbb{R}^5$
defined in Section 4.  We trace each derivation path from $\mathcal{P}$ to
the final output, identifying the specific geometric operation at each step
and its implementation in the codebase.

Throughout, we write $\pi_S$ for the orthogonal projection onto the
coordinate subset $S$, $\Phi_{\rho/\tau}$ for the rational supremum operator
(Definition 2.12), $\mathrm{env}^-$ for the lower envelope (pointwise
minimum over a family of functions), and $\mathrm{env}^+$ for the upper
envelope.


### 5.1 Overview: The Derivation Tree

Every pipeline output can be expressed as a composition of at most four
operations applied to $\mathcal{P}$.  The complete derivation tree is:

$$
\mathcal{P} \subset \mathbb{R}^5
$$
$$
\swarrow \qquad\qquad \downarrow \qquad\qquad \searrow
$$
$$
\pi_{\{0,1,2\}}(\mathcal{P}) \qquad
\pi_{\{0,1,3\}}(\mathcal{P}) \qquad
\pi_{\{0,1,2\}}(\mathcal{P}_\zeta)
$$
$$
R_{\mathrm{LV}} \subset \mathbb{R}^3 \qquad\;
R_{\mathrm{energy}} \subset \mathbb{R}^3 \qquad\;\;
R_{\mathrm{ZLV}} \subset \mathbb{R}^3
$$
$$
\downarrow \Phi_{\rho/\tau} \qquad\qquad
\downarrow \Phi_{\rho^*/\tau} \qquad\qquad
\downarrow \Phi_{\rho/\tau}
$$
$$
\{r_i(\sigma)\} \qquad\qquad\;
\{r^*_j(\sigma)\} \qquad\qquad\;
\{r^\zeta_k(\sigma)\}
$$
$$
\searrow\; \mathrm{env}^+ \qquad\quad
\downarrow\; \mathrm{env}^+ \qquad\quad
\swarrow\; \mathrm{env}^+
$$
$$
A_{\mathrm{raw}}(\sigma) \qquad\qquad\qquad\qquad
A^*_{\mathrm{raw}}(\sigma)
$$
$$
\downarrow\; \mathrm{env}^- \qquad\qquad\qquad\quad\;\;
\downarrow\; \mathrm{env}^-
$$
$$
A(\sigma) \qquad\qquad\qquad\qquad\qquad
A^*(\sigma)
$$
$$
\searrow \qquad\qquad\qquad\qquad \swarrow
$$
$$
\theta = \sup_\sigma \max(\alpha, \beta)
$$

We now describe each node and edge in detail.


### 5.2 The LV Region: $\pi_{\{0,1,2\}}(\mathcal{P})$

**Definition.**  The *large value region* is the projection of
$\mathcal{P}$ onto the coordinate subspace $(\sigma, \tau, \rho)$:

$$
R_{\mathrm{LV}}
= \pi_{\{0,1,2\}}(\mathcal{P})
= \bigl\{(\sigma, \tau, \rho) :
\exists\, \rho^*, s \text{ with }
(\sigma, \tau, \rho, \rho^*, s) \in \mathcal{P}\bigr\}
\;\subset\; \mathbb{R}^3.
$$

**Geometric character.**  $R_{\mathrm{LV}}$ is the *shadow* of the
five-dimensional body onto the first three coordinates.  Since projection
preserves the union structure, $R_{\mathrm{LV}} = \bigsqcup_j
\pi_{\{0,1,2\}}(P_j)$ where $P_j$ are the convex pieces of $\mathcal{P}$.
Each projected piece is a convex polytope in $\mathbb{R}^3$ (projection of a
convex polytope is convex), though the pieces may overlap after projection.

**Implementation.**  The function `lver_to_lv` (`additive_energy.py`, line
372) converts each piece to its V-representation, drops coordinates 3 and 4,
and reconstructs the H-representation via `Polytope.from_V_rep`.  A
simplification pass (`Region.simplify`) merges adjacent pieces where
possible.

**What is lost.**  The projection eliminates all constraints that involve
$\rho^*$ or $s$ non-trivially.  In particular, the Heath-Brown relations
(which couple $s$ to $\rho$ and $\tau$) lose their indirect coupling to
$\rho^*$ upon projection.  This information loss is irreversible: the LV
region does not determine the energy region or the original
$\mathcal{P}$.

**Alternative construction.**  The pipeline also constructs the LV region
*without* going through $\mathcal{P}$, via `compute_large_value_region`
(`zero_density_estimate.py`, line 148), which directly intersects
three-dimensional LV constraints and applies raise-to-power transforms in
$\mathbb{R}^3$.  The result is identical to $\pi_{\{0,1,2\}}(\mathcal{P})$
when all constraints that lift to $\mathbb{R}^5$ are also represented in
$\mathbb{R}^3$ — which holds for the LV-type constraints (Section 4.3.2)
but not for the direct LVER constraints (Section 4.3.1), which have no 3D
counterpart.  Thus the $\mathcal{P}$-based construction is strictly more
informative.


### 5.3 The ZLV Region

**Definition.**  The *zeta large value region* is:

$$
R_{\mathrm{ZLV}}
= \pi_{\{0,1,2\}}(\mathcal{P}_\zeta)
$$

where $\mathcal{P}_\zeta$ denotes $\mathcal{P}$ constructed with the
additional constraint $\tau \ge 2$ and with zeta-specific LVER hypotheses
included (see the `zeta=True` branch in `compute_best_lver`).  Equivalently,

$$
R_{\mathrm{ZLV}}
= \pi_{\{0,1,2\}}\bigl(\mathcal{P} \cap \{\tau \ge 2\}\bigr)
\;\;\cap\;\;
\pi_{\{0,1,2\}}\bigl(\textstyle\bigcap_i R_i^{\mathrm{zeta}}\bigr)
$$

where $R_i^{\mathrm{zeta}}$ are the zeta-specific LVER constraints.

**Relationship to LV.**  $R_{\mathrm{ZLV}} \subseteq R_{\mathrm{LV}}
\cap \{\tau \ge 2\}$.  The inclusion may be strict because ZLV receives
additional constraints from beta bounds (`beta_to_zlv`) and mu bounds
(`mu_to_zlv`) that are not present in the LV constraint set.


### 5.4 The Energy Region: $\pi_{\{0,1,3\}}(\mathcal{P})$

**Definition.**  The *energy region* (or *LV* region*) is the projection of
$\mathcal{P}$ onto the coordinate subspace $(\sigma, \tau, \rho^*)$:

$$
R_{\mathrm{energy}}
= \pi_{\{0,1,3\}}(\mathcal{P})
= \bigl\{(\sigma, \tau, \rho^*) :
\exists\, \rho, s \text{ with }
(\sigma, \tau, \rho, \rho^*, s) \in \mathcal{P}\bigr\}
\;\subset\; \mathbb{R}^3.
$$

**Implementation.**  The function `lver_to_energy` (`additive_energy.py`,
line 420) applies `Region.project({0, 1, 3})`, and `compute_LV_star`
(line 470) combines the construction of $\mathcal{P}$ with the projection
in a single call.

**What is lost.**  Coordinates $\rho$ (index 2) and $s$ (index 4) are
eliminated.  The constraints that couple $\rho$ to $\rho^*$ (e.g., those
from `ep_to_lver`) lose their $\rho$-component, leaving only the marginal
constraint on $\rho^*$.

**Symmetry with LV.**  The LV region and the energy region are the two
principal three-dimensional shadows of $\mathcal{P}$:

$$
R_{\mathrm{LV}} = \pi_{\sigma,\tau,\rho}(\mathcal{P}),
\qquad
R_{\mathrm{energy}} = \pi_{\sigma,\tau,\rho^*}(\mathcal{P}).
$$

They share the $(\sigma, \tau)$ subspace and differ only in which of $\rho$
or $\rho^*$ is retained.  Their joint information content is strictly less
than that of $\mathcal{P}$ itself: knowing both projections does not
determine $\mathcal{P}$, because the cross-constraints involving $s$ are
lost in both projections.


### 5.5 The Rational Supremum: From $\mathbb{R}^3$ to $\mathbb{R}^1$

The transition from three-dimensional regions to one-dimensional functions
is the most geometrically complex step in the pipeline.  It applies the
rational supremum operator (Definition 2.12) to a projected region.

**The operation.**  Given a 3D region $R$ with coordinates
$(\sigma, \tau, \rho)$ decomposed as a disjoint union of convex polytopes
$R = \bigsqcup_j P_j$, compute

$$
\Phi_{\rho/\tau}(R)(\sigma)
= \sup\bigl\{\rho / \tau : (\sigma, \tau, \rho) \in R,\; \tau > 0\bigr\}.
$$

**Algorithm.**  As described in Section 2.6, the implementation
(`compute_sup_rho_on_tau`, `zero_density_estimate.py`, line 242) proceeds by:

1. **Edge enumeration.**  For each polytope $P_j$, compute the
   V-representation and extract all edges (pairs of adjacent vertices) from
   the adjacency structure of the polyhedron.  A visited-set prevents
   duplicate processing.

2. **Parameterization.**  For each edge with endpoints
   $(\sigma_1, \tau_1, \rho_1)$ and $(\sigma_2, \tau_2, \rho_2)$ with
   $\sigma_1 \ne \sigma_2$, parameterize $\tau$ and $\rho$ as affine
   functions of $\sigma$ along the edge:
   $$
   \tau(\sigma) = \frac{\tau_1 - \tau_2}{\sigma_1 - \sigma_2}\,\sigma
   + \frac{\sigma_1\tau_2 - \sigma_2\tau_1}{\sigma_1 - \sigma_2},
   \qquad
   \rho(\sigma) = \frac{\rho_1 - \rho_2}{\sigma_1 - \sigma_2}\,\sigma
   + \frac{\sigma_1\rho_2 - \sigma_2\rho_1}{\sigma_1 - \sigma_2}.
   $$

3. **Ratio.**  Compute $r(\sigma) = \rho(\sigma)/\tau(\sigma)$, a rational
   function of degree at most $(1,1)$, defined on the interval
   $[\min(\sigma_1,\sigma_2),\, \max(\sigma_1,\sigma_2)]$.

4. **Upper envelope.**  Collect all such $(r, I)$ pairs and compute their
   pointwise maximum via `RationalFunction.max`, which resolves algebraic
   intersections between pairs of rational functions using `sympy.solve`.

**Output.**  A piecewise-rational function $\Phi_{\rho/\tau}(R)$ on a
partition of the $\sigma$-interval.

**Why the supremum is attained on edges.**  The function $\rho/\tau$ is a
linear-fractional (quasi-convex) function of $(\tau, \rho)$ for fixed
$\sigma$.  Over a convex polytope, the maximum of a linear-fractional
function is attained at a vertex.  As $\sigma$ varies continuously, the
maximizing vertex traces a path along the edges of the polytope.  Hence the
supremum over $\tau$ is realized along edges of the polytope (projected
onto the $\sigma$-axis), and $\rho/\tau$ along each edge is a
degree-$(1,1)$ rational function of $\sigma$.


### 5.6 The ZD Envelope: $A(\sigma)$

The zero density estimate $A(\sigma)$ is obtained by composing the rational
supremum with a lower envelope.  There are several routes from
$\mathcal{P}$ to $A(\sigma)$; the pipeline computes all of them and takes
their minimum.

#### 5.6.1 Route 1: LV/ZLV path (method 1, `lv_zlv_to_zd`)

This route works in $\mathbb{R}^3$ without constructing $\mathcal{P}$
explicitly.

1. Choose a parameter $\tau_0$ (a constant or an affine function of
   $\sigma$).
2. Compute the LV region restricted to $\tau \in [\tau_0, 2\tau_0]$:
   $$
   R_{\mathrm{LV}}^{[\tau_0, 2\tau_0]}
   = R_{\mathrm{LV}} \cap \{\tau_0 \le \tau \le 2\tau_0\}.
   $$
3. Compute $\Phi_{\rho/\tau}(R_{\mathrm{LV}}^{[\tau_0, 2\tau_0]})$.
4. Compute the ZLV region restricted to $\tau \in [2, \tau_0]$:
   $$
   R_{\mathrm{ZLV}}^{[2, \tau_0]}
   = R_{\mathrm{ZLV}} \cap \{2 \le \tau \le \tau_0\}.
   $$
5. Compute $\Phi_{\rho/\tau}(R_{\mathrm{ZLV}}^{[2, \tau_0]})$.
6. Take the upper envelope of (3) and (5):
   $$
   A_{\mathrm{raw}}(\sigma)
   = \mathrm{env}^+\bigl(
   \Phi_{\rho/\tau}(R_{\mathrm{LV}}^{[\tau_0, 2\tau_0]}),\;
   \Phi_{\rho/\tau}(R_{\mathrm{ZLV}}^{[2, \tau_0]})
   \bigr).
   $$

The upper envelope is necessary because $A(\sigma)$ is defined as a
*supremum* over $\tau$: one must take the worst case over both the LV and
ZLV $\tau$-ranges.

**Implementation.**  `lv_zlv_to_zd` (`zero_density_estimate.py`, line 300).
The raise-to-power transform (scaling $\tau$ and $\rho$ by $k$) is applied
in the LV region to cover the range $[\tau_0, 2\tau_0]$ from information
originally available on smaller $\tau$ values.

#### 5.6.2 Route 2: LV/ZLV path (method 2, `lv_zlv_to_zd2`)

Identical to Route 1 except $\tau_0$ is taken to be an affine function
$\tau_0(\sigma) = m\sigma + c$, and the $\tau$-ranges become
$[\frac{2}{3}\tau_0, \tau_0]$ and $[2, \frac{4}{3}\tau_0]$.  This gives
different (and sometimes tighter) bounds because the $\tau$-domain adapts
to $\sigma$.

**Implementation.**  `lv_zlv_to_zd2` (`zero_density_estimate.py`, line 393).

#### 5.6.3 Route 3: LVER path (`lver_to_zd`)

This route goes through $\mathcal{P}$ explicitly.

1. Construct $\mathcal{P}$ (the LVER) and optionally $\mathcal{P}_\zeta$
   (the zeta LVER) over specified $(\sigma, \tau)$-domains.
2. Project each to $(\sigma, \tau, \rho)$:
   $$
   R = \pi_{\{0,1,2\}}(\mathcal{P}), \qquad
   R_\zeta = \pi_{\{0,1,2\}}(\mathcal{P}_\zeta).
   $$
3. Apply $\Phi_{\rho/\tau}$ to each.
4. Take the upper envelope.

**Implementation.**  `lver_to_zd` (`zero_density_estimate.py`, line 471).
This route is strictly more powerful than Routes 1–2 when direct LVER
constraints (Section 4.3.1) are present, because those constraints tighten
the projection beyond what is achievable by intersecting only 3D regions.

#### 5.6.4 Route 4: Direct EP formulas

Two additional routes bypass the polyhedral machinery entirely, computing
$A(\sigma)$ from exponent pairs via closed-form rational expressions:

- `ivic_ep_to_zd` (`zero_density_estimate.py`, line 542): produces
  $A(\sigma) \le 3m/((3m-2)\sigma + 2 - m)$ for suitable $m$ and $\sigma$
  ranges.
- `bourgain_ep_to_zd` (`zero_density_estimate.py`, line 629): produces
  $A(\sigma) \le 4k/(2(1+k)\sigma - 1 - l)$ for suitable EP $(k,l)$.

These are not derived from $\mathcal{P}$ via projection; they are
independent paths from EP data to ZD bounds.  In the Skyline framework,
they contribute additional rational curves to the family over which the
lower envelope is taken.

#### 5.6.5 Selection: the lower envelope

After all routes have been evaluated, the final zero density estimate is:

$$
A(\sigma)
= \mathrm{env}^-\bigl(
A^{(1)}_{\mathrm{raw}}(\sigma),\;
A^{(2)}_{\mathrm{raw}}(\sigma),\;
\ldots,\;
A^{(n)}_{\mathrm{raw}}(\sigma),\;
A_{\mathrm{lit}}(\sigma)
\bigr)
$$

where $A^{(i)}_{\mathrm{raw}}$ are the derived bounds and
$A_{\mathrm{lit}}$ are the literature zero density estimates.  The lower
envelope is computed by `best_zero_density_estimate`
(`zero_density_estimate.py`, line 765), which calls `RationalFunction.min`.

**Geometric meaning.**  The final $A(\sigma)$ is the lower boundary of the
epigraph
$$
\mathrm{epi}(A)
= \bigl\{(\sigma, y) : y \ge A^{(i)}(\sigma) \text{ for some } i\bigr\}
$$
— a one-dimensional analogue of the convex hull computation in the EP
stage.


### 5.7 The ZDE Envelope: $A^*(\sigma)$

The zero density energy estimate $A^*(\sigma)$ follows an analogous path
through the *energy projection* rather than the LV projection.

**Route.**

1. Construct $\mathcal{P}$ over a domain $\tau_0 \le \tau \le 2\tau_0$
   (and $\mathcal{P}_\zeta$ over $2 \le \tau \le \tau_0$).
2. Project each to $(\sigma, \tau, \rho^*)$:
   $$
   R_{\mathrm{energy}}
   = \pi_{\{0,1,3\}}(\mathcal{P}),
   \qquad
   R_{\mathrm{energy}}^\zeta
   = \pi_{\{0,1,3\}}(\mathcal{P}_\zeta).
   $$
3. Apply the rational supremum $\Phi_{\rho^*/\tau}$ to each.
4. Take the upper envelope.
5. Divide by $(1 - \sigma)$:
   $$
   A^*_{\mathrm{raw}}(\sigma)
   = \frac{1}{1 - \sigma}\;
   \mathrm{env}^+\bigl(
   \Phi_{\rho^*/\tau}(R_{\mathrm{energy}}),\;
   \Phi_{\rho^*/\tau}(R_{\mathrm{energy}}^\zeta)
   \bigr).
   $$
6. The final estimate is the lower envelope over all derivation methods:
   $A^*(\sigma) = \mathrm{env}^-(A^{*,(1)}_{\mathrm{raw}}, \ldots,
   A_{\mathrm{lit}}^*)$.

**Implementation.**  `lver_to_energy_bound`
(`zero_density_energy_estimate.py`, line 251) constructs $\mathcal{P}$,
projects, computes the rational supremum via `compute_sup_LV_on_tau`
(which is structurally identical to `compute_sup_rho_on_tau` but operates on
$(\sigma, \tau, \rho^*)$ data), and divides by the rational function
$(1 - \sigma) = RF([-1, 1])$.  The selection is performed by
`compute_best_energy_bound` (line 403) via `RationalFunction.min`.

**The division by $(1 - \sigma)$.**  This normalization introduces a simple
pole at $\sigma = 1$ in the rational functions comprising $A^*$.  The pole
is harmless because the pipeline restricts $\sigma$ to the interval
$[\frac{1}{2}, 1)$ (the constant `ZERO_DENSITY_SIGMA_LIMIT = 0.999`
truncates the domain before $\sigma = 1$).  Algebraically, the division
maps a degree-$(1,1)$ rational function $r(\sigma) = (c\sigma + d)/(a\sigma + b)$ to the
degree-$(1,2)$ function $(c\sigma + d)/((a\sigma + b)(-\sigma + 1))$,
increasing the degree of the envelope.


### 5.8 The EP Hull and Beta Envelope as Derived Objects

The exponent pair hull and beta envelope do not arise as projections of
$\mathcal{P}$ in the same direct sense as the LV and energy regions.
Instead, they occupy a *dual* position: they generate constraints on
$\mathcal{P}$ (via `ep_to_lver` and `beta_to_zlv`), and they are
themselves derived from a separate two-dimensional construction.
Nevertheless, they fit naturally into the Skyline framework as objects
determined by the *input data* to $\mathcal{P}$ rather than by its
*projections*.

#### 5.8.1 The EP hull

The EP hull is $\mathrm{conv}(S)$ where $S = \{(k_i, l_i)\}$ is the set of
all known exponent pairs (after iterative expansion by A, B, C transforms
and beta-to-EP conversion).  It lives in $\mathbb{R}^2$ and is computed by
`scipy.spatial.ConvexHull`.

The EP hull is related to $\mathcal{P}$ as follows: each vertex $(k, l)$ of
the hull generates, via `ep_to_lver`, a collection of half-space constraints
on $\mathcal{P}$.  Thus the EP hull *parameterizes a family of constraints*
on $\mathcal{P}$.  A larger EP hull (more vertices) produces more
constraints, yielding a tighter $\mathcal{P}$.

#### 5.8.2 The beta envelope

The beta envelope $\beta^*(\alpha) = \min_i\{(l_i - k_i)\alpha + k_i\}$ is
the lower envelope of the family of affine functions dual to the EP hull
vertices (Section 2.7, Remark 2.15).  It is a concave piecewise-affine
function on $[0, 1/2]$.

The beta envelope is related to $\mathcal{P}$ via `beta_to_zlv`: each
affine piece of $\beta^*$ generates a half-space in $\mathbb{R}^3$ (the
zero-set boundary in ZLV space), which lifts to a half-space in
$\mathbb{R}^5$.  Thus the beta envelope, like the EP hull, *parameterizes a
family of constraints* on $\mathcal{P}$.

#### 5.8.3 The mu hull

The mu hull is the convex hull of $\{(\sigma_i, \mu_i)\} \subset
\mathbb{R}^2$.  It is related to the EP hull by the linear isomorphism
$(k, l) \mapsto (l - k, k)$ and to $\mathcal{P}$ via `mu_to_zlv`: each
vertex generates a half-space in ZLV space, hence in $\mathbb{R}^5$.


### 5.9 The Prime Gap Bound: $\theta$

The prime gap bound is the final scalar output, computed from $A(\sigma)$
and $A^*(\sigma)$.

**Construction** (`compute_gap2`, `prime_gap.py`, line 11):

1. Compute $A(\sigma)$ and $A^*(\sigma)$ as piecewise-rational functions
   (Sections 5.6–5.7).
2. Partition $[\frac{1}{2}, 1]$ into subintervals aligned with the
   breakpoints of both $A$ and $A^*$.
3. On each subinterval, define two rational functions of $\sigma$:
   $$
   \alpha(\sigma) = 4\sigma - 2
   + \frac{2(A^*(\sigma)(1 - \sigma) - 1)}{A^*(\sigma) - A(\sigma)},
   \qquad
   \beta(\sigma) = 4\sigma - 2
   + \frac{A^*(\sigma)(1 - \sigma) - 1}{A(\sigma)}.
   $$
4. Find the stationary points of $\alpha$ and $\beta$ on each subinterval
   (via `sympy.solve` on the derivative) and evaluate at all critical points
   and endpoints.
5. Take $\theta = \sup_\sigma \max(\alpha(\sigma), \beta(\sigma))$ over all
   subintervals.

**Geometric meaning.**  The functions $\alpha$ and $\beta$ are rational
functions of $\sigma$ whose coefficients are themselves rational functions
of $A(\sigma)$ and $A^*(\sigma)$.  The scalar $\theta$ is the maximum of
these two rational surfaces over the one-dimensional domain.  It is the
terminal dimensional collapse:

$$
\mathbb{R}^5
\;\xrightarrow{\;\pi\;}\;
\mathbb{R}^3
\;\xrightarrow{\;\Phi_{\rho/\tau}\;}\;
\mathbb{R}^1
\;\xrightarrow{\;\mathrm{env}^-\;}\;
\mathbb{R}^1
\;\xrightarrow{\;\sup\;}\;
\mathbb{R}^0.
$$


### 5.10 Non-Reconstructibility

We noted in Theorem 4.9 that $\mathcal{P}$ determines all downstream
objects.  The converse is false:

**Remark 5.1** (Non-reconstructibility).
The pair $(R_{\mathrm{LV}}, R_{\mathrm{energy}})$ does not determine
$\mathcal{P}$.

*Proof sketch.*
Consider two five-dimensional polytopes $\mathcal{P}$ and $\mathcal{P}'$
that differ only in their constraints involving $s$ (coordinate 4) but agree
on all constraints involving only $(\sigma, \tau, \rho)$ or only
$(\sigma, \tau, \rho^*)$.  Then
$\pi_{\{0,1,2\}}(\mathcal{P}) = \pi_{\{0,1,2\}}(\mathcal{P}')$ and
$\pi_{\{0,1,3\}}(\mathcal{P}) = \pi_{\{0,1,3\}}(\mathcal{P}')$, but
$\mathcal{P} \ne \mathcal{P}'$.  The $s$-coordinate couples $\rho$ and
$\rho^*$ through joint constraints (e.g., the Heath-Brown relations
$s \le f(\rho, \tau)$ combined with $\rho^* \le g(s, \sigma)$), but this
coupling is invisible in either projection taken alone.
$\square$

More strongly:

**Remark 5.2.**  The functions $A(\sigma)$ and $A^*(\sigma)$ do not
determine the 3D regions $R_{\mathrm{LV}}$ and $R_{\mathrm{energy}}$.

*Proof sketch.*  The rational supremum $\Phi_{\rho/\tau}$ is a
many-to-one map: different 3D regions can yield the same 1D function.
For instance, modifying $R_{\mathrm{LV}}$ in a region of $(\sigma, \tau)$-space
where $\rho/\tau$ is not maximal does not change $\Phi_{\rho/\tau}$.
$\square$

These observations formalize the information hierarchy:

$$
\mathcal{P}
\;\;\supsetneq\;\;
(R_{\mathrm{LV}},\, R_{\mathrm{energy}})
\;\;\supsetneq\;\;
(A(\sigma),\, A^*(\sigma))
\;\;\supsetneq\;\;
\theta
$$

where $\supsetneq$ denotes "strictly more informative."  Each step down the
dimension ladder discards information that cannot be recovered.


### 5.11 Summary of Derivation Paths

We collect the complete mapping from $\mathcal{P}$ to each output in a
single table.

| Output | Formula | Operations | Code path |
|--------|---------|-----------|-----------|
| $R_{\mathrm{LV}}$ | $\pi_{\{0,1,2\}}(\mathcal{P})$ | Project | `lver_to_lv` |
| $R_{\mathrm{ZLV}}$ | $\pi_{\{0,1,2\}}(\mathcal{P}_\zeta)$ | Project | `lver_to_lv` (zeta) |
| $R_{\mathrm{energy}}$ | $\pi_{\{0,1,3\}}(\mathcal{P})$ | Project | `lver_to_energy` |
| $\mathrm{LV}^*$ | $\pi_{\{0,1,3\}}(\mathcal{P})$ | Project | `compute_LV_star` |
| $A_{\mathrm{raw}}^{(i)}(\sigma)$ | $\Phi_{\rho/\tau}(\pi_{\{0,1,2\}}(\mathcal{P}^{(i)}))$ | Project + Sup | `lver_to_zd` / `lv_zlv_to_zd` |
| $A(\sigma)$ | $\mathrm{env}^-(\{A^{(i)}_{\mathrm{raw}}\} \cup A_{\mathrm{lit}})$ | Lower envelope | `best_zero_density_estimate` |
| $A^*_{\mathrm{raw}}(\sigma)$ | $\Phi_{\rho^*/\tau}(\pi_{\{0,1,3\}}(\mathcal{P})) / (1{-}\sigma)$ | Project + Sup + Divide | `lver_to_energy_bound` |
| $A^*(\sigma)$ | $\mathrm{env}^-(\{A^{*,(j)}_{\mathrm{raw}}\} \cup A^*_{\mathrm{lit}})$ | Lower envelope | `compute_best_energy_bound` |
| $\theta$ | $\sup_\sigma \max(\alpha(\sigma; A, A^*),\, \beta(\sigma; A, A^*))$ | Sup of max | `compute_gap2` |
| EP hull | $\mathrm{conv}(\{(k_i, l_i)\})$ | Convex hull in $\mathbb{R}^2$ | `compute_convex_hull` |
| $\beta^*(\alpha)$ | $\min_i\{(l_i{-}k_i)\alpha + k_i\}$ | Lower envelope of affines | `compute_best_beta_bounds` |
| $\mu^*(\sigma)$ | Lower hull of $\{(\sigma_i, \mu_i)\}$ | Convex hull in $\mathbb{R}^2$ | `best_mu_bound` |

Every row is either a projection, an envelope, a supremum, or a composition
thereof, confirming Theorem 4.9.

## 6. The EXPDB Skyline Invariant

This section formally defines the EXPDB Skyline, establishes it as a
monotone invariant of the pipeline, and proves that the iterative flow
converges to a fixed point.


### 6.1 Definition of the Skyline

We fix a literature hypothesis set $\mathcal{H}_0$ (the output of
`literature.py`) and a domain $\mathcal{D} \subseteq [\frac{1}{2}, 1]
\times [0, T]$ in $(\sigma, \tau)$-space.

**Definition 6.1** (EXPDB Skyline).
The *EXPDB Skyline* associated to $(\mathcal{H}_0, \mathcal{D})$ is the
tuple

$$
\Sigma = \Sigma(\mathcal{H}_0, \mathcal{D})
= \bigl(\,
\mathcal{C}_{\mathrm{EP}},\;
\beta^*,\;
\mathcal{C}_{\mu},\;
R_{\mathrm{LV}},\;
R_{\mathrm{ZLV}},\;
\mathcal{P},\;
A,\;
A^*,\;
\theta
\,\bigr)
$$

where:

| Component | Symbol | Space | Definition |
|-----------|--------|-------|-----------|
| EP hull | $\mathcal{C}_{\mathrm{EP}}$ | Convex body in $\mathbb{R}^2$ | $\mathrm{conv}\bigl(\{(k_i, l_i)\}\bigr)$ after iterative expansion (Section 5.8.1) |
| Beta envelope | $\beta^*$ | Piecewise-affine function on $[0, \frac{1}{2}]$ | Lower envelope of $\{(l_i - k_i)\alpha + k_i\}$ (Section 5.8.2) |
| Mu hull | $\mathcal{C}_{\mu}$ | Convex body in $\mathbb{R}^2$ | Lower convex hull of $\{(\sigma_j, \mu_j)\}$ (Section 5.8.3) |
| LV region | $R_{\mathrm{LV}}$ | Region in $\mathbb{R}^3$ | $\pi_{\{0,1,2\}}(\mathcal{P})$ (Section 5.2) |
| ZLV region | $R_{\mathrm{ZLV}}$ | Region in $\mathbb{R}^3$ | $\pi_{\{0,1,2\}}(\mathcal{P}_\zeta)$ (Section 5.3) |
| Master region | $\mathcal{P}$ | Region in $\mathbb{R}^5$ | $\mathcal{P}(\mathcal{H}, \mathcal{D})$ (Definition 4.1) |
| ZD estimate | $A$ | Piecewise-rational on $[\frac{1}{2}, 1]$ | $\mathrm{env}^-\bigl(\{\Phi_{\rho/\tau}(\cdot)\}\bigr)$ (Section 5.6) |
| ZDE estimate | $A^*$ | Piecewise-rational on $[\frac{1}{2}, 1]$ | $\mathrm{env}^-\bigl(\{\Phi_{\rho^*/\tau}(\cdot)/(1{-}\sigma)\}\bigr)$ (Section 5.7) |
| Prime gap bound | $\theta$ | $\mathbb{R}$ | $\sup_\sigma \max(\alpha, \beta)$ (Section 5.9) |

The Skyline is the complete collection of boundary objects produced by the
pipeline at every level of the dimension ladder.

**Remark 6.2.**  The components of $\Sigma$ are not independent.  By
Theorem 4.9, the components $R_{\mathrm{LV}}$, $R_{\mathrm{ZLV}}$, $A$,
$A^*$, and $\theta$ are all determined by $\mathcal{P}$.  Conversely,
$\mathcal{P}$ depends on $\mathcal{C}_{\mathrm{EP}}$, $\beta^*$, and
$\mathcal{C}_{\mu}$ (which generate constraints on $\mathcal{P}$).  The
Skyline records *all* intermediate objects, including those that are
logically redundant, because each occupies a distinct position in the
dimension ladder and because the pipeline produces them through distinct
code paths.


### 6.2 The State Lattice

We equip the space of Skylines with the product partial order defined in
Section 2.8 (Definition 2.18).  Recall that the order on each component is
"tighter is smaller":

| Component | Order $\preceq$ (tighter) | Meet $\wedge$ |
|-----------|--------------------------|---------------|
| $\mathcal{C}_{\mathrm{EP}}$ | $H_1 \preceq H_2$ iff $H_1 \supseteq H_2$ (larger hull is tighter) | Convex hull of the union |
| $\beta^*$ | $f \preceq g$ iff $f \le g$ pointwise (lower is tighter) | Pointwise minimum |
| $\mathcal{C}_{\mu}$ | $H_1 \preceq H_2$ iff lower boundary of $H_1$ $\le$ lower boundary of $H_2$ | Convex hull of the union |
| $R_{\mathrm{LV}}$ | $R_1 \preceq R_2$ iff $R_1 \subseteq R_2$ (smaller region is tighter) | Intersection |
| $R_{\mathrm{ZLV}}$ | Same as $R_{\mathrm{LV}}$ | Intersection |
| $\mathcal{P}$ | $P_1 \preceq P_2$ iff $P_1 \subseteq P_2$ | Intersection |
| $A$ | $f \preceq g$ iff $f \le g$ pointwise | Pointwise minimum |
| $A^*$ | Same as $A$ | Pointwise minimum |
| $\theta$ | $\le$ (standard order on $\mathbb{R}$) | Minimum |

The product order is: $\Sigma_1 \preceq \Sigma_2$ iff every component of
$\Sigma_1$ is at least as tight as the corresponding component of
$\Sigma_2$.

**Remark 6.3** (Ascending vs. descending).
The convention deserves comment.  For the EP hull and Mu hull, "tighter"
means *larger* (more known pairs yield a larger hull, which in turn produces
more tangent-line constraints downstream).  For all other components,
"tighter" means *smaller* (a smaller feasible region or a lower function
value is a stronger bound).  The product lattice $\mathcal{L}$ accommodates
both conventions by using the reversed inclusion order for hulls.


### 6.3 The Pipeline Operator $\Phi$

The EXPDB pipeline defines a map $\Phi: \mathcal{L} \to \mathcal{L}$ that
takes a Skyline state and produces a refined Skyline state.  We decompose
$\Phi$ into nine component operators, one per Skyline component, applied in
the following order.

**Stage 1: EP expansion.**
$$
\Phi_{\mathrm{EP}}(\Sigma)
= \mathrm{conv}\Bigl(
\mathcal{C}_{\mathrm{EP}}
\;\cup\; \bigl\{T(p) : T \in \{A,B,C\},\; p \in \mathrm{vert}(\mathcal{C}_{\mathrm{EP}})\bigr\}
\;\cup\; \mathrm{BetaToEP}(\beta^*)
\Bigr)
$$

This applies the A, B, C transforms to all current hull vertices, adds any
new exponent pairs obtained by converting the current beta envelope back to
EPs via hull-edge duality (Section 5.8.2), and recomputes the convex hull.
The operator is iterated up to `search_depth` times within a single call to
`compute_exp_pairs`.

**Stage 2: Beta refinement.**
$$
\Phi_{\beta}(\Sigma)
= \mathrm{env}^-\Bigl(
\mathrm{EPtoBeta}(\mathcal{C}_{\mathrm{EP}})
\;\cup\; \mathrm{DToBeta}(\mathcal{C}_{\mathrm{EP}})
\;\cup\; \mathrm{VdC}_\beta(\beta^*)
\Bigr)
$$

This converts each EP hull vertex to an affine beta bound, applies the
D-process to obtain additional piecewise-affine bounds, applies the van der
Corput beta iteration to the current envelope, and takes the lower envelope
of all pieces.

**Stage 3: Mu refinement.**
$$
\Phi_{\mu}(\Sigma)
= \mathrm{LowerHull}\Bigl(
\mathrm{EPtoMu}(\mathcal{C}_{\mathrm{EP}})
\;\cup\; \mathrm{BetaToMu}(\beta^*)
\;\cup\; \mathrm{FuncEq}(\mathcal{C}_{\mu})
\;\cup\; \mathcal{C}_{\mu}
\Bigr)
$$

This collects mu points from EPs (linear map), from beta bounds
(Legendre-type evaluation), and from the functional equation (involution),
and recomputes the lower convex hull.

**Stage 4: LV intersection.**
$$
\Phi_{\mathrm{LV}}(\Sigma)
= R_{\mathrm{LV}}^{(\mathrm{lit})}
\;\cap\; \bigcap_{k=2}^{K} \Lambda_k(R_{\mathrm{LV}}^{(\mathrm{lit})})
$$

This intersects all literature LV regions with their raise-to-power
rescalings.  (In Route 3 of Section 5.6, this is subsumed by the LVER
construction; here we record it as a separate stage because Routes 1–2
operate purely in $\mathbb{R}^3$.)

**Stage 5: ZLV construction.**
$$
\Phi_{\mathrm{ZLV}}(\Sigma)
= \Phi_{\mathrm{LV}}(\Sigma) \cap \{\tau \ge 2\}
\;\cap\; \mathrm{BetaToZLV}(\beta^*)
\;\cap\; \mathrm{MuToZLV}(\mathcal{C}_{\mu})
$$

**Stage 6: Master region construction.**
$$
\Phi_{\mathcal{P}}(\Sigma)
= \mathcal{P}(\mathcal{H}, \mathcal{D})
$$

as defined in Definition 4.1 — the intersection of all LVER constraints
(direct, lifted, EP-derived, and raise-to-power) within the domain
$\mathcal{D}$.  This is the central contraction step.

**Stage 7: ZD envelope.**
$$
\Phi_A(\Sigma)
= \mathrm{env}^-\Bigl(
\bigl\{\Phi_{\rho/\tau}\bigl(\pi_{\{0,1,2\}}(\mathcal{P}^{(i)})\bigr)\bigr\}_i
\;\cup\; A_{\mathrm{lit}}
\;\cup\; A_{\mathrm{EP}}
\Bigr)
$$

where $\mathcal{P}^{(i)}$ ranges over instances of $\mathcal{P}$ constructed
with different $(\sigma, \tau)$-domain choices and $\tau_0$ parameters, and
$A_{\mathrm{EP}}$ denotes the direct EP-based ZD estimates (Routes 4 in
Section 5.6).

**Stage 8: ZDE envelope.**
$$
\Phi_{A^*}(\Sigma)
= \mathrm{env}^-\Bigl(
\bigl\{\Phi_{\rho^*/\tau}\bigl(\pi_{\{0,1,3\}}(\mathcal{P}^{(j)})\bigr)
/ (1 - \sigma)\bigr\}_j
\;\cup\; A^*_{\mathrm{lit}}
\Bigr)
$$

**Stage 9: Scalar extraction.**
$$
\Phi_\theta(\Sigma)
= \sup_\sigma \max\bigl(\alpha(\sigma;\, \Phi_A, \Phi_{A^*}),\;
\beta(\sigma;\, \Phi_A, \Phi_{A^*})\bigr)
$$

The full operator is the composition:
$$
\Phi = (\Phi_\theta \circ \Phi_{A^*} \circ \Phi_A \circ
\Phi_{\mathcal{P}} \circ \Phi_{\mathrm{ZLV}} \circ \Phi_{\mathrm{LV}}
\circ \Phi_\mu \circ \Phi_\beta \circ \Phi_{\mathrm{EP}}).
$$


### 6.4 Monotonicity

**Theorem 6.4** (Monotonicity of $\Phi$).
The operator $\Phi$ is monotone on the state lattice $\mathcal{L}$: if
$\Sigma_1 \preceq \Sigma_2$, then $\Phi(\Sigma_1) \preceq \Phi(\Sigma_2)$.

*Proof.*
We verify monotonicity for each component operator.

*Stage 1 ($\Phi_{\mathrm{EP}}$).*  If
$\mathcal{C}_{\mathrm{EP}}^{(1)} \supseteq \mathcal{C}_{\mathrm{EP}}^{(2)}$
(i.e., hull 1 is at least as large as hull 2), then applying the same set of
transforms to a superset of vertices produces a superset of output points.
Taking the convex hull preserves the superset relation.  The
$\mathrm{BetaToEP}$ step is also monotone: a lower beta envelope (tighter)
has breakpoints that correspond to at least as many hull edges, producing at
least as many EP points.  Hence
$\Phi_{\mathrm{EP}}(\Sigma_1) \supseteq \Phi_{\mathrm{EP}}(\Sigma_2)$.

*Stage 2 ($\Phi_\beta$).*  A larger EP hull produces more tangent-line
affine bounds (more terms in the minimum), so the lower envelope can only
decrease.  The VdC-$\beta$ iteration is monotone: it derives new affine
bounds from the existing envelope, and a lower input envelope yields
lower-or-equal derived bounds.  Hence
$\Phi_\beta(\Sigma_1) \le \Phi_\beta(\Sigma_2)$ pointwise.

*Stage 3 ($\Phi_\mu$).*  Monotone by the same argument: more EP points and a
lower beta envelope produce more mu points, yielding a lower (tighter) hull
boundary.

*Stage 4 ($\Phi_{\mathrm{LV}}$).*  If
$R_{\mathrm{LV}}^{(1)} \subseteq R_{\mathrm{LV}}^{(2)}$ (tighter
region), then adding the same raise-to-power rescalings and intersecting
preserves inclusion: $\Phi_{\mathrm{LV}}(\Sigma_1) \subseteq
\Phi_{\mathrm{LV}}(\Sigma_2)$.

*Stage 5 ($\Phi_{\mathrm{ZLV}}$).*  Monotone because intersection with
additional half-spaces (from tighter beta and mu bounds) preserves inclusion.

*Stage 6 ($\Phi_{\mathcal{P}}$).*  By Proposition 4.6, a hypothesis set
with more (or tighter) constraints produces a smaller $\mathcal{P}$.  Since
all upstream stages are monotone, tighter inputs propagate to a tighter
$\mathcal{P}$.

*Stage 7 ($\Phi_A$).*  The projection $\pi_{\{0,1,2\}}$ is monotone
(Proposition 4.6 and the monotonicity of projection in the inclusion order).
The rational supremum $\Phi_{\rho/\tau}$ is monotone: a smaller region
yields a smaller supremum.  The lower envelope of a superset of functions
is at most the lower envelope of a subset.  Hence $\Phi_A$ is monotone.

*Stage 8 ($\Phi_{A^*}$).*  Identical argument with the energy projection.

*Stage 9 ($\Phi_\theta$).*  The supremum of a maximum of two functions is
monotone in each function argument: if $A_1 \le A_2$ and $A_1^* \le A_2^*$
pointwise, then the rational expressions $\alpha(\sigma; A_1, A_1^*)$ and
$\beta(\sigma; A_1, A_1^*)$ are at most the corresponding expressions with
$(A_2, A_2^*)$ (this can be verified from the explicit formulas in
`compute_gap2`, noting that $\alpha$ and $\beta$ are both increasing in $A$
and $A^*$).  Hence $\Phi_\theta(\Sigma_1) \le \Phi_\theta(\Sigma_2)$.
$\square$


### 6.5 Contractivity

**Theorem 6.5** (Contractivity of $\Phi$).
For any reachable state $\Sigma$ (obtained by applying the pipeline to
$\mathcal{H}_0$), $\Phi(\Sigma) \preceq \Sigma$.

*Proof.*
We verify that each component of $\Phi(\Sigma)$ is at least as tight as the
corresponding component of $\Sigma$.

*EP hull.*  The transform loop can only add new points to the hull (it never
removes existing vertices).  The convex hull of a superset contains the
original hull.  Hence
$\Phi_{\mathrm{EP}}(\Sigma) \supseteq \mathcal{C}_{\mathrm{EP}}$.

*Beta envelope.*  The lower envelope of a larger collection of affine
functions is pointwise $\le$ the lower envelope of a subset.  The VdC-$\beta$
iteration produces new affine pieces that are $\le$ existing pieces where
they improve the bound, and leaves the bound unchanged elsewhere.  Hence
$\Phi_\beta(\Sigma) \le \beta^*$ pointwise.

*Mu hull.*  Adding new mu points (from newly derived EPs and beta bounds)
can only lower (or maintain) the lower hull boundary.

*LV region.*  Intersecting with additional constraints (raise-to-power
rescalings) can only shrink the region:
$\Phi_{\mathrm{LV}}(\Sigma) \subseteq R_{\mathrm{LV}}$.

*ZLV region.*  Same argument.

*Master region.*  $\Phi_{\mathcal{P}}(\Sigma) \subseteq \mathcal{P}$
because the new $\mathcal{P}$ is defined as an intersection that includes
all constraints used to define the previous $\mathcal{P}$, plus any new
constraints from tightened upstream components.

*ZD and ZDE.*  The lower envelope of a superset of candidate functions is
$\le$ the lower envelope of a subset.  New derivation routes may produce
additional candidate functions, and the envelope over the expanded set can
only decrease.

*Scalar.*  Follows from the monotonicity of the $\alpha, \beta$ formulas in
$A$ and $A^*$: tighter functions yield a smaller supremum.
$\square$


### 6.6 Convergence

**Theorem 6.6** (Finite convergence).
Let $\Sigma_0$ be the initial Skyline state obtained from the literature
hypotheses $\mathcal{H}_0$.  The sequence
$\Sigma_0, \Phi(\Sigma_0), \Phi^2(\Sigma_0), \ldots$ stabilizes: there
exists $N \in \mathbb{N}$ such that $\Phi^N(\Sigma_0) = \Phi^{N+1}(\Sigma_0)$.

*Proof.*
By Theorems 6.4 and 6.5, the sequence $(\Sigma_n)_{n \ge 0}$ is a
descending chain in $\mathcal{L}$:
$\Sigma_0 \succeq \Sigma_1 \succeq \Sigma_2 \succeq \cdots$.  We show
that this chain must stabilize.

*EP component.*  The EP hull is a convex polygon in $\mathbb{R}^2$ whose
vertices are rational points with denominators bounded by the products of
denominators appearing in the transforms.  At each iteration, the transform
loop applies rational maps to existing vertices and prunes to hull vertices.
The number of hull vertices is bounded (by the `search_depth` parameter and
the observation that the A-process contracts, limiting the number of new
points that can appear on the hull boundary after finitely many steps).
More directly, EXPDB imposes a hard truncation:
`search_depth` $\le$ `EXP_PAIR_TRUNCATION` $= 20$, so at most 20
iterations are applied.  The EP hull stabilizes after at most 20 rounds.

*Beta component.*  The lower envelope of finitely many affine functions has
finitely many pieces.  Each round of the VdC-$\beta$ iteration can add at
most finitely many new pieces (each pair of existing pieces produces at most
one new candidate piece).  The `BETA_TRUNCATION` constant bounds the number
of iterations.  The beta envelope stabilizes in finitely many steps.

*Mu component.*  The convex hull of finitely many rational points in
$\mathbb{R}^2$ is computed once from the available EP and beta data and does
not iterate.  It stabilizes in one step.

*LV, ZLV, $\mathcal{P}$ components.*  These are constructed by a single
intersection of finitely many regions.  There is no iterative loop; the
construction is a single-pass computation.  These components are determined
by the upstream EP, beta, and mu components and by the literature
hypotheses; once the upstream components stabilize, these stabilize
immediately.

*ZD, ZDE components.*  Each is a lower envelope of finitely many
piecewise-rational functions.  The set of candidate functions is determined
by the upstream regions, the literature estimates, and the direct EP-based
formulas.  Once the upstream components stabilize, the set of candidates is
fixed, and the lower envelope is a deterministic computation.

*Scalar component.*  Determined by $A$ and $A^*$.  Once these stabilize,
$\theta$ is fixed.

Combining these observations, stabilization occurs after at most
$N = \mathtt{EXP\_PAIR\_TRUNCATION}$ iterations of the EP loop, plus
at most $\mathtt{BETA\_TRUNCATION}$ iterations of the VdC-$\beta$ loop
(these run within a single call to the pipeline rather than as
iterated applications of $\Phi$), plus one pass through each of the
remaining stages.  In practice, $N$ is small (typically 5–10 for the EP
loop).
$\square$

**Definition 6.7** (Skyline fixed point).
The *Skyline fixed point* is $\Sigma^* = \lim_{n \to \infty} \Phi^n(\Sigma_0)
= \Phi^N(\Sigma_0)$.  It is the tightest Skyline derivable from
$\mathcal{H}_0$ using the transformations available in EXPDB.


### 6.7 Uniqueness and Optimality

**Proposition 6.8** (Uniqueness).
The Skyline fixed point $\Sigma^*$ is the unique fixed point of $\Phi$ that
is reachable from $\Sigma_0$.

*Proof.*
The sequence $(\Sigma_n)$ is monotonically descending and converges to
$\Sigma^*$.  If $\Sigma'$ were another fixed point with
$\Sigma' \preceq \Sigma^*$ (strictly tighter), then by contractivity
$\Phi(\Sigma') = \Sigma' \preceq \Sigma^*$, and by monotonicity
$\Sigma^* = \Phi(\Sigma^*) \preceq \Phi(\Sigma') = \Sigma'$.  Hence
$\Sigma^* \preceq \Sigma'$, contradicting the assumption.  Thus
$\Sigma^* = \Sigma'$.
$\square$

**Remark 6.9** (Optimality relative to the transformation set).
$\Sigma^*$ is optimal in the following precise sense: for each component,
the corresponding bound is the tightest that can be obtained by any finite
sequence of applications of the transformations cataloged in Section 3.5
to the axioms in $\mathcal{H}_0$.  It is *not* optimal in an absolute
sense — a larger transformation set (e.g., one including Huxley subdivision,
which is declared `NotImplementedError` in the current codebase) might yield
a strictly tighter fixed point.

**Remark 6.10** (Dependence on parameters).
The Skyline $\Sigma^*$ depends on two classes of parameters:
- **Continuous parameters**: the $\tau_0$ choices in each
  `prove_zero_density` call and the domain $\mathcal{D}$.  Different
  choices yield different instances of $\mathcal{P}$ and hence different
  ZD/ZDE candidates entering the lower envelope.  The current codebase uses
  manually selected $\tau_0$ values; optimizing over $\tau_0$ is an open
  problem (Section 9).
- **Discrete parameters**: the truncation constants
  (`search_depth`, `BETA_TRUNCATION`, etc.).  Increasing these parameters
  can only tighten the Skyline (more iterations of the EP loop, more
  rescaling factors in raise-to-power), but they increase computation time.


### 6.8 Structural Properties of the Skyline

We record several structural properties that follow from the definitions and
the results of Sections 4–5.

**Proposition 6.11** (Rational representability).
Every component of $\Sigma^*$ is finitely representable over $\mathbb{Q}$:

- $\mathcal{C}_{\mathrm{EP}}$ and $\mathcal{C}_\mu$ are convex hulls of
  finitely many rational points.
- $\beta^*$ is a piecewise-affine function with rational slopes, intercepts,
  and breakpoints.
- $R_{\mathrm{LV}}$, $R_{\mathrm{ZLV}}$, and $\mathcal{P}$ are finite
  disjoint unions of polytopes with rational H-representations.
- $A$ and $A^*$ are piecewise-rational functions with rational coefficients
  and rational breakpoints.
- $\theta$ is a computable real number (an algebraic number determined by a
  finite system of polynomial equations with rational coefficients).

*Proof.*  Each component is constructed from rational input data by
operations that preserve rationality: convex hull, affine transformation,
intersection of rational half-spaces, projection of rational polytopes,
quotients of rational polynomials, and root-finding over $\mathbb{Q}[x]$.
$\square$

**Proposition 6.12** (Monotonicity in axioms).
If $\mathcal{H}_0 \subseteq \mathcal{H}_0'$, then
$\Sigma^*(\mathcal{H}_0') \preceq \Sigma^*(\mathcal{H}_0)$.

*Proof.*  A larger axiom set yields a larger initial EP hull, a lower
initial beta envelope, and more half-space constraints on $\mathcal{P}$.
By Theorem 6.4, these propagate through $\Phi$ to a tighter fixed point.
$\square$

**Proposition 6.13** (Semicontinuity in the domain).
The map $\mathcal{D} \mapsto \Sigma^*(\mathcal{H}_0, \mathcal{D})$ is
monotone in the inclusion order: if $\mathcal{D}_1 \subseteq \mathcal{D}_2$,
then $\mathcal{P}(\mathcal{H}_0, \mathcal{D}_1) \subseteq
\mathcal{P}(\mathcal{H}_0, \mathcal{D}_2)$ (Proposition 4.7), and this
propagates to all downstream components.

**Proposition 6.14** (Factorization through $\mathcal{P}$).
The Skyline factors through the master region: defining
$\mathrm{Sky}(\mathcal{P}) = (R_{\mathrm{LV}}, R_{\mathrm{ZLV}}, A, A^*,
\theta)$ as the tuple of components determined by $\mathcal{P}$ alone
(Theorem 4.9), the full Skyline satisfies

$$
\Sigma^*
= \bigl(\mathcal{C}_{\mathrm{EP}}^*,\; \beta^{**},\;
\mathcal{C}_\mu^*,\;
\mathrm{Sky}(\mathcal{P}^*)\bigr)
$$

where the first three components are upstream objects that *generate*
$\mathcal{P}^*$ and the last five are *derived from* $\mathcal{P}^*$.  The
master region $\mathcal{P}^*$ is the bottleneck through which all upstream
information passes to produce downstream bounds.


### 6.9 The Skyline as a Geometric Object

We conclude by describing the Skyline itself as a geometric entity.

The Skyline $\Sigma^*$ is a heterogeneous geometric object — a tuple of
shapes of different dimensions living in different ambient spaces.  It can
be visualized as a *stratified boundary*:

- **Stratum 5**: The boundary $\partial\mathcal{P}^*$ of the master region
  in $\mathbb{R}^5$.  This is a four-dimensional polyhedral complex.

- **Stratum 3**: The boundaries $\partial R_{\mathrm{LV}}$ and
  $\partial R_{\mathrm{energy}}$ in $\mathbb{R}^3$.  These are
  two-dimensional polyhedral complexes, obtained as the boundaries of the
  shadows of $\mathcal{P}^*$.

- **Stratum 2**: The hull boundaries $\partial\mathcal{C}_{\mathrm{EP}}$
  and $\partial\mathcal{C}_\mu$ in $\mathbb{R}^2$.  These are
  one-dimensional piecewise-linear curves (convex polygon boundaries).

- **Stratum 1**: The graph curves $A(\sigma)$, $A^*(\sigma)$, and
  $\beta^*(\alpha)$ in $\mathbb{R}^2$ (as graphs of 1D functions).  These
  are one-dimensional piecewise-rational (or piecewise-affine) curves.

- **Stratum 0**: The scalar $\theta \in \mathbb{R}$.

The strata are connected by the projection and envelope maps described in
Section 5.  Information flows strictly from higher strata to lower strata
(Remark 5.1).  The Skyline is, in this sense, a *filtered geometric object*:
a sequence of boundaries of decreasing dimension, each derived from the one
above, terminating in a point.

The name "Skyline" is motivated by this picture: viewed from the
$\sigma$-axis, the successive boundaries form a descending profile — the
silhouette of the master polytope as seen through a hierarchy of projections.

## 7. Consequences

This section develops the structural consequences of the Skyline framework
established in Sections 4–6.  We examine the dimension ladder, the duality
web, the flow structure, and the fixed-point hierarchy — four perspectives
on a single geometric object.


### 7.1 The Dimension Ladder

The EXPDB pipeline produces objects in five distinct ambient dimensions.
The Skyline framework organizes these into a strictly ordered chain, which
we call the *dimension ladder*.

**Definition 7.1** (Dimension ladder).
The dimension ladder is the sequence of ambient spaces

$$
\mathbb{R}^0
\;\longleftarrow\;
\mathbb{R}^1
\;\longleftarrow\;
\mathbb{R}^2
\;\longleftarrow\;
\mathbb{R}^3
\;\longleftarrow\;
\mathbb{R}^5
$$

together with the maps between them:

| Source | Target | Map | Implementation |
|--------|--------|-----|---------------|
| $\mathbb{R}^5$ | $\mathbb{R}^3$ | Projection $\pi_S$ (Section 5.2–5.4) | `Region.project` |
| $\mathbb{R}^3$ | $\mathbb{R}^1$ | Rational supremum $\Phi_{\rho/\tau}$ (Section 5.5) | `compute_sup_rho_on_tau` |
| $\mathbb{R}^1$ | $\mathbb{R}^1$ | Lower envelope $\mathrm{env}^-$ (Section 5.6.5) | `RationalFunction.min` |
| $\mathbb{R}^1$ | $\mathbb{R}^0$ | Supremum $\sup_\sigma$ (Section 5.9) | `compute_gap2` |

and the ascending maps:

| Source | Target | Map | Implementation |
|--------|--------|-----|---------------|
| $\mathbb{R}^2$ | $\mathbb{R}^5$ | Constraint generation (Section 4.3.4) | `ep_to_lver` |
| $\mathbb{R}^1$ | $\mathbb{R}^3$ | Zero-set embedding (Section 4.3.3) | `beta_to_zlv`, `mu_to_zlv` |
| $\mathbb{R}^3$ | $\mathbb{R}^5$ | Lifting (Section 4.3.2) | `lv_to_lver` |

Note that $\mathbb{R}^4$ is absent.  The coordinate $s$ always appears
jointly with $(\sigma, \tau, \rho, \rho^*)$; there is no four-dimensional
stage in the pipeline.

**Proposition 7.2** (Strict information loss).
Each descending map in the ladder is strictly lossy: the target object does
not determine the source.  Specifically:

(a) $\pi_{\{0,1,2\}}(\mathcal{P})$ does not determine $\mathcal{P}$
    (Remark 5.1).

(b) $\Phi_{\rho/\tau}(R_{\mathrm{LV}})$ does not determine $R_{\mathrm{LV}}$
    (Remark 5.2).

(c) $\sup_\sigma A(\sigma)$ does not determine $A(\sigma)$.

Each ascending map, by contrast, is information-preserving in a weak sense:
the constraints generated by a 2D object (e.g., an EP point) are fully
determined by that object, so no information is lost in the *generation*
step.  However, the constraints are only a subset of those defining
$\mathcal{P}$, so the ascending map does not determine $\mathcal{P}$ either.

**Corollary 7.3** (Improvement propagation).
Improvements at higher levels of the ladder propagate downward
automatically (by monotonicity, Theorem 6.4).  Improvements at lower levels
do not propagate upward.  Consequently:

- A new literature LVER result (adding a half-space to $\mathcal{P}$ in
  $\mathbb{R}^5$) improves all downstream objects: LV region, ZD estimate,
  ZDE estimate, and $\theta$.
- A new literature ZD result (adding a rational curve to the 1D envelope)
  improves $A(\sigma)$ and $\theta$ but has no effect on $\mathcal{P}$,
  $R_{\mathrm{LV}}$, or $A^*(\sigma)$.
- A new literature EP (adding a point to the 2D hull) can improve
  $\mathcal{P}$ (via `ep_to_lver`) and all downstream objects, but only
  through the constraint-generation mechanism — not through any direct
  projection from $\mathbb{R}^2$ to $\mathbb{R}^5$.


### 7.2 The Duality Web

Three dualities organize the Skyline.  Each exchanges a "primal" object
with a "dual" object of the same or different type.

#### 7.2.1 EP $\leftrightarrow$ Beta: Point-Line Duality

This is the oldest and most complete duality in the system.

**The forward map (EP $\to$ Beta).**  Each point $(k_i, l_i)$ on the EP hull
defines the affine function $\beta_i(\alpha) = (l_i - k_i)\alpha + k_i$.
The beta envelope $\beta^* = \min_i \beta_i$ is the lower envelope of this
family of lines.

**The backward map (Beta $\to$ EP).**  Each edge of the beta envelope — an
affine piece with slope $m$ and intercept $c$ on a maximal interval — defines
the EP point $(c, m + c)$.  This is the tangent-line extraction from the
convex hull of the epigraph $\{(\alpha, \beta) : \beta \ge \beta^*(\alpha)\}$.

**Exactness.**  The forward and backward maps are mutually inverse on the
level of combinatorial data: hull vertices biject with envelope pieces, and
hull edges biject with envelope breakpoints.  This is an instance of
Legendre–Fenchel duality for polyhedral convex functions restricted to
$\mathbb{Q}$.

**Algebraic structure.**  The duality is *involutory* on the combinatorial
level but *non-involutory* on the set level: the round-trip
$\mathrm{EP} \to \mathrm{Beta} \to \mathrm{EP}$ can produce *new* EP
points (from hull edges of the beta epigraph that were not present as
original EP hull vertices).  This is the source of the EP $\leftrightarrow$
Beta feedback loop (Section 7.3).

#### 7.2.2 LV $\leftrightarrow$ LVER: Section-Projection Adjunction

The relationship between the LV region and the LVER is an instance of the
general adjunction between lifting and projection (Section 2.2).

**Lifting** (LV $\to$ LVER): $\mathrm{lift}(R_{\mathrm{LV}}) =
R_{\mathrm{LV}} \times [0, M]^2$.

**Projection** (LVER $\to$ LV): $\pi_{\{0,1,2\}}(\mathcal{P})$.

The key identity is: for any region $Q \subset \mathbb{R}^5$,
$$
\pi_{\{0,1,2\}}(Q) \subseteq R
\quad\Longleftrightarrow\quad
Q \subseteq \mathrm{lift}(R)
\quad\text{(when the lift bounds are sufficiently large).}
$$

This is the defining property of an adjunction: lifting is right adjoint to
projection.  The consequence is that
$\pi_{\{0,1,2\}}(\mathrm{lift}(R)) \supseteq R$ (projecting a lift only
expands), while $\mathrm{lift}(\pi_{\{0,1,2\}}(\mathcal{P})) \supseteq
\mathcal{P}$ (lifting a projection loses cross-coordinate constraints).

The *adjunction gap* — the difference between $\mathcal{P}$ and
$\mathrm{lift}(\pi_{\{0,1,2\}}(\mathcal{P}))$ — measures the information
content of the direct LVER constraints (Section 4.3.1) and the EP-derived
LVER constraints (Section 4.3.4), which couple $\rho$ and $\rho^*$ through
$s$.  When these constraints are trivial, the gap vanishes and the 3D
pipeline (Routes 1–2 of Section 5.6) is as powerful as the 5D pipeline
(Route 3).

#### 7.2.3 EP $\leftrightarrow$ Mu: Linear Isomorphism

The EP hull and the mu hull are related by the invertible linear map
$L: (k, l) \mapsto (l - k, k)$, with inverse $L^{-1}: (\sigma, \mu)
\mapsto (\mu, \sigma + \mu)$.  This is not a duality in the projective
sense but a simple coordinate change.  The lower boundary of $\mathcal{C}_\mu$
is the image under $L$ of the lower-left boundary of $\mathcal{C}_{\mathrm{EP}}$.

The functional equation $(\sigma, \mu) \mapsto (1 - \sigma, \mu + \sigma -
\frac{1}{2})$ is an affine involution of the mu hull that has no analogue in
the EP hull (it does not lift to a rational transformation on $(k, l)$).
This breaks the symmetry between the two 2D stages: the mu hull can be
strictly tighter than the linear image of the EP hull because it receives
additional points from the functional equation.

#### 7.2.4 Dual projections of $\mathcal{P}$

The two principal 3D projections of $\mathcal{P}$ —
$\pi_{\{0,1,2\}}(\mathcal{P})$ (LV) and $\pi_{\{0,1,3\}}(\mathcal{P})$
(energy) — are "dual" in the sense that they capture complementary marginals
of the same 5D body:

$$
\text{LV} = \text{``}\rho\text{-shadow''}, \qquad
\text{energy} = \text{``}\rho^*\text{-shadow''}.
$$

Both share the $(\sigma, \tau)$ subspace.  The $s$-coordinate, eliminated in
both projections, is the hidden variable that couples them.  The pair
(LV, energy) is analogous to a pair of marginal distributions of a joint
distribution: each marginal constrains the joint, but the joint contains
strictly more information than both marginals combined (Remark 5.1).


### 7.3 Flow Structure

The EXPDB pipeline contains two feedback loops.  We describe their geometry.

#### 7.3.1 The EP $\leftrightarrow$ Beta loop

This is the only genuinely iterative loop in the pipeline.  Its geometry is:

$$
\mathcal{C}_{\mathrm{EP}}
\;\xrightarrow{\;\text{tangent lines}\;}\;
\beta^*
\;\xrightarrow{\;\text{hull edges}\;}\;
\mathcal{C}_{\mathrm{EP}}'
\;\xrightarrow{\;\text{A,B,C transforms}\;}\;
\mathcal{C}_{\mathrm{EP}}''
\;\xrightarrow{\;\text{tangent lines}\;}\;
\cdots
$$

**State space.**  Convex polygons in $\mathbb{R}^2$ (the EP hull), ordered by
inclusion.

**Update rule.**  At each iteration: (1) convert hull vertices to tangent
lines, forming the beta envelope; (2) extract the hull edges of the beta
epigraph as new EP points; (3) apply A, B, C transforms to all hull
vertices; (4) recompute the convex hull.

**Monotonicity.**  The hull is non-decreasing: $\mathcal{C}_{\mathrm{EP}}^{(n)}
\subseteq \mathcal{C}_{\mathrm{EP}}^{(n+1)}$.  New points can only enlarge
the hull.

**Convergence mechanism.**  The A-process $(k, l) \mapsto (k/(2k+2),
\frac{1}{2} + l/(2k+2))$ is a contraction toward $(0, \frac{1}{2})$.  Its
Jacobian at a point $(k, l)$ is

$$
J_A(k, l) = \begin{pmatrix}
\frac{\partial}{\partial k}\frac{k}{2k+2} &
\frac{\partial}{\partial l}\frac{k}{2k+2} \\[4pt]
\frac{\partial}{\partial k}\bigl(\frac{1}{2}+\frac{l}{2k+2}\bigr) &
\frac{\partial}{\partial l}\bigl(\frac{1}{2}+\frac{l}{2k+2}\bigr)
\end{pmatrix}
= \begin{pmatrix}
\frac{1}{(k+1)^2} & 0 \\[4pt]
\frac{-l}{(2k+2)^2} & \frac{1}{2k+2}
\end{pmatrix}.
$$

For $k \ge 0$, both diagonal entries have absolute value $\le 1$
(with equality only at $k = 0$), so $A$ is a (weak) contraction in a
neighborhood of the fixed point $(0, \frac{1}{2})$.  The spectral radius of
$J_A$ at the fixed point is $1$ (the contraction is not strict at the fixed
point itself), but iterated application drives any initial point toward the
fixed point because the orbit $A^n(k, l)$ satisfies
$k_n = k / \prod_{i=0}^{n-1}(2k_i + 2) \to 0$.

The B-process is an involution: $B^2 = \mathrm{id}$.  It does not contract
but *reflects* the hull, generating new vertices on the opposite side of the
line $l = k + \frac{1}{2}$.

The interaction of A (contraction) and B (reflection) produces a dense orbit
on the lower-left boundary of the hull, progressively filling in the curve
that interpolates between the known EP points.  After finitely many
iterations (bounded by `search_depth`), the set of hull vertices stabilizes
up to the resolution imposed by the rational arithmetic.

#### 7.3.2 The LVER $\to$ LV $\to$ LVER loop

This loop is present in the pipeline architecture but is executed as a
single pass in the current codebase:

$$
\mathrm{LV}
\;\xrightarrow{\;\text{lift}\;}\;
\mathrm{LVER}_{\mathrm{lifted}}
\;\xrightarrow{\;\text{intersect with direct LVER}\;}\;
\mathcal{P}
\;\xrightarrow{\;\pi_{\{0,1,2\}}\;}\;
\mathrm{LV}'
$$

The output $\mathrm{LV}'$ is at least as tight as the input $\mathrm{LV}$
(because $\mathcal{P}$ includes all LV constraints plus additional
constraints from direct LVER and EP-derived LVER).  In principle, iterating
this loop could yield progressively tighter LV regions:

$$
\mathrm{LV}
\;\to\; \mathrm{LV}'
\;\to\; \mathrm{LV}''
\;\to\; \cdots
$$

In practice, the loop stabilizes after a single pass because the projection
$\pi_{\{0,1,2\}}(\mathcal{P})$ already incorporates all available LVER
constraints.  Iterating would only re-derive the same LV region (the
intersection is idempotent, and the projection of the intersection equals
the intersection of the projections when all constraints are included).


### 7.4 Fixed Points and Attractors

The Skyline $\Sigma^*$ is the fixed point of the pipeline operator $\Phi$
(Theorem 6.6).  We now describe the fixed-point structure at each level of
the dimension ladder.

#### 7.4.1 EP fixed points

The A, B, C transforms on $\mathbb{R}^2$ have the following fixed-point
structure:

| Transform | Fixed points | Nature |
|-----------|-------------|--------|
| $A$: $(k,l) \mapsto (k/(2k+2), 1/2 + l/(2k+2))$ | $(0, 1/2)$ | Global attractor (weakly contracting) |
| $B$: $(k,l) \mapsto (l - 1/2, k + 1/2)$ | Line $\{l = k + 1/2\}$ | Period-2 orbits off the fixed line |
| $C$: $(k,l) \mapsto (k/(12+48k), (11+44k+l)/(12+48k))$ | $(0, 11/12)$ | Global attractor |

The *semigroup* generated by $\{A, B, C\}$ has a unique global attractor:
the point $(0, 1/2)$.  This is because:
- $A$ maps every point closer to $(0, 1/2)$ (strictly, except at the fixed
  point).
- $B(0, 1/2) = (0, 1/2)$ (the attractor is a fixed point of $B$).
- $C$ maps every point closer to $(0, 11/12)$, and
  $A(0, 11/12) = (0, 1/2 + 11/24) = (0, 23/24)$, which is closer to
  $(0, 1/2)$ than $(0, 11/12)$ is.

In the limit, the EP hull would collapse to the single point $(0, 1/2)$.
In practice, the hull has finitely many vertices and the attractor is
approached but never reached.

#### 7.4.2 Beta fixed point

The beta envelope $\beta^*(\alpha)$ descends toward $\beta(\alpha) =
\alpha/2$, the affine function corresponding to the EP attractor
$(0, 1/2)$ via the duality $\beta = (l - k)\alpha + k = (1/2)\alpha$.

#### 7.4.3 Mu fixed point

The lower boundary of the mu hull descends toward $\mu(\sigma) = 0$ for
$\sigma \ge 1/2$, the image of the EP attractor under the linear map
$(k, l) \mapsto (l - k, k) = (1/2, 0)$.

#### 7.4.4 The conjectural fixed point of $\mathcal{P}$

The master region $\mathcal{P}$ is contracting (Theorem 6.5): each new
constraint shrinks it.  The *conjectural limiting region*
$\mathcal{P}_\infty$ is the intersection of $\mathcal{B}$ with the "true"
set of constraints — i.e., those that hold for all values of the parameters,
not merely those known from the literature.  The relationship between
$\mathcal{P}^*$ (the Skyline fixed point) and $\mathcal{P}_\infty$ is:

$$
\mathcal{P}_\infty
\;\subseteq\;
\mathcal{P}^*
\;\subseteq\;
\mathcal{B}
$$

The gap $\mathcal{P}^* \setminus \mathcal{P}_\infty$ represents the
constraints that are true but not yet derivable from the current
literature using the current transformation set.

#### 7.4.5 The scalar attractor

The prime gap bound $\theta$ is a monotonically non-increasing function of
the Skyline state (Theorem 6.5).  The conjectural limiting value
$\theta_\infty$ is determined by $\mathcal{P}_\infty$ via the chain of
projections, suprema, and envelopes.  The current best $\theta^*$ satisfies
$\theta^* \ge \theta_\infty$, with the gap determined by the quality of the
current literature constraints.

#### 7.4.6 The fixed-point hierarchy

The fixed points at each level form a hierarchy:

$$
\begin{aligned}
&\text{EP attractor } (0, 1/2) \\
&\qquad\Downarrow \text{ (tangent line duality)} \\
&\text{Beta attractor } \beta(\alpha) = \alpha/2 \\
&\qquad\Downarrow \text{ (zero-set embedding)} \\
&\text{ZLV attractor: } \rho = 0 \text{ for } \sigma \ge \tau \cdot (\alpha/2) \\
&\qquad\Downarrow \text{ (lifting)} \\
&\text{$\mathcal{P}$ attractor: } \mathcal{P}_\infty \\
&\qquad\Downarrow \text{ (projection + rational supremum)} \\
&\text{ZD attractor: } A(\sigma) = 0 \text{ for } \sigma > 1/2 \\
&\qquad\Downarrow \text{ (supremum)} \\
&\text{Scalar attractor: } \theta = 0
\end{aligned}
$$

At each level, the attractor is the image of the level-above attractor under
the appropriate descending map.  The conjectured vanishing of $A(\sigma)$ for
$\sigma > 1/2$ (the density hypothesis) and of $\theta$ (the prime gap
exponent) are reflections, in dimension 1 and dimension 0 respectively, of
the EP attractor at dimension 2.


### 7.5 Sensitivity Structure

We conclude by describing how the Skyline responds to perturbations of
the axiom set.

**Definition 7.4** (Marginal value of a hypothesis).
Let $h$ be a hypothesis in $\mathcal{H}_0$.  The *marginal value of $h$
at level $\ell$* is the change in the $\ell$-th Skyline component when $h$
is removed:

$$
\Delta_\ell(h)
= \Sigma^*_\ell(\mathcal{H}_0)
\;\ominus\;
\Sigma^*_\ell(\mathcal{H}_0 \setminus \{h\})
$$

where $\ominus$ denotes the appropriate difference operation at level $\ell$
(set difference for regions, pointwise difference for functions, arithmetic
difference for scalars).

**Proposition 7.5** (Sparsity of dependence).
For a generic hypothesis set, most hypotheses have zero marginal value at
the scalar level: $\Delta_\theta(h) = 0$ for all but finitely many
$h \in \mathcal{H}_0$.

*Proof sketch.*
The scalar $\theta$ depends on $A(\sigma)$ and $A^*(\sigma)$ through the
supremum $\sup_\sigma \max(\alpha, \beta)$.  This supremum is attained at
finitely many critical $\sigma$-values.  At each critical $\sigma$, the ZD
and ZDE bounds are determined by one piece of the respective lower envelopes.
Each such piece traces back (through the rational supremum and projection)
to finitely many polytope edges in $\mathcal{P}$, which in turn depend on
finitely many input half-spaces.  Hence $\theta$ depends on finitely many
hypotheses from $\mathcal{H}_0$, and removing any other hypothesis has no
effect.
$\square$

This sparsity has a practical consequence: the dependency-tracking mechanism
in EXPDB (the `dependencies` attribute and the `track_dependencies` flag in
the distributive-law intersection) identifies precisely which literature
results are load-bearing for the final bound $\theta$.  The Skyline
framework interprets this tracking geometrically: a hypothesis is
load-bearing if and only if it contributes a half-space to $\mathcal{P}$
that is active (i.e., the half-space's bounding hyperplane intersects
$\partial\mathcal{P}^*$) at a point that lies on the projection path from
$\mathcal{P}$ to the critical $\sigma$-value where $\theta$ is attained.

**Remark 7.6** (Redundancy).
The complement of the load-bearing set consists of *redundant* hypotheses:
those whose removal does not change $\theta$.  Identifying redundant
hypotheses is valuable for proof simplification (finding minimal axiom sets)
and for understanding which literature results are truly essential.  The
`proof_complexity` and `proof_depth` metrics on the Hypothesis DAG
(Section 3.1) provide heuristic proxies for this; the Skyline framework
provides the exact geometric criterion.

## 8. Comparison with the Factor Skyline

The Erdős–Tao factorization project [ET] addresses a different problem in
number theory — the factorization of $N!$ into large factors — using a
computational pipeline that bears structural resemblance to EXPDB.  In this
section we compare the two frameworks, identify their common geometric
substrate, and discuss the prospects for unification.  The comparison is
structural, not mathematical: we treat both systems as polyhedral
computation engines and ask how their architectures relate.


### 8.1 The Factor Problem

The Erdős–Tao project studies the following question: given integers $N$ and
$T$, express $N!$ as a product of factors each at least $T$.  The goal is to
maximize the number of such factors (equivalently, to minimize the residual
that cannot be decomposed into factors $\ge T$).  The problem is
parameterized by the ratio $T/N$ and has a rich asymptotic structure as
$N \to \infty$.

The computational approach proceeds as follows:

1. **Sieve.**  Compute the prime factorization of $N!$: for each prime
   $p \le N$, the exponent of $p$ in $N!$ is $\sum_{i \ge 1} \lfloor N/p^i
   \rfloor$.

2. **Smooth decomposition.**  Identify which integers $j \in [T, N]$ are
   *$P$-smooth* (all prime factors $\le P$) for a suitable smoothness bound
   $P$.  Each smooth $j$ has a known prime factorization in terms of small
   primes.

3. **Linear program.**  Construct an LP whose variables $x_j$ represent the
   multiplicity of factor $j$ in the decomposition.  The constraints enforce
   that the total usage of each prime $p$ does not exceed its exponent in
   $N!$:
   $$
   \sum_{j \ge T} f_{j,p}\, x_j \;\le\; c_p
   \qquad\text{for each prime } p \le P
   $$
   where $f_{j,p}$ is the exponent of $p$ in $j$ and $c_p$ is the exponent
   of $p$ in $N!$.  The objective is $\max \sum_j x_j$.

4. **Dual certificate.**  Extract the dual variables $\pi_p$ (one per prime
   constraint) to certify an upper bound on the number of factors.  The dual
   feasibility condition is $\sum_p \pi_p f_{j,p} \ge 1$ for each
   $j \in [T, N]$, and the dual objective is $\sum_p \pi_p c_p$.

5. **Rounding and verification.**  Round the LP solution to integers and
   verify that the resulting factorization is valid.

This pipeline — sieve, LP, dual certificate, rounding — is the Factor
Skyline analogue of EXPDB's pipeline of axiom seeding, constraint
intersection, projection, and envelope extraction.


### 8.2 Structural Parallels

We identify five structural parallels between the two systems.

#### 8.2.1 Polyhedral feasible region

Both systems operate on a polyhedral feasible region defined by rational
half-spaces.

| Feature | EXPDB Skyline | Factor Skyline |
|---------|--------------|----------------|
| Ambient dimension | 5 (fixed: $\sigma, \tau, \rho, \rho^*, s$) | $N - T + 1$ (variable: one dimension per potential factor $j$) |
| Number of constraints | $O(\text{literature results} \times \text{rescalings})$ | $O(\pi(P))$ (one per small prime) |
| Coefficient field | $\mathbb{Q}$ (exact rational arithmetic via `pycddlib`) | $\mathbb{Q}$ (exact rational arithmetic for certificates; floating-point for LP solving via Gurobi) |
| Bounding box | Fixed box $\mathcal{B} \subset \mathbb{R}^5$ | Implicitly bounded by $x_j \le c_p / f_{j,p}$ |

In EXPDB, the polytope is low-dimensional (5D) with many constraints.  In
the Factor Skyline, the polytope is high-dimensional ($N - T + 1$ dimensions)
with few constraints (one per prime $\le P$).  This is a fundamental
geometric difference: EXPDB's master polytope $\mathcal{P}$ has far more
facets than vertices, while the Factor LP polytope has far more vertices
than facets.

#### 8.2.2 Axioms as half-spaces

Both systems begin with a collection of "axioms" that are encoded as
half-space constraints.

| | EXPDB | Factor |
|---|------|--------|
| Axiom source | Published literature results | Prime factorization of $N!$ |
| Axiom form | $a_0 + a_1\sigma + a_2\tau + a_3\rho + a_4\rho^* + a_5 s \ge 0$ | $\sum_j f_{j,p}\, x_j \le c_p$ |
| Axiom count | Tens to low hundreds | $\pi(P)$ (hundreds to thousands) |
| Axiom type | Heterogeneous (different hypothesis types) | Homogeneous (one prime constraint per prime) |

In EXPDB, axioms are heterogeneous and their geometric meaning varies by
type.  In the Factor Skyline, axioms are homogeneous: every constraint has
the same structure (prime budget).

#### 8.2.3 Monotone contraction

Both systems define a monotone operator on their respective feasible
regions.

In EXPDB: adding a new literature result adds a half-space, shrinking
$\mathcal{P}$.  The operator $\Phi$ is a contraction (Theorem 6.5).

In the Factor Skyline: increasing $N$ (with $T$ scaling proportionally) adds
new prime constraints and new factor variables.  The LP value (maximum number
of factors, normalized by $N$) is a monotone function of the constraint
matrix.  The dual certificate provides an upper bound that descends as the
LP is tightened.

#### 8.2.4 Duality

Both systems exhibit a primal-dual structure.

In EXPDB: the EP $\leftrightarrow$ Beta duality (Section 7.2.1) exchanges
points with tangent lines.  The LV $\leftrightarrow$ LVER adjunction
(Section 7.2.2) exchanges projected regions with lifted regions.

In the Factor Skyline: the primal LP (factor multiplicities $x_j$) is dual
to the certificate LP (prime valuations $\pi_p$).  The dual variables $\pi_p$
assign a "cost" to each prime, and the dual feasibility condition
$\sum_p \pi_p f_{j,p} \ge 1$ states that every factor $j \ge T$ has total
prime cost at least 1.  This is a classical LP duality, not a projective
duality, but it serves an analogous role: it provides the certificate that
bounds the objective.

#### 8.2.5 Dimensional reduction to a scalar

Both systems ultimately extract a single scalar from a high-dimensional
polyhedral object.

| | EXPDB | Factor |
|---|------|--------|
| Input dimension | 5 | $N - T + 1$ |
| Output | $\theta$ (prime gap exponent) | $f(N, T) / N$ (factor density) |
| Reduction mechanism | Projection → rational supremum → envelope → scalar supremum | LP objective → dual bound → rounding |
| Intermediate objects | 3D regions, 1D piecewise-rational functions | Dual variables $\pi_p$, reduced costs |


### 8.3 Structural Differences

Despite the parallels, the two systems differ in fundamental geometric ways.

#### 8.3.1 Fixed vs. variable dimension

EXPDB operates in a fixed ambient dimension ($\mathbb{R}^5$) regardless of
the number of literature results.  Adding a new result adds a constraint to
the same 5D space.  The Factor Skyline operates in a dimension that grows
with the problem size ($N - T + 1$).  This makes the Factor LP
fundamentally harder to visualize but amenable to LP solvers that scale with
dimension.

#### 8.3.2 Iterative flow vs. single LP

EXPDB's pipeline is an *iterative flow* with feedback loops (EP
$\leftrightarrow$ Beta) and a multi-stage cascade (Section 7.3).  The
Factor Skyline is a *single-shot LP*: once the constraint matrix is
assembled, the LP solver finds the optimum in one call.  There is no
iterative refinement or feedback.

The greedy algorithm (`greedy.py`) provides an alternative to the LP, but
it is a heuristic primal method, not an iterative flow in the Skyline sense.

#### 8.3.3 Non-convex regions vs. convex polytope

EXPDB's master region $\mathcal{P}$ is a disjoint union of convex polytopes
(Proposition 4.4) — a non-convex region.  The non-convexity arises from the
`from_union_of_halfplanes` construction, which represents sub-level sets of
pointwise maxima of affine functions.  The Factor LP polytope is a single
convex polytope (the intersection of half-spaces defining the LP feasible
region).

#### 8.3.4 Exact projection vs. LP relaxation

EXPDB computes exact projections (via vertex enumeration in `pycddlib`) and
exact envelopes (via algebraic root-finding in `sympy`).  All intermediate
results are exact rational numbers.

The Factor Skyline uses floating-point LP solving (via Gurobi) with
post-hoc rational certificate verification.  The LP solution is
floating-point; the dual variables are rounded to rationals; and a separate
verification step (`verify.py`) checks that the rounded certificate is
valid.  This hybrid exact/approximate approach is necessitated by the high
dimension of the LP.

#### 8.3.5 Proof structure

EXPDB produces machine-readable proofs as dependency DAGs
(Section 3.1).  Each derived hypothesis carries a dependency set, and the
full proof is a tree whose leaves are literature citations.  The system
interfaces with Lean 4 for formal verification.

The Factor Skyline produces dual certificates: a vector $(\pi_p)$ of
rational dual variables that certify an upper bound.  The certificate is
verifiable by a finite check ($\sum_p \pi_p f_{j,p} \ge 1$ for each $j$),
but it is not structured as a dependency tree.  There is no formal
verification interface (though the rational rounding in `facfac.py` provides
a rigorous bound when the dual variables are monotone).


### 8.4 A Common Abstraction

Despite these differences, both systems can be described in a common
abstract framework.

**Definition 8.1** (Skyline system).
A *skyline system* is a tuple $(\mathcal{A}, \mathcal{C}, \mathcal{P},
\pi, \phi)$ where:

- $\mathcal{A}$ is a finite set of *axioms* (literature results or prime
  factorizations).
- $\mathcal{C}: \mathcal{A} \to \{\text{rational half-spaces in }
  \mathbb{R}^d\}$ is a *constraint map* that converts each axiom into one
  or more half-space constraints.
- $\mathcal{P} = \bigcap_{a \in \mathcal{A}} \mathcal{C}(a) \cap
  \mathcal{B}$ is the *master region* (the intersection of all constraints
  within a bounding box $\mathcal{B}$).
- $\pi: \mathbb{R}^d \to \mathbb{R}^k$ ($k < d$) is a *reduction map*
  (projection, rational supremum, or LP objective) that extracts a
  lower-dimensional output from $\mathcal{P}$.
- $\phi: \mathbb{R}^k \to \mathbb{R}$ is a *scalar extraction* (supremum,
  lower envelope, or objective evaluation) that produces the final bound.

The *skyline* is the boundary $\partial\pi(\mathcal{P})$ (or the graph of
$\phi \circ \pi$), and the *skyline invariant* is the scalar
$\phi(\pi(\mathcal{P}))$.

| Component | EXPDB instantiation | Factor instantiation |
|-----------|-------------------|---------------------|
| $\mathcal{A}$ | Literature hypothesis set $\mathcal{H}_0$ | Prime factorization $\{(p, c_p)\}$ |
| $\mathcal{C}$ | Sections 4.3.1–4.3.5 | $\sum_j f_{j,p} x_j \le c_p$ |
| $\mathcal{P}$ | Master region $\mathcal{P} \subset \mathbb{R}^5$ | LP feasible region $\subset \mathbb{R}^{N-T+1}$ |
| $d$ | 5 | $N - T + 1$ |
| $\pi$ | $\pi_{\{0,1,2\}} \circ \Phi_{\rho/\tau} \circ \mathrm{env}^-$ | LP objective $\sum_j x_j$ |
| $\phi$ | $\sup_\sigma \max(\alpha, \beta)$ | Identity (the LP value is the scalar) |
| Skyline | Stratified boundary (Section 6.9) | Upper boundary of LP polytope |

Both systems satisfy the *skyline monotonicity property*: adding an axiom
(a new literature result or a new prime constraint) can only tighten the
master region and hence can only improve the final bound.

Both systems satisfy the *skyline rationality property*: all vertices of
$\mathcal{P}$, and hence all boundary objects in the skyline, are
representable over $\mathbb{Q}$.


### 8.5 Toward Unification

The common abstraction of Section 8.4 suggests several directions for
bringing the two frameworks closer together.

#### 8.5.1 Shared computational infrastructure

Both systems rely on rational polyhedral computation: `pycddlib` in EXPDB,
Gurobi with rational certificate rounding in the Factor Skyline.  A
shared infrastructure layer — providing exact LP solving, projection,
vertex enumeration, and certificate generation over $\mathbb{Q}$ — would
benefit both projects.  The `pycddlib` library, already used in EXPDB,
could in principle replace Gurobi for the Factor LP when the dimension is
small enough, providing exact solutions without the need for
floating-point rounding.

#### 8.5.2 Proof certificates as geometric objects

In EXPDB, the proof of a bound is a dependency DAG rooted at the literature.
In the Factor Skyline, the proof is a dual certificate $(\pi_p)$.  Both can
be understood as *witnesses for the emptiness of the complement*:

- In EXPDB, the proof witnesses that no five-tuple
  $(\sigma, \tau, \rho, \rho^*, s)$ outside $\mathcal{P}$ is consistent with
  the axioms.
- In the Factor Skyline, the dual certificate witnesses that no assignment
  $x_j$ exceeding the LP value is feasible.

A unified proof format would represent both as certificates of infeasibility
for the complement region, expressible as linear combinations of the
defining half-spaces (a Farkas-type certificate).

#### 8.5.3 Iterative refinement for the Factor LP

The Factor Skyline currently solves a single LP.  One could introduce an
iterative structure analogous to EXPDB's feedback loops: solve the LP,
extract dual variables, use them to generate new constraints (e.g.,
Gomory cuts or column generation), and re-solve.  This would make the Factor
pipeline a genuine iterative flow with a convergence theorem analogous to
Theorem 6.6.

#### 8.5.4 Dimensional reduction for EXPDB

Conversely, EXPDB could benefit from LP-based techniques.  The rational
supremum $\Phi_{\rho/\tau}$ (Section 2.6) is equivalent to a parametric
linear-fractional program over the polytope pieces of $\mathcal{P}$.  Modern
LP solvers could potentially compute this more efficiently than the current
vertex-enumeration approach, especially if the number of polytope pieces is
large.

#### 8.5.5 A common formal language

Both systems produce numerical bounds that could in principle be formally
verified.  EXPDB already interfaces with Lean 4; the Factor Skyline produces
rational certificates that are amenable to formal verification.  A common
formalization — expressing both skyline systems in a single proof assistant
framework — would provide a unified foundation for verified computational
number theory.


### 8.6 Summary

The EXPDB Skyline and the Factor Skyline are instantiations of the same
abstract pattern: a polyhedral feasible region defined by rational axioms,
reduced to a scalar bound by a chain of geometric operations, with a
monotonicity guarantee that ensures the bound improves as axioms accumulate.
They differ in dimension (fixed 5D vs. variable high-D), in iteration
structure (multi-stage flow vs. single LP), in convexity (non-convex region
vs. convex polytope), and in proof format (dependency DAG vs. dual
certificate).  The common abstraction (Definition 8.1) provides a framework
for potential unification, and the shared reliance on rational polyhedral
computation suggests practical opportunities for cross-pollination.

## 9. Discussion and Future Directions

We have shown that the EXPDB pipeline operates on a single five-dimensional
polyhedral region $\mathcal{P}$, that all intermediate and final objects are
projections, envelopes, or scalar extractions of $\mathcal{P}$, and that the
pipeline is a monotone contraction converging to a unique fixed point — the
EXPDB Skyline.  In this concluding section we discuss the implications of
this geometric picture, identify concrete opportunities for improvement, and
pose open questions.


### 9.1 Algorithmic Implications

The polyhedral reinterpretation suggests that the tightness of EXPDB bounds
is governed by two factors: the number and quality of half-spaces defining
$\mathcal{P}$, and the efficiency of the geometric operations that extract
downstream bounds.  We address each in turn.

#### 9.1.1 Marginal returns from new literature results

Each new literature result contributes one or more half-spaces to
$\mathcal{P}$.  The marginal improvement in the final scalar $\theta$ depends
on whether the new half-space is *active* — whether it intersects the
boundary $\partial\mathcal{P}^*$ in the region traversed by the projection
path leading to the critical $\sigma$-value where $\theta$ is attained
(Proposition 7.5).

This suggests a *targeting principle*: new literature results are most
valuable when they tighten $\mathcal{P}$ along the specific boundary faces
that participate in the optimal projection path.  The Skyline framework
makes this targeting precise: the dependency-tracking mechanism
(`track_dependencies=True` in the distributive-law intersection) identifies
exactly which input half-spaces are active at the optimum.  A researcher
seeking to improve $\theta$ could examine the active half-spaces, identify
which boundary face of $\mathcal{P}$ is limiting, and direct analytical
effort at that face.

#### 9.1.2 The role of the auxiliary coordinate $s$

The coordinate $s$ (index 4) is eliminated by projection in every output
stage — it never appears in the LV region, the energy region, the ZD
estimate, or the prime gap bound.  Yet $s$ is essential: it couples the
$\rho$-boundary and the $\rho^*$-boundary of $\mathcal{P}$ through the
Heath-Brown relations and other joint constraints (Section 4.7).  Removing
$s$ from the ambient space — working directly in $\mathbb{R}^4$ rather than
$\mathbb{R}^5$ — would lose these coupling constraints and weaken the final
bounds.

This observation generalizes: one could consider adding further auxiliary
coordinates to the ambient space (e.g., a sixth coordinate encoding
additional structural information from a new family of estimates).  Each
additional coordinate increases the ambient dimension and the cost of
polyhedral computations (vertex enumeration, projection), but it also
enables the expression of joint constraints that would be invisible in
lower-dimensional projections.  The present analysis shows that EXPDB's
choice of five coordinates is not an arbitrary design decision but reflects
the current state of available joint constraints in the literature.


### 9.2 Specific Improvements to EXPDB

The codebase contains several features marked as unimplemented (`TODO`,
`NotImplementedError`) that the Skyline framework helps to contextualize.

#### 9.2.1 Huxley subdivision

The function `apply_huxley_subdivision` (`large_values.py`, line 422) is
declared but raises `NotImplementedError`.  In the Skyline framework, Huxley
subdivision is a refinement of the LV region that splits polytope faces
along hyperplanes and re-optimizes.  Geometrically, it introduces new
half-spaces that subdivide $\mathcal{P}$ without adding new literature
axioms — it is a *structural refinement* of the polyhedral decomposition
rather than a *data refinement* from new axioms.

The Skyline framework predicts that Huxley subdivision can improve the ZD
envelope $A(\sigma)$ by introducing finer polytope edges along which the
rational supremum $\Phi_{\rho/\tau}$ is evaluated.  The improvement is
bounded by the width of the current polytope faces in the $\tau$ direction:
a face that spans a wide $\tau$-interval may contain an edge with high
$\rho/\tau$ that could be reduced by subdivision.

#### 9.2.2 Automated $\tau_0$ selection

The splitting parameter $\tau_0$ — which divides the $\tau$ domain between
the LV range $[\tau_0, 2\tau_0]$ and the ZLV range $[2, \tau_0]$ in the ZD
derivation (Section 5.6) — is currently chosen manually for each
`prove_zero_density` call.  Different choices yield different polytope
decompositions and hence different ZD estimates, all of which enter the
lower envelope.

In the Skyline framework, $\tau_0$ parameterizes a family of polytope slices
of $\mathcal{P}$.  The optimal $\tau_0(\sigma)$ is the one that minimizes
$\Phi_{\rho/\tau}$ at each $\sigma$ — i.e., the choice that places the
$\tau$-domain boundary at the point where the supremum $\rho/\tau$ is
minimized.  This is a parametric optimization problem over the polytope
edges of $\mathcal{P}$, and it could in principle be solved exactly by
enumerating the finitely many combinatorial types of optimal $\tau_0$ as
$\sigma$ varies.

More precisely, for each polytope piece $P_j$ of $\mathcal{P}$ and each
edge of $P_j$, the rational supremum $\rho/\tau$ along that edge depends
on the $\tau$-domain (which determines whether the edge contributes to the
LV or ZLV supremum).  The optimal $\tau_0$ is the one that minimizes the
maximum of all contributing edges.  Since there are finitely many edges
and each contributes a rational function of $(\sigma, \tau_0)$, the optimal
$\tau_0(\sigma)$ is piecewise-algebraic and computable.

#### 9.2.3 The B-process for beta bounds

The comment at `bound_beta.py`, line 83 reads: "TODO: create a method to
implement the B-process for beta bounds."  Currently, the van der Corput
B-process is implemented only for exponent pairs (the involution
$(k, l) \mapsto (l - 1/2, k + 1/2)$), not for beta bounds directly.  In the
Skyline framework, the B-process on beta bounds would correspond to a
symmetry of the beta envelope under the change of variables
$\alpha \mapsto 1 - \alpha$, combined with an affine shift.  Implementing
this would add new affine pieces to the beta envelope that are currently
obtained only through the EP $\leftrightarrow$ Beta duality loop.  The
direct implementation would bypass one round of the feedback loop and
potentially accelerate convergence.

#### 9.2.4 Lean proof generation

The comment at `hypotheses.py`, line 42 reads: "TODO: add `Lean proof`
attribute."  The Skyline framework suggests a strategy for Lean proof
generation: since every derived bound factors through $\mathcal{P}$
(Proposition 6.14), a formal proof needs to verify only three types of
steps:

1. That each axiom half-space is a valid consequence of the corresponding
   literature result (a mathematical lemma, verified once per result).
2. That the polyhedral operations (intersection, projection, vertex
   enumeration) are correctly implemented (a computational certificate,
   verifiable by checking the H- and V-representations).
3. That the rational supremum and envelope computations produce the claimed
   piecewise-rational functions (an algebraic identity, verifiable by
   evaluation at finitely many rational test points).

The modular structure of the Skyline — axioms $\to$ half-spaces $\to$
intersection $\to$ projection $\to$ envelope $\to$ scalar — decomposes the
proof obligation into a small number of generic lemmas (valid for any
polyhedral system) and a larger number of instance-specific axiom
verifications.


### 9.3 Connections to Convex Optimization

The polyhedral reinterpretation connects EXPDB to the theory of convex
optimization in several ways.

#### 9.3.1 Parametric linear-fractional programming

The rational supremum $\Phi_{\rho/\tau}$ (Definition 2.12) is the optimal
value of a parametric linear-fractional program: for each fixed $\sigma$,
maximize $\rho/\tau$ subject to $(\sigma, \tau, \rho) \in R_{\mathrm{LV}}$.
Linear-fractional programs can be reduced to linear programs by the
Charnes-Cooper transformation $u = 1/\tau$, $v = \rho/\tau$, yielding
$\max v$ subject to the transformed constraints.  This LP is parameterized
by $\sigma$, and its optimal value as a function of $\sigma$ is
piecewise-rational by the theory of parametric LP.

This connection suggests that the current edge-enumeration approach
(Section 2.6) could be replaced or supplemented by parametric LP solvers,
which would avoid the need to enumerate all edges of the polytope
decomposition.  The parametric LP approach would be particularly advantageous
when the number of polytope pieces is large (since it works directly in the
H-representation without computing V-representations).

#### 9.3.2 Sensitivity analysis

The dual variables of the parametric LP at each $\sigma$-value identify
which constraints of $R_{\mathrm{LV}}$ are active (binding) at the optimum.
These active constraints correspond to the active half-spaces of
$\mathcal{P}$ along the optimal projection path.  Standard LP sensitivity
analysis would quantify the marginal improvement in $\Phi_{\rho/\tau}$
from tightening each constraint — providing a direct measure of the marginal
value of each literature hypothesis (Definition 7.4) without requiring the
full Skyline to be recomputed.

#### 9.3.3 Column generation

In the Factor Skyline (Section 8), the LP has many variables (one per
potential factor) but few constraints (one per prime).  Column generation —
adding variables dynamically based on the current dual solution — is a
natural approach.  In EXPDB, the analogous technique would be *constraint
generation*: dynamically adding half-spaces to $\mathcal{P}$ based on which
regions of the boundary are limiting.  The raise-to-power transform
(Section 4.3.5) is already a form of constraint generation: it creates new
half-spaces (rescaled copies of existing constraints) that tighten
$\mathcal{P}$ at larger $\tau$ values.


### 9.4 Extensions of the Framework

#### 9.4.1 Higher-dimensional master regions

The current master region lives in $\mathbb{R}^5$.  If new families of
estimates are discovered that introduce additional parameters beyond
$(\sigma, \tau, \rho, \rho^*, s)$, the framework extends naturally to
$\mathbb{R}^{5+k}$ by adding coordinates and constraints.  The Skyline
machinery — intersection, projection, rational supremum, envelope — works
in any dimension.  The computational cost of vertex enumeration and
projection grows with dimension, but the structural results (monotonicity,
contractivity, convergence) hold in any ambient dimension.

#### 9.4.2 Multiple scalar outputs

The current pipeline terminates in a single scalar $\theta$.  The framework
could accommodate multiple scalar outputs — e.g., prime gap bounds at
different exponents, or bounds on different number-theoretic quantities —
by defining multiple reduction maps from $\mathcal{P}$.  Each reduction
map would produce its own 1D envelope, and the collection of all such
envelopes would form an *extended Skyline*.

#### 9.4.3 Time-varying Skylines

The literature hypothesis set $\mathcal{H}_0$ grows over time as new results
are published.  The Skyline $\Sigma^*(\mathcal{H}_0)$ is a monotone function
of $\mathcal{H}_0$ (Proposition 6.12): as the literature expands, the
Skyline tightens.  One could define the *Skyline trajectory*
$\{\Sigma^*(t)\}_{t \ge 1920}$ as the Skyline evaluated on the hypothesis
set available at time $t$.  This trajectory is a descending path in the
state lattice $\mathcal{L}$ and provides a quantitative history of progress
in the field — a "computational time series" of analytic number theory.


### 9.5 Open Questions

We conclude with five open questions that the Skyline framework raises.

**Question 1** (Finite determination).
*Is the Skyline fixed point $\Sigma^*$ determined by finitely many
"extremal" literature results?*

By Proposition 7.5, the scalar $\theta$ depends on finitely many hypotheses.
But does this extend to all components of $\Sigma^*$?  Specifically: is
there a finite subset $\mathcal{H}' \subset \mathcal{H}_0$ such that
$\Sigma^*(\mathcal{H}') = \Sigma^*(\mathcal{H}_0)$?  If so, the minimal
such $\mathcal{H}'$ would be the *essential axiom set* — the smallest
collection of literature results that fully determines the current best
bounds.

**Question 2** (Combinatorial complexity).
*What is the combinatorial complexity of $\mathcal{P}$ (number of vertices,
edges, facets) as a function of the number of input hypotheses?*

The H-representation of $\mathcal{P}$ has $O(n)$ constraints where $n$ is
the number of hypotheses (after raise-to-power expansion).  In the worst
case, a polytope in $\mathbb{R}^5$ with $n$ facets can have
$O(n^{\lfloor 5/2 \rfloor}) = O(n^2)$ vertices (by the upper bound theorem
for polytopes).  Does the specific structure of EXPDB constraints yield a
better bound?  The answer would determine the computational complexity of
the Skyline computation.

**Question 3** (Algebraic fixed point).
*Can the EP $\leftrightarrow$ Beta feedback loop be replaced by a single
algebraic computation?*

The iterative loop (Section 7.3.1) converges to a fixed hull
$\mathcal{C}_{\mathrm{EP}}^*$.  In principle, the fixed-point condition
$\Phi_{\mathrm{EP}}(\mathcal{C}_{\mathrm{EP}}^*) =
\mathcal{C}_{\mathrm{EP}}^*$ is a system of algebraic equations (the hull
vertices must be fixed under the A, B, C transforms and the
Beta $\to$ EP duality).  Solving this system directly — rather than
iterating to convergence — would yield the exact fixed hull in one step.
Is this system tractable?  What is its algebraic degree?

**Question 4** (Skyline distance).
*Is there a natural metric on the space of Skylines that quantifies the
distance between the current state $\Sigma^*$ and the conjectural optimum
$\Sigma_\infty$?*

A candidate metric could be defined as the Hausdorff distance between
$\mathcal{P}^*$ and $\mathcal{P}_\infty$ (if the latter were known), or as
the $L^1$ distance between $A^*(\sigma)$ and $A_\infty(\sigma)$ on
$[\frac{1}{2}, 1]$.  Without knowledge of $\Sigma_\infty$, one could
define a *gap metric* based on the difference between the primal bound
(the computed $\theta$) and a conjectured lower bound (if available).

**Question 5** (Universality).
*Is the skyline system abstraction (Definition 8.1) the right level of
generality?*

We have shown that both EXPDB and the Factor Skyline instantiate the
pattern: axioms $\to$ half-spaces $\to$ master region $\to$ reduction $\to$
scalar.  Are there other computational systems in number theory (or beyond)
that fit this pattern?  Candidates include:

- The Polymath projects that use LP or semidefinite relaxations to derive
  bounds (e.g., bounds on gaps between primes, bounds on cap sets).
- Automated theorem provers that search over polyhedral feasible regions
  (e.g., sum-of-squares hierarchies in real algebraic geometry).
- The theory of Newton polytopes in algebraic geometry, where the polytope
  of a polynomial controls its asymptotic behavior.

A positive answer would suggest that the skyline system is a natural
computational primitive for a broad class of mathematical optimization
problems.

## Appendix A. Mapping Code Modules to Geometric Operations

This appendix provides a complete reference mapping from the EXPDB source
code (under `blueprint/src/python/`) to the geometric operations and
objects defined in the paper.  It is intended for readers who wish to
trace every structural claim back to the implementation.

All line numbers refer to the EXPDB repository at commit `af351a3`.


### A.1 Module Inventory

The codebase consists of 24 Python modules totalling 10,696 lines.  We
list each module with its line count, classification (Section 3), and
primary geometric role.

| Module | Lines | Classification | Geometric role |
|--------|------:|---------------|----------------|
| `__init__.py` | 0 | Package marker | — |
| `constants.py` | 42 | Infrastructure (B) | Bounding box parameters (§4.2) |
| `reference.py` | 184 | Infrastructure (B) | Bibliographic metadata |
| `hypotheses.py` | 268 | Infrastructure (B) | Hypothesis and Hypothesis\_Set: the typed assertion and collection classes (§3.1–3.3) |
| `transform.py` | 25 | Infrastructure (B) | Transform wrapper: callable $\mathsf{Hyp} \to \mathsf{Hyp}$ (§3.2) |
| `polynomial.py` | 133 | Geometry (C) | Univariate dense polynomial arithmetic |
| `functions.py` | 1,002 | Geometry (C) | Interval, Affine, Affine2, Piecewise, RationalFunction (§2.4–2.5) |
| `polytope.py` | 835 | Geometry (C) | Polytope: H-rep, V-rep, intersection, projection, lifting, scaling (§2.1–2.2) |
| `region.py` | 470 | Geometry (C) | Region: boolean algebra over polytopes (§2.3) |
| `helpers/str_helper.py` | 35 | Utility (E) | Affine expression formatting |
| `helpers/region_helper.py` | 53 | Utility (E) | Pairwise union simplification for polytope lists |
| `helpers/__init__.py` | 0 | Package marker | — |
| `bound_beta.py` | 341 | Transformation (A) | Beta bounds, VdC-$\beta$ iteration, EP$\to$Beta (§5.8.2, §7.3.1) |
| `bound_mu.py` | 333 | Transformation (A) | Mu bounds, EP$\to$Mu, functional equation, convex hull (§5.8.3) |
| `exponent_pair.py` | 462 | Transformation (A) | EP expansion, convex hull, Beta$\to$EP duality (§5.8.1, §7.2.1) |
| `large_values.py` | 430 | Transformation (A/C) | LV region construction, raise-to-power, Bourgain optimization (§5.2) |
| `zeta_large_values.py` | 228 | Transformation (A) | ZLV construction: LV$\to$ZLV, Beta$\to$ZLV, Mu$\to$ZLV (§5.3) |
| `additive_energy.py` | 500 | Transformation (A/C) | LVER construction, projection, LV* computation (§4.4, §5.2, §5.4) |
| `zero_density_estimate.py` | 863 | Propagation (D) | ZD derivation: rational supremum, LV/ZLV$\to$ZD, LVER$\to$ZD (§5.5–5.6) |
| `zero_density_energy_estimate.py` | 456 | Propagation (D) | ZDE derivation: energy projection, rational supremum (§5.7) |
| `prime_gap.py` | 120 | Propagation (D) | Terminal scalar extraction: $\theta$ computation (§5.9) |
| `literature.py` | 1,439 | Axiom layer (D) | Populates the global hypothesis set from the literature (§3.4) |
| `derived.py` | 1,384 | Orchestration (D) | Pipeline driver: prove\_* routines, prove\_all (§3.7) |
| `examples.py` | 620 | Utility (E) | Demonstration scripts |
| `visualizations.py` | 473 | Utility (E) | Matplotlib plots for all bound types |


### A.2 Geometric Primitives: Code to Definition Mapping

| Paper object | Definition | Code class / function | Module | Line |
|-------------|-----------|----------------------|--------|-----:|
| Rational half-space | Def. 2.1 | Row of `cdd.Matrix` | `polytope.py` | 131 |
| H-polytope | Def. 2.2 | `Polytope.__init__` | `polytope.py` | 110 |
| V-polytope | Def. 2.3 | `Polytope.from_V_rep` | `polytope.py` | 348 |
| Bounding box | Def. 2.4 | `Polytope.rect` | `polytope.py` | 317 |
| Polytope intersection | §2.2 | `Polytope.intersection` | `polytope.py` | 211 |
| Polytope set difference | §2.2 | `Polytope.set_minus` | `polytope.py` | 550 |
| Polytope scaling | §2.2 | `Polytope.scale_all` | `polytope.py` | 480 |
| Polytope projection | §2.2 | `Polytope.project` | `polytope.py` | 745 |
| Polytope lifting | §2.2 | `Polytope.lift` | `polytope.py` | 765 |
| Emptiness test | §2.2 | `Polytope.is_empty` | `polytope.py` | 600 |
| Subset test | §2.2 | `Polytope.is_subset_of` | `polytope.py` | 660 |
| Vertex enumeration | §2.2 | `Polytope.compute_V_rep` | `polytope.py` | 391 |
| Edge enumeration | §2.6 | `Polytope.get_edges` | `polytope.py` | 440 |
| Region (boolean combination) | Def. 2.5 | `Region.__init__` | `region.py` | 35 |
| Region from polytope | §2.3 | `Region.from_polytope` | `region.py` | 94 |
| Region from halfplane union | §2.3 | `Region.from_union_of_halfplanes` | `region.py` | 98 |
| Region intersection | §2.3 | `Region.intersect` | `region.py` | 146 |
| Region union | §2.3 | `Region.union` | `region.py` | 140 |
| Region disjoint union | §2.3 | `Region.disjoint_union` | `region.py` | 143 |
| Disjoint decomposition | §2.3 | `Region.as_disjoint_union` | `region.py` | 294 |
| Region simplification | §2.3 | `Region.simplify` | `region.py` | 462 |
| Region projection | §2.3 | `Region.project` | `region.py` | 261 |
| Region lifting | §2.3 | `Region.lift` | `region.py` | 253 |
| Region scaling | §2.3 | `Region.scale_all` | `region.py` | 240 |
| 1D affine function | Def. 2.6 | `Affine.__init__` | `functions.py` | 134 |
| Multi-dim affine function | Def. 2.7 | `Affine2.__init__` | `functions.py` | 322 |
| Piecewise-affine function | Def. 2.8 | `Piecewise.__init__` | `functions.py` | 445 |
| Lower envelope (1D affine) | §2.4 | `Affine.min_with` | `functions.py` | 310 |
| Upper envelope (1D affine) | §2.4 | `Affine.max_with` | `functions.py` | 318 |
| Min of multi-dim affine | §2.4 | `Affine2.min_with` | `functions.py` | 415 |
| Piecewise min | §2.4 | `Piecewise.min_with` | `functions.py` | 536 |
| Rational function | Def. 2.9 | `RationalFunction.__init__` | `functions.py` | 742 |
| Lower envelope (rational) | §2.5 | `RationalFunction.min` | `functions.py` | 871 |
| Upper envelope (rational) | §2.5 | `RationalFunction.max` | `functions.py` | 883 |
| Optimal selection engine | §2.5 | `RationalFunction._compute_optimal` | `functions.py` | 818 |
| Interval | §2.4 | `Interval.__init__` | `functions.py` | 14 |
| 2D convex hull | Def. 2.14 | `scipy.spatial.ConvexHull` | `exponent_pair.py` | 10 |


### A.3 Master Region Construction: Code to Section Mapping

| Construction step | Paper section | Code function | Module | Line |
|-------------------|-------------|--------------|--------|-----:|
| Bounding box $\mathcal{B}$ | §4.2 | `Large_Value_Energy_Region.default_constraints` | `additive_energy.py` | 51 |
| Direct LVER constraints | §4.3.1 | `add_lver_heath_brown_1979`, etc. | `literature.py` | 903+ |
| Lifted LV constraints | §4.3.2 | `lv_to_lver` | `additive_energy.py` | 243 |
| Beta $\to$ ZLV embedding | §4.3.3 | `beta_to_zlv` | `zeta_large_values.py` | 105 |
| Mu $\to$ ZLV embedding | §4.3.3 | `mu_to_zlv` | `zeta_large_values.py` | 182 |
| EP $\to$ LVER constraints | §4.3.4 | `ep_to_lver` | `additive_energy.py` | 204 |
| Raise-to-power (LVER) | §4.3.5 | `get_raise_to_power_hypothesis` | `additive_energy.py` | 169 |
| Raise-to-power (LV) | §4.3.5 | `raise_to_power_hypothesis` | `large_values.py` | 214 |
| Master region $\mathcal{P}$ | Def. 4.1 | `compute_best_lver` | `additive_energy.py` | 296 |


### A.4 Projections and Envelopes: Code to Section Mapping

| Derived object | Paper section | Code function | Module | Line |
|---------------|-------------|--------------|--------|-----:|
| $R_{\mathrm{LV}} = \pi_{\{0,1,2\}}(\mathcal{P})$ | §5.2 | `lver_to_lv` | `additive_energy.py` | 372 |
| $R_{\mathrm{ZLV}}$ | §5.3 | `lver_to_lv` (zeta branch) | `additive_energy.py` | 372 |
| $R_{\mathrm{energy}} = \pi_{\{0,1,3\}}(\mathcal{P})$ | §5.4 | `lver_to_energy` | `additive_energy.py` | 420 |
| $\mathrm{LV}^* = \pi_{\{0,1,3\}}(\mathcal{P})$ | §5.4 | `compute_LV_star` | `additive_energy.py` | 470 |
| LV region (3D direct) | §5.2 | `compute_large_value_region` | `zero_density_estimate.py` | 148 |
| LV combination | §5.2 | `combine_large_value_estimates` | `large_values.py` | 166 |
| ZLV construction | §5.3 | `compute_large_value_estimate` | `zeta_large_values.py` | 65 |
| Rational supremum $\Phi_{\rho/\tau}$ | §5.5 | `compute_sup_rho_on_tau` | `zero_density_estimate.py` | 242 |
| Rational supremum (energy) | §5.7 | `compute_sup_LV_on_tau` | `zero_density_energy_estimate.py` | 338 |
| ZD via LV/ZLV (method 1) | §5.6.1 | `lv_zlv_to_zd` | `zero_density_estimate.py` | 300 |
| ZD via LV/ZLV (method 2) | §5.6.2 | `lv_zlv_to_zd2` | `zero_density_estimate.py` | 393 |
| ZD via LVER | §5.6.3 | `lver_to_zd` | `zero_density_estimate.py` | 471 |
| ZD via EP (Ivić) | §5.6.4 | `ivic_ep_to_zd` | `zero_density_estimate.py` | 542 |
| ZD via EP (Bourgain) | §5.6.4 | `bourgain_ep_to_zd` | `zero_density_estimate.py` | 629 |
| ZD lower envelope | §5.6.5 | `best_zero_density_estimate` | `zero_density_estimate.py` | 765 |
| ZDE via LVER | §5.7 | `lver_to_energy_bound` | `zero_density_energy_estimate.py` | 251 |
| ZDE lower envelope | §5.7 | `compute_best_energy_bound` | `zero_density_energy_estimate.py` | 403 |
| Prime gap $\theta$ | §5.9 | `compute_gap2` | `prime_gap.py` | 11 |
| Prime exception $\mu_{\mathrm{PNT}}(\theta)$ | §5.9 | `prime_excep` | `prime_gap.py` | 72 |


### A.5 Transformations: Code to Section Mapping

| Transformation | Paper section | Code function | Module | Line |
|---------------|-------------|--------------|--------|-----:|
| A-process (EP $\to$ EP) | §3.5, §7.4.1 | `A_transform_function` | `literature.py` | 507 |
| B-process (EP $\to$ EP) | §3.5, §7.4.1 | `B_transform_function` | `literature.py` | 524 |
| C-process (EP $\to$ EP) | §3.5, §7.4.1 | `C_transform_function` | `literature.py` | 540 |
| D-process (EP $\to$ Beta) | §3.5 | `D_transform_function` | `literature.py` | 557 |
| EP iterative expansion | §7.3.1 | `compute_exp_pairs` | `exponent_pair.py` | 72 |
| EP convex hull | §5.8.1 | `compute_convex_hull` | `exponent_pair.py` | 122 |
| EP $\to$ Beta | §3.5 | `exponent_pairs_to_beta_bounds` | `bound_beta.py` | 98 |
| Beta $\to$ EP (duality) | §7.2.1 | `beta_bounds_to_exponent_pairs` | `exponent_pair.py` | 155 |
| Best beta (lower envelope) | §5.8.2 | `compute_best_beta_bounds` | `bound_beta.py` | 128 |
| VdC-$\beta$ iteration | §7.3.1 | `apply_van_der_corput_process_for_beta` | `bound_beta.py` | 165 |
| EP $\to$ Mu | §5.8.3 | `exponent_pair_to_mu_bound` | `bound_mu.py` | 136 |
| Beta $\to$ Mu | §5.8.3 | `beta_bounds_to_mu_bounds` | `bound_mu.py` | 163 |
| Functional equation (Mu) | §7.2.3 | `apply_functional_equation` | `bound_mu.py` | 113 |
| Mu convexity | §7.2.3 | `apply_mu_convexity` | `bound_mu.py` | 124 |
| Mu convex hull | §5.8.3 | `compute_convex_hull` | `bound_mu.py` | 220 |
| Best mu bound | §5.8.3 | `best_mu_bound` | `bound_mu.py` | 229 |
| LV $\to$ ZLV | §5.3 | `lv_to_zlv` | `zeta_large_values.py` | 82 |
| Beta $\to$ ZLV | §4.3.3 | `beta_to_zlv` | `zeta_large_values.py` | 105 |
| Mu $\to$ ZLV | §4.3.3 | `mu_to_zlv` | `zeta_large_values.py` | 182 |
| Bourgain LV optimization | §3.5 | `optimize_bourgain_large_value_estimate` | `large_values.py` | 237 |
| Huxley subdivision (stub) | §9.2.1 | `apply_huxley_subdivision` | `large_values.py` | 422 |


### A.6 Orchestration: Code to Section Mapping

| Pipeline stage | Paper section | Code function | Module | Line |
|---------------|-------------|--------------|--------|-----:|
| Axiom loading | §3.4 | Module-level code | `literature.py` | 1–1439 |
| Top-level driver | §3.7 | `prove_all` | `derived.py` | 1377 |
| EP proof stage | §3.7 | `prove_exponent_pairs` | `derived.py` | 210 |
| Mu bound computation | §3.7 | `compute_best_mu_bound` | `derived.py` | 229 |
| LV proof stage | §3.7 | `prove_all_large_value_estimates` | `derived.py` | 455 |
| ZD proof stage | §3.7 | `prove_all_zero_density_estimates` | `derived.py` | 845 |
| ZDE proof stage | §3.7 | `prove_all_zero_density_energy_estimates` | `derived.py` | 1299 |
| ZD individual proof | §5.6 | `prove_zero_density` | `derived.py` | 464 |
| ZDE individual proof | §5.7 | `prove_heath_brown_energy_estimate`, etc. | `derived.py` | 871+ |
| Prime gap computation | §5.9 | `prove_prime_gap2` | `derived.py` | 1317 |
| Best ZD selection | §5.6.5 | `compute_best_zero_density` | `derived.py` | 828 |


### A.7 Skyline Components: Code to Definition Mapping

| Skyline component | Definition | Construction code | Selection code |
|-------------------|-----------|-------------------|---------------|
| $\mathcal{C}_{\mathrm{EP}}$ | Def. 6.1 | `compute_exp_pairs` (exponent\_pair.py:72) | `compute_convex_hull` (exponent\_pair.py:122) |
| $\beta^*$ | Def. 6.1 | `exponent_pairs_to_beta_bounds` (bound\_beta.py:98) | `compute_best_beta_bounds` (bound\_beta.py:128) |
| $\mathcal{C}_\mu$ | Def. 6.1 | `get_bounds` (bound\_mu.py:200) | `compute_convex_hull` (bound\_mu.py:220) |
| $R_{\mathrm{LV}}$ | Def. 6.1 | `compute_large_value_region` (zero\_density\_estimate.py:148) | `Region.intersect` + `as_disjoint_union` |
| $R_{\mathrm{ZLV}}$ | Def. 6.1 | `compute_large_value_estimate` (zeta\_large\_values.py:65) | `Region.intersect` + `as_disjoint_union` |
| $\mathcal{P}$ | Def. 4.1 | `compute_best_lver` (additive\_energy.py:296) | `Region.intersect` + `as_disjoint_union` |
| $A(\sigma)$ | Def. 6.1 | `lv_zlv_to_zd` / `lver_to_zd` (zero\_density\_estimate.py:300/471) | `best_zero_density_estimate` (zero\_density\_estimate.py:765) |
| $A^*(\sigma)$ | Def. 6.1 | `lver_to_energy_bound` (zero\_density\_energy\_estimate.py:251) | `compute_best_energy_bound` (zero\_density\_energy\_estimate.py:403) |
| $\theta$ | Def. 6.1 | `compute_gap2` (prime\_gap.py:11) | — (single computation) |


### A.8 Constants and Parameters

| Constant | Value | Paper reference | Code location |
|----------|-------|----------------|--------------|
| `TAU_UPPER_LIMIT` | $10^6$ | §4.2 ($T$ in $\mathcal{B}$) | `constants.py:22` |
| `LV_DEFAULT_UPPER_BOUND` | $10^6$ | §4.2 ($M$ in $\mathcal{B}$) | `constants.py:25` |
| `EXP_PAIR_TRUNCATION` | 20 | §6.6 (EP loop bound) | `constants.py:10` |
| `BETA_TRUNCATION` | 20 | §6.6 (Beta loop bound) | `constants.py:7` |
| `LARGE_VALUES_TRUNCATION` | 20 | §3.8 | `constants.py:13` |
| `ALPHA_UPPER_LIMIT` | 100 | §3.8 | `constants.py:16` |
| `ZERO_DENSITY_SIGMA_LIMIT` | 0.999 | §5.7 (pole avoidance) | `constants.py:29` |
| `search_depth` (default) | 5 | §7.3.1 (EP iteration depth) | `exponent_pair.py:73` |
| `SIMPLIFY_EVERY` | 20 | §2.3 (intersection heuristic) | `region.py:360` |
| `UNION_THRESHOLD` | 5 | §2.3 (intersection heuristic) | `region.py:361` |


### References 

- [TTY25] T. Tao, T. Trudgian, A. Yang, "New exponent pairs, zero density
  estimates, and zero additive energy estimates: a systematic approach,"
  arXiv:2501.16779, 2025.

- [ET] (Factor Skyline reference — to be completed.)

- [F] K. Fukuda, `cddlib` / `pycddlib`: An implementation of the double
  description method for polyhedral computation.

- [MSP+17] A. Meurer et al., "SymPy: Symbolic computing in Python,"
  PeerJ Computer Science 3:e103, 2017.

- [MRTT53] T. S. Motzkin, H. Raiffa, G. L. Thompson, R. M. Thrall,
  "The double description method," in *Contributions to the Theory of Games*,
  vol. II, Annals of Mathematics Studies 28, Princeton, 1953, pp. 51–73.

- [BCBM01] A. Bemporad, K. Fukuda, F. D. Torrisi, "Convexity recognition
  of the union of polyhedra," *Computational Geometry* 18(3), 2001,
  pp. 141–154.

- [BDH96] C. B. Barber, D. P. Dobkin, H. Huhdanpaa, "The Quickhull
  algorithm for convex hulls," *ACM Transactions on Mathematical Software*
  22(4), 1996, pp. 469–483.

