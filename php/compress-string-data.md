# Compress string or data

There are different methods available which use different algorithms to compress and decompress. e.g `gzcompress`, `gzinflate`, `bzcompress`,...

With `gzcompress` I was able to compress upto 530% of my string data.

`gzcompress`:
```php
<?php
$compressed = gzcompress('Compress me', 9);
$decompress = gzuncompress($compressed);
echo $compressed."\n";
echo $decompress;
?>
```


