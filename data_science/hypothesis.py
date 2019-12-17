from data_science.probability import normal_cdf, inverse_normal_cdf
import math
import random


def normal_approximation_to_binominal(n, p):
    """
    Аппроксимация биноминальной случайной величины нормальным распределением;
    Находит mu и sigma, которые соответствуют binominal(n, p)
    """
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma


# Вероятность, что значение нормальной случайной величины
# лежит ниже порогового значения
normal_probability_below = normal_cdf


def normal_probability_above(lo, mu=0, sigma=1):
    """Оно выше порогового значения если оно не ниже его"""
    return 1 - normal_cdf(lo, mu, sigma)


def normal_probability_between(lo, hi, mu=0, sigma=1):
    """Оно лежит между, если оно между, если оно меньше hi, но не ниже lo"""
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)


def normal_probability_outside(lo, hi, mu=0, sigma=1):
    """Оно лежит за пределами, если оно не внутри"""
    return 1 - normal_probability_between(lo, hi, mu, sigma)


def normal_upper_bound(probability, mu=0, sigma=1):
    """
    Верхняя граница нормальной величины
    Возвращает z, для которого P(Z <= z) = probability
    """
    return inverse_normal_cdf(probability, mu, sigma)


def normal_lower_bound(probability, mu=0, sigma=1):
    """
    Нижняя граница нормально величины
    Возвращает z, для которого P(Z >= z) = probability
    """
    return inverse_normal_cdf(1 - probability, mu, sigma)


def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """
    Двусторонние границы нормальной величны
    Возвращает симметричные (вокруг своего значения) границы,
    в пределах которой находится указанная вероятность
    """
    tail_probability = (1 - probability) / 2

    # Верхняя граница должна иметь значение хвостовой вероятности
    # tail_probability ниже ее
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    # Нижняя граница должна иметь значение хвостовой вероятности
    # tail_probability ниже её
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)
    return lower_bound, upper_bound


def two_sided_p_value(x, mu=0, sigma=1):
    """Двустороннее p - значение"""
    if x >= mu:
        # Если х больше среднего значения, то значения в хвосте больше х
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # Если х меньше среднего значения, то значения в хвосте меньше х
        return 2 * normal_probability_below(x, mu, sigma)


def run_experiment():
    """
    Провести эксперимент: бросить уравновешенную монету 1000 раз
    True - орлы, False - решки
    """
    return [random.random() < 0.5 for _ in range(1000)]


def reject_fairness(experiment):
    """
    Отвергнуть уравновешенность монеты
    Используя 5% уровни значимости
    """
    num_heads = len([flip for flip in experiment if flip])  # число орлов
    return num_heads < 469 or num_heads > 531


def estimated_parameters(N, n):
    p = n / N
    sigma = math.sqrt(p * (1 - p) / N)
    return p, sigma


def a_b_test_statistic(N_A, n_A, N_B, n_B):
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)


def B(alpha, beta):
    """
    Нормализация;
    Нормализующая константа, блягодаря которой сумма вероятностей равна 1
    """
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)


def beta_pdf(x, alpha, beta):
    """
    ДФР для бета распределений случайной величины
    """
    if x < 0 or x > 1:  # За пределами [0, 1] нет веса
        return 0
    return x ** (alpha - 1) * (1 - x) ** (beta - 1) / B(alpha, beta)
