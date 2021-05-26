# How to connect different tables?
Now we will see operations with more than one table. For that we use a primary key and a foreign key.

First we can create the following table:

```sql
CREATE TABLE login (
	ID serial NOT NULL PRIMARY KEY,
	secret VARCHAR(100) NOT NULL,
	name text UNIQUE NOT NULL
);
```

At first, we have the `ID` column, with type `serial` that is an Auto-incrementing integer value. Every time a new user is created this value is incremented. The `NOT NULL` parameter is to make sure that all rows have an `ID` value. And seting something as a primary key, it is saying that when we are looking for something this will be used as the main selector.

The `secret` column is of type `VARCHAR` that is a string with a determined number of characters (could be the hash). It also is required for the existence of a ROW. And finally, the `name` column is of type `text` that is a string of any size and is `UNIQUE`, which determine that it wont exist duplicates of names in the database, it will not accept repeated names. And it has the `NOT NULL` parameter as well.

When inserting a value in this table we can make the following command:

```sql
INSERT INTO login (secret, name) VALUES ('abc', 'Andrei');
```
Notice that we don't specifies an `ID` as it will be generated for us. Any data from the database can be used as a foreign key. We will se that now.

### Foreign keys
Imagine we have two tables in the same database:

```
test=# SELECT * FROM login;
 id | secret |  name  
----+--------+--------
  1 | abc    | Andrei
  2 | abc    | Mandir
  3 | abc    | feipe
```

```
test=# SELECT * FROM users;
  name  | age |  birthday  | score 
--------+-----+------------+-------
 feipe  |  10 | 1996-10-13 |    50
 feipe  |  10 | 1996-10-13 |    50
 Andrei |  10 | 1996-10-13 |    60
 Mandir |  11 | 1396-10-13 |    60
```

These two databases can interact with one another. For example, with the following command:

```sql
SELECT * FROM table_1 JOIN table_2 ON table_1.column_name = table_2.column_name;
```

if we run the following command for both previously mentioned tables, we receive:

```
test=# SELECT * FROM users JOIN LOGIN ON users.name = login.name WHERE login.name  = 'feipe';
 name  | age |  birthday  | score | id | secret | name  
-------+-----+------------+-------+----+--------+-------
 feipe |  10 | 1996-10-13 |    50 |  3 | abc    | feipe
 feipe |  10 | 1996-10-13 |    50 |  3 | abc    | feipe
(2 rows)
```


This command will take all elementes from the union of both `users` and `login` tables using the `name` column in both to sync the rows. Thing is that each table can have unique data restrictions. We can imagine a table named `twits` that have all twits from every user and there they are identified by the ID. We can receive all twits from a user by using the `JOIN` command with the `users` table with the `twits` table.

