# IBM Quantum setup

This page is technical preparation for a learner who already has access. It does not invite you, and it does not collect your email. The access policy is [qpu-access.md](qpu-access.md).

Lab 001 does not need any of the account steps below. Levels 1 and 2 use the packages in [../requirements.txt](../requirements.txt) only.

## Versions checked for this release

Checked on 18 November 2026, with Python 3.12.3, and with no IBM credentials in the environment.

| Package | Version | Role |
| --- | --- | --- |
| qiskit | 2.6.2 | Circuits, statevectors, local primitives, transpiler |
| numpy | 2.5.5 | Arrays used by those objects |
| matplotlib | 3.11.2 | The counts chart in Lab 001 |
| qiskit-ibm-runtime | 0.52.1 | Imported locally to confirm symbols. Not used to open an account or submit a job. Not required for Lab 001. |

Qiskit 2.6.2 requires Python 3.10 or newer. The local notebook was executed against the three required packages. The runtime package was inspected for import paths only.

Official pages opened the same day are listed in [../resources/official-docs.md](../resources/official-docs.md). Product interfaces change. If you are setting up months later, read those pages again before you copy a snippet.

## Local path, which is the default

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python tests/smoke_lab001.py
```

Then open the Lab 001 notebook and run it with `RUN_REAL_HARDWARE` left `False`.

The notebook uses `QuantumCircuit`, `Statevector`, `StatevectorSampler`, `StatevectorEstimator`, and `generate_preset_pass_manager`. Those are current Qiskit SDK interfaces. The local sampler and estimator are the reference implementations of the version-2 primitive interfaces. A primitive unified bloc, or PUB, is the tuple you hand to `run`. Lab 001 prints the tuples it uses.

Retired interfaces are not used. In particular, the notebook does not call `IBMQ.load_account()` and does not call `execute()`.

## Hardware path, after an invitation

Use this section only after Kevin A. Robinson has sent you an IBM invitation. The request is made in the [Skool community](https://www.skool.com/quantum-for-the-qulture-8361): join, complete [getting-started.md](getting-started.md), and submit there the email address that should receive the invitation. He sends the invite himself. This page has no IBM invite link, and it does not ask you to record that email.

Install the runtime package only when you are ready to use a seat:

```bash
pip install qiskit-ibm-runtime==0.52.1
```

Save the account on your own machine, outside this repository. The IBM documentation for `QiskitRuntimeService.save_account` is the source of truth for the arguments. The values you will need are an API key and, preferably, the instance identifier your administrator gave you. That identifier is a Cloud Resource Name. It is a secret in practice. Do not paste it into a notebook, a pull request, a chat, or a file under this clone.

A saved account belongs in the location the SDK chooses under your home directory, or in another path outside the repository. This repository's `.gitignore` excludes `.env`, `.qiskit/`, and common key filenames in case a tool writes them into the clone anyway. Deleting a secret from a later commit does not remove it from history. Do not commit it the first time.

When the notebook's hardware flag is set in your private copy, the code does four things:

1. It constructs `QiskitRuntimeService()` with no token in the source, so the saved account is read from your machine.
2. It selects an operational backend with `least_busy(min_num_qubits=2, operational=True, simulator=False)`.
3. It transpiles with `generate_preset_pass_manager` and submits one sampler job of 1024 shots through the client-side `Sampler` (`from qiskit_ibm_runtime import Sampler`). In version 0.52.1 that name is the client-side primitive, and `SamplerV2` is an alias of the same class. The older server-side sampler lives under `qiskit_ibm_runtime.server_side` and is not the path this lab uses.
4. It prints the backend name, the qubit count, the transpiled circuit, the shot count, and the counts. It does not print the token, the instance identifier, or the account.

As of the 0.52.1 source inspected locally, `least_busy` still accepts `operational` and `simulator` as filters. That matches the `backends` examples in the installed package. Confirm the signature in the version you install before you rely on it.

If the hardware path cannot run, the notebook tells you the exception type and stops. It does not invent counts. Your local sample from earlier in the notebook is still a valid result for the foundations.

## Bit order

Qiskit's own bit-ordering guide is part of Lab 001, because the printed strings are easy to misread. On the local sampler we tested, the rightmost character is qubit 0. The same IBM guide says some service primitives have returned big-endian strings, while Executor returns little-endian strings. The client-side sampler delegates to Executor. Even so, the lab asks a hardware user to check order with a known one-qubit circuit before interpreting a Bell-state string. This repository did not run that check on a device.

## What we could not verify

No real backend was queried. No job was submitted. Transpilation in the notebook uses `GenericBackendV2` from `qiskit.providers.fake_provider`, which is a local stand-in with a coupling map we specify. The word "fake" in that module name means the device is local. The lab does not use it to fabricate hardware counts.
