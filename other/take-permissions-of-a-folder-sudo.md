# Take permissions of a folder using sudo on Linux

Replace with folder name:
```
sudo chmod a+rwx /var/log/nginx/
```
This too:
```
sudo chown -R www-data:www-data /var/log/nginx;
sudo chmod -R 755 /var/log/nginx;
```
