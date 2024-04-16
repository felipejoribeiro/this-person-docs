# Flask Request-Response cycle
Now we must see how flask do things under the hood. Here we will see some design aspects regarding the framework.

## Application and request context
When a client makes a request, flask creates some objects for the `view functions` that will handle the request. An example is the `request` object, which encapsulates the `http` request that came in. This isn't done by arguments in the view function, as not every view function will need these objects and adding then to every view function would not be ideal. In place of that, what flask uses `contexts` to temporally make certain objects globally accessible. So the following code is possible:

```python
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)
```

This globally available `request` object doesn't affect other threads as it is created in the context of the running thread. Each request gives birth to a process in the thread pool available in the server (When this option is enabled).

There are two contests to variables in a `flask` app. Here they are:


| variable name | Context | Description
| - | - | -
| current_app | Application context | The application instance for the active application.
| g | Application context | An object that the application can use for temporary storage during the handling of a request. This variable is reset with each request.
| request | Request context | The request object, which encapsulates the contents of an `HTTP` request sent by the client.
| session | Request context | The user session, a dictionary that the application can use to store values that are "remembered" between requests.

Flask activates (or pushes) the application and request contexts before dispatching a request to the application, and removes them after a request is handled. When the application context is pushed `g` and `current_app` becomes available to the thread, likewise, when the request context is pushed, `request` and `session` become available as well. If you try to access then in a context other then a request or an applications an error will occur.

The following python shell commands show how this work:

```python

>>> from hello import app
>>> from flask import current_app
>>> current_app.name
Traceback (most recent call last):
...
RuntimeError: working outside of application context
>>> app_ctx = app.app_context()
>>> app_ctx.push()
>>> current_app.name
'hello'
>>> app_ctx.pop()
```

So these context are created and dispatched on each thread.

## Request dispatching
When a request comes to the server the flask server looks at it's `URL map` which contains a mapping of addresses to view functions. This is done in the `app` script. You can see this by running a python shell and doing the following:

```python
(venv) $ python
>>> from hello import app
>>> app.url_map
Map([<Rule '/' (HEAD, OPTIONS, GET) -> index>,
 <Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
 <Rule '/user/<name>' (HEAD, OPTIONS, GET) -> user>])
```
The `/static/` route is a special route create by `flask` to give access to static files. You can se the `http` request method as well with `(HEAD, OPTIONS, GET)`. This sinilise that the view function is called when a `GET` command is sent to the specified route. `HEAD` and `OPTIONS` methods are assign automatically to each route.

## The request object
So flask will expose the `request` object as a context variable named `request`. This has all information that the client included in the `HTTP` request. Here we have some useful attributes:

|Attribute or Method | Description
|-|-
|form|A dictionary with all the form fields submitted with the request.
|args|A dictionary with all the arguments passed in the query string of the URL.
|values|A dictionary that combines the values in form and args.
|cookies|A dictionary with all the cookies included in the request.
|headers|A dictionary with all the HTTP headers included in the request.
|files|A dictionary with all the file uploads included with the request.
|get_data()|Returns the buffered data from the request body.
|get_json()|Returns a Python dictionary with the parsed JSON included in the body of the request.
|blueprit|The name of the Flask blueprint that is handling the request. Blueprints are introduced in Chapter 7.
|endpoit|The name of the Flask endpoint that is handling the request. Flask uses the name of the view function as the endpoint name for a route.
|method|The HTTP request method, such as GET or POST.
|scheme|The URL scheme (http or https).
|is_secure()|Returns True if the request came through a secure (HTTPS) connection.
|host|The host defined in the request, including the port number if given by the client.
|path|The path portion of the URL.
|query_string|The query string portion of the URL, as a raw binary value.
|full_path|The path and query string portions of the URL.
|url|The complete URL requested by the client.
|base_url|Same as url, but without the query string component.
|remote_addr|The IP address of the client.
|environ|The raw WSGI environment dictionary for the request.

## Request hooks
Some times there's code that must be executed before or after a request. For example, maybe we must create a database connection or authenticate the user making the request. Instead of duplicating the code in every single view function we can use these functions that flask will always call before or after a request is despatched. These are implemented as decorators. The most important are:

- `before_request`: Registers a function to run before each request.
- `before_first_request`: Registers a function to run only before the first request is handled. This can be a convenient way to add server initialization tasks.
- `after_request`: Registers a function to run after each request, but only if no unhandled exceptions ocurred.
- `teardown_request`: Registers a function to run after each request, even if unhandled exceptions occurred.

A commom pattern to share data between request hook functions and view functions is to use the `g` context global as storage. For example, a before_request handler can load the logged-in user from the database and store it in `g.user`. Then the view function can retrieve the information from this variable.

## Response 
When a view function is called flask expects that the function will return the response. This can be a simple string that will return as `html` to the client browser. Other important thing is the `status code` which flask by default sets to `200` that indicates that the request was a success.
To change the response status code you just has to return it as a second argument in the response, as follows:

```python
@app.route('/')
def index():
    return '<h1>Bad Request</h1>', 400
```

In this case we have a `400` that indicates an error. You can add a third argument, that is a dictionary of headers that are added to the `http` response.

Other option to configure the response of a view function is the `make_response()` function. It can be used as follows:

```python
from flask import make_response
@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>', 200)
    response.set_cookie('answer', '42')
```

In this case we can send a cookie to the browser. The `make_response()` creates a object that can be further configured with some methods. And in the function call you can express the third argument as well to append things to the header of the response. But other thins are possible calling the methos and attributes of the `response` object as we can se in the table ahead:

|Attribute or method | Description 
|-|-
|status_code|The numeric HTTP status code
|headers|A dictionary-like object with all the headers that will be sent with the response
|set_cookie()|Adds a cookie to the response
|delete_cookie()|Removes a cookie
|content_length|The length of the response body
|content_type|The media type of the response body
|set_data()|Sets the response body as a string or bytes value
|get_data()|Gets the response body

There is a special response called `redirect` that is used a lot. To address that the flask team created a dedicated function that is `redirect()` which gives a response with `302` status code and the `URL` to navigate to. Here we can see it in use:

```python
from flask import redirect
@app.route('/')
def index():
    return redirect('http://www.example.com')
```

Other special response is teh `abort()` function, which is used for error handling. The following code returns a `404` error when the given user `url` isn't a valid user:

```python
from flask import abort
@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, {}</h1>'.format(user.name)
```




