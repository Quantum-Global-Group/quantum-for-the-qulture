# Documentation guide

Each important topic has one canonical page. Add a link to that page instead of pasting a second copy. If two pages disagree, fix them in the same change.

## Canonical pages

| Topic | Page |
| --- | --- |
| Public front door | [../README.md](../README.md) |
| Purpose | [vision.md](vision.md) |
| How we teach | [learning-philosophy.md](learning-philosophy.md) |
| Path a learner walks | [learner-journey.md](learner-journey.md) |
| Systems around the lab | [architecture.md](architecture.md) |
| What to do today | [getting-started.md](getting-started.md) |
| Levels and Lab 001's place | [learning-pathway.md](learning-pathway.md) |
| Install and APIs | [ibm-quantum-setup.md](ibm-quantum-setup.md) |
| Classroom seat policy | [qpu-access.md](qpu-access.md) |
| Secrets and personal data | [security-and-privacy.md](security-and-privacy.md) |
| Roles, at an introductory level | [career-pathways.md](career-pathways.md) |
| Certification as a later path | [certification-journey.md](certification-journey.md) |
| Work that is not built | [../ROADMAP.md](../ROADMAP.md) |
| Official external pages | [../resources/official-docs.md](../resources/official-docs.md) |
| Qubi Bell Pairs pointer | [../qubis/bell-pairs/README.md](../qubis/bell-pairs/README.md) |
| Lab 001 | [../labs/01_entanglement/README.md](../labs/01_entanglement/README.md) |

## Writing rules

- Prefer a short page a person can finish on a phone. Use headings, then prose. Use a table when the rows are real parallel facts.
- Relative links only, inside the repository.
- Introduce a term before you rely on it. Point to the lab or the page that defines it.
- When you cite a product's behavior, name the official page and the date you opened it. Do not write that a page was checked if it was not.
- Do not invent a community URL, a video, or a download.
- Do not copy third-party lessons into this repository. Link them.
- Callouts are defined in [learning-philosophy.md](learning-philosophy.md). Use them for an action, not for decoration.

## Find it in the docs

A "find it in the docs" activity names one official page and one thing to look for, such as the signature of a class or the convention for bit order. The activity fails if the page has moved. Update the link. Do not paste the vendor page into our docs to avoid that maintenance.

## Notebooks

A lab notebook is documentation and code together. The code has to run from top to bottom with no credentials. Predictions are written before the cell that checks them. Outputs that are committed were produced by a run. Do not hand-edit an output to make a result look cleaner.

## Templates

New labs start from [../templates/](../templates/). If the template and Lab 001 drift, update the template so the next lab inherits the correction.
