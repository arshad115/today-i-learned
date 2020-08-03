### Strip non-alphabetical or non-alphanumeric characters in a string

Python characters have a function `isalpha()` and `isalnum()` which can be used to strip non-alphabetical or non-alphanumeric characters in a string.

```py
s = ''.join(x for x in s if x.isalnum())
s = ''.join(x for x in s if x.isalpha())
```