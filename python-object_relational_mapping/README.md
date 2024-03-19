# Object-Relational Mapping (ORM) with Python

This project bridges the powerful worlds of databases and Python through the use of Object-Relational Mapping (ORM). Specifically, the project focuses on the utilization of the MySQLdb module to interact with MySQL databases and the SQLAlchemy module as an ORM tool.

## Learning Objectives

- How to connect to a MySQL database from a Python script.
- How to SELECT rows in a MySQL table from a Python script.
- How to INSERT rows in a MySQL table from a Python script.
- Understanding what ORM means.
- How to map a Python Class to a MySQL table.

## Requirements

- Python 3.8.5
- MySQLdb version 2.0.x
- SQLAlchemy version 1.4.x
- All files should end with a new line.
- Code should use the `pycodestyle` style (version 2.7.*).
- All files must be executable.
- The length of files will be tested using `wc`.

## Installation

### MySQL 8.0 on Ubuntu 20.04 LTS

```bash
sudo apt update
sudo apt install mysql-server
mysql --version
```

### MySQLdb module version 2.0.x

```bash
sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev
sudo pip3 install mysqlclient
```

### SQLAlchemy module version 1.4.x

```bash
sudo pip3 install SQLAlchemy
```

## Tasks

### 0. Get all states

A script that lists all states from the database `hbtn_0e_0_usa`. It uses MySQLdb to connect and execute SQL queries.

### 1. Filter states

A script that lists all states starting with `N` from the database. It demonstrates basic filtering.

### 2. Filter states by user input

This script takes an argument and shows all values in the `states` table where name matches the argument.

### 3. SQL Injection...

Improvement over the previous task to safeguard against SQL injection.

### 4. Cities by states

Lists all cities from the database `hbtn_0e_4_usa` using a JOIN operation.

### 5. All cities by state

Takes the name of a state as an argument and lists all cities of that state, demonstrating how to prevent SQL injections.

### 6. First state model

Introduces the use of SQLAlchemy ORM by defining a State class and mapping it to the states table.

### 7. All states via SQLAlchemy

A script that lists all State objects from the database using SQLAlchemy.

### 8. First state

Prints the first State object from the database.

### 9. Contains `a`

Lists all State objects that contain the letter 'a'.

### 10. Get a state

Prints the State object with a name passed as an argument.

### 11. Add a new state

Adds the State object "Louisiana" to the database.

### 12. Update a state

Updates the name of a State object from the database.

### 13. Delete states

Deletes all State objects with a name containing the letter 'a'.

### 14. Cities in state

Expands upon the ORM concept by including a City class and demonstrating how to work with related objects.

## Summary

This project showcases the flexibility and power of combining Python scripting with relational database management systems (RDBMS) like MySQL, emphasizing the importance of ORM tools like SQLAlchemy for efficient database manipulation and interaction.