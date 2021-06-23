# First basic application
Here we will create a basic first flask application. In all flask applications you must create an application instance, for which the web server passes all requests it receives from clients. It uses a protocol called Web Server Gateway Interface (WSGI, pronounces "wiz-ghee"). The application is a instance of the flask class. It can be created with:

```python
from flask import Flask
app = Flask(__name__)
```

Flask uses the `__name__` argument to locate the application, which allows it to locate other files that are part of the application. You can use other things in this input, but for simple applications this is all that is needed.

## Routes and view functions
The rout is how you tell tell the application what to do for each request. This is done by associating each address with a function. This can be done with a decorator, as follows:

```python
@app.route('/')
def index():
	return '<h1>Hello World!</h1>'
```

Decorators are functions that take your functions as input and returns an extended version of it. The previous function is called in the root url. There is another way of doing this too, as follows:

```python
def index():
    return '<h1>Hello World!</h1>'
app.add_url_rule('/', 'index', index)
```
The function `add_url_rule()` takes the addres, end point name and function as inputs.

Functions like these, called from the `URL` are called **view function**. The return value from the view function is what the browser receives as response from the request. This response can be a simple text with `HTML` content, or more complex forms as we will see ahead. Embedding html code directly in your python code leads to code that is difficult to maintain. A better way to tho this will be discussed further.

Routes can have dynamic addresses as well. Like when you see your username in your `Facebook` profile page. The following example has a implementation of such feature:

```python
@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, {}!</h1>'.format(name)
```

The text in the `URL` in the place of the dynamic part will enter the function as an input. In this case in the `name` variable. These are `strings` by default, but can have different types if you declare it with `/user/<int:id>` for example. Flask supports these types: `string`, `int`, `float` and path for routes. The path type is a special string type that can include forward slashes, unlike the string type.

Here we have a minimal functional basic flask application:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
```

If you get the `AttributeError: module 'importlib._bootstrap' has no attribute 'SourceFileLoader'` error, maybe your python version is off, or a lib maybe. 

To run the app, just run the following commands: `export FLASK_APP=hello.py` and `flask run`.

There is other way another way of initiating the development server, with .

If everything is ok you can enter the provided link and see your `/` endpoint. If you try to access any other, it will result in an `404 - not found` page. This way of serving the the app is intended just for development. The proper way of serving in production will be discussed further.









