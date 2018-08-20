# Float Left/Right with display:flex

`float: left;` ro `float: right;` does not work with `display: flex;`.

### Solution: `margin: auto;`

Lets say the parent has the style property `display: flex;`. Now if you want the children to float left or right, do as follows.

#### Float Right
Use:
```css
style="margin-right: auto;"
```

#### Float Left
Use:
```css
style="margin-left: auto;"
```

### Complete code
```html
  <div style="display: flex;">
        <div style="margin-right: auto;">Float left</div>
        <div style="margin-left: auto;">Float right</div>
  </div>
```

Code on jsfiddle:
[https://jsfiddle.net/arshad115/h3qwLvuy/1/](https://jsfiddle.net/arshad115/h3qwLvuy/1/)
