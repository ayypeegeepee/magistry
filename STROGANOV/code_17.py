import numpy as np
from scipy.stats import kstest

# Генерируем выборку из выбранного распределения (например, нормального распределения)
sample = np.random.normal(loc=0, scale=1, size=1000)

# Выполняем расчет критерия Колмогорова-Смирнова
D, p_value = kstest(sample, 'norm')

# Выводим результаты
print("Статистика D: ", D)
print("p-значение: ", p_value)
