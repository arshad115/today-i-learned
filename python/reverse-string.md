# Reverse string

Can be done via many ways; I like the slicing way or the reversed method:

```python
def reverse_string(s):
    return s[::-1]
def reversed_string(s):
    return''.join(reversed(s))
```

P.S. Slicing is the fastest way to reverse a string in python.

