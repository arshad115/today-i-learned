# Docstring for describing functions

The methods in python can be described with docstring. Docstring for a method can be accessed using `__doc__`.

```python

def add(self):
    """Create a new user.
    Line 2 of comment...
    And so on... 
    """

def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2

print(square.__doc__)
```
