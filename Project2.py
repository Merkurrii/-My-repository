# Написать программу, которая на вход принимает положительное число, а на выходе
# считает сумму составляющих его цифр.

number = int(input("Введите положительное число: "))
if number <= 0:
    print("Ошибка: Введите положительное число")
else:
    number_str = str(number)
sum_of_digits = 0
for digit in number_str:
    sum_of_digits += int(digit)
    print(f"Сумма цифр в числе {number} равна {sum_of_digits}")