from a_man_lib import lcg_step, Monte_Carlo_int, ab_rand
import math
import matplotlib.pyplot as plt

N = [500*i for i in range(1, 100)] # Number of random points for Monte Carlo integration

def P3_func1(x):
    return math.sin(x)**2

interval = [-1, 1] # Integration interval for problem 3 function 1

# Analytical integral value for comparison (constant reference)
analytical_integral_value = 0.5453

mc_integrals = []
errors = []
root_N = [1 / math.sqrt(n) for n in N]  # Reference line for 1/sqrt(N)

for n in N:
    int_1 = Monte_Carlo_int(P3_func1, interval[0], interval[1], n, lcg_step)
    int_val, sig_f_sq = int_1[0], int_1[1]
    mc_integrals.append(int_val)
    errors.append(abs(int_val - analytical_integral_value))

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(N, mc_integrals, marker='o', linestyle='-', color='b', label='Monte Carlo Estimate')
plt.axhline(y=analytical_integral_value, color='r', linestyle='--', label=f'Analytical Reference ({analytical_integral_value:.4f})')
plt.xlabel('Number of Points (N)', fontsize=12)
plt.ylabel('Integral Value', fontsize=12)
plt.title(r'Monte Carlo Integration Convergence for $\sin^2(x)$ on $[-1, 1]$', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()

plt.show()

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(N, errors, marker='x', linestyle='--', color='g', label= r'Errors')
plt.plot(N, root_N, linestyle=':', color='orange', label=r'$1/\sqrt{N}$ Reference') 
plt.ylabel('Error', fontsize=12)
plt.title(r'Monte Carlo Error for $\sin^2(x)$ on $[-1, 1]$', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()
plt.show()

### end of the problem ###
### Image Attached in classroom for reference. ###
