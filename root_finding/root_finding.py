import math

"""
Root Finding and Polynomial Routines
Here I've implemented classical single-variable root finding methods (Bisection, Regula Falsi,
Newton-Raphson, Fixed-Point), an automated root bracketing routine, and polynomial root solvers
including Laguerre's method with synthetic polynomial deflation.
"""

def brkt(func, a, b):
    """
    Find a bounding bracket [a, b] where func(a) and func(b) have opposite signs (func(a)*func(b) < 0).
    I start with an initial range [a, b]. If they have the same sign, I expand the interval outwards
    in the direction of the smaller magnitude value by a factor beta until the root is bracketed.
    """
    # Safety check: if already bracketed, return immediately
    if func(a) * func(b) < 0:
        return a, b

    beta = 0.2
    iter_count = 0

    while func(a) * func(b) > 0:
        # I shift whichever endpoint is closer to zero further outward
        if abs(func(a)) < abs(func(b)):
            a = a - beta * (b - a)
        else:
            b = b + beta * (b - a)

        iter_count += 1
        if iter_count == 500:
            break

    print(f"iteration count to find braket {iter_count}")

    if func(a) * func(b) > 0:
        print("braket not found")

    return a, b


def root_bis(func, a, b):
    """
    Find a root of func in the bracketed interval [a, b] using the Bisection method.
    At each step, I calculate midpoint c = (a + b) / 2 and replace either a or b to keep
    the sign change bracketed until the residual |func(c)| drops below tolerance.
    """
    tol = 1e-6
    iter_count = 0
    tol_check = 1

    while tol_check > tol:
        c = (a + b) / 2.0

        if func(c) == 0:
            return c, func(c)

        if func(a) * func(c) < 0:
            b = c
        else:
            a = c

        tol_check = abs(func(c))
        iter_count += 1

        if iter_count == 500:
            break

    print(f"total no. of iteration are {iter_count}")
    return c, func(c)


def root_Reg_f(func, a, b):
    """
    Find a root of func using Regula Falsi (False Position method).
    Unlike bisection which cuts intervals strictly in half, here I use the linear secant line
    between (a, func(a)) and (b, func(b)) to estimate the x-intercept, often giving faster convergence.
    """
    tol = 1e-6
    iter_count = 0
    tol_check = 1

    while tol_check > tol:
        # Calculate false position intercept c
        c = a - func(a) * ((b - a) / (func(b) - func(a)))
        fc = func(c)
        tol_check = abs(fc)

        if fc == 0:
            return c, fc

        if fc * func(a) < 0:
            b = c
        else:
            a = c

        iter_count += 1
        if iter_count == 1000:
            break

    print(f"total no. of iteration are {iter_count}")
    return c, func(c)


def Nwt_Raph(f_x, df_x, x_0):
    """
    Find a root using the Newton-Raphson method given the function f_x and its derivative df_x.
    I iteratively update x_{k+1} = x_k - f(x_k) / f'(x_k) starting from guess x_0.
    """
    tlr = 1e-6
    x_k = x_0
    tol_check = 1
    iter_count = 0

    while tol_check > tlr:
        iter_count += 1
        x_k_1 = x_k - f_x(x_k) / df_x(x_k)
        tol_check = abs(f_x(x_k))
        x_k = x_k_1

        if iter_count == 1000:
            print("Tolerance not reached")
            break

    print(f"total no. of iteration is {iter_count}")
    return x_k


def Fixed_Point(g_x, x_0):
    """
    Find a fixed point such that x = g(x) using the Fixed-Point Iteration scheme.
    I start from an initial guess x_0 and repeatedly apply g(x) until successive values
    differ by less than my prescribed tolerance.
    """
    tlr = 1e-6
    x_k = x_0
    tol_check = 1
    iter_count = 0

    while tol_check > tlr:
        iter_count += 1
        x_k_1 = g_x(x_k)
        tol_check = abs(x_k - x_k_1)
        x_k = x_k_1

        if iter_count == 500:
            print("Tolerance not reached")
            break

    print(f"total no. of iteration is {iter_count}")
    return x_k


def deflation(pol, beta):
    """
    Deflate a polynomial by factoring out a known root beta using Horner-like synthetic division:
    P(x) = (x - beta) * Q(x).
    pol is provided in descending degree order: [a_n, a_{n-1}, ..., a_1, a_0].
    I return the quotient polynomial coefficients Q(x).
    """
    ord_val = len(pol) - 1
    if ord_val < 1:
        return []

    quotient = [0] * ord_val
    quotient[0] = pol[0]

    for i in range(1, ord_val):
        quotient[i] = pol[i] + beta * quotient[i - 1]

    return quotient


def Lag_Pol(pol, x_g):
    """
    Find a root of a polynomial using Laguerre's Method starting from initial guess x_g.
    Laguerre's method is cubically convergent for simple roots and very robust even with poor guesses.
    I compute P(x), P'(x), and P''(x) at each step to determine the step adjustment 'a'.
    pol is passed in descending degree order: [a_n, ..., a_0].
    """
    ord_val = len(pol) - 1
    x_k = x_g
    iter_max = 200
    tolerance = 1e-6

    # Reverse polynomial coefficients so index matches power: [a_0, a_1, ..., a_n]
    p_coeffs = pol[::-1]

    for iter_num in range(iter_max):
        p = 0
        p_p = 0
        p_pp = 0

        for idx, val in enumerate(p_coeffs):
            p += val * (x_k ** idx)
            if idx > 0:
                p_p += val * idx * (x_k ** (idx - 1))
            if idx > 1:
                p_pp += val * (idx * (idx - 1)) * (x_k ** (idx - 2))

        if p == 0:
            return x_k

        G = p_p / p
        H = G**2 - (p_pp / p)

        radicand = (ord_val - 1) * (ord_val * H - G**2)
        sqrt_term = math.sqrt(radicand)

        d1 = G + sqrt_term
        d2 = G - sqrt_term

        # Choose the denominator with larger absolute value for numerical stability
        den = d1 if abs(d1) > abs(d2) else d2
        a = ord_val / den if den != 0 else ord_val

        if abs(a) < tolerance:
            return x_k - a

        x_k = x_k - a

    return x_k
