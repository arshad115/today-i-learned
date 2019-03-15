# Convert list to dictionary with indexes

```python
>>> lst = ['A','B','C']
>>> {k: v for v, k in enumerate(lst)}
{'A': 0, 'C': 2, 'B': 1}
```
[Source](https://stackoverflow.com/questions/36459969/python-convert-list-to-dictionary-with-indexes)