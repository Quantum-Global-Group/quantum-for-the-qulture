# Start here

You can learn the foundations of Lab 001 with no IBM account and no quantum computer. Pick the level that matches what you want to do today. You can move up later.

## Level 1. See and understand

1. Read [vision.md](vision.md) if you want the purpose, or skip to the lab if you want the work.
2. Open [the Lab 001 overview](../labs/01_entanglement/README.md).
3. Open the beginner notebook, [entanglement_beginner.ipynb](../labs/01_entanglement/entanglement_beginner.ipynb), or follow a facilitator who runs it. Use [the worksheet](../labs/01_entanglement/STUDENT_WORKSHEET.md) when you move on to the advanced notebook.
4. If you are in a room with Qubi kits, use Stop 1 of the beginner notebook. The physical activity is Qolour's Bell Pairs lesson, linked from [the Qubi page](../qubis/bell-pairs/README.md). The advanced notebook keeps the same observation in section 08.

Stop here if your question was "what is this state, and what would a measurement show?"

## Level 2. Code and simulate

1. Install Python 3.10 or newer. This lab was run on Python 3.12.3.
2. Create a virtual environment and install the tested packages:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Confirm the offline check passes. It does not contact IBM and it does not need a token:

```bash
python tests/smoke_lab001.py
```

4. Open [labs/01_entanglement/entanglement_beginner.ipynb](../labs/01_entanglement/entanglement_beginner.ipynb) in Jupyter or Colab and run the cells from top to bottom. Leave `RUN_REAL_HARDWARE` and `I_AUTHORIZE_ONE_QPU_JOB` set to `False`. The advanced notebook, [entanglement_hands_to_hardware.ipynb](../labs/01_entanglement/entanglement_hands_to_hardware.ipynb), is the original reference. Leave its hardware flag `False` as well.

You now have your own counts. Write what they show, and what they do not show, on the worksheet.

## Level 3. Hardware, only if you mean it

Do this after level 2, and only after Kevin A. Robinson has sent you an IBM invitation. Join the [Skool community](https://www.skool.com/quantum-for-the-qulture-8361), complete this Start Here page, and submit in Skool the email address that should receive the invitation. He reviews that request and sends the invitation himself. There is no public IBM invite page. Read [qpu-access.md](qpu-access.md), then [ibm-quantum-setup.md](ibm-quantum-setup.md). This repository cannot grant a seat, and it does not store the email.

## The learning community

Join [Quantum for the Qulture on Skool](https://www.skool.com/quantum-for-the-qulture-8361). A community session adds video, a guided Qubi demonstration, discussion, and the hardware onboarding conversation. The notebook is not locked behind that membership.

Hardware access is requested in Skool after you finish Start Here. You submit the email address that should receive the IBM invitation. Kevin A. Robinson reviews the request and sends the invitation himself. Do not put that email in this repository.

## If you are teaching

Use [the instructor guide](../labs/01_entanglement/INSTRUCTOR_GUIDE.md). It has cuts for 60, 90, and 120 minutes, in person and virtual. The simulation is the backup when a kit or a device is unavailable.

## If you are looking for a role

Read [career-pathways.md](career-pathways.md) after the lab, not instead of it. Completing Lab 001 does not qualify you for a job.

## If something fails

- `ModuleNotFoundError`: the virtual environment is not active, or `pip install -r requirements.txt` did not finish.
- The smoke test fails on a clean install of the pinned versions: open an issue and paste the assertion, not a screenshot of any account page.
- You were about to paste a token into a file in this repository: stop. Tokens stay outside git. See [security-and-privacy.md](security-and-privacy.md).
