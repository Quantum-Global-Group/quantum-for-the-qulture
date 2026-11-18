# Roadmap

This page lists work that is not in the repository yet. It is not a promise that a lab exists. The only complete lab today is [Lab 001](labs/01_entanglement/README.md).

Design the pathway for a cohort of 10 learners, then 25, then 50, then 100. That includes instructors, collaborators, workshops, and testing. Do not shape the public materials around a crowd of 10,000.

## Labs after 001

Each future lab keeps the same sequence: see it, understand it, map it, code it, run it, measure it, interpret it, find your pathway.

| Lab | Working title | What it adds after Lab 001 |
| --- | --- | --- |
| 002 | Measurement | A single shot, a basis, and a histogram, before more gates. |
| 003 | Quantum gates | A wider gate set, once states and measurement are already in hand. |
| 004 | Bell inequality | A CHSH-style test. Lab 001 correlations are not that test. |

Lab 002 comes before a broader gate catalog so that measurement has its own lesson. Lab 004 is where a claim about nonlocality would have to be earned. Lab 001 does not make that claim.

## Tracks

These are directions for later material, not folders full of empty courses.

- Foundations: states, gates, measurement, entanglement.
- Mathematics: vectors, inner products, and the linear algebra each lab actually uses.
- Qiskit: circuits, primitives, and reading results.
- Hardware modalities: superconducting devices first, because that is what the optional IBM path runs. Other modalities get a page when a lab needs them.
- Applications: only after a learner can say what was measured.
- Security: how to handle credentials, results, and claims about cryptographic consequence.
- Workforce: the introductory map in [docs/career-pathways.md](docs/career-pathways.md), then deeper role preparation outside this first release.

The certification path is described in [docs/certification-journey.md](docs/certification-journey.md). It is a study architecture, not a set of exam notebooks.

## Later product surfaces

Not built here, and not scheduled by this file:

- Dashboards and cohort tools.
- Portfolio publishing.
- Organization-specific tracks.
- Learning analytics.
- Extra hardware providers.

The Quantum Global Group website, the learning community, Qolour, and IBM Quantum stay separate systems. How they connect is described in [docs/architecture.md](docs/architecture.md).

## Public learning and later services

This repository is the public education layer. A later private service can sit beside it. One concept name for that kind of engagement is the Quantum Global Group Quantum Workforce Readiness Sprint. No price, client list, or delivery method belongs in this repository.

## Scale of a lab session

Instructor timing for Lab 001 already covers 60, 90, and 120 minutes. Later labs should publish the same three cuts before they are marked complete.
