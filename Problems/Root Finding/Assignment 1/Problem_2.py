from a_man_lib import root_bis, root_Reg_f
import math

# defining function in problem 2
def p2_func(x): # here a,b are the intervals
    f_val = math.log(x/2)-math.sin(5*x/2)
    return f_val

# brakets
a = 1.5
b = 3.0

# root finding using bisection method
root1, f_root1 = root_bis(p2_func, a, b)
print(f"value of root using bisection is {root1} with f(root) value is {f_root1}")

# root finding using Regula Falsi method
root2, f_root2 = root_Reg_f(p2_func, a, b)
print(f"value of root using Regula Falsi is {root2} with f(root) value is {f_root2}")

# end of the problem #
# answer in txt file #
# terminal out put #
"""
total no. of iteration are 18
value of root using bisection is 2.623140335083008 with f(root) value is 7.154571934897547e-10
total no. of iteration are 5
value of root using Regula Falsi is 2.62314050689124 with f(root) value is -3.4720778063768165e-07
"""
