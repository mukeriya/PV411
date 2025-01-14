# x = 1
#
# while x < 5:
#     print(x)
#     x += 1

# x1 = int(input('Enter x1: '))
# x2 = int(input('Enter x2: '))
#
# x = x1 + 1
# total_sum = 0
#
# while x < x2:
#     total_sum += x
#     x += 1
#
# print(total_sum)
# 2 3 4 5

# lower_bound = int(input('Enter x1: '))
# upper_bound = int(input('Enter x2: '))
#
# i = lower_bound + 1
# total_sum = 0
#
# while i < upper_bound:
#     total_sum += i
#     i += 1
#
# print(total_sum)

# while True:
# while 1:
# while True:
#     x = int(input('Enter x: '))
#     y = int(input('Enter y: '))
#
#     print('Result:', x + y)
#
# i = 1
#
# while True:
#     i *= 54
#     print(i)

# import time
#
# x = 0
#
# while True:
#     print(x)
#     x += 1
#     time.sleep(1)
# import random
#
# print(random.randint(1, 10))
# from random import randint

# print(randint(1, 10))
# print(locals())

# x = 0
# i = 0
#
# while i < 2:
#     j = 0
#     while j < 2:
#         x += 1
#         j += 1
#
#     i += 1
#
# print(x)

# i = 1
#
# while i <= 10:
#     j = 1
#     while j <= 10:
#         print(i, '*', j, '=', i * j, end='\t')
#         j += 1
#     print()
#     i += 1


# lower_bound = 33
# upper_bound = 13

# if upper_bound < lower_bound:
#     temp = lower_bound
#     lower_bound = upper_bound
#     upper_bound = temp

# if upper_bound < lower_bound:
#     upper_bound = upper_bound + lower_bound
#     lower_bound = upper_bound - lower_bound
#     upper_bound = upper_bound - lower_bound

# x, y = 1, 2

# if upper_bound < lower_bound:
#     lower_bound, upper_bound = upper_bound, lower_bound

# print(lower_bound)
# print(upper_bound)


# i = 1
#
# while i < 10:
#     print(i)
#     i += 1
#     break
#
# print('End')


# while True:
#
#     print('1. Sum')
#     print('2. Diff')
#     print('9. Exit')
#
#     choice = int(input('Select: '))
#
#     if choice == 9:
#         print('Goodbye')
#         break
#
#     if choice == 1:
#         ...
#     elif choice == 2:
#         ...

# i = 1
#
# while True:
#
#     if i > 3:
#         break
#
#     print(i)
#     i += 1


# i = 0
#
# while i < 10:
#
#     if i % 2 == 0:
#         i += 1
#         continue
#
#     print(i)
#     i += 1

# i = 1
#
# while i < 5:
#     print(i)
#     if i == 4:
#         break
#     i += 1
# else:
#     print('End')


# i = 1
#
# while i < 10:
#     i += 1
#     if i % 2 != 0:
#         continue
#
#     if i == 5:
#         break
#
#     print(i)


# lower_bound = int(input("Введите первое число: "))
# upper_bound = int(input("Введите второе число: "))
#
# i = lower_bound
# while i <= upper_bound:
#     if i % 2 != 0:
#         print(i)
#     i += 1

lower_bound = 1
upper_bound = 10

print('=' * 50)

for i in range(upper_bound + 1):  # from 0
    print(i)

print('=' * 50)

for i in range(lower_bound, upper_bound + 1):
    print(i)

print('=' * 50)

for i in range(lower_bound, upper_bound + 1, 2):
    print(i)

print('=' * 50)

for i in range(upper_bound, lower_bound - 1, -1):
    print(i)

print('=' * 50)

for row in range(1, 11):
    for col in range(1, 11):
        print(row * col, end='\t')
    print()

for i in range(1, 10):
    if i % 2 != 0:
        continue

    print(i)

for i in range(1, 10):
    if i == 8:
        break

    print(i)

KM_TO_MILES_COEF = 0.000621371

number = 2
for _ in range(3):
    number *= number

print(number)
