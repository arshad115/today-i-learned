# Load data in webView second time

If you use, `webview.loadData()` it doesn't work in the subsequent calls. Instead use `WebView.loadDataWithBaseURL()` like this:

```java
WebView.loadDataWithBaseURL(null, data.toString(), "text/html","UTF-8", null);
```

