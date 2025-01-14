# elapsed_seconds = int(input("Enter the number of seconds that have passed since the beginning of the day: "))
#
# seconds_in_a_day = 24 * 60 * 60
#
# if 0 <= elapsed_seconds <= seconds_in_a_day:
#     remaining_seconds = seconds_in_a_day - elapsed_seconds
#
#     hours = remaining_seconds // 3600
#     minutes = (remaining_seconds % 3600) // 60
#     seconds = remaining_seconds % 60
#
#     print('1. In hours')
#     print('2. In minutes')
#     print('3. In seconds')
#
#     choice = input('Select: ')
#
#     if choice == '1':
#         pass
#     else:
#         pass
#
#     # Виведення результату
#     print(f"Lost by midnight: {hours} hours, {minutes} minutes, {seconds} secnds.")
# else:
#     print("Incorrect does not matter! Enter number of seconds from 0 to 86400.")
#
# import math
#
# diameter = float(input("Введите диаметр круга: "))
#
# radius = diameter / 2
# area = math.pi * (radius ** 2)
#
# print(f"Площадь круга с диаметром {diameter} равна {area:.2f}")
#
# price = float(input("цена приставки"))
# consoles_number = int(input("кол-во приставок"))
# discount = float(input("cкидка"))
#
# print('1. Total price')
# print('2. Price per 1 unit with discount')
#
# total_amount = price * consoles_number * (1 - discount / 100)
# one_console = price * (1 - discount / 100)
# print(f"общая сумма {total_amount}")
# print(f"цена одной приставки {one_console}")
#
# hours = int(input('Enter: '))
#
#
#
# if 0 <= hours < 6:
#     print("Good Night")
# elif 6 <= hours < 13:
#     print("Good Morning")
# elif 13 <= hours < 17:
#     print("Good Day")
# elif 17 <= hours < 24:
#     print("Good Evening")
# else:
#     print("ошибка! Введите число от 0 до 23.")

print('1. ')
print('2. ')
print('3. ')

choice = input('Select: ')

match choice:
    case '1':
        print('First')
    case '2':
        print('Second')
    case '3':
        print('Third')
    case _:
        print('Default')
