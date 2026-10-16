"""
My Computational Physics Library (a_man_lib)
This is my primary physics and numerical methods library. I have modularized it into
specialized submodules:
- lin_alg: Matrix and vector operations, direct and iterative linear system solvers
- ode: Ordinary differential equation solvers (Runge-Kutta 4th order)
- root_finding: Root finding methods and polynomial root solvers
- integration: Numerical integration and quadrature routines
- math_utils: LCG random generators, progressions, complex numbers, file parsers

For backwards compatibility with existing assignment and problem scripts, all routines
are re-exported directly below.
"""

# 1. Linear Algebra Routines
from lin_alg import (
    mat_mul,
    mat_T,
    dot_product,
    mat_vec,
    aug_mat,
    gauss_jordan,
    LU_Decomp,
    chsk,
    forward_substitution,
    forward_substitution_chsk,
    back_substitution,
    jacobi,
    gauss_sdl,
    SOR,
)

# 2. ODE Solvers
from ode import (
    RK4,
    RK4_Modified,
)

# 3. Root Finding & Polynomial Routines
from root_finding import (
    brkt,
    root_bis,
    root_Reg_f,
    Nwt_Raph,
    Fixed_Point,
    deflation,
    Lag_Pol,
)

# 4. Numerical Integration
from integration import (
    Mid_Pnt,
    Trpz,
    sim_s,
    ab_rand,
    Monte_Carlo_int,
    Gauss_Quad,
)

# 5. Math Utilities & File Parsing
from math_utils import (
    lcg_generator,
    seed,
    lcg_step,
    fact,
    GP,
    HP,
    MyComplex,
    vector_op,
    parse_matrix_file,
    parse_vector_file,
)

__all__ = [
    # Linear Algebra
    "mat_mul",
    "mat_T",
    "dot_product",
    "mat_vec",
    "aug_mat",
    "gauss_jordan",
    "LU_Decomp",
    "chsk",
    "forward_substitution",
    "forward_substitution_chsk",
    "back_substitution",
    "jacobi",
    "gauss_sdl",
    "SOR",
    # ODEs
    "RK4",
    "RK4_Modified",
    # Root Finding
    "brkt",
    "root_bis",
    "root_Reg_f",
    "Nwt_Raph",
    "Fixed_Point",
    "deflation",
    "Lag_Pol",
    # Integration
    "Mid_Pnt",
    "Trpz",
    "sim_s",
    "ab_rand",
    "Monte_Carlo_int",
    "Gauss_Quad",
    # Math Utilities
    "lcg_generator",
    "seed",
    "lcg_step",
    "fact",
    "GP",
    "HP",
    "MyComplex",
    "vector_op",
    "parse_matrix_file",
    "parse_vector_file",
]
