# Enable gzip compression

To enable gzip compression in PHP use this single line of code:

```php
  <?php
    ob_start("ob_gzhandler");
  ?>
```

This will add the gzip headers and also tell the browser that the page is compressed using gzip, so that the browser can decompress it easily.
I saved around 230% of data transfer per page using gzip.
