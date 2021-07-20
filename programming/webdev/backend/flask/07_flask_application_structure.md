# Big application structure
Having all your code in one file can be very convenient, but this way of handling things don't scale very well. The complexity grows fast and managing the application resources becomes almost impossible at some point.

Here we will see how to organize a project with packages and modules.

## The basic layout

```
flasky
  │ requirements.txt
  │ config.py
  │ flasky.py
  │ migrations/
  │ venv/
  └ app/
  │   │ templates/
  │   │ static/
  │   │ main/
  │   │  │ __init__.py
  │   │  │ errors.py
  │   │  │ forms.py
  │   │  └ views.py
  │   │ __init__.py
  │   │ email.py
  │   └ models.py
  └ tests/
      │ __init__.py
      └ test*.py
```

There is four directories in the `root` directory of the application. The source code is present in the `app` directory. The `migration` folder contains the database migration scripts. Unit tests are written in a tests package and the venv folder contains the python virtual environment where the application runs.

In the `requirements.txt` file there is the dependencies of the project. The `config.py` file stores the configuration settings. The `flasky.py` file defines the `flask` application instance, and also includes a few tasks that help manage the application.

## The config.py file
Most applications need several configurations. One example is using different databases during development, testing and production. To better handle that we can use an hierarchy of configuration classes.
Here goes an example:

```python
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
```

The `config` class contains settings that are common to all configurations. The different subclasses have specific settings.

The best practice is to import from environment variables these settings. Specially if you are dealling with source control. As you will not be able to erase the information after commit.

The creation, form the beginning of test environments is a must for better future developments, even if you don't pretend to create the infrastructure now.


## The app directory
Inside the app directory will be located all the implementation of the application including the `templates` and `static` directories. The more important modules are implemented in the same directory as the app too.

## The importance of an Application factory
Creating the application and configuring it globally in the file that `gevent` runs is convenient for prototyping, but presents a series of inconveniences in further development being the most important one the lack of flexibility.

To implement that we can move the app creation to a `factory function`. With this approach we can even create multiple application instances at the same time with different configurations. Here goes an example:

```python
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    # attach routes and custom error pages here
    return app

```
This constructor imports most of the Flask extensions currently in use, but because there isn't any application instance to initialize them with , it creates them uninitialized by passing no arguments into their constructors.

