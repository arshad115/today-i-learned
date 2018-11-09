# Bind local method to Dom event listener

Lets say you have a method called which you want to be called on some event. You can add the event listener and while adding you should `bind` this event with `this` :D 

```ts
  localTypescriptMethod() {
    console.log('hi :)');
  }

  addClick() {
    window.addEventListener('click', this.localTypescriptMethod.bind(this));
  }
```
