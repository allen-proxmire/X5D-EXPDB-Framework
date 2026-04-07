## Analysis of `verify.py` (file #1)

### Purpose
This is a **verification script** for a "Down-Reorganize-Up" algorithm. It proves that a certain multiplicative rearrangement of the integers in `(0, N]` is feasible, working entirely with exact arithmetic (`Fraction`).

### Algorithmic Structure

**Phase 1 — DOWN (lines 25–75):**
- Starts with the conceptual list `L_1 = (0, N]` (fraction = 1).
- For each prime `p` up to `K_dn = 2^11 = 2048`, it iterates over existing lists `L_k` and repeatedly extracts multiples of `p`. Each extraction:
  - Adds `(1/t) * fraction[t] / p` to the **budget** for prime `p` (harvested prime factors).
  - Spawns a new sub-list `L_{tp}` inheriting the parent's density.
  - Reduces `L_t`'s density by factor `(1 - 1/p)` (Euler-product sieving).
- After all primes, there are exactly `K_dn` lists `L_1, …, L_{2048}`, each tracking what fraction of `(0, N/k]` it holds.

**Phase 2 — REORGANIZE (lines 77–156):**
- Regroups the `L_k` lists by **how large a multiplier** is needed to bring elements up to `N/3`. For each `L_k`, elements in `(N/(3m+r), N/(3m)]` need multiplier `m` or `m+1`.
- Accumulates into `part[k]` (partial intervals) and `whole[k]` (complete intervals), then computes `total[k]` — the total fraction of `(0, N]` landing in each multiplier bucket `S_k`.
- Computes a CDF of these totals and verifies it sums to 1 (plus a "special" tail for elements needing multiplier > `K_up`).

**Phase 3 — UP (lines 169–218):**
- The **special tail** `(0, N/(3·K_up)]` is handled by repeated doubling: on average each element uses `V+2` powers of 2.
- **CDF dominance check** (line 188): verifies `multiples_cdf[k] <= total_cdf[k]` for all `k` — i.e., the proposed multiplier assignment (from external `data.multiples`) never exceeds what's available.
- **Budget check** (line 209): for each prime `p`, verifies that the total prime factors *spent* (including the special doubling cost charged to prime 2) does not exceed the prime factors *harvested* in Phase 1.
- Reports slack in both constraints.

### Key Multiplicative Structure
- The algorithm is a **bookkeeping proof** that the integers `1, …, N` can be rearranged so that each `a_n * n >= N/3`, using only the prime factors extracted by the sieve.
- The sieve is an Euler-product decomposition: each prime `p` contributes factors that are "banked" then "spent" to multiply small elements upward.
- The threshold `N/3` is the target; elements already above it need multiplier 1, smaller ones need larger multipliers funded by the budget.
- `K_dn = K_up = 2^11 = 2048` controls the resolution/truncation of both the sieve depth and the multiplier range.

## Analysis of `facfac.py` (file #2)

### Purpose
Optimally decompose `N!` into as many factors as possible, each of size at least `T` (default `⌈N/3⌉`), using **linear programming** (Gurobi) followed by a **greedy** mop-up.

### Data Structures
- **`Problem(N, T, c, f)`**: `c[p]` = total exponent of prime `p` in `N!`; `f[j][p]` = exponent of `p` in `j`.
- **`Factorization(c, f, r, a)`**: `f[j]` = how many times factor `j` is used; `c` = primes consumed; `r` = residual (unused) prime exponents; `a` = LP dual variables (per-prime "prices").

### Algorithmic Structure

**`sieve(N, T)`** — Computes the complete prime factorization of every integer `1..N` and aggregates into the total prime content of `N!`. Verified exactly against `factorial(N)` for small `N`.

**`lpfac(prob)` — The LP core:**
- **Decision variables**: `x[j]` for each `j ∈ [T, N]` — how many times `j` appears as a factor.
- **Constraints**: for each prime `p`, the total exponent of `p` consumed across all chosen factors must not exceed `c[p]` (the exponent in `N!`).
- **Objective**: maximize `Σ x[j]` — the total number of factors ≥ `T`.
- Optionally enforces **monotone dual variables** (`z` variables) for a rigorous upper bound.
- After solving, rounds LP solution to integers and extracts a **dual certificate** (`sa[p]`) — rounded-up dual prices that yield a provable upper bound on the number of factors.

**`greedy(prob, fact)` — Residual cleanup:**
- Takes the leftover prime exponents `r` and greedily assigns them to the largest available factors `j ≥ T` whose prime requirements can be met.
- Handles edge cases where the residual product exceeds `N` by swapping adjacent primes in existing factors.
- If the final residual is itself ≥ `T`, it becomes one more factor.

**`oeis(N)` — Threshold binary search:**
- Binary searches for the largest `T` such that `N!` can still be written as ≥ `N` factors all ≥ `T`. This computes OEIS sequence A034258.

### Key Multiplicative Structure
- The problem is: **write `N!` as a product of `N` integers, each ≥ `T`**. This is equivalent to finding a permutation `σ` where `σ(n) · n ≥ T` for all `n`, since `N! = Π n`.
- The LP relaxation gives the prime-budget viewpoint: each prime `p` has a "bank" of `v_p(N!)` copies, and each large factor `j ≥ T` "withdraws" `v_p(j)` copies of `p`. Maximize the number of withdrawals within budget.
- The dual variables `a[p]` assign a **price per prime**, and the dual bound `Σ a[p] · c[p]` is a rigorous upper bound on the factor count.
- Default threshold `T = ⌈N/3⌉` directly parallels the `N/3` target in `verify.py`.

## Analysis of `smoothfac.py` (file #3)

### Purpose
A **scalable variant** of `facfac.py` that decomposes `N!` into factors ≥ `T`, but splits the work by **smoothness**: large primes (≥ √T) are handled greedily upfront, and only the **√T-smooth** factors enter the LP. This dramatically reduces LP size for large `N`.

### Algorithmic Structure

**Smoothness split (lines 38–94):**

1. **Sieve small primes** (`p < √T`): For each small prime, sieve through `1..N`, recording `f[j] = largest prime factor of j` and accumulating `c[p]` = total exponent of `p` in `N!`. Only integers whose largest prime factor is < √T are "smooth."

2. **Sieve large primes** (`p ≥ √T`): For each large prime, mark all its multiples as **non-smooth** (`f[j] = 0`). Then immediately apply a **greedy complement** strategy:
   - For large prime `p`, the factor `p · ⌈T/p⌉` is ≥ `T` and uses `p` exactly once.
   - Assign all `c[p]` copies of `p` to this factor greedily (`f[p·j] = -c[p]`).
   - **Deflate** the small-prime budget: the smooth part of the complement `⌈T/p⌉` consumes small-prime exponents from `c`.

**LP on smooth factors (lines 123–161):**
- Variables `x[j]` only for smooth `j ∈ [T, N]` (those with `f[j] > 1`).
- Constraints: for each small prime `p`, total consumption ≤ `c[p]` (already reduced by greedy non-smooth allocations).
- Objective: maximize `Σ x[j]`.
- This LP is much smaller than `facfac.py`'s since it excludes all non-smooth columns.

**LP rounding + greedy cleanup (lines 163–213):**
- Round LP solution to integers, deflate consumed primes.
- Greedy pass on remaining small-prime budget: find the largest unused prime, pair it with a smooth factor ≥ `T`, repeat.

**Output:**
- Reports `total factors = non-smooth + LP + greedy`.
- Returns `[lower_bound, upper_bound]` where UB = non-smooth count + LP relaxation value.

### Key Multiplicative Structure
- The critical insight is that **large primes are easy**: a prime `p ≥ √T` needs only a cofactor of size `⌈T/p⌉ ≤ √T` to form a valid factor ≥ `T`. Each copy of `p` in `N!` is consumed this way.
- The hard optimization is over **smooth numbers** — integers in `[T, N]` composed entirely of small primes — which compete for the shared small-prime budget.
- The `f[]` array serves triple duty: during sieving it stores the largest prime factor; after the greedy phase, negative values encode factor multiplicities. This is a memory-efficient encoding for very large `N`.
- Same default threshold `T = ⌈N/3⌉` as the other files.

## Analysis of `greedy.py` (file #4)

### Purpose
A **pure greedy algorithm** (adapted from Andrew Sutherland's Maple code) for factoring `N!` into as many factors as possible, each ≥ `T`. No LP — just a single top-down greedy pass.

### Algorithmic Structure

**Setup (lines 9–20):**
- Enumerate all primes `P` up to `T`.
- Compute `E[i]` = exponent of `P[i]` in `N!` via Legendre's formula: `v_p(N!) = Σ ⌊N/p^k⌋`.

**Free factors (lines 22–24):**
- Every prime `p ∈ [T, N]` is itself a valid factor (≥ `T`). Each such prime appears `⌊N/p⌋` times in `N!`. Collect all of these immediately — they cost nothing from the small-prime budget.

**Main greedy loop (lines 34–75):**
1. Find the **largest remaining prime** `P[i]` with `E[i] > 0`.
2. Search for the **smallest cofactor** `m` such that `m · P[i] ≥ T` and the prime exponents of `m · P[i]` are all available in the remaining budget `E`.
3. Compute `divisions` = how many times this factor `m · P[i]` can be extracted (the bottleneck across all primes in its factorization).
4. Extract all `divisions` copies: decrement `E[j]` for each prime `j` dividing `m · P[i]`.
5. The `minm` variable is an optimization: once we've confirmed that all cofactors below `m` fail for a given prime, skip them on future iterations.

**Termination:** When `m` reaches `T` (meaning `P[i] = 1` would be needed, i.e., no valid pairing exists) or all primes are exhausted.

### Key Multiplicative Structure

- **Largest-prime-first ordering**: The algorithm processes primes from largest to smallest. This is the greedy heuristic — scarce primes (high index, low multiplicity) are paired first, before the abundant small primes consume the cofactor space.
- **Cofactor search**: For prime `p`, the minimum cofactor is `⌈T/p⌉`. The search `m, m+1, m+2, …` walks upward until finding an `m` whose prime factorization is affordable. This is a **feasibility scan** over potential column heights.
- **Batch extraction**: `divisions` extracts all affordable copies at once, not just one. This is critical for efficiency — a prime `p` near `T/2` paired with cofactor 2 can be extracted `min(E[p], E[2])` times in one step.
- **No backtracking**: Once a pairing is made, it's permanent. This is what distinguishes it from the LP approaches — `facfac.py` and `smoothfac.py` can find globally better allocations, while this greedy can get stuck with suboptimal pairings.
- The free-factor collection (primes ≥ `T`) is identical to what `smoothfac.py` does for primes ≥ `√T` but at a coarser threshold — only primes that are *individually* ≥ `T` need no cofactor at all.

### Relation to the Other Files
This is the simplest algorithm in the pipeline. It serves as a **baseline** and a fast heuristic for large `N` (the hardcoded call is `N=300000, T=100000`). The LP-based methods (`facfac.py`, `smoothfac.py`) can provably do better by optimizing globally, but this greedy is fast and often sufficient to demonstrate `|L| ≥ N`.

## Analysis of `rearrange_lp.py` (file #5)

### Purpose
Generate a **linear program in lp_solve format** that checks whether the small-prime content of `1, …, N` can be rearranged so that every element is lifted above threshold `T`. This is the most explicitly **earth-moving** formulation in the project.

### Algorithmic Structure

**Smooth number enumeration (lines 5–26):**
- `smooth_via_heap(B, primes)` generates all `P`-smooth numbers up to `B` in sorted order via a min-heap. These are the candidate **multipliers** — the smooth numbers that can be assembled from the small-prime budget.

**Budget and target computation (lines 43–58):**
- For each integer `i ∈ [1, N]`:
  1. **Strip small primes**: divide out all primes ≤ `P`, accumulating each into `budget[p]`.
  2. **Compute the non-smooth residue** `t` — the part of `i` that has no prime factor ≤ `P`.
  3. **Find the smallest smooth multiplier** `s` such that `t · s ≥ T`. Record `target[s] += 1`.

So `target[s]` counts how many integers need smooth multiplier *exactly* `s` (the smallest sufficient one), and `budget[p]` is the total supply of prime `p` extracted from all integers.

**LP generation — Earth-moving constraints (lines 63–71):**
- Decision variable `a_s` = how many integers are assigned smooth multiplier `s`.
- The earth-moving constraints enforce **CDF dominance from above**: scanning multipliers from largest to smallest, the cumulative assignment `Σ_{s' ≥ s} a_{s'}` must be ≥ the cumulative demand `Σ_{s' ≥ s} target[s']`. This ensures that enough integers are "moved down" (assigned large multipliers) before assigning small ones.
- This is exactly the discrete Monge–Kantorovich condition: the transport plan `a` must dominate the demand CDF.

**LP generation — Prime budget constraints (lines 74–85):**
- For each prime `p ≤ P`: the total `p`-content consumed by the assignment, `Σ_s v_p(s) · a_s`, must not exceed `budget[p]`.

**No objective function** (line 61): This is a **pure feasibility** LP. The question is not "maximize" but "does a valid earth-moving exist?"

### Key Multiplicative Structure

- **The non-smooth residue `t`** is the crux. Each integer `i` is factored as `i = (smooth part) × t`. The smooth part's prime content goes into the budget. The residue `t` determines the *minimum* multiplier needed: the smallest smooth `s` with `t · s ≥ T`.
- **The smooth multipliers are the transport destinations.** Each `a_s` represents mass moved to multiplier level `s`. The CDF constraint ensures monotone coupling — you can't assign a small multiplier to something that needs a large one.
- **Default threshold is `N/4`** (line 106), not `N/3` as in the other files. This is a weaker target, suggesting this formulation may be used for exploring different constants.
- **Parameter `P`** controls the smoothness bound independently of `T`. This decouples the "width of the skyline base" from the "height target" — you can solve the earth-moving over just 2-smooth, or {2,3}-smooth, or larger prime sets, studying how the feasibility changes with the available prime palette.
- The reversed scan order in the CDF constraints (largest `s` first) is the natural direction: heavy lifting (large multipliers) must be committed first, then lighter adjustments fill in.

### Contrast with the Other Files
This is the **cleanest expression of the earth-moving** that `verify.py` checks. Where `verify.py` works with continuous densities and CDFs, `rearrange_lp.py` generates the discrete integer program directly. Where `facfac.py` maximizes factor count, this checks feasibility of a specific rearrangement. It is the bridge between the asymptotic density argument (`verify.py`) and the explicit factorial decomposition (`facfac.py`/`smoothfac.py`).

## Analysis of `one_fourth.py` (file #6)

### Purpose
A **negative result / impossibility proof**: demonstrates that for sufficiently large `N`, it is **not** possible to split `N!` into `N` factors each ≥ `N/4` using only rearrangements of powers of 2 and 3. This establishes a hard barrier at `N/4` for {2,3}-smooth multipliers.

### Algorithmic Structure

**Setup (lines 9–26):**
- Works entirely in the {2,3}-smooth world. Enumerates all numbers of the form `2^a · 3^b` up to `4M` where `M = 4 · 3^9 = 78732`.
- The coprime fraction is `1/3` — one-third of integers are coprime to 6.

**Distribution computation (lines 35–66):**
- For each smooth multiplier `x ≤ M`, computes `dist[x]`: the fraction of integers in `(0, N]` that, after stripping all factors of 2 and 3, need *exactly* multiplier `x` to reach `N/4`.
- An integer originally at position `n/N ∈ (0, 1]` needs multiplier `x` if its {2,3}-stripped residue `t` satisfies `t · x ≥ N/4` but `t · x_{prev} < N/4`.
- The inner loop over `y` (the original {2,3}-smooth part) accounts for the fact that stripping 2s and 3s from different starting points leads to the same residue needing multiplier `x`. The density contribution is `(1/3) · (hi - lo) · (1/y)`.

**Dual proof by weighted inequality sum (lines 68–149):**
- Constructs a **weighted combination** of three types of inequalities, all with coefficients that are multiples of `1/32`:

  1. **Prime budget for 2** (coeff `2/32`): `Σ_x v_2(x) · a_x ≤ 1` (the 2-budget is `v_2(N!) / N → 1`).
  2. **Prime budget for 3** (coeff `3/32`): `Σ_x v_3(x) · a_x ≤ 1/2` (the 3-budget is `v_3(N!) / N → 1/2`).
  3. **Earth-moving CDF constraints** (various coefficients): `Σ_{y ≤ x} a_y ≤ CDF(x)` — the partial sum of assignments up to multiplier `x` can't exceed the cumulative demand.

- The earth-moving coefficients are selective: `2/32` for `x = 1`, `1/32` for "nice" `x` (those with `x ≤ M` and power of 2 at most 2), and `0` otherwise.

**The punchline (lines 142–149):**
- Verifies that the weighted LHS has coefficient ≥ 1 for *every* smooth number `x`. So `Σ a_x ≤ LHS(a)`.
- Verifies that the weighted RHS is **strictly less than 1**.
- Therefore `Σ a_x < 1`, meaning the total fraction of integers that can be successfully paired is less than 1. **Not all of `N!` can be covered.**

**Quantification (lines 153–207):**
- Recomputes the bound as `b + O(c/N) ≥ 1`, deriving the explicit constant `b < 1` and the threshold `N₀ = ⌈c/(1-b)⌉` above which the impossibility holds.

### Key Multiplicative Structure

- This is a **Farkas lemma / LP duality** argument done by hand. The three inequality families (two prime budgets + earth-moving CDF constraints) are the constraints of the primal feasibility LP. The carefully chosen coefficients `(2/32, 3/32, various/32)` form a **dual certificate** proving infeasibility.
- The restriction to primes {2, 3} makes the smooth numbers a discrete lattice `2^a · 3^b`, and the entire computation is exact over `Fraction`.
- The threshold `N/4` (not `N/3`) is critical: at `N/3`, the argument would fail (the project's other files show `N/3` *is* achievable). This file proves that `N/4` is **beyond reach** with only {2,3}-rearrangements — you cannot improve the constant from `1/3` to `1/4` using just the two smallest primes.
- The parameter `M = 4 · 3^9` is the truncation point: multipliers beyond `M` already have LHS coefficient ≥ 1 from the prime budgets alone (line 104), so only multipliers ≤ `M` need the earth-moving constraints to push their coefficients above 1.
- The "nice" condition (power of 2 ≤ 2) for earth-moving coefficients is an optimized choice — not all CDF constraints contribute equally, and this selection was tuned to make the RHS as small as possible while keeping all LHS coefficients ≥ 1.

### Role in the Project
This is the **converse** to the constructive algorithms. While `verify.py` proves that `N/3` is achievable (using all primes), `one_fourth.py` proves that `N/4` is not achievable with only {2,3}. Together they bracket the problem: the achievable threshold lies in `[N/4, N/3]`, and improving beyond `N/3` requires primes beyond 2 and 3 — but reaching `N/4` is impossible even with them restricted to {2,3}.

## Analysis of `prove43631.py` (file #7)

### Purpose
A **rigorous, exact-arithmetic verification** that `t(43631) < T = ⌈43631/3⌉ = 14544` — i.e., it is **impossible** to factor `43631!` into `43631` factors each ≥ `14544`. This is a concrete upper bound proof for a specific `N`, using an LP dual certificate.

### Algorithmic Structure

**The dual certificate (lines 25–132):**
- A hand-provided table of 131 entries mapping primes to integer numerators over a common denominator 1257 = 3 × 419.
- These define dual variables `a[p] = lp_bounds[p] / 1257` for each listed prime. Primes between listed values inherit the most recent `a[p]` (piecewise-constant interpolation, line 143). All primes ≥ 14549 get `a[p] = 1257/1257 = 1`.

**Three verification checks:**

1. **Bound check (lines 166–172):** Compute the dual objective:
   ```
   bound = Σ_p a[p] · v_p(43631!)
   ```
   Assert `bound < N = 43631`. This is the **dual upper bound** on the maximum number of factors ≥ T extractable from `N!`. If this is less than `N`, then `N!` cannot be split into `N` factors each ≥ T.

2. **Dual feasibility check (lines 179–184):** For every integer `j ∈ [T, N]`:
   ```
   Σ_p a[p] · v_p(j) ≥ 1
   ```
   This is the LP dual constraint: every candidate factor `j ≥ T` must have "prime-weighted cost" at least 1. This ensures the dual is feasible and the bound is valid.

3. **Monotonicity check (lines 187–191):** The `a[p]` values are **non-decreasing** in `p`. This is the rigorous monotonicity condition from `facfac.py`'s `z`-variable formulation. It ensures the bound is a valid relaxation.

### Key Multiplicative Structure

- The dual variables `a[p]` are **prices per prime**. Small primes (p = 2, 3) are cheap (`a[2] ≈ 0.072`, `a[3] ≈ 0.115`) because they're abundant in `N!`. Large primes are expensive (approaching 1) because they're scarce.
- The dual objective `Σ a[p] · v_p(N!)` is the **total cost of the factorial** under these prices. If this total cost is less than `N`, then even if every factor `j ≥ T` costs at least 1 unit, you can't afford `N` of them.
- The piecewise-constant interpolation of `a[p]` means the price schedule has ~131 steps. Between consecutive listed primes, the price is flat — this is an artifact of the LP solver finding that many primes in a range have the same shadow price at optimality.
- The denominator 1257 = 3 × 419 is the LCM structure of the optimal dual: all dual variables are rational with this denominator, reflecting the structure of the LP basis.
- The specific `N = 43631` is chosen because it is (presumably) the smallest `N` where `t(N) < ⌈N/3⌉` — i.e., the Erdős–Guy–Selfridge bound of `N/3` first fails here. The certificate proves this failure rigorously.

### Role in the Project
This is the **sharp boundary marker**. Where `verify.py` proves `N/3` works asymptotically and `facfac.py`/`smoothfac.py` construct factorizations for specific `N`, this file proves that at `N = 43631`, the `N/3` threshold is **too aggressive** — the prime budget is insufficient. It is the exact-arithmetic, computer-verified counterpart to the LP solver's floating-point output.

## Analysis of `calculations.py` (file #8)

### Purpose
Verify the **analytic error bounds** from Section 7 of the paper for a specific large `N` (~10^10.69). This checks that the asymptotic argument — that `N!` can be split into `N` factors each ≥ `N/3` — holds at this concrete `N` by bounding all error terms.

### Algorithmic Structure

**Core framework: Proposition 7.1 verification.**
The function `evaluate(t, N, A, K, L)` checks two aggregate inequalities:

1. **Delta condition** (`delta_sum < delta`): The sum of eight error terms δ₁ through δ₈ must be less than the main term `δ = log(N/t) - 1`. This controls the **counting error** — how many factors ≥ `t` we can extract.

2. **Alpha condition** (`alpha_sum < 1`): The sum of seven error terms α₁ through α₇ must be less than 1. This controls the **prime budget error** — ensuring the prime factors are not over-spent.

**Parameters:**
- `N = 10^10.69 ≈ 4.9 × 10^10`, `t = N/3`, `A = 189`, `K = 293`, `L = 4.5`
- `K` is a smoothness cutoff for "medium" primes
- `A` controls an approximation parameter (related to `σ = 3N/(tA)`)
- `L` indexes into a table of `κ(L)` values — logarithmic gap parameters from sieve theory

**The error terms:**

*Delta terms (counting errors):*
- **δ₁** (Lemma 8.2): Approximation error from the `N/3` threshold rounding — `3N/(2tA) + 4/N`
- **δ₂** (§7.7): Integral of a step function `f_α` on `(ε, 1]` with prime number theorem error — the main analytic term
- **δ₃** (Corollary 8.4): Contribution from primes ≤ `t/K` and small primes ≤ `√N`
- **δ₄** (§7.9): Error from "medium" primes in `(K, K(1+σ)]`
- **δ₅** (§7.10): Discrepancy between two counting functions `A` and `B` for primes ≤ `K`
- **δ₆** (§7.11): A `κ/N` tail term
- **δ₇** (§7.12, §8.4): Error from the {2,3}-smooth structure — involves `B_lower` for primes 2 and 3
- **δ₈** (§7.13): Another tail term `2(log t + κ)/N`

*Alpha terms (budget errors):*
- **α₁**: Zero (no contribution)
- **α₂** (§7.16): Cross-term between primes 2 and 3, parameterized by `γ₂, γ₃`
- **α₃** (Corollary 8.4): Small-prime contribution scaled by `κ**`
- **α₄** (§7.18): Medium-prime budget error
- **α₅** (§7.19): Discrepancy budget error for primes ≤ K
- **α₆** (§7.20): Tail budget term
- **α₇** (§7.21): Finite-N correction for primes 2 and 3

**Supporting functions:**
- `E(N)`: Effective error term in the prime number theorem (eq. 2.15)
- `pixy_upper/lower`: Bounds on `π(x) - π(y)` using PNT with error
- `kappa(L)`: Tabulated logarithmic gaps `log(9/8), log(32/27), log(4/3), log(3/2), log(2)` depending on `L` (Table 1 of the paper)
- `gamma_2, gamma_3`: Parameters controlling the {2,3}-factorization trade-off
- `kappa_starstar`: The maximum of two "fancy kappa" functions — the effective gap after accounting for {2,3} interactions
- `total_variation, f_integ`: Exact computation of the total variation and integral of the step function `f_α(x) = ⌊1/x⌋ · log(⌈1/(αx)⌉ · α · x)` on `(ε, 1]`
- `A_upper/lower, B_upper/lower`: Bounds on two prime-counting sums over coprime-to-6 integers — these are the concrete versions of the asymptotic sieve estimates

### Key Multiplicative Structure

- The **A and B functions** are the heart of the analytic argument. `A` counts how many primes `p` contribute to the factorization budget via multiplier `m` (coprime to 6), using intervals of the form `(t/min(m,K), t(1+σ)/m]`. `B` counts the same primes but weighted by their actual contribution `k/N` to the budget. The discrepancy `|A - B|` is bounded by the δ₅ and α₅ terms.

- The **γ₂, γ₃ parameters** control a delicate trade-off: extracting powers of 2 uses up budget that could help with powers of 3, and vice versa. The `gamma_2` and `gamma_3` functions compute the optimal balance point. This is the analytic version of the interplay between the 2-budget and 3-budget in `one_fourth.py`.

- The **κ(L) function** encodes the multiplicative gap structure: for smooth numbers of level `L`, the ratio between consecutive smooth numbers is at most `e^{κ(L)}`. The five cases correspond to different density regimes of smooth numbers. This is the **analytic shadow** of the discrete column-spacing in the Factor Skyline.

- The **`f_integ` and `total_variation` functions** compute properties of the step function that arises when you sum `⌊1/x⌋ · log(⌈N/(tx)⌉ · t · x/N)` over the unit interval. This function's integral gives the main term of the factor count, and its total variation controls the PNT error via a Stieltjes integration bound (Lemma 2.2).

- The comment at line 6 is significant: the bounds are **not monotone in N**, meaning each `N` must be checked individually (or via interval arithmetic). This is why the code works for a single `N` and the author notes a rewrite is needed.

### Role in the Project
This is the **analytic verification engine** — the bridge between the paper's theoretical bounds and a computer-checked proof. Where `prove43631.py` verifies a small-`N` impossibility via LP duals, this file verifies that the asymptotic argument (which proves possibility for large `N`) kicks in by `N ≈ 10^{10.69}`. Together with the LP-based tools covering finite `N`, they form a complete proof pipeline.

---

## All Eight Files Analyzed

Here is a summary of the complete pipeline:

| File | Role | Method | Threshold |
|---|---|---|---|
| `verify.py` | Asymptotic feasibility proof | Density sieve + earth-moving CDF check | N/3 |
| `facfac.py` | Exact factorial decomposition | Full LP (Gurobi) + greedy + dual certificate | ⌈N/3⌉ |
| `smoothfac.py` | Scalable factorial decomposition | Smooth/non-smooth split + reduced LP | ⌈N/3⌉ |
| `greedy.py` | Fast baseline heuristic | Pure greedy, largest-prime-first | T (configurable) |
| `rearrange_lp.py` | Earth-moving LP generator | Smooth multipliers + CDF constraints | ⌈N/4⌉ |
| `one_fourth.py` | Impossibility proof for N/4 | Hand-crafted dual certificate over {2,3} | N/4 |
| `prove43631.py` | Sharp impossibility at N=43631 | LP dual certificate verification | ⌈N/3⌉ |
| `calculations.py` | Analytic bound verification | PNT error terms, sieve estimates | N/3 |

Ready for your next instruction — whether that's the Factor Skyline reinterpretation of the full 8-file pipeline, or any other direction.