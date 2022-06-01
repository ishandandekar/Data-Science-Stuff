# A library-free collection of functions made in context of linear algebra.
# Hope this makes your math in python easier!

def gen_zeros(rows: int, cols: int):
    """Returns a matrix where every value is 0

    Args:
        rows (int): number of rows of matrix
        cols (int): number of columns of matrix

    Returns:
        list: a n-dim array of shape
    """
    mat = list()
    for i in range(rows):
        for j in range(cols):
            mat[i][j] = 0
    return mat


def gen_identity(shape: int):
    """Returns an identity matrix

    Args:
        shape (int): number of rows or columns of matrix

    Returns:
        list: an identity matrix
    """
    mat = gen_zeros(rows=shape, cols=shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            if i == j:
                mat[i][j] = 1
    return mat


def copy_matrix(matrix):
    """Returns a copy of the matrix

    Args:
        matrix (Iterable): an object which is iterable representing a matrix of 2 dimensions

    Returns:
        list: copy of the matrix
    """
    rows = len(matrix)
    cols = len(matrix[0])
    copy = gen_zeros(rows, cols)
    for i in range(rows):
        for j in range(cols):
            copy[i][j] = matrix[i][j]
    return copy


def gen_transpose(matrix):
    """Returns the transpose of the matrix

    Args:
        matrix (list): list representing a matrix

    Returns:
        list: transpose of the matrix
    """
    if not isinstance(matrix[0], list):
        matrix = [matrix]

    rows = len(matrix)
    cols = len(matrix[0])

    # Section 3: MT is zeros matrix with transposed dimensions
    transpose = gen_zeros(rows, cols)

    # Section 4: Copy values from M to it's transpose MT
    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]

    return transpose


def add_matrix(A, B):
    """Adds two matrices

    Args:
        A (list): list representing a matrix
        B (list): list representing a matrix

    Raises:
        ArithmeticError: Shape of matrix A and B should match

    Returns:
        list: representing addition of matrices
    """
    rows_a = len(A)
    cols_a = len(A[0])
    rows_b = len(B)
    cols_b = len(B[0])
    if rows_a == rows_b and cols_a == cols_b:
        matrix = gen_zeros(rows_a, cols_a)
        for i in range(rows_a):
            for j in range(cols_a):
                matrix[i][j] = A[i][j]+B[i][j]
        return matrix
    else:
        raise ArithmeticError("Shape of matrices don't match!")


def subtract_matrix(A, B):
    """Subtracts two matrices

    Args:
        A (list): list representing a matrix
        B (list): list representing a matrix

    Raises:
        ArithmeticError: Shape of matrix A and B should match

    Returns:
        list: representing subtraction of matrices
    """
    rows_a = len(A)
    cols_a = len(A[0])
    rows_b = len(B)
    cols_b = len(B[0])
    if rows_a == rows_b and cols_a == cols_b:
        matrix = gen_zeros(rows_a, cols_a)
        for i in range(rows_a):
            for j in range(cols_a):
                matrix[i][j] = A[i][j]-B[i][j]
        return matrix
    else:
        raise ArithmeticError("Shape of matrices don't match!")


def matrix_multiply(A, B):
    """Multiplies two matrices

    Args:
        A (list): representing a matrix
        B (list): representing a matrix

    Raises:
        ArithmeticError: Shapes of matrices should be same

    Returns:
        list: representing a matrix
    """
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if colsA != rowsB:
        raise ArithmeticError(
            'Number of A columns must equal number of B rows.')
    C = gen_zeros(rowsA, colsB)
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C


def is_equal(A, B, tol: int = None):
    """Checks if two matrices are equal

    Args:
        A (list): representing a matrix
        B (list): representing a matrix
        tol (int, optional): tolerance of numbers in the matrix. Defaults to None.

    Returns:
        bool: A boolean value representing if the matrices are equal or not
    """
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False

    for i in range(len(A)):
        for j in range(len(A[0])):
            if tol is None:
                if A[i][j] != B[i][j]:
                    return False
            else:
                if round(A[i][j], tol) != round(B[i][j], tol):
                    return False

    return True


def dot_product(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if rowsA != rowsB or colsA != colsB:
        raise ArithmeticError('Matrices are NOT the same size.')

    result = 0
    for i in range(rowsA):
        for j in range(colsB):
            result += A[i][j] * B[i][j]

    return result


def is_square(matrix):
    """Checks if the matrix is a square matrix

    Args:
        matrix (list): representing a matrix

    Returns:
        bool: represents the result of the condition
    """
    if len(matrix) == len(matrix[0]):
        return True
    return False


def get_trace(matrix):
    """Returns trace of the matrix

    Args:
        matrix (list): representing the matrix

    Raises:
        ArithmeticError: to check if the matrix is a square matrix

    Returns:
        int: trace of the matrix
    """
    if is_square(matrix):
        tr = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == j:
                    tr += matrix[i][i]
        return tr
    else:
        raise ArithmeticError("The matrix should be a square")


def get_sparsity_score(matrix):
    """Returns sparsity of the matrix

    Args:
        matrix (list): represents the matrix

    Returns:
        float: sparsity of the matrix rounded to 3 decimal places
    """
    rows = len(matrix)
    cols = len(matrix[0])
    total_elements = rows*cols
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                count += 1
    return round(cols/total_elements, 3)
