# Instructor guide. Lab 001

Entanglement: From Your Hands to Real Hardware.

An initiative by Quantum Global Group. Use this guide with the [notebook](entanglement_hands_to_hardware.ipynb) and the [worksheet](STUDENT_WORKSHEET.md). The notebook is the student-facing explanation. This page is the plan, the answers you should expect, and the places a room usually gets stuck.

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
- Optional: Qubi kits and Qolour's Bell Pairs lesson, linked from [../../qubis/bell-pairs/README.md](../../qubis/bell-pairs/README.md). Test the link before class. If it fails, use the prompts in notebook section 08.
- Optional hardware: one invited account, used by the instructor, for a single job. The simulation is the planned backup, not a disappointment.

## Qubi preparation

Do the physical activity before the algebra if the kits are in the room. Ask the five prompts and collect observations on a board. Do not invent extra controls. Do not skip ahead to "they are entangled" before the group has said what it saw.

If you are virtual, share the official lesson only when you have confirmed it loads. Otherwise read the prompts and ask people to predict a pattern. Say clearly that a verbal stand-in is not the physical model.

## Classroom readiness

- Install from `requirements.txt` before the session if learners will run level 2. Python 3.10 or newer. The published run used Python 3.12.3, Qiskit 2.6.2, NumPy 2.5.5, and Matplotlib 3.11.2.
- Run `python tests/smoke_lab001.py` on the instructor machine the day of class.
- Confirm the notebook still has `RUN_REAL_HARDWARE = False`.
- Decide in advance whether any hardware job will be run. If yes, it is one job, after the local result is on screen.

## IBM requirements

None for the lesson to succeed. A Classroom seat is required only for the optional demonstration. Policy: [../../docs/qpu-access.md](../../docs/qpu-access.md). Do not put a learner email or an instance identifier on a slide or in the repository.

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

Skip the estimator detail and both transpilation examples. Assign them as a follow-up for level 2.

### 90 minutes

Add the observable table and the three expectations. Have the group compute the agreement metric from the counts on the screen. Discuss why an agreement of 1 is still not proof. Show the circuit drawing and the bit-order example with X on qubit 0.

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
