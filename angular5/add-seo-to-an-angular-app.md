# Add SEO to an Angular App

Angular apps are not search engine and crawler friendly because all the script is loaded on the client side. To solve this issue, one has to run some code on the server side. It's pretty easy. You just have to add the Angular Universal plugin. 

To install, we will use this [ng-toolkit](ng add @ng-toolkit/universal):

```ts
ng add @ng-toolkit/universal
```

All the files will be added by this toolkit and your app will be search engine friendly. But, before you serve your app, make sure to build it first using 'prod' argument. 
