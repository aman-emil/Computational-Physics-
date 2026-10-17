import matplotlib.pyplot as plt
from a_man_lib import chsk, forward_substitution_chsk, back_substitution

def make_tridiagonal_matrix(N):
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            if i == j:
                row.append(2)
            elif abs(i - j) == 1:
                row.append(-1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

# Grid 
x0 = 0
xn = 1
dx = 0.01
step = int((xn - x0) / dx)


x_intr = [x0 + i * dx for i in range(step + 1)]

def d2ydx2(x):
    return -2

f_vals = [d2ydx2(x) * (-dx**2) for x in x_intr]

# Boundary conditions (alpha for x0, beta for xn)
alpha = 1
beta = 3 
f_vals[0] += alpha
f_vals[-1] += beta

# Adjust matrix size for interior points (N = step - 1)
N = step - 1
Tr_Dia = make_tridiagonal_matrix(N)

x_interior = x_intr[1:-1]
f_vals_interior = f_vals[1:-1]
f_vals_interior[0] += alpha  
f_vals_interior[-1] += beta  

Tr_Dia = make_tridiagonal_matrix(len(f_vals_interior))

L = chsk(Tr_Dia)
y_sub = forward_substitution_chsk(L, f_vals_interior)
U = [[L[j][i] for j in range(len(L))] for i in range(len(L))]
Val_interior = back_substitution(U, y_sub)

# Full numerical solution vector including boundaries
Val = [alpha] + Val_interior + [beta]

# Analytic Solution 
y_analytic = [-x**2 + 3*x + 1 for x in x_intr]

plt.figure(figsize=(9, 5))
plt.plot(x_intr, Val, label='Numerical Solution (Val)', color='blue', linewidth=2)
plt.plot(x_intr, y_analytic, label='Analytic Solution ($y = -x^2 + 3x + 1$)', color='red', linestyle='--', linewidth=2)

plt.title('Comparison of Numerical and Analytic Solutions')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.grid(True)
plt.savefig("Problem_3.png")
plt.show()