# Some basic SQL commands
Now we will study some `PostgreSQL`commands. To interact with the database directly, we must enter the database withe the `psql "name"` command. If you registered your linux user as a user of the database this is enough. But if you didn't do that you must change to a database user with `sudo -iu postgres` and then enter the database with the initial command.

### Creating tables
To create a new table in the database we use the command:

```sql
CREATE TABLE table_name (column_1 datatype, column_2 datatype, column_3 datatype);
```

\*Don't forget the semicolon on the end of the line.

In the `datatype` you must specify the type of the data that will be saved. Those can be:
- smallint (2byte integer)
- int (4byte integer)
- integer (4byte integer)
- bigint (8byte integer)
- real (4byte single precision floating-point number)
- double precision (8byte double precision floating-point number)
- money (currency value)
- timestamp (date and time)
- date (date in the YYYY-MM-DD format)
- xml (xml data)
- json (textual json data)
- jsonb (binary json data)
- character [(n)] (fixed-length character string)
- boolean (bool)
- text (variable length character string)
- cidr (ipv4 or ipv6 network address)
- cidr (ipv4 or ipv6 host address)

And there is much more. You can see those in https://www.postgresql.org/docs/9.5/datatype.html . Aside than that. we have the `table_name` and `table_column` that are respectively the tables name and column identifier.

After executing the command you can check the existing tables with the `\d` command. Here is an example of output:

```
            List of relations
 Schema | Name  | Type  |      Owner      
--------+-------+-------+-----------------
 public | users | table | felipejoribeiro
(1 row)
```
And finally, if you want to leave the shell, just execute the `\q` command.

### Insert information in an SQL table.
Now, to insert information in the table that we just created we must use the following command:

```sql
INSERT INTO table_name (column_1, column_2, column_3) VALUES (value_1, value_2, value_3);
```
So, the `table_name` argument specify the table to insert information, the `column` arguments specifies what columns to populate with data and the `value` arguments inform the data. If you don't populate all columns with information it will be put `NULL` in their fields.


### Query information from SQL table.

You can check the info that is in the table in the terminal with the following command:

```sql
SELECT column_1, column_2, column_3 FROM table_name;
```

With the `column` arguments you can specify the columns from which you want information along side the name of the table in the database. here goes an output:

```
 name  | age |  birthday  
-------+-----+------------
 felipe |  24 | 2972-20-55
 felipe |     | 2986-20-56
(2 rows)
```

Note that one of the database info elements is `NULL`. To query all columns you can use the `*` argument. like, with the `SELECT * FROM table_name;` command.


### Alter the table.
If you need to add a new column to your table you will use the following command:

```sql
ALTER TABLE table_name ADD column_name data_type;
```

So you need to specify what table to alter, the `ADD` opperation, the name of the new column and the datatype. The new column will be added and all existing rows will stay with `NULL` in this field.


### Update values in the table.
To update information in the table, so, to put new information in an existing row by replacing the existing information, the following command is used:

```sql
UPDATE table_name SET column_name = value_1 WHERE column_name = value_2;
```

So, the `value_1` is the information that will be stored and the `value_2` is used to identify the row where the information will be stored. It is interesting that the rows that where edited where sent to the end of the database. This is important because means that the row indice isn't a good identificaton as it can change.

Here goes another example:

```sql
UPDATE table_name SET column_name = value_1 WHERE column_name = value_2 OR column_name_2 = value_3;
```

In this case all rows that satisfies these two requirements will be updated. You can use the `AND` command too to make the query more specific. You can refer to the same column too but with more then one value to select two rows to be modified based in information from the same column.

### Advanced text based selections.

But what if we need to be more specific? Like, what if i need data from all users whose initial letter of the name is `A`? We can execute the command:

```sql
SELECT * FROM table_name WHERE column_name LIKE 'A%';
```

So the percentage sign indicates any amount of text. Other important operator is the `_` (underline). It indicates a single character. So to select all names whose the second letter is `R` we can use the `_R%` selection, for example.

### Sorting the results.
You can sort the results in order by giving a colum to use as parameter in the following manner:

```sql
SELECT * FROM table_name ORDER BY column_name DESC;
```

So this command, besides returning the information, it sorts the results in decreasing order in relation to the column which the name was specified in the function. To sort in the ascending order we use the `ASC` argument in the place of the `DESC`.

### Taking mathematic values from numerical data.
To take the average value from a group of numerical data it's farilly simple. Just execute the following command:

```sql
SELECT AVG(column_name) FROM users;
```


This will return the average value of the column_name stored values. You can specify from where to calculate too, with the `WHERE` command. To take the sum of the numbers you can use the `SUM()` command and to take the number of entries you can use the `COUNT()` command. This last can be used in strings too.


### Deleting rows or table from the database.
For deleting entries from the database we can use the `DELETE` command as follows:

```sql
DELETE FROM table_name WHERE column_name = "Fábio";
```

To delete the table we can we use the `DROP` command:

```sql
DROP TABLE table_name;
```

