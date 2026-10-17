import math
import matplotlib.pyplot as plt

# User's defined x-ranges and step sizes
x_r1 = [0 + 0.02 * i for i in range(101)]
dx1 = x_r1[2] - x_r1[1]

# 1. Forward Euler
y_p1_FE = [] 
y_p1_0 = 0  # initial condition 
y_n = y_p1_0
for x_n in x_r1:
    y_n1 = y_n + dx1 * (y_n - x_n**2)
    y_p1_FE.append(y_n1)
    y_n = y_n1

# 2. Backward Euler (Note: using x_{n+1} which is x_n + dx1 for standard BE formulation)
y_p1_BE = [] 
y_n = y_p1_0
for x_n in x_r1:
    # Adjusted to use (x_n + dx1) for the implicit step
    y_n1 = (y_n - dx1 * ((x_n + dx1)**2)) / (1 - dx1)
    y_p1_BE.append(y_n1)
    y_n = y_n1

# 3. Predictor-Corrector method 
y_p1_PC = [] 
y_n = y_p1_0
for x_n in x_r1:
    kappa1 = dx1 * (y_n - x_n**2)
    y_n1_pred = y_n + dx1 * (y_n - x_n**2)
    kappa2 = dx1 * (y_n1_pred - (x_n + dx1)**2)
    kappa = (kappa1 + kappa2) / 2
    y_n1 = y_n + kappa    
    y_p1_PC.append(y_n1)
    y_n = y_n1

# 4. Theoretical (Exact) Solution
y_exact = []
for x in x_r1:
    # From the image: y(x) = x^2 + 2x + 2 - 2e^x
    exact_val = x**2 + 2*x + 2 - 2*math.exp(x)
    y_exact.append(exact_val)

# Plotting the results
plt.figure(figsize=(10, 6))

plt.plot(x_r1, y_p1_FE, label='Forward Euler', linestyle='--', color='blue')
plt.plot(x_r1, y_p1_BE, label='Backward Euler', linestyle='-.', color='green')
plt.plot(x_r1, y_p1_PC, label='Predictor-Corrector', linestyle=':', color='purple', linewidth=2)
plt.plot(x_r1, y_exact, label='Theoretical (Exact)', linestyle='-', color='red', alpha=0.7)

plt.title('Numerical vs Theoretical Solutions for dy/dx = y - x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()