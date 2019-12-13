import random
import math
from collections import Counter
from matplotlib import pyplot as plt


BOY = 'boy'
GIRL = 'girl'


def random_kid():
    return random.choice([BOY, GIRL])


def uniform_pdf(x):
    """
    Дифференциальная функция равномерного распределения (ДФР)
    probability density function
    """
    return 1 if x >= 0 and x < 1 else 0


def uniform_cdf(x):
    """
    Интегральная функция распределения (ИФР)
    cumulative distribution function
    Возвращает вероятность того,
    что равномерно распределенная случайная величина <=x
    """
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1


def normal_pdf(x, mu=0, sigma=1):
    """ДФР нормального распределения"""
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x - mu) ** 2 / 2 / (sigma * sigma)) / (sqrt_two_pi * sigma))


def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """
    Обратная ИФР нормального распределения
    tolerance - константа точности
    Найти приближенную версию, используя двоичный поиск
    """

    # если не стандартизировано, стандартизировать и прошкалировать
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z, low_p = -10.0, 0  # normal_cdf(-10) = (очень близко) к 0
    hi_z, hi_p = 10.0, 0  # normal_cdf(10) = (очень близко) к 1

    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2  # Взять серидину
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            #  Значение серидины всё еще низкое, искать выше его
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            #  Значение середины всё еще слишком высокое, искать ниже
            hi_z, hi_p = mid_z, mid_p
        else:
            break

    return mid_z


def bernully_trial(p):
    """
    Независимое испытание Бернулли, в котором имеется всего два
    случайных исхода (1 и 0) с постоянной вероятностью
    """
    return 1 if random.random() < p else 0


def binominal(n, p):
    """Биноминальное распределение"""
    return sum(bernully_trial(p) for _ in range(n))


def make_hist(p, n, num_points, plt=plt):
    data = [binominal(n, p) for _ in range(num_points)]
    histogram = Counter(data)
    #  Столбчатая диаграмма, показывающая фактические биноминальные выборки
    plt.bar(
        [x - 0.4 for x in histogram.keys()],
        [v / num_points for v in histogram.values()],
        0.8, color='0.75'
    )
    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    #  Линейный график, показывающий нормальное приближение
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma) for i in xs]

    plt.plot(xs, ys)
    plt.title("Биноминальное распределение и его нормальное приближение")
    plt.show()


def plot_normal_pdfs(plt=plt):
    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0, sigma=1')
    plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
    plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
    plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
    plt.legend()
    plt.show()


def plot_normal_cdfs(plt=plt):
    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], '-', label='mu=0, sigma=1')
    plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
    plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
    plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
    plt.legend(loc=4)
    plt.show()

# if __name__ == "__main__":
#     pass
#     #  проверка парадокса мальчика и девочки
#     both_girls = 0
#     older_girl = 0
#     either_girl = 0

#     random.seed(0)

#     for _ in range(10000):
#         younger = random_kid()
#         older = random_kid()
#         if older == GIRL:   # старшая?
#             older_girl += 1

#         if older == GIRL and younger == GIRL:   # обе?
#             both_girls += 1

#         if older == GIRL or younger == GIRL:    # любая из двух?
#             either_girl += 1

#     print("P(обе | старшая):", both_girls / older_girl)
#     print("P(обе | любая):", both_girls / either_girl)
