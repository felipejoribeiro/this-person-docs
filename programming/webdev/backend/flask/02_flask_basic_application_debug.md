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

There is other way another way of initiating the development server. First you will have to include in your code the following:

```python
if __name__ = "__main__":
    app.run()
```
Than you can run the development server by runing this code with `python app.py`.

If everything is ok you can enter the provided link and see your `/` endpoint. If you try to access any other, it will result in an `404 - not found` page. This way of serving the the app is intended just for development. The proper way of serving in production will be discussed further.

## Dynamic routes
It's possible to have dynamic `url` with conditional behavior. This allows the developer to interact with the page address treating elements of it as variables. You can se the method in the following code:

```python
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
```

And the routes can be added without problem. The only thing that you must pay attention is to not make two identicall routes. Other important thing to take notice is that the `/` route is simply the base `url`. So if you host your application in under a domain name only the domain name in the address will call this route.

## Debug mode
Flask has a debugging mode that will reload the page when you edit some source file and will show you the error in the browner when something goes wrong. These two modules are not active by default To activate this feature you must set the `FLASK_DEBUG` environment variable. Like as follows:

```bash
export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run
```
So, with these commands you will initiate the development server with de debug mode enabled. If you use the `app.run()` method than you will need to insert the right flags as follows:

```python
app.run(debug=True)
```

And then just execute the script with `python app.py`.

Never activate the debugger in a production server. The debugger allows the client to request remote code execution, so it makes the production server vulnerable to attacks. As a simple protection measure, the debugger needs to be activated with a PIN, printed to the console by the flask run command.

## Command line options
There are numerous options then running `flask run`. These options allows the developer to personalise the running server to an extent. You can see all available options with the `flask --help` command.

One command that is very usefull is the `flask shell` command. With this line of code you can open a shell in the context of the running application and interact with it. This is usefull for debugging, tests and maintenance.

To se the `flask run` options you can run `flask run --help`. Some information reggarding the development server will be exposed, like how, by deffault, it will not support any sort of concurrency just to simplify debbuging. This can be changed with a `--with-threads` flag after the command. The `--host` flag is particularly usefull as it tells the web server what network interface to listen to for connections from clients. By default this value is set to `localhost`. So only connections originated in the computer running the server are accepted. The following command enables other computers in the public network to connect to the server:

```bash
flask run --host 0.0.0.0
```
Now the server is accessible for any computer in the public network. In the `http://<IP>:5000` address.
There are flags to control the reload functionality and the debbuging functionality as well.



