---
title: Remove element from DOM
excerpt: Remove an existing element from the DOM after checking that it exists.
---

```js
var element = document.getElementById("veryCoolID");
if (element != null) {
    element.parentNode.removeChild(element);
}
```
