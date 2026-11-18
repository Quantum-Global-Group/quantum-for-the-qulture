# Security and privacy

The public materials can be cloned by anyone. Treat every file in the repository as public, including files in a pull request.

## Never commit

- API tokens, keys, passwords, or session cookies.
- IBM instance identifiers, including a Cloud Resource Name.
- A saved Qiskit account file, a `.env` file, or a private key.
- Learner names paired with emails, waitlists, seat assignments, or community exports.
- Invitation URLs for the Classroom.

`.gitignore` excludes the usual filenames. Ignore rules are a backstop, not a review. Read the diff before you commit.

If a secret lands in a commit, rotating the secret matters more than rewriting the story. Tell the founder. Assume the secret is copied.

## Hardware jobs

`RUN_REAL_HARDWARE` defaults to `False`. The smoke test checks that the committed notebook keeps it that way. Tests, local checks, and any future automation must not flip the flag and must not submit a job.

When a learner does run hardware, the notebook may print the backend name, the qubit count, the transpiled circuit, the shot count, and the counts. It must not print the account, the token, or the instance identifier. Error handling prints the exception type, not the message, so an error string cannot echo a secret into the notebook output.

## Personal data

This repository is the wrong place for a roster. Access requests are described as policy in [qpu-access.md](qpu-access.md) and are collected, if at all, in the learning community. Do not open an issue that contains a learner's email or an account identifier. If someone else does, remove it and ask them to rotate anything that was exposed.

## Results

Counts and circuits from Lab 001's local simulator are not personal data. A hardware job identifier might be tied to an account. The committed notebook does not contain one, and the hardware section does not print one.

## Claims

Do not publish a result you did not run. The notebook's hardware branch says when it did not run. The local counts are labeled as local counts.

## Where account data lives

`QiskitRuntimeService.save_account`, when a learner chooses to use it, writes outside this repository by default. Keep it that way. Instructions are in [ibm-quantum-setup.md](ibm-quantum-setup.md).
