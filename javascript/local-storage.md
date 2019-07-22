# Local Storage

Browsers store variables in the local storage as strings, so you have to parse them into JSON or use strings.

```js
//to get
let myVar = window.localStorage.getItem('myVar');

//to set
window.localStorage.setItem("myVar", myVar);
```
