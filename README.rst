Django Database Logs
====================

`Django Database Logs <http://www.grantjenks.com/docs/django-dblog/>`__ is an
Apache2 licensed Django application that enables logging to the database.


Quickstart
----------

Installing Django Database Logs is simple with `pip
<http://www.pip-installer.org/>`_::

    $ pip install django-dblog

Changes to ``settings.py`` example:

.. code::

   INSTALLED_APPS += ['dblog']

   LOGGING = {
       'version': 1,
       'disable_existing_loggers': False,
       'handlers': {
           'dblog': {
               'class': 'dblog.DBLogHandler',
           },
       },
       'loggers': {
           'dblog': {
               'handlers': ['dblog'],
               'level': 'DEBUG',
               'propagate': False,
           },
       },
   }

Using the logger, example:

.. code::

   import logging

   dblog = logging.getLogger('dblog.' + __name__)

   dblog.info('This message will go in the dblog Record table.')


Reference and Indices
---------------------

* `Django Database Logs Documentation`_
* `Django Database Logs at PyPI`_
* `Django Database Logs at GitHub`_
* `Django Database Logs Issue Tracker`_

.. _`Django Database Logs Documentation`: http://www.grantjenks.com/docs/dblog/
.. _`Django Database Logs at PyPI`: https://pypi.python.org/pypi/django-dblog/
.. _`Django Database Logs at GitHub`: https://github.com/grantjenks/django-dblog
.. _`Django Database Logs Issue Tracker`: https://github.com/grantjenks/django-dblog/issues


Django Database Logs License
----------------------------

Copyright 2018-2022 Grant Jenks

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
