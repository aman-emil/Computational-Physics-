##############################################################
# Problem 2
##############################################################

import matplotlib.pyplot as plt 

m = 32768  # definig m as global as i will need it in the plot

def lcg_generator(N,x0): # No. of element taht i want in the array, x0 is the seed here
    a = 1103515245
    c = 12345
    m = 32768 
    i = 0 # using it here as counter  
    random_array = []
    while i < N : 
        x1  = (a*x0 + c) % m
        random_array.append(x1)
        x0 = x1
        i +=1 
    for idx,val in enumerate(random_array) : 
        random_array[idx] = val/m
    return random_array

def correlation_func(rand_num_list,k): # rand_arr is the random nuumber array and k is the lag between x_i and x_(i+k)
    y = rand_num_list[k:]
    x = rand_num_list[:-k] 
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

random_array = lcg_generator(1000, 24)
xy = correlation_func(random_array,5)
x = xy[0]
y = xy[1]
plt_correlation(x,y,5)

## end of the problem
