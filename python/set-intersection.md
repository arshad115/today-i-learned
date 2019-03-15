# Set intersection

Get common elements in two or more sets:

### Input
```python
set1 = {2, 4, 5, 6}  
set2 = {4, 6, 7, 8}  
set3 = {4,6,8} 
  
# intersection of two sets 
print("set1 intersection set2 : ", set1.intersection(set2)) 
  
# intersection of three sets 
print("set1 intersection set2 intersection set3 :", set1.intersection(set2,set3)) 
```

### Output
```py
set1 intersection set2 :  {4, 6}
set1 intersection set2 intersection set3 : {4, 6}
```
