---
title: Check Postgres db table in Docker
excerpt: Open a PostgreSQL shell inside a Docker container, list tables, inspect a schema, and query its rows.
---

```bash
# List running containers to find the container ID or name
docker ps

# Access the PostgreSQL container
docker exec -it postgres_container bash

# Connect to PostgreSQL
psql -U postgres -d mydatabase

# List all tables
\dt

# Describe the structure of the 'ratings' table
\d ratings

# Query data from the 'ratings' table
SELECT * FROM ratings;
```
