# Show logs from TimingLogger

If you are using `TimingLogger` to log the times of code execution then they don't just show up in the logcat. You have to enable them like so:

> Run this command in the console/terminal

```java
adb shell setprop log.tag.MyTag VERBOSE
```

*MyTag* is the first argument which you pass to create an instance of `TimingLogger`.