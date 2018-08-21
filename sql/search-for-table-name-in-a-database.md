# Search for a table name in a database

## Search for a table
    Use this query to search for a table:
    
    ```sql
    SELECT * FROM INFORMATION_SCHEMA.TABLES 
    WHERE TABLE_NAME LIKE '%%'
    ```
