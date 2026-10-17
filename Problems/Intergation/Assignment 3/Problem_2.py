from a_man_lib import Gauss_Quad, sim_s
import math

interval = [-1, 1]
N_quad = 4


def P2_func1(x):
  return (x**2) / (1 + x**4)


int_quad_analytical = 0.487495494
int_val_quad = Gauss_Quad(P2_func1, interval[0], interval[1], N_quad)

# Calculate the error for Gauss Quadrature
error_quad = abs(int_quad_analytical - int_val_quad)

i = 4
while True:
  int_sims = sim_s(P2_func1, interval[0], interval[1], i)
  error_sims = abs(int_quad_analytical - int_sims)

  # Check if Simpson's error matches or falls below Gauss error 
  if math.isclose(error_sims, error_quad, rel_tol=1e-7, abs_tol=1e-7) or (
      error_sims <= error_quad
  ):
    break

  i += 2  # Increment i (adjust step size as sim_s requires even numbers, e.g., i += 2)

print(f"no. of simpson iteration required to match where errors match: {i}")
print(f"Gauss Quadrature Value: {int_val_quad:.9f} | Error: {error_quad:.9e}")
print(f"Simpson's Rule Value: {int_sims:.9f} | Error: {error_sims:.9e}")


### end of the problem ###
### Terminal Output for reference ###
"""
no. of simpson iteration required to match where errors match: 6
Gauss Quadrature Value: 0.481572699 | Error: 5.922794511e-03
Simpson's Rule Value: 0.489788506 | Error: 2.293012132e-03
"""