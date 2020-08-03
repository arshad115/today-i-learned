### Check if list contains unique elements

Python sets are always unique, so we can compare the length of the original list with a list of set of the original list.

```py
# using set() + len() 
# to check all unique list elements 
isListUnique = len(set(test_list)) == len(test_list) 
```