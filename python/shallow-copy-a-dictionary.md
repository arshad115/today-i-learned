# Shallow copy a dictionary

Assignment statements in Python do not copy objects, they create bindings between a target and an object. For collections that are mutable or contain mutable items, a copy is sometimes needed so one can change one copy without changing the other. 

```python
shallow_copy_of_other_dict = {**other_dict}
```

More info [here](https://docs.python.org/3.7/library/copy.html)