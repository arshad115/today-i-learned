# Sort dictionary by value

The builtin method "sorted()" can be used to sort a dictionary by values. 

```python
orders = {
	'cappuccino': 54,
	'latte': 56,
	'espresso': 72,
	'americano': 48,
	'cortado': 41
}

# Sort in ascending order
sort_orders_asc = {k:v for k, v in sorted(orders.items(), key= lambda x: x[1])}

# Sort in descending order
sort_orders_desc = {k:v for k, v in sorted(orders.items(), key= lambda x: x[1], reverse=True)}
```

More info [here](https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value)