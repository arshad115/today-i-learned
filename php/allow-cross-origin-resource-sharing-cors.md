# Allow CORS - Cross origin resource sharing 

When writing APIs in PHP, you want other domains to access your server and you can enable it on your sever with this simple header:

```php
<?php
header('Access-Control-Allow-Origin: *'); 
?>
```
