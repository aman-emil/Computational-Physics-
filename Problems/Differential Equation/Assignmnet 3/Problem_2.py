from a_man_lib import RK4
import matplotlib.pyplot as plt
import math 


# problem 2 
def P2_Func_1(x,y):
    f_val = (x+y)**2
    return f_val

# making preparation to pass into the integrator 
func_list = [P2_Func_1]
interval  = [0, math.pi/5]
y0_vec = [1]
time_step_size = [0.05,0.15]

for dx in time_step_size: 
    # running the integrator 
    Y_history,x_intr = RK4(func_list, interval, y0_vec, dx)

    # Y_theoretical Values 
    y_theory = [math.tan(x + math.pi / 4) - x for x in x_intr]

    # Y_history contains [ [y1_0, y2_0, ...], [y1_1, y2_1, ...], ... ]
    y1_vals = [y[0] for y in Y_history]

    # 2. Extract pairs of (x, y1)
    xy1_pairs = list(zip(x_intr, y1_vals))

    # 3. Plot y1 vs x
    plt.figure(figsize=(8, 5))
    plt.plot(x_intr, y_theory, label=r'$y_1(x)$', linestyle = "--", color='r', linewidth=2)
    plt.plot(x_intr, y1_vals, label=r'$y_1(x)$', color='b', linewidth=1)
    plt.title(r'RK4 Solution for $\frac{dy}{dx} = (x+y)^2$', fontsize=14)
    plt.xlabel('x', fontsize=12)
    plt.ylabel(r'$y$', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.savefig(f"Problem_2_{dx}.png")
    plt.show()

## end of the problem ## 
## image attached in google classroom for reference ##
