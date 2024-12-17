# Data types and ```print```

Display some text in console

```python
print('Hello world')
print("Hello world")
```

Result:

```commandline
Hello world
Hello world
```

Every string value must be included in quotes. '' or ""

## Escape sequence

```python
print('Hello \' \"world')
print('Hello \' \" \\ world')

print('Hello\nworld\n\n\n\n\nasd;lka')
print('Hello\tworld')
print('Hello    world')
print('Hello\bworld')
print('Hello\rworld')
```

- \n - new line
- \t - tab
- \b - backspace character
- \r - return carriage

```python
print('Hello')
print('World')

print('Hello\nWorld')
```

## Data types

In python exists next data types:

- int (integer) - numeric value (```4```)
- float - floating number (```3.4```)
- str (string) - text value (```"Hello world"```)

```python
print('2' + '2')  # string (str)
print(2 + 2)  # integer (int)
```

## Math operations

### Operators

- ```-```
- ```+```
- ```*```
- ```/```
- ```**```
- ```//```
- ```%```

Operators can be Unary, Binary or Ternary (Depends on amount of operands)

```Operand``` - is a value that used with operator

```python
print(2 + 2)
print(2 * 2)
print(2 / 2)
print(2 - 2)
print(2 ** 2)
print(2 // 2)
print(-2)

print(2 + 2 * 2)
print((2 + 2) * 2)
```

Parentheses ```()``` - use for order of operations, or order of evaluation

```python
print(15 % 10)  # 15 - 10 = 5
print(30 % 15)
print(45 % 30)
print(634134351 % 2)  # 0 1
print(10 % 15)
```

## Hotkeys

- ```Ctrl + Alt + L``` - Format Code
- ```Ctrl + D``` - Copy and Paste
- ```Ctrl + X``` - Cut
- ```Shift + F10``` - Run code
- ```Ctrl + Shift + Arrows(Up/Down)``` - Move line

## Block string

```python
print('''
Hello
world
''')
```

## Priority of operators

1. ```+```, ```-``` Unary
2. ```**```
3. ```*```, ```/```, ```%```
4. ```+```, ```-``` Binary

```python
print(0o123)  #
print(0xff)  #
print(0.2)  #
print(.2)  #
print(2.5)  #
print(-0.4)  #
print(0.00000000000000000001)  #
print(1e15)  #
print(1000000000000000)  #
print(1_000_000_000_000_000)  #
```

## Colors

```python
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"
```