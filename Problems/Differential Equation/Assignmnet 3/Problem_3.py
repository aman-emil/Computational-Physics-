import matplotlib.pyplot as plt
from a_man_lib import RK4

# Parameters
mu = 0.15
k = 1.0
m = 1.0
omega_sq = k / m

# the system of first-order ODEs
# Your RK4 function passes (*y0, x), so the arguments are (x, v, t)
def dxdt(x, v, t):
    return v

def dvdt(x, v, t):
    return -mu * v - omega_sq * x

# Initial conditions and time range
interval = [0, 40]
y0_vec = [1.0, 0.0]
slope_list = [dxdt, dvdt]

# Solve using the provided RK4 function
y_hist, t_arr = RK4(slope_list, interval, y0_vec, dx=0.01)

# x and v values
x_vals = [state[0] for state in y_hist]
v_vals = [state[1] for state in y_hist]

# Total Energy: E = 0.5 * m * v^2 + 0.5 * k * x^2
energy_vals = [0.5 * m * v**2 + 0.5 * k * x**2 for x, v in zip(x_vals, v_vals)]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t_arr, x_vals, label='Position (x)', color='blue')
plt.plot(t_arr, v_vals, label='Velocity (v)', color='orange')
plt.plot(t_arr, energy_vals, label='Total Energy (E)', color='green', linestyle='--')
    
plt.title('Damped Simple Harmonic Oscillator')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude / Energy')
plt.legend()
plt.grid(True)
plt.savefig("Problem_3.png")
plt.show()

## end of the problem ##
## image attached in google classroom for reference ##
