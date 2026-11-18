# Instructor guide. Lab 001

Entanglement: From Your Hands to Real Hardware.

An initiative by Quantum Global Group. Use this guide with the [beginner notebook](entanglement_beginner.ipynb), the [advanced notebook](entanglement_hands_to_hardware.ipynb), and the [worksheet](STUDENT_WORKSHEET.md). The beginner notebook is the first experience. The advanced notebook keeps the original mathematics, the statevectors, the purity analysis, and the experiments. The worksheet follows the advanced notebook. This page is the plan, the answers you should expect, and the places a room usually gets stuck.

## Beginner session

Use this cut when the room is meeting entanglement for the first time. The advanced timing below still applies when the room is working through the original notebook.

| Minutes | Focus |
| --- | --- |
| 5 | The route on the first screen. Hardware stays off. Name who has Qubis and who is on the no-Qubi story. |
| 10 | Stop 1. Battery, Bluetooth, orientation, and the pair activity if the kits are in the room. Otherwise the shared classical bit. Each person writes the three notes. |
| 15 | Q01 through Q05, then the Phi Plus circuit and the bit-order check. One letter at a time. The explanation waits for the letter. |
| 15 | Sampler counts, then Phi Plus against Phi Minus in Z and in X. |
| 10 | ZZ and XX with Estimator, or assign them if the hour is short. |
| 5 | Show the mock transpilation. Read the hardware cell and leave both flags false. Close with the four sentences. |

A wrong answer should get a short reason and one practice question, then the letter that fits. Do not move on by announcing the letter before the learner has chosen. The score lives in that kernel. It is not a grade book and it is not the certification exam.

The published local sample, seed 7 and 512 shots on Qiskit 2.6.2, is 241 of `00` and 271 of `11` for Phi Plus in Z and in X, and for Phi Minus in Z. Phi Minus in X is 241 of `01` and 271 of `10`. Estimator returns +1, +1 for Phi Plus ZZ and XX, and +1, -1 for Phi Minus ZZ and XX. If a later Qiskit build moves the finite counts, say so. Do not replace them with a hardware story.

### Beginner answer key

| Question | Letter | The idea the letter protects |
| --- | --- | --- |
| Q01 | B | Qubis are a teaching model. |
| Q02 | A | Only 00 and 11 is Z-basis correlation. |
| Q03 | C | H on qubit 0 creates a superposition. It does not entangle. |
| Q04 | B | H then CX(0, 1) prepares Phi Plus. |
| Q05 | C | The string 01 means q1 is 0 and q0 is 1. |
| Q06 | B | X on qubit 0 moves Phi Plus to the pair 01 and 10. |
| Q07 | C | Z on qubit 0 changes the relative sign to Phi Minus. |
| Q08 | A | Phi Plus and Phi Minus share the Z histogram. |
| Q09 | C | 512 shots land near an even split and may miss it. |
| Q10 | A | `result[0].data.meas.get_counts()` reads the first PUB. |
| Q11 | B | H on both qubits turns the Z readout into an X question. |
| Q12 | A | ZZ on Phi Plus is +1. |
| Q13 | B | XX on Phi Minus is -1. |
| Q14 | B | One PUB, and the shot count applies to each parameter setting. |
| Q15 | C | `assign_parameters` returns a new circuit by default. |
| Q16 | B | Transpilation rewrites a logical circuit into an ISA circuit. |
| Q17 | C | Predict, simulate, then authorize one job on purpose. |
| Q18 | C | Z correlation is real. A Bell inequality is a different experiment. |

## Objectives

By the end, a learner can:

- Identify `|0>`, `|1>`, `|+>`, `|->`, `|00>`, and `|Phi+>` as vectors.
- Apply the CNOT rule on the computational basis and state an input that does not become entangled.
- Explain Qiskit bit order: qubit 0 is the rightmost character.
- Build H on qubit 0 and CX(0, 1), and match the statevector to `|Phi+>`.
- Read a 1024-shot local sample, including an uneven `00`/`11` split and an agreement of 1.
- Say why those counts do not prove entanglement or Bell nonlocality, and quote `<ZZ> = +1`, `<XX> = +1`, `<YY> = -1`.
- Describe one local transpilation where the basis changed and one where routing increased depth.
- Leave hardware off unless the room has an approved seat and a reason to spend one job.

## Prerequisites

Arithmetic, the idea of a column vector, and, for level 2, a working Python environment. Physics degrees and IBM accounts are not prerequisites. Learners who cannot install software can stay on level 1 while someone else runs the notebook.

## Materials

- Printed worksheets.
- A way to display the notebook, or one laptop per pair.
- Optional: Qubi kits and Qolour's Bell Pairs lesson, linked from [../../qubis/bell-pairs/README.md](../../qubis/bell-pairs/README.md). Test the link before class. If it fails, use Stop 1 of the beginner notebook or the prompts in section 08 of the advanced notebook.
- Optional hardware: one invited account, used by the instructor, for a single job. The simulation is the planned backup, not a disappointment.

## Qubi preparation

Do the physical activity before the algebra if the kits are in the room. Ask the five prompts and collect observations on a board. Do not invent extra controls. Do not skip ahead to "they are entangled" before the group has said what it saw.

If you are virtual, share the official lesson only when you have confirmed it loads. Otherwise read the prompts and ask people to predict a pattern. Say clearly that a verbal stand-in is not the physical model.

## Classroom readiness

- Install from `requirements.txt` before the session if learners will run level 2. Python 3.10 or newer. The published run used Python 3.12.3, Qiskit 2.6.2, NumPy 2.5.5, and Matplotlib 3.11.2.
- Run `python tests/smoke_lab001.py` on the instructor machine the day of class.
- Confirm the beginner notebook still has `RUN_REAL_HARDWARE = False` and `I_AUTHORIZE_ONE_QPU_JOB = False`, and the advanced notebook still has `RUN_REAL_HARDWARE = False`.
- Decide in advance whether any hardware job will be run. If yes, it is one job, after the local result is on screen.

## IBM requirements

None for the lesson to succeed. A Classroom seat is required only for the optional demonstration. A learner requests that seat in the [Skool community](https://www.skool.com/quantum-for-the-qulture-8361), after Start Here, by submitting the email address that should receive the IBM invitation. Kevin A. Robinson reviews the request and sends the invitation himself. There is no public invite link. Policy: [../../docs/qpu-access.md](../../docs/qpu-access.md). Do not put a learner email or an instance identifier on a slide or in the repository.

## Timing

### 60 minutes

| Minutes | Focus |
| --- | --- |
| 5 | Welcome, the question, the level each person is on. |
| 10 | Qubi prompts, or the five written prompts if there is no kit. |
| 15 | `|0>`, `|+>`, CNOT rule, one entangled input and one that is not. |
| 15 | Build the circuit, draw it, run the local sampler. |
| 10 | Interpretation and one career sentence. |
| 5 | Where the rest of the notebook lives for later. |

Skip the estimator detail and both transpilation examples. Assign them as a follow-up for level 2. The memory walk in section 10 is homework for this cut. The pictures are hints the learner may replace. The columns and the CNOT table are still the answers.

### 90 minutes

Add the observable table and the three expectations. Have the group compute the agreement metric from the counts on the screen. Discuss why an agreement of 1 is still not proof. Show the circuit drawing and the bit-order example with X on qubit 0. Take five minutes for each person to name four stops in a place they know. Do not spend the time perfecting the pictures.

### 120 minutes

Add primitives and the printed PUB. Run both local transpilation examples and ask the room which depth went up and why that is allowed. If a seat is available and you planned it, the instructor submits one hardware job and the group writes the hardware box. Otherwise say that the box stays blank and move to reflection. Virtual and in-person versions use the same 120-minute outline. The only planned difference is whether Qubi is physical or prompted.

## Discussion prompts

- What did the hands show that the vector makes precise?
- Why is `|01>` not in `|Phi+>`?
- CNOT copied a bit in the basis table. What else has to be true before the output is entangled?
- If `00` appears 517 times and `11` appears 507 times, what is broken? The expected answer is: nothing in the state. The sample is finite.
- What would a classical mixture of `|00>` and `|11>` produce in the Z basis?

## Misconceptions to correct when they appear

- "The qubits message each other." The circuit prepares one joint state. The correlations are properties of that state.
- "The memory picture is the state." The picture is a hint back to the column, the gate, or the circuit. Those remain the answer.
- "CNOT means entanglement." Show CX on `|00>`, which stays a basis state. Then show H on the control first.
- "Only `00` and `11` proves the Bell state." A mixture can do that in the computational basis. The X and Y expectations are part of the distinction. A Bell inequality is Lab 004, which is not written yet.
- "The simulator run was a quantum computer." It was a local statevector sample. Say the backend name if you do run hardware, and do not blur the two.
- "Depth should have gone down." In the published local examples it does not. Basis change and routing can add gates.
- "I am ready for a quantum job." The career page says this lab is not a qualification. Repeat that without apology.

## Outcomes to look for on the worksheet

- CNOT table: target after is 0, 1, 1, 0. Control-then-target strings: 00, 01, 11, 10. Qiskit strings: 00, 10, 11, 01.
- `|Phi+>` amplitudes about 0.7071 on `|00>` and `|11>`, and 0 elsewhere.
- Expectations +1, +1, and -1 for ZZ, XX, and YY.
- Local counts from the seeded notebook: `00` is 517 and `11` is 507 when the seed is 7 and the shots are 1024. Agreement is 1. Another seed is allowed if the learner says so. Leakage into `01` or `10` on this simulator means the circuit was changed.
- Hardware box blank, unless you actually ran a job and the learner copied those counts.

## Troubleshooting

- Import error: the environment does not have the pinned packages. Do not debug by skipping the virtual environment.
- Sampler complains about measurements: the sampled circuit needs `measure_all`. The estimator circuit must not include measurements.
- Counts are `01` when the learner expected `10`: they put X on the other qubit, or they are reading the string backwards. Run the one-qubit check in section 06.
- Someone sets the hardware flag and has no account: the cell prints an exception type and invents nothing. Thank them for the test, set the flag back to `False`, and continue with the local counts.
- Qolour's page does not load: use the prompts. Do not substitute a random video.
- A learner pastes a token into chat or into a cell: stop, have them revoke it, and do not commit the notebook.

## Optional hardware demo

Only if you planned it, you have a seat, and the local result is already visible. Change the flag in an unsaved copy, or in a copy that will not be committed. Submit the one job the notebook describes. Read the backend name and the counts. Compare them with the ideal state using the questions in section 16. If the queue is long, do not wait past the point where interpretation gets rushed. The local result is a complete close for the session.

## Simulation backup

The seeded local sample is the backup and the default. Tell the room the numbers came from `StatevectorSampler`, seed 7, 1024 shots. That is a precise statement, and it is enough.
