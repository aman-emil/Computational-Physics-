

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


# global seed
seed = 24

def lcg_step():
    m = 32768
    a = 1103515245
    c = 12345
    global seed
    seed = (a * seed + c) % m
    return seed / m


def myrand(seed=0):
    if not hasattr(myrand, "x0"):
        myrand.x0 = 0
    a = 1103515245
    c = 12345
    m = 2**31
    if seed:
        myrand.x0 = seed
    x1 = (a * myrand.x0 + c) % m
    rn = x1 / m  # converting to [0.0, 1.0]
    myrand.x0 = x1
    return rn


def fact(n) :
    fval = 1
    for i in range(1,n+1):
        fval *= i
    return(fval)

def mat_mul(mat1,mat2) :
    mat_AB = []
    cols = len(mat1)
    mat2_trasposed = [list(row) for row in zip(*mat2)]
    for i in (mat1):
        for j in (mat2_trasposed) :
            sum_var = 0
            for v1,v2 in zip(i,j) :
                sum_var += v1*v2
            mat_AB.append(sum_var)
        reshaped_list = [mat_AB[i : i + cols] for i in range(0, len(mat_AB), cols)]
    return reshaped_list

def mat_T(mat):
    return [list(row) for row in zip(*mat)]

"""def mat_reshape(mat, col):
    return [list(mat[i : i + cols) for i in range(0, len(mat), cols)]"""

def dot_product(vec1, vec2) :
    dot_prd_val  = 0
    for v1,v2 in zip(vec1, vec2) :
        dot_prd_val += v1*v2
    return dot_prd_val


def mat_vec(mat1, vec1):
    vec_f = []
    for v1 in mat1 :
        sum = 0
        for v2,v3 in zip(v1,vec1) :
            sum += v2*v3
        vec_f.append(sum)
    return vec_f


def GP(t0, r, N):
    if N == 1 :
        return t0
    return t0 + GP(t0*r, r, N-1)


def HP(t0,d,N):
    if N == 1 :
        return 1/t0

    den = t0 + (N-1)*d
    return HP(t0,d,N-1) + 1/den


class MyComplex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return MyComplex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return MyComplex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = (self.real * other.real) - (self.imag * other.imag)
        imag_part = (self.real * other.imag) + (self.imag * other.real)
        return MyComplex(real_part, imag_part)

    def modulus(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def __str__(self):
        sign = "+" if self.imag >= 0 else "-"
        return f"({self.real} {sign} {abs(self.imag)}j)"
