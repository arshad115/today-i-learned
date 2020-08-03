### Iterate over nested lists

Python lists follow this logic when iterating: `[thing for thing in list_of_things]`

```py
mylist = [[x for x in range(10)] for _ in range(10)]
```