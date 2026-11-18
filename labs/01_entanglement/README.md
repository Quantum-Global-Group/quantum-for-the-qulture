# Lab 001. Entanglement: From Your Hands to Real Hardware

**See it with Qubis. Build it with Qiskit. Run it on a real quantum computer.**

**Question.** Can I experience entanglement, represent it mathematically, build the circuit, simulate it, run it on hardware, and interpret the results?

An initiative by Quantum Global Group.

You can answer the scientific part of that question with no IBM account. The hardware run is optional and stays switched off in this repository.

## The state you will build

The lab builds one two-qubit state, often called Phi-plus:

```text
|Phi+> = (|00> + |11>) / sqrt(2)
```

You will see why those two basis states appear, why the other two do not, and which expectations the state has: `<ZZ> = +1`, `<XX> = +1`, and `<YY> = -1`. A histogram of `00` and `11` is a correlation in one basis. It is not yet a Bell inequality, and the lab does not call it one.

## Three levels

| Level | What you do | Account |
| --- | --- | --- |
| 1. See and understand | Qubi prompts or the written observation, then the vectors and the worksheet. | None |
| 2. Code and simulate | Run the notebook locally. 1024 shots, no network job. | None |
| 3. Hardware | After Kevin A. Robinson sends the IBM invitation, one job in your own copy. | Classroom seat |

Setup for level 2 is [../../docs/getting-started.md](../../docs/getting-started.md). Hardware access is requested in the [Skool community](https://www.skool.com/quantum-for-the-qulture-8361): join, complete Start Here, and submit there the email address that should receive the IBM invitation. He reviews the request and sends the invitation himself. There is no public IBM invite link. This repository does not store that email. The seat policy is [../../docs/qpu-access.md](../../docs/qpu-access.md).

## Files

- Notebook: [entanglement_hands_to_hardware.ipynb](entanglement_hands_to_hardware.ipynb)
- Worksheet: [STUDENT_WORKSHEET.md](STUDENT_WORKSHEET.md)
- Instructor guide: [INSTRUCTOR_GUIDE.md](INSTRUCTOR_GUIDE.md)
- Qubi lesson pointer: [../../qubis/bell-pairs/README.md](../../qubis/bell-pairs/README.md)
- Assets: [assets/future-demos.md](assets/future-demos.md)

The notebook has sections 00 through 18. Run them in order. `RUN_REAL_HARDWARE` is `False`.

## Check the science without opening a notebook

From the repository root, after `pip install -r requirements.txt`:

```bash
python tests/smoke_lab001.py
```

That check rebuilds the state, the CNOT cases, the three expectations, the local sample, and a local transpilation. It does not read a credential.

## What you should be able to say at the end

- Which vector is `|0>`, which is `|+>`, and which is `|Phi+>`.
- What CX does to each computational basis input, and why a basis input is not an entangled output.
- Why Qiskit prints qubit 0 on the right of a bitstring.
- What your 1024 local shots were, and why an uneven split of `00` and `11` can still be a perfect agreement score.
- Why that score does not prove entanglement, and why `<XX>` and `<YY>` are part of the description.
- What changed when the circuit was rewritten for a local device stand-in, including a case where depth grew.
- Whether you collected a hardware result. If you did not, you say that.
- The four stops of the memory walk, in your own pictures, and the fact each stop points back to: the state columns, what I, X, H, and CX do, the CNOT rule, and `|Phi+>`.
