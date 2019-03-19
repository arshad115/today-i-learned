# Create Stream from a Base64 String

Make sure your image data does not contain some header information at the beginning:
```csharp
imageCode = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAABkC...
```
This will cause an error. Just remove everything in front of and including the first comma, and you good to go.

```csharp
imageCode = "iVBORw0KGgoAAAANSUhEUgAAAMgAAABkC...
```

### Covert base64 image to a stream
```csharp
Stream memStream = new MemoryStream(Convert.FromBase64String(base64StringData));
```
