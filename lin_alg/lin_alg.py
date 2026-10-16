import math

"""
Linear Algebra Routines
I wrote these functions to handle core matrix and vector operations from scratch,
including matrix multiplication, factorizations (LU, Cholesky), direct solvers (Gauss-Jordan,
forward/back substitution), and iterative solvers (Jacobi, Gauss-Seidel, SOR).
"""

def mat_mul(mat1, mat2):
    """
    Multiply two matrices mat1 (A) and mat2 (B).
    I first transpose mat2 so I can easily do row-by-row dot products,
    then reshape the flat output list into an m x n matrix.
    """
    mat_AB = []
    cols = len(mat1)
    mat2_trasposed = [list(row) for row in zip(*mat2)]
    for i in mat1:
        for j in mat2_trasposed:
            sum_var = 0
            for v1, v2 in zip(i, j):
                sum_var += v1 * v2
            mat_AB.append(sum_var)
    reshaped_list = [mat_AB[i : i + cols] for i in range(0, len(mat_AB), cols)]
    return reshaped_list


def mat_T(mat):
    """
    Compute the transpose of a matrix.
    I use python's zip(*mat) unpacking trick to swap rows and columns cleanly.
    """
    return [list(row) for row in zip(*mat)]


def dot_product(vec1, vec2):
    """
    Compute the scalar dot product of two vectors vec1 and vec2.
    I iterate pairwise and accumulate the products of corresponding elements.
    """
    dot_prd_val = 0
    for v1, v2 in zip(vec1, vec2):
        dot_prd_val += v1 * v2
    return dot_prd_val


def mat_vec(mat1, vec1):
    """
    Multiply a matrix by a vector: A * x.
    I take each row of mat1 and compute its dot product with vec1.
    """
    vec_f = []
    for v1 in mat1:
        sum_val = 0
        for v2, v3 in zip(v1, vec1):
            sum_val += v2 * v3
        vec_f.append(sum_val)
    return vec_f


def aug_mat(matrix, vector):
    """
    Construct an augmented matrix [A | b] by appending vector elements as the last column.
    I use this before feeding systems into elimination routines like Gauss-Jordan.
    """
    augmented_matrix = [row + [val] for row, val in zip(matrix, vector)]
    return augmented_matrix


def gauss_jordan(matrix):
    """
    Solve a linear system using Gauss-Jordan elimination with partial pivoting.
    I take an augmented matrix [A | b], perform forward and backward elimination
    to transform the matrix into reduced row echelon form (diagonal matrix),
    normalize each row by the pivot value, and return the solution vector.
    """
    mat = [row[:] for row in matrix]
    n_rows = len(mat)
    n_cols = len(mat[0])

    # Forward elimination with partial pivoting (sorting descending by absolute pivot)
    for j in range(min(n_rows, n_cols)):
        fixed = mat[:j]
        active = mat[j:]
        active.sort(key=lambda r: abs(r[j]), reverse=True)
        mat = fixed + active

        pivot_row = mat[j]
        pivot_val = pivot_row[j]
        if pivot_val == 0:
            continue

        for i in range(j + 1, n_rows):
            current_row = mat[i]
            current_val = current_row[j]
            if current_val != 0:
                mat[i] = [
                    (pivot_val * c_elem) - (current_val * p_elem)
                    for p_elem, c_elem in zip(pivot_row, current_row)
                ]

    # Backward elimination to eliminate elements above the diagonal
    for j in range(min(n_rows, n_cols) - 1, -1, -1):
        pivot_row = mat[j]
        pivot_val = pivot_row[j]
        if pivot_val == 0:
            continue

        for i in range(j - 1, -1, -1):
            current_row = mat[i]
            current_val = current_row[j]
            if current_val != 0:
                mat[i] = [
                    (pivot_val * c_elem) - (current_val * p_elem)
                    for p_elem, c_elem in zip(pivot_row, current_row)
                ]

    # Normalize rows to make diagonal entries equal to 1
    for i in range(min(n_rows, n_cols)):
        pivot_val = mat[i][i]
        if pivot_val != 0:
            mat[i] = [val / pivot_val for val in mat[i]]

    # Extract the last column which contains the solutions
    sol_vector = [row[-1] for row in mat]
    return sol_vector


def LU_Decomp(A):
    """
    Perform in-place Doolittle LU decomposition of square matrix A (A = L * U).
    I store U in the upper triangle (including diagonal) and L in the strictly
    lower triangle (with implicit 1s along L's diagonal).
    Includes row swapping if I encounter a zero pivot on the diagonal.
    """
    n = len(A)

    for i in range(n):
        # Check for zero pivot and swap with a subsequent row if needed
        if A[i][i] == 0:
            swap_row = -1
            for r in range(i + 1, n):
                if A[r][i] != 0:
                    swap_row = r
                    break

            if swap_row != -1:
                A[i], A[swap_row] = A[swap_row], A[i]
            else:
                raise ValueError("Matrix is singular or leading submatrix has a zero determinant. LU decomposition fails!")

        # Upper triangular entries: U[i][j] = A[i][j] - sum_{k < i}(L[i][k] * U[k][j])
        for j in range(i, n):
            s = 0
            for k in range(i):
                s += A[i][k] * A[k][j]
            A[i][j] = A[i][j] - s

        # Lower triangular entries: L[j][i] = (A[j][i] - sum_{k < i}(L[j][k] * U[k][i])) / U[i][i]
        for j in range(i + 1, n):
            s = 0
            for k in range(i):
                s += A[j][k] * A[k][i]
            A[j][i] = (A[j][i] - s) / A[i][i]

    return A


def chsk(matrix):
    """
    Perform in-place Cholesky decomposition of a symmetric, positive-definite matrix A = L * L^T.
    I first verify that the matrix is symmetric. Then I compute the lower triangular matrix L
    in-place, zeroing out the upper triangular entries.
    """
    n = len(matrix)

    # First, I check whether the input matrix is symmetric
    for i in range(n):
        for j in range(i):
            if matrix[i][j] != matrix[j][i]:
                print("asymmetric matrix")
                return None

    # Compute Cholesky factor L in-place
    for i in range(n):
        for j in range(i + 1):
            s = 0
            if i == j:
                # Diagonal entries: L[i][i] = sqrt(A[i][i] - sum(L[i][k]^2))
                for k in range(j):
                    s += matrix[i][k] ** 2

                val = matrix[i][i] - s
                matrix[i][i] = math.sqrt(val)
            else:
                # Off-diagonal entries: L[i][j] = (A[i][j] - sum(L[i][k]*L[j][k])) / L[j][j]
                for k in range(j):
                    s += matrix[i][k] * matrix[j][k]

                matrix[i][j] = (matrix[i][j] - s) / matrix[j][j]

        # Zero out the upper triangle
        for j in range(i + 1, n):
            matrix[i][j] = 0

    return matrix


def forward_substitution(L, b):
    """
    Perform forward substitution to solve L * y = b, assuming unit lower triangular matrix L (L[i][i] = 1).
    I use this step right after LU decomposition (where L has ones on the diagonal).
    """
    n = len(b)
    y = [0.0] * n

    for i in range(n):
        sum_val = 0.0
        for j in range(i):
            sum_val += L[i][j] * y[j]
        y[i] = b[i] - sum_val

    return y


def forward_substitution_chsk(L, b):
    """
    Perform forward substitution to solve L * y = b for a non-unit lower triangular matrix L.
    Unlike standard Doolittle L, the Cholesky factor has non-unit values on its diagonal,
    so I divide by L[i][i] at each step.
    """
    n = len(b)
    y = [0.0] * n

    for i in range(n):
        sum_val = 0.0
        for j in range(i):
            sum_val += L[i][j] * y[j]
        y[i] = (b[i] - sum_val) / L[i][i]

    return y


def back_substitution(U, y):
    """
    Perform backward substitution to solve U * x = y for an upper triangular matrix U.
    I iterate from the bottom row upwards, substituting known values of x into earlier rows.
    """
    n = len(y)
    x = [0.0] * n

    for i in range(n - 1, -1, -1):
        sum_val = 0.0
        for j in range(i + 1, n):
            sum_val += U[i][j] * x[j]

        x[i] = (y[i] - sum_val) / U[i][i]

    return x


def jacobi(A, b, guess):
    """
    Solve A * x = b iteratively using the Jacobi method.
    In each iteration, I compute new approximations using only values from the previous iteration,
    checking convergence against Euclidean distance tolerance.
    """
    iter_n = 500
    tol = 1e-6
    col_mat = len(A)

    # I make sure diagonal entries are non-zero by swapping rows if necessary
    for i in range(col_mat):
        if A[i][i] == 0:
            l = i + 1
            swapped = False
            while l < col_mat:
                if A[l][i] != 0:
                    A[i], A[l] = A[l], A[i]
                    b[i], b[l] = b[l], b[i]
                    swapped = True
                    break
                l += 1
            if not swapped:
                raise ValueError(f"Matrix is singular or column {i} has all zeros below diagonal.")

    x_1 = [1] * len(b)
    x = list(guess)

    for iter in range(iter_n):
        for i in range(len(x)):
            sum_val = 0
            for j in range(len(x)):
                if i != j:
                    sum_val += A[i][j] * x[j]
            nval = (1 / A[i][i]) * (b[i] - sum_val)
            x_1[i] = nval

        tol_sum = 0
        for idx in range(col_mat):
            diff = abs(x[idx] - x_1[idx])
            tol_sum += diff
        if math.sqrt(tol_sum) < tol:
            break
        x = list(x_1)

    return x


def gauss_sdl(A, b, guess):
    """
    Solve A * x = b iteratively using the Gauss-Seidel method.
    Unlike Jacobi, I immediately use the updated solution components in the current iteration,
    which usually gives me faster convergence.
    """
    tol = 1e-3
    iter_n = 100
    col_mat = len(A)

    # Pivot row swap to ensure non-zero diagonal entries
    for i in range(col_mat):
        if A[i][i] == 0:
            l = i + 1
            swapped = False
            while l < col_mat:
                if A[l][i] != 0:
                    A[i], A[l] = A[l], A[i]
                    b[i], b[l] = b[l], b[i]
                    swapped = True
                    break
                l += 1
            if not swapped:
                raise ValueError(f"Matrix is singular or column {i} has all zeros below diagonal.")

    x = [float(val) for val in guess]
    col_len = len(A)

    for iter in range(iter_n):
        tol_var = 0.0

        for i in range(col_len):
            sum1 = 0.0
            sum2 = 0.0

            for j in range(0, i):
                sum1 += A[i][j] * x[j]
            for j in range(i + 1, col_len):
                sum2 += A[i][j] * x[j]

            nval = (1 / A[i][i]) * (b[i] - sum1 - sum2)
            tol_var += (nval - x[i]) ** 2
            x[i] = nval

        distance = math.sqrt(tol_var)
        if distance < tol:
            print(f"Converged in {iter + 1} iterations.")
            break

    return x


def SOR(A, b, guess, ome):
    """
    Solve A * x = b iteratively using Successive Over-Relaxation (SOR).
    I introduce a relaxation factor 'ome' (omega) to accelerate the Gauss-Seidel convergence
    rate (over-relaxation for omega in (1, 2)).
    """
    iter_n = 500
    tol = 1e-6
    col_mat = len(A)

    for i in range(col_mat):
        if A[i][i] == 0:
            l = i + 1
            swapped = False
            while l < col_mat:
                if A[l][i] != 0:
                    A[i], A[l] = A[l], A[i]
                    b[i], b[l] = b[l], b[i]
                    swapped = True
                    break
                l += 1
            if not swapped:
                raise ValueError(f"Matrix is singular or column {i} has all zeros below diagonal.")

    x = [float(val) for val in guess]
    col_len = len(A)
    iter_count = 0

    for iter in range(iter_n):
        iter_count += 1
        tol_var = 0.0

        for i in range(col_len):
            sum1 = 0.0
            sum2 = 0.0

            for j in range(0, i):
                sum1 += A[i][j] * x[j]
            for j in range(i + 1, col_len):
                sum2 += A[i][j] * x[j]
            x_new = (1 - ome) * x[i] + (ome / A[i][i]) * (b[i] - sum1 - sum2)
            tol_var += (x_new - x[i]) ** 2
            x[i] = x_new

        if math.sqrt(tol_var) < tol:
            break

    print(f"Converged in {iter_count} iterations.")
    return x
