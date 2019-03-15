# Trim strings in Python

In Python strings can be trimmed using the following three functions:

* **strip()**: returns a new string after removing any leading and trailing whitespaces including tabs (\t).
* **rstrip()**: returns a new string with trailing whitespace removed. It’s easier to remember as removing white spaces from “right” side of the string.
* **lstrip()**: returns a new string with leading whitespace removed, or removing whitespaces from the “left” side of the string.

Equivalent of `C#`'s `Trim()` funciton is `strip()`.


```python
str = '  abc  '
>>> str.strip()
'abc'
>>> str.rstrip()
'  abc'
>>> str.lstrip()
'abc  '
```

