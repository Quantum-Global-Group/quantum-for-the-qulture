# Quantum for the Qulture

**A hands-on pathway from quantum curiosity to quantum capability.**

**See it. Understand it. Code it. Run it. Interpret it. Find your pathway.**

An initiative by Quantum Global Group.

## What this is

Quantum for the Qulture is the public learning pathway of Quantum Global Group. You move from a quantum idea you can point at, to the mathematics that defines it, to a Qiskit circuit you can run and explain. This repository is where that pathway is built.

The first complete lab is [Entanglement: From Your Hands to Real Hardware](labs/01_entanglement/README.md). Further labs are listed in [ROADMAP.md](ROADMAP.md) and are not written yet.

## Who it is for

Curious beginners, students, technical professionals, educators, organizations, and career explorers. Lab 001 is a shared starting point. It is not a full curriculum for every audience. The purpose and the boundaries are in [docs/vision.md](docs/vision.md).

## What you can learn now

You can learn what a qubit state is, how the gates H and CX change a two-qubit state, what the Bell state `|Phi+>` looks like as a vector, what a local sample of 1024 shots does and does not prove, and how a circuit changes when it is rewritten for a device's basis gates. The teaching order is in [docs/learning-philosophy.md](docs/learning-philosophy.md).

## The method

See it, understand it, map it, code it, run it, measure it, interpret it, find your pathway.

Each lesson answers six questions: what are we doing, why, how does it work, what happened, what does it mean, and where can I go next.

## Three ways to take part

| Level | You do this | IBM account |
| --- | --- | --- |
| 1. See and understand | Read, predict, and use the worksheet. Use a Qubi kit if you are in a room that has one. | Not required |
| 2. Code and simulate | Run the notebook locally with Qiskit. | Not required |
| 3. Run on real hardware | After an invitation, submit one deliberate job. | Required, and capacity is limited |

Hardware is never a prerequisite for the foundations. Details are in [docs/learning-pathway.md](docs/learning-pathway.md).

## What a Qubi is

A Qubi is a physical model of a qubit made by [Qolour](https://www.qolour.com/). You can hold it and use it to see a two-qubit pattern before you write a matrix. The Bell Pairs activity we point to is Qolour's lesson. We link it. We do not copy it. See [qubis/bell-pairs/README.md](qubis/bell-pairs/README.md).

Qubi is for seeing. Qiskit is for representing the same idea in code. An IBM quantum processor is for running an approved circuit on hardware.

## What Qiskit is

Qiskit is the open-source software development kit used in these labs to build circuits and to study their results. IBM documents the current SDK and the IBM Quantum platform in the [IBM Quantum documentation](https://quantum.cloud.ibm.com/docs/). Lab 001 uses the current local primitives, `StatevectorSampler` and `StatevectorEstimator`, and does not use the retired `IBMQ.load_account()` or `execute()` interfaces.

## Do I need advanced mathematics?

No. Lab 001 uses column vectors, addition, and a square root, and it shows each vector. Linear algebra will grow in later labs. You do not need a physics degree to begin.

## Do I need an IBM account?

No, unless you choose level 3. Levels 1 and 2 are complete without one. Level 3 depends on a Classroom seat. Capacity is about 100 seats, invitations are manual, and this repository does not grant access. Read [docs/qpu-access.md](docs/qpu-access.md).

## Do the labs work without hardware?

Yes. The notebook simulates the Bell circuit locally. The hardware section is in the file so you can see the real steps, and it is switched off. Opening the notebook does not submit a job.

## Start here

1. Read [docs/getting-started.md](docs/getting-started.md) and choose level 1, 2, or 3.
2. Open [Lab 001](labs/01_entanglement/README.md).
3. If you write code, install from [requirements.txt](requirements.txt) and run `python tests/smoke_lab001.py` before you trust your setup.
4. Keep secrets out of git. The rules are in [docs/security-and-privacy.md](docs/security-and-privacy.md).

The learning community, hosted on Skool, is where video, guided Qubi demonstrations, discussion, and hardware onboarding live. The notebook is not locked behind membership. The community link will be added when the founder supplies it.

## Learning roadmap

The path a person walks is [docs/learner-journey.md](docs/learner-journey.md). How the website, the community, Qolour, IBM Quantum, and this repository divide the work is [docs/architecture.md](docs/architecture.md). What comes after Lab 001 is [ROADMAP.md](ROADMAP.md).

## Lab index

| Lab | Status | Question |
| --- | --- | --- |
| [001. Entanglement: From Your Hands to Real Hardware](labs/01_entanglement/README.md) | Complete | Can I see, represent, build, simulate, and interpret a Bell state? |

## Career pathways

An introductory map of roles, and the training this lab does not replace, is in [docs/career-pathways.md](docs/career-pathways.md). An optional later credential is described in [docs/certification-journey.md](docs/certification-journey.md). Lab 001 does not qualify you for a job and does not certify you.

## Official documentation

IBM Quantum documentation, IBM Quantum Learning, Qiskit, and Qolour are the external sources. The links we actually use are collected in [resources/official-docs.md](resources/official-docs.md).

## Repository map

```text
README.md                 front door
ROADMAP.md                work that is not built yet
CONTRIBUTING.md           how to propose a change
LICENSE                   notice: a final license is not chosen
requirements.txt          tested local packages
docs/                     vision, pathway, access, security
labs/01_entanglement/     Lab 001 notebook, worksheet, instructor guide
templates/                starting points for the next lab
qubis/bell-pairs/         pointer to Qolour's lesson
resources/official-docs.md
tests/smoke_lab001.py     offline check, no IBM credentials
```

How those pages stay consistent is [docs/documentation-guide.md](docs/documentation-guide.md).

## License

A final license has not been chosen. Kevin A. Robinson must approve it. Until then, all rights are reserved. See [LICENSE](LICENSE).
