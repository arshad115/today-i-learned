# Get only unique values from a Javascript Array

Following function only gives out the unique/distinct values from the array.

```js
  uniqueArray (arrArg) {
    return arrArg.filter(function(elem, pos, arr) {
      return arr.indexOf(elem) === pos;
    });
  }
```

Prototype function:

```js
Array.prototype.unique = function() {
  return this.filter(function (value, index, self) { 
    return self.indexOf(value) === index;
  });
}

//Usage:
var arr = ['a', 1, 'a', 2, '1']
arr.unique(); // => ['a', 1, 2, '1']

```
