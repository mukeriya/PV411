# Conditional statements

```python
x = 10
y = 5

print(x > y)  # True
print(x < y)  # False
print(x >= y)  # True
print(x <= y)  # False
print(x == y)  # False
print(x != y)  # True
```

```python
print('a' > 'b')  # False
print(ord('a'))  # 97
print(ord('A'))  # 65
print(ord('b'))  # 98
print(chr(65))  # A
```

## Cast type to bool

Any none empty value is a ```True```
Any empty value (like a empty string ```""```, ```0```, ```None```, ```0.0```) - is a ```False```

```python
print(bool(''))  # False
print(bool(' '))  # True
print(bool(1))  # True
print(bool(0))  # False
print(bool(654))  # True
print(bool(-1))  # True
print(bool(None))  # False
print(bool(0.1))  # True
print(bool(0.0))  # False
```

## ```and```, ```or```, ```not```

```python
A = True
B = True

print(A and B)  # True and True = True
print(A or B)  # True or True = True

A = True
B = False

print(A and B)  # True and False = False
print(A or B)  # True or False = True

A = False
B = True

print(A and B)  # False and True = False
print(A or B)  # False or True = True

A = False
B = False

print(A and B)  # False and False = False
print(A or B)  # False or False = False

A = True

print(not A)  # not True = False

A = False

print(not A)  # not False = True
```

---

## Examples

```python
age = 20

if age >= 18:
    print('Hello')

print('End')
```

![img.png](img%2Fimg.png)

---

```python
age = 15

if age >= 18:
    print('Hello')
else:
    print('Access denied')

print('End')
```

![img_2.png](img%2Fimg_2.png)

---

```python
import getpass

username = input('Enter username: ')
password = getpass.getpass(prompt='Enter password: ')

if username != 'admin' or password != 'admin':
    print('Access denied')
    exit()

print('Admin panel')
```

---

```python
number = int(input('Enter a number: '))

if number % 5 == 0:
    print('Number is divisible by 5')
else:
    print('Number is not divisible by 5')
```

![img_3.png](img%2Fimg_3.png)

## Menu example

```python
print('1. Sum')
print('2. Difference')
print('3. Prod')

user_choice = input('Select: ')

if user_choice == '1':
    print('First')
elif user_choice == '2':
    print('Second')
elif user_choice == '3':
    print('Third')
elif user_choice == '4':
    print('Fourth')
else:
    print('Incorrect value')
```

## Range check improvement

### Bad solution

```python
age = int(input('Enter age: '))

if 0 <= age and age < 12:
    print('Child')
elif 12 <= age and age < 18:
    print('Teenager')
elif 18 <= age and age < 50:
    print('Adult')
elif 50 <= age and age < 150:
    print('Old')
else:
    print('Incorrect age')
```

Issues:

- Duplicate checks
- Using ```age and age``` almost range check ```< age <```

### Good solution

```python
age = int(input('Enter age: '))

if age < 0 or age > 150:
    print('Incorrect age')
elif age < 12:
    print('Child')
elif age < 18:
    print('Teenager')
elif age < 50:
    print('Adult')
elif age < 150:
    print('Old')
```

## Multiple checks (Nested checks)

```python
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
```

Issues:

- Nested ```if``` checks (less is better and more readable)
- No readability

### Better
```python
is_admin = True  # Чи користувач адмін
has_wifi = True  # Чи є інтернет з'єднання
has_logged = True  # Чи користувач увійшов в аккаунт

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
```
