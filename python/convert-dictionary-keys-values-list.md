# Convert dictionary values or keys to list

In Python 3, the `dict.keys()` or `dict.values()` method returns a [dictionary view object](http://docs.python.org/3/library/stdtypes.html#dictionary-view-objects), which acts as a set. Iterating over the dictionary directly also yields keys, so turning a dictionary into a list results in a list of all the keys or values.

```python
orders = {
	'cappuccino': 54,
	'latte': 56,
	'espresso': 72,
	'americano': 48,
	'cortado': 41
}

keys = list(orders.keys())
values = list(orders.values())
```
[Source](<https://stackoverflow.com/questions/18552001/accessing-dict-keys-element-by-index-in-python3> )