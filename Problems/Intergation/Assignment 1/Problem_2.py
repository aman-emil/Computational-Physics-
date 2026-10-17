from a_man_lib import Mid_Pnt, Trpz
import math 

Itr_arr = [4, 8, 15, 20]

# Problem 1 
interval_a = [1, 2]
def P2a_func(x): 
    return 1 / x

# Problem 2 
interval_b = [0, math.pi / 2]
def P2b_func(x):
    return x * math.cos(x)

# Problem 3 
interval_c = [0, 1]
def P3c_func(x): 
    return x * math.atan(x)

problems = [
    ("Problem 1", P2a_func, interval_a),
    ("Problem 2", P2b_func, interval_b),
    ("Problem 3", P3c_func, interval_c)
]

print(f"{'Problem':<12} {'N':<6} {'Midpoint':<14} {'Trapezoidal':<14}")
print("-" * 46)

for name, func, interval in problems:
    for N in Itr_arr:
        mid_val = Mid_Pnt(func, interval, N)
        trpz_val = Trpz(func, interval, N)
        print(f"{name:<12} {N:<6} {mid_val:<14.6f} {trpz_val:<14.6f}")

###### End of The Problem #######
###### Terminal Output  ######

# Roll No 2411124
# Aman Kumar Singh

"""
Problem      N      Midpoint       Trapezoidal
----------------------------------------------
Problem 1    4      0.691220       0.697024
Problem 1    8      0.692661       0.694122
Problem 1    15     0.693008       0.693425
Problem 1    20     0.693069       0.693303
Problem 2    4      0.587448       0.537607
Problem 2    8      0.574934       0.562528
Problem 2    15     0.571972       0.568446
Problem 2    20     0.571457       0.569475
Problem 3    4      0.282046       0.292098
Problem 3    8      0.284561       0.287072
Problem 3    15     0.285160       0.285874
Problem 3    20     0.285264       0.285666
"""
