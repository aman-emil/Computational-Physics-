import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from a_man_lib import RK4

# Parameters
a = 0.2
b = 0.2
c = 5.7

# Rossler system equations
# RK4 function passes (*y0, x), so the arguments are (x, y, z, t)
def dxdt(x, y, z, t):
    return -y - z

def dydt(x, y, z, t):
    return x + a * y

def dzdt(x, y, z, t):
    return b + z * (x - c)

# Initial conditions and time range
interval = [0, 100]
y0_vec = [1.0, 0, 0]
slope_list = [dxdt, dydt, dzdt]

# Running the solver
y_hist, t_arr = RK4(slope_list, interval, y0_vec, dx=0.01)

# x, y, and z values
x_vals = [state[0] for state in y_hist]
y_vals = [state[1] for state in y_hist]
z_vals = [state[2] for state in y_hist]

# Plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_vals, y_vals, z_vals, color='purple', lw=0.8)
    
ax.set_title('Rössler Attractor')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.savefig("Problem_4.png")
plt.show()

## end of the problem ##
## image attached in google classroom for reference ##

