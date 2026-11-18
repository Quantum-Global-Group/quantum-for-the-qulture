# Learning pathway

Start with Lab 001. The later labs on [../ROADMAP.md](../ROADMAP.md) are described there and are not available yet.

## Three levels

Hardware is never required for the foundations.

### Level 1. See and understand

No IBM account. No local install, if you are reading beside someone who will run the code. You can finish the beginner questions from the explanations, and the worksheet from the advanced notebook. In a classroom with Qubi kits, this level includes Stop 1 of the beginner notebook. Section 08 of the advanced notebook is the same observation for a group that is already in that file.

### Level 2. Code and simulate

Install the packages in [../requirements.txt](../requirements.txt). Run the notebook on your own machine. Qiskit simulates the circuit locally. You still do not need an IBM account or a Classroom seat.

### Level 3. Run on real hardware

Optional, and only for an eligible learner who has been invited. Read [qpu-access.md](qpu-access.md) and [ibm-quantum-setup.md](ibm-quantum-setup.md). Set the hardware flag yourself, in your own copy, after you understand the local result. Submit one job on purpose. This repository's copy of the notebook leaves the flag off.

## What Lab 001 covers

The question of the lab: can you experience entanglement, represent it mathematically, build the circuit, simulate it, run it on hardware if you choose, and interpret the results?

Two notebooks walk a single state, the Bell state often written Phi-plus. The beginner notebook is the first file. The advanced notebook keeps the original development:

```text
|Phi+> = (|00> + |11>) / sqrt(2)
```

The beginner notebook introduces the words it needs, one at a time: qubit, state, basis, gate, circuit, measurement, probability, observable, and backend. It builds Phi Plus with H and CX, changes it with one X or one Z, samples Z and X with the local sampler, estimates ZZ and XX, and transpiles the circuit on a local mock backend. The advanced notebook adds the vectors, the matrices, the purity argument, and the YY expectation. In both files the hardware section is present and inactive.

## Suggested order inside the lab

1. Open the beginner notebook. Name the level you are on today.
2. If you are in a room with Qubi kits, do the observation before the circuit. If you are not, use the no-Qubi story in Stop 1.
3. Answer one question at a time. Predict the state after H, then after CX, before you run those cells.
4. Predict the counts, then sample. Compare Phi Plus and Phi Minus in the Z basis and the X basis.
5. Read the estimator values as exact properties of the state, and the counts as a finite sample.
6. Look at the transpiled circuit and say what changed. The mock backend is not a hardware result.
7. Leave hardware off unless you are on level 3 and you mean to spend a job. The beginner notebook asks for two flags and a typed confirmation.
8. Write the interpretation. The worksheet matches the advanced notebook.
9. When you want the matrices and the purity argument, open the advanced notebook. Its four-stop memory walk is the practice in [learning-philosophy.md](learning-philosophy.md). The beginner notebook points at that walk. It does not replace it.

## Where the official pages fit

Each major idea in the lab points at a current official page. The list is [../resources/official-docs.md](../resources/official-docs.md). If a page and the notebook ever disagree, trust the page for the product, and open an issue about the notebook.

## What this pathway does not include yet

Measurement as its own lab, a wider gate set, and a Bell inequality. Certification study beyond the orientation in [certification-journey.md](certification-journey.md). Role training beyond the orientation in [career-pathways.md](career-pathways.md).
