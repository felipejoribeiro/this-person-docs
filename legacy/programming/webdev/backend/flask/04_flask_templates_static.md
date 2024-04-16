# Flask Templates
The flask view functions have two distinct purposes disguised as one, which creates a problem. The first purpose of a task is to generate a response to a request. For simple requests this is enough. But, there are many situations where a request triggers a change in the state of the application, and the view function is the location where this happens.

An example is when a user registers himself. The request comes with the `form` information. Then the view function submits this information to a database and then generates a response to inform if the account was properly created. These two tasks are formally called `business` logic and `presentation` logic respectively. Keep both together is prone to error. The best alternative is using templates.

The templates are files containing the text of a response with placeholder variables for the dynamic parts that will be known from the request. The process that replaces these variables with the actual values and returns a final response is called `rendering`. For this process flask uses the `Jinja2` engine.

## The Jinja2 template engine
In its simplest form, a Jinja2 template is a file that contains the text of a response. An example of this dynamic template can be seen ahead:

```html
<h1>Hello, {{ name }}!</h1>
Rendering Templates
```

By default these templates are found in a `templates` subdirectory that is inside the apps main directory. Than, if you want to show one of these templates, just implement the following syntax in your code:

```python
from flask import Flask, render_template

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
```

So now we can separate the visual part of the app from the logic. The `render_template()` function integrates with the Jinja2 engine. The first argument takes the template location and from the second up you can send the variables that will be replaced in the text.

## Variables
When you place `{{ name }}` in your template you are telling Jinja2 to find the `name` variable in the function declaration. The engine recognizes variables of any type, even complex types like lists dictionaries and objects. Here are some examples:

```html
<p>A value from a dictionary: {{ mydict['key'] }}.</p>
<p>A value from a list: {{ mylist[3] }}.</p>
<p>A value from a list, with a variable index: {{ mylist[myintvar] }}.</p>
<p>A value from an object's method: {{ myobj.somemethod() }}.</p>
```

Variables can be modified with filters like in the following example where we capitalize the text:

```html
Hello, {{ name|capitalize }}
```
Here we have the commonly used filters that come with Jinja2:

|Filter name|Description
|-|-
|safe|Renders the value without applying escaping
|capitalize|Converts the first character of the value to uppercase and the rest to |lowercaselower |Converts the value to lowercase characters
|upper |Converts the value to uppercase characters
|title| Capitalizes each word in the value
|trim|Removes leading and trailing whitespace from the value
|striptags|Removes any HTML tags from the value before rendering



The safe filter is important as Jinja2, by default, `escapes` all variables for security purposes. For example, if a variable is set to `<h1>Hello</h1>`, Jinja2 will render the string as `&lt;h1&gt;Hello&lt;/h1&gt;`, So the text will only be a string and will not be interpreted by the browser. With the `safe` filter it will pass the `html` code to be interpreted, but this is insecure if you are dealing with something the user has submitted, so use with caution.

## Control structures
There are ways of controlling the execution flow in your template code and render somethings conditionally. The following example shows how:

```html
{% if user %}
    Hello, {{ user }}!
{% else %}
    Hello, Stranger!
{% endif %}
```

Another common need in template is to render a list of itens based in a logical list of a input variable. This can be done in template too with the following snippet:

```html
<ul>

    {% for comment in comments %}

        <li>{{ comment }}</li>

    {% endfor %}

</ul>
```

Jinja2 also supports `macros` that are similar to functions in python. Check this example:

```html
{% macro render_comment(comment) %}
    <li>{{ comment }}</li>
{% endmacro %}

<ul>
    {% for comment in comments %}
        {{ render_comment(comment) }}
    {% endfor %}
</ul>
```

You can store these macros in standalone files that are then imported from all the templates that need them:

```html
{% import 'macros.html' as macros %}
<ul>
    {% for comment in comments %}
        {{ macros.render_comment(comment) }}
    {% endfor %}
</ul>
Portions of template code that need to be repeated in several
```

Portions of `html` code that are used over and over again can be stored in separated files to and included  when necessary to avoid repetition:

```html
{% include 'common.html' %}
```

Other option is the creation of templates with inheritance. These smart templates are like python classes. So first, we create a `base.html` template as follows:

```html
<html>
<head>
    {% block head %}
    <title>{% block title %}{% endblock %} - My Application</title>
    {% endblock %}
</head>
<body>
    {% block body %}
    {% endblock %}
</body>
</html>
```
Then, these `blocks` can be overridden by derived templates. These block directives determine where additional content will go. In this example we have the `head`, `title` and `body` blocks. Notice that you can have blocks inside blocks.

Here goes an example of tamplate expanding the `base.html` tamplate:

```html
{% extends "base.html" %}
{% block title %}Index{% endblock %}
{% block head %}
    {{ super() }}
    <style>
    </style>
{% endblock %}
{% block body %}
<h1>Hello, World!</h1>
{% endblock %}
```

The `extends` directive says that this templates derives from `base.html`. Then we define the other blocks with content which are inserted in the proper place. Notice that when there is content in both the base and derived templates, the content from the derived template is used. But you can use the `super()` directive to reference the content in the base template.

## Bootstrap
Managing bootstrap with flask is farely simple. Other than simply create your templates with references in html and css to the `bootstrap` framework, flask offers an extension to better organize it in the code. The extension is calles `flask-bootstrap` and can be installed with pip. But you must initiate it in the code with:

```python
from flask_bootstrap import Bootstrap
#...
bootstrap = Bootstrap(app)
```

There are two patterns for initialization of extensions. One of which is by calling the constructor on the app (as an argument), as shown in the example above. There are other methods of doing this. Which will not be discussed now.

Now that the extension is enabled, a base template that includes all teh Bootstrap files and general structure is available to the application. Then you just need to extend the bootstrap template as follows:

```html
{% extends "bootstrap/base.html" %}
{% block title %}Flasky{% endblock %}
{% block navbar %}
<div class="navbar navbar-inverse" role="navigation">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle"
             data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="/">Flasky</a>
        </div>
        <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="/">Home</a></li>
            </ul>
        </div>
    </div>
</div>
{% endblock %}
{% block content %}
<div class="container">
    <div class="page-header">
        <h1>Hello, {{ name }}!</h1>
    </div>
</div>
{% endblock %}
```
Here are other usefull blocks:

|Block name|Description
|-|-
|doc|The entire HTML document
|html_attribs|Attributes inside the `<html>` tag
|html|The contents of the `<html>` tag
|head|The contents of the `<head>` tag
|title|The contents of the `<title>` tag
|metas|The list of `<meta>` tags
|styles|CSS definitions
|body_attribs|Attributes inside the `<body>` tag
|body|The contents of the `<body>` tag
|navbar|User-defined navigation bar
|content|User-defined page content
|scripts|JavaScript declarations at the bottom of the document

Many of the blocks in this table are used by `flask-bootstrap` itself so overridding them directly would cause problems. So remember of using `super()`, if you forget it, important elements of the template will be lost, like the `css` and `javascript` references. So, to add a new javascript file to the project you would need to do the following:

```html
{% block scripts %}
{{ super() }}
<script type="text/javascript" src="my-script.js"></script>
{% endblock %}
```

## Custom Error page
The `404` pages that represent `Not found` are very ugly by default in an `flask` app. But don't worry, its possible to customise said page. They can be based on regular templates. The two most common error codes are `404` that occur when a client request a page or rout that isn't known. And `500` that occur when there is a unhandled exception in the application. On the following example we can define a custom page for these scenarios:

```python
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
```

So flask returns what must be shown in the screen and the error code to let the browser know that an error happended.

## Links
If your app has more than one page than you will need links to send the user to the different pages like the ones present in the navigation bar. You can use basic `html` for that in simple enough cases, but that can become rapidly inviable. Like if you use dynamic routes, or if you change frequently your routes. In those cases more elaborate methods are required for a better development experience (in the case of dynamic routes these advanced methods are even necessary).

To assist with that flask gives the `url_for()` function, which generates the `URL` from the information stored in the application's `URL` map. An example of this function usage is with `url_for('index')` that represents the `/` route, that is, the root `URL` of the application. If you use `url_for('index', _external=True)` it would return the absolute `URL` which would be `http://localhost:5000/` in this example.

Relative `url` are sufficient when generation links that connect the different routes. The absolute one is used only when generating links that will be exported to be used outside of the web browser.

Dynamic `url`s can be created by passing the dynamic parts as keyword arguments. For example `url_for('user', name='john', _external=True)` would return `http://localhost:5000/user/john`. These arguments are not limited to dynamic routes. The function can add others, like in the example `url_for('user', name='john', page=2, version=1)` that would return `/user/john?page=2&version=1`.

## Static files
Besides python code and templates, there are other usefull files that can be necessary for rendering the page, like `CSS` files that are referenced from the `html` code in the templates.

Remember that flask creates a special `route` defined as `/static/<filename>`. This route is dedicated to serve the static files in the `static` folder in the root directory by default, and subdirectories are allowed. So, calling `url_for('static', filename='css/styles.css', _external=True)` would return `http://localhost:5000/static/css/styles.css`.

Here is how this would work in a real project to add a `favicon` icon to the page:

```html
{% block head %}
{{ super() }}
<link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}"
    type="image/x-icon">
<link rel="icon" href="{{ url_for('static', filename='favicon.ico') }}"
    type="image/x-icon">
{% endblock %}
```

## Dates and times with flask-moment
Handling dates and times in the web is complex when the users work in different parts of the globe. The server needs a time unity that is independent of the geolocalization, like the `UTC` (Coordinated Universal Time). But users want to see dates and time in their local time frame. This can be done with the `Moment.js` extension in the browsers. Flask have an extension to integrate nicely with this tool, the `Flask-Moment`. You would need to install it with:

```bash
pip install flask-moment
```
And to initialize, the process is similar to the flask-bootstrap extension:

```python
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# ...
```

It is dependent on `jQuery.js` and `Moment.js`. Both must be included somewhere in the `html` code. To render the date in the template the following must be done:

```html
{% block scripts %}
{{ super() }}
{{ moment.include_moment() }}
{% endblock %}
```

So Flask-Moment makes a `moment` object available to the template. To render the date you must pass the `UTC` time as follows:

```python
from datetime import datetime
@app.route('/')
def index():
    return render_template('index.html',
                           current_time=datetime.utcnow())
```

And, in the `html` you would do:

```html
<p>The local date and time is {{ moment(current_time).format('LLL') }}.</p>
<p>That was {{ moment(current_time).fromNow(refresh=True) }}</p>
```

Notice that the `format('LLL')` referes to the local time according to the time-zone of the client. From `L` to `LLLL` there is four different levels of verbosity. And `format()` accepts too a long list of format specifiers. The `refresh=True` argument keeps the time up to date. There are other functions like `fromNow()` That calculates the time passed from the time given by the server. There are others like `fromTime()`, `calendar()`, `valueOf()`, and `unix()` methods from `Moment.js`. One can configure the language too, with the following code:

```html
{% block scripts %}
{{ super() }}
{{ moment.include_moment() }}
{{ moment.locale('es') }}
{% endblock %}
```








