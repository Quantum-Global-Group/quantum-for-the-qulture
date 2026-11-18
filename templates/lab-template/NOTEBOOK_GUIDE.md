# Notebook guide

Use this outline for a new lab notebook. Keep the code that teaches visible in the notebook. Do not hide the calculation in a module the learner never sees.

Lab 001 follows this shape: [../../labs/01_entanglement/entanglement_hands_to_hardware.ipynb](../../labs/01_entanglement/entanglement_hands_to_hardware.ipynb).

## Cell pattern

A section is a short markdown explanation, then a code cell, then a few sentences of interpretation. Predictions are markdown that appears before the code that checks them.

Every code cell must run after the cells above it, with no IBM credentials. Set a seed when a sample should be reproducible, and say that a different seed moves the finite counts.

## Required habits

- Name constants for shots and for any hardware flag. The hardware flag defaults to `False`.
- Import hardware libraries only inside the branch that runs when the flag is true.
- Print backend name, circuit, shots, and counts. Do not print tokens, instance identifiers, or exception messages.
- If a hardware path cannot run, say so. Do not invent counts.
- Use current Qiskit primitives. Do not call `IBMQ.load_account()` or `execute()`.
- When you show a transpiled circuit, say which local backend you used. Do not claim that depth always falls.
- Point each major idea at one official page with a FIND IT IN THE DOCS line.

## Section skeleton

Adapt the titles. Do not add a section you cannot finish.

1. Welcome. The question, in the learner's words, as a QULTURE CHECK.
2. Access. Three levels, and a pointer to the access policy.
3. Environment. Print the package versions you tested.
4. Language. One definition per term you will use.
5. The mathematical objects.
6. The operation, including a case that does the interesting thing and a case that does not.
7. The measurement or observable.
8. The "see it" activity, with a real link or an honest statement that the link is not ready.
9. Map, on paper or in vectors, before the framework.
10. Build the circuit and draw it.
11. Simulate locally. Predictions first.
12. Name the primitive and show the PUB you actually passed.
13. Transpile on a documented local backend.
14. Hardware, off by default.
15. Compare ideal, local, and hardware-if-any.
16. Interpret. What is missing.
17. Where this sits relative to an external credential, checked against a live page.
18. Reflection and one next step.

## Setup cell you can copy

```python
import qiskit
import numpy as np

SEED = 7
SHOTS = 1024
RUN_REAL_HARDWARE = False

print("qiskit", qiskit.__version__)
print("numpy", np.__version__)
print("RUN_REAL_HARDWARE", RUN_REAL_HARDWARE)
print("This cell does not read an IBM account.")
```

Change `SEED` only if you re-run the notebook and commit the new outputs. Do not hand-edit outputs.
