import math
from a_man_lib import SOR

matrix = [
    [2, -1, 0, 0, 0, 0, 0, 0, 0, 0],
    [-1, 2, -1, 0, 0, 0, 0, 0, 0, 0],
    [0, -1, 2, -1, 0, 0, 0, 0, 0, 0],
    [0, 0, -1, 2, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, -1, 2, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, 2, -1, 0, 0, 0],
    [0, 0, 0, 0, 0, -1, 2, -1, 0, 0],
    [0, 0, 0, 0, 0, 0, -1, 2, -1, 0],
    [0, 0, 0, 0, 0, 0, 0, -1, 2, -1],
    [0, 0, 0, 0, 0, 0, 0, 0, -1, 2]
]

vector = [1.0] * len(matrix)

guess = []
for val in range(len(vector)):
    guess.append(0)

# Jacobi Method
sol_or = SOR(matrix, vector, guess, 1.57)
print(f"solution vector using sor is {sol_or}")

##### End of the problem ######
##### Terminal Output #####
"""Converged in 34 iterations.
solution vector using sor is [5.000000392470314, 9.000000596993203, 12.000000648722352, 14.00000058706583, 15.00000046260419, 15.000000330590336, 14.000000229423769, 12.000000157219056, 9.000000080166739, 5.000000031813165]"""
