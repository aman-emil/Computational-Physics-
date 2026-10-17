from a_man_lib import Gauss_Quad, sim_s
import math

interval = [0,"infty"]
N_quad = 5

def P3_func1(x): 
    func_val = math.exp(-x)/(1+x)
    return func_val 

intint_quad_analytical = 0.59635

int_val_quad = Gauss_Quad(P3_func1, interval[0], interval[1], N_quad)
error_quad = abs(intint_quad_analytical - int_val_quad)
(intint_quad_analytical - int_val_quad)
print(f"Gauss Quadrature Value: {int_val_quad:.9f} | Error: {error_quad:.9e}")

### End of the problem ###
### Terminal Output for reference ###
"""
Gauss Quadrature Value: 0.595084088 | Error: 1.265912031e-03
"""
