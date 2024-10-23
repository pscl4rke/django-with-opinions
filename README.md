

A Blank Django Project, But With Opinions
=========================================

As understood by `django-admin startproject --template`.

Opinions:

* Jinja is better than Django's own templating.

To use:

    $ mkdir /path/to/my-foobar-codebase
    $ cd /path/to/my-foobar-codebase
    $ django-admin startproject \
        --template /path/to/this/directory \
        foobar .
    $ rm README.md
    $ pip install jinja2


