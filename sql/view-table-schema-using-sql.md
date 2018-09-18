# View table schema using SQL

Use this query to get the schema:

```sql
select *
from INFORMATION_SCHEMA.COLUMNS
where TABLE_NAME='tableName'
```

[Stackoverflow](https://stackoverflow.com/questions/18298433/how-can-i-show-the-table-structure-in-sql-server-query)
