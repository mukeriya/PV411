# print(10 > 5)  # True
# print(10 < 5)  # False
# print(10 > 10)  # False
# print(10 >= 10)  # True
# print(10 <= 10)  # True
# print(10 == 10)  # True
# print(10 == 15)  # False
# print(10 != 15)  # True


# user_age = int(input('Enter your age: '))
#
# print(user_age >= 18)

A = True
B = True

print(A and B)
print(A or B)

A = True
B = False

print(A and B)
print(A or B)

A = False
B = True

print(A and B)
print(A or B)

A = False
B = False

print(A and B)
print(A or B)

A = True

print(not A)

A = False

print(not A)

time = 7
has_ticket = False
has_money = True
has_luggage = False

print(has_money or has_ticket and not has_luggage and time < 18)
print((has_money or has_ticket) and not has_luggage and time < 18)

# not
# and
# or

# number = int(input('Enter a number: '))
#
# print(number % 2 == 0)


age = int(input('Enter your age: '))

print(18 <= age < 55)  # age >= 18 and age < 55
