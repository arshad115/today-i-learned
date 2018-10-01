# Cast or deserialize a Json object to a class in C#

Deserialize Javascript/Json objects using [JavaScriptSerializer](https://docs.microsoft.com/de-de/dotnet/api/system.web.script.serialization.javascriptserializer?view=netframework-4.7.2) in C#.

```cs
using System.Web.Script.Serialization;

    ////////////////////////////////////////////////
    public class MyClass
    {
        public string name { get; set; }
    }
    ////////////////////////////////////////////////
    
    var data = "{ \"name\":\"Test\" }"; // your json string
    
    JavaScriptSerializer json_serializer = new JavaScriptSerializer();
    try
    {
        MyClass myClassObject = json_serializer.Deserialize<MyClass>(data);
    }
    catch (Exception e)
    {
        throw;
    }

```
