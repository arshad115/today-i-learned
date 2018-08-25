# Circular ImageView with Picasso

If you are using the [Picasso](http://square.github.io/picasso/) library to load images on Android and you want to show a circular image then use [Picasso Transformations](https://github.com/wasabeef/picasso-transformations) library to transform the image before loading. 

### Import

```java
implementation 'jp.wasabeef:picasso-transformations:2.2.1'
```

### Usage 

You can use the `CropCircleTransformation` to get a rounded image which you can pass to the view.

```java
Picasso.with(mContext).load(R.drawable.demo)
    .transform(new CropCircleTransformation())
    .into(holder.image);
```

P.S. The library also has other useful image transformations which you can use. Check them out here: [Picasso Transformations](https://github.com/wasabeef/picasso-transformations)
