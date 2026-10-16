
##############################################################
# Problem 4
##############################################################

import math
import matplotlib.pyplot as plt
from a_man_lib import lcg_step

lam_A = 0.0347
lam_B = 0.0198

# Initial conditions
N_A = 500
N_B = 0
N_C = 0

# Time
dt = 1.0
max_time = 150


time_history = []
history_A = []
history_B = []
history_C = []


for current_time in range(0, max_time + 1):
    time_history.append(float(current_time))
    history_A.append(N_A)
    history_B.append(N_B)
    history_C.append(N_C)

    decays_A_to_B = 0
    decays_B_to_C = 0

    prob_A = lam_A * dt
    for _ in range(N_A):
        if lcg_step() < prob_A:
            decays_A_to_B += 1

    prob_B = lam_B * dt
    for _ in range(N_B):
        if lcg_step() < prob_B:
            decays_B_to_C += 1
    N_A -= decays_A_to_B
    N_B += (decays_A_to_B - decays_B_to_C)
    N_C += decays_B_to_C

# --- Plotting with Matplotlib ---
plt.figure(figsize=(10, 6))
plt.plot(time_history, history_A, label='Nuclei A', color='crimson', lw=2)
plt.plot(time_history, history_B, label='Nuclei B', color='darkorange', lw=2)
plt.plot(time_history, history_C, label='Nuclei C', color='forestgreen', lw=2)


plt.title('Radioactive Decay Chain Simulation (A → B → C)', fontsize=14, fontweight='bold')
plt.xlabel('Time (t)', fontsize=12)
plt.ylabel('Number of Nuclei (N)', fontsize=12)
plt.xlim(0, max_time)
plt.ylim(0, 520)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11)

plt.show()

## end of problem
