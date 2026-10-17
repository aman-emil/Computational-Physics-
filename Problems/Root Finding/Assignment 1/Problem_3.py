import math
from a_man_lib import brkt, root_bis, root_Reg_f

# braket function is defined in library

# defining the function in problem 3
def P3_func(x):
    f_val = -x - math.cos(x)
    return f_val

# old brakets
a = 2
b = 4

# finding the new brackets
a_new, b_new = brkt(P3_func, a, b)

# finding roots

# root finding using bisection method
root1, f_root1 = root_bis(P3_func, a_new, b_new)
print(f"value of root using bisection is {root1} with f(root) value is {f_root1}")

# root finding using Regula Falsi method
root2, f_root2 = root_Reg_f(P3_func, a_new, b_new)
print(f"value of root using Regula Falsi is {root2} with f(root) value is {f_root2}")


# end of the problem #
# out of the problem is in text file attached#
# terminal output #
"""
iteration count to find braket 5
total no. of iteration are 22
value of root using bisection is -0.7390849560546873 with f(root) value is -2.964978876862645e-07
total no. of iteration are 6
value of root using Regula Falsi is -0.7390850545962979 with f(root) value is -1.315774721399876e-07

"""
