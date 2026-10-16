import copy

"""
Ordinary Differential Equations (ODE) Solvers
I wrote these numerical integration routines to solve systems of coupled first-order ODEs.
Both implementations use the classical 4th-order Runge-Kutta (RK4) method.
"""

def RK4(slope_list, interval, y0_vec, dx=0.01):
    """
    Solve coupled ODEs using the classical 4th-order Runge-Kutta (RK4) scheme.
    Each derivative function in slope_list is expected to accept unpacked variables (*y, x),
    meaning f(y0, y1, ..., yn, x).
    I return the full trajectory y_hist alongside the discretized domain x_intr.
    """
    int_range = int((interval[-1] - interval[0]) / dx)
    x_int_0 = interval[0]

    # Generate x grid points across the integration interval
    x_intr = [x_int_0 + i * dx for i in range(int_range)]

    # Clone the initial conditions vector so I don't mutate external state
    y0 = list(y0_vec)
    y_hist = [copy.deepcopy(y0)]

    for x in x_intr[:-1]:
        n = len(slope_list)

        # Step 1: k1 slopes at the start of the step
        kp1 = [dx * func(*y0, x) for func in slope_list]

        # Step 2: k2 slopes evaluated at the midpoint using k1
        y_k2 = [y0[i] + kp1[i] / 2 for i in range(n)]
        kp2 = [dx * func(*y_k2, x + dx / 2) for func in slope_list]

        # Step 3: k3 slopes evaluated at the midpoint using k2
        y_k3 = [y0[i] + kp2[i] / 2 for i in range(n)]
        kp3 = [dx * func(*y_k3, x + dx / 2) for func in slope_list]

        # Step 4: k4 slopes evaluated at the end of the interval using k3
        y_k4 = [y0[i] + kp3[i] for i in range(n)]
        kp4 = [dx * func(*y_k4, x + dx) for func in slope_list]

        # Weighted combination of slopes to advance to the next step
        for i in range(n):
            y0[i] = y0[i] + (1.0 / 6.0) * (kp1[i] + 2 * kp2[i] + 2 * kp3[i] + kp4[i])

        y_hist.append(copy.deepcopy(y0))

    return y_hist, x_intr


def RK4_Modified(slope_list, interval, y0_vec, dx=0.01):
    """
    Generalized 4th-order Runge-Kutta solver.
    Unlike RK4 where derivative functions take unpacked args (*y, x),
    here each function in slope_list takes the state vector directly as f(y_vec, x).
    This makes it much more convenient when handling arbitrarily large or dynamic state vectors.
    """
    int_range = int((interval[-1] - interval[0]) / dx)
    x_int_0 = interval[0]

    # Discretize domain into step increments of dx
    x_intr = [x_int_0 + i * dx for i in range(int_range)]

    y0 = list(y0_vec)
    y_hist = [copy.deepcopy(y0)]

    for x in x_intr[:-1]:
        n = len(slope_list)

        # k1 slopes evaluated at current state y0 and time/position x
        kp1 = [dx * func(y0, x) for func in slope_list]

        # k2 slopes at half-step midpoint
        y_k2 = [y0[i] + kp1[i] / 2 for i in range(n)]
        kp2 = [dx * func(y_k2, x + dx / 2) for func in slope_list]

        # k3 slopes at half-step midpoint
        y_k3 = [y0[i] + kp2[i] / 2 for i in range(n)]
        kp3 = [dx * func(y_k3, x + dx / 2) for func in slope_list]

        # k4 slopes at full step
        y_k4 = [y0[i] + kp3[i] for i in range(n)]
        kp4 = [dx * func(y_k4, x + dx) for func in slope_list]

        # Advance state vector with weighted RK4 formula
        for i in range(n):
            y0[i] = y0[i] + (1.0 / 6.0) * (kp1[i] + 2 * kp2[i] + 2 * kp3[i] + kp4[i])

        y_hist.append(copy.deepcopy(y0))

    return y_hist, x_intr
