# Reservoir sampling a list

Getting k random elements from a list of unknown size:

```python
import random
def random_subset( iterator, K ):
    result = []
    N = 0

    for item in iterator:
        N += 1
        if len( result ) < K:
            result.append( item )
        else:
            s = int(random.random() * N)
            if s < K:
                result[ s ] = item

    return result
```

Got it from [here](https://stackoverflow.com/questions/2612648/reservoir-sampling)