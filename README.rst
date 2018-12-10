Paywall
========

Paywall assignment, A `django`_ application consists of login, register and posts API written in `python`_ 3.6.


Install Dependencies
--------------------

.. code-block:: bash

    $ pip install -r requirements.txt


Deployment
----------

.. code:: bash

    $ python manage.py migrate

**Note**: user must be created in order to test the task, the easiest way to do so is to
create super user.

.. code:: bash

    $ python manage.py createsuperuser


Then load fixtures.

.. code :: bash

    $ python manage.py loaddata posts


Development server
------------------

.. code:: bash

    $ python manage.py runserver


Project structure
-----------------
::

    .
    ├── api                             # api application contains everything related to api
    │   └── rest                        # all restful APIs versions will live here
    │       └── v1                      # api version 1
    │           ├── paginators.py       # contains custom pagination classes
    │           ├── serializers.py      # contains classes that serialize objects to json/xml and vice versa
    │           ├── urls.py             # api version 1 exposed urls
    │           └── views.py            # views to process requests
    │
    ├── posts                           # contains models and related logic.
    │   ├── fixtures                    # 20 placeholder posts
    │   ├── admin.py                    # admin customization
    │   ├── apps.py                     # entry point for django project (used in paywall.settings)
    │   └── models.py                   # Post model and PostQuerySet.
    │
    ├── paywall                         # root application.
    │   ├── settings.py                 # contains settings and configurations for all applications
    │   ├── urls.py                     # public accessible urls
    │   ├── utils.py                    # contains utility functions (send_welcome_email)
    │   └── wsgi.py                     # entry point for wsgi
    │
    ├── wall                            # serves production reactJS application
    │   ├── urls.py                     # public accessible urls
    │   └── views.py                    # only home page view
    │
    ├── requirements.txt                # project dependencies
    ├── manage.py                       # entry point for django cli commands
    └── README.rst

.. _python: https://www.python.org/
.. _django: https://www.djangoproject.com/