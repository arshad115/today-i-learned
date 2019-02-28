### Print object to string

To convert object to string whenever you print it, add the `__str__` method in your class like so: 

```py
 class Test:
    def __str__(self):
        return "My Objects array "  + ' '.join(map(str, self.tags))
```

Input:
```py
self.tags = ['t02', 'tr2', 't52', 'tp6', 'th5', 't37', 'ts2', 'tl5', 'tn3', 't44', 'th4', 'tv2', 'tq1', 'tn6', 'td']
```

Output:
```py
My Objects array t02 tr2 t52 tp6 th5 t37 ts2 tl5 tn3 t44 th4 tv2 tq1 tn6 td
```
