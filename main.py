from pulp import *
import numpy as np
from scipy.integrate import quad

#Завдання 1
model = LpProblem("Максимізація_виробництва_напоїв", LpMaximize)
Lemonade = LpVariable("Лимонад", 0)
Juice = LpVariable("Фруктовий сік", 0)

model += Lemonade + Juice

model += 2*Lemonade + Juice <= 100, "Обмеження води"
model += Lemonade <= 50, "Обмеження цукру"
model += Lemonade <= 30, "Обмеження лимонного соку"
model += 2*Juice <= 40, "Обмеження фруктового пюре"

model.solve()

print("Задача1:")
print("Кількість Лимонаду:", Lemonade.varValue)
print("Кількість Фруктового соку:", Juice.varValue)
print("Загальна кількість вироблених продуктів:", value(model.objective))

#Завдання 2

def f(x):
    return x ** 2

a = 0
b = 2

analytic_result, _ = quad(f, a, b)

n_samples = 100000
x_samples = np.random.uniform(a, b, n_samples)
y_samples = f(x_samples)

monte_carlo_result = (b - a) * np.mean(y_samples)

analytic_result, monte_carlo_result

print(f'\n Задача 2: \n Значення інтегралу обчислене: \n Аналітичним методом: {analytic_result} \n Методом Монте-Карло: {monte_carlo_result}')