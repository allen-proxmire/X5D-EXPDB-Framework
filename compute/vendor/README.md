# Vendored Upstream

## `expdb/`

A clone of the upstream [Tao–Trudgian–Yang Analytic Number Theory
Exponent Database](https://github.com/teorth/expdb), pinned at commit
`af351a3`.

This is a full git clone (its own `.git` directory is preserved), not a
git submodule. It is vendored — rather than installed — because the
pipeline scripts in `compute/` apply a scipy-based replacement for the
`pycddlib` polytope backend, which removes the C-extension build
dependency.

The vendored code is **not modified for the X5D reinterpretation**. The
X5D-EXPDB perspective described in
[`../../examples/expdb/`](../../examples/expdb/) is purely descriptive:
it does not alter the upstream EXPDB code.

## Updating the vendor

To pull a newer version of upstream EXPDB:

```bash
cd compute/vendor/expdb
git fetch origin
git checkout <new-commit>
```

After updating, verify that the pipeline scripts in `compute/` still
run, and update the pinned commit hash above.
