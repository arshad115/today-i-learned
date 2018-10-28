# Add Cache-Control headers

To add headers to your static resources in Firebase hosting, add the `headers` section within `hosting` in the `firebase.json` file:

```json
"hosting": {
  // Add the "headers" section within "hosting".
  "headers": [ {
    "source" : "**/*.@(eot|otf|ttf|ttc|woff|font.css)",
    "headers" : [ {
      "key" : "Access-Control-Allow-Origin",
      "value" : "*"
    } ]
  }, {
    "source" : "**/*.@(jpg|jpeg|gif|png)",
    "headers" : [ {
      "key" : "Cache-Control",
      "value" : "max-age=300000"
    } ]
  }, {
    // Sets the cache header for 404 pages to cache for 5 minutes
    "source" : "404.html",
    "headers" : [ {
      "key" : "Cache-Control",
      "value" : "max-age=300"
    } ]
  } ]
}
```

[More info](https://firebase.google.com/docs/hosting/url-redirects-rewrites)