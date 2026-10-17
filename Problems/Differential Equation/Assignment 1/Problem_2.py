import math
import matplotlib.pyplot as plt
from a_man_lib import Nwt_Raph

x_r2 = [ (0+math.pi/100)*i for i in range(101)]
dx2 = x_r2[2]-x_r2[1] 

# 1. Forward Euler
y_p2_FE = [] 
y_p2_0 = 1  # initial condition 
y_n = y_p2_0
for x_n in x_r1:
    y_n1 = y_n + dx1 * (y_n + x_n)**2
    y_p2_FE.append(y_n1)
    y_n = y_n1

# defining function to parse in newton raphson 
def f_yn(yn,x_n1,dx2=dx2):
    def F_n(y_n1):
        return y_n1-y_n-dx2*(x_n1+y_n1)**2
    return F_n

def df_yn(x_n1, dx2=dx2):
    def dF_n(y_n1):
        return 1-2*dx2*(x_n1+y_n1)
    return dF_n

# 2. Backward Euler (Note: using x_{n+1} which is x_n + dx1 for standard BE formulation)
y_p2_BE = [] 
y_n = y_p2_0
for x_n in x_r2 :
    F_n = f_yn(y_n,x_n+dx2)
    dF_n = df_yn(x_n+dx2)
    y_n1 = Nwt_Raph(F_n,dF_n,5)
    y_p2_BE.append(y_n1)
    y_n = y_n1

# 3. Predictor-Corrector method 
y_p1_PC = [] 
y_n = y_p2_0
for x_n in x_r2:
    kappa1 = dx2 * (y_n + x_n)**2
    y_n1_pred = y_n + dx2 * (y_n + x_n)**2
    kappa2 = dx1 * (y_n1_pred + (x_n + dx1))**2
    kappa = (kappa1 + kappa2) / 2
    y_n1 = y_n + kappa    
    y_p1_PC.append(y_n1)
    y_n = y_n1
