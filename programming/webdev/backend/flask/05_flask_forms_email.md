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

| Field type          | Description
| -                   | -
| BooleanField        | Checkbox with True and False values
| DateField           | Text field that accepts a datetime.date value in a given format
| DateTimeField       | Text field that accepts a datetime.datetime value in a given format
| DecimalField        | Text field that accepts a decimal.Decimal value
| FileField           | File upload field
| HiddenField         | Hidden text field
| MultipleFileField   | Multiple file upload field
| FieldList           | List of fields of a given type
| FloatField          | Text field that accepts a floating-point value
| FormField           | Form embedded as a field in a container form
| IntegerField        | Text field that accepts an integer value
| PasswordField       | Password text field
| RadioField          | List of radio buttons
| SelectField         | Drop-down list of choices
| SelectMultipleField | Drop-down list of choices with multiple selection
| SubmitField         | Form submission button
| StringField         | Text field
| TextAreaField       | Multiple-line text field

And the validators are the following:

| Validator    | Description
| -            | -
| DataRequired | Validates that the field contains data after type conversion
| Email        | Validates an email address
| EqualTo      | Compares the values of two fields; useful when requesting a password to be entered twice for
| confirmation | InputRequired Validates that the field contains data before type conversion
| IPAddress    | Validates an IPv4 network address
| Length       | Validates the length of the string entered
| MacAddress   | Validates a MAC address
| NumberRange  | Validates that the value entered is within a numeric range
| Optional     | Allows empty input in the field, skipping additional validators
| Regexp       | Validates the input against a regular expression
| URL          | Validates a URL
| UUID         | Validates a UUID
| AnyOf        | Validates that the input is one of a list of possible values
| NoneOf       | Validates that the input is none of a list of possible values

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

# Email
Many applications need to notify users in some occasions. A good method is via email. Python has a standard library `smtplib` that sends emails, but flask has its own wrapper for it that integrates nicely with the app. It's called `Flask-Mail` and it connects to localhost at port 25 and sends email without authentication. you can install it with `pip install flask-mail`. Here goes some configurations:

| Key           | Default   | Description
| -             | -         | -
| MAIL_SERVER   | localhost | Hostname or IP address of the email server
| MAIL_PORT     | 25        | Port of the email server
| MAIL_USE_TLS  | False     | Enable Transport Layer Security (TLS) security
| MAIL_USE_SSL  | False     | Enable Secure Sockets Layer (SSL) security
| MAIL_USERNAME | None      | Mail account username
| MAIL_PASSWORD | None      | Mail account password

During development it may be more convenient to connect to an external `SMTP` server. The following application uses `Google Gmail` account:

```python
import os
# ...
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
```

But remember, never write account credentials directly in your scripts. More so if you pretend to release the project in open source field. If that is the case, have a script that imports this information from environment variables, or from a file that isn't tracked by git.

Notice that it takes the credentials from environment variable, so don't forget to declare then before initiating the app:

```bash
export  MAIL_USERNAME=<Gmail username>
export  MAIL_PASSWORD=<Gmail password>
```

Remember too that Gmail accounts are configured by default ro require external applications to use OAuth2 authentication to connect to the email server. You can change that in your accounts settings enabling "Allow less secure apps". If enabling this configuration in your personal account concerns you, create a secondary account just for that.

To use the extension you must initialize it with:

```python
from flask_mail import Mail
mail = Mail(app)
```

## Sending an email from the python shell
You can start a python shell and send a test email:

```bash
(venv) $ flask shell
>>> from flask_mail import Message
>>> from hello import mail

>>> msg = Message('test email', sender='you@example.com',
        recipients=['you@example.com'])
>>> msg.body = 'This is the plain text body'
>>> msg.html = 'This is the <b>HTML</b> body'
>>> with app.app_context():
       mail.send(msg)

```

So it's important to have an application context runing as the `send()` method uses `current_app`.

## Integrating emails with the application
To avoid having to create email messages manually every time, it is a good idea to abstract the common parts of the application's email sending functionality into a  function. An additional benefit, you can render emails from `Jinja2` templates.
The implementation can be seen ahead:

```python
from flask_mail import Message

app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
```
There must be two versions, one in plain text and one in `html`. Now you can call this function from your view functions to send automated responses as follows:

```python

# ...

app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')

# ...

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            if app.config['FLASKY_ADMIN']:
                send_email(app.config['FLASKY_ADMIN'], 'New User',
                           'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False))
```

So now when someone registers the form an response email is sent to the user. Remember to set the `FLASKY_ADMIN` environment variable before testing.


## Asynchronous Email
Sending the email can freeze the request thread for a moment. Such thing makes the browser application irresponsive during that time. To avoid that the email can be sent through a background thread. Like in the following example:

```python
from threading import Thread

def send_async_email(app, msg):
    with app.app_context:
        mail.send(msg)

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
```

This implementation highlights an interesting problem. Many flask extensions operate under the assumption that there are active application and/or request contexts. Like how `send()` requires `current_app` to work. But this creates a problem, as another thread would take off the function from the application context. So we need to create this context artificially with `app.app_context()`. The app instance is passed to the thread as an argument so that a context can be create.

If you test this new version you will notice how it is more fluid. But its important to notice that if you have a server that creates lots and lots of emails, better than create a job for every email is to have a dedicated one just for doing that.











