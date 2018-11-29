# Add an attribute to a json object using spread operator

The [Spread Operator](https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/Operators/Spread_operator) is "..." *three dots*, which allows to extend an object.

Code for adding attributes to an existing json object:

```
var parts = ['shoulders', 'knees'];
var lyrics = ['head', ...parts, 'and', 'toes']; // ["head", "shoulders", "knees", "and", "toes"]
```

You can also extend the same object also:
```
parts =  [...parts, 'and', 'toes'];
```
