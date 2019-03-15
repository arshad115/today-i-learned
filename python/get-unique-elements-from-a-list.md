# Get unique elements from a list

The following function is one of the many provided in the link below. This one is order preserving.

```python
def uniqueElements(seq, idfun=None): 
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       # in old Python versions:
       # if seen.has_key(marker)
       # but in new ones:
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return result
```

More info [here](https://www.peterbe.com/plog/uniqifiers-benchmark)