"""Pure Python version of the educational H-gate notebook demo.

This script demonstrates:
1) H|0> -> (|0> + |1>) / sqrt(2) with ~50/50 measurements
2) H(H|0>) -> |0> (because H^2 = I)
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicSimulator
from qiskit.quantum_info import Statevector


@dataclass
class DemoResult:
    counts: dict[str, int]
    p0_exact: float
    p1_exact: float
    p0_empirical: float
    p1_empirical: float


def run_single_h_demo(backend: BasicSimulator, shots: int, seed: int) -> DemoResult:
    """Run H|0> superposition demo and return exact + sampled probabilities."""
    qc = QuantumCircuit(1)
    qc.h(0)
    p0_exact, p1_exact = Statevector.from_instruction(qc).probabilities()

    qc_measure = QuantumCircuit(1, 1)
    qc_measure.h(0)
    qc_measure.measure(0, 0)
    compiled = transpile(qc_measure, backend, seed_transpiler=seed)
    result = backend.run(compiled, shots=shots, seed_simulator=seed).result()
    counts = result.get_counts()

    count_0 = counts.get("0", 0)
    count_1 = counts.get("1", 0)
    p0_empirical = count_0 / shots
    p1_empirical = count_1 / shots

    return DemoResult(counts, p0_exact, p1_exact, p0_empirical, p1_empirical)


def run_double_h_demo(backend: BasicSimulator, shots: int, seed: int) -> DemoResult:
    """Run H(H|0>) identity demo and return exact + sampled probabilities."""
    qc = QuantumCircuit(1)
    qc.h(0)
    qc.h(0)
    p0_exact, p1_exact = Statevector.from_instruction(qc).probabilities()

    qc_measure = QuantumCircuit(1, 1)
    qc_measure.h(0)
    qc_measure.h(0)
    qc_measure.measure(0, 0)
    compiled = transpile(qc_measure, backend, seed_transpiler=seed)
    result = backend.run(compiled, shots=shots, seed_simulator=seed).result()
    counts = result.get_counts()

    count_0 = counts.get("0", 0)
    count_1 = counts.get("1", 0)
    p0_empirical = count_0 / shots
    p1_empirical = count_1 / shots

    return DemoResult(counts, p0_exact, p1_exact, p0_empirical, p1_empirical)


def validate_results(single_h: DemoResult, double_h: DemoResult) -> None:
    """Lightweight educational checks mirroring the notebook assertions."""
    assert abs(single_h.p0_exact - 0.5) < 1e-9 and abs(single_h.p1_exact - 0.5) < 1e-9
    assert abs(single_h.p0_empirical - 0.5) < 0.08 and abs(single_h.p1_empirical - 0.5) < 0.08

    assert abs(double_h.p0_exact - 1.0) < 1e-9 and abs(double_h.p1_exact) < 1e-9
    assert double_h.p0_empirical > 0.95


def print_summary(single_h: DemoResult, double_h: DemoResult) -> None:
    print("=== Demo 1: H|0> creates superposition ===")
    print(f"Exact probabilities: P(0)={single_h.p0_exact:.3f}, P(1)={single_h.p1_exact:.3f}")
    print(f"Measured counts: {single_h.counts}")
    print(
        f"Empirical probabilities: P(0)={single_h.p0_empirical:.3f}, "
        f"P(1)={single_h.p1_empirical:.3f}"
    )
    print()

    print("=== Demo 2: H(H|0>) returns to |0> ===")
    print(f"Exact probabilities: P(0)={double_h.p0_exact:.3f}, P(1)={double_h.p1_exact:.3f}")
    print(f"Measured counts: {double_h.counts}")
    print(
        f"Empirical probabilities: P(0)={double_h.p0_empirical:.3f}, "
        f"P(1)={double_h.p1_empirical:.3f}"
    )


def maybe_plot(single_h: DemoResult, double_h: DemoResult, output_path: str | None) -> None:
    if output_path is None:
        return

    fig, axes = plt.subplots(1, 2, figsize=(10, 3))

    axes[0].bar(["0", "1"], [single_h.counts.get("0", 0), single_h.counts.get("1", 0)])
    axes[0].set_title("H|0> measurement counts")
    axes[0].set_xlabel("Measured bit")
    axes[0].set_ylabel("Counts")
    axes[0].grid(axis="y", alpha=0.25)

    axes[1].bar(["0", "1"], [double_h.counts.get("0", 0), double_h.counts.get("1", 0)])
    axes[1].set_title("H(H|0>) measurement counts")
    axes[1].set_xlabel("Measured bit")
    axes[1].set_ylabel("Counts")
    axes[1].grid(axis="y", alpha=0.25)

    plt.tight_layout()
    fig.savefig(output_path, dpi=120)
    print(f"Saved plot: {output_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Educational Qiskit demo: superposition with H and identity via H twice."
    )
    parser.add_argument("--shots", type=int, default=2000, help="Number of measurement shots")
    parser.add_argument("--seed", type=int, default=7, help="Seed for transpiler/simulator")
    parser.add_argument(
        "--plot",
        default="quantum_alpha_counts.png",
        help="Output PNG path for count plots; use --plot none to disable",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    plot_path = None if str(args.plot).lower() == "none" else args.plot

    backend = BasicSimulator()
    single_h = run_single_h_demo(backend=backend, shots=args.shots, seed=args.seed)
    double_h = run_double_h_demo(backend=backend, shots=args.shots, seed=args.seed)

    validate_results(single_h, double_h)
    print_summary(single_h, double_h)
    print("\nValidation passed.")

    maybe_plot(single_h, double_h, output_path=plot_path)


if __name__ == "__main__":
    main()

