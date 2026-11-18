# Official documentation

These are primary sources for this pathway. Pages were opened on 18 November 2026 unless a row says otherwise. Open them again when you teach, because the products change. If a page and a lab disagree about Qiskit or IBM Quantum, the official page wins for the product, and the lab should be corrected.

We link these sources. We do not copy their courses into this repository.

## Start here, outside this repository

| Source | What to look for |
| --- | --- |
| [IBM Quantum documentation](https://quantum.cloud.ibm.com/docs/) | The current entry point for Qiskit and IBM Quantum Platform. |
| [IBM Quantum Learning](https://quantum.cloud.ibm.com/learning/) | Courses and classroom modules. Lab 001 is not a substitute for a course. |
| [Qolour](https://www.qolour.com/) | The organization that makes Qubi, the physical model qubit. |
| [Qolour, Bell Pairs lesson](https://www.qolour.com/educator-course/bell-pairs) | The hands-on lesson. Stop 1 of the beginner notebook and section 08 of the advanced notebook both point here. |
| [Qolour Quickstart](https://www.qolour.com/quickstart) | Battery, orientation, app, and firmware steps for a physical Qubi. Opened 18 November 2026. |
| [Qolour, send a Qubi activity to a quantum computer](https://www.qolour.com/send-to-qc) | The app's own route. It is separate from the Lab 001 notebook. Opened 18 November 2026. |

## Pages Lab 001 uses

| Topic | Page |
| --- | --- |
| Local Sampler and Estimator, and PUBs | [Exact simulation with Qiskit SDK primitives](https://quantum.cloud.ibm.com/docs/en/qiskit/simulate-with-qiskit-sdk-primitives) |
| Bit order, including how strings are printed | [Bit-ordering in the Qiskit SDK](https://quantum.cloud.ibm.com/docs/en/qiskit/bit-ordering) |
| Preset transpiler pass manager | [generate_preset_pass_manager](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.transpiler.generate_preset_pass_manager) |
| StatevectorSampler | [StatevectorSampler API](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.primitives.StatevectorSampler) |
| StatevectorEstimator | [StatevectorEstimator API](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.primitives.StatevectorEstimator) |
| Hardware sampler, client-side primitive | [Sampler quickstart](https://quantum.cloud.ibm.com/docs/en/ibm-quantum-compute/get-started-with-sampler) |
| Why the import changed in 0.50 and 0.52 | [Migrate from server-side to client-side Sampler and Estimator](https://quantum.cloud.ibm.com/docs/en/guides/migrate-to-client-side-primitives) |
| Account service | [QiskitRuntimeService](https://quantum.cloud.ibm.com/docs/en/api/qiskit-ibm-runtime/qiskit-runtime-service) |
| Current certification, credential C9008400 | [IBM Certified Quantum Computation using Qiskit v2.X Developer - Associate](https://www.ibm.com/training/certification/ibm-certified-quantum-computation-using-qiskit-v2x-developer-associate-C9008400) |

The withdrawn v0.2X credential was still described, as withdrawn, on IBM's page for credential C0010300 on the same date. Lab 001 does not teach toward that exam. See [../docs/certification-journey.md](../docs/certification-journey.md).

## Versions named by those pages

The primitives guide and the bit-ordering guide said their examples were developed with `qiskit[all]~=2.6.1` or newer. This repository tests `qiskit==2.6.2`.

The sampler quickstart said its older sample was developed with `qiskit-ibm-runtime~=0.47.0`, and the same page also showed the client-side sampler introduced in 0.50.0. The release notes and the package imported locally on 18 November 2026 identify 0.52.1 as a version in which the top-level `Sampler` is that client-side class. Lab 001 follows the 0.52.1 import, not the 0.47 sample, and does not execute it.

## A documentation exercise

Pick one row above. Open the page. Find the sentence or signature the lab relies on. If it has moved, write down the new location and update the lab in a pull request. That exercise is the "find it in the docs" habit used inside Lab 001.
