##############################################################
# Problem 3 
##############################################################


import math
import matplotlib.pyplot as plt
from a_man_lib import lcg_step

N_min = 50
N_max = 5000
pi_val_iter = []
num_iter = [i for i in range(N_max-N_min)]

for i in range(N_min,N_max):
    inn = 0
    out = 0
    for j in range(i):
        x = lcg_step()
        y = lcg_step()
        if x**2 + y**2 <= 1 :
            inn += 1
    pi = 4*(inn/i)
    pi_val_iter.append(pi)


y = pi_val_iter
x = num_iter

print(f"Final Estimated Pi at N=5000: {pi_val_iter[-1]}")

# =====================================================================
plt.figure(figsize=(10, 6))
plt.scatter(x ,y , label="LCG Monte Carlo Estimate", color="blue", linewidth=1.5)
plt.axhline(y=math.pi, color="red", linestyle="--", label=f"True Value of pi ({math.pi:.4f})")
plt.title("Convergence of $pi$ ", fontsize=14)
plt.xlabel("Number of Throws (N)", fontsize=12)
plt.ylabel(r"Estimated Value of $pi$", fontsize=12)
plt.xlim(20, 5000)
plt.ylim(2.0, 4.0)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(fontsize=11)
plt.show()

## end of the problem
