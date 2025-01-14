# Loops

Loops in Python are constructs that allow you to repeatedly execute a block of code as long as specified condition is
true or for a defined number of iterations. Python provides 2 main types of loops

## ```while```

Syntax:

```python
while condition:
    pass
    # Code to execute 
```

Example:

```python
x = 1

while x < 5:
    print(x)
    x += 1
```

Result:

```commandline
1
2
3
4
```

## Iteration

In programming, iterations refer to the repeated execution of a block of code, typically within a loop. Each repetition
is called an __iteration__. Iterations, are commonly used to process items in a sequence, perform repetitive tasks or
implement logic that requires repetition.

## Infinite loop

An infinite loop is a loop that continues to execute indefinitely because the loop`s termination condition is never met
or intentionally omitted. In programmin, this can happen either by design (for processes like server listening) or by
mistake (causing a bug).

Using ```while True:```

```python
while True:
    print('This will run forever.')
```

```python
while True:
    x = int(input('Enter x: '))
    y = int(input('Enter y: '))

    print('Result:', x + y)
```

Missing increment:

```python
i = 0
while i < 5:
    print('This is an infinite loop because i is not updated!')
```

## Nested loops

```python
x = 0
i = 0

while i < 2:  # For each iteration of the outer loop
    j = 0
    while j < 2:  # there are 2 iterations of inner loop
        x += 1
        j += 1

    i += 1

print(x)
```

Result:

```commandline
4
```

### Multiplication table

```i``` and ```j``` are traditionally used as loop counters due to their brevity and clarity. This practice originated
from mathematics and programming, where they were commonly used as variables for iteration.

```i``` for the first level
```j``` for the second level
```k``` for the third level
Example:

```python
i = 1

while i <= 10:
    j = 1
    while j <= 10:
        print(i, '*', j, '=', i * j, end='\t')
        j += 1
    print()
    i += 1
```

Alternatives:
While ```i``` and ```j``` are common, it is recommended to use descriptive names in real projects to enhance code
readability:

```python

row = 0
while row < 3:
    column = 0
    while column < 2:
        print('row =', row, 'column = ', column)
        column += 1
    row += 1
```

## Examples of ```while``` loop

### Calculate sum in range

```python
lower_bound = int(input('Enter start: '))
upper_bound = int(input('Enter end: '))

i = lower_bound + 1
total_sum = 0

while i < upper_bound:
    total_sum += i
    i += 1

print(total_sum)
```

Result

```commandline
Enter start: 1
Enter end: 6
14
```

## Swap 2 variables

```python
lower_bound = 33
upper_bound = 13

if upper_bound < lower_bound:
    temp = lower_bound
    lower_bound = upper_bound
    upper_bound = temp

print(lower_bound)  # 13
print(upper_bound)  # 33
```

```python
lower_bound = 33
upper_bound = 13

if upper_bound < lower_bound:
    upper_bound = upper_bound + lower_bound
    lower_bound = upper_bound - lower_bound
    upper_bound = upper_bound - lower_bound

print(lower_bound)  # 13
print(upper_bound)  # 33
```

```python
lower_bound = 33
upper_bound = 13

if upper_bound < lower_bound:
    lower_bound, upper_bound = upper_bound, lower_bound

print(lower_bound)  # 13
print(upper_bound)  # 33
```

## ```for```

```for``` loops, unlike ```while``` loops, iterate not based on a condition but for eah element in a list, set, tuple or
other collection of elements. In other words, for each iteration of the loop, one of the elements in collection is used.
For example, to check expiration date of food products in a store, person needs to sequentially take eah item from their
basket and ensure that the expiration date has not passed. Here, the basket of products serves as collection of
elements. The products are elements, and checking the expiration date of one product is an iteration of the loop.

Example:

```python
for i in range(1, 10):  # Last element not included!
    print(i)
```
Result:
```commandline
1
2
3
4
5
6
7
8
9
```

### Variants of using ```range``` function

- ```range(end)``` - sequence from 0 to ```end```
- ```range(start, end)``` - sequence from ```start``` to ```end```
- ```range(start, end, step)``` - sequence from ```start``` to ```end``` with step - ```step```

Examples:

```python
upper_bound = 5

for i in range(upper_bound + 1):  # adds 1 to include last element
    print(i)
```
```commandline
0
1
2
3
4
5
```

---
```python
lower_bound = 1
upper_bound = 5

for i in range(lower_bound, upper_bound + 1):
    print(i)
```
```commandline
1
2
3
4
5
```
---
```python
lower_bound = 1
upper_bound = 5

for i in range(lower_bound, upper_bound + 1, 2):
    print(i)
```
```commandline
1
3
5
```
---
Reverse order:
```python
lower_bound = 1
upper_bound = 5

for i in range(upper_bound, lower_bound - 1, -1):
    print(i)
```
```commandline
5
4
3
2
1
```


## ```continue```, ```break```

```continue``` - skips the rest of the current iteration and moves to the next iteration of the loop. Ofter used to skip unwanted elements in a sequence or to avoid executing some part of the code under certain conditions.
Example:
```python
for i in range(5):
    if i == 2:
        continue # Skip this iteration when i is 2
    print(i)

# Output: 0, 1, 2, 3, 4
```
```break``` - immediately exits the loop. regardless of the loop condition. Commonly used to terminate a loop early when a specific condition is met
Example:
```python
for i in range(5):
    if i == 3:
        break # Exit the loop when num is 3
    print(i)
# Output: 0, 1, 2
```

### Using  ```continue``` and ```break``` together

```python
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    if i > 5:
        break  # Stop the loop if i is grater than 5
    print(i)
# Output: 1, 3, 5
```