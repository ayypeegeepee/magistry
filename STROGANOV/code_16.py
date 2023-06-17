import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Генерация выборки
sample = np.random.normal(loc=0, scale=1, size=1000)

# Оценка параметров распределения
mu_hat = np.mean(sample)
sigma_hat = np.std(sample)

# Визуализация гистограммы выборки
plt.hist(sample, bins='auto', density=True, alpha=0.7, label='Исследуемая выборка')

# Визуализация теоретической функции плотности для полученных оценок параметров
x = np.linspace(-4, 4, 100)
pdf = norm.pdf(x, loc=mu_hat, scale=sigma_hat)
plt.plot(x, pdf, 'r', label='Теоретическая плотность')

# Настройка графика
plt.xlabel('Значения выборки')
plt.ylabel('Вероятность')
plt.title('Гистограмма выборки и теоретическая функция плотности')
plt.legend()

# Отображение графика
plt.show()
