### Convert list to string

Convert list `self.tags` and add spaces in between the list items.

```py
' '.join(map(str, self.tags))
```

Input:
```py
self.tags = ['t02', 'tr2', 't52', 'tp6', 'th5', 't37', 'ts2', 'tl5', 'tn3', 't44', 'th4', 'tv2', 'tq1', 'tn6', 'td']
```

Output:
```py
t02 tr2 t52 tp6 th5 t37 ts2 tl5 tn3 t44 th4 tv2 tq1 tn6 td
```
