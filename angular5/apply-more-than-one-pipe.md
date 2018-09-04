# Apply two or more pipes

To transforme the data, we can apply multiple pipes. It is called [chaining](https://angular.io/guide/pipes), the same as in method chaining. 

```ts
The chained hero's birthday is
{{ birthday | date | uppercase}}
```
This example—which displays FRIDAY, APRIL 15, 1988—chains the same pipes as above, but passes in a parameter to date as well.