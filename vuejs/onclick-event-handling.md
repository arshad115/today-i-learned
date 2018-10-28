# OnClick Event Handling

 Use the `v-on` directive to listen to DOM events and run some JavaScript when they’re triggered. You can also use the method name:

```js
<div id="example-2">
  <!-- `greet` is the name of a method defined below -->
  <button v-on:click="greet">Greet</button>
</div>

var example2 = new Vue({
  el: '#example-2',
  data: {
    name: 'Vue.js'
  },
  // define methods under the `methods` object
  methods: {
    greet: function (event) {
      // `this` inside methods points to the Vue instance
      alert('Hello ' + this.name + '!')
      // `event` is the native DOM event
      if (event) {
        alert(event.target.tagName)
      }
    }
  }
})

// you can invoke methods in JavaScript too
example2.greet() // => 'Hello Vue.js!'
```

More details [here](https://vuejs.org/v2/guide/events.html).