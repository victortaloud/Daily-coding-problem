"""This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:
```python
def cons(a, b):
    return lambda f : f(a, b)
```
Implement car and cdr."""
def cons(a, b):
    return lambda f : f(a, b)

def car(func):
    z = lambda x, y: x
    return func(z)

def cdr(func):
    z = lambda x, y: y
    return func(z)

cons_instance = cons('a','b')
print(car(cons_instance))
print(cdr(cons_instance))