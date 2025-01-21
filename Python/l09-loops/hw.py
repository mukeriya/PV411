# Завдання 1
# Користувач вводить із клавіатури два числа.
# Потрібно порахувати окремо суму парних чисел,
# непарних чисел і чисел, кратних 9 у зазначеному
# діапазоні, а також середньоарифметичне кожної групи.
#
# sum_of_even_numbers = 0
# count_of_even_numbers = 0
#
# sum_of_odd_numbers = 0
# count_of_odd_numbers = 0
#
# sum_of_numbers_divisible_by_9 = 0
# count_of_numbers_divisible_by_9 = 0
#
# start = int(input('Enter start of range: '))
# end = int(input('Enter end of range: '))
import random
import time

# for
# while

# 1
# 10

# for i in range(start, end + 1):  # 1 2 3 4 5 6 7 8 9 10
#     if i % 2 == 0:
#         sum_of_even_numbers += i
#         count_of_even_numbers += 1
#     else:
#         sum_of_odd_numbers += i
#         count_of_odd_numbers += 1
#
#     if i % 9 == 0:
#         sum_of_numbers_divisible_by_9 += i
#         count_of_numbers_divisible_by_9 += 1
#
# print("Sum of even:", sum_of_even_numbers, 'Avg:', sum_of_even_numbers / count_of_even_numbers)
# print("Sum of odd:", sum_of_odd_numbers, 'Avg:', sum_of_odd_numbers / count_of_odd_numbers)
# print("Sum of divisible by 9:", sum_of_numbers_divisible_by_9, 'Avg:',
#       sum_of_numbers_divisible_by_9 / count_of_numbers_divisible_by_9)

# Завдання 3
# Користувач вводить із клавіатури числа. Якщо число більше нуля,
# потрібно вивести напис "Number is positive", якщо менше нуля —
# "Number is negative", якщо дорівнює нулю — "Number is equal to
# zero". Коли користувач вводить число 7, програма припиняє свою
# роботу і виводить на екран напис "Good bye!".

# while True:
#     number = int(input('Enter a number: '))
#
#     if number == 7:
#         print('Goodbye')
#         break
#
#     if number > 0:
#         print('Number is positive')
#     elif number < 0:
#         print('Number is negative')
#     else:
#         print('Number is zero')


# COUNT_OF_CLOTHES = 10
#
# for i in range(COUNT_OF_CLOTHES):
#     if random.randint(0, 1) != 1:  # Чи підходить нам ця річ?
#         print('Викидуємо річ номер:', i)
#     elif random.randint(0, 1) != 1:  # Чи подобається нам ця річ?
#         print('Не подобається та викидуємо річ номер:', i)
#     else:
#         print('Відкладаємо річ номер:', i)

# energy = 100
#
# while True:
#
#     if energy < 0:
#         print('We tired')
#         break
#
#     time.sleep(1)
#
#     if random.randint(1, 4) == 1:
#         energy += random.randint(1, 10)
#         print('We found some information about homework and we increase energy. Energy:', energy)
#
#     if random.randint(1, 10) == 1:
#         print('Yes, we complete homework and left energy is ' + str(energy))
#         break
#     else:
#         energy -= 5
#         print('Again fail. Left energy:', energy)

# Сума усіх чисел в діпазоні від 1 до n, які кратні 3 або 5

# 1. Прийняти число n +
# 2. Сформувати послідовність від 1 до n +
# 3. Для кожного числа, яке знаходиться в діапазоні від 1 до n потрібно зробити наступне
#   3.1. Перевірити чи число кратне 3 або 5. Якщо це істина додати в суму. +

end = int(input('Enter n: '))

total_sum = 0

for i in range(end):
    if i % 3 == 0 or i % 5 == 0:
        total_sum += i

print(total_sum)

# 3 6 9 - 18
# 5 - 23
