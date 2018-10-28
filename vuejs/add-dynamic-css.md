# Add dynamic Css Style or Class

You can use the `v-bind` property to use dynamic css. You have two directives, namely: *`v-bind:style`* and *`v-bind:class`*.

For dynamic styles:

```js
//data model
data() {
  return {
    fontSize: 10
  }
}

//template
<button v-on:click="fontSize++">
  Increase font size
</button>
<button v-on:click="fontSize--">
  Decrease font size
</button>

<p v-bind:style="{ fontSize: fontSize + 'px' }">
  Font size is: {{ fontSize }}
</p>
```



For dynamic classes:

```js
//data model
data() {
  return {
    selected: 'Home',
    menuItems: ['Home', 'About', 'Contact']
  }
}

//template
<ul>
  <li v-for="item in menuItems"
    v-on:click="selected = item"
    v-bind:class="{ selected: selected == item}">
      {{item}}
  </li>
</ul>
```



More details here: [Dynamic Styles With Vue.js](https://alligator.io/vuejs/dynamic-styles/)