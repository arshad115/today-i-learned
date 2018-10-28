# Add a new file type to context menu in Windows 10

I wanted to add the option to create a new ` Mardown` file to the context menu in Windows 10. Its a really simple process.

Step 1. Open `regedit` using `Run`.

Step 2. Go to `HKEY_CLASSES_ROOT `.

Step 3. Find the extension type, in my case `.md`.

Step 4. Create a new `key` named: `ShellNew`.

Step 5. In this newly created key, create a string named: `NullFile` and assign it a value of 1.

That's it! 

Now you will be seeing your new file type extension in the new context menu of Windows. 

[Link with pictures](https://www.techrepublic.com/article/how-to-add-a-new-file-type-to-the-microsoft-windows-10-context-menu/)