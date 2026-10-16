import math

"""
Mathematical Utilities and Helper Routines
I grouped my general-purpose math and support functions here:
- Linear Congruential Generators (LCG) for pseudorandom numbers
- Factorial calculation
- Progression series summations (Geometric and Harmonic progressions)
- Custom Complex Number class
- Element-wise vector operations
- Text file parsers for matrices and vectors
"""

def lcg_generator(N, x0):
    """
    Generate an array of N pseudorandom floats in [0, 1) using a Linear Congruential Generator.
    I use the classic parameters: multiplier a = 1103515245, increment c = 12345, and modulus m = 32768.
    x0 is the seed value I start from.
    """
    a = 1103515245
    c = 12345
    m = 32768
    i = 0
    random_array = []
    while i < N:
        x1 = (a * x0 + c) % m
        random_array.append(x1)
        x0 = x1
        i += 1
    for idx, val in enumerate(random_array):
        random_array[idx] = val / m
    return random_array


# Global seed used by lcg_step for sequential random queries
seed = 24

def lcg_step():
    """
    Produce the next single pseudorandom float in [0, 1) by advancing my global seed.
    This lets me pass this function around as a continuous random number stream
    (e.g., inside Monte Carlo integration).
    """
    m = 32768
    a = 1103515245
    c = 12345
    global seed
    seed = (a * seed + c) % m
    return seed / m


def fact(n):
    """
    Compute the factorial of integer n (n!) iteratively.
    I accumulate products from 1 to n.
    """
    fval = 1
    for i in range(1, n + 1):
        fval *= i
    return fval


def GP(t0, r, N):
    """
    Compute the sum of the first N terms of a Geometric Progression (GP) recursively.
    t0 is the initial term, r is the common ratio, and N is the count of terms.
    """
    if N == 1:
        return t0
    return t0 + GP(t0 * r, r, N - 1)


def HP(t0, d, N):
    """
    Compute the sum of the first N terms of a Harmonic Progression (HP) recursively.
    The k-th denominator follows an AP: t0 + (k-1)*d.
    """
    if N == 1:
        return 1.0 / t0

    den = t0 + (N - 1) * d
    return HP(t0, d, N - 1) + 1.0 / den


class MyComplex:
    """
    A lightweight complex number implementation I built from scratch.
    It supports basic arithmetic operations (+, -, *), calculating the modulus,
    and formatted string output.
    """
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return MyComplex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return MyComplex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        real_part = (self.real * other.real) - (self.imag * other.imag)
        imag_part = (self.real * other.imag) + (self.imag * other.real)
        return MyComplex(real_part, imag_part)

    def modulus(self):
        """Compute the magnitude / Euclidean norm of the complex number."""
        return math.sqrt(self.real**2 + self.imag**2)

    def __str__(self):
        sign = "+" if self.imag >= 0 else "-"
        return f"({self.real} {sign} {abs(self.imag)}j)"


def vector_op(list1, list2, op):
    """
    Perform element-wise binary operations between two lists/vectors.
    Supported operations: '+', '-', and '*'.
    """
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y
    }
    return [ops[op](x, y) for x, y in zip(list1, list2)]


def parse_matrix_file(file_path):
    """
    Read and parse a matrix from a plain text file.
    I handle both space-separated and comma-separated numeric entries,
    casting each value to float or int as appropriate.
    """
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                row = [float(val) if '.' in val else int(val) for val in line.replace(',', ' ').split()]
                matrix.append(row)
    return matrix


def parse_vector_file(file_path):
    """
    Read and parse a 1D vector from a plain text file.
    I flatten lines into a continuous 1D numeric list.
    """
    vector = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                values = [float(val) if '.' in val else int(val) for val in line.replace(',', ' ').split()]
                vector.extend(values)
    return vector
