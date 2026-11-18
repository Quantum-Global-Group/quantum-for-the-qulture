# Worksheet. Entanglement, from your hands to real hardware

Lab 001 of Quantum for the Qulture, an initiative of Quantum Global Group.

You can complete this sheet from the notebook, from a class demonstration, or from the Qubi observation plus the printed results. Write the prediction before you see the run. Lines are there so the reasoning has somewhere to go.

Name:

Date:

I am working at level: 1 see and understand / 2 code and simulate / 3 hardware

## Readiness

I can add vectors and I know what a square root is.

Yes / Not yet. What I need:

_________________________________________________________________

I can run a Python notebook, or I am pairing with someone who can.

Yes / Not yet.

I have an IBM Classroom seat.

Yes / No. I do not need one for levels 1 and 2.

## Vocabulary

After you meet each word, write a definition you could say out loud.

| Word | My definition |
| --- | --- |
| Qubit | |
| State | |
| Basis | |
| Gate | |
| Circuit | |
| Measurement | |
| Probability | |
| Observable | |
| Backend | |
| Superposition | |
| Amplitude | |
| Entanglement | |
| Shot | |

## States

Match the label to the vector. Use the order `|0>`, then `|1>`, for one qubit, and the Qiskit order for two qubits (the rightmost bit is qubit 0).

| Label | Vector I wrote |
| --- | --- |
| `|0>` | |
| `|1>` | |
| `|+>` | |
| `|->` | |
| `|00>` | |
| `|Phi+>` | |

Which of these is a superposition?

_________________________________________________________________

What does the relative minus sign in `|->` change, if both amplitudes have the same size?

_________________________________________________________________

## CNOT

Control is qubit 0. Target is qubit 1. Fill the target-after column yourself, then the two ways of writing the result.

| Control | Target before | Target after | Written as control then target | Qiskit bitstring, target then control |
| --- | --- | --- | --- | --- |
| 0 | 0 |  |  |  |
| 0 | 1 |  |  |  |
| 1 | 0 |  |  |  |
| 1 | 1 |  |  |  |

A computational-basis input stays unentangled after CNOT. Write one input that does become entangled, and say what you do to the control before the CNOT.

_________________________________________________________________

_________________________________________________________________

## Observables

Draw a line from the observable to the beginner meaning that matches it.

- I
- X
- Y
- Z

Meanings:

- Leaves every state with expectation +1.
- Distinguishes `|0>` and `|1>`.
- Distinguishes `|+>` and `|->`.
- Is sensitive to the imaginary relative phase.

For `|Phi+>`, write the three expectations the lab computes.

`<ZZ>` =

`<XX>` =

`<YY>` =

What does `<ZZ> = +1` say about a pair of computational-basis bits?

_________________________________________________________________

## Circuit prediction

Start in `|00>`. You will apply H to qubit 0, then CX with control 0 and target 1.

The state I expect after H, before CX:

_________________________________________________________________

The state I expect after CX:

_________________________________________________________________

The bitstrings I expect to see, and the ones I expect not to see:

_________________________________________________________________

## Local observations

Seed, if you used one:

Shots:

Counts:

`00`:

`11`:

`01`:

`10`:

Agreement `(n00 + n11) / shots`:

The split between `00` and `11` was not exactly half. What should I call that effect?

_________________________________________________________________

## Hardware observations

Leave this blank if you did not submit a job. An empty section is an honest result.

Backend name:

Shots:

Counts:

One thing that differed from the local sample, if you have both:

_________________________________________________________________

I did not run hardware. What I used instead:

_________________________________________________________________

## Interpretation

What state were we trying to prepare?

_________________________________________________________________

What did we actually measure?

_________________________________________________________________

Which basis was that measurement in?

_________________________________________________________________

What can I defend from this evidence?

_________________________________________________________________

What is still missing?

_________________________________________________________________

What measurement would help next?

_________________________________________________________________

## Memory walk

This is Jonas von Essen's public practice, not a copied course. Pick a place you already know. Put one picture at each stop. The picture is yours. The fact in the middle column is the part you still have to be able to say with the notebook closed.

My place:

_________________________________________________________________

| Stop | The fact I must still say | My image |
| --- | --- | --- |
| States | `|0>`, `|1>`, `|+>`, `|->` as columns | |
| Gates | What I, X, H, and CX each do | |
| CNOT | Control 0 leaves the target. Control 1 flips it. Which way I write the bits. | |
| Bell | H on qubit 0, then CX(0, 1), is `(|00> + |11>) / sqrt(2)` | |

Date I walked it with the notes closed:

What was blank:

Next walk. Longer gap if the stops came back. Shorter gap if one was blank:

_________________________________________________________________

## Reflection

One sentence I could use to explain this state to a friend, without saying that one qubit sends a message to the other:

_________________________________________________________________

_________________________________________________________________

## Career exploration

From [the career page](../../docs/career-pathways.md), one role I recognize from work I have already done:

_________________________________________________________________

The prerequisite I would still need:

_________________________________________________________________

The role-specific training this lab did not give me:

_________________________________________________________________

Lab 001 does not qualify me for that role. What I might do in the next month anyway:

_________________________________________________________________
