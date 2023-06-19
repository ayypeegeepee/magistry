import numpy as np
from scipy.stats import weibull_min
from scipy.optimize import minimize


def generate_failure_times(n_samples, shape, scale):
    failure_times = weibull_min.rvs(shape, scale=scale, size=n_samples)
    return failure_times


def estimate_parameters(failure_times):
    # Метод максимального правдоподобия для оценки параметров формы и масштаба
    shape, loc, scale = weibull_min.fit(failure_times, floc=0)
    return shape, scale


# Генерация выборки времен наработки на отказ
n_samples = 1000  # Количество выборок
shape_true = 2  # Истинное значение параметра формы
scale_true = 10  # Истинное значение параметра масштаба

failure_times = generate_failure_times(n_samples, shape_true, scale_true)

# Оценка параметров распределения
shape_estimate, scale_estimate = estimate_parameters(failure_times)

# Вывод результатов
print("Истинные значения параметров:")
print("Параметр формы:", shape_true)
print("Параметр масштаба:", scale_true)
print()
print("Оценки параметров по выборке:")
print("Параметр формы:", shape_estimate)
print("Параметр масштаба:", scale_estimate)
