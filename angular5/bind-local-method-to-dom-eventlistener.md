# Bind local method to Dom event listener

Lets say you have a method called which you want to be called on some event. 

### Method 1
You can add the event listener and while adding you should `bind` this event with `this` :D 

```ts
  localTypescriptMethod() {
    console.log('hi :)');
  }

  addClick() {
    window.addEventListener('click', this.localTypescriptMethod.bind(this));
  }
```

### Method 2
Use [HostListener](https://angular.io/api/core/HostListener) to bind the method to the click event, or some other event.

```ts
@HostListener('document:click')
  localTypescriptMethod() {
    console.log('hi :)');
  }
```
