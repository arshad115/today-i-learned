Angular calls ngOnInit for a compoment's initialization. It is a good place to perform initialization logic but can throw errors, 
because the variables can be undefined which are binded to the views. 

In typescript you can use:
```ts
if(typeof myVariable == "undefined") //no errors
```

To avoid angular throwing out undefined errors in html, you can use the following two methods:

### 1. Using *ngIf
```html
<component-or-tag *ngIf="myVariable" ></component-or-tag>
```
This will not throw errors and wait for the myVariable to be initialized. 

### 2. Using safe navigation operator ( ?. ) to allow variable to be null or undefined
```html
<component-or-tag>{{myVariable?.property}}</component-or-tag>
```
This is sure way to check if the value is null or undefiend. Atleast, the app doesn't crash. More details here: [the-safe-navigation-operator](https://angular.io/guide/template-syntax#the-safe-navigation-operator----and-null-property-paths)
