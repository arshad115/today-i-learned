### Add current user as the owner of a folder to give write permissions

Run the following commands:

```
sudo chmod -R 757 /var/www
sudo chown -R $USER:$USER /var/www
```

Replace with your own folder
