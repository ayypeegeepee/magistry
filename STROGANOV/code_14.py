import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import moment


def generate_sample(n_samples, mean, std):
    sample = np.random.normal(mean, std, n_samples)
    return sample


def calculate_statistics(sample):
    mean = np.mean(sample)
    variance = np.var(sample)
    std_dev = np.std(sample)
    skewness = moment(sample, moment=3)
    kurtosis = moment(sample, moment=4)
    return mean, variance, std_dev, skewness, kurtosis


# Генерация выборки
n_samples = 1000  # Количество элементов в выборке
mean_true = 0  # Истинное значение среднего
std_true = 1  # Истинное значение стандартного отклонения

sample = generate_sample(n_samples, mean_true, std_true)

# Расчет основных характеристик выборки
mean, variance, std_dev, skewness, kurtosis = calculate_statistics(sample)

# Построение гистограммы
plt.hist(sample, bins='auto')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.title('Гистограмма выборки')
plt.show()

# Вывод результатов
print("Основные характеристики выборки:")
print("Среднее:", mean)
print("Дисперсия:", variance)
print("Стандартное отклонение:", std_dev)
print("Асимметрия:", skewness)
print("Эксцесс:", kurtosis)
