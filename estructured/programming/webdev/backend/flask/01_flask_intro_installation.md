# The FLASK framework
Flask is known as a "micro-framework" because it's small enough that once you become familiar with it, you will likely be able to read and understand all of its source code.

It has a minimal but competent core which is largely extensible with plugins and libraries. That's good as you can compose your server just with the tools you need. It has three main dependencies:

- Werkzeug: Brings routing, debugging and Web Server Gateway Interface (WSGI).
- Jinja2: Provides template support.
- Click: Command line integrantion.

These are all althored by the inventor of flask hinself. There is no native support for database access, validating web forms, authentication or other high-level endeavors. The developer must create hinself these tools or use extensions.

## Installation
The best way of doing this is with virtual environments, as it allows the developer to have various python environments, one for each project and they don't affect the global python installation in your system, solving some inter-project dependency problems.

After creating and activating the virtual environment, install the `flask` package with the `pip install flask` command. After that you can see what packages are installed with the `pip freeze` command.
If you installed the `flask` package you can se that the three core packages were installed already (`Jinja2`, `Werkzeug` and `click`).

And that is it. You are ready to create some basic `web` aplications.


