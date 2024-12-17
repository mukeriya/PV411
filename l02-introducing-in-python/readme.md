# Variables and ```print```

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