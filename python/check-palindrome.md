---
title: Check if a string is a palindrome
excerpt: Compare a Python string with its reversed slice to check whether it is a palindrome.
---

Slicing is the way to go.

```py
def isPalindrome(s): 
    return s == s[::-1] 
```
