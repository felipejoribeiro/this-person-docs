# Flask forms and email
The templates until here are all unidirectional. Only the server sends information to the client and not the other way around. But these cases are necessary for a miriade of applications. The `html` protocol offers te ability of creating forms, in which a user can enter information and send it via a `POST` request for the server. This is done with the `request` object.

Some tasks in these practices can become very repetitive and tedious. Like the creation of the `html` code for the forms and the validation of the submitted form data. The `Flask-WTF` extension makes working with wev forms a much more pleasant experience. It is a wrapper around the `WTForms` package. You can install it with `pip install flask-wtf`. The extansion doesn't need to be initialized in the application level but it expects the application to have a secret key configured. This is a string that is used to encrypt the information in the form. To configure it you must do the following in your application:
```python
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
```

The `app.config()` method is a way of configuring the flask app. Configurations are added with the standard dictionary syntax. There is better ways of managing this that will be discussed further. This is how flask protects the app against `CSRF`(Cross Site Request Forgery) attacks. For further security this value should be stored in an environment variable instead of plain text more details further.

## Forms classes
When using the `flask-wtf` extension, each web form is represented in the server by a class that inherits from the class FlaskForm. The class defines the list of fields in the form, each represented by an object. Each field object can have one or more validators attached. The validator checks if the data sent by the user is valid. Here goes a form example:

```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
```

So here we define a form with a text input and a submit button. The class extended `FlaskForm` and added two objects that defined form elements. That's how it works. The `StringField()` defines the input method and the first argument represents the `<input>` element in `html`. Same thing with the `SubmitField()` method. The `validators=[DataRequired()]` ensures that the field has information.

The fields are:

|Field type|Description
|-|-
|BooleanField|Checkbox with True and False values
|DateField|Text field that accepts a datetime.date value in a given format
|DateTimeField|Text field that accepts a datetime.datetime value in a given format
|DecimalField|Text field that accepts a decimal.Decimal value
|FileField|File upload field
|HiddenField|Hidden text field
|MultipleFileField|Multiple file upload field
|FieldList|List of fields of a given type
|FloatField|Text field that accepts a floating-point value
|FormField|Form embedded as a field in a container form
|IntegerField|Text field that accepts an integer value
|PasswordField|Password text field
|RadioField|List of radio buttons
|SelectField|Drop-down list of choices
|SelectMultipleField|Drop-down list of choices with multiple selection
|SubmitField|Form submission button
|StringField|Text field
|TextAreaField|Multiple-line text field

And the validators are the following:

|Validator|Description
|-|-
|DataRequired|Validates that the field contains data after type conversion
|Email|Validates an email address
|EqualTo|Compares the values of two fields; useful when requesting a password to be entered twice for
|confirmation|InputRequired Validates that the field contains data before type conversion
|IPAddress|Validates an IPv4 network address
|Length|Validates the length of the string entered
|MacAddress|Validates a MAC address
|NumberRange|Validates that the value entered is within a numeric range
|Optional|Allows empty input in the field, skipping additional validators
|Regexp|Validates the input against a regular expression
|URL|Validates a URL
|UUID|Validates a UUID
|AnyOf|Validates that the input is one of a list of possible values
|NoneOf|Validates that the input is none of a list of possible values

## Rendering the forms
Having the server expect the form isn't enough. The client side must be implemented as well. For that we need rendering and placement. That can be done with the following code:

```html
<form method="POST">
    {{ form.hidden_tag() }}
    {{ form.name.label }} {{ form.name() }}
    {{ form.submit() }}
</form>
```
Remember to pass the form as an input in the template as previously explained.

Notice that in adition to the name and submit fields, the form has a `form.hidden_tag()` element. This is a hidden field used by Flask-WTF to implement `CSRF` protection.

To define the style for the form you must add `class` and `id` to the form with code like:

```html
<form method="POST">
    {{ form.hidden_tag() }}
    {{ form.name.label }} {{ form.name(id='my-text-field') }}
    {{ form.submit() }}
</form>
```

You can style the form with bootstrap as well with the following:

```html
{% import "bootstrap/wtf.html" as wtf %}
{{ wtf.quick_form(form) }}
```
So the entire thing becomes:

```html
{% extends "base.html" %}
{% import "bootstrap/wtf.html" as wtf %}
{% block title %}Flasky{% endblock %}
{% block page_content %}
<div class="page-header">
    <h1>Hello, {% if name %}{{ name }}{% else %}Stranger{% endif %}!</h1>
</div>
{{ wtf.quick_form(form) }}
{% endblock %}
```
## Managing the view function
The view function that sends `form` pages must deal with the response as well. That can be done as following:
```python
@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)
```
In this case the `route` is configured to handle the `GET` and  `POST` requests. When this is not defined the `route` is configured to `GET` by default.

Submissions are universally done as a `POST` request. This is due to the fact that the `GET` request don't have a body so the that would go in the `url` of the request as a query string which isn't by no means ideal. The `name` variable is used to store the received name from the form. The `validate_on_submit()` method returns `True` when the form is submitted and the data is accepted by all the field validators. So this is used to see if the form must be rewritten or processed. When the user enters the form for the first time the server will receive a GET request with no data, so the `validate_on_submit()` will return `False`.

## Redirects and user sessions
If you ask to refresh the browser after submit a `form` something interesting will happens. The browsers repeat the last `http` request that was issued when refreshing. So it will send the `POST` request again with the information. And the browser will likely send a notification asking if you want really do that. Majority of people don't understand this message, so is good practice to never leave a `POST` request as the last request sent by the browser.

This is possible by responding the `POST` request with a `redirect` instead of a normal response. Redirect is a special type of response that contains a `URL` instead of a string wth a `HTML` code. When the browser receives a `redirect` response, it launches a `GET` request for the given `URL` and that is the page that is displayed. Now the last request was a `GET`, so no problem will occur with a refresh.

This trick is know as `POST/REDIRECT/GET` pattern. But there is another problem, if you make another request the `name` that was sent in the `POST` request will be lost. To counter that we can use the concept of `user session` which enables information saving through requests. The information is saved in `user session`, that is a private storage that is available to each connected client. By default user session are stored in client-side cookies that are cryptographically signed using the configured secret key. Any modification in the cookie content would render the signature invalid, invalidating the session.

The following code implements the sesisons and `POST/REDIRECT/GET` pattern:

```python
from flask import Flask, render_template, session, redirect, url_for

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))
```

So, `session['name']` is remembered through requests and saved in the client side.

## Message Flashing
Sometimes it's good to send a message to the client to give update in some backend process. This could be a confirmation message, a warning message or a fail message. A typical example is when you submit a `form` with wrong information, and the page is reloaded with a message above the `form` element with the `error`. Or when you try to login in your account but you miss your password, and a error message appear. Flask includes this as a core feature. It uses the `flash()` method.

Here goes an example:

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html',
        form = form, name = session.get('name'))
```

In this case it compares the sent name with the previous saved. If it is different it send a message with a warning. The message handling must be dealled with in the client side too, in the template. There is a `get_flashed_messages()` method for this, to retrieve the information and render it:

```html
{% block content %}
<div class="container">
    {% for message in get_flashed_messages() %}
    <div class="alert alert-warning">
        <button type="button" class="close" data-dismiss="alert">&times;</button>
        {{ message }}
    </div>
    {% endfor %}
    {% block page_content %}{% endblock %}
</div>
{% endblock %}
```
In this example the mensages are rendered using the bootstrap template for style.
A for loop is used because there could be multiple messages queued for display, one for each time `flash()` was called in the previous request cycle. This is necessary because all messages that are not displayed are discarted. And more than one can emerge.


