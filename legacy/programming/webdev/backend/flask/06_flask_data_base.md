# Flask and data bases
Databases organize data and a program can access then via query when needed. There are the `relational` database and the `No relational` database, known respectively as `SQL` and `NoSQL` databases that differs in the query language they use.

## SQL databases
These databases stores data in tables, which model the different entities in the application's domain. That is, for a management table, probably there will have definitions for users, orders and products tables. This `table` has a fixed number of columns and many rows as necessary. So a costumers table will have information about the costumers, like name, email and password hash. Each row is a data nuget that is what the table is about.

These tables have a special column named `primary key`, which stores a unique identifier for each row stored in the table. They can also have columns called `foreign keys` which reference the primary key of a row in the same o other table. These links between tables are called `relationships` and are the foundation of relational databases.

Check this example:


```
     ._________.      .___________.
     |  roles  |      |   users   | 
     |_________|      |___________|
     | id      |-|-+  | id        |
     | name    |   |  | username  |
     |         |   |  | password  |
     |         |   +-<| role_id   |
     .---------.      .-----------.

```

This graphical style is called `entity-relationship diagram`. It lists the columns of the databases and express its foreign relations. The `-|` sign in the arrow indicates that only one element from the roles table is involved in this relationship. And the `-<` sign signifies that multiple elements from the `users` table can have this reference. If the relation were one for one, then both would be `-|`, for example.

## NoSQL databases
These are databases that do not follow the relational model described before. A common organization method used instead is the `collections` and `documents` model, that replaces tables by the former and records by the latter. This design patter make joins difficult, so most of then do not support this operation. So this operation must be done in the application itself, by takin the `role_id` in one table and making a new `query` in the other (assuming a situation like the last example).
A common countermeasure is to use just one database and have duplicate information, but avoid multiple related tables.

## Comparing these two types
The principal difference between these two is that the `SQL` database follows the `ACID` paradigm that implies Atomicity, Consistency, Isolation and Durability, which makes the database extremely reliable. But that comes with a performance cost. But for medium size applications both are very performant and capable.

## Databases and python
Python has libraries to deal with all sorts of databases, opensource or commercial. Flasks puts no restrictions on what database packages can be used, so you can chose at will.

There are also a number of database abstraction layer packages, such as `SQLAlchemy` or `MongoEngine`. That allows the developer to work with higher level with regular python objects instead of database entities such as tables, documents and query languages.

There is a number of things to evaluate when choosing a database framework:
- *Ease of use*: When comparing straight database engines and database abstractions, the second group wins. These abstractions are called `object-relational mappers` (ORMs) or `object-document mappers` (ODMs). They convert high level object-oriented operations to low level database instructions.

- *Performance*: There is an overhang when using `ORMs` and `ODMs`, but in most cases that is negligible, and the gains in productivity make it justifiable. The best thing is to chose an abstraction layer that supports access to the underlying database in case specific operations. So when the performance impact is measurable then you can ponder about use the direct instructions.

- *Portability*: You must pay attention on what database frameworks are available in the plataforms you are headed to deploy your application. Choosing the most popular is a safe move.

- *Flask integration*: Choosing a database that integrates well with flask is advised too. This is good to avoid the developers to write integration directives thenselves. So checking the availability of packages is a good practice.

## Flask-SQLAlchemy
The `Flask-SQLAlchemy` ia a flask extension that simplifies the use of `SQLAlchemy` inside the application. You can install teh package with pip:

```bash
pip install flask-sqlalchemy
```

The database is specified as a `URL`. Here are some examples of declaring the database:

| Database engine       | URL
| -                     | -
| MySQL                 | mysql://username:password@hostname/database
| Postgres              | postgresql://username:password@hostname/database
| SQLite (Linux, macOS) | sqlite:////absolute/path/to/database
| SQLite (Windows)      | sqlite:///c:/absolute/path/to/database

In the `URL` you must specify the `hostname` that refers to the server where the database is hosted (this could be `localhost`, for example). There is the name of the database too in the url. For databases that require authentication you must send the `username` and `password` as well.

This `URL` must be configured as the key `SALALCHEMY_DATABASE_URI` in the flask configuration object. The lib documentation also suggests setting the key `SQLALCHEMY_TRACK_MODIFICATIONS` to `false` to use less memory, unless signals for object changes are needed. There are more configuration options in the documentation.

```python
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

```

The db object instantiated from the class SQLAlchemy represents the database and provides access to all the functionality of Flask-SQLAlchemy.

## Model definition
`Model` is the persistent entities used by the application. In the context of `ORM`, a model is typically a Python class with attributes that match the columns of a corresponding database table.

`Flask-SQLAlchemy` provides a base class with methods and other helper classes that are used to define the data structure.
The `users` and `roles` example could be defined as follows:

```python
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    def __repr__(self):
        return '<User %r>' % self.username
```

It's always good to name your tables as the default name don't follow good conventions.

The first argument in the `db.Column()` method is th type of the database column and model attribute. Here goes the available ones:

| Type name    | Python type             | Description
| -            | -                       | -
| Integer      | int                     | Regular integer, typically 32 bits
| SmallInteger | int                     | Short-range integer, typically 16 bits
| BigInteger   | int or long             | Unlimited precision integer
| Float        | float                   | Floating-point number
| Numeric      | decimal.Decimal         | Fixed-point number
| String       | str                     | Variable-length string
| Text         | str                     | Variable-length string, optimized for large or unbounded length
| Unicode      | unicode                 | Variable-length Unicode string
| UnicodeText  | unicode                 | Variable-length Unicode string, optimized for large or unbounded length
| Boolean      | bool                    | Boolean value
| Date         | datetime.date           | Date value
| Time         | datetime.time           | Time value
| DateTime     | datetime.datetime       | Date and time value
| Interval     | datetime.timedelta Time | interval
| Enum         | str                     | List of string values
| PickleType   | Any Python object       | Automatic Pickle serialization
| LargeBinary  | str                     | Binary blob

The remaining arguments specify configuration options for each attribute:

| Option name | Description
| -           | -
| primary_key | If set to True, the column is the table’s primary key.
| unique      | If set to True, do not allow duplicate values for this column.
| index       | If set to True, create an index for this column, so that queries are more efficient.
| nullable    | If set to True, allow empty values for this column. If set to False, the column will not allow null values.
| default     | Define a default value for the column.

Flask requires that all models have defined a primary key column. It's commonly named id. Notice that both models include a `__repr__()` method to give them a readable string representation that can be used for debugging and testing purposes.

## Relationships
Relationships can be implemented here as well. Here we can use the example of the `users` and `roles` again. Check how it would be implemented in flask_sqlalchemy:

```python
class Role(db.Model):
    # ...
    users = db.relationship('User', backref='role')

class User(db.Model):
    # ...
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
```
Here, the `role_id` column is added to the `User` table as a `foreign key`. The `roles.id` argument in `db.ForeignKey()` specifies that the column should be interpreted as having id values from rows in the roles table. The `users` attribute added to the `Role` model represents the object-oriented view of the relationship. Given an instance of the `Role` class, the users attribute will return the list of users associated with that role (so, the other way around).

Some times the `db.relationship()` can locate the relationship's foreign key on its own, but sometimes it cannot. There are configuration options to this function as well:

| Option name   | Description
| -             | -
| backref       | Add a back reference in the other model in the relationship.
| primaryjoin   | Specify the join condition between the two models explicitly. This is necessary only for ambiguous relationships.
| lazy          | Specify how the related items are to be loaded. Possible values are select (items are loaded on demand the first time they are accessed), immediate (items are loaded when the source object is loaded), joined (items are loaded immediately, but as a join), subquery (items are loaded immediately, but as a subquery), noload (items are never loaded), and dynamic (instead of loading the items, the query that can load them is given).
| uselist       | If set to False, use a scalar instead of a list.
| order_by      | Specify the ordering used for the items in the relationship.
| secondary     | Specify the name of the association table to use in many-to-many relationships.
| secondaryjoin | Specify the secondary join condition for many-to-many relationships when SQLAlchemy cannot determine it on its own.

There are other types other relationships besides `one-to-many` as this one. One example is the `one-to-one` relationship, and it can be implemented using `one` in the place of `many` in the previous example. There is an aditional type, more complex, called `many-to-many` that needs a third table to describe the relations. It will be better discussed ahead.

## Database operations 
Now we will explore some database operations via `flak shell`. Make sure that the environment variable `FLASK_APP` is set to the proper app before calling the shell.

## Creating new tables
First we must create the databases. The `db.create_all()` method locates all the subclasses of `db.Model` and creates corresponding tables in the database for them.

```python
from hello import db
db.create_all()
```

By default it creates a `SQLite` database.

## Inserting rows
Now we can create a few `rows` in `Users`:

```python
from hello import Role, User

admin_role = Role(name='Admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')

user_john = User(username='john', role=admin_role)
user_susan = User(username='susan', role=user_role)
user_david = User(username='david', role=user_role)
```
These data weren't written to the database yet and just exist in memory. To do that you must perform the following opperations:

```python
db.session.add(admin_role)
db.session.add(mod_role)
db.session.add(user_role)
db.session.add(user_john)
db.session.add(user_susan)
db.session.add(user_david)
db.session.commit()
```
Then it will write the information in nonvolatile memory. If an error occur while the session is being written, the whole session is discarded. This is good as avoid partial updates in the database that would lead to database inconsistences.

You can call `db.session.rollback()` too, if you want to trash all modifications present in the present session. 

## Modifying rows
The `add()` method can be also used to update models. This can be done with the following instructions:

```python
admin_role.name = 'Administrator'
db.session.add(admin_role)
db.session.commit()
```

## Deleting rows
There is also a `delete()` method. The following code deletes the `Moderator` role from the database:

```python
db.session.delete(mod_role)
db.session.commit()
```
Notice that the change, as always must be committed.

## Querying Rows
There is a `query` object that the `Flask-SQLAlchemy` makes available for each model. The most basic one is the following, which returns the entire contents of the table:

```python
Role.query.all()
User.query.all()
```
But, you can make the search more specific with the help of the `filter_by`. The following code has an example:

```python
User.query.filter_by(role=user_role).all()
```
It's possible to inspect the native `SQL` command that was issued as a string:

```python
str(User.query.filter_by(role=user_role))
```

Here is an output example:

```
'SELECT users.id AS users_id, users.username AS users_username,
users.role_id AS users_role_id \nFROM users \nWHERE :param_1 = users.role_id'
```

## Loading existing databases
Not always you want to create stuff. If you just initiated an app and just want to load information from the databases. Here is the command:

```python
user_role = Role.query.filter_by(name='User').first()
```

So here we loaded just the first result and not `all()`. If the query don't find results it will return `None`. Multiple filters can be performed in chain to better describe what is the required data. There are a number of fiters too, as follows:

| Option      | Description
| -           | -
| filter()    | Returns a new query that adds an additional filter to the original query
| filter_by() | Returns a new query that adds an additional equality filter to the original query
| limit()     | Returns a new query that limits the number of results of the original query to the given number
| offset()    | Returns a new query that applies an offset into the list of results of the original query
| order_by()  | Returns a new query that sorts the results of the original query according to the given criteria
| group_by()  | Returns a new query that groups the results of the original query according to the given criteria

Besides `all()` there are other query execution methods as follows:

| Option         | Description
| -              | -
| all()          | Returns all the results of a query as a list
| first()        | Returns the first result of a query, or None if there are no results
| first_or_404() | Returns the first result of a query, or aborts the request and sends a 404 error as the response if there are no results
| get()          | Returns the row that matches the given primary key, or None if no matching row is found
| get_or_404()   | Returns the row that matches the given primary key or, if the key is not found, aborts the request and sends a 404 error as the response
| count()        | Returns the result count of the query
| paginate()     | Returns a Pagination object that contains the specified range of results

Relationships function in a similar way to queries. The following example queries the `one-to-many` relationship between roles and users from both ends:

```python
>>> users = user_role.users
>>> users
>>> users
[<User 'susan'>, <User 'david'>]
>>> users[0].role
<Role 'User'>
```
Querying in this way has a small problem. It always does an `all()` internally to return the list of users. As the query operator is in hide, you can't refine the query with filters. 

To prevent this, we can add a additional configuration when creating the relationship:

```python
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # users = db.relationship('User', backref='role')   # old way
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name
```

With the `lazy` configuration the query will return a query that hasn't executed yet, so you can add filters and further configuration:

```python
>>> user_role.users.order_by(User.username).all()
[<User 'david'>, <User 'susan'>]
>>> user_role.users.count()
2
```

## Database use in view functions
Now we can perform these database operations in our view functions. Here goes an example of usage inside the `index()` view function described before:

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',
        form=form, name=session.get('name'),
        known=session.get('known', False))
```

So, here, each time a name is bubmitted the application checks for it in the database using the `filter_by()` query fileter. Remember to create the tables before tinker with then.

You can make the frontend have information about the save process as well:

```html
{% extends "base.html" %}
{% import "bootstrap/wtf.html" as wtf %}

{% block title %}Flasky{% endblock %}
{% block page_content %}
    <div class="page-header">
        <h1>Hello, {% if name %}{{ name }}{% else %}Stranger{% endif %}!</h1>
        {% if not known %}
        <p>Pleased to meet you!</p>
        {% else %}
        <p>Happy to see you again!</p>
        {% endif %}
    </div>

    {{ wtf.quick_form(form) }}
{% endblock %}
```

So if the name was present in the database the website will greet you accordingly.

## Integration with the python shell
Having to import the database instance and the models each time a shell session is started is loads of work. You can automatically import these objects.

You can add a `shell context processor` with the `app.shell_context_processor` decorator.
This is shown in the following example:

```python
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)
```

So, now, when you initiate a `flask shell` it will import these things without the need fo action.

## Database migrations with flask-migrate
There are moments when you have to alter a database. The only way of making a table the updated version of itself is by destroying it first. The harmless and most reliable method of doing this is with the `database migration framework`. It works similarly to a source code version controll, but it keeps track of the database schema, allowing incremental changes to be applied.

There is a framework called `Alembic` that was written by the `SQLAlchemy` developer. But dealing directly with it isn't necessary. For that you can use the `Flask-Migrate` extension. It is a `Alembic` wrapper that integrates it sinlessly with the flask command.
 
## Creating a Migration repository
First, we must install the tool with `pip install flask-migrate`. Then we must import it in our project with `from flask_migrate import Migrate`. And in the code you must do the following:

```python
from flask_migrate import Migrate

# ...

migrate = Migrate(app, db)
```

Now, when you work in a new project, you can add support for database migrations with the `init` subcommand:

```bash
(venv) $ flask db init
  Creating directory /home/flask/flasky/migrations...done
  Creating directory /home/flask/flasky/migrations/versions...done
  Generating /home/flask/flasky/migrations/alembic.ini...done
  Generating /home/flask/flasky/migrations/env.py...done
  Generating /home/flask/flasky/migrations/env.pyc...done
  Generating /home/flask/flasky/migrations/README...done
  Generating /home/flask/flasky/migrations/script.py.mako...done
  Please edit configuration/connection/logging settings in
  '/home/flask/flasky/migrations/alembic.ini' before proceeding.
```

This command create the directory where all the migration scripts will be stored. These files must be added to version controll along with the rest of the application, they are important.


## Creating a migration script
We represent a database migration in `Alembic` with a `migration script`. This script has two functions called `upgrade()` and `downgrade()`. The first applies the changes that are parte of the migration and the second remove then. This means that the `Alembic` tool can rewind history when necessary.

There are two ways of doing a migration, the fist is manual, and it creates a migration script skeleton with the `upgrade` and `downgrade` functions for the developer to write. And there is the automatically way, that instructs `Alembic` to look at the models in memory and figure it alt ways of changing the databases to conform to it. The the tool generate the code in the migration methods.

You must be cautious as this automatically generated scripts can have mistakes. An example is if you want to change a column name, and when generating the migration script, the tool deletes the column and creates a new one, and the data in the column is lost. So is good practice that even when you generate the migration script automatically, at least you must read the code before applying changes.

The following workflow is a good way of doing this:

1. Make the necessary changes to the model classes.
2. Create an automatic migration script with the `flask db migrate` command.
3. Review the generated script and adjust it so that it accurately represents the changes that were made to the models.
4. Add the migration script to source control.
5. Apply the migration to the database with the `flask db upgrade` command.

## Upgrading the database
Once a migration script has been reviewed and accepted, you can make the `flask db upgrade` command to performe the changes in the real database. For the first migration, this is effectively equivalent to calling `db.create_all()`, but in successive migrations the `flask db upgrade` command applies updates to the tables without affecting their contents.

If you already done the `db.create_all()` command you can take an error when trying to upgrade. To solve that you must mark the database as upgraded with the `flask db stamp` command.

## Adding more migrations
Then, when you are working in an application, you will find that you will need to make changes to the database very often, now that you already have done the fist, the other have a very similar workflow:

1. Make the necessary changes in the database models.
2. Generate a migration with the `flak db migrate` command.
3. Review the generated migration script and correct it if it has any inaccuracies.
4. Apply the changes to the database with the `flask db upgrade` command.

If you already did this, but didn't committed to version controll yet, you can expand the script to incorporate new changes as you make then. This will save you to have a lot of small migration scripts. The proceature is the following:

1. Remove the last migration from the database with the flask db downgrade com‐
mand (note that this may cause some data to be lost).
2. Delete the last migration script, which is now orphaned.
3. Generate a new database migration with the flask db migrate command,
which will now include the changes in the migration script you just removed, plus any other changes you've made to the models.
4. Review and apply the migration script as described previously.


