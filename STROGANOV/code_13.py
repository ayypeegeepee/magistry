import numpy as np
from scipy.stats import norm
from scipy.stats import jarque_bera


def generate_sample(n_samples, mean, std):
    sample = np.random.normal(mean, std, n_samples)
    return sample


def test_normality(sample):
    _, p_value = jarque_bera(sample)
    if p_value > 0.05:
        result = "Выборка является нормальной"
    else:
        result = "Выборка не является нормальной"
    return result


# Генерация выборки
n_samples = 1000  # Количество элементов в выборке
mean_true = 0  # Истинное значение среднего
std_true = 1  # Истинное значение стандартного отклонения

sample = generate_sample(n_samples, mean_true, std_true)

# Проверка нормальности выборки
for i in range(100):
    result = test_normality(sample)
    print("Истинное значение среднего:", mean_true)
    print("Истинное значение стандартного отклонения:", std_true)
    print()
    print(f"{i})", "Результат проверки нормальности выборки:", result)

# Вывод результатов

