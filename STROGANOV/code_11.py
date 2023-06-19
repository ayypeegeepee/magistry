import numpy as np

def generate_system_trajectories(n_trajectories, time_horizon, failure_rate, repair_rate):
    system_states = np.zeros((n_trajectories, time_horizon), dtype=int)  # Матрица для хранения состояний системы

    for i in range(n_trajectories):
        time = 0
        while time < time_horizon:
            # Генерация времени до следующего отказа и времени восстановления
            time_to_failure = np.random.exponential(1/failure_rate)
            time_to_repair = np.random.exponential(1/repair_rate)

            # Если время до отказа меньше времени до восстановления, система переходит в состояние отказа
            if time_to_failure < time_to_repair:
                failure_duration = int(np.ceil(time_to_failure))  # Продолжительность отказа (округление вверх)
                system_states[i, time:time + failure_duration] = 0  # Система в состоянии отказа
                time += failure_duration
            else:  # Время до восстановления меньше времени до отказа
                repair_duration = int(np.ceil(time_to_repair))  # Продолжительность восстановления (округление вверх)
                system_states[i, time:time + repair_duration] = 1  # Система в состоянии работоспособности
                time += repair_duration

    return system_states


def calculate_reliability(system_states):
    reliability_single = np.mean(system_states)  # Средняя вероятность пребывания в работоспособном состоянии (по одной реализации)
    reliability_mean = np.mean(system_states, axis=0)  # Средняя вероятность пребывания в работоспособном состоянии (по множеству реализаций)

    return reliability_single, reliability_mean


# Параметры системы
n_trajectories = 1000  # Количество выборочных траекторий
time_horizon = 1000  # Горизонт времени
failure_rate = 0.02  # Интенсивность отказов
repair_rate = 0.05  # Интенсивность восстановления

# Генерация выборочных траекторий системы
system_states = generate_system_trajectories(n_trajectories, time_horizon, failure_rate, repair_rate)

# Оценка среднего
reliability_single, reliability_mean = calculate_reliability(system_states)

# Вывод результатов
print("Средняя вероятность пребывания в работоспособном состоянии (по одной реализации):", reliability_single)
print("Средняя вероятность пребывания в работоспособном состоянии (по множеству реализаций):", reliability_mean)

# Проверка близости средних
difference = np.abs(reliability_single - reliability_mean)
print("Разница между средними:", difference)
