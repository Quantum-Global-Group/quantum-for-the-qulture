# Learning pathway

Start with Lab 001. The later labs on [../ROADMAP.md](../ROADMAP.md) are described there and are not available yet.

## Three levels

Hardware is never required for the foundations.

### Level 1. See and understand

No IBM account. No local install, if you are reading beside someone who will run the code. You can finish the worksheet from the explanations and the printed notebook results. In a classroom with Qubi kits, this level includes the hands-on observation in section 08 of the lab.

### Level 2. Code and simulate

Install the packages in [../requirements.txt](../requirements.txt). Run the notebook on your own machine. Qiskit simulates the circuit locally. You still do not need an IBM account or a Classroom seat.

### Level 3. Run on real hardware

Optional, and only for an eligible learner who has been invited. Read [qpu-access.md](qpu-access.md) and [ibm-quantum-setup.md](ibm-quantum-setup.md). Set the hardware flag yourself, in your own copy, after you understand the local result. Submit one job on purpose. This repository's copy of the notebook leaves the flag off.

## What Lab 001 covers

The question of the lab: can you experience entanglement, represent it mathematically, build the circuit, simulate it, run it on hardware if you choose, and interpret the results?

The notebook walks a single state, the Bell state often written Phi-plus:

```text
|Phi+> = (|00> + |11>) / sqrt(2)
```

Along the way it teaches the words it uses: qubit, state, basis, gate, circuit, measurement, probability, observable, and backend. It builds that state with H and CX, samples it with the local sampler, estimates three Pauli expectations, and transpiles the circuit to a local stand-in for a device. The hardware section is present and inactive.

## Suggested order inside the lab

1. Read the welcome and name the level you are on today.
2. If you are in a room with Qubi kits, do the observation before the algebra.
3. Predict the state after H, then after CX, before you run those cells.
4. Predict the counts, then sample.
5. Read the estimator values as exact properties of the state, and the counts as a finite sample.
6. Look at the transpiled circuit and say what changed.
7. Leave hardware off unless you are on level 3 and you mean to spend a job.
8. Write the interpretation in the worksheet.

## Where the official pages fit

Each major idea in the lab points at a current official page. The list is [../resources/official-docs.md](../resources/official-docs.md). If a page and the notebook ever disagree, trust the page for the product, and open an issue about the notebook.

## What this pathway does not include yet

Measurement as its own lab, a wider gate set, and a Bell inequality. Certification study beyond the orientation in [certification-journey.md](certification-journey.md). Role training beyond the orientation in [career-pathways.md](career-pathways.md).
