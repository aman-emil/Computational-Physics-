import matplotlib.pyplot as plt
from a_man_lib import RK4

# Parameters from the problem[cite: 3]
alpha = 0.01
Ta = 20.0
L = 10.0
Interval = [0.0, L]

# Define the system of first-order ODEs
def func1(T, dTdx, x):
    return dTdx

def func2(T, dTdx, x):
    # d^2T/dx^2 + alpha(Ta - T) = 0  =>  d^2T/dx^2 = alpha(T - Ta)
    return alpha * (T - Ta)

slope_list = [func1, func2]

# Initial guesses for chi (slope at x = 0)
x_guess_1 = 5.0
x_guess_2 = 25.0

chi_upper = max(x_guess_1, x_guess_2)
chi_lower = min(x_guess_1, x_guess_2)

tol = 1000.0
target_val = 200.0  # Boundary condition at x = L is T(L) = 200
wrong_curves = []

max_iterations = 50
iteration_count = 0

while tol > 0.05 and iteration_count < max_iterations:
    iteration_count += 1
    
    # Initial conditions: T(0) = 40, dT/dx(0) = chi
    y0_lower = [40.0, chi_lower]
    y0_upper = [40.0, chi_upper]
    
    # Integrate both boundary guesses
    y_hist_lower, x_intr = RK4(slope_list, Interval, y0_lower, dx=0.01)
    y_hist_upper, x_intr = RK4(slope_list, Interval, y0_upper, dx=0.01)

    T_vals_lower = [state[0] for state in y_hist_lower]
    T_vals_upper = [state[0] for state in y_hist_upper]

    # Store wrong curves for plotting
    wrong_curves.append((x_intr, T_vals_lower, f"Iter {iteration_count} (lower)"))
    wrong_curves.append((x_intr, T_vals_upper, f"Iter {iteration_count} (upper)"))

    # Boundary residuals at x = L (last element)
    T_b_lower = T_vals_lower[-1]
    T_b_upper = T_vals_upper[-1]
    
    tol = abs(T_b_lower - target_val)
    if tol < 0.05:
        break

    # Lagrange interpolation for chi
    chi_new = chi_lower + ((chi_upper - chi_lower) / (T_b_upper - T_b_lower)) * (target_val - T_b_lower)

    # Bracket update logic
    if (T_b_lower - target_val) * (T_b_upper - target_val) < 0:
        y_hist_new, _ = RK4(slope_list, Interval, [40.0, chi_new], dx=0.01)
        T_b_new = y_hist_new[-1][0]
        if (T_b_lower - target_val) * (T_b_new - target_val) < 0:
            chi_upper = chi_new
        else:
            chi_lower = chi_new
    else:
        chi_lower = chi_upper
        chi_upper = chi_new

# Final converged integration run
y_hist_final, x_intr = RK4(slope_list, Interval, [40.0, chi_lower], dx=0.01)
T_vals_final = [state[0] for state in y_hist_final]

# Find x where T = 100°C
x_at_100 = None
for x_val, t_val in zip(x_intr, T_vals_final):
    if t_val >= 100.0:
        x_at_100 = x_val
        break
print(f"Temperature reaches 100°C at x approx {x_at_100:.3f} m")

# Plotting results
plt.figure(figsize=(10, 6))

for x_vals, t_vals, label in wrong_curves:
    plt.plot(x_vals, t_vals, color='violet', alpha=0.5, linestyle=':')

plt.plot(x_intr, T_vals_final, color='red', linewidth=2.5, label=f'Converged Solution (chi={chi_lower:.4f})')
plt.axhline(y=100, color='blue', linestyle='--', label='T = 100°C')
if x_at_100 is not None:
    plt.axvline(x=x_at_100, color='green', linestyle=':', label=f'x = {x_at_100:.3f} m')

plt.title('Heat Conduction in a Thin Rod')
plt.xlabel('Position x (m)')
plt.ylabel('Temperature T (°C)')
plt.legend()
plt.grid(True)
plt.savefig("Problem_2.png")
plt.show()

## End of the problem ##
## Terminal Output for refernce ## 
"""Temperature reaches 100°C at x approx 4.420 m"""