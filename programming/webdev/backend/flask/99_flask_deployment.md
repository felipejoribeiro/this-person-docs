# Flask deployment
The basic web server that comes with `flask` isn't robust, secure or efficient enough to work in a production environment.

There are tasks that must be performed in the server. Like database creation and update. Perform these tasks manually is prone to error and time consumming. These can be added to flasky.py to be performed automatically.

```python
from flask_migrate import upgrade
from app.models import Role, User
@manager.command
def deploy():
    """Run deployment tasks."""
    # migrate database to latest revision
    upgrade()
    # create or update user roles
    Role.insert_roles()
    # ensure all users are following themselves
    User.add_self_follows()
```

These functions were created before and they are all called from this one function to simplify deploy. These functions are designed in a way that there is no problem in running then multiple times. So they can be runned in any update or installation without worries.

## Logging of errors during production
When in development mode, you can debug the application directly on the browser, `Werkzeug` interactive debugger is available. In production this is different. All errors are silenced and all the user sees is the code `500` error page. But these errors aren't lost as flask write then in a log file.

On the startup `flask` creates a `logging.logger` class and attaches it to the application instance as `app.logger`. In debug mode this logger writes to the console, but in production there is no handlers configured to it by default. The following handler is configured to send the error to the administrator email:


```python
class ProductionConfig(Config):
    # ...
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        # email errors to the administrators
        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr(cls, 'MAIL_USERNAME', None) is not None:
            credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIL_USE_TLS', None):
                secure = ()
        mail_handler = SMTPHandler(
            mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
            fromaddr=cls.FLASKY_MAIL_SENDER,
            toaddrs=[cls.FLASKY_ADMIN],
            subject=cls.FLASKY_MAIL_SUBJECT_PREFIX + ' Application Error',
            credentials=credentials,
            secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)
```

Recall that all configuration classes have an `init_app()` static method that is invoked by `create_app()`, so now the application logger is configured to send errors to an email recipient.

## Cloud hosting
A way of hosting the service in the cloud is by hosting it in a virtual machine somewhere, like in the `E2C` service from Amazon Web Services (AWS). This modality is like deploying the application in a traditional server.

Other deployment model, more advanced, is based in containers. A container isolates an application in an image of the application and its environment. And the image contains teh application and all the dependencies it needs to run. A container plataform, like `Docker` can run these images in any system in which it runs.

A final way of deployment is with Plataform as a Service (PaaS). The most known provider is `Heroku`. In this way of serving, you just upload the application code to the server and it is managed by the third party. It has auto scaling too, so it simplify the backend.


## The Heroku Platform
Heroku is one of the first `PaaS` providers, beggining operations in 2007. It is very flexible and supports a variety of programming languages, including python. To send the code to the servers, the developer uses `GIT` to `push` the application to Heroku special `Git` server, which automatically triggers the installation, upgrade, configuration, and deployment of the application.

For scaling, the plataform define `web dynos` and `worker dynos` that are computational units that perform the tasks determined by the app. Scaling becomes only a metter of increasing the number of these unitis.

The platform offers lots of add-ons and plug-ins for databases, email support and many other things.

### Preparations
The first thing you must do is have the application in a `GIT` repository. This is necessary as this is how you send the code for deployment. Then you must create an account on Heroku, there is a free tier that allows you to host simple applications.

Then you must install the `Heroku CLI`, which provides integration with the service. Then authenticate with your account credentials with a terminal login. The login command already creates an `SSH` key pair to send to the service so that you can `push` stuff, but you can create other keys with the `keys:add` command if necessary.

TODO: Will continue later this section

## Docker deployment
TODO: Will continue later this section

## Traditional deployment
If you have a server or a cloud provider like `E2C` or `DigitalOcean` you can follow this type of deployment. It is the more laborious, but offers tremendous flexibility.

### Server Setup




