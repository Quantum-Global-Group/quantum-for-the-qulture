"""Offline checks for Lab 001.

Run from the repository root after installing requirements.txt.
No IBM credentials are read. No hardware job is submitted.
"""

from __future__ import annotations

import ast
import contextlib
import io
import json
import re
import sys
import warnings
from pathlib import Path

import numpy as np
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator, StatevectorSampler
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit.quantum_info import SparsePauliOp, Statevector, partial_trace
from qiskit.transpiler import generate_preset_pass_manager

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "labs" / "01_entanglement" / "entanglement_hands_to_hardware.ipynb"
BEGINNER = ROOT / "labs" / "01_entanglement" / "entanglement_beginner.ipynb"
SEED = 7
SHOTS = 1024
BEGINNER_SHOTS = 512

LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
SECRET_PATTERNS = (
    re.compile("AKIA" + r"[0-9A-Z]{16}"),
    re.compile("-" * 5 + "BEGIN"),
    re.compile("crn:" + "v1:"),
    re.compile("sk_" + "live_"),
    re.compile("x-access-" + "token"),
)
BANNED_PUBLIC_WORDS = (
    "Curs" + "or",
    "AI-gener" + "ated",
    "Chat" + "GPT",
    "Cla" + "ude",
)
# The beginner notebook tells a learner to paste a tutor prompt into a separate chat.
# That product name is allowed in that one file. It is still banned everywhere else.
CHAT_NAME = "Chat" + "GPT"
CHAT_NAME_ALLOWED = {BEGINNER.resolve()}


def bell_circuit() -> QuantumCircuit:
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.cx(0, 1)
    return circuit


def reduced_purity(circuit: QuantumCircuit) -> float:
    state = Statevector.from_instruction(circuit)
    reduced = partial_trace(state, [1])
    return float(np.real(reduced.purity()))


def check_bell_vector() -> None:
    state = Statevector.from_instruction(bell_circuit())
    expected = np.zeros(4, dtype=complex)
    expected[0] = 1 / np.sqrt(2)
    expected[3] = 1 / np.sqrt(2)
    if not np.allclose(state.data, expected):
        raise AssertionError(f"Bell vector mismatch: {state.data}")
    for label, value in (("ZZ", 1), ("XX", 1), ("YY", -1), ("ZI", 0), ("IZ", 0)):
        got = state.expectation_value(SparsePauliOp(label))
        if not np.allclose(got, value):
            raise AssertionError(f"{label} expectation {got}, expected {value}")


def check_cnot_and_entanglement() -> None:
    expected = {(0, 0): "00", (0, 1): "10", (1, 0): "11", (1, 1): "01"}
    for control, target in expected:
        circuit = QuantumCircuit(2)
        if control:
            circuit.x(0)
        if target:
            circuit.x(1)
        circuit.cx(0, 1)
        probabilities = Statevector.from_instruction(circuit).probabilities_dict()
        bitstring = str(max(probabilities, key=probabilities.get))
        if bitstring != expected[(control, target)]:
            raise AssertionError(
                f"CNOT {(control, target)} -> {bitstring}, expected {expected[(control, target)]}"
            )
        if reduced_purity(circuit) <= 0.99:
            raise AssertionError("Basis input became entangled under CNOT")

    product = QuantumCircuit(2)
    product.cx(0, 1)
    entangled = bell_circuit()
    target_superposition = QuantumCircuit(2)
    target_superposition.h(1)
    target_superposition.cx(0, 1)
    if reduced_purity(product) <= 0.99:
        raise AssertionError("CX on |00> should stay a product state")
    if reduced_purity(entangled) >= 0.51:
        raise AssertionError("H then CX should be entangled")
    if reduced_purity(target_superposition) <= 0.99:
        raise AssertionError("H on the target should stay a product state")


def check_sampler_and_estimator() -> None:
    measured = bell_circuit()
    measured.measure_all()
    counts = (
        StatevectorSampler(seed=SEED)
        .run([(measured,)], shots=SHOTS)
        .result()[0]
        .data.meas.get_counts()
    )
    parsed = {str(bit): int(value) for bit, value in counts.items()}
    if parsed.get("01", 0) or parsed.get("10", 0):
        raise AssertionError(f"Unexpected leakage: {parsed}")
    if parsed.get("00", 0) + parsed.get("11", 0) != SHOTS:
        raise AssertionError(f"Counts do not sum to {SHOTS}: {parsed}")
    if parsed.get("00") != 517 or parsed.get("11") != 507:
        raise AssertionError(
            f"Seed {SEED} counts changed for this Qiskit build: {parsed}"
        )

    observables = [SparsePauliOp(label) for label in ("ZZ", "XX", "YY")]
    evs = (
        StatevectorEstimator()
        .run([(bell_circuit(), observables)])
        .result()[0]
        .data.evs
    )
    if not np.allclose(evs, [1, 1, -1]):
        raise AssertionError(f"Estimator values {evs}")


def check_local_transpilation() -> None:
    measured = bell_circuit()
    measured.measure_all()
    backend = GenericBackendV2(
        num_qubits=5,
        coupling_map=[[0, 1], [1, 2], [2, 3], [3, 4]],
        basis_gates=["rz", "sx", "x", "cx"],
        seed=SEED,
    )
    neighbor = generate_preset_pass_manager(
        optimization_level=1, backend=backend, seed_transpiler=SEED
    ).run(measured)
    routed = generate_preset_pass_manager(
        optimization_level=1,
        backend=backend,
        initial_layout=[0, 2],
        seed_transpiler=SEED,
    ).run(measured)
    neighbor_ops = dict(neighbor.count_ops())
    routed_ops = dict(routed.count_ops())
    if "h" in neighbor_ops:
        raise AssertionError(f"Hadamard survived basis translation: {neighbor_ops}")
    if "rz" not in neighbor_ops and "sx" not in neighbor_ops:
        raise AssertionError(f"Basis translation missing: {neighbor_ops}")
    if routed.depth() <= measured.depth():
        raise AssertionError(
            f"Expected routing to increase depth, logical {measured.depth()} routed {routed.depth()}"
        )
    if routed_ops.get("cx", 0) <= 1:
        raise AssertionError(f"Expected extra CX from routing: {routed_ops}")


def notebook_sources() -> tuple[str, str]:
    if not NOTEBOOK.exists():
        raise AssertionError(f"Missing notebook: {NOTEBOOK}")
    document = json.loads(NOTEBOOK.read_text())
    code_parts = []
    all_parts = []
    for cell in document["cells"]:
        source = "".join(cell["source"])
        all_parts.append(source)
        if cell["cell_type"] == "code":
            ast.parse(source)
            code_parts.append(source)
    return "\n".join(all_parts), "\n".join(code_parts)


def check_notebook_source(source: str, code_source: str) -> None:
    if "RUN_REAL_HARDWARE = False" not in source:
        raise AssertionError("Hardware flag default is missing")
    if "RUN_REAL_HARDWARE = True" in source:
        raise AssertionError("Committed notebook must not set the hardware flag")
    for banned in ("IBMQ", "load_account", ".execute("):
        if banned in code_source:
            raise AssertionError(f"Notebook code contains retired or unsafe call pattern: {banned}")
    if "StatevectorSampler" not in code_source or "StatevectorEstimator" not in code_source:
        raise AssertionError("Notebook is missing the local primitives")
    if "GenericBackendV2" not in code_source:
        raise AssertionError("Notebook is missing the local transpilation backend")


def iter_repo_files():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in {".git", ".venv", "__pycache__", ".ipynb_checkpoints"} for part in path.parts):
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf"}:
            continue
        yield path


def markdown_targets(path: Path, text: str):
    if path.suffix == ".ipynb":
        document = json.loads(text)
        chunks = []
        for cell in document.get("cells", []):
            if cell.get("cell_type") == "markdown":
                chunks.append("".join(cell.get("source", [])))
        text = "\n".join(chunks)
    elif path.suffix != ".md":
        return
    for match in LINK.finditer(text):
        yield match.group(1).strip()


def check_links_and_secrets() -> None:
    link_errors = []
    for path in iter_repo_files():
        text = path.read_text(errors="replace")
        for word in BANNED_PUBLIC_WORDS:
            if word == CHAT_NAME and path.resolve() in CHAT_NAME_ALLOWED:
                continue
            if word in text:
                raise AssertionError(f"{path} contains a banned public word")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                raise AssertionError(f"{path} matches secret pattern {pattern.pattern}")
        if EMAIL.search(text):
            raise AssertionError(f"{path} contains an email address")
        if path.suffix not in {".md", ".ipynb"}:
            continue
        for target in markdown_targets(path, text):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if target.startswith("#"):
                continue
            relative = target.split("#", 1)[0]
            if not relative:
                continue
            resolved = (path.parent / relative).resolve()
            if not resolved.exists():
                link_errors.append(f"{path.relative_to(ROOT)} -> {target}")
    if link_errors:
        raise AssertionError("Broken relative links:\n" + "\n".join(link_errors))


BEGINNER_KEY = {
    "Q01": "B",
    "Q02": "A",
    "Q03": "C",
    "Q04": "B",
    "Q05": "C",
    "Q06": "B",
    "Q07": "C",
    "Q08": "A",
    "Q09": "C",
    "Q10": "A",
    "Q11": "B",
    "Q12": "A",
    "Q13": "B",
    "Q14": "B",
    "Q15": "C",
    "Q16": "B",
    "Q17": "C",
    "Q18": "C",
}


def install_hardware_tripwire():
    """Make a runtime service or sampler constructor fail closed.

    Importing the class does not submit a job. Replacing the constructor
    means a later call in this process cannot open an account.
    """
    try:
        import qiskit_ibm_runtime as runtime_mod
        from qiskit_ibm_runtime.executor_sampler import Sampler as HardwareSampler
    except ImportError:
        return None

    saved = (runtime_mod, HardwareSampler, runtime_mod.QiskitRuntimeService, HardwareSampler.__init__)

    def blocked(*_args, **_kwargs):
        raise AssertionError("A hardware service or sampler constructor was called")

    runtime_mod.QiskitRuntimeService = blocked
    HardwareSampler.__init__ = blocked
    return saved


def restore_hardware_tripwire(saved) -> None:
    if saved is None:
        return
    runtime_mod, hardware_sampler, service, init = saved
    runtime_mod.QiskitRuntimeService = service
    hardware_sampler.__init__ = init


def check_question_behavior(bank_source: str) -> None:
    namespace = {"__name__": "beginner_questions"}
    stdout = io.StringIO()
    with contextlib.redirect_stdout(stdout):
        exec(compile(bank_source, "beginner_questions", "exec"), namespace, namespace)
    bank = namespace["QUESTION_BANK"]
    if list(bank) != [f"Q{number:02d}" for number in range(1, 19)]:
        raise AssertionError(f"Question ids are {list(bank)}")
    for qid, expected in BEGINNER_KEY.items():
        question = bank[qid]
        letters = [letter for letter, _text in question["choices"]]
        if letters != ["A", "B", "C", "D"]:
            raise AssertionError(f"{qid} choices are not A through D")
        if question["answer"] != expected:
            raise AssertionError(f"{qid} key is {question['answer']}, reviewed letter is {expected}")
        if len(question["why_correct"]) != 2:
            raise AssertionError(f"{qid} correct explanation is not two sentences")
        if not 3 <= len(question["why_wrong"]) <= 6:
            raise AssertionError(f"{qid} wrong explanation has {len(question['why_wrong'])} sentences")
        if not question["practice"].endswith("?"):
            raise AssertionError(f"{qid} practice prompt is not a question")
        for letter in "ABCD":
            namespace["learner_answers"].clear()
            result = namespace["review"](qid, letter)
            if letter == expected:
                if result["status"] != "correct" or result["practice"] is not None:
                    raise AssertionError(f"{qid} correct letter was not accepted")
            else:
                if result["status"] != "incorrect":
                    raise AssertionError(f"{qid} letter {letter} was not marked incorrect")
                if result["practice"] != question["practice"]:
                    raise AssertionError(f"{qid} wrong answer did not offer the practice question")
                if not 3 <= len(result["sentences"]) <= 6:
                    raise AssertionError(f"{qid} wrong-answer text was not 3 to 6 sentences")

    namespace["learner_answers"].clear()
    namespace["input"] = lambda _prompt="": "SKIP"
    with contextlib.redirect_stdout(io.StringIO()):
        namespace["ask_one"]("Q01")
    if "Q01" in namespace["learner_answers"]:
        raise AssertionError("SKIP was stored as an answer")

    replies = iter(["A", "q0 is the rightmost bit", "C"])

    def scripted(_prompt=""):
        return next(replies)

    namespace["learner_answers"].clear()
    namespace["input"] = scripted
    with contextlib.redirect_stdout(io.StringIO()):
        namespace["ask_one"]("Q05")
        if namespace["learner_answers"].get("Q05") != "A":
            raise AssertionError("The first Q05 attempt was not stored")
        namespace["ask_one"]("Q05")
    if namespace["learner_answers"].get("Q05") != "C":
        raise AssertionError("Revisiting Q05 did not replace the stored letter")


def check_beginner_science(namespace: dict) -> None:
    phi = namespace["phi_plus"]
    phi_minus = namespace["phi_minus"]
    psi_plus = namespace["psi_plus"]
    phi_report = namespace["amplitude_report"](phi)
    minus_report = namespace["amplitude_report"](phi_minus)
    psi_report = namespace["amplitude_report"](psi_plus)
    if "+0.7071|00>" not in phi_report or "+0.7071|11>" not in phi_report:
        raise AssertionError(f"Phi Plus amplitudes {phi_report}")
    if "+0.7071|00>" not in minus_report or "-0.7071|11>" not in minus_report:
        raise AssertionError(f"Phi Minus amplitudes {minus_report}")
    if "+0.7071|01>" not in psi_report or "+0.7071|10>" not in psi_report:
        raise AssertionError(f"Psi Plus amplitudes {psi_report}")
    if namespace["probability_report"](phi) != namespace["probability_report"](phi_minus):
        raise AssertionError("Phi Plus and Phi Minus Z probabilities diverged")
    if namespace["probability_report"](namespace["order_check"]) != {"01": 1.0}:
        raise AssertionError("X on qubit 0 did not produce 01")
    counts = namespace["local_counts"]
    if counts != {"00": 241, "11": 271}:
        raise AssertionError(f"Beginner seed {SEED} counts changed: {counts}")
    if sum(counts.values()) != BEGINNER_SHOTS:
        raise AssertionError("Beginner sample did not use 512 shots")

    def sample(circuit, basis):
        return namespace["sample_in_basis"](circuit, basis)

    if sample(phi, "Z") != {"00": 241, "11": 271}:
        raise AssertionError("Phi Plus Z sample changed")
    if sample(phi, "X") != {"00": 241, "11": 271}:
        raise AssertionError("Phi Plus X sample changed")
    if sample(phi_minus, "Z") != {"00": 241, "11": 271}:
        raise AssertionError("Phi Minus Z sample changed")
    if sample(phi_minus, "X") != {"01": 241, "10": 271}:
        raise AssertionError("Phi Minus X sample changed")

    estimator = StatevectorEstimator()
    expected = {
        ("phi_plus", "ZZ"): 1,
        ("phi_plus", "XX"): 1,
        ("phi_minus", "ZZ"): 1,
        ("phi_minus", "XX"): -1,
    }
    for (circuit_name, label), value in expected.items():
        circuit = namespace["phi_plus"] if circuit_name == "phi_plus" else namespace["phi_minus"]
        evs = estimator.run([(circuit, SparsePauliOp(label))]).result()[0].data.evs
        got = round(float(np.real(np.asarray(evs).reshape(-1)[0])))
        if got != value:
            raise AssertionError(f"{circuit_name} {label} expectation {got}, expected {value}")

    if namespace["rotation"].num_parameters != 1:
        raise AssertionError("assign_parameters changed the original circuit")
    if namespace["bound"].num_parameters != 0 or namespace["bound"] is namespace["rotation"]:
        raise AssertionError("assign_parameters did not return a new bound circuit")
    if len(namespace["example_result"]) != 1:
        raise AssertionError("Two parameter settings were counted as two PUBs")
    setting_0 = namespace["count_report"](namespace["example_result"][0].data.meas.get_counts(0))
    setting_1 = namespace["count_report"](namespace["example_result"][0].data.meas.get_counts(1))
    if setting_0 != {"0": 64} or setting_1 != {"1": 64}:
        raise AssertionError(f"Parameter PUB counts {setting_0} and {setting_1}")

    isa_ops = dict(namespace["isa_circuit"].count_ops())
    if "h" in isa_ops or "swap" in isa_ops:
        raise AssertionError(f"Neighbor mock ISA was unexpected: {isa_ops}")
    if "rz" not in isa_ops and "sx" not in isa_ops:
        raise AssertionError(f"Mock ISA did not change basis gates: {isa_ops}")
    if namespace["hardware_counts"] is not None or namespace["hardware_job_id"] is not None:
        raise AssertionError("Hardware result appeared while the flags were false")
    if namespace["RUN_REAL_HARDWARE"] is not False or namespace["I_AUTHORIZE_ONE_QPU_JOB"] is not False:
        raise AssertionError("Hardware flags were changed during execution")
    if len(namespace["learner_answers"]) != 18:
        raise AssertionError("The in-order run did not record 18 answers")
    if any(namespace["QUESTION_BANK"][qid]["answer"] != chosen for qid, chosen in namespace["learner_answers"].items()):
        raise AssertionError("The in-order run stored a wrong letter")


def check_beginner_lab() -> None:
    if not BEGINNER.exists():
        raise AssertionError(f"Missing beginner notebook: {BEGINNER}")
    document = json.loads(BEGINNER.read_text())
    nbformat_ok = document.get("nbformat") == 4
    if not nbformat_ok:
        raise AssertionError("Beginner notebook is not nbformat 4")
    text_parts = []
    code_parts = []
    bank_source = None
    question_order = []
    for cell in document["cells"]:
        source = "".join(cell["source"])
        text_parts.append(source)
        if cell["cell_type"] != "code":
            for match in LINK.finditer(source):
                target = match.group(1).strip()
                if target.startswith("#"):
                    continue
                if not target.startswith(("http://", "https://")):
                    raise AssertionError(f"Beginner notebook has a non-public link: {target}")
            continue
        ast.parse(source)
        code_parts.append(source)
        if "QUESTION_BANK = " in source:
            bank_source = source
        question_order.extend(re.findall(r'ask_one\("(Q\d\d)"\)', source))
    if bank_source is None:
        raise AssertionError("Beginner notebook is missing the question bank")
    if question_order != [f"Q{number:02d}" for number in range(1, 19)]:
        raise AssertionError(f"Questions are not asked in order: {question_order}")
    code_source = "\n".join(code_parts)
    full_source = "\n".join(text_parts)
    for required in (
        "RUN_REAL_HARDWARE = False",
        "I_AUTHORIZE_ONE_QPU_JOB = False",
        "typed.strip() != \"RUN\"",
        "from qiskit_ibm_runtime.executor_sampler import Sampler as HardwareSampler",
        "hardware_sampler.run",
        "No hardware counts were invented.",
        "You are my Quantum for the Qulture learning coach.",
        "Wait for my answer.",
        "Jonas von Essen",
    ):
        if required not in full_source and required not in code_source:
            if required not in full_source:
                raise AssertionError(f"Beginner notebook is missing {required}")
    if "RUN_REAL_HARDWARE = True" in code_source or "I_AUTHORIZE_ONE_QPU_JOB = True" in code_source:
        raise AssertionError("Beginner code sets a hardware flag")
    for banned in ("IBMQ", "load_account", ".execute(", "apply_layout"):
        if banned in code_source:
            raise AssertionError(f"Beginner code contains {banned}")
    run_at = code_source.index("hardware_sampler.run")
    if code_source.index("typed.strip() != \"RUN\"") > run_at:
        raise AssertionError("Hardware run is not behind the typed confirmation")
    if code_source.index("if not (RUN_REAL_HARDWARE and I_AUTHORIZE_ONE_QPU_JOB)") > run_at:
        raise AssertionError("Hardware run is not behind the two flags")
    if "{'11': 271, '00': 241}" not in full_source:
        raise AssertionError("Published local counts are missing from the lesson text")
    if "241 of 01 and 271 of 10" not in full_source:
        raise AssertionError("Published Phi Minus X counts are missing from the lesson text")
    coach = "Copy this into " + CHAT_NAME
    if coach not in full_source:
        raise AssertionError("The tutor prompt's copy instruction is missing")

    check_question_behavior(bank_source)

    import matplotlib

    matplotlib.use("Agg", force=True)
    warnings.filterwarnings("ignore", message="FigureCanvasAgg is non-interactive")
    namespace = {"__name__": "beginner_notebook"}
    replies = iter(BEGINNER_KEY[qid] for qid in question_order)

    def scripted(_prompt=""):
        try:
            return next(replies)
        except StopIteration as exc:
            raise AssertionError("The notebook asked for input after the 18 answers") from exc

    namespace["input"] = scripted
    saved = install_hardware_tripwire()
    stdout = io.StringIO()
    try:
        with contextlib.redirect_stdout(stdout):
            for index, cell in enumerate(document["cells"]):
                if cell["cell_type"] != "code":
                    continue
                source = "".join(cell["source"])
                exec(compile(source, f"beginner_cell_{index}", "exec"), namespace, namespace)
    finally:
        restore_hardware_tripwire(saved)
    output = stdout.getvalue()
    if output.count("Correct.") != 18 or "Not quite" in output:
        raise AssertionError("The in-order run did not accept the 18 reviewed letters")
    for phrase in (
        "Hardware skipped. No IBM account was opened. No job was submitted.",
        "MOCK backend, not hardware.",
        "REAL hardware: not run.",
        "Local packages are already importable. Skipping installation.",
    ):
        if phrase not in output:
            raise AssertionError(f"Beginner run did not print {phrase}")
    if "No hardware counts were invented." in output:
        raise AssertionError("The hardware exception path ran during the local test")
    check_beginner_science(namespace)


def main() -> int:
    check_bell_vector()
    check_cnot_and_entanglement()
    check_sampler_and_estimator()
    check_local_transpilation()
    source, code_source = notebook_sources()
    check_notebook_source(source, code_source)
    check_beginner_lab()
    check_links_and_secrets()
    print("Lab 001 offline smoke test passed.")
    print(f"Bell sample seed {SEED}: 00 -> 517, 11 -> 507, agreement 1.0, shots {SHOTS}.")
    print(
        f"Beginner sample seed {SEED}: 00 -> 241, 11 -> 271, shots {BEGINNER_SHOTS}. "
        "Phi Minus in X: 01 -> 241, 10 -> 271. Eighteen questions checked."
    )
    print("No IBM credentials were used. No hardware job was submitted.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except AssertionError as exc:
        print(f"SMOKE TEST FAILED: {exc}", file=sys.stderr)
        sys.exit(1)
