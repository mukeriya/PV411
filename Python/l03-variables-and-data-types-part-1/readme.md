# Variables and data types

## [Naming conventions](https://en.wikipedia.org/wiki/Naming_convention_(programming))

- ```snake_case``` - my_name, upload_file
- ```kebab-case``` - first-name, upload-file
- ```SNAKE_UPPER_CASE``` - FIRST_NAME, UPLOAD_FILE
- ```PascalCase``` - FirstName, UploadFile
- ```camelCase``` - firstName, uploadFile

## Concat

Concatenation - operation that combine two or more strings

```python
first_name = 'Oleksandr'

last_name = 'Mukeria'

print(first_name + ' ' + last_name)
```

```commandline
Oleksandr Mukeria
```

---

## Data type convertion

```python
x = float(input('Enter x: '))
y = float(input('Enter y: '))

print(x + y)
```

```commandline
Enter x: 5
Enter y: 5
10
```

### ```int```

```python
print(int('5'))  # 5
print(int(True))  # 1
print(int(False))  # 0
print(int(2.54))  # 2
print(int('2.54'))  # Error!
```

### ```str```

```python
print(str(5))  # 5
print(str(True))  # True
print(str(False))  # False
print(str(2.5))  # 2.5
```

### ```float```

```python
print(float(5))  # 5.0
print(float('5.2'))  # 5.2
print(float(True))  # 1.0
print(float(False))  # 0.0
print(float('2,5'))  # Error!
```

### ```bool```

```python
print(bool(5))  # True
print(bool(1))  # True
print(bool(0.1))  # True
print(bool(-5))  # True
print(bool(0))  # False
print(bool(0.0))  # False
print(bool(''))  # False
print(bool(' '))  # True
print(bool('abc'))  # True
```

## Compound assignment operators

Combined operators - are a shorter way to apply an arithmetic or bitwise operation and to assign the value of the
operation to the variable on the left-hand side

### ```+=```

```python
x = 5

x = x + 1

print(x)  # 6
```

or

```python
x = 5

x += 1

print(x)  # 6
```

---

### ```-=```

```python
x = 5

x = x - 1

print(x)  # 4
```

or

```python
x = 5

x -= 1

print(x)  # 4
```

---

### ```*=```

```python
x = 5

x = x * 3

print(x)  # 15
```

or

```python
x = 5

x *= 3

print(x)  # 15
```

---

### ```/=```

```python
x = 5

x = x / 2

print(x)  # 2.5
```

or

```python
x = 5

x /= 2

print(x)  # 2.5
```

---

### ```**=```

```python
x = 5

x = x ** 2

print(x)  # 25
```

or

```python
x = 5

x **= 1

print(x)  # 25
```

---

### ```//=```

```python
x = 5

x = x // 2

print(x)  # 2
```

or

```python
x = 5

x //= 1

print(x)  # 2
```

---

### ```%=```

```python
x = 5

x = x % 2

print(x)  # 1
```

or

```python
x = 5

x %= 2

print(x)  # 1
```

---


## Examples

```python
name = input('Enter your name: ')

print('Welcome', name)
```

```commandline
Enter your name: Sasha
Welcome Sasha
```
---
```python
x = input('Enter x: ')
y = input('Enter y: ')

print(x + y)  # Concat
print(type(x))
print(type(y))
```
```commandline
Enter x: 5
Enter y: 5
55
<class 'str'>
<class 'str'>
```
---

```python
x = int(input('Enter x: '))
y = int(input('Enter y: '))

print(x + y)
print(type(x))
print(type(y))
```
```commandline
Enter x: 5
Enter y: 5
10
<class 'int'>
<class 'int'>
```

---

```python
pi = 3.14

r = float(input('Enter radius: '))

print(pi * r ** 2)
```

```commandline
Enter radius: 15
706.5
```