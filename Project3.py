# Написать программу, переводящую температура с Цельсия на Фаренгейт и обратно.

celsius = float(input("Введите температуру в градусах Цельсия: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} градусов Цельсия = {fahrenheit} градусов Фаренгейта")
celsius_new = (fahrenheit - 32) * 5/9
print(f"{fahrenheit} градусов Фаренгейта = {celsius_new} градусов Цельсия")