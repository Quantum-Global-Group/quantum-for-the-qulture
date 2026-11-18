# Contributing

Quantum for the Qulture is an initiative of Quantum Global Group. This repository holds the public learning pathway: documentation, labs, templates, and the offline checks that keep Lab 001 honest.

The license is not settled. Read [LICENSE](LICENSE) before you copy material out of this repository or send a contribution you need to relicense. Kevin A. Robinson has to approve the final license.

## How to propose a change

Open a pull request against `main`. Describe what a learner can do after the change that they could not do before. A new lab should follow [templates/lab-template/README.md](templates/lab-template/README.md), [templates/lesson-template/LESSON.md](templates/lesson-template/LESSON.md), and [templates/worksheet-template/WORKSHEET.md](templates/worksheet-template/WORKSHEET.md). Lab 001 is the working example of that pattern.

Do not add an empty course folder or a notebook that does not run.

## What stays out of git

Never commit an API token, an account key, a Cloud Resource Name, a password, a `.env` file, a saved Qiskit account file, a learner email, a waitlist, or a community export. The public access policy is in [docs/qpu-access.md](docs/qpu-access.md). The handling rules are in [docs/security-and-privacy.md](docs/security-and-privacy.md).

Hardware is optional. `RUN_REAL_HARDWARE` in Lab 001 stays `False` in the committed notebook. Do not submit a quantum job from a test, a script in this repository, or a continuous-integration run.

## Check before you open the pull request

From a clean environment, with no IBM credentials:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python tests/smoke_lab001.py
```

The smoke test checks the Bell-state mathematics, the 18 beginner questions, the local sampler, local transpilation, relative links, and the hardware flags. It runs the beginner notebook's local cells with both hardware switches off. It does not contact IBM and it does not submit a job.

## Documentation

One topic has one canonical page. Update that page instead of starting a second copy. The map is in [docs/documentation-guide.md](docs/documentation-guide.md). When a page depends on an external product, name the page you checked and the date you checked it.
