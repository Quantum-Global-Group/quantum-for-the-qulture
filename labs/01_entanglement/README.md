# Lab 001. Entanglement: From Your Hands to Real Hardware

**See it with Qubis. Build it with Qiskit. Run it on a real quantum computer.**

**Question.** Can I experience entanglement, represent it mathematically, build the circuit, simulate it, run it on hardware, and interpret the results?

An initiative by Quantum Global Group.

You can answer the scientific part of that question with no IBM account. The hardware run is optional and stays switched off in this repository.

## Which notebook to open

| Notebook | Open it when | File |
| --- | --- | --- |
| Beginner, recommended first | You want to observe, predict, answer one question at a time, build Phi Plus, simulate, and compare the Z and X bases | [entanglement_beginner.ipynb](entanglement_beginner.ipynb) |
| Advanced reference | You want the original vectors, matrices, purity analysis, YY expectation, and experiments | [entanglement_hands_to_hardware.ipynb](entanglement_hands_to_hardware.ipynb) |

Start with the beginner notebook. The advanced notebook was not replaced.

### How a student opens the beginner lesson

1. In a clone of this repository, install from [requirements.txt](../../requirements.txt) and open `labs/01_entanglement/entanglement_beginner.ipynb` in Jupyter. Python 3.10 or newer. The tested run used Python 3.12.3.
2. Or upload that notebook file by itself to Google Colab. Its links point at public pages. The core path does not need the rest of the clone beside it, and it installs the local packages if they are missing.
3. Run the cells from the top. At each question, type one letter. The explanation is printed after you answer. SKIP leaves a question for later. The score lasts for that kernel session.
4. Leave `RUN_REAL_HARDWARE` and `I_AUTHORIZE_ONE_QPU_JOB` set to `False`. A job also requires the typed word `RUN`. Opening the file does not submit one.
5. Open the advanced notebook when the amplitudes feel familiar and you want the matrices, the purity argument, and the memory walk in full.

A copy-ready tutor prompt sits near the top of the beginner notebook. Paste it into a separate chat if you want a coach. The notebook itself does not call an outside service.

## The state you will build

The lab builds one two-qubit state, often called Phi-plus:

```text
|Phi+> = (|00> + |11>) / sqrt(2)
```

You will see why those two basis states appear, why the other two do not, and which expectations the state has: `<ZZ> = +1`, `<XX> = +1`, and `<YY> = -1`. A histogram of `00` and `11` is a correlation in one basis. It is not yet a Bell inequality, and the lab does not call it one.

## Three levels

| Level | What you do | Account |
| --- | --- | --- |
| 1. See and understand | Qubi prompts or the written observation, then the beginner questions. The worksheet follows the advanced notebook. | None |
| 2. Code and simulate | Run the beginner notebook locally. 512 shots in that file, no network job. The advanced notebook uses 1024. | None |
| 3. Hardware | After Kevin A. Robinson sends the IBM invitation, one job in your own copy. | Classroom seat |

Setup for level 2 is [../../docs/getting-started.md](../../docs/getting-started.md). Hardware access is requested in the [Skool community](https://www.skool.com/quantum-for-the-qulture-8361): join, complete Start Here, and submit there the email address that should receive the IBM invitation. He reviews the request and sends the invitation himself. There is no public IBM invite link. This repository does not store that email. The seat policy is [../../docs/qpu-access.md](../../docs/qpu-access.md).

## Files

- Beginner notebook: [entanglement_beginner.ipynb](entanglement_beginner.ipynb)
- Advanced notebook: [entanglement_hands_to_hardware.ipynb](entanglement_hands_to_hardware.ipynb)
- Worksheet: [STUDENT_WORKSHEET.md](STUDENT_WORKSHEET.md)
- Instructor guide: [INSTRUCTOR_GUIDE.md](INSTRUCTOR_GUIDE.md)
- Qubi lesson pointer: [../../qubis/bell-pairs/README.md](../../qubis/bell-pairs/README.md)
- Assets: [assets/future-demos.md](assets/future-demos.md)

The advanced notebook has sections 00 through 18. Run either notebook from the top. In both files the hardware flag stays `False`. The beginner file also keeps `I_AUTHORIZE_ONE_QPU_JOB` set to `False`.

## Check the science without opening a notebook

From the repository root, after `pip install -r requirements.txt`:

```bash
python tests/smoke_lab001.py
```

That check rebuilds the state, the CNOT cases, the three expectations, the local sample, and a local transpilation. It also runs the beginner notebook's local cells, with the hardware flags left off, and checks all 18 questions. It does not read a credential.

## What the beginner notebook asks you to say

- A Qubi is a teaching model, and a Z histogram of 00 and 11 is a correlation.
- H on qubit 0, then CX(0, 1), prepares Phi Plus.
- Qiskit prints q1 q0, so qubit 0 is the rightmost bit.
- X on qubit 0 of Phi Plus moves the bits to 01 and 10. Z on qubit 0 changes the relative sign and leaves the Z probabilities on 00 and 11.
- Phi Plus and Phi Minus agree in the Z basis and disagree in the X basis.
- Sampler returns counts. Estimator returns an expectation. For Phi Plus those expectations are +1 and +1 for ZZ and XX. For Phi Minus, XX is -1.
- Transpilation rewrites a logical circuit into an ISA circuit. The mock backend in the lesson is not a hardware result.
- Whether a device job was run. If it was not, the hardware column stays empty.

## What the advanced notebook asks you to say at the end

- Which vector is `|0>`, which is `|+>`, and which is `|Phi+>`.
- What CX does to each computational basis input, and why a basis input is not an entangled output.
- Why Qiskit prints qubit 0 on the right of a bitstring.
- What your 1024 local shots were, and why an uneven split of `00` and `11` can still be a perfect agreement score.
- Why that score does not prove entanglement, and why `<XX>` and `<YY>` are part of the description.
- What changed when the circuit was rewritten for a local device stand-in, including a case where depth grew.
- Whether you collected a hardware result. If you did not, you say that.
- The four stops of the memory walk, in your own pictures, and the fact each stop points back to: the state columns, what I, X, H, and CX do, the CNOT rule, and `|Phi+>`.
