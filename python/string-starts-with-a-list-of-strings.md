### String starts with a list of strings

`str.startswith` allows you to pass a tuple of strings to check if the string starts with any of them.

```py
if mystr.startswith((']', ')', '}')):
    return False
```