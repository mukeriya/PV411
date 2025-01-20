# i = 0
#
# while i < 10:
#     print(i)
#     i += 1
# import time
# from random import randint
#
# is_request_successful = False
# MAX_ATTEMPTS_COUNT = 5
#
# attempts = 0
#
# while not is_request_successful and attempts < MAX_ATTEMPTS_COUNT:
#     attempts += 1
#     time.sleep(1)
#
#     if randint(1, 5) == 1:
#         is_request_successful = True
#         print('Request success')
#     else:
#         print('Request failed')
#
# for i in range(10):  # 0 - 10
#     print(i)
#
# for i in range(1, 10):  # 1 - 10
#     print(i)
#
# for i in range(1, 10, 2):  # 1 - 10 with step
#     print(i)


# for i in range(10):
#     if i % 2 == 0:
#         continue
#
#     print(i)
#
# for i in range(10):
#     if i > 7 and i % 2 == 0:
#         break
#
#     print(i)


# while True:
#     print('1. ')
#     print('2. ')
#     print('3. ')
#     print('4. ')
#     print('9. Exit')
#
#     choose = int(input('Select: '))
#
#     if choose == 1:
#         print('First')
#     elif choose == 2:
#         print('Second')
#     elif choose == 3:
#         print('Third')
#     elif choose == 9:
#         break
#     else:
#         print('Invalid menu item')
#
# print('Goodbye')

#
# # First version
# number = int(input('Enter number: '))
#
# is_prime = True
#
# if number <= 1:
#     is_prime = False
# else:
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#             break
#     print('Count of iterations of v1', i)
#
# # Second version
# # number = int(input('Enter number: '))
#
# if number <= 1:
#     is_prime = False
# else:
#     for i in range(2, number // 2 + 1):
#         if number % i == 0:
#             is_prime = False
#             break
#     print('Count of iterations of v2', i)
#
# # Third version
#
#
# if number <= 1:
#     is_prime = False
# else:
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             is_prime = False
#             break
#     print('Count of iterations of v3', i)
#
# if is_prime:
#     print('Number is prime')
# else:
#     print('Number is not prime')

# 25 - 24, 13, 5


# number = None
#
# while True:
#     number = int(input('Enter number: '))
#
#     if number > 0:
#         break
#
#     print('Invalid value. Value must be greater than 0')
#
# print(number)


import time
from random import randint

start = time.time()

time.sleep(1)

end = time.time()

print(end - start)

print(randint(1, 10))
