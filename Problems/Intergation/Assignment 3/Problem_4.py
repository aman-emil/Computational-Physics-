from a_man_lib import Gauss_Quad, sim_s
import math

interval = [0, "infty"]
N_quad = 5
pwr = 4
def P4_func1(x):
    func_val = math.exp(-x)*(x**pwr)
    return func_val 

intint_quad_analytical = math.factorial(pwr)

int_val_quad = Gauss_Quad(P4_func1, interval[0], interval[1], N_quad)
error_quad = abs(intint_quad_analytical - int_val_quad)
(intint_quad_analytical - int_val_quad)
print(f"Gauss Quadrature Value: {int_val_quad:.9f} | Error: {error_quad:.9e}")

### End of the problem ###
### Terminal Output for reference ###
"""
Gauss Quadrature Value: 23.999999990 | Error: 9.598245754e-09
"""