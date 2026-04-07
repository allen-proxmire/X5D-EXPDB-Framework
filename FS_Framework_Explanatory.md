# The Factor Skyline Framework: An Architectural Language for Dynamical Systems

**Allen Proxmire**

**April 2026**

---

## Table of Contents

**Chapter 1 — Why an Architectural Framework?**
- 1.1 The Missing Language
- 1.2 What Traditional Classifications Miss
- 1.3 The Structural Gap
- 1.4 What We Need

**Chapter 2 — What FS Is**
- 2.1 Systems as Architectures
- 2.2 Channels
- 2.3 Envelopes
- 2.4 Constraint Surfaces
- 2.5 Poles
- 2.6 The FS Criteria
- 2.7 Putting It Together

**Chapter 3 — Channels: The Building Blocks**
- 3.1 The Nine Channel Types
- 3.2 Local and Nonlocal
- 3.3 Stabilizing and Destabilizing
- 3.4 How Channels Combine
- 3.5 Why Channels Are Atomic

**Chapter 4 — Mode 1: Envelope Derivation**
- 4.1 What an Envelope Is
- 4.2 Forbidden Configurations
- 4.3 Necessary Configurations
- 4.4 Envelope Inequalities
- 4.5 Closed and Open Envelopes
- 4.6 Examples

**Chapter 5 — Mode 2: Extremal Dynamics**
- 5.1 What Extremal Means
- 5.2 The Ten Extremal Types
- 5.3 Universal Inequalities
- 5.4 Attractors
- 5.5 Why Extremal Dynamics Reveal the Skeleton

**Chapter 6 — Mode 3: Constraint Surface Geometry**
- 6.1 What a Constraint Surface Is
- 6.2 Faces and Closure
- 6.3 Five Surface Types
- 6.4 Dissipation Geometry
- 6.5 Why Geometry Is the Deepest Layer

**Chapter 7 — The FS Criteria**
- 7.1 Minimality
- 7.2 Locality
- 7.3 Determinism
- 7.4 Generative Sufficiency
- 7.5 Envelope Tightness
- 7.6 Structural Optimality
- 7.7 Why These Six

**Chapter 8 — The PDE Atlas**
- 8.1 The Idea of an Atlas
- 8.2 The Seven Poles
- 8.3 Why the Taxonomy Is Finite
- 8.4 Apex Architectures
- 8.5 The Summary Table

**Chapter 9 — FS Beyond PDEs**
- 9.1 A General Language
- 9.2 Physical Ontologies
- 9.3 Dynamical Systems
- 9.4 Geometry
- 9.5 Computation and Learning

**Chapter 10 — Implications and Future Directions**
- 10.1 What FS Enables
- 10.2 Reframing PDE Theory
- 10.3 Reframing Physical Modeling
- 10.4 Open Directions

**Chapter 11 — Closing Reflections**
- 11.1 The Core Insight
- 11.2 The Value of Architectural Thinking
- 11.3 The Future

---

# Chapter 1 — Why an Architectural Framework?

## 1.1 The Missing Language

Mathematics has powerful tools for analyzing individual systems. Given a partial differential equation, we can study its existence theory, derive energy estimates, classify its singularities, compute its long-time behavior. Given a geometric flow, we can prove curvature pinching estimates, identify blowup models, and construct surgery procedures. Given a conservation law, we can develop entropy solutions, prove contraction properties, and characterize shock dynamics.

What mathematics does not have — and what it needs — is a language for *comparing* these analyses across systems. A fluid dynamicist studying the Navier–Stokes equations and a geometric analyst studying Ricci flow both encounter the same structural phenomena: parabolic smoothing competing with nonlinear concentration, curvature-driven evolution producing finite-time singularities, monotone quantities controlling the approach to canonical forms. Yet the two communities have largely developed their tools in parallel, with limited exchange of structural insight.

This is not merely an organizational inconvenience. The absence of a common structural language means that deep analogies go unrecognized, that structural insights proven in one domain are not transferred to another, and that the reasons behind major open problems — like the regularity of three-dimensional Navier–Stokes solutions — are harder to isolate, because we lack the vocabulary to say precisely *what structural feature* of the Navier–Stokes architecture makes it harder than, say, the Burgers equation or the KdV equation, both of which share its nonlinear transport mechanism but are completely understood.

## 1.2 What Traditional Classifications Miss

The classical classification of PDEs into elliptic, parabolic, and hyperbolic types captures the *analytical character* of the principal symbol — whether the equation smooths, propagates, or oscillates. This is useful for selecting analytical tools (maximum principles for elliptic, energy estimates for parabolic, characteristics for hyperbolic) but tells us nothing about the *structural architecture* of the equation: how many independent mechanisms it has, how those mechanisms interact, what invariants constrain the dynamics, and what qualitative behaviors the architecture permits or forbids.

Consider: the heat equation, the Allen–Cahn equation, the Cahn–Hilliard equation, the porous medium equation, the thin-film equation, and the Fokker–Planck equation are all "parabolic." Yet their dynamics are qualitatively different — the heat equation smooths to uniformity, Allen–Cahn selects phases and annihilates interfaces, Cahn–Hilliard coarsens domains while conserving mass, the porous medium equation spreads with finite speed and free boundaries, the thin-film equation combines fourth-order smoothing with degenerate contact-line motion, and Fokker–Planck describes the drift and diffusion of probability densities toward Gibbs–Boltzmann equilibrium. Calling them all "parabolic" captures their shared analytical character but misses everything that makes them structurally distinct.

Similarly, the distinction between "integrable" and "non-integrable" captures whether the inverse scattering transform applies but does not explain *what structural features* produce integrability (the bi-Hamiltonian structure, the Lax pair, the infinite conservation laws) or how integrability relates to other closure mechanisms (the viscosity-solution framework for Hamilton–Jacobi, the Perelman monotonicity for Ricci flow, the Kruzkov entropy framework for conservation laws).

## 1.3 The Structural Gap

The gap is between *analytical classification* (what tools apply) and *structural classification* (what the architecture is). The analytical classification tells us *how to study* a system; the structural classification tells us *what the system is* — what mechanisms it has, how they interact, what they can and cannot produce.

Bridging this gap requires a framework that can:

1. **Decompose** any system into its constituent mechanisms — the independent dynamical channels that drive the evolution.
2. **Derive** the structural constraints that the system's axioms impose — the envelope of admissible states and evolutions.
3. **Construct** the geometric object that encodes all channel relationships — the constraint surface.
4. **Compare** the results across systems — identifying shared structures, structural analogies, and structural hierarchies.
5. **Evaluate** the structural quality of each system — measuring its minimality, locality, determinism, and other architectural properties.

## 1.4 What We Need

We need an *architectural language* — a set of concepts and methods that can express the structural properties of any dynamical system in a common vocabulary, enabling comparison, classification, and insight across domains.

The Factor Skyline Framework is this language. It was developed not as an abstract theoretical exercise but as a practical tool for understanding the structural relationships among the major nonlinear PDEs of mathematical physics — and, more broadly, for understanding what makes some mathematical structures simple, some complex, some well-behaved, some pathological, some integrable, some turbulent, some tractable, and some open.

The name "Factor Skyline" comes from the framework's origin in the study of the multiplicative structure of the integers — the "skyline" of prime factorization — but the framework itself is general: it applies to any system that can be decomposed into interacting channels with definite structural properties.

---

# Chapter 2 — What FS Is

## 2.1 Systems as Architectures

The central idea of FS is simple: every dynamical system is an *architecture* — a structured composition of channels, conservation laws, symmetries, and constraints. The architecture determines what the system can do (its dynamical repertoire), what it cannot do (its forbidden configurations), and how it behaves at its structural limits (its extremal dynamics).

An architecture is not the same as a solution. A solution is a specific trajectory — a particular evolution from particular initial data. An architecture is the *structural framework* that generates all possible trajectories — the rules of the game, not any particular play. The FS framework analyzes architectures, not solutions.

An architecture is also not the same as an equation. An equation is a symbolic representation — a formula written in a specific coordinate system with specific notation. An architecture is the *structural content* of the equation — the channels, invariants, and constraints that persist regardless of how the equation is written. Two different-looking equations can have the same architecture (as when the Allen–Cahn equation is written in various normalizations), and two similar-looking equations can have different architectures (as when the Burgers equation and the KdV equation differ by a single dispersive term but have qualitatively different dynamics).

## 2.2 Channels

A *channel* is an independent dynamical mechanism within a system. It is characterized by four properties:

- **Locality:** Does the channel depend only on the state at each point (local), or does it couple distant points through an integral operator or a global equation (nonlocal)?
- **Linearity:** Is the channel linear in the state, quasilinear (linear in the highest derivatives with state-dependent coefficients), or fully nonlinear?
- **Stability role:** Does the channel stabilize the dynamics (smooth, spread, damp), destabilize them (steepen, concentrate, amplify), or is it neutral (a symmetry or constraint)?
- **Scale action:** How does the channel's effect depend on the spatial scale? Does it act preferentially on small scales (like diffusion, which damps high wavenumbers fastest) or on large scales (like nonlocal aggregation, which amplifies long-wavelength perturbations)?

The channels are the *atomic units* of the architecture — the irreducible building blocks from which the dynamics are constructed. Every qualitative feature of the system (smoothing, steepening, soliton formation, blowup, convergence to equilibrium) can be traced to the interaction of specific channels.

## 2.3 Envelopes

An *envelope* is the maximal set of constraints that the system's axioms impose on all admissible states and evolutions. It is the boundary of the structurally possible — everything inside is consistent with the axioms; everything outside violates at least one.

The envelope is derived through three steps:

1. **Forbidden configurations:** What the system *cannot* do. For example, the Allen–Cahn equation cannot increase its free energy (the gradient-flow structure forbids it). The incompressible Navier–Stokes equations cannot have compressible velocity fields (the divergence-free constraint forbids it). The Hamilton–Jacobi equation cannot smooth (the absence of diffusion forbids it).

2. **Necessary configurations:** What the system *must* do. For example, the porous medium equation must have finite-speed propagation (the degeneracy at $u = 0$ forces it). The KdV equation must have infinitely many conservation laws (the bi-Hamiltonian structure forces it). The Keller–Segel system must blow up when the mass exceeds $8\pi$ (the free-energy analysis forces it).

3. **Envelope inequalities:** The quantitative bounds that define the boundary of the envelope — energy inequalities, contraction properties, decay estimates, blowup criteria. These are the sharp, irreducible bounds that cannot be improved.

## 2.4 Constraint Surfaces

A *constraint surface* is the geometric object in channel space that encodes all structural relationships among the channels. Think of it this way: at each instant, the system's state determines how active each channel is — how much diffusion is happening, how much steepening, how much curvature concentration. The set of all possible channel-activity states, subject to the system's structural constraints, forms a geometric object — the constraint surface.

The constraint surface's properties determine the system's qualitative behavior:

- A **closed** surface (all faces sealed) means the dynamics cannot escape — the system is globally well-posed.
- An **open** surface (one or more faces unsealed) means the dynamics might escape — the system may develop singularities or have open well-posedness questions.
- A **contracting** surface means the dynamics shrink toward a lower-dimensional attractor — the system converges to equilibrium.
- An **isoenergetic** surface means the dynamics circulate on a fixed-dimensional level set — the system is Hamiltonian, with no convergence but no escape.

## 2.5 Poles

A *structural pole* is a qualitatively distinct region of the architectural space where specific channel combinations dominate. Systems near the same pole share qualitative features — they have the same type of smoothing, the same type of singularity, the same type of long-time behavior.

The PDE Atlas reveals seven poles:

- **Diffusive:** Dominated by parabolic smoothing. Systems smooth, spread, and converge to equilibria. (Fokker–Planck, porous medium, Allen–Cahn, Cahn–Hilliard.)
- **Hyperbolic:** Dominated by first-order nonlinear transport. Systems steepen and form shocks. (Hamilton–Jacobi, Burgers.)
- **Dispersive:** Dominated by oscillatory spreading. Systems oscillate, form solitons, and conserve energy. (Nonlinear Schrödinger, KdV.)
- **Geometric:** Dominated by curvature-driven evolution. Systems smooth geometrically but develop curvature singularities. (Mean curvature flow, Ricci flow.)
- **Aggregation:** Dominated by nonlocal self-attraction. Systems concentrate mass. (Keller–Segel.)
- **Fluid:** Complex multi-channel architecture with nonlocal pressure and open regularity. (Navier–Stokes.)
- **Integrable:** Maximum structural resources — infinite conservation laws, exact solvability. (KdV as the apex.)

The poles are not rigid categories — they are *tendencies*. A system can have features of multiple poles (KdV has both dispersive and hyperbolic features). But the dominant pole determines the qualitative character.

## 2.6 The FS Criteria

FS evaluates each architecture against six criteria:

1. **Minimality:** Are the axioms irreducible? Is the architecture the simplest that generates its dynamics?
2. **Locality:** Are all channels local? Is the architecture free of nonlocal operators?
3. **Determinism:** Is the evolution globally well-posed? Are solutions unique?
4. **Generative Sufficiency:** Does the architecture generate all its observed phenomena from the axioms?
5. **Envelope Tightness:** Are the envelope bounds sharp? Is the envelope fully closed?
6. **Structural Optimality:** Is the architecture free of anomalies? Is it the most economical system for its dynamics?

Each criterion receives a verdict: PASS, CONDITIONAL, or FAIL. The number of PASSes is the FS score, ranging from 0 to 6.

## 2.7 Putting It Together

The FS analysis of a system follows a workflow:

1. **Identify the axioms** — the structural commitments that define the architecture.
2. **Decompose into channels** — the independent mechanisms driving the dynamics.
3. **Derive the envelope** (Mode 1) — the forbidden and necessary configurations, the envelope inequalities.
4. **Identify the extremal dynamics** (Mode 2) — the behaviors at the boundary of the envelope.
5. **Construct the constraint surface** (Mode 3) — the geometric object encoding channel relationships.
6. **Evaluate the FS criteria** — the six-criterion assessment of structural quality.
7. **Assign to a pole** — the structural classification within the atlas.

The output is an *atlas entry* — a complete structural profile that can be compared with any other entry.

---

# Chapter 3 — Channels: The Building Blocks

## 3.1 The Nine Channel Types

Across the sixteen PDEs evaluated in the atlas, nine fundamental channel types appear. Every PDE is a composition of channels drawn from this finite set.

**Diffusion.** The spreading of a quantity through amplitude decay. The Laplacian $\Delta u$ and its relatives — nonlinear diffusion $\Delta(u^m)$, biharmonic $-\Delta^2 u$, the Lichnerowicz Laplacian. Diffusion damps high-wavenumber modes at rate $k^2$ (or $k^4$ for biharmonic), preferentially smoothing small-scale features. It is the universal stabilizer — the channel that prevents infinitely sharp structures from persisting. Every parabolic PDE has a diffusion channel.

**Dispersion.** The spreading of a quantity through phase interference — different frequency components traveling at different speeds, so that their superposition averages out. The Schrödinger operator $i\partial_t + \Delta$ and the KdV dispersive term $u_{xxx}$. Dispersion reduces the amplitude $\|u\|_{L^\infty}$ without reducing the mass $\|u\|_{L^2}$ — it spreads without dissipating. The mechanism is *oscillatory*, not *decaying*: the amplitude decreases because the wave components dephase, not because energy is lost.

**Transport.** The movement of a quantity along its own gradient. The self-advection $u\partial_x u$ in Burgers, the Hamiltonian transport $H(\nabla u)$ in Hamilton–Jacobi, the advective nonlinearity $(\mathbf{u} \cdot \nabla)\mathbf{u}$ in Navier–Stokes. Transport steepens gradients — fast regions outrun slow regions, compressing the profile. Without a counterbalancing mechanism (diffusion or dispersion), transport produces shocks in finite time. It is the universal destabilizer for first-order dynamics.

**Curvature.** The geometric evolution driven by the curvature of a surface or a metric. Mean curvature $V_n = H$ for surfaces, Ricci curvature $\partial_t g = -2\,\text{Ric}$ for metrics. Curvature channels are *dual-natured*: they smooth at low curvature (the "heat equation for shapes") but concentrate at high curvature (the quadratic reaction $\text{Rm} \ast \text{Rm}$ can overwhelm the Laplacian smoothing). This duality produces the characteristic dynamics of geometric flows: smoothing → concentration → singularity → topology change.

**Aggregation.** The nonlocal self-attraction of a density field through a global potential. The chemotactic drift $-\nabla \cdot (u \nabla v)$ in Keller–Segel, where $v = (-\Delta)^{-1}u$ is the chemoattractant determined by a Poisson equation. Aggregation is *nonlocal* (the potential at one point depends on the density everywhere) and *destabilizing* (the positive feedback loop: more density → stronger signal → more drift → more density). It is the only channel type that can drive *mass-concentrating blowup* — the density itself collapsing into a Dirac delta.

**Pressure.** The nonlocal constraint enforcement in incompressible fluid dynamics. The pressure Poisson equation $\Delta p = -\partial_i\partial_j(u_iu_j)$ in Navier–Stokes. Pressure is nonlocal (the Poisson solve couples all points) but *energy-neutral* (pressure does no work on a divergence-free velocity field). Its role is not to drive the dynamics but to enforce the incompressibility constraint — it pushes the fluid apart when it tries to compress. Structurally, pressure is a Lagrange multiplier, not a force.

**Reaction.** The local, zeroth-order nonlinear transformation of a field. The double-well potential $\phi - \phi^3$ in Allen–Cahn, the general kinetics $\mathbf{R}(\mathbf{u})$ in reaction–diffusion systems. Reaction acts at each point independently of spatial structure — it is *scale-free* (no spatial derivatives). Its stability role depends entirely on the specific kinetics: monostable (convergent), bistable (switching), oscillatory (limit cycles), excitable (threshold-dependent), or chaotic.

**Conservation.** The preservation of a total quantity — mass, probability, energy, momentum. Enforced by the divergence-form structure of the PDE ($\partial_t u = -\nabla \cdot \mathbf{J}$) and no-flux boundary conditions. Conservation is a *constraint*, not a force — it restricts the dynamics to a hyperplane in function space without determining the trajectory on that hyperplane.

**Gauge.** The invariance of the system under a symmetry group — phase rotation $\psi \to e^{i\theta}\psi$ in NLS, diffeomorphism invariance in Ricci flow, tangential reparametrization in mean curvature flow. Gauge symmetries generate conservation laws (via Noether's theorem) and introduce redundancies that must be managed (via gauge-fixing tricks like DeTurck for Ricci flow).

## 3.2 Local and Nonlocal

The locality axis is the sharpest structural divide in the atlas. Of the sixteen evaluated architectures, twelve are *fully local* — every channel depends only on the state and its derivatives at each point. Two have nonlocal channels: Navier–Stokes (one nonlocal channel: pressure) and Keller–Segel (two nonlocal channels: aggregation and potential).

The crucial distinction is the *role* of the nonlocality. In Navier–Stokes, the pressure is a *constraint-enforcement mechanism* — it keeps the velocity divergence-free but does no work. It is a structural inconvenience, not a dynamical driver. In Keller–Segel, the chemoattractant is a *driving mechanism* — it creates the long-range attraction that produces mass concentration. The same mathematical object (a Poisson equation) serves opposite dynamical purposes: repulsion in NS, attraction in KS.

## 3.3 Stabilizing and Destabilizing

Every channel has a stability role — it either helps the system stay smooth and well-behaved, or it drives the system toward singularity and complexity:

- **Unconditionally stabilizing:** Diffusion, dispersion, conservation.
- **Unconditionally destabilizing:** Transport (steepening), aggregation (concentration).
- **Dual-natured:** Curvature (smoothes at low values, concentrates at high values).
- **Constitutive-dependent:** Reaction (depends on the specific kinetics).
- **Neutral:** Pressure, gauge (structural constraints, not forces).

The *fundamental tension* of every PDE is the competition between its stabilizing and destabilizing channels. The outcome of this competition — whether the stabilizing channels can control the destabilizing ones for all time — is the system's *well-posedness question*. When the stabilizing channels win unconditionally (as in Allen–Cahn, PME, Fokker–Planck), the system is globally well-posed. When the destabilizing channels can win for some data (as in focusing NLS, Keller–Segel, or Navier–Stokes in 3D), the system may blow up.

## 3.4 How Channels Combine

Channels do not act independently — they interact through several mechanisms:

**Balance.** Two opposing channels reach equilibrium at a specific scale, producing a coherent structure. Diffusion balances reaction at the Allen–Cahn interface width $\varepsilon$. Dispersion balances advection at the KdV soliton. Diffusion balances aggregation at the Keller–Segel critical mass $8\pi$.

**Competition.** Two opposing channels compete across a range of scales, with the outcome determined by a control parameter. Viscosity competes with advection in NS (controlled by the Reynolds number). Diffusion competes with aggregation in KS (controlled by the total mass).

**Cooperation.** Two channels with the same tendency reinforce each other. The diffusion and conservation channels in PME cooperate to produce self-similar spreading.

**Nullity.** A channel contributes nothing to a specific accounting. The advection and pressure channels in NS are both *energy-null* — they do zero net work in the energy budget, despite driving the entire nonlinear dynamics. The free energy in NS is controlled by a two-channel accounting (viscous dissipation minus forcing power), even though the system has five channels.

## 3.5 Why Channels Are Atomic

The channels are the *irreducible building blocks* of the FS framework because:

1. **Finiteness.** The number of qualitatively distinct channel types is *finite* — approximately nine. This means the space of possible architectures is finite-dimensional (at least at the qualitative level), enabling a finite taxonomy.

2. **Universality.** The same channel types appear across different domains — diffusion in heat transfer, in probability (Fokker–Planck), in geometry (Lichnerowicz Laplacian); transport in fluid mechanics, in traffic flow, in conservation laws; curvature in surface evolution and in Ricci flow. The channels are *domain-independent structural units*.

3. **Independence.** Each channel has a definite structural character (locality, linearity, stability, scale action) that is independent of the other channels. The diffusion channel is stabilizing regardless of what reaction channel accompanies it. The transport channel is destabilizing regardless of whether diffusion or dispersion provides the counterbalance. This independence is what makes the decomposition meaningful — the channels are genuinely atomic, not artificially separated.

---

# Chapter 4 — Mode 1: Envelope Derivation

## 4.1 What an Envelope Is

Imagine you are given a PDE — say, the porous medium equation $\partial_t u = \Delta(u^m)$ with $m > 1$ — and asked: "What can this equation do? What are the limits of its behavior?" The envelope is the answer to this question. It is the complete catalog of structural constraints — the things the equation *must* do, the things it *cannot* do, and the quantitative bounds that separate the possible from the impossible.

The envelope is not a single number or a single inequality. It is a *system* of constraints — typically 9 to 12 for the PDEs in the atlas — that together define the boundary of the architecture's dynamical repertoire. Some constraints are equalities (conservation laws — exact, inviolable), some are one-sided inequalities (energy bounds — the energy can decrease but not increase), and some are conditional (regularity criteria — the solution is smooth as long as a specific quantity stays bounded).

The power of the envelope is that it applies to *every* solution of the PDE, not just to specific initial data or specific parameter values. The envelope is *architectural* — it holds because of the structure of the equation, not because of any particular trajectory.

## 4.2 Forbidden Configurations

The first step in deriving the envelope is identifying what the architecture *cannot* do. These are the *forbidden configurations* — states or behaviors that violate the axioms.

For the porous medium equation, the forbidden configurations include: negative densities (the maximum principle prevents them), nonlocal coupling (the equation is local — no Poisson equation, no integral operators), infinite-speed propagation (the degeneracy at $u = 0$ enforces finite speed), and blowup (the combination of mass conservation and diffusion prevents concentration).

For the Navier–Stokes equations, the forbidden configurations include: compressible velocity fields (the divergence-free constraint prohibits them), non-Newtonian stress (the constitutive law selects linear viscosity), and anisotropic viscosity (the isotropy axiom forbids it).

Each forbidden configuration is traceable to a specific axiom — a specific structural commitment that excludes the behavior. The forbidden configurations define the *exterior* of the envelope: the region of state space that the system can never access.

## 4.3 Necessary Configurations

The second step identifies what the architecture *must* do — structures that are forced into existence by the axioms.

For the KdV equation, the necessary configurations include: infinitely many conservation laws (forced by the bi-Hamiltonian structure through the Lenard recursion), soliton solutions (forced by the balance between advection and dispersion), elastic soliton collisions (forced by the integrability and the infinite conservation laws), and global smooth solutions (forced by the infinite conservation laws controlling every Sobolev norm).

For the Keller–Segel system, the necessary configurations include: mass conservation (forced by the divergence-form structure), free-energy dissipation (forced by the Wasserstein gradient-flow structure), the critical mass $M_c = 8\pi$ (forced by the logarithmic Hardy–Littlewood–Sobolev inequality), and blowup for supercritical mass (forced by the unboundedness of the free energy below $M > 8\pi$).

The necessary configurations define the *interior structure* of the envelope: the features that every admissible evolution must exhibit.

## 4.4 Envelope Inequalities

The third step derives the quantitative bounds — the sharp, irreducible inequalities that define the precise boundary of the envelope.

These come in several flavors:

- **Conservation identities:** Exact equalities that hold for all solutions. Mass conservation $\int u \, dx = M$. Energy conservation $H[\psi(t)] = H[\psi_0]$. Exact, inviolable, tight.

- **Dissipation identities:** The rate of energy decrease. $dF/dt = -M\|\mu\|^2$ for Allen–Cahn. $dA/dt = -\int H^2 \, dS$ for mean curvature flow. Exact for smooth solutions.

- **Contraction inequalities:** Bounds on how far apart two solutions can be. $\|u(t) - v(t)\|_{L^1} \leq \|u_0 - v_0\|_{L^1}$ for porous medium. $\|v(t) - w(t)\|_{L^\infty} \leq \|v_0 - w_0\|_{L^\infty}$ for Hamilton–Jacobi. These are the strongest stability estimates.

- **Regularity bounds:** Estimates on derivatives. The Shi estimates for Ricci flow ($|\nabla^k \text{Rm}| \leq C|\text{Rm}|/t^{k/2}$). The Strichartz estimates for NLS. The Oleinik bound $\partial_x v \leq 1/t$ for Burgers.

- **Blowup criteria:** Conditions under which singularity occurs. The virial identity for focusing NLS ($V''(t) = 8H$ — if $H < 0$, the variance reaches zero in finite time). The critical mass $M = 8\pi$ for Keller–Segel.

## 4.5 Closed and Open Envelopes

An envelope is *closed* if every face of the constraint surface is sealed — the dynamics cannot escape in any direction. An envelope is *open* if one or more faces are unsealed — the dynamics might escape through an uncontrolled direction.

The closed envelopes are the structurally sound architectures — the systems where we can prove that smooth solutions exist globally, are unique, and behave predictably. The Fokker–Planck equation, the porous medium equation, the Allen–Cahn equation, the KdV equation — all have closed envelopes.

The open envelopes are the structurally challenging architectures — the systems where blowup may occur, well-posedness is conditional, or the long-time behavior is unknown. The three-dimensional Navier–Stokes equations have an open enstrophy face. The focusing NLS in dimension two or higher has an open collapse face. The Keller–Segel system has an open blowup face for supercritical mass.

The *degree* of openness matters. The NLS focusing collapse face is *sharp*: the exact threshold mass $M_* = \|Q\|_{L^2}^2$ is known, the blowup rate is characterized, and the blowup profile is identified. The NS enstrophy face is *unresolved*: we do not know whether smooth solutions exist globally, what the threshold is, or what the blowup profile would look like. The KS blowup face is *well-characterized*: the threshold $M = 8\pi$ is exact, the blowup rate is bounded, and the concentrated mass is quantized at $8\pi$.

## 4.6 Examples

**The PME envelope** is the tightest of any nonlinear PDE in the atlas. Ten unconditional inequalities, all sharp, sealed by four independent mechanisms (degeneracy, entropy dissipation, $L^1$ contraction, mass conservation). The envelope is fully closed — no open faces, no conditional estimates, no unresolved questions. The Barenblatt profile saturates every bound.

**The NLS envelope** depends on the sign of the nonlinearity. For the defocusing case, the positive-definite energy controls the $H^1$ norm unconditionally — the envelope is fully closed. For the focusing case in dimension two, the critical mass $M_* = \|Q\|_{L^2}^2$ provides a sharp bifurcation: below $M_*$, the envelope is closed (global existence + scattering); above $M_*$, the envelope has an open collapse face (blowup is possible and the dynamics are partially characterized).

**The KS envelope** is mass-bifurcated: fully closed for $M < 8\pi$ (global existence, steady-state convergence), open for $M > 8\pi$ (finite-time mass-concentrating blowup with quantized mass at $8\pi$). The threshold $8\pi$ is determined by the best constant in the logarithmic Hardy–Littlewood–Sobolev inequality — the deepest variational characterization of any blowup threshold in the atlas.

---

# Chapter 5 — Mode 2: Extremal Dynamics

## 5.1 What Extremal Means

Mode 2 asks: "What does the architecture *do* at its structural limits?" The extremal dynamics are the behaviors at the *boundary* of the envelope — the most extreme states that the architecture can reach. They are not the generic or typical behaviors (which might be boring — most solutions of most PDEs eventually settle down) but the *limiting* behaviors that reveal the architecture's true character.

If the envelope is a box, the extremal dynamics are what happens when the system pushes against the walls of the box. Does it bounce back (stable equilibrium)? Does it break through (blowup)? Does it slide along the wall (shock propagation)? Does it settle into a corner (soliton formation)?

## 5.2 The Ten Extremal Types

Across the atlas, ten fundamental types of extremal behavior appear:

1. **Diffusive spreading.** The system smooths and spreads — amplitude decays, support expands, the density approaches a universal profile. The Barenblatt profile of PME, the Gibbs–Boltzmann of FP, the flat-film attractor of TFE.

2. **Shock formation.** Gradients steepen until the solution develops a discontinuity. The entropy/viscosity framework selects the unique physical continuation. The Burgers shock, the HJ gradient kink.

3. **Soliton formation.** Dispersion and nonlinearity reach a balance, producing localized, shape-preserving traveling waves. The KdV sech$^2$ soliton, the NLS complex sech soliton.

4. **Scattering.** The nonlinear solution approaches a free linear solution as $t \to \infty$. The nonlinearity "turns off" because the dispersive spreading reduces the amplitude. Defocusing NLS scattering.

5. **Amplitude concentration (blowup).** The solution concentrates at a point — the amplitude grows without bound. The focusing NLS collapse, where $\|\nabla \psi\| \to \infty$.

6. **Mass concentration (blowup).** The density itself concentrates into a Dirac delta. The Keller–Segel blowup, where $u \to M_0 \delta(x - x_0)$ with $M_0 \geq 8\pi$.

7. **Interface dynamics.** Diffuse interfaces between phases move according to geometric laws — mean curvature for Allen–Cahn, surface diffusion for Cahn–Hilliard. The interfaces can shrink (AC extinction), merge (CH coarsening), or develop contact-line motion (TFE).

8. **Curvature blowup.** The curvature of a surface or metric grows without bound at a point. The MCF neckpinch, the RF Type I singularity. The blowup profile is a self-similar shrinker (round sphere, round cylinder).

9. **Topology change.** The singularity changes the connectivity of the domain. MCF neckpinch splits a surface into two components. RF surgery simplifies the connected-sum decomposition of a 3-manifold.

10. **Extinction.** The state variable ceases to exist. MCF surfaces shrink to round points. AC interfaces vanish. The architecture reaches its terminal state.

## 5.3 Universal Inequalities

Each architecture has a set of *universal inequalities* — quantitative bounds that hold for every admissible solution. These are the architecture's "laws of physics" — the inviolable structural constraints that no trajectory can escape.

The universal inequalities fall into natural categories:

- **Conservation laws** (exact): mass, energy, momentum. These are the strongest constraints — they hold with equality for all time.
- **Contraction properties** (monotone): $L^1$ contraction for PME and Burgers, $L^\infty$ contraction for HJ and Burgers, Wasserstein contraction for FP. These ensure that nearby solutions stay nearby.
- **Dispersive/smoothing estimates** (decay): the Airy decay $t^{-1/3}$ for KdV, the Schrödinger decay $t^{-d/2}$ for NLS, the parabolic smoothing $t^{-k/2}$ for heat-type equations. These ensure that amplitudes decrease over time.
- **Monotone functionals** (Lyapunov/Perelman): the free-energy decrease for AC/CH, the Perelman W-entropy increase for Ricci flow, the area decrease for MCF. These ensure that the system moves in a definite direction.
- **Threshold conditions** (bifurcation): the critical mass $8\pi$ for KS, the critical NLS mass $M_*$, the Fujita exponent for reaction–diffusion blowup. These identify the precise boundaries between global existence and singularity formation.

## 5.4 Attractors

The *attractor* of a system is the long-time state to which generic solutions converge. The atlas reveals six qualitatively distinct attractor types:

- **Fixed-point attractors:** A single steady state. The Gibbs–Boltzmann equilibrium (FP), the uniform phases $\pm 1$ (AC), the radial steady state (KS subcritical).
- **Self-similar attractors:** A one-parameter family of profiles. The Barenblatt profile (PME), the N-wave (Burgers), the source-type profile (TFE).
- **Soliton resolution:** Decomposition into persistent coherent structures plus dispersing radiation. The KdV soliton resolution, the NLS 1D soliton resolution.
- **Scattering:** Approach to a free linear solution. The defocusing NLS scattering.
- **Geometric attractors:** Convergence to canonical geometric forms. The round sphere (MCF extinction), the Einstein metric (RF long-time), the Thurston geometric decomposition (RF with surgery).
- **Singular attractors:** Blowup as the terminal state. The Dirac delta (KS supercritical), the round point (MCF convex extinction).

## 5.5 Why Extremal Dynamics Reveal the Skeleton

The extremal dynamics are the architectural *skeleton* of the system — the structural bones that support all the other behaviors. The generic behavior (what most solutions do most of the time) can be complicated and hard to describe, but the extremal behavior (what happens at the limits) is typically *simple and universal*: a few canonical blowup profiles, a few self-similar attractors, a few soliton solutions.

This is because the extremal dynamics are controlled by the *structural channels* — the stabilizing and destabilizing mechanisms that define the architecture. At the limits, the competition between channels resolves into a simple outcome: one channel wins, and the dynamics approach a canonical form dictated by that channel. The Burgers shock is the canonical outcome when transport wins over nothing. The KdV soliton is the canonical outcome when transport and dispersion are balanced. The Barenblatt profile is the canonical outcome when nonlinear diffusion wins over everything.

The extremal dynamics are where the architecture's *true character* is revealed — where the structural channels show their hand and the constraint surface's geometry becomes visible.

---

# Chapter 6 — Mode 3: Constraint Surface Geometry

## 6.1 What a Constraint Surface Is

The constraint surface is the *deepest structural object* in the FS analysis. It is the geometric object in channel space that encodes *all* structural relationships among the channels — not just the individual channel properties (which Mode 1 derives) and the extremal behaviors (which Mode 2 identifies) but the *geometry of how the channels interact*.

Think of it this way. Each channel has a "dial" — a level of activity at each point in space and time. The diffusion dial measures how much smoothing is happening. The transport dial measures how much steepening. The curvature dial measures how much geometric evolution. The set of all possible dial settings, subject to the system's structural constraints, forms a geometric object — the constraint surface.

The constraint surface is the *phase portrait of the architecture* — the map of all possible dynamical states, organized by their channel activities.

## 6.2 Faces and Closure

The constraint surface has *faces* — codimension-1 boundaries that the dynamics can potentially approach. Each face corresponds to a specific structural limit — a direction in which a channel is pushed to its extreme.

A face is *sealed* if a structural mechanism prevents the dynamics from crossing it. The free-energy monotonicity seals the oscillatory face of AC/CH (the dynamics cannot oscillate because the free energy can only decrease). The $L^1$ contraction seals the chaotic face of Burgers (the dynamics cannot exhibit sensitive dependence because $L^1$ distances decrease). The infinite conservation laws of KdV seal the blowup face (every Sobolev norm is bounded for all time).

A face is *open* if no known mechanism prevents crossing. The NS enstrophy face is open — we do not know whether the vortex stretching can overwhelm the viscous damping in 3D. The NLS focusing collapse face is open in dimensions three and higher — we know blowup occurs for large data but do not have a complete classification for all initial conditions.

The *closure* of the constraint surface — whether all faces are sealed — is the primary structural diagnostic. A fully closed surface means the architecture is structurally sound: globally well-posed, predictable, controllable. An open surface means the architecture has unresolved structural questions.

## 6.3 Five Surface Types

The atlas reveals five qualitatively distinct constraint-surface geometries:

**Contracting (Lyapunov).** The surface contracts over time — the dynamics descend a Lyapunov functional toward an attractor. The free-energy decrease of AC/CH, the entropy dissipation of PME, the linear spectral decay of FP. Contracting surfaces produce convergence to equilibrium. They are the *simplest* surface type and the hallmark of the diffusive pole.

**Isoenergetic (Hamiltonian).** The surface has fixed dimension — the dynamics circulate on a level set of the conserved quantities without contracting or expanding. The energy-momentum level sets of NLS, the infinite-dimensional tori of KdV. Isoenergetic surfaces produce solitons, quasi-periodic orbits, and scattering. They are the hallmark of the dispersive pole.

**Entropy-resolved (hyperbolic).** The surface develops folds (characteristic crossings) that are resolved by an entropy/viscosity selection principle. The Burgers shock surface, the HJ kink surface. The resolution introduces irreversibility: information is lost at shocks, and the surface simplifies over time. The hallmark of the hyperbolic pole.

**Geometrically dissipative.** The surface contracts through a *geometric* mechanism — area decrease (MCF), curvature decrease (RF) — rather than through a scalar Lyapunov functional. Geometrically dissipative surfaces produce curvature singularities that are required for the architecture's topological program (MCF genus reduction, RF geometrization). The hallmark of the geometric pole.

**Mass-stratified.** The surface's topology depends on a conserved scalar (the total mass $M$ for KS). Below a threshold ($M < 8\pi$), the surface is contracting (global existence). Above the threshold ($M > 8\pi$), the surface has an open blowup face. The surface is *stratified*: each mass value determines a different constraint-surface geometry. The hallmark of the aggregation pole.

## 6.4 Dissipation Geometry

The *dissipation geometry* of the constraint surface describes how energy, entropy, or free energy is distributed and consumed across the channels. Different architectures have qualitatively different dissipation geometries:

- **Volumetric dissipation:** Energy is dissipated everywhere in the domain, at a rate determined by the local state. All parabolic architectures (FP, PME, AC, CH, TFE) and MCF have volumetric dissipation.
- **Zero dissipation:** No energy is lost — the Hamiltonian structure preserves energy exactly. NLS and KdV have zero dissipation.
- **Shock-concentrated dissipation:** Energy is dissipated only at shocks — a set of measure zero in space. Between shocks, energy is exactly conserved. Burgers has this unique dissipation mode.
- **Nonlocal dissipation:** The dissipation rate at each point depends on the global state (through a nonlocal potential). KS has the only nonlocal dissipation in the atlas.

The dissipation geometry determines the *direction* of the dynamics on the constraint surface: volumetrically dissipative systems flow "downhill" everywhere; Hamiltonian systems flow on level sets; shock-concentrated systems flow on level sets between shocks and lose energy at shocks.

## 6.5 Why Geometry Is the Deepest Layer

The constraint surface is the deepest layer of the FS analysis because it captures *all* structural relationships simultaneously — not just the individual channel properties (Mode 1) or the extremal behaviors (Mode 2) but the *full geometry of channel interactions*. The closure, dimensionality, and singularity structure of the constraint surface determine the system's qualitative character more completely than any individual inequality or any individual extremal behavior.

The constraint surface is where the *poles* become visible. Systems at the same pole have qualitatively similar constraint-surface geometries: contracting surfaces at the diffusive pole, isoenergetic surfaces at the dispersive pole, entropy-resolved surfaces at the hyperbolic pole. The constraint-surface geometry is the *defining structural feature* of each pole — the geometric property that makes diffusive systems smooth, dispersive systems oscillate, and hyperbolic systems steepen.

---

# Chapter 7 — The FS Criteria

## 7.1 Minimality

Minimality asks: *Is this architecture the simplest it can be?*

An architecture is minimal if its axioms are irreducible — each axiom is independent (not derivable from the others), and each is necessary (removing it changes the qualitative architecture). Non-minimal elements include: constitutive selections (choosing a specific free-energy potential when any double-well would work), geometric restrictions (restricting to Euclidean space when the PDE could be formulated on manifolds), and redundant axioms (axioms that are consequences of others).

The architectures with the strongest minimality are those with zero constitutive parameters and zero non-minimal axioms: Hamilton–Jacobi, Burgers, MCF, KdV, and Ricci flow all have *zero adjustable parameters* — the equation itself has no coefficients to choose. The architectures with the weakest minimality are those with multiple constitutive selections: Allen–Cahn and Cahn–Hilliard each have three non-minimal axioms (specific free energy, specific mobility, Euclidean geometry).

## 7.2 Locality

Locality asks: *Is everything local?*

An architecture passes locality if every channel depends only on the state and its derivatives at each point. This is the *strongest form of structural locality* — no integral operators, no global solves, no coupling between distant points.

Twelve of the sixteen evaluated architectures are fully local. Navier–Stokes has one nonlocal channel (pressure — a constraint mechanism). Keller–Segel has two nonlocal channels (aggregation and potential — a driving mechanism). The KS nonlocality is the *most consequential* in the atlas: it is the primary dynamical mechanism, not a secondary constraint, and it is what drives the mass-concentrating blowup.

## 7.3 Determinism

Determinism asks: *Is the future determined by the past?*

This means: do smooth (or appropriate weak) solutions exist globally in time, are they unique, and do they depend continuously on the initial data? The answer varies dramatically across the atlas:

- **Unconditional global determinism:** FP, PME, AC, CH, KdV, HJ, Burgers, NLS (defocusing), NLS (focusing 1D). For these architectures, smooth (or entropy/viscosity) solutions exist for all time, are unique, and are Lipschitz-continuously dependent on the initial data. Full determinism.

- **Conditional/regime-dependent determinism:** NLS (focusing $d \geq 2$), KS ($M > 8\pi$), TFE ($0 < n < 1$), MCF, RF. For these, determinism holds in some regimes but not others — either blowup occurs for some data (requiring a weak-solution continuation), or the well-posedness theory is essentially but not fully complete.

- **Open determinism:** NS (3D). Whether smooth solutions exist globally is the most famous open problem in mathematical physics. The Clay Millennium Prize is offered for its resolution.

## 7.4 Generative Sufficiency

Generative sufficiency asks: *Does the architecture generate all its observed phenomena from the axioms?*

This is a measure of *completeness*: does the PDE theory account for everything the PDE does, or are there observed behaviors that the theory cannot explain?

The strongest generative sufficiency belongs to the KdV equation: every phenomenon — solitons, elastic collisions, dispersive radiation, the exact soliton resolution — is rigorously derived from the axioms with exact formulas. The generative gap is *zero*.

Most PDEs have small but nonzero gaps: the exact coarsening exponents of Cahn–Hilliard are proved as upper bounds but not as exact rates; the complete classification of NLS blowup dynamics in $d \geq 3$ is deep but not fully settled; the post-blowup continuation of Keller–Segel measure-valued solutions has unresolved uniqueness questions.

## 7.5 Envelope Tightness

Envelope tightness asks: *Are the bounds sharp, and is the envelope fully closed?*

A tight envelope has sharp inequalities (each bound is achieved by some admissible state) and a fully closed constraint surface (no open faces). The tightest envelopes belong to the architectures whose theory is most complete: PME (every bound saturated by the Barenblatt profile), KdV (every bound saturated by soliton solutions or exactly computed via IST), and FP (spectral theory gives exact convergence rates).

An envelope is less tight when it has open faces (NS 3D enstrophy gap), when some bounds are known to be suboptimal (CH coarsening rate), or when the closure is regime-dependent (NLS focusing, KS supercritical).

## 7.6 Structural Optimality

Structural optimality asks: *Is the architecture free of anomalies, and is it the simplest system generating its dynamics?*

An anomaly is a structural feature that is both *necessary* (forced by the axioms) and *potentially destructive* (threatening self-consistency). The NS vortex stretching sub-channel is an anomaly: it is forced by 3D geometry + incompressibility + advection, and it may drive regularity loss. The KS nonlocal aggregation is an anomaly in the structural-optimality sense: it is the primary dynamical mechanism, but it is nonlocal.

The architectures with the strongest structural optimality are those with *zero anomalies and zero constitutive parameters*: KdV, Ricci flow, MCF, Hamilton–Jacobi, Burgers, PME, FP, and the defocusing NLS. These architectures are *maximally economical* — the simplest systems that generate their respective dynamics.

## 7.7 Why These Six

The six FS criteria are not arbitrary — they capture the six fundamental dimensions of *architectural quality*:

- Minimality measures *economy* (is the architecture lean?).
- Locality measures *simplicity* (is the architecture free of nonlocal entanglement?).
- Determinism measures *predictability* (is the future determined?).
- Generative sufficiency measures *completeness* (does the theory explain everything?).
- Envelope tightness measures *sharpness* (are the bounds optimal?).
- Structural optimality measures *elegance* (is the architecture the best of its kind?).

Together, these six criteria measure the *structural soundness* of an architecture — its quality as a mathematical object, independent of its physical importance or practical utility. An architecture can be physically important but structurally flawed (NS in 3D: score 0, but it describes all fluid flow). An architecture can be structurally perfect but physically simple (FP: score 5, but it describes linear drift–diffusion).

---

# Chapter 8 — The PDE Atlas

## 8.1 The Idea of an Atlas

An atlas is a collection of maps — each map showing a different region, but all drawn in the same projection, with the same symbols, the same scale, the same legend. You can compare any two maps because they speak the same visual language.

The PDE Atlas is a collection of structural profiles — each profile describing a different PDE, but all analyzed through the same FS methodology, with the same concepts (channels, envelopes, constraint surfaces, poles), the same criteria (minimality, locality, determinism, generative sufficiency, envelope tightness, structural optimality), and the same scoring (PASS/CONDITIONAL/FAIL). You can compare any two PDEs because they speak the same structural language.

The atlas currently contains sixteen entries — the major nonlinear PDEs of mathematical physics. It is not exhaustive (many important PDEs are not yet evaluated), but it is *representative*: it covers all seven structural poles and all seven closure modes.

## 8.2 The Seven Poles

**The Diffusive Pole** contains the architectures dominated by parabolic smoothing: Fokker–Planck (linear, drift+diffusion, Gibbs–Boltzmann equilibrium), the porous medium equation (nonlinear degenerate, finite-speed, Barenblatt attractor), the thin-film equation (fourth-order degenerate, contact-line geometry), Allen–Cahn (gradient-flow, interface extinction), Cahn–Hilliard (conserved gradient-flow, coarsening), and reaction–diffusion (the broadest class, pattern-forming).

**The Hyperbolic Pole** contains the architectures dominated by first-order transport: Hamilton–Jacobi (variational closure, Hopf–Lax formula, no smoothing) and inviscid Burgers (conservation-law closure, $L^1 + L^\infty$ contraction, shock-concentrated dissipation).

**The Dispersive Pole** contains the architectures dominated by oscillatory spreading: the nonlinear Schrödinger equation (complex-valued, Hamiltonian, solitons in focusing 1D, scattering in defocusing) and the Korteweg–de Vries equation (real-valued, bi-Hamiltonian, completely integrable, soliton resolution).

**The Geometric Pole** contains the architectures whose state variables are geometric objects: mean curvature flow (extrinsic curvature, surface evolution, genus reduction) and Ricci flow (intrinsic curvature, metric evolution, geometrization theorem).

**The Aggregation Pole** contains the Keller–Segel system — the architecture with nonlocal self-attraction, mass-concentrating blowup, and the sharp threshold $M = 8\pi$.

**The Fluid Pole** contains the Navier–Stokes equations — the architecture with nonlocal pressure, incompressibility, and the open 3D regularity problem.

**The Integrable Apex** is the KdV equation — the architecture with infinite conservation laws, exact solvability, and the deepest structural resources of any nonlinear PDE.

## 8.3 Why the Taxonomy Is Finite

The taxonomy has seven poles because the number of qualitatively distinct channel compositions is finite. There are approximately nine channel types, and they combine in a finite number of qualitatively distinct ways. Adding diffusion to transport gives a different architecture than adding dispersion to transport. But there are only so many fundamentally different combinations.

This finiteness is not a limitation — it is a *structural feature* of the PDE landscape. The fact that the taxonomy is finite means that the space of possible PDE dynamics is *bounded* — there are not infinitely many qualitatively different types of behavior, but a finite number of poles, each with a characteristic dynamical signature.

## 8.4 Apex Architectures

The atlas identifies two *apex architectures* — PDEs that achieve the deepest structural results within their respective poles:

**KdV as the integrable apex.** The KdV equation has: infinite conservation laws (from the bi-Hamiltonian structure), exact solvability (from the inverse scattering transform), a fully classified constraint surface (every point labeled by scattering data), zero constitutive parameters, and the soliton resolution theorem (every solution decomposes uniquely into solitons + radiation). The soliton resolution is the *dynamical analogue of the fundamental theorem of arithmetic*: just as every integer decomposes uniquely into primes, every KdV solution decomposes uniquely into solitons.

**Ricci flow as the geometric apex.** Ricci flow has: the Perelman monotonicity formulas (the deepest monotone quantities in the atlas), the Hamilton–Perelman surgery program (the most complete singularity-resolution framework), the geometrization theorem (classifying the topology of closed 3-manifolds), and the resolution of the Poincaré conjecture (the only Clay Millennium Problem solved by a PDE). Three axioms generate the complete topological classification of 3-dimensional spaces — the highest structural amplification ratio in mathematics.

## 8.5 The Summary Table

[Figure 1: FS_Atlas_Summary_Table.png — Summary of PDE architectures, poles, and FS scores.]

The summary table presents each architecture's pole, locality, singularity type, nonlocality, integrability, gradient-flow structure, and FS score. The table is the *compressed visual representation* of the atlas — a single image containing the entire structural taxonomy.

---

# Chapter 9 — FS Beyond PDEs

## 9.1 A General Language

The FS framework is not tied to PDEs. Its core concepts — channels, envelopes, constraint surfaces, poles — are *domain-independent*. They apply to any system that can be decomposed into interacting mechanisms with definite structural properties.

The key insight is that the *same structural phenomena* appear across different mathematical domains: decomposition into irreducible components (prime factorization, soliton resolution, geometric decomposition), competition between stabilizing and destabilizing mechanisms (diffusion vs. advection, entropy vs. aggregation, parabolic smoothing vs. curvature reaction), and the existence of canonical forms (equilibria, self-similar profiles, solitons, Einstein metrics).

These structural phenomena are not tied to PDEs — they are *architectural universals* that appear whenever a system is composed of interacting channels.

## 9.2 Physical Ontologies

The FS framework originated in the study of the *Factor Skyline* — the two-dimensional representation of the integers in which each integer $n$ becomes a column of width $\text{lpf}(n)$ (least prime factor) and height $n/\text{lpf}(n)$. The FS primitives (width, height, activation, coverage, escape) are the "channels" of the arithmetic structure, and the prime number theorem, Mertens' theorem, and the Chebyshev conservation law are the "envelope inequalities."

The arithmetic skyline is a *static architecture* — the integers do not evolve in time. But it shares deep structural parallels with the dynamical PDE architectures: the sieve decomposition of integers into primes parallels the KdV soliton resolution; the prime distribution (PNT) parallels the Gibbs–Boltzmann equilibrium of FP; the coverage conservation (Chebyshev) parallels the mass conservation of PME.

These parallels are not coincidental — they reflect the *universality of architectural structure*. Decomposition, conservation, canonical forms, and structural thresholds appear in arithmetic, in PDEs, in geometry, and in physics, because they are *properties of architectures*, not of any specific domain.

## 9.3 Dynamical Systems

The FS framework extends naturally to finite-dimensional dynamical systems $\dot{x} = f(x)$. The channels are the components of $f$: linear terms (eigenvalue structure), nonlinear terms (bifurcation structure), coupling terms (network topology). The envelope is the set of invariant manifolds, Lyapunov functions, and conserved quantities. The constraint surface is the phase portrait.

The poles of finite-dimensional dynamical systems include: gradient (Lyapunov descent to fixed points), Hamiltonian (energy-preserving, quasi-periodic), dissipative-chaotic (strange attractors, sensitive dependence), and integrable (Liouville theorem, action-angle coordinates, invariant tori).

## 9.4 Geometry

The FS framework applies to *geometric structures* — Riemannian manifolds, symplectic manifolds, algebraic varieties — viewed as static architectures whose "channels" are the curvature components and whose "envelope" is the set of geometric constraints (Einstein condition, Kähler condition, Calabi–Yau condition).

The geometric flows (Ricci flow, Kähler–Ricci flow, mean curvature flow, Willmore flow) are the *dynamical extensions* of these static architectures — they evolve the geometry toward its canonical form, using the curvature as the driving mechanism.

## 9.5 Computation and Learning

Neural network architectures can be viewed through the FS lens: the layer types (convolutional, recurrent, attention, normalization) are channels; the representable functions are the envelope; the loss landscape is the constraint surface. The FS criteria apply directly: Is the architecture minimal (no unnecessary layers)? Is it local (convolutional) or nonlocal (attention)? Is training deterministic (does it converge to a unique solution)? Does it generate all the features of the data distribution?

This perspective is speculative but suggestive. The explosive growth of neural architecture design — with hundreds of competing architectures, each with different layer combinations — calls out for the kind of structural classification that FS provides. If the FS framework can identify the "poles" of neural architectures (the qualitatively distinct channel combinations that produce distinct computational behaviors), it could provide a principled basis for architecture design.

---

# Chapter 10 — Implications and Future Directions

## 10.1 What FS Enables

The FS framework enables several things that were previously impossible or extremely difficult:

**Cross-domain comparison.** For the first time, we can *rigorously compare* the Navier–Stokes equations with Ricci flow, the Keller–Segel system with the NLS, or the KdV equation with the porous medium equation — not by analogy or metaphor but through a *common structural language* that identifies the specific channels, envelopes, and constraint surfaces of each architecture.

**Structural diagnosis.** Given a new PDE, FS provides a systematic method for identifying its structural properties: decompose into channels, derive the envelope, construct the constraint surface, evaluate the criteria. The output is a complete structural profile that immediately reveals the system's pole, closure mode, and structural quality — before any detailed analysis is performed.

**Open-problem localization.** The atlas localizes the difficulty of the NS 3D regularity problem to a specific structural feature: the interaction of the self-advection channel with the incompressibility constraint and the nonlocal pressure channel. Burgers (which has self-advection without incompressibility or pressure) is completely understood. KdV (which adds dispersion to Burgers' advection) is exactly solvable. The structural addition of incompressibility + pressure is *precisely* what makes NS intractable — and this identification suggests that any resolution of the NS problem must come to terms with this specific structural interaction.

## 10.2 Reframing PDE Theory

The FS framework suggests a shift in how we think about PDE theory: from *equation-centered* (each PDE studied individually, with its own community and its own tools) to *architecture-centered* (PDEs studied as instances of structural types, with shared tools and transferable insights).

In the architecture-centered view:
- A new PDE is first classified by its channels and pole, then analyzed using the tools appropriate to that pole.
- A result proved for one architecture at a given pole is examined for transferability to other architectures at the same pole.
- An open problem is localized to a specific structural feature, and the resolution strategy is guided by how similar features are handled at other poles.

## 10.3 Reframing Physical Modeling

The FS framework also suggests a shift in how we think about physical modeling: from *equation-first* (start with the PDE and study its properties) to *architecture-first* (start with the structural requirements and select the simplest architecture that satisfies them).

In the architecture-first approach:
- The modeler specifies the required channels (diffusion + advection? diffusion + reaction? diffusion + aggregation?) and the required structural properties (conservation? locality? gradient-flow structure?).
- The FS framework identifies the *structural pole* that matches these requirements.
- The simplest architecture at that pole is selected as the model.

This approach would produce *structurally minimal* models — models with the fewest channels and the simplest architecture that generate the required phenomenology.

## 10.4 Open Directions

The FS framework motivates several research programs:

**Extending the atlas.** The current atlas covers sixteen PDEs. Important systems not yet evaluated include: the Boltzmann equation, the Vlasov–Poisson system, the Euler equations (inviscid), the Ginzburg–Landau equation (complex, with diffusion + dispersion), the Kuramoto–Sivashinsky equation (fourth-order + instability), the Camassa–Holm equation (integrable, wave-breaking), the surface quasi-geostrophic equation (2D analogue of 3D Euler), and the Yang–Mills equations (gauge theory).

**Stochastic extensions.** Adding noise channels (additive, multiplicative, space-time) to the FS framework would enable the analysis of stochastic PDEs — connecting to the theory of regularity structures and paracontrolled distributions.

**Computational FS.** Developing software tools for automating the FS analysis — channel identification, envelope computation, constraint-surface visualization — would make the framework accessible to a broader community.

**FS-guided numerics.** Developing numerical methods that *respect the channel structure* — preserving conservation laws, maintaining the correct stability roles, and correctly discretizing nonlocal channels — could produce more robust and efficient simulations.

---

# Chapter 11 — Closing Reflections

## 11.1 The Core Insight

The core insight of the Factor Skyline Framework is simple but powerful: *every dynamical system is a composition of channels, and the qualitative behavior of the system is determined by the interactions among those channels within the constraint surface defined by the system's axioms.*

This insight transforms the study of dynamical systems from a collection of individual analyses (each system studied with its own tools, in its own community, with its own vocabulary) into a *unified structural enterprise* (all systems analyzed with the same concepts, in the same framework, with the same vocabulary).

The transformation is not merely organizational. It reveals structural relationships that were previously invisible — the opposite nonlocal roles of KS and NS, the extrinsic–intrinsic duality of MCF and RF, the conservation experiment of AC vs. CH, the integrable kinship of NLS and KdV, the structural localization of the NS regularity problem. These relationships are not visible from within any single community — they become visible only when the systems are placed side by side in a common framework.

## 11.2 The Value of Architectural Thinking

Architectural thinking — analyzing systems through their structural properties rather than their specific solutions — has a distinguished history in mathematics. Galois theory classifies polynomial equations by their symmetry groups. Category theory classifies mathematical structures by their morphisms. Thurston's geometrization classifies 3-manifolds by their model geometries.

The FS framework extends this tradition to dynamical systems. It classifies PDEs by their channel compositions, envelopes, constraint surfaces, and poles — producing a structural taxonomy that reveals the *deep reasons* behind the phenomena that PDE theory studies.

The value of this classification is not that it replaces detailed analysis — it does not. The $L^1$ contraction of Burgers still needs to be proved; the Perelman monotonicity of Ricci flow still needs to be discovered; the soliton resolution of KdV still needs the inverse scattering transform. What the classification provides is *context*: it shows where each result fits in the structural landscape, what it has in common with results in other domains, and what it tells us about the architecture's character.

## 11.3 The Future

The Factor Skyline Framework is a beginning, not an end. The PDE Atlas covers sixteen systems; the mathematical universe contains thousands. The FS methodology has been demonstrated for PDEs; it could be extended to ODEs, stochastic systems, geometric structures, computational architectures, and physical ontologies. The seven poles and seven closure modes identified in the current atlas may be the beginning of a larger taxonomy that encompasses all of mathematical dynamics.

The ultimate vision is ambitious but concrete: a *structural atlas of mathematics* — a comprehensive map of the architectural landscape, showing the poles, the connections, the hierarchies, and the apex structures that organize the mathematical universe. The Factor Skyline Framework provides the language for this atlas. The PDE Atlas provides the first detailed map. The territory is vast, and the exploration has only begun.

---

*End of document.*
