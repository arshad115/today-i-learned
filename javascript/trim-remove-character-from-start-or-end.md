> Trim/Remove first or last character in Javascript

While using C#, if you want to remove the first character or the last character then you can simply use one of the following lines of code:

```cs
//Trim start
string trimmed = str.TrimStart('?', '.', ',');

//Trim End
string trimmed1 = str.TrimEnd('?', '.', ',');

//Trim start single character
string trimsingle = str.TrimStart('?');

```

Javascript's trim method doesn't accept any paramters. To do the same in Javascript, use the following methods:

### Remove the first character
```javascript
//Trim start
var myString = '!thisIsMyString';
var sillyString = myString.substr(1);

```

### Remove the last character
```javascript
//Trim end
var myString = 'thisIsMyString!';
var sillyString = myString.slice(0, -1);

```

### Remove the first character and last character
```javascript
//Trim start and end
var myString = '!thisIsMyString!';
var sillyString = myString.substr(1).slice(0, -1);
```

You can do the same in typescript, as typescript is the same as javascript with some additional features. 

Learnt and shamelessly copied some code from [Removing A Character From The Start/End of a String In Javascript](https://ilikekillnerds.com/2016/05/removing-character-startend-string-javascript/)
