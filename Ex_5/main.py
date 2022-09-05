# Расстояние между 2 точками
import math

x_1 = int(input("Введите X1 "))
y_1 = int(input("Введите Y1 "))
x_2 = int(input("Введите X2 "))
y_2 = int(input("Введите Y2 "))
dist = math.sqrt(((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2))
print(round(dist, 3))
