
from a_man_lib import myrand
import math
import matplotlib.pyplot as plt


myrand.seed = 24

def exp_dist(a=1):
    rand_num = myrand()
    exp_rand_num = (-1/a)*math.log(rand_num, math.e)
    return exp_rand_num

# generating 5000 exponential distribution random number
exp_rand_num_list = []

i = 0
while i < 5000:
    exp_rand_num_list.append(exp_dist())
    i += 1

xbins = [i*0.1 for i in range(0,100)]



fig, ax = plt.subplots(figsize=(8, 5))

# Plot the normalized histogram
ax.hist(exp_rand_num_list, bins=xbins, density=True, color='skyblue', edgecolor='black', alpha=0.7)
ax.set_title("Probability Density Distribution", fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel("Value", fontsize=12, labelpad=10)
ax.set_ylabel("Probability Density", fontsize=12, labelpad=10) # Crucial for density=True
ax.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
