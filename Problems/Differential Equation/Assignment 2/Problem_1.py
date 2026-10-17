import matplotlib.pyplot as plt
from a_man_lib import RK4

# Parameters from the problem
Y = 2e11
q = 5000
alpha = 0.05 * 0.05
I = alpha**2 / 12
L = 2.0

# Define functions for the system of first-order ODEs
def func1(y, dy, x):
    return dy

def func2(y, dy, x):
    f_val = -(q / (2 * Y * I)) * x * (x - L)
    return f_val

Interval = [0, L]
slope_list = [func1, func2]

# Initial guesses for chi (slope at x = 0)
x_guess_1 = 0.01
x_guess_2 = 0.06

chi_upper = max(x_guess_1, x_guess_2)
chi_lower = min(x_guess_1, x_guess_2)

tol = 1000.0  # Initial tolerance flag to enter the loop
target_val = 0.0  # Boundary condition at x = L is y(L) = 0
wrong_curves = []  # Array to store all intermediate/wrong deflection curves

max_iterations = 50
iteration_count = 0

while tol > 0.001 and iteration_count < max_iterations:
    iteration_count += 1
    
    y0_lower = [0.0, chi_lower]
    y0_upper = [0.0, chi_upper]
    
    # Integrate both boundary guesses
    y_hist_lower, x_intr = RK4(slope_list, Interval, y0_lower, dx=0.01)
    y_hist_upper, x_intr = RK4(slope_list, Interval, y0_upper, dx=0.01)

    y_vals_lower = [state[0] for state in y_hist_lower]
    y_vals_upper = [state[0] for state in y_hist_upper]

    # Store wrong curves for later plotting
    wrong_curves.append((x_intr, y_vals_lower, f"Iter {iteration_count} (lower)"))
    wrong_curves.append((x_intr, y_vals_upper, f"Iter {iteration_count} (upper)"))

    # Boundary residuals at x = L (i.e., last element)
    y_b_lower = y_vals_lower[-1]
    y_b_upper = y_vals_upper[-1]
    
    # Calculate current tolerance based on boundary mismatch
    tol = abs(y_b_lower - target_val)
    if tol < 1e-6:
        break

    # Lagrange interpolation formula from image: 
    # chi = chi_l + ((chi_h - chi_l) / (y_chi_h(b) - y_chi_l(b))) * (y(b) - y_chi_l(b))[cite: 2]
    # Here y(b) target is 0.0
    chi_new = chi_lower + ((chi_upper - chi_lower) / (y_b_upper - y_b_lower)) * (target_val - y_b_lower)

    # Bracket update logic based on residuals/signs
    if y_b_lower * y_b_upper < 0:
        # Standard root bracketing: choose which side chi_new replaces
        if y_b_lower * ((RK4(slope_list, Interval, [0.0, chi_new], dx=0.01)[0][-1][0]) - target_val) < 0:
            chi_upper = chi_new
        else:
            chi_lower = chi_new
    else:
        # Fallback adjustment if signs match
        chi_lower = chi_upper
        chi_upper = chi_new

# Final converged integration run
y_hist_final, x_intr = RK4(slope_list, Interval, [0.0, chi_lower], dx=0.01)
y_vals_final = [state[0] for state in y_hist_final]

# Plotting results
plt.figure(figsize=(10, 6))

# Plot all stored wrong curves faintly
for x_vals, y_vals, label in wrong_curves:
    plt.plot(x_vals, y_vals, color='orange', alpha=0.5, linestyle=':')

# Highlight the final converged solution
plt.plot(x_intr, y_vals_final, color='blue', linewidth=2.5, label=f'Converged Solution (chi={chi_lower:.4f})')

plt.title('Shooting Method with Lagrange Interpolation for Beam Deflection')
plt.xlabel('x')
plt.ylabel('Deflection y(x)')
plt.legend()
plt.grid(True)
plt.savefig("Problem_1.png")
plt.show()

def find_min_and_half_min(lst):
    m = min(lst)
    return m, m / 2

mx,hmx = find_min_and_half_min(y_vals_final)

print(f"Maximum Depression {abs(mx)}")
print(f"Half Maximum Depression {abs(hmx)}")

## End of the problem ##
## Terminal Output for refernce ## 
""""
Maximum Depression -0.009919601999999972
Half Maximum Depression -0.004959800999999986
"""
