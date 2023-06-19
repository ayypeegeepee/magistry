import numpy as np
from scipy.stats import uniform, norm, lognorm, expon, gamma, rayleigh, weibull_min

# Равномерное распределение
a, b = 0, 10  # Интервал [a, b]
uniform_params = uniform.fit(np.random.uniform(a, b, 1000))
print("Параметры равномерного распределения:", uniform_params)

# Нормальное распределение
mu, sigma = 0, 1  # Среднее и стандартное отклонение
normal_params = norm.fit(np.random.normal(mu, sigma, 1000))
print("Параметры нормального распределения:", normal_params)

# Логнормальное распределение
mu_ln, sigma_ln = 0, 1  # Параметры нормального распределения
lognormal_params = lognorm.fit(np.random.lognormal(mu_ln, sigma_ln, 1000))
print("Параметры логнормального распределения:", lognormal_params)

# Экспоненциальное распределение
lambda_exp = 0.5  # Параметр экспоненциального распределения
exponential_params = expon.fit(np.random.exponential(1/lambda_exp, 1000))
print("Параметры экспоненциального распределения:", exponential_params)

# Гамма-распределение
k_gamma, theta_gamma = 2, 1  # Параметры гамма-распределения
gamma_params = gamma.fit(np.random.gamma(k_gamma, theta_gamma, 1000))
print("Параметры гамма-распределения:", gamma_params)

# Рэлеевское распределение
sigma_rayleigh = 1  # Параметр рэлеевского распределения
rayleigh_params = rayleigh.fit(np.random.rayleigh(sigma_rayleigh, 1000))
print("Параметры рэлеевского распределения:", rayleigh_params)

# Вейбулловское распределение
k_weibull, lambda_weibull = 1, 1  # Параметры вейбулловского распределения
weibull_params = weibull_min.fit(np.random.weibull(k_weibull, 1000))
print("Параметры вейбулловского распределения:", weibull_params)
