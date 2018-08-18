# Using and importing custom font in Angular 5

To import a custom font in an Angular application, follow these steps:

1. Place the font files in `assets/fonts` folder.

2. In your `style.less` or `style.css` or `style.scss` file, declare a `font-face` like below, with all the font files which you have added in the previous step.

```css
@font-face {
    font-family: custom-bold;
    src: url('assets/fonts/custom-bold.woff') format('woff'), url('assets/fonts/custom-bold.woff2') format('woff2'), url('assets/fonts/custom-bold.eot') format('eot'), url('assets/fonts/custom-bold.ttf') format('truetype');
    font-weight: normal;
  }
``` 

3. After declaring the font, you can use it anywhere like so:

```css
  font-family: 'custom-bold';
```
