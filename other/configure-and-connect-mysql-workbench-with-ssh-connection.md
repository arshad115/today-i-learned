# Configure and connect Mysql Workbench with SSH connection

Make sure, mysql is installed on your server.

1. First of all, bind your server ip in your `mysqlId.cnf` file:

   `nano /etc/mysql/mysql.confd.d/mysqlId.cnf `

   Place the server ip in this line:

   `bind-address = YOUR_SERVER_IP `

2.  Restart mysql `sudo service mysql restart`

3.  Open port on firewall `sudo ufw allow 3306/tcp`

4. Create a new user and grant all permissions

   1. `CREATE USER 'newuser'@'YOUR_SERVER_IP' IDENTIFIED BY 'password';` 
   2. `GRANT ALL PRIVILEGES ON \* . * TO 'newuser'@'YOUR_SERVER_IP';`
   3. `FLUSH PRIVILEGES;` 
   4. `sudo service mysql restart`

5. Server side is set up now. Now use your ssh credentials and newly created user in mysql workbench to connect. Make sure you are using your private key and that private key is in the `OpenSSH` format. You can export it in `OpenSSH` format using `PUTTYGen` - I spent days scratching my head, because its not documented anywhere!

   In the image below, hostname will be your server ip.

![](https://dev.mysql.com/doc/workbench/en/images/wb-manage-db-connections-ssh-parameters.png)