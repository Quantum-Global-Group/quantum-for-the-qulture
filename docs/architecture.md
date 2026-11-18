# Architecture

Quantum for the Qulture is one piece of a larger system. This repository is the piece that holds the labs and the public learning documents. The other pieces stay where they are. We document how a learner moves between them. We do not rebuild them here.

## Where each job lives

| Piece | Role for a learner | Where it lives |
| --- | --- | --- |
| This repository | Build the circuit, run it locally, read the pathway | Quantum-Global-Group/quantum-for-the-qulture |
| Quantum Global Group website | Discover the organization and its public tools | [https://www.quantumglobalgroup.io/](https://www.quantumglobalgroup.io/) |
| Learning community | Video, discussion, Qubi demonstrations, hardware onboarding | [Skool community](https://www.skool.com/quantum-for-the-qulture-8361) |
| Qolour and Qubi | See a model qubit in your hands | [https://www.qolour.com/](https://www.qolour.com/) |
| IBM Quantum | Run an approved circuit on hardware | IBM Quantum Platform and our Classroom seats |
| Career Navigator | Find a direction from skills and interests | Separate website surface. Not implemented in this repository. |
| Portfolio | Later home for work a learner chooses to show | Not built yet. |

GitHub is where you build. The community is where a cohort is guided. Qolour is where you see it. IBM Quantum is where you run it on hardware. Quantum Global Group connects those pieces.

## What this repository refuses to duplicate

The marketing site and any workforce application are separate codebases. The Career Navigator and any readiness product stay outside this tree. Lab notebooks are not gated behind the community, and this repository does not store a seat roster.

A private record of Classroom seats, if one is kept, lives outside this repository. The public policy for those seats is [qpu-access.md](qpu-access.md).

## Long-term surfaces

These names describe later integration points. None of them is a module in this repository today.

- Navigator: a path recommendation. Today that product is separate.
- Readiness: a check of prerequisites before a cohort or a hardware seat.
- Classroom: IBM Quantum Classroom seats, managed by people, not by a script here.
- Portfolio: a place for work the learner decides to publish.

## How a lab is assembled

A lab has one folder. Lab 001 shows the shape:

- A README that states the question and the three access levels.
- One notebook that runs from top to bottom with `RUN_REAL_HARDWARE` left `False`.
- A student worksheet that can be used on paper.
- An instructor guide with 60, 90, and 120 minute cuts.
- An assets folder that contains only real files. A pointer to a future demo is allowed. A fictional video link is not.

Shared starting points for the next lab live in [../templates/](../templates/). Official links live in [../resources/official-docs.md](../resources/official-docs.md). The Qubi pointer for Bell pairs lives in [../qubis/bell-pairs/README.md](../qubis/bell-pairs/README.md).

## Runtime shape of Lab 001

```text
Learner notebook
    |
    +-- Level 1: read, predict, worksheet
    |
    +-- Level 2: Qiskit Statevector, StatevectorSampler,
    |            StatevectorEstimator, local GenericBackendV2
    |            (no account, no network job)
    |
    +-- Level 3, off by default: QiskitRuntimeService and the
                 client-side Sampler, one job, safe metadata only
```

The level 3 branch is code a learner can read. The committed notebook does not enter it. Tests do not enter it.

## Scale

The documents assume a learning community that can be taught as 10 people, then 25, then 50, then 100, with seats held back for instructors, collaborators, workshops, and testing. They do not assume a consumer platform.
