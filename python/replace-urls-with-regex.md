# Replace URLs using Regex

Replacing urls with regex is very easy.

```python
import re
text = re.sub('http://\S+|https://\S+', '', textWithURLs)
```


