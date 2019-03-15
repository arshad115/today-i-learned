### Create a stream from string

Use this function:
```csharp
public static Stream GenerateStreamFromString(string s)
{
    var stream = new MemoryStream();
    var writer = new StreamWriter(stream);
    writer.Write(s);
    writer.Flush();
    stream.Position = 0;
    return stream;
}
```

Don't forget to close the stream after using it.

Got it from [here](https://stackoverflow.com/questions/1879395/how-do-i-generate-a-stream-from-a-string)
