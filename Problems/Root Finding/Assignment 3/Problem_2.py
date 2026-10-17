import math
from a_man_lib import Lag_Pol, deflation

P1 = [1, -1, -7, 1, 6]
P2 = [1, 0, -5, 0, 4]
P3 = [2, 0, -19.5, 0.5, 13.5, -4.5]

def find_all_roots(pol, initial_guess=0.0):
    roots = []
    current_pol = list(pol)
    
    # Looping until polynomial is reduced to degree 1 
    while len(current_pol) > 2:
        # Find a root using Laguerre's method
        root = Lag_Pol(current_pol, initial_guess)
        roots.append(root)
        
        # Deflate the polynomial using the found root
        current_pol = deflation(current_pol, root)
        
    # For the last remaining linear factor: ax + b = 0  =>  x = -b / a
    if len(current_pol) == 2:
        last_root = -current_pol[1] / current_pol[0]
        last_root = last_root.real
        roots.append(last_root)
        
    return roots

for plnm in [P1, P2, P3]: 
    all_roots = find_all_roots(plnm, initial_guess=0.0)
    print(f"Found Roots for polynomial whose coefficient in descenting order is {P1}:, {all_roots} \n")


###### End of the Problems ######
###### Terminal Output ######
"""
Found Roots for polynomial whose coefficient in descenting order is [1, -1, -7, 1, 6]:, [-1.0, 1.0, -2.0, 3.0]
Found Roots for polynomial whose coefficient in descenting order is [1, -1, -7, 1, 6]:, [1.0, -1.0, 2.0, -2.0]
Found Roots for polynomial whose coefficient in descenting order is [1, -1, -7, 1, 6]:, [0.4999998765881134, 0.5000001234118783, -0.9999999999999891, 2.9999999999999987, -3.0000000000000013]
"""

