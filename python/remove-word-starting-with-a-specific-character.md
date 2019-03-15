# Remove word starting with a specific character

Take out the word if it starts with a certain letter. It can be done with regex or without. I prefer the regex one:

```python
import re
clean = re.sub(r'(\s)?@\w+', r'\1', '@myStupidFriend please remove the mention')
```

