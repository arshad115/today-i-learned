# Hide an element based on window size

In the [previous til](add-window-resize-event-listener-comopnent.md), I posted the code for window resize event listener, now we will use it to show/hide elements.

### Typescript
```ts
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  host: {
    '(window:resize)': 'onResize($event)'
  }
})
public windowWidth: any;
export class AppComponent{
   constructor() {
    this.windowWidth = document.body.clientWidth;
   }
   onResize(event){
     this.windowWidth = event.target.innerWidth;
   }
}
```

### Template
> Only show if window width is greater than 720 pixels.
```html
<div *ngIf="windowWidth > 720"></div>

```
