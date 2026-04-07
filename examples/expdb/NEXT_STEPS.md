# EXPDB Bottleneck Analysis: What Needs to Happen Next

## What We Know (from the simplified analysis)

1. **θ = 17/30 = 0.5667** after Guth-Maynard (confirmed).
2. **Huxley is slack.** All pre-GM zero-density estimates are superseded.
3. **Sensitivity at the Ingham level:** d(θ)/d(A) = 1/A² ≈ 0.188.
4. **The density hypothesis target:** A = 2, θ = 1/2. Current gap: A - 2 ≈ 0.308.

## What We Don't Know (requires the full pipeline)

1. Whether α(σ) or β(σ) is binding at σ*.
2. The value of A*(σ*) and the ratio A*/A at σ*.
3. Which half-spaces of P are tight at the optimal point.
4. The dual variables (sensitivities) for each binding constraint.
5. Whether the bottleneck has shifted from LV to energy.

## The Concrete Project

### Step 1: Clone EXPDB

```bash
git clone https://github.com/teorth/expdb.git
cd expdb
pip install -r requirements.txt  # or equivalent
```

### Step 2: Verify the current state

Run the pipeline as-is to confirm the pre-existing θ value:

```python
from prime_gap import compute_gap2
# This should give θ = 7/12 with the current literature set
# (or whatever the latest value is after recent updates)
```

### Step 3: Add the Guth-Maynard hypothesis

In `literature.py`, add a new large value estimate:

```python
# Guth-Maynard (2024): N(σ,T) ≤ T^{30(1-σ)/13 + o(1)}
# This translates to: in the LV region R_LV ⊂ R³,
# the constraint ρ ≤ (30/13)(1-σ)τ
# (or equivalently, the zero-density exponent A(σ) ≤ (30/13)(1-σ))
#
# The exact form depends on how GM's Theorem 1.1 translates
# to EXPDB's hypothesis format. Check the paper for the precise
# large value estimate statement.
```

### Step 4: Rerun the pipeline

```python
from prime_gap import compute_gap2
# Rerun with the updated literature set
# Extract θ, σ*, and which function (α or β) is binding
```

### Step 5: Extract binding constraints

At the optimal σ*, identify which half-spaces of P are tight.
This requires modifying `compute_best_lver` or `compute_gap2`
to output the active constraints at the optimal point.

The key modification: after computing P and finding σ*, evaluate
each half-space constraint at the optimal 5-tuple and check which
ones have residual ≈ 0 (tight) vs. residual >> 0 (slack).

### Step 6: Sensitivity analysis

For each binding constraint i, perturb it by ε and recompute θ:

```python
for constraint in binding_constraints:
    theta_plus = compute_gap2(perturb(constraint, +epsilon))
    theta_minus = compute_gap2(perturb(constraint, -epsilon))
    sensitivity[constraint] = (theta_plus - theta_minus) / (2 * epsilon)
```

Rank by |sensitivity| to find the most impactful next target.

### Step 7: Write the report

The output should be:
- Updated θ and σ*.
- Table of binding constraints with sources and sensitivities.
- Whether α or β is binding (determines LV vs. energy bottleneck).
- The A*/A ratio at σ* (determines how close the energy side is to binding).
- Ranked list of next improvement targets.

## Why This Matters

The EXPDB pipeline is a *linear program* (or a sequence of polyhedral
operations that reduce to LP). LP duality theory guarantees that the
dual variables at the optimal point tell you exactly:
- Which constraints are binding (dual variable > 0).
- How much the objective (θ) would change if each constraint were
  relaxed by a small amount.
- Which constraints are irrelevant (dual variable = 0).

This is not speculation — it's standard LP sensitivity analysis applied
to a specific, computationally well-defined problem. The only missing
ingredient is running the actual code.

## Estimated Effort

- Cloning and understanding EXPDB: 2-4 hours.
- Adding the GM hypothesis: 1-2 hours (mostly translating the paper's
  statement into EXPDB's hypothesis format).
- Running the pipeline: minutes (it's a Python script).
- Extracting binding constraints: 2-4 hours (requires reading the code
  to find where to hook in the constraint-extraction logic).
- Sensitivity analysis: 2-4 hours (perturbation loop + ranking).
- Writing the report: 2-4 hours.

Total: roughly 1-2 days of focused work for someone comfortable
with Python and the EXPDB codebase.
