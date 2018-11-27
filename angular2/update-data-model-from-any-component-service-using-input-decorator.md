# Update Data Model from any component or service using @Input Decorator

Lets say, you are already loaded data from a service and after some time the data is changed in the service, the bounded model is not updated. The solution is very easy, add an [Input](https://angular.io/api/core/Input) decorator to the variable.
As mentioned on the Angular site:
> Declares a data-bound input property, which Angular automatically updates during change detection.

Just add '@Input()` before your property name and use it directly in the template, the model will be updated automatically on changes. 

```ts
//In myservice
@Input() isVisible: boolean;

//In another component template
<div  *ngIf="myservice.isVisible"></div>
```
