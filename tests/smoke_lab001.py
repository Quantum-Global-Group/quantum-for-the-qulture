"""Offline checks for Lab 001.

Run from the repository root after installing requirements.txt.
No IBM credentials are read. No hardware job is submitted.
"""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path

import numpy as np
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator, StatevectorSampler
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit.quantum_info import SparsePauliOp, Statevector, partial_trace
from qiskit.transpiler import generate_preset_pass_manager

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "labs" / "01_entanglement" / "entanglement_hands_to_hardware.ipynb"
SEED = 7
SHOTS = 1024

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


def main() -> int:
    check_bell_vector()
    check_cnot_and_entanglement()
    check_sampler_and_estimator()
    check_local_transpilation()
    source, code_source = notebook_sources()
    check_notebook_source(source, code_source)
    check_links_and_secrets()
    print("Lab 001 offline smoke test passed.")
    print(f"Bell sample seed {SEED}: 00 -> 517, 11 -> 507, agreement 1.0, shots {SHOTS}.")
    print("No IBM credentials were used. No hardware job was submitted.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except AssertionError as exc:
        print(f"SMOKE TEST FAILED: {exc}", file=sys.stderr)
        sys.exit(1)
