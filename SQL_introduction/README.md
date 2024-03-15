```markdown
# SQL - Introduction Project

## Project Information

- **Project Title:** SQL - Introduction
- **Level:** Novice
- **By:** Guillaume
- **Weight:** 1

## Concepts

For this project, the focus is on the following concept:

- Databases

## Resources

To complete this project, the following resources are recommended:

- [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
- [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial)
- [Basic SQL statements: DDL and DML](http://www.petefreitag.com/cheatsheets/sql/)
- [Basic queries: SQL and RA](http://infolab.stanford.edu/~ullman/fcdb/oracle/or-queries.html)
- [SQL technique: functions](https://www.w3schools.com/sql/sql_functions.asp)
- [SQL technique: subqueries](https://www.w3resource.com/sql/subqueries/understanding-sql-subqueries.php)
- [MySQL Cheat Sheet](https://devhints.io/mysql)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-syntax.html)

## Learning Objectives

Upon completion of this project, you should be able to:

- Describe what a database is and its purposes.
- Explain the concept of a relational database.
- Understand what SQL stands for.
- Describe what MySQL is and its functionalities.
- Demonstrate how to create a database in MySQL.
- Understand the difference between DDL (Data Definition Language) and DML (Data Manipulation Language).
- Perform table creation and alteration.
- Execute data selection from a table.
- Implement data insertion, updating, and deletion.
- Utilize subqueries in SQL queries.
- Apply MySQL functions in queries.

## General Requirements

- **Editors:** vi, vim, emacs.
- **Environment:** All scripts will be tested on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25).
- **Documentation:** A `README.md` file at the root of the folder of the project is mandatory.
- **Style:** All SQL keywords should be in uppercase (e.g., SELECT, WHERE).
- **Comments:** All your SQL queries should have a comment just before, explaining the task.

## Setup Instructions

1. **Install MySQL on Ubuntu 20.04 LTS:**

```bash
sudo apt update
sudo apt install mysql-server
mysql --version
```

2. **Connect to your MySQL server:**

```bash
sudo mysql
```

3. **Use the provided SQL scripts to interact with the database as per the project tasks.**

## Tasks

This project consists of multiple tasks starting from basic database and table creation, data manipulation, to advanced SQL queries involving subqueries and functions. Each task builds upon the previous one, requiring the use of SQL statements to manipulate and query data within the MySQL server.

### Example Task: List Databases

**Objective:** Write a script that lists all databases of your MySQL server.

**Requirements:**

- Do not use the `SELECT` or `SHOW` statements for tasks not permitting them.
- Follow the naming conventions and guidelines for SQL scripting.

**Example Usage:**

```bash
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
```
