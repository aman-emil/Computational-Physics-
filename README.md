# Computational Physics Toolkit (`a_man_lib`)

A modular, standalone Python numerical methods and computational physics library built from scratch with standard Python (`math` & `copy`), without external dependencies like NumPy or SciPy.

---

## 📁 Repository Structure

Each module is organized into its own folder according to its python filename:

```text
.
├── .gitignore
├── README.md
├── a_man_lib/
│   ├── __init__.py
│   └── a_man_lib.py        # Central re-export entrypoint for all routines
├── integration/
│   ├── __init__.py
│   └── integration.py      # Numerical quadrature & Monte Carlo integration
├── lin_alg/
│   ├── __init__.py
│   └── lin_alg.py          # Matrix & vector linear algebra routines & solvers
├── math_utils/
│   ├── __init__.py
│   └── math_utils.py       # Helper routines, LCG generators, complex numbers & file I/O
├── ode/
│   ├── __init__.py
│   └── ode.py              # Ordinary Differential Equation solvers (RK4, RK4_Modified)
└── root_finding/
    ├── __init__.py
    └── root_finding.py     # Root-finding algorithms and polynomial solvers
```

---

## 🚀 Module Overview & Key Functions

### 1. `lin_alg/` — Linear Algebra
Provides linear system solvers, matrix decompositions, and vector operations.
- **Matrix Operations**: `mat_mul`, `mat_T` (transpose), `dot_product`, `mat_vec`, `aug_mat`.
- **Direct Solvers**:
  - `gauss_jordan`: Gauss-Jordan elimination with partial pivoting for linear equations and matrix inversion.
  - `LU_Decomp`: Doolittle LU factorization with partial pivoting.
  - `chsk`: Cholesky decomposition for symmetric positive-definite matrices.
  - `forward_substitution`, `forward_substitution_chsk`, `back_substitution`.
- **Iterative Solvers**:
  - `jacobi`: Jacobi relaxation method.
  - `gauss_sdl`: Gauss-Seidel iterative method.
  - `SOR`: Successive Over-Relaxation solver with relaxation parameter $\omega$.

### 2. `integration/` — Numerical Integration & Quadrature
Routines for definite integrals across 1D domains.
- **Newton-Cotes Quadratures**:
  - `Mid_Pnt`: Midpoint rule for $N$ intervals.
  - `Trpz`: Trapezoidal rule for $N$ intervals.
  - `sim_s`: Simpson's $1/3$ composite rule.
- **Monte Carlo Integration**:
  - `Monte_Carlo_int`: Stochastic integration using an LCG generator, returning both the estimate and variance ($\sigma^2$).
  - `ab_rand`: Scaled random interval sampling utility.
- **Gaussian Quadrature**:
  - `Gauss_Quad`: Gauss-Legendre quadrature (default $N=4$) and Gauss-Laguerre quadrature (default $N=4$) for semi-infinite $[0, \infty)$ integrals.

### 3. `ode/` — Ordinary Differential Equations
Solvers for initial value problems (IVP) of coupled first-order ODE systems.
- `RK4(slope_list, interval, y0_vec, dx=0.01)`: Classical 4th-order Runge-Kutta solver where derivatives accept unpacked arguments `f(*y, x)`.
- `RK4_Modified(slope_list, interval, y0_vec, dx=0.01)`: Generalized RK4 solver where derivatives accept the state vector `f(y_vec, x)`.

### 4. `root_finding/` — Root-Finding & Polynomial Solvers
Methods to find zeros of single-variable nonlinear functions and polynomials.
- `brkt`: Automatic bracket finder for functions where $\text{sign}(f(a)) \neq \text{sign}(f(b))$.
- `root_bis`: Bisection method.
- `root_Reg_f`: Regula Falsi (false position) method.
- `Nwt_Raph`: Newton-Raphson method with derivative checking.
- `Fixed_Point`: Fixed-point iteration ($x = g(x)$).
- `Lag_Pol`: Laguerre's polynomial root-finding method.
- `deflation`: Synthetic polynomial deflation by synthetic division.

### 5. `math_utils/` — Mathematical Utilities & Helpers
General-purpose numerical tools and file parsers.
- **Random Number Generation**: `lcg_generator`, `seed`, `lcg_step` (Linear Congruential Generator).
- **Series & Special Functions**: `fact` (iterative factorial), `GP` (Geometric Progression sum), `HP` (Harmonic Progression sum).
- **Complex Numbers**: `MyComplex` class supporting addition, subtraction, multiplication, and modulus.
- **Vector Math & File Parsing**:
  - `vector_op`: Element-wise arithmetic (`+`, `-`, `*`).
  - `parse_matrix_file`, `parse_vector_file`: Robust loaders for text-based matrix and vector files.

### 6. `a_man_lib/` — Central Import Hub
Re-exports all functionality from every subfolder so existing scripts can continue using:
```python
from a_man_lib import mat_mul, RK4, Gauss_Quad
# or
import a_man_lib as aml
```

---

## 💻 Quick Usage Examples

### Using Individual Modules
```python
from lin_alg import mat_mul, LU_Decomp
from integration import sim_s
from ode import RK4

# Example: Simpson's 1/3 Integration of f(x) = x^2 from 0 to 1
val = sim_s(lambda x: x**2, [0, 1], N=100)
print("Integral:", val)
```

### Using the Unified Library
```python
import a_man_lib as aml

# Example: Root finding with Newton-Raphson
f = lambda x: x**2 - 2
df = lambda x: 2 * x
root = aml.Nwt_Raph(f, df, 1.0)
print("Square root of 2:", root)
```

---

## 🛠️ Git Instructions for Uploading

To initialize and upload this repository to your GitHub/Git remote:

1. **Initialize Git repository**:
   ```bash
   git init -b main
   ```

2. **Stage and commit all files**:
   ```bash
   git add .
   git commit -m "feat: organize computational physics library into modular packages"
   ```

3. **Link to your remote GitHub repository**:
   ```bash
   git remote add origin https://github.com/<your-username>/<your-repo-name>.git
   ```

4. **Push to GitHub**:
   ```bash
   git push -u origin main
   ```
