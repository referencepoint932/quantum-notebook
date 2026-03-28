# Copilot Instructions — quantum-notebook

## Project overview

Educational Jupyter notebook series teaching quantum computing concepts through progressive lessons. 
Each notebook builds on the previous one, progressing from basic superposition through interference-based algorithms. 
`quantum_alpha.py` is a standalone CLI script that mirrors the H-gate notebook demo.
More standalone scripts are welcome if they fit the same pattern of demonstrating a single concept with a 
simple circuit and visualization.

## Tech stack

- **Qiskit 2.x** — circuit construction, simulation, visualization
- **Qiskit BasicSimulator** — all simulations run locally (no Azure Quantum workspace connections)
- **NumPy** — linear algebra for state manipulation
- **Matplotlib** — all plotting (no Qiskit `plot_histogram`; charts are hand-built with `plt.subplots`)

## Environment setup

```sh
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Running

```sh
# Run the standalone demo script
python quantum_alpha.py               # defaults: 2000 shots, seed=7, saves PNG
python quantum_alpha.py --plot none   # skip plot output

# Notebooks — open in JupyterLab or VS Code
jupyter lab
```

## Notebook conventions

- **Numbering**: `1XX_quantum_<topic>.ipynb` — the prefix determines lesson order (100 → 104).
- **Structure per notebook**: title (🔬 emoji + concept name) → "Setup & imports" section → concept explanation with LaTeX math → code demos → validation assertions → takeaways table.
- **Imports**: each notebook is self-contained. Imports are repeated in every notebook's setup cell rather than shared.
- **Simulation pattern**: build circuit → get exact `Statevector` probabilities → add measurement gate → `transpile` + `backend.run(shots=N)` → compare exact vs empirical.
- **Visualization**: Bloch spheres via `plot_bloch_multivector`, bar charts via raw matplotlib. Plots use `figsize`, `grid(axis="y", alpha=0.25)`, and `edgecolor="black"`.
- **Validation**: notebooks end with `assert` statements comparing exact probabilities (within `1e-9`) and empirical results (within tolerance like `0.08`).
- **Seeds**: `random.randint(0, 2**32 - 1)` for notebook randomness; the CLI script uses a fixed default seed (`--seed 7`).

## Notebook progression

1. **100** — Superposition: Hadamard gate, Bloch sphere visualization
2. **101** — H-gate deep dive: statevector inspection, measurement histograms, H²=I identity
3. **102** — Unitary transformations: unitarity verification, norm preservation, Bloch rotations, oracle model, universality
4. **103** — Deutsch algorithm (work in progress — has `todo` placeholder cells)
5. **104** — Interference: phase kickback, Bernstein-Vazirani, Grover's search, QPE, Simon's algorithm, EPR pairs, Gottesman-Knill boundary

## Code style (quantum_alpha.py)

- Type hints with `from __future__ import annotations`
- `@dataclass` for structured results
- Functions return data; printing and plotting are separate concerns
- `argparse` for CLI interface
