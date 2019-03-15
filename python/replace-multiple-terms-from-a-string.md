# Replace multiple terms from a string

Replacing multiple terms in a string.

```python
def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces:
        # Check if string is in the main string
        if elem in mainString:
            # Replace the string
            mainString = mainString.replace(elem, newString)

    return mainString

wordsToRemove = ['via', 'test', 'good']
text = replaceMultiple(originalText, wordsToRemove, '')
```

Got it from [here](https://thispointer.com/python-how-to-replace-single-or-multiple-characters-in-a-string/)
