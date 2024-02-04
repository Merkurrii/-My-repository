#Написать программу, которая получает на вход в консоли месяц, а на выходе выдает количество дней в нем.

month = input("Введите месяц (например, Январь, Февраль и т. д.): ")
days_in_month = {
    "Январь": 31,
    "Февраль": 28, 
    "Март": 31,
    "Апрель": 30,
    "Май": 31,
    "Июнь": 30,
    "Июль": 31,
    "Август": 31,
    "Сентябрь": 30,
    "Октябрь": 31,
    "Ноябрь": 30,
    "Декабрь": 31
}
if month in days_in_month:
    print(f"В месяце {month} {days_in_month[month]} дней")
else:
    print("Такого месяца нет. Пожалуйста, введите корректное название месяца.")