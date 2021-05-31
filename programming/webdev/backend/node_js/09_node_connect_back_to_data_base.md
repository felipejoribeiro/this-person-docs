# Connect your backend to the data base
Now, for better information storing, you need to connect your server to a database. For that we can use, yet, another `npm` package. You must install `knex.js`. It works with `Postgres`, `MSSQL`, `MyWQL`, `MariaDB`, `SQLite3` and `Oracle`. So it covers most relational databases and bring then directly to your javascript code. Other option is the `pg-promise` that enable simple `SQL` commands with the `SQL` syntax.
To install `Knex.js` you just need to run `npm install knex --save`. And as we are runing `postgreSQL` we need to install `pg` too with the `npm install pg` command.

To connect to the database you need to import the new library with the following arguments:

```javascript
var knex = require('knex') 

// Identifying the database
const database = knex({
	client: 'pg',
	connection: {
		host: '127.0.0.1',
		user: 'user_name',
		password: '',
		database: 'data_base_name'
	}
});
```

So we use the `pg` client as our database is `PostgreSQL` and we describe how to connect with the database. Note that this is the same information that we must enter in the `DBeaver`.

To make `SQL` commands one need to use the following syntax:

```javascript
database.select('*').from('data_base_name').then(data => {
  console.log(data);
});
```

So that already makes a `SELECT` command. The builder responds with a promisse that we can handle with a `then()` javascript command. The response comes with a list of selected data. It's important to notice that  in another example, we can se how to insert new values:

```javascript
pg.insert({
    column: data,
    column: data,
    column: data
  })
  .into('data_base_name')
  .returning('column')
  .then(column_returned => {
    res.json(column_returned[0]);
  })
  .catch(error => {
    console.log(error);
  })
```

So with this command we add values to our database with the information to each column defined by us. It returns the column specified, but remember that it returns a list, so you need to specify the indice even if there is only one element, we do this in this case with `[0]`.  Each end point in the restfull `API` is concerned with a type of operation most of witch involve database manipulation.

```javascript
pg('data_base_name').where('column_name', '=', value)
  .increment('column_name', 1)
  .returning('column_name')
  .then(response => {
    res.json(response);
  })
  .catch(_ => {
    res.status(400).json("error");
  })
```

With this command you can increment the numerical value on the specified column. Then you can return the new value and check the status of the response. If there isn't any one with the specified `column_name` `value` in the data base the response will be an empty list. So you can check it in the response part.

```javascript
pg.transaction(trx => {
  trx.insert({
    column_name: value,
    column_name: value
    })
    .into('data_base_1')
    .returning('column_name')
    .then(value_returned => {
      trx('data_base_2')
        .returning('*')
        .insert({
          column_name: value_returned,
          column_name: value,
          column_name: value
        })
        .then(data => {
          res.json(data[0]);
        })
        .catch(_=> {
          res.status(400).json('unable to register')
        })
    })
    .then(trx.commit)
    .catch(_ => {
      res.status(400).json("error");
    })
})
```

This last operation is called a transaction and it is important as it permits creating two requests to more than one database and both operations are done only both operations are done. So this is very important when we are dealing with relational databases as avery entry in one database must have an analogous entry in the other. Notice that there is a column that existis in both databases, so we passa the information stored in one of then as input of the other to assure that we are saving the same information. If the operation in one of the databases fail both will be canceled.
