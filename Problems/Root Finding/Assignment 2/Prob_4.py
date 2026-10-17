import math
from a_man_lib import mat_vec, vector_op

# I create numpy like vectorized multiplication, addition and subtraction function vecotr_op in my library, i have used them here

# defining function
def P4_func(x,y):
    fval1 = 3*x**2 - 2*x*y - 3
    fval2 = 3*y**2 - 4*x*y
    return [fval1, fval2]

# defining jacobian matrix for the above function
def Jacobian(x,y) :
    Jv11 = 6*x - 2*y
    Jv12 = -2*x
    Jv21 = -4*y
    Jv22 = 6*y - 4*x

    Jac_Mat = [[Jv11,Jv12],[Jv21,Jv22]]

    return Jac_Mat


# defining inverse of a matrix
def inverse_2x2(matrix):
    a, b = matrix[0]
    c, d = matrix[1]

    det = (a * d) - (b * c)

    if det == 0:
        print("Matrix is Singular")
        return None

    return [
        [d / det, -b / det],
        [-c / det, a / det]
    ]

# defining Newton Raphson Method
def Nwt_Raph_2D(f_x, Jacobian, x_0):
    tlr = 1e-6 # Tolerance
    x_k = x_0 #  initial guess
    tol_check = 1 # tolerance checking variable initialization
    iter_count = 0 # iteration count

    while tol_check > tlr :
        # iteration count update
        iter_count += 1

        # getting the function value
        x = x_k[0]
        y = x_k[1]

        # function value at that point
        f_k = f_x(x,y)

        # Jacobian Matrix
        jac_mat = Jacobian(x,y)

        # Taking Inverse of Jacobian
        jac_inv = inverse_2x2(jac_mat)


        # iteration variable update
        J_inv_fx_k  = mat_vec(jac_inv,f_k)

        x_k_1 = vector_op(x_k,J_inv_fx_k,"-")

        x_n = x_k_1[0]
        y_n = x_k_1[1]

        # updateing tolerance variable
        diff_norm = (x_n-x)**2 + (y_n-y)**2


        norm_x_k_1 = math.sqrt(x_n**2 + y_n**2)
        tol_check = math.sqrt(diff_norm)/norm_x_k_1


        # updating x variable
        x_k = x_k_1

        #  exit loop for max iteration
        if iter_count == 1000 :
            print("Tolerance not reached")
            break

    # printing maximum no of iteration reached
    print(f"total no. of iteration is {iter_count}")

    return x_k

print("\n")
root = Nwt_Raph_2D(P4_func, Jacobian, [2,3])
print(f"Root obtained from Newton Raphson 2d function are x:{root[0]:.4f} and y:{root[1]:.4f}")
f1, f2 = P4_func(root[0],root[1])
print(f"value of function at those points are {f1} and {f2} for f1 and f2 respectively")

###### end of the problem #######
###### Out put of the terminal #######
"""
total no. of iteration is 5
Root obtained from Newton Raphson 2d function are x:3.0000 and y:4.0000
value of function at those points are 1.4210854715202004e-14 and -7.105427357601002e-15 for f1 and f2 respectively
"""
