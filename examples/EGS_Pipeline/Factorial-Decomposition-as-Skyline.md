# The Factorial-Decomposition Pipeline as Factor Skyline Geometry

## I. The Skyline as a Geometric Object

Place the integers `1, …, N` along a horizontal axis. Each integer `n` becomes a **column** with:

- **Width** `w(n) = lpf(n)` — the least prime factor of `n`
- **Height** `h(n) = n / lpf(n)` — the cofactor after removing one copy of that smallest prime

The product `w(n) · h(n) = n` is the area of the column. The full skyline is the silhouette formed by these `N` columns. It is not a smooth curve — it is jagged, with columns of width 2 dominating (half of all integers), columns of width 3 appearing among the odd multiples of 3, and increasingly rare wide columns for large primes `p = lpf(n) = n` (the primes themselves, which are columns of width `n` and height 1).

The **total area** under the skyline is `Σ n = N(N+1)/2`, but the *multiplicative* content is `N! = Π n`. The skyline encodes both the additive and multiplicative structure simultaneously: the horizontal axis stratifies by smallest prime factor, and the vertical axis records the cofactor residue.

---

## II. The Horizon Line: Smooth vs. Non-Smooth

Draw a vertical line at width `√T` (where `T = ⌈N/3⌉`). This is the **smoothness horizon**.

**Left of the horizon** (`w(n) < √T`): Columns rooted in small primes. These integers *may* be √T-smooth (all prime factors ≤ √T) or may contain a hidden large prime deeper in their factorization. The smooth ones are the battleground — they compete for the shared small-prime budget and are the subject of the LP in `smoothfac.py`.

**Right of the horizon** (`w(n) ≥ √T`): Columns rooted in large primes. Every such integer `n = p · h` has `p ≥ √T` and `h = n/p`. Since `p ≥ √T`, the cofactor needed to bring `p` up to threshold `T` is at most `⌈T/p⌉ ≤ √T`. These are **self-completing towers**: each one can be paired with a tiny smooth cofactor to form a valid factor ≥ `T`. This is exactly what `smoothfac.py` does in lines 80–93 — it greedily assigns every copy of large prime `p` to the factor `p · ⌈T/p⌉`, then deflates the small-prime budget accordingly.

The horizon line is the geometric expression of the computational insight: **tall narrow towers (large-prime columns) are trivially paired; the optimization lives entirely in the low wide mass left of the horizon.**

---

## III. Prime Budgets as Layer Areas

Slice the skyline horizontally by prime. The **p-layer** consists of all prime-p content across all columns: every integer `n` divisible by `p` contributes `v_p(n)` units of mass to the p-layer. The total mass of the p-layer is `v_p(N!) = Σ_{k≥1} ⌊N/p^k⌋`.

In `verify.py`, the `budget[p]` variable accumulates exactly this: the DOWN phase sieves through primes in order, and each extraction `budget[p] += (1/t) · fraction[t] / p` is harvesting one unit of p-layer area from the density of list `L_t`.

In `facfac.py`, the constraint `Σ_j f[j][p] · x[j] ≤ c[p]` says: the total p-layer area consumed by chosen factors must not exceed the p-layer's total mass. The LP constraint matrix is the **skyline's prime-layer decomposition** — each column `j ≥ T` of the LP corresponds to a skyline column, and each row `p` corresponds to a horizontal layer.

The skyline's area is thus **doubly stratified**: vertically by column identity `n`, and horizontally by prime layer `p`. The budget constraints are that no horizontal layer is over-drawn.

---

## IV. The N/3 Threshold as a Height Target

Draw a horizontal line at height `N/3` across the skyline. This is the **target horizon**.

- Columns with `n ≥ N/3` (i.e., `h(n) · w(n) ≥ N/3`) are already **above the target**. They need multiplier 1. In the permutation `σ`, these elements can be mapped to themselves or to nearby values.
- Columns with `n < N/3` are **below the target**. Element `n` needs a multiplier `m ≥ ⌈(N/3)/n⌉` to lift it above the line.

The REORGANIZE phase in `verify.py` (lines 77–156) is precisely the sorting of below-target columns by their **deficit** — how far below `N/3` they sit. The variable `multiple = (k//3) + 1` computes the minimum integer multiplier needed. The sub-lists `S_1, S_2, …, S_{K_{up}}` are **horizontal bands** of the skyline, sliced by how much lifting each band requires.

The `total[k]` values are the **mass in each band**: how much of `(0, N]` sits at deficit level `k`. The CDF `total_cdf[k]` is the cumulative mass from the top of the skyline downward — the integrated skyline profile from height `N/3` downward.

---

## V. LP Dual Variables as the Cost Landscape

The LP in `facfac.py` has a dual: assign a **price** `a[p]` to each prime layer such that every valid factor `j ≥ T` has total prime-price ≥ 1:

```
Σ_p v_p(j) · a[p] ≥ 1   for all j ∈ [T, N]
```

and the total cost `Σ_p a[p] · v_p(N!)` is minimized (equaling the max factor count).

In the skyline, this defines a **cost landscape**: each prime layer `p` has a height `a[p]`, and the "cost" of using a skyline column `j` is the sum of layer-heights it passes through. The dual constraint says every column tall enough (≥ T) must pass through at least unit cost worth of layers.

The monotonicity condition (`a[p] ≤ a[q]` for `p < q`), enforced by the `z` variables in `facfac.py`'s rigorous mode, means the cost landscape is **non-decreasing in prime index** — smaller primes are cheaper per unit. This is geometrically natural: prime 2 is abundant (the 2-layer is thick), so its per-unit price is low. Large primes are scarce, so their per-unit price is high.

The dual cost landscape is the **shadow price surface** draped over the skyline: it tells you, at each horizontal layer, how expensive it is to consume one unit of that layer's area. The optimal factor count equals the total cost of the entire skyline under this surface.

---

## VI. The DOWN Phase as Skyline Erosion

The DOWN phase in `verify.py` is a **progressive erosion** of the skyline. Starting from the full silhouette of `1, …, N`:

1. **Prime 2 pass**: Every even column `n` has its width-2 base stripped. The column `n` splits into an odd residue (which stays in `L_1` at reduced density `1 - 1/2`) and a half-height copy that goes to `L_2`. The extracted width-2 slabs are banked in `budget[2]`.

2. **Prime 3 pass**: From the remaining density in each list, multiples of 3 are stripped. The 3-slabs go to `budget[3]`.

3. **Continue through all primes up to `K_{dn}`**.

After all primes, the original skyline has been eroded into `K_{dn}` residual lists `L_1, …, L_{K_{dn}}`, each a fractional copy of an interval `(0, N/k]`. The eroded material sits in the prime budgets. The skyline has been **decomposed into its prime layers** — each layer's mass extracted and warehoused separately.

The Euler product structure `fraction[t] *= (1 - 1/p)` is the **density decay** of each residual list under successive erosion passes. After all primes up to `K_{dn}`, `L_k` holds only those integers coprime to all primes dividing `k` — a density given by the product `Π_{p | k} (1 - 1/p)`.

---

## VII. Earth-Moving: Redistribution of Skyline Mass

The UP phase is the **inverse** of erosion: the warehoused prime-layer slabs are reassembled and placed beneath below-target columns to lift them above `N/3`.

The CDF dominance check in `verify.py` (line 188: `multiples_cdf[k] ≤ total_cdf[k]`) is the **earth-mover's feasibility condition**: when you sort the demand (how much mass needs lifting by multiplier ≤ k) against the supply (how much multiplier capacity ≤ k is available from `data.multiples`), supply must dominate demand at every level. This is exactly the condition for a valid coupling in the Monge–Kantorovich transport: the CDF of the target measure must dominate the CDF of the source measure pointwise.

The `special` tail — elements in `(0, N/(3·K_{up})]` needing multiplier > `K_{up} = 2^V` — is handled by pure doubling: an average of `V+2` powers of 2 each. In the skyline, this is the **deep basement** of the skyline, far below the target. These columns are so short that only repeated width-2 extensions can reach the target. The cost `special * (V+2)` is charged against the 2-layer budget, which is the thickest layer and can absorb it.

The budget verification (line 209: `spent ≤ budget[p]`) confirms that the earth-moving didn't overdraw any layer. For each prime `p`, the total mass moved via p-slabs (including the special doubling charged to `p = 2`) must not exceed what was extracted during erosion.

---

## VIII. Greedy Pairings as Column Assembly

The `greedy()` function in both `facfac.py` and `smoothfac.py` is a **column assembly** operation on the residual skyline.

After the LP rounds its continuous solution to integers, there are leftover prime-layer fragments — partial slabs that weren't assigned to any factor. The greedy pass scans from the largest remaining prime downward and assembles these fragments into complete columns of height ≥ T:

1. Find the largest prime `p` with remaining budget.
2. Find the smallest factor `j ≥ T` divisible by `p` whose full prime-layer requirements can be met.
3. Assemble that column: withdraw `v_q(j)` from every layer `q | j`.
4. Repeat.

In `smoothfac.py`, the non-smooth greedy pairing (lines 80–93) is even more explicit: for large prime `p`, the column `p · ⌈T/p⌉` is assembled by stacking the width-p slab atop a smooth base of height `⌈T/p⌉`. The "deflation" loop (lines 88–93) descends through the smooth base's factorization, withdrawing from each small-prime layer.

The swap operation in `facfac.py`'s greedy (lines 263–276) — exchanging adjacent primes between a factor and the residual — is a **column surgery**: replacing one prime slab with a neighboring one to make the residual product fit within `[T, N]`.

---

## IX. Synthesis: The Three Files as Three Views of One Skyline

| Aspect | `verify.py` | `facfac.py` | `smoothfac.py` |
|---|---|---|---|
| **Skyline representation** | Fractional densities over intervals | Explicit prime exponent vectors | Sieve array with sign encoding |
| **Erosion** | DOWN phase: prime-by-prime density reduction | Implicit in LP constraint matrix | Two-phase sieve: smooth then non-smooth |
| **Horizon line** | Not needed (works at full resolution `K_{dn}`) | Not needed (all factors enter LP) | Explicit at `√T`: splits greedy towers from LP battleground |
| **Area constraints** | `budget[p]` | `c[p]` as LP RHS | `c[p]` as LP RHS after greedy deflation |
| **Cost landscape** | Not computed (verification only) | Dual variables `a[p]` | Dual variables `row[i].pi` |
| **Earth-moving** | Explicit CDF dominance check | LP primal-dual complementarity | LP + greedy assembly |
| **Column assembly** | Implicit in `multiples[k]` from external data | `greedy()` function | Two-pass: non-smooth greedy + smooth greedy |
| **Height target** | `N/3` via `multiple = (k//3)+1` | `T = ⌈N/3⌉` as LP variable range | `T = ⌈N/3⌉` as LP variable range |

The three files are **three cross-sections of the same skyline**:

- `verify.py` works in the **measure-theoretic** cross-section: densities, CDFs, earth-moving. It never constructs explicit factors — it proves the transport is feasible.
- `facfac.py` works in the **algebraic** cross-section: explicit prime exponents, LP over the full column set, dual certificates. It constructs actual factorizations of `N!`.
- `smoothfac.py` works in the **geometric** cross-section: it literally draws the horizon line at `√T`, handles the tall towers to the right by inspection, and solves the hard optimization only over the smooth mass to the left.

The Factor Skyline unifies all three: it is the 2D object whose horizontal stratification is the prime-layer budget system, whose vertical profile is the target-deficit distribution, whose smooth/non-smooth partition is the horizon line, and whose feasible rearrangements are the earth-movings that lift every column above `N/3` without overdrawing any layer.

