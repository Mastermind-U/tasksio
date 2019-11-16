from collections import Counter
from vectors import sum_of_squares
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
