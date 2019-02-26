### Replace everything in a string before a certain point using regex

To remove/replace anything in a string to a certain point, use the following regex:

```js
  var alphabet = "ABCDEFGHIJKLMNOPQRSTUVEXYZ";
  var replaced = alphabet.replace(/^.+M/,'');
```

This will replace everything before `M` and including `M`.

[Stackoverflow](https://stackoverflow.com/questions/10568815/replace-all-text-before-a-certain-point)
