# 🔬 Collection of Quantum Algorithms through the decades

A progressive Jupyter notebook collection that demonstrates quantum computing concepts 
through hands-on lessons. 

We start with basic superposition and interference-based algorithms, outline
quantum optimizations and move towards topological quantum computing and quantum simulation.

All circuits run **locally** using [Qiskit 2.x](https://qiskit.org/) and `BasicSimulator`. 
No cloud accounts or hardware access required.

---

## 📚 Contents

### Quantum Fundamentals (100-series)

| # | Notebook | Topic |
|---|----------|-------|
| 100 | [`100_quantum_superposition.ipynb`](algorithms/100_quantum_superposition.ipynb) | Superposition — Hadamard gate, Bloch sphere visualization |
| 101 | [`101_quantum_H.ipynb`](algorithms/101_quantum_H.ipynb) | H-gate deep dive — statevector inspection, measurement histograms, H² = I identity |
| 102 | [`102_quantum_unitary.ipynb`](algorithms/102_quantum_unitary.ipynb) | Unitary transformations — unitarity verification, norm preservation, Bloch rotations, oracle model |
| 103 | [`103_quantum_deutsch.ipynb`](algorithms/103_quantum_deutsch.ipynb) | Deutsch & Deutsch–Jozsa — phase kickback, interference, exponential quantum advantage, universal blueprint |
| 104 | [`104_quantum_interference.ipynb`](algorithms/104_quantum_interference.ipynb) | Interference — phase kickback, Bernstein–Vazirani, Grover's search, QPE, Simon's algorithm, EPR pairs |

### Quantum Optimization (200-series)

| # | Notebook | Topic |
|---|----------|-------|
| 200 | [`200_quantum_hamiltonian.ipynb`](algorithms/200_quantum_hamiltonian.ipynb) | Hamiltonians & Ising model — energy operators, Pauli algebra, Ising spin systems, variational principle |
| 201 | [`201_quantum_qaoa.ipynb`](algorithms/201_quantum_qaoa.ipynb) | QAOA — MaxCut, cost/mixer Hamiltonians, QAOA ansatz, hybrid optimization, depth scaling |
| 202 | [`202_quantum_qubo.ipynb`](algorithms/202_quantum_qubo.ipynb) | QUBO — quadratic binary optimization, QUBO↔Ising equivalence, penalty methods, QAOA integration |

### Topological Quantum Computing (300-series)

| # | Notebook | Topic |
|---|----------|-------|
| 300 | [`300_quantum_majorana.ipynb`](algorithms/300_quantum_majorana.ipynb) | Majorana qubits — Kitaev chain, topological phases, zero modes, non-Abelian braiding, winding number |

### Quantum Simulation & Chemistry (400-series)

| # | Notebook | Topic |
|---|----------|-------|
| 400 | [`400_quantum_simulation.ipynb`](algorithms/400_quantum_simulation.ipynb) | Quantum simulation — Hamiltonian dynamics, Trotter decomposition, fidelity analysis |
| 401 | [`401_quantum_vqe.ipynb`](algorithms/401_quantum_vqe.ipynb) | VQE — variational quantum eigensolver, ansatz design, optimizer comparison |
| 402 | [`402_quantum_chemistry.ipynb`](algorithms/402_quantum_chemistry.ipynb) | Quantum chemistry — molecular Hamiltonians, H₂ & LiH dissociation, active space methods |
| 403 | [`403_quantum_biology.ipynb`](algorithms/403_quantum_biology.ipynb) | Quantum biology — protein folding, radical pairs, FMO dynamics, DNA search |

---

## 🛠️ Tech Stack

- **[Qiskit 2.x](https://qiskit.org/)** — circuit construction, simulation, visualization
- **Qiskit BasicSimulator** — all simulations run locally (no cloud workspace needed)
- **[NumPy](https://numpy.org/)** — linear algebra for state manipulation
- **[Matplotlib](https://matplotlib.org/)** — hand-built charts and visualizations (no `plot_histogram`)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+

### Setup

```bash
# Clone the repository
git clone https://github.com/<your-username>/quantum-notebook.git
cd quantum-notebook

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt
```

### Run the Notebooks

```bash
jupyter lab
```

Open any notebook in `algorithms/` and run cells top-to-bottom. Each notebook is self-contained — no shared imports or state between files.

### Run the CLI Demo

`quantum_alpha.py` is a standalone script that mirrors the H-gate notebook demo:

```bash
python quantum_alpha.py                    # 2 000 shots, seed=7, saves PNG
python quantum_alpha.py --shots 5000       # custom shot count
python quantum_alpha.py --plot none        # skip plot output
```

---

## 📓 Notebook Structure

Every notebook follows a consistent pattern:

1. **🔬 Title** — concept name with emoji header
2. **Setup & imports** — self-contained; all imports repeated per notebook
3. **Concept explanation** — LaTeX math and prose
4. **Code demos** — build circuit → exact `Statevector` probabilities → measure → `transpile` + `backend.run(shots=N)` → compare exact vs. empirical
5. **Visualization** — Bloch spheres (`plot_bloch_multivector`) and hand-built bar charts (`plt.subplots`)
6. **Validation** — `assert` statements verify exact probabilities (within `1e-9`) and empirical results (within tolerance)
7. **Takeaways** — summary table of key concepts

---

## 🗂️ Project Structure

```
quantum-notebook/
├── algorithms/
│   ├── 100_quantum_superposition.ipynb
│   ├── 101_quantum_H.ipynb
│   ├── 102_quantum_unitary.ipynb
│   ├── 103_quantum_deutsch.ipynb
│   ├── 104_quantum_interference.ipynb
│   ├── 200_quantum_hamiltonian.ipynb
│   ├── 201_quantum_qaoa.ipynb
│   ├── 202_quantum_qubo.ipynb
│   ├── 300_quantum_majorana.ipynb
│   ├── 400_quantum_simulation.ipynb
│   ├── 401_quantum_vqe.ipynb
│   ├── 402_quantum_chemistry.ipynb
│   ├── 403_quantum_biology.ipynb
│   └── *.png                          # generated visualizations
├── quantum_alpha.py                    # standalone CLI demo script
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🤝 Contributing

Contributions are welcome! Ideas for new notebooks or standalone scripts that demonstrate a single quantum concept with a simple circuit and visualization are especially encouraged.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-concept`)
3. Follow the existing notebook conventions (numbering, structure, validation)
4. Submit a pull request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

Created by Dr. Boris Milanovic, 2026.