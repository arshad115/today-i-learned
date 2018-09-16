# Get Firebase Project Name

Firebase Project or App name is available as global variable here:

```js
process.env.GCLOUD_PROJECT
```

You can use this variable simply to get the app name or current domain like so:

```
    const domainName = 'https://' + process.env.GCLOUD_PROJECT + '.firebaseapp.com';
    console.log(domainName)
```

