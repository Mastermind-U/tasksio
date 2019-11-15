def shape(A):
    """Получить значения формы матрицы"""
    num_rows = len(A)
    num_cols = len(A[0] if A else 0)
    return num_rows, num_cols


def get_row(A, i):
    """Получить i-ю строку"""
    return A[i]


def get_column(A, j):
    """Получить j-й столбец"""
    return [item[j] for item in A]


def make_matrix(num_rows: int, num_cols: int, func):
    """
    Возвращает матрицу размером num_rows * num_cols,
    (i, j)-й элемент которой равен функции func(i, j)
    """
    return [[func(i, j) for j in range(num_cols)] for i in range(num_rows)]
