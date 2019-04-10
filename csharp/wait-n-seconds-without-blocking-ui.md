### Wait N Seconds without blocking ui

```csharp
private void WaitNSeconds(int segundos)
{
    if (segundos < 1) return;
    DateTime _desired = DateTime.Now.AddSeconds(segundos);
    while (DateTime.Now < _desired) {
         System.Windows.Forms.Application.DoEvents();
    }
}
```

From [here](https://stackoverflow.com/questions/22158278/wait-some-seconds-without-blocking-ui-execution)
