# Indexes in strings

indexes starts from 0 and he also can be negative

```python
text = input('Enter: ')

print(text[0])
print('Hello'[1])
```

```commandline
Enter: Greetings
G
e
```

```python
text = input('Enter: ')

print(text[len(text) - 1])
print(text[-1])
```


|                | H   | e  | l  | l  | o  |    | w  | r  | l  | d  |
|----------------|-----|----|----|----|----|----|----|----|----|----|
| Normal index   | 0   | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 
| Negative index | -10 | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 | 

```commandline
Enter: Hello world
d
d
```