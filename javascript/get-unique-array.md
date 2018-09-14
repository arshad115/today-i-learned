# Get only unique values from a Javascript Array

Following function only gives out the unique/distinct values from the array.

```js
  uniqueArray (arrArg) {
    return arrArg.filter(function(elem, pos, arr) {
      return arr.indexOf(elem) === pos;
    });
  }
```
