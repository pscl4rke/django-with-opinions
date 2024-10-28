

A Blank Django Project, But With Opinions
=========================================

As understood by `django-admin startproject --template`.

Opinions:

* Makefiles are handy for development.
* Environment variables are better than hardcoding.
* Jinja is better than Django's own templating.
* You want a basic theme/layout to get started.
* There should be pages for 404, 500, etc.
* No favicons unless explicitly set.
* Lean into logging. Seriously!
* Pyflakes is quick and useful.
* It's good to test and get coverage stats.
* Type-checking keep you sane, despite Django hating it.

To use:

    $ mkdir /path/to/venvs
    $ python3 -m venv foobar
    $ source ./foobar/bin/activate
    $ pip install django jinja2 pyflakes coverage utterless \
                  mypy django-stubs

    $ mkdir /path/to/my-foobar-codebase
    $ cd /path/to/my-foobar-codebase
    $ django-admin startproject \
        --template /path/to/this/directory \
        --extension py,cfg \
        foobar .

    $ rm README.md
    $ pip freeze > requirements.txt


