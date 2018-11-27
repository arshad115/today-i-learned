# Add a Window Resize event listener for a component

Register a window resize event listener within a component: 

```ts
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  host: {
    '(window:resize)': 'onResize($event)'
  }
})
export class AppComponent{
   onResize(event){
     console.log(event.target.innerWidth); // window width
   }
}
```

There are other ways also, I got the answer from [here](https://stackoverflow.com/questions/35527456/angular-window-resize-event).
