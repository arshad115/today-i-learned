# Split dictionary into chunks

Get smaller chunks of dictionary!

```python
def split_dict_equally(input_dict, chunks=2):
    "Splits dict by keys. Returns a list of dictionaries."
    # prep with empty dicts
    return_list = [dict() for idx in xrange(chunks)]
    idx = 0
    for k,v in input_dict.iteritems():
        return_list[idx][k] = v
        if idx < chunks-1:  # indexes start at 0
            idx += 1
        else:
            idx = 0
    return return_list
```
[Source](https://gist.github.com/miloir/2196917)
