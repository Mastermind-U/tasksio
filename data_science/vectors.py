from functools import reduce
import math

height_weight_age = [175, 68, 40]
grades = [95, 80, 75, 62]


def vector_add(v, w):
    """Сложение векторов"""
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_subtract(v, w):
    """Вычитание векторов"""
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors):
    """Суммирует все соответствующие элементы"""
    return reduce(vector_add, vectors)


def scalar_multiply(c: float or int, v: list = []):
    """Умножение вектора на скаляр"""
    return [c * v_i for v_i in v]


def vector_mean(vectors):
    """Компонентное среднее значение списка векторов (одинакового размера)"""
    return scalar_multiply(1 / len(vectors), vector_sum(vectors))


def dot(v, w):
    """Скалярное произведение (v_i * w_i + ... + v_n * w_n)"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    """Сумма квадратов вектора (v_1 * v_1 + ... + v_n * v_n)"""
    return dot(v, v)


def magnitude(v):
    """Величина (длина) вектора"""
    return math.sqrt(sum_of_squares(v))


def squared_distance(v, w):
    """Квадрат расстояния между векторами ((v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2) """
    return sum_of_squares(vector_subtract(v, w))


def distance(v, w):
    """Расстояние между двумя векторами"""
    return magnitude(vector_subtract(v, w))
