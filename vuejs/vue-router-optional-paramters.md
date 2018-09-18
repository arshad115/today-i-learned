# Optional parameters in Vue Router

Making parameteres optional is very easy. You just have to add a `?` at the end of the paramater. Like so:

```js
const router = new VueRouter({
	routes: [
  	{ path: '/product/:product/:optional?' }
  ]
})
```
Here are the Route contexts of such requests, you can see the optional paramter is set to true:
### /product/123/asd:
```json
{
  "meta": {},
  "path": "/product/123/asd",
  "hash": "",
  "query": {},
  "params": {
    "product": "123",
    "optional": "asd"
  },
  "fullPath": "/product/123/asd",
  "matched": [
    {
      "path": "/product/:product/:optional?",
      "regex": {
        "keys": [
          {
            "name": "product",
            "prefix": "/",
            "delimiter": "/",
            "optional": false,
            "repeat": false,
            "partial": false,
            "asterisk": false,
            "pattern": "[^\\/]+?"
          },
          {
            "name": "optional",
            "prefix": "/",
            "delimiter": "/",
            "optional": true,
            "repeat": false,
            "partial": false,
            "asterisk": false,
            "pattern": "[^\\/]+?"
          }
        ]
      },
      "components": {},
      "instances": {},
      "meta": {},
      "props": {}
    }
  ]
}
```

### /product/123/:
```json
{
  "meta": {},
  "path": "/product/123/",
  "hash": "",
  "query": {},
  "params": {
    "product": "123"
  },
  "fullPath": "/product/123/",
  "matched": [
    {
      "path": "/product/:product/:optional?",
      "regex": {
        "keys": [
          {
            "name": "product",
            "prefix": "/",
            "delimiter": "/",
            "optional": false,
            "repeat": false,
            "partial": false,
            "asterisk": false,
            "pattern": "[^\\/]+?"
          },
          {
            "name": "optional",
            "prefix": "/",
            "delimiter": "/",
            "optional": true,
            "repeat": false,
            "partial": false,
            "asterisk": false,
            "pattern": "[^\\/]+?"
          }
        ]
      },
      "components": {},
      "instances": {},
      "meta": {},
      "props": {}
    }
  ]
}
```

