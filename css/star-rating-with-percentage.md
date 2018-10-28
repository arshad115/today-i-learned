# Star ratings with percentage

Made in pure css(not by me). Just copy paste.

HTML:

```html
<div class="star-ratings-css">
  <div class="star-ratings-css-top" style="width: 54%"><span>★</span><span>★</span><span>★</span><span>★</span><span>★</span></div>
  <div class="star-ratings-css-bottom"><span>★</span><span>★</span><span>★</span><span>★</span><span>★</span></div>
</div>
```

Css:

```css
.star-ratings-css {
  unicode-bidi: bidi-override;
  color: #c5c5c5;
  font-size: 25px;
  height: 25px;
  width: 100px;
  margin: 0 auto;
  position: relative;
  padding: 0;
  text-shadow: 0px 1px 0 #a2a2a2;
  
  &-top {
    color: #e7711b;
    padding: 0;
    position: absolute;
    z-index: 1;
    display: block;
    top: 0;
    left: 0;
    overflow: hidden;
  }
  &-bottom {
    padding: 0;
    display: block;
    z-index: 0;
  }
}
```

[Codepen.io](https://codepen.io/Bluetidepro/pen/GkpEa)