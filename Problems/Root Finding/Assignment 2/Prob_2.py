from a_man_lib import Nwt_Raph, root_Reg_f, brkt, root_bis
import math


# defining problem 2
def P2_Func(x):
    return 3*x + math.sin(x) - math.e**(x)

# differential form of Problem 2 function :
def dP2_Func(x):
    return 3 + math.cos(x) - math.e**(x)

# defining bracket
a = 1.5
b = 2

# Solving Using Bisection Method
print("\n")
root_1,f_root1 = root_bis(P2_Func, a, b)
print(f"root obtained throug bisection method is {root_1}")
print(f"function value at that root is {f_root1}")
print("\n")

# Solving using root_Reg_f
root_2, f_root2 = root_Reg_f(P2_Func, a, b)
print(f"root obtained throug Regular Falsi method is {root_2}")
print(f"function value at that root is {f_root2}")
print("\n")

# Solving using Newton Raphson is
root_3 = Nwt_Raph(P2_Func,dP2_Func, 2)
print(f"root obtained throug Newton Raphson method is {root_3}")
print(f"function value at that root is {P2_Func(root_2)}")
print("\n")

# Comparing
print("convergence rate are of order")
print("Newton Raphson > Regular Falsi > Bisection Method")


##### end of the problem #####
##### Terminal output #####
"""
total no. of iteration are 15
root obtained throug bisection method is 1.8900299072265625
function value at that root is -7.000460797712549e-07


total no. of iteration are 7
root obtained throug Regular Falsi method is 1.8900296818840359
function value at that root is 1.863172869320806e-07


total no. of iteration is 4
root obtained throug Newton Raphson method is 1.8900297292519856
function value at that root is 1.863172869320806e-07


convergence rate are of order
Newton Raphson > Regular Falsi > Bisection Method
"""
