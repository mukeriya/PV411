# print(bool(''))  # False
# print(bool(' '))  # True
# print(bool(1))  # True
# print(bool(0))  # False
# print(bool(654))  # True
# print(bool(-1))  # True
# print(bool(None))  # False
# print(bool(0.1))  # True
# print(bool(0.0))  # False
#
# print(not not 0.1)


# age = 20
#
# if age >= 18:
#     print('Hello')
#
# print('End')

# import getpass
#
# username = input('Enter username: ')
# password = getpass.getpass(prompt='Enter password: ')
#
# if username != 'admin' or password != 'admin':
#     print('Access denied')
#     exit()
#
# print('Admin panel')

# age = 15
#
# if age >= 18:
#     print('Hello')
# else:
#     print('Access denied')
#
# print('End')


# number = int(input('Enter a number: '))
#
# if number % 5 == 0:
#     print('Number is divisible by 5')
# else:
#     print('Number is not divisible by 5')


# print('1. Sum')
# print('2. Product')
# print('3. Difference')
#
# user_choice = input('Select: ')
#
# if user_choice == '1':
#     print('')
# if user_choice == '2':
#     print('')


# login = input('Enter login: ')
#
# if login == 'admin':
#     print('Admin panel')
# else:
#     print('User panel')
#
#
# print('1. Sum')
# print('2. Product')
# print('3. Difference')
#
# user_choice = input('Select: ')
#
# if user_choice == '1':
#     print('First')
# if user_choice == '2':
#     print('Second')
# number = int(input("Enter: "))
#
# if number % 2 == 0:
#     print(f"{number} - Even number")
# else:
#     print(f"{number} - Odd number")


# print('1. Sum')
# print('2. Difference')
# print('3. Prod')
#
# user_choice = input('Select: ')
#
# if user_choice == '1':
#     print('First')
#
# if user_choice == '2':
#     print('Second')
#
# if user_choice == '3':
#     print('Third')

# print('1. Sum')
# print('2. Difference')
# print('3. Prod')
#
# user_choice = input('Select: ')
#
# if user_choice == '1':
#     print('First')
# elif user_choice == '2':
#     print('Second')
# elif user_choice == '3':
#     print('Third')
# else:
#     print('Incorrect value')
#
# age = int(input('Enter age: '))
#
# if age < 0 or age > 150:
#     print('Incorrect age')
# elif age < 12:
#     print('Child')
# elif age < 18:
#     print('Teenager')
# elif age < 50:
#     print('Adult')
# elif age < 150:
#     print('Old')

# DRY - Dont repeat yourself
# YAGNI


is_admin = True  # Чи користувач адмін
has_wifi = True  # Чи є інтернет з'єднання
has_logged = True  # Чи користувач увійшов в аккаунт

if has_wifi:
    if has_logged:
        if is_admin:
            print('Admin Panel')
        else:
            print('Access Denied')
    else:
        print('You need to login')
else:
    print('No Connection!')

if not has_wifi:
    print('No connection!')
    exit()

if not has_logged:
    print('You need to login')
    exit()

if not is_admin:
    print('Access Denied')
    exit()

print('Admin panel')
