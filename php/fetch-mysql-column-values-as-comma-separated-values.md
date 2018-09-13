# Fetch MySql column values as array 

When using MySQl in PHP,  if you want to get the column values as an array, then simply change the `fetch_argument` in the PDO `fetchAll` call like this:

```php
<?php
$recipes = $result->fetchAll(PDO::FETCH_COLUMN);
?>
```

Using `PDO::FETCH_COLUMN` will return the column as an array instead of the regular, 2d array when using `FETCH_ASSOC`. You can also specify which columns values you want, returns the first column values if you don't specify. Read more about [PDO Statement fetchAll here](http://php.net/manual/de/pdostatement.fetchall.php).

