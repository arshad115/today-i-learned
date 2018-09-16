# Get directory name and filename of the current module in Nodejs

We can use the variables `__dirname` and `__filename` to get the directory and filename respectively. These variables appear global, but they are not. Read more about them [here](https://nodejs.org/api/modules.html#modules_dirname).

### __dirname

Example: running `node example.js` from `/Users/mjr` 

```js
console.log(__dirname);
// Prints: /Users/mjr
console.log(path.dirname(__filename));
// Prints: /Users/mjr

```

### `__filename` 
```javascript
console.log(__filename);
// Prints: /Users/mjr/example.js
console.log(__dirname);
// Prints: /Users/mjr

```

### 