# text = input('Enter: ')
#
# print(text[0])
# print('Hello'[1])
#


# number = input('Enter: ')
#
# tens = int(number[0])
# digit = int(number[1])
#
# print(tens)
# print(digit)
#
# print(tens + digit)

# text = input('Enter: ')
#
# print(text[len(text) - 1])
# print(text[-1])

# print(10 % 3)  # 10 - 9 = 1
# print(15 % 3)  # 0
# print(45 % 20)  # 5

number = int(input('Enter: '))

hundreds = number // 100 % 10  # 674 // 100 = 6
tens = number // 10 % 10  # 674 // 10 = 67
digit = number % 10  # 674 % 10 = 4

print(hundreds)
print(tens)
print(digit)

print(hundreds + tens + digit)
