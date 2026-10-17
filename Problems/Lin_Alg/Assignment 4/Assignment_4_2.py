import math
from a_man_lib import gauss_sdl, jacobi, parse_matrix_file, parse_vector_file



matrix = parse_matrix_file("Matrix.txt")

vector = parse_vector_file("vector.txt")

guess = []
for val in range(len(vector)):
    guess.append(0)

# Jacobi method

# Gauss-Seidel method
sol_g = gauss_sdl(matrix, vector, guess)
print(f"solution vector using Gauss-Seidel is {sol_g}")

# Jacobi Method
sol_j = jacobi(matrix, vector, guess)
print(f"solution vector using jacobi is {sol_j}")

### end of the problem ####
### Terminal Output ####
"""Converged in 9 iterations.
solution vector using Gauss-Seidel is [0.9997098859166726, 0.9997523718921002, 0.9998943180762581, 0.9998249005584512, 0.9998505432158709, 0.9999362153230322]
solution vector using jacobi is [0.9999999999997295, 0.9999999999996175, 0.9999999999997295, 0.9999999999997295, 0.9999999999996175, 0.9999999999997295]"""
