##############################################################
# Problem 1  
##############################################################

import matplotlib.pyplot as plt 

def q_dirty(N,c):
    x_i = 0.1 # seed 
    i = 0 # pointer 
    rand_num = []
    while i < N+1 : 
        x_i1 = c*x_i*(1-x_i)
        rand_num.append(x_i1)
        x_i = x_i1 
        i += 1 
    print({"Random Number Generation"})
    return rand_num

def correlation_func(rand_arr,k): # rand_arr is the random nuumber array and k is the lag between x_i and x_(i+k)
    y = rand_arr[k:]
    x = rand_arr[:-k] 
    print(len(x))
    print(len(y))
    return [x,y]

def plt_correlation(x, y, k): 
    fig, ax = plt.subplots(figsize=(8, 6), layout="constrained")
    ax.scatter(x, y, label=f'Correlation Lag {k}', color='blue')
    ax.set_title(f'Correlation Function $x_{{i+{k}}}$ and $x_i$', fontsize=14, fontweight='bold')
    ax.set_xlabel('$x_i$', fontsize=12)
    ax.set_ylabel(f'$x_{{i+{k}}}$', fontsize=12)
    ax.grid(True, linestyle=':', alpha=0.6)   
    ax.legend(loc='upper right')
    plt.show()

random_array = q_dirty(1000,4)
xy = correlation_func(random_array,10)
x = xy[0]
y = xy[1]
plt_correlation(x,y,10)

## end of the problem
