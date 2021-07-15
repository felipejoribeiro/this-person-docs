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

The best practice is to import from environment variables these settings.


