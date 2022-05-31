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
