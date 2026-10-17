from a_man_lib import parse_matrix_file, parse_vector_file, aug_mat, gauss_jordan, LU_Decomp, forward_substitution, back_substitution


# problem 1 part(a)
matrix = parse_matrix_file("matrix_f.txt")
vector = parse_vector_file("vec_f.txt")
matrix_a = aug_mat(matrix,vector)

# using gauss jordan method
results = gauss_jordan(matrix_a)

print("\nResult from Gauss Jordan Method")
for idx, val in enumerate(results):
    print(f"value of a_{idx+1} is {val}")


# problem 2 part(b)
LU_Decomp_mat = LU_Decomp(matrix)
y = forward_substitution(LU_Decomp_mat,vector)
x = back_substitution(LU_Decomp_mat,y)

print("\nResult from LU Decomposition Method")
for idx, x in enumerate(results):
    print(f"value of a_{idx+1} is {x}")

###############################################################
##### End of the problem ##############

######################################
# results
"""
Result from Gauss Jordan Method
value of a_1 is -1.7618170439978602
value of a_2 is 0.8962280338740121
value of a_3 is 4.051931404116157
value of a_4 is -1.6171308025395414
value of a_5 is 2.041913538501913
value of a_6 is 0.15183248715593553

Result from LU Decomposition Method
value of a_1 is -1.7618170439978602
value of a_2 is 0.8962280338740121
value of a_3 is 4.051931404116157
value of a_4 is -1.6171308025395414
value of a_5 is 2.041913538501913
value of a_6 is 0.15183248715593553

"""
