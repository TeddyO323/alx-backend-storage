Here's the content in markdown format for your README.md file:

# 0x00. MySQL advanced

## Back-end | SQL | MySQL

## Concepts
For this project, we expect you to look at this concept:

- [Advanced SQL](https://intranet.alxswe.com/concepts/601)

## Resources
Read or watch:

- [MySQL cheatsheet](https://devhints.io/mysql)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.liquidweb.com/kb/mysql-optimization-how-to-leverage-mysql-database-indexing/)
- [Stored Procedure](https://www.mysqltutorial.org/mysql-stored-procedure-tutorial.aspx)
- [Triggers](https://www.mysqltutorial.org/mysql-triggers.aspx)
- [Views](https://www.mysqltutorial.org/mysql-views-tutorial.aspx)
- [Functions and Operators](https://dev.mysql.com/doc/refman/5.7/en/functions.html)
- [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-table.html)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html)
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/5.7/en/create-index.html)
- [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/5.7/en/create-view.html)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- How to create tables with constraints
- How to optimize queries by adding indexes
- What is and how to implement stored procedures and functions in MySQL
- What is and how to implement views in MySQL
- What is and how to implement triggers in MySQL

## Requirements
### General
- All your files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE...)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

## More Info
Comments for your SQL file:

```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

Use "container-on-demand" to run MySQL
- Ask for container Ubuntu 18.04 - Python 3.7
- Connect via SSH
- Or via the WebTerminal
- In the container, you should start MySQL before playing with it:
```
$ service mysql start
 * MySQL Community Server 5.7.30 is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password: 
Database
information_schema
mysql
performance_schema
sys
$
```
- In the container, credentials are `root/root`

How to import a SQL dump

```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

## Tasks

### [0. We are all unique!](./0-uniq_users.sql)
Write a SQL script that creates a table `users` following these requirements:

- With these attributes:
  - `id`, integer, never null, auto increment and primary key
  - `email`, string (255 characters), never null and unique
  - `name`, string (255 characters)

- If the table already exists, your script should not fail
- Your script can be executed on any database

**Context:** Make an attribute unique directly in the table schema will enforce your business rules and avoid bugs in your application

### [1. In and not out](./1-country_users.sql)
Write a SQL script that creates a table `users` following these requirements:

- With these attributes:
  - `id`, integer, never null, auto increment and primary key
  - `email`, string (255 characters), never null and unique
  - `name`, string (255 characters)
  - `country`, enumeration of countries: US, CO and TN, never null (default will be the first element of the enumeration, here US)

- If the table already exists, your script should not fail
- Your script can be executed on any database

### [2. Best band ever!](./2-fans.sql)
Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans.

**Requirements:**
- Import this table dump: [metal_bands.sql.zip](https://intranet.alxswe.com/rltoken/bZxsI58XOk5d6o5j3ic9pw)
- Column names must be: `origin` and `nb_fans`
- Your script can be executed on any database

**Context:** Calculate/compute something is always power intensive... better to distribute the load!

### [3. Old school band](./3-glam_rock.sql)
Write a SQL script that lists all bands with `Glam rock` as their main style, ranked by their longevity.

**Requirements:**
- Import this table dump: [metal_bands.sql.zip](https://intranet.alxswe.com/rltoken/bZxsI58XOk5d6o5j3ic9pw)
- Column names must be: `band_name` and `lifespan` (in years until 2022 - please use 2022 instead of `YEAR(CURDATE())`)
- You should use attributes `formed` and `split` for computing the lifespan
- Your script can be executed on any database

### [4. Buy buy buy](./4-store.sql)
Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

**Quantity in the table `items` can be negative.**

**Context:** Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc... to keep your data in a good shape, let MySQL do it for you!

### [5. Email validation to sent](./5-valid_email.sql)
Write a SQL script that creates a trigger that resets the attribute `valid_email` only when the email has been changed.

**Context:** Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!

### [6. Add bonus](./6-bonus.sql)
Write a SQL script that creates a stored procedure `AddBonus` that adds a new correction for a student.

**Requirements:**
- Procedure `AddBonus` is taking 3 inputs (in this order):
  - `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)
  - `project_name`, a new or already exists `projects` - if no `projects.name` found in the table, you should create it
  - `score`, the score value for the correction

**Context:** Write code in SQL is a nice level up!

### [7. Average score](./7-average_score.sql)
Write a SQL script that creates a stored procedure `ComputeAverageScoreForUser` that computes and store the average score for a student.

**Note:** An average score can be a decimal

**Requirements:**
- Procedure `ComputeAverageScoreForUser` is taking Apologies, let me complete the requirements for task 7:

Requirements:
- Procedure ComputeAverageScoreForUser is taking 1 input:
    - user_id, a users.id value (you can assume user_id is linked to an existing users)

### [8. Optimize simple search](./8-index_my_names.sql)
Write a SQL script that creates an index `idx_name_first` on the table `names` and the first letter of `name`.

Requirements:
- Import this table dump: [names.sql.zip](https://intranet.alxswe.com/rltoken/9QL7kTH3VQKGbMB9Mba-Lw)
- Only the first letter of `name` must be indexed

Context: Index is not the solution for any performance issue, but well used, it's really powerful!

### [9. Optimize search and score](./9-index_name_score.sql)
Write a SQL script that creates an index `idx_name_first_score` on the table `names` and the first letter of `name` and the `score`.

Requirements:
- Import this table dump: [names.sql.zip](https://intranet.alxswe.com/rltoken/9QL7kTH3VQKGbMB9Mba-Lw) 
- Only the first letter of `name` AND `score` must be indexed

### [10. Safe divide](./10-div.sql)
Write a SQL script that creates a function `SafeDiv` that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

Requirements:
- You must create a function
- The function `SafeDiv` takes 2 arguments:
    - a, INT
    - b, INT
- And returns a / b or 0 if b == 0

### [11. No table for a meeting](./11-need_meeting.sql)
Write a SQL script that creates a view `need_meeting` that lists all students that have a score under 80 (strict) and no `last_meeting` or more than 1 month.

Requirements:
- The view `need_meeting` should return all students `name` when:
    - They score are under (strict) to 80 
    - AND no `last_meeting` date OR more than a month

### [12. Average weighted score](./100-average_weighted_score.sql)
Write a SQL script that creates a stored procedure `ComputeAverageWeightedScoreForUser` that computes and store the average weighted score for a student.

**Requirements:**
- Procedure `ComputeAverageScoreForUser` is taking 1 input:
    - `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)

**Tips:**
- [Calculate-Weighted-Average](https://intranet.alxswe.com/rltoken/EOSSN309D1yK65IiM6OkIA)

### [13. Average weighted score for all!](./101-average_weighted_score.sql) 
Write a SQL script that creates a stored procedure `ComputeAverageWeightedScoreForUsers` that computes and store the average weighted score for all students.

**Requirements:**
- Procedure `ComputeAverageWeightedScoreForUsers` is not taking any input.

**Tips:**
- [Calculate-Weighted-Average](https://intranet.alxswe.com/rltoken/EOSSN309D1yK65IiM6OkIA) 

```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

Use "container-on-demand" to run MySQL
- Ask for container Ubuntu 18.04 - Python 3.7
- Connect via SSH
- Or via the WebTerminal
- In the container, you should start MySQL before playing with it:
```
$ service mysql start
 * MySQL Community Server 5.7.30 is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password: 
Database
information_schema
mysql
performance_schema
sys
$
```
- In the container, credentials are `root/root`

How to import a SQL dump

```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

