```markdown
# SQL - More Queries

## Project Overview

- **Level:** Amateur
- **Weight:** 1

## Resources

### Reading

- [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://dev.mysql.com/doc/refman/8.0/en/grant.html)
- [MySQL constraints](https://dev.mysql.com/doc/refman/8.0/en/constraint-primary-key.html)
- [Subqueries, Joins, and Unions](https://www.mysqltutorial.org/mysql-subquery/)
- [MySQL Cheat Sheet](https://devhints.io/mysql)
- [SQL Style Guide](https://www.sqlstyle.guide/)

### Extra Resources on Database Design

- [Database Design](https://www.databasestar.com/data-modeling-introduction/)
- [Normalization](https://www.studytonight.com/dbms/database-normalization.php)
- [ER Modeling](https://www.lucidchart.com/pages/er-diagrams)

## Learning Objectives

After completing this project, you should be able to:

- Create a new MySQL user and manage its privileges.
- Understand the role and application of `PRIMARY KEY` and `FOREIGN KEY`.
- Use `NOT NULL` and `UNIQUE` constraints.
- Retrieve data from multiple tables in one request with subqueries.
- Utilize `JOIN` and `UNION` to combine data from different tables.
- Distinguish between different types of joins.

## General Requirements

- **Editors:** vi, vim, emacs
- **Environment:** All SQL files should run on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25).
- **Documentation:** A `README.md` file at the project root is mandatory.
- **SQL Standards:** All keywords should be uppercase (e.g., `SELECT`, `WHERE`).

## More Info

### SQL File Comments

```sql
-- Comment describing the SQL script
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

### MySQL Installation (Ubuntu 20.04 LTS)

```bash
sudo apt update
sudo apt install mysql-server
mysql --version
```

### Connecting to MySQL Server

```bash
sudo mysql
```

### Importing SQL Dump

```bash
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
curl -s "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/.../hbtn_0d_tvshows.sql" | mysql -uroot -p hbtn_0d_tvshows
```

## Tasks

1. **My Privileges:** Script that lists all privileges of specified MySQL users.
2. **Root user:** Create a MySQL server user with all privileges.
3. **Always a Name:** Create a table that includes `NOT NULL`.
4. **ID can't be null:** Table creation with an `id` that has a default value and cannot be null.
5. **Unique ID:** Ensure `id` is unique in a table.
6. **States Table:** Create a `states` table with a `PRIMARY KEY`.
7. **Cities Table:** Incorporate `FOREIGN KEY` in `cities` table referencing `states`.
8. **Cities of California:** List cities from a specific state using subqueries.
9. **Cities by States:** Use a single SELECT statement to join cities and states.
10. **Genre ID by Show:** List all shows and their genres by id.
11. **Genre ID for All Shows:** Similar to the previous task but include shows without a genre.
12. **No Genre:** List shows that do not have any genres.
13. **Number of Shows by Genre:** Count shows per genre.
14. **My Genres:** List genres of a specific show.
15. **Only Comedy:** List all Comedy shows.
16. **List Shows and Genres:** Show all shows and their respective genres, including those without a genre.

### Repository Structure

Each SQL script should perform the task as described, adhering to the project specifications and requirements.

```plaintext
holbertonschool-higher_level_programming/
└── SQL_more_queries/
    ├── 0-privileges.sql
    ├── 1-create_user.sql
    ├── 2-create_read_user.sql
    ├── 3-force_name.sql
    ├── 4-never_empty.sql
    ...
```
