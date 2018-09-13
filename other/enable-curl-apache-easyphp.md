# Enable Curl in PHP.ini running on EasyPHP

Removing the semicolon from `;extension=php_curl.dll` in `php.ini` did not work for me on Windows with EasyPHP. The solution is to go to the `eds-binaries` folder then inside your `php` folder, copy the `libssh2.dll` to your `apache\bin` folder in `httpserver` folder of your EasyPHP installation.

Restart apache and it curl should work. You can also put the `libssh2.dll` in `C:\Windows\`

Answer found [here](https://stackoverflow.com/questions/34905939/activation-curl-on-easyphp)