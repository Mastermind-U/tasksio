from collections import Counter
from data_science.vectors import sum_of_squares, dot
import math


def mean(x):
    """Вычисление среднего значения"""
    return sum(x) / len(x)


def median(vector):
    """Возвращает ближайшее к середине значение для vector"""
    n = len(vector)
    sorted_v = sorted(vector)
    midpoint = n // 2
    return sorted_v[midpoint] if n % 2 == 0 else (sorted_v[midpoint - 1] + sorted_v[midpoint])


def quantile(x, p):
    """Возвращает значение в x, соответствующему р-му проценту данных"""
    return sorted(x)[int(p * len(x))]


def mode(x):
    """Возвращает список, поскольку мод может быть больше одной"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]


def data_range(x):
    """Вычисление изменчивости"""
    return max(x) - min(x)


def de_mean(x):
    """
    Вектор отклонений от среднего.
    Пересчитать x, вычтя его среднее (среднее результата будет = 0)
    """
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def variance(x):
    """
    Дисперсия - это средняя сумма квадратов отклонений от среднего;
    В зарубежной литературе это - variance
    Предполагается что вектор х состоит как минимум из 2-х элементов
    """
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)


def standard_deviation(x):
    """Стандартное отклонение"""
    return math.sqrt(variance(x))


def interquartile_range(x):
    """Интерквартильный размах"""
    return quantile(x, 0.75) - quantile(x, 0.25)


def covariance(x, y):
    """Ковариация"""
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)


def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    # если переменные не меняются, то корреляция равна 0
    return 0
