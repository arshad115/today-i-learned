# Pass data to routerLink

If you want to pass data to a url using a property like so: `/user/:id/details`, then:

```js
[routerLink]="['user', user.id, 'details']"
```

 Solution found here: [How to pass a parameter to routerLink that is somewhere inside the URL](https://stackoverflow.com/questions/38062702/how-to-pass-a-parameter-to-routerlink-that-is-somewhere-inside-the-url)