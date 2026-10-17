from a_man_lib import Mid_Pnt, ab_rand, lcg_step, sim_s
import math

interval_a = [1,2]
N_mid_point_a = 289 
N_simson_a = 20 
def P2_func1(x): 
    return 1/x

interval_b = [0,math.pi/2]
N_mid_point_b = 610
N_simson_b = 22
def P2_func2(x): 
    return x * math.cos(x)


int_m_1 = Mid_Pnt(P2_func1, interval_a, N_mid_point_a) # mid_point integration for problem 2 function 1
int_m_2 = Mid_Pnt(P2_func2, interval_b, N_mid_point_b) # mid_point integration for problem 2 function 2
int_s_1 = sim_s(P2_func1, interval_a[0], interval_a[-1], N_simson_a) # simpson integration for problem 2 function 1
int_s_2 = sim_s(P2_func2, interval_b[0], interval_b[-1], N_simson_b) # simpson integration for problem 2 function 2


print(f"{'Method':<12} | {'Function 1 (1/x)':<22} | {'Function 2 (x*cos(x))':<22}")
print("-" * 62)
print(f"{'Midpoint':<12} | {int_m_1:<22.6f} | {int_m_2:<22.6f}")
print(f"{'Simpson':<12} | {int_s_1:<22.6f} | {int_s_2:<22.6f}")

### end of the problem ###
### Terminal Output Attached Here ###
"""
Method       | Function 1 (1/x)       | Function 2 (x*cos(x)) 
--------------------------------------------------------------
Midpoint     | 0.693147               | 0.570797              
Simpson      | 0.693147               | 0.570797   
"""