### LDAP query search filter syntax

LDAP (Lightweight Directory Access Protocol) query filter syntax can be found [here](https://docs.microsoft.com/en-us/windows/desktop/ADSI/search-filter-syntax)

I will mention a few useful ones here:

```csharp
query = "(cn=*bob*)"; //contains 'bob' anywhere in cn
query = "(&(objectClass=user)(email=*))"; //users which have email
query = "(!(email=*))"; //users witout email
query = "(&(objectClass=user)(| (cn=andy*)(cn=steve*)(cn=margaret*)))"; //user entries with a common name that starts with "andy", "steve", or "margaret"
```
