# Find all tables with a specific column name

### Search Tables:
```sql
SELECT      c.name  AS 'ColumnName'
            ,t.name AS 'TableName'
FROM        sys.columns c
JOIN        sys.tables  t   ON c.object_id = t.object_id
WHERE       c.name LIKE '%MyName%'
ORDER BY    TableName
            ,ColumnName;
```

### Search Tables & Views:
```sql
SELECT      COLUMN_NAME AS 'ColumnName'
            ,TABLE_NAME AS  'TableName'
FROM        INFORMATION_SCHEMA.COLUMNS
WHERE       COLUMN_NAME LIKE '%MyName%'
ORDER BY    TableName
            ,ColumnName;
```

Learnt from [here](https://stackoverflow.com/questions/4849652/find-all-tables-containing-column-with-specified-name-ms-sql-server)
