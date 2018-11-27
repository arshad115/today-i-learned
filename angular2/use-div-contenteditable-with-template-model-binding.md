# Use div contenteditable property with template model binding

If you have div with contenteditable property and you want to bind data model with it, it does not work in angular. While you can edit the div, but the model is not binded/updated.

# Solution:
 You have to implment `ControlValueAccessor`. To make things easier, just use this package:
  [ng-contenteditable](https://github.com/KostyaTretyak/ng-contenteditable)
  
 Solution found here: [how-to-use-ngmodel-on-divs-contenteditable-in-angular2](https://stackoverflow.com/questions/35378087/how-to-use-ngmodel-on-divs-contenteditable-in-angular2)
