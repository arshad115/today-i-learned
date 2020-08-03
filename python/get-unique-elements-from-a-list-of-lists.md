# Get unique elements from a list of lists

Using set with tuple:

```python
unique_data = [list(x) for x in set(tuple(x) for x in testdata)]
```

More info [here](https://stackoverflow.com/questions/3724551/python-uniqueness-for-list-of-lists) and [here](https://www.peterbe.com/plog/uniqifiers-benchmark)