import math
from a_man_lib import chsk, parse_matrix_file, parse_vector_file, forward_substitution_chsk, back_substitution, mat_T

# Name : Aman Kumar Singh
# Roll_No : 2411124

matrix = parse_matrix_file('mat_p3.txt')
vector = parse_vector_file('vec_p3.txt')

chsk_mat = chsk(matrix)
chsk_mat_T = mat_T(chsk_mat)

print("Cholesky Decomposition Matrix")
for row in chsk_mat:
    print(row)


y = forward_substitution_chsk(chsk_mat, vector)
x = back_substitution(chsk_mat_T, y)

print("\n resulting solution for vector x is")

for idx, val in enumerate(x):
    print(f"value of x_{idx} is {val:.4f}")

# End of the problem
# output

"""Cholesky Decomposition Matrix
[2.0, 0, 0, 0]
[0.5, 1.6583123951777, 0, 0]
[0.5, -0.753778361444409, 1.087114613009218, 0]
[0.5, 0.45226701686664544, 0.08362420100070905, 1.2403473458920844]

 resulting solution for vector x is
value of x_0 is 0.0000
value of x_1 is 1.0000
value of x_2 is 1.0000
value of x_3 is 1.0000"""
