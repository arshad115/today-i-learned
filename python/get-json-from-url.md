# Get json from a URL

Getting and parsing a json from a url. So Easy!

```python
import json,urllib.request
data = urllib.request.urlopen("https://api.coindesk.com/v1/bpi/currentprice/usd.json").read()
output = json.loads(data)
```

