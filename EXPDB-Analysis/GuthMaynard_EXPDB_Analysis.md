# How Guth–Maynard (2024) Reshapes the EXPDB Skyline: A Structural Analysis

Allen Proxmire

April 2026

---

## 1. What This Document Is and Is Not

This document analyzes how the Guth–Maynard (2024) large value estimate fits into the EXPDB pipeline as described in the EXPDB-Skyline paper. It uses the polyhedral framework (the master region $\mathcal{P} \subset \mathbb{R}^5$) to understand which constraints are tightened, how the effect propagates, and what the next bottleneck is.

**What this document does:**
- Identifies the specific half-space that Guth–Maynard adds to $\mathcal{P}$.
- Traces the propagation through the dimension ladder $\mathcal{P} \to R_{\text{LV}} \to A(\sigma) \to \theta$.
- Identifies the structural bottleneck after incorporation.
- Describes the computational project needed to make this fully rigorous.

**What this document does NOT do:**
- It does not run the EXPDB code (that requires forking the repository and executing the Python pipeline).
- It does not compute exact numerical values of $\theta$ (that requires the full LP computation).
- It does not prove any new analytical results.

---

## 2. The Guth–Maynard Result as a Half-Space

### 2.1 The Result

Guth and Maynard prove a new large value estimate for Dirichlet polynomials. In the EXPDB coordinate system $(\sigma, \tau, \rho)$, a large value estimate constrains the *large value region* $R_{\text{LV}} \subset \mathbb{R}^3$ — the set of triples $(\sigma, \tau, \rho)$ for which a Dirichlet polynomial of length $N$ can have at least $N^\rho$ values of size at least $N^\sigma$ on a set of $N^\tau$ well-spaced points.

The classical large value estimates constrain $R_{\text{LV}}$ through affine inequalities of the form:

$$a_0 + a_1 \sigma + a_2 \tau + a_3 \rho \geq 0$$

Each such inequality defines a half-space in $(\sigma, \tau, \rho)$-space, and $R_{\text{LV}}$ is the intersection of all such half-spaces (within the bounding box).

### 2.2 The Pre-Guth–Maynard Landscape

Before Guth–Maynard, the binding large value estimates near the critical line $\rho \approx 3\sigma/4$ included:

- **Huxley (1972):** The zero-density estimate $N(\sigma, T) \leq T^{12(1-\sigma)/5 + o(1)}$, which corresponds to $A(\sigma) \leq 12(1-\sigma)/5$ (the zero-density exponent). This was the binding constraint for the prime gap bound $\theta$.

- **Montgomery (1971):** $\rho \leq 2(1-\sigma)$ (the "trivial" large value bound from the mean value theorem). Always active near $\sigma = 1$.

- **Halász (1968):** $\rho \leq 1 - \sigma + \tau/2$ (the Halász-type bound). Active in certain $(\sigma, \tau)$ regions.

- **Jutila (1977) / Huxley (1972):** Various bounds constraining $R_{\text{LV}}$ in the intermediate $\sigma$ range.

The binding constraint for $\theta$ was Huxley's $A(\sigma) = 12(1-\sigma)/5$, achieved at a specific $\sigma^* \approx 0.833$.

### 2.3 What Guth–Maynard Adds

The Guth–Maynard result improves the large value estimate near $\rho \approx 3\sigma/4$. In EXPDB terms, it adds a new half-space constraint to $R_{\text{LV}}$ that is *tighter than Huxley* in the critical region.

Specifically, the Guth–Maynard bound gives:

$$N(\sigma, T) \leq T^{30(1-\sigma)/13 + o(1)}$$

which corresponds to a zero-density exponent:

$$A_{\text{GM}}(\sigma) = \frac{30(1-\sigma)}{13}$$

compared to Huxley's:

$$A_{\text{Hux}}(\sigma) = \frac{12(1-\sigma)}{5}$$

Since $30/13 \approx 2.307 < 12/5 = 2.4$, the Guth–Maynard bound is strictly tighter for all $\sigma \in (1/2, 1)$.

### 2.4 How the Half-Space Cuts $R_{\text{LV}}$

The Guth–Maynard half-space cuts off a *slice* of the previously admissible $R_{\text{LV}}$. Geometrically:

- **Before GM:** The face of $R_{\text{LV}}$ near the critical region was determined by Huxley's bound, with slope $12/5$ in $(1-\sigma)$.
- **After GM:** A new face with slope $30/13$ replaces the Huxley face, cutting the polytope more aggressively.

The cut is most significant in the $\sigma$ range where $A_{\text{GM}}(\sigma)$ is tighter than $A_{\text{Hux}}(\sigma)$ — which is *the entire range* $(1/2, 1)$, since $30/13 < 12/5$ uniformly. But the impact on $\theta$ depends on where the supremum $\theta = \sup_\sigma \max(\alpha, \beta)$ is achieved.

---

## 3. Propagation Through the Pipeline

### 3.1 The Dimension Ladder

The EXPDB pipeline descends:

$$\mathcal{P} \subset \mathbb{R}^5 \;\xrightarrow{\pi}\; R_{\text{LV}} \subset \mathbb{R}^3 \;\xrightarrow{\sup \rho/\tau}\; A(\sigma) \;\xrightarrow{\text{env}^-}\; A^*(\sigma) \;\xrightarrow{\sup_\sigma}\; \theta$$

The Guth–Maynard result enters at the $R_{\text{LV}}$ level (lifted to $\mathcal{P}$ by adding trivial bounds on $\rho^*$ and $s$). Its effect propagates:

1. **$R_{\text{LV}} \to A(\sigma)$:** The tighter LV region produces a tighter zero-density estimate $A(\sigma)$. Specifically, $A(\sigma)$ changes from $12(1-\sigma)/5$ (Huxley) to $30(1-\sigma)/13$ (Guth–Maynard) in the region where GM is binding.

2. **$A(\sigma) \to \theta$:** The tighter $A(\sigma)$ produces a tighter $\theta$ through the formulas:

$$\alpha(\sigma) = 4\sigma - 2 + \frac{2(A^*(\sigma)(1-\sigma) - 1)}{A^*(\sigma) - A(\sigma)}$$

$$\beta(\sigma) = 4\sigma - 2 + \frac{A^*(\sigma)(1-\sigma) - 1}{A(\sigma)}$$

$$\theta = \sup_\sigma \max(\alpha(\sigma), \beta(\sigma))$$

Since $A(\sigma)$ appears in the *denominator* of some terms, a decrease in $A(\sigma)$ can have a non-trivial (and not always monotone) effect on $\theta$. The exact effect depends on the relative values of $A(\sigma)$ and $A^*(\sigma)$ at the optimal $\sigma^*$.

### 3.2 The Pre-GM and Post-GM Values of $\theta$

**Before Guth–Maynard:**

The best prime gap exponent was $\theta = 7/12 \approx 0.5833$, meaning primes in almost all short intervals of length $x^{7/12 + \varepsilon}$. This corresponds to the Huxley zero-density estimate $A(\sigma) = 12(1-\sigma)/5$ being the binding constraint.

**After Guth–Maynard:**

The improved zero-density estimate gives $\theta = 17/30 \approx 0.5667$, meaning primes in short intervals of length $x^{17/30 + \varepsilon}$. The improvement is:

$$\Delta\theta = 7/12 - 17/30 = 35/60 - 34/60 = 1/60 \approx 0.0167$$

This is a small but significant improvement — moving $\theta$ closer to the Riemann Hypothesis target of $\theta = 1/2$.

### 3.3 Where $\sigma^*$ Is Achieved

The optimal $\sigma^*$ where $\theta$ is achieved shifts when the binding zero-density estimate changes. The exact location of $\sigma^*$ depends on the interplay between $A(\sigma)$ and $A^*(\sigma)$ — it requires the full pipeline computation to determine precisely.

However, based on the structure of the formulas, $\sigma^*$ is expected to be in the range $0.8 < \sigma^* < 0.9$ — the region where the zero-density estimate is most constraining.

---

## 4. Binding Constraints After Guth–Maynard

### 4.1 What Remains Binding

After incorporating Guth–Maynard, the constraints on $\mathcal{P}$ that are *binding* (tight at the optimal point) are expected to include:

1. **Guth–Maynard (2024):** The new large value estimate. This is now the *primary binding constraint* for the zero-density exponent $A(\sigma)$ in the critical $\sigma$ range.

2. **Zero-density energy estimates:** The $A^*(\sigma)$ function, which enters the $\theta$ computation through the $\alpha(\sigma)$ and $\beta(\sigma)$ formulas. The binding constraints for $A^*$ come from the energy region $R_{\text{energy}} = \pi_{\sigma,\tau,\rho^*}(\mathcal{P})$, which is the *complementary* projection to $R_{\text{LV}}$.

3. **Exponent pair constraints:** The EP hull constrains $\mathcal{P}$ through the lifted EP-to-LVER construction (Section 4.3.4 of the EXPDB-Skyline paper). The specific binding EPs depend on $\sigma^*$.

4. **Heath-Brown energy relations:** The direct LVER constraints coupling $\rho$, $\rho^*$, and $s$ through the $s \leq f(\rho, \tau)$ relations. These are binding when the $s$-coordinate couples the LV and energy projections.

### 4.2 What Becomes Slack

After Guth–Maynard, the constraints that are *slack* (not binding at $\sigma^*$) are expected to include:

1. **Huxley (1972) zero-density estimate:** Completely superseded by Guth–Maynard. The Huxley half-space is now strictly interior to the Guth–Maynard half-space in the binding region.

2. **Pre-2024 large value estimates** in the $\rho \approx 3\sigma/4$ region: Any LV estimate that is weaker than Guth–Maynard near the critical $\sigma$ range becomes slack.

3. **Montgomery's mean-value bound:** Active near $\sigma = 1$ but not at the optimal $\sigma^* \approx 0.85$.

### 4.3 The Binding Constraint Structure

The binding constraints form a *minimal determining set* — the smallest collection of literature results that determines the current value of $\theta$. Proposition 6.12 of the EXPDB-Skyline paper guarantees that this set is monotone in the inclusion order: adding results can only tighten $\theta$.

The post-Guth–Maynard binding set is expected to have the structure:

| Constraint Type | Source | Role |
|----------------|--------|------|
| Large value estimate | **Guth–Maynard (2024)** | Binding for $A(\sigma)$ |
| Zero-density energy | Heath-Brown / Ivić | Binding for $A^*(\sigma)$ |
| Exponent pair | Bourgain / Huxley | Binding for EP hull → LVER |
| LVER coupling | Heath-Brown (1979) | Coupling $\rho$ and $\rho^*$ through $s$ |

---

## 5. Sensitivity Analysis: The Next Bottleneck

### 5.1 The Leverage Question

For each binding constraint, the *leverage* is: how much would $\theta$ improve if that constraint were tightened by a given amount?

The leverage depends on the *dual variable* at the binding constraint — the sensitivity of the objective function to the constraint's right-hand side. In linear programming terms, the dual variable $\lambda_i$ of constraint $i$ satisfies:

$$\frac{\partial \theta}{\partial b_i} = \lambda_i$$

where $b_i$ is the right-hand side of constraint $i$.

### 5.2 Expected Bottleneck Ranking

Based on the pipeline structure (without running the full computation), the expected ranking of next bottlenecks is:

**Bottleneck 1: The zero-density energy estimate $A^*(\sigma)$.**

After Guth–Maynard tightens $A(\sigma)$, the binding constraint for $\theta$ is expected to shift partially toward $A^*(\sigma)$. The formulas for $\alpha(\sigma)$ and $\beta(\sigma)$ involve *both* $A$ and $A^*$:

$$\alpha = 4\sigma - 2 + \frac{2(A^*(1-\sigma) - 1)}{A^* - A}$$

When $A$ decreases (Guth–Maynard), the denominator $A^* - A$ changes, and the relative importance of $A^*$ increases. The next improvement to $\theta$ may come from tightening $A^*(\sigma)$ rather than further tightening $A(\sigma)$.

**Why this matters:** $A^*(\sigma)$ is derived from the *energy region* $R_{\text{energy}} = \pi_{\sigma,\tau,\rho^*}(\mathcal{P})$ — the *other* three-dimensional projection of the master polytope. Improving $A^*$ requires new *additive energy estimates* or *zero-density energy estimates*, not further large value estimates. The bottleneck may have shifted from the LV world to the energy world.

**Bottleneck 2: Exponent pairs near the critical line.**

The exponent pairs constrain $\mathcal{P}$ through the EP-to-LVER construction. If the binding EP is an old result (e.g., a classical Huxley EP), improving it could tighten the LVER constraints and propagate to $\theta$. The Bourgain optimization (`optimize_bourgain_large_value_estimate`) already exploits this, but there may be room for improvement with new EPs.

**Bottleneck 3: The coupling constraints (LVER).**

The Heath-Brown relations $s \leq f(\rho, \tau)$ couple the LV and energy projections through the $s$-coordinate. These are the constraints that make $\mathcal{P}$ a *genuine five-dimensional object* (not just a product of two three-dimensional objects). Improving these coupling constraints — proving tighter relationships between additive energy $s$ and large values $\rho$ — could tighten $\mathcal{P}$ in a way that affects *both* $A$ and $A^*$ simultaneously.

### 5.3 The Geometric Picture

Before Guth–Maynard, the master polytope $\mathcal{P}$ had a face in the $\rho$-direction determined by Huxley. The Guth–Maynard result *shaved off* a piece of $\mathcal{P}$ on this face, tightening the LV projection.

After incorporating Guth–Maynard, the polytope $\mathcal{P}$ has a new shape. The question is: which remaining face is now the *outermost* — the face whose tightening would most reduce $\theta$?

The geometric intuition: $\theta$ is the result of a sequence of projections and suprema applied to $\mathcal{P}$. Each projection discards some coordinates; each supremum takes the worst case over the remaining coordinates. The binding face of $\mathcal{P}$ is the face whose projection and supremum produce the current value of $\theta$.

After Guth–Maynard tightened the $\rho$-face, the binding face may have shifted to:
- The $\rho^*$-direction (energy estimates).
- The $s$-direction (coupling constraints).
- A different $\sigma$-slice of the $\rho$-face (where GM is not as tight).

---

## 6. The Computational Project

### 6.1 What Needs to Be Computed

To make this analysis rigorous, the following computational steps are needed:

1. **Fork the EXPDB repository** (https://github.com/teorth/expdb).

2. **Add the Guth–Maynard result** as a new hypothesis in `literature.py`. The hypothesis should be a `Large_Value_Estimate` or a direct LVER constraint, encoding the bound $A(\sigma) \leq 30(1-\sigma)/13$ (or the more precise form from the paper).

3. **Run `compute_best_lver`** to compute the updated master polytope $\mathcal{P}$.

4. **Run `compute_gap2`** to compute the updated $\theta$ and the optimal $\sigma^*$.

5. **Extract the binding constraints** at $\sigma^*$: which half-spaces of $\mathcal{P}$ are tight at the point where $\theta$ is achieved.

6. **Compute the dual variables** (sensitivities): for each binding constraint, how much $\theta$ would change if the constraint were tightened by $\varepsilon$.

7. **Rank the binding constraints by leverage** and identify the single most impactful next target.

### 6.2 Expected Output

The output would be a table:

| Rank | Binding Constraint | Source | Leverage ($\partial\theta/\partial b_i$) | Suggested Target |
|------|-------------------|--------|------------------------------------------|------------------|
| 1 | [most impactful] | [paper] | [value] | [specific analytical improvement needed] |
| 2 | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |

This table would be a *roadmap for the next improvement to $\theta$* — telling the analytic number theory community exactly where to focus.

### 6.3 Potential for a Publication

If executed, this analysis would constitute a legitimate computational contribution. The paper would be:

**Title:** "Binding Constraints and Next Bottlenecks in the EXPDB Prime Gap Pipeline After Guth–Maynard"

**Content:** A computational analysis identifying the binding constraints, their sensitivities, and the most impactful targets for further improvement.

**Venue:** arXiv:math.NT, potentially *Experimental Mathematics* or *Mathematics of Computation*.

---

## 7. Limitations

1. **This analysis is structural, not analytical.** It identifies *where* improvements are needed but cannot produce the improvements. Proving a tighter $A^*(\sigma)$ or a tighter coupling constraint requires new analytical ideas — not geometric reinterpretation.

2. **The exact binding constraints depend on the full EXPDB computation.** The analysis above is based on the pipeline structure and the known form of the Guth–Maynard result, but the precise binding set and sensitivities require running the code.

3. **The EXPDB pipeline has parameters** (truncation depth, $\tau_0$ selection, etc.) that affect the output. The binding constraints may be parameter-dependent.

4. **The Guth–Maynard result may interact with other recent results** (e.g., new exponent pairs, new additive energy bounds) that have been added to EXPDB since the EXPDB-Skyline paper was written. The full analysis should use the *current* EXPDB literature set, not the one from the paper.
