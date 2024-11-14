---
id: 1716862221-python-version-package-management-poetry-pyenv
aliases:
  - python-version-package-management-poetry-pyenv
tags:
  - pyenv
  - poetry
  - python
---

# Python package and version management

![python-snake-evolution-header.png](../assets/from_notes/1716862221-python-version-package-management-poetry-pyenv-2024-05-27-23-19-52-python-snake-evolution-header.png)

## Introduction

Managing python versions and package versions for each project isn't a simple task. This is a classic problem that emmerges from the fact that **Python** is installed in the system and the packages are installed globally. This can lead to conflicts between different projects that require different versions of Python and packages.

Luckily, there are some open source tools that can help with this problem now-a-days:

- **pyenv**: Simple Python version management, which allows to easily switch between different versions of Python in your system, and to create virtual environments with different versions of Python.
- **virtualenv**: Simple way to create isolated Python environments with different versions of Python and packages which are specific to each project.
- **poetry**: Simple way to management and package dependencies for Python projects. It works like other package managers like **npm** and **yarn**, by creating a lock file with all dependencies and versions for each project, even integrating with **virtualenv**.

## Pyenv

This is a python version management tool that allows you to switch between python versions easily. It works like other prograns like **arcklinux-java** for controlling the java version in **arch-linux** systems, or **nvm** for controlling the node version in **node.js** projects. You can even specify the python version for specific directories with a `.python-version` file specifying the version to be used.

### Installation

It is very simple to install **pyenv**. You can use the following command to install it in your system:

```bash
curl https://pyenv.run | bash
```

After the installation, you must add the following lines to your `.bashrc` or `.zshrc` file:

```bash
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

### Usage

With **pyenv** you can easily switch between python versions. You can list all available versions with the following command:

```bash
pyenv install --list # List all available versions
pyenv install 3.9.5 # Install a specific version
pyenv global 3.9.5 # Set the global version
pyenv local 3.9.5 # Set the local version
```

## Virtualenv

Now you can specify the python version for each project with **pyenv**. But you still have the problem of managing packages that are specific for each project. **Python** has a built-in tool for this called **virtualenv**. It allows you to create isolated environments for each project, with different versions of python and packages.

### Installation

To install **virtualenv** you can use the following command:

```bash
pip install virtualenv
```

### Usage

With **virtualenv** you can create a new environment with the following command:

```bash
python -m venv env
```

This will create a new `env` directory with the isolated environment. You can activate the environment with the following command:

```bash
source env/bin/activate
```

Now, if you issue the `which python` command, you will see that the python version is the one from the `env` directory. You can install packages with the `pip` command, and they will be installed in the `env` directory, independently of the global python installation.

Creating new environments can be done by deleting this directory and creating a new one, imagine these directories as entire **Python** isntallation instances.

## Poetry

Now that you can manage python versions with **pyenv** and specific package versions with **virtualenv**, you can use **poetry** to manage the dependencies for each project separetely.

**Poetry** works like other package managers like **npm** and **yarn**, by creating a lock file with all dependencies and versions for each project. If you don't integrate it with **virtualenv** it will create a separated environment by it's own, but i recommend using it with **virtualenv** to have more control over your environment.

Besides managing dependencies, **poetry** can package your projects and publish them to **PyPi**. It can also create a new projects with the following command:

```bash
poetry new my_project
```

The main benefits of using it instead of a pure `requirements.txt` file are:

- It separates direct dependencies from indirect dependencies;
- It has a lock file that is updated when any dependency version changes;
- It's dependency resolver is better than pip's;

### Installation

To install **poetry** you can use the following command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Usage

Poetry is a big and complex tool, but you can use it to manage dependencies with the following commands:

```bash
poetry install # Install dependencies
poetry add package_name # Add a new package
poetry remove package_name # Remove a package
poetry update package_name # Update a package
poetry run python script.py # Run a python script
poetry shell # Activate the virtual environment
```
