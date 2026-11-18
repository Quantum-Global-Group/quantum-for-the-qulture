# QPU access policy

Quantum for the Qulture learners may request access to our IBM Quantum Classroom while capacity is available. Invitations are managed through our learning community.

This page is the public policy. It is not an application form. Do not send an email address, a roster, or an account identifier into this repository.

## What a seat is

A Classroom seat is permission to use our IBM Quantum instance for approved learning activities. Capacity is about 100 seats. That number is a limit, not a target. Unused seats may be reassigned. Seats are also held for instructors, collaborators, workshops, and testing, so the program does not plan to fill every seat with individual learners.

Access is not unlimited, and it is not automatic. A request can be declined or delayed because the work does not need hardware yet, or because capacity is being held for a class.

## How a request moves

A person, not a script in this repository, does each step.

1. Join the learning community. The community is hosted on Skool. The link will be added when the founder supplies it.
2. Complete [getting-started.md](getting-started.md), including a local run of Lab 001.
3. Request access in the community, using the questions below.
4. An administrator reviews the request.
5. If a seat should be used, the administrator sends a manual invitation.
6. The learner accepts the invitation on IBM's own site.
7. The learner completes [ibm-quantum-setup.md](ibm-quantum-setup.md).
8. The learner runs an approved hardware activity, starting with the optional section of Lab 001, one job at a time.

This repository does not send invitations, does not store the invitation URL, and does not keep an admin page.

## Questions an administrator should ask

Ask these in the community, not in git.

- Which email address should receive the IBM invitation?
- What is your experience with quantum computing so far?
- Why do you need a quantum processor for the work in front of you, rather than the local simulator?

Those answers are personal data. They stay in the community tool that collected them.

## Seat states

Administrators may describe a seat with one of these words. This list is vocabulary. It is not a table of learners.

| State | Meaning |
| --- | --- |
| REQUESTED | A person has asked, and nobody has decided. |
| WAITLISTED | The request is reasonable, and no seat should be used yet. |
| INVITED | A manual invitation has been sent and not yet accepted. |
| ACTIVE | The person has accepted and may run approved activities. |
| INACTIVE | The person still holds a seat and is not using it. |
| RELEASED | The seat is free to assign again. |

A private tracker of who is in which state belongs outside this repository.

## How a learner should spend a seat

Run locally first. Decide what you expect. Then submit one job, look at it, and write the interpretation before you submit another. The notebook defaults to no hardware job so that opening the file is always safe.

Approved hardware activities are the labs that say so. Exploring the device out of curiosity still costs queue time that other learners need. If you are finished with the activity, say so, so the seat can return to RELEASED.

## What this policy does not do

It does not rank people. It does not claim that seats are almost gone. It does not promise that every request becomes an invitation. It does not connect this repository to an automation tool.
