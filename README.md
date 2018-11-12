Django DB Pool Backends
=======================

**A mysql / postgres database backend for Django which provides persistence connection pools implemented by DBUtils.**


Requirements
------------
* [Django 1.8.2+](https://www.djangoproject.com/download/)
* [MySQL](https://dev.mysql.com/downloads/mysql/) or [PostgreSQL](http://initd.org/psycopg/) for your database


Usage
-----

like this:

    'default': {
        'ENGINE': 'django_dbpool.db.backends.mysql',  # or  'ENGINE': 'django_dbpool.db.backends.postgresql',
        'NAME': 'test',
        'USER': 'test',
        'PASSWORD': 'test123',
        'HOST': 'localhost',
        'PORT': 3306,
        # The POOL will be used to generate the connection pool instance
        'POOL': {
            'min_size': 10,  # Default '0' means empty connection pool when start
            'max_size': 50  # Default '0' means unlimit connection pool size
        },
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'isolation_level': 'read committed'
        }
    }
