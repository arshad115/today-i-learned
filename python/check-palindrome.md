### Check if string is numeric

Slicing is the way to go.

```py
def isPalindrome(s): 
    return s == s[::-1] 
```