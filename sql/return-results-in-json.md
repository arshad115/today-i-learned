# Return results in json

The following works for `MS SQL Server`:

```sql
SELECT *
FROM Table 
where id = 1
FOR JSON AUTO, Without_Array_Wrapper;
```
Result:
```json
{"id":1,"name":"test"}
```
