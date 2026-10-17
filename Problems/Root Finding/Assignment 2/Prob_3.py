from a_man_lib import Fixed_Point
import math

# Solving for Problem 3
def P3_func(x):
    return x**2 - 2*x - 3

# defining g_x for P3_x

def gx_p3_x(x):
    return math.sqrt(3+2*x)

# Parsing to function to find root
print("\n")
root = Fixed_Point(gx_p3_x, 1.5)
print(f"root obtained throug Fixed Point method is {root}")
print(f"value of function at that root {P3_func(root)}")

##### end of the problem #####
##### Terminal output #####
"""
total no. of iteration is 14
root obtained throug Fixed Point method is 2.9999996376780813
value of function at that root -1.4492875441973752e-06
"""
