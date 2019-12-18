from data_science.vectors import vector_subtract, scalar_multiply
import random


def sum_of_squares(v):
    """Вычисляет сумму квадратов вектора v"""
    return sum(v_i ** 2 for v_i in v)


def difference_quotient(f, x, h):
    """Отношение приращений"""
    return (f(x + h) - f(x)) / h


def partial_difference_quotient(f, v, i, h):
    """
    Частное отношение приращений
    Вычислить i-е частное отношение приращений функции f в векторе v
    """
    # прибавить h только к i-му элементу v
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h


def estimate_gradient(f, v, h=0.00001):
    """Оценить градиент"""
    return [partial_difference_quotient(f, v, i, h) for i, _ in enumerate(v)]


def step(v, direction, step_size):
    """
    Сделать шаг градиента
    Двигаться с шаговым размером step_size в направлении от v
    """
    return [v_i + step_size * direction_i for v_i, direction_i in zip(v, direction)]


def sum_of_squares_gradient(v):
    """Градиент суммы квадратов"""
    return [2 * v_i for v_i in v]


def safe(f):
    """
    Безопасная версия
    Вернуть новую функцию, одинаковую с f, за исключением того,
    что она возвращает бесконечность всякий раз когда f выдает ошибку
    """
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print(e)
            return float('inf')

    return safe_f


def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    """
    Пакетная минимизация
    Использует градиентный спуск для нахождения вектора theta, который
    минимизирует целевую функцию target_fn
    """
    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]
    theta = theta_0  # установить тета в начальное значение
    target_fn = safe(target_fn)
    value = target_fn(theta)
    while True:
        gradient = gradient_fn(theta)
        next_thetas = [step(theta, gradient, -step_size) for step_size in step_sizes]

        # выбрать то, которое минимизирует функцию ошибок
        next_theta = min(next_thetas, key=target_fn)
        next_value = target_fn(next_theta)

        # остановиться если функция не сходится (стремится к пределу)
        if abs(value - next_value) < tolerance:
            return theta
        else:
            theta, value = next_theta, next_value


def negatate(f):
    """Вернуть функцию, которая для любого входящего x возвращает -f(x)"""
    return lambda *args, **kwargs: -f(*args, **kwargs)


def negatate_all(f):
    """Тоже самое, когда f возвращает список чисел"""
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]


def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    """Пакетная максимизация путём минимизации отрицания"""
    return minimize_batch(negatate(target_fn), negatate_all(gradient_fn), theta_0, tolerance)


def in_random_order(data):
    """Генератор, возвращающий элементы данных в случайном порядке"""
    indexes = [i for i, _ in enumerate(data)]
    random.shuffle(indexes)
    for i in indexes:
        yield data[i]


def minimize_stohastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    """Стохастическая минимизация"""
    data = zip(x, y)
    theta = theta_0  # первоначальная гипотеза
    alpha = alpha_0  # первоначальный размер шага
    min_theta, min_value = None, float('inf')
    iterations_with_no_enviroment = 0

    # остановиться если достигли 100 итераций без улучшений
    while iterations_with_no_enviroment < 100:
        value = sum(target_fn(x_i, y_i, theta) for x_i, y_i in data)
        if value < min_value:
            # Если найден новый минимум, то запомнить его
            # поэтому пытаемся сжать размер шага
            alpha *= 0.9

            # И делаем шаг градиента для каждой из этих точек данных
            for x_i, y_i in in_random_order(data):
                gradient_i = gradient_fn(x_i, y_i, theta)
                theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))

    return min_theta


def maximize_stohastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    """Стохастическая максимизация"""
    return minimize_stohastic(
        negatate(target_fn),
        negatate_all(gradient_fn),
        x, y, theta_0, alpha_0
    )
