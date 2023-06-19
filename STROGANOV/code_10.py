import numpy as np
import matplotlib.pyplot as plt

def generate_system_trajectories(n_trajectories, time_horizon, failure_rate, repair_rate):
    system_states = np.zeros((n_trajectories, time_horizon))  # Матрица для хранения состояний системы

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


def plot_system_availability(system_states):
    availability = np.mean(system_states, axis=0)  # Вычисление средней работоспособности системы
    time = np.arange(system_states.shape[1])  # Временная шкала

    plt.plot(time, availability)
    plt.xlabel('Время')
    plt.ylabel('Работоспособность')
    plt.title('График работоспособности системы')
    plt.grid(True)
    plt.show()


def plot_system_downtime(system_states):
    downtime = np.sum(system_states == 0, axis=0)  # Вычисление времени простоя системы
    time = np.arange(system_states.shape[1])  # Временная шкала

    plt.plot(time, downtime)
    plt.xlabel('Время')
    plt.ylabel('Простой')
    plt.title('График простоя системы')
    plt.grid(True)
    plt.show()


# Параметры системы
n_trajectories = 100  # Количество выборочных траекторий
time_horizon = 1000  # Горизонт времени
failure_rate = 0.02  # Интенсивность отказов
repair_rate = 0.05  # Интенсивность восстановления

# Генерация выборочных траекторий системы
system_states = generate_system_trajectories(n_trajectories, time_horizon, failure_rate, repair_rate)

# Построение графиков работоспособности и простоя системы
plot_system_availability(system_states)
plot_system_downtime(system_states)
