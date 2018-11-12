# -*- coding: utf-8 -*-
"""
PostgreSQL database backend for Django.

Requires psycopg 2: http://initd.org/projects/psycopg2
"""

from django.core.exceptions import ImproperlyConfigured
from django.db.backends.postgresql.base import DatabaseWrapper as PostgresDatabaseWrapper

try:
    import psycopg2 as Database
    from ..pool import DBWrapper
    import psycopg2.extensions
    import psycopg2.extras
except ImportError as e:
    raise ImproperlyConfigured("Error loading psycopg2 module: %s" % e)

Database = DBWrapper(Database)


class DatabaseWrapper(PostgresDatabaseWrapper):
    Database = Database

    def get_connection_params(self):
        params = super().get_connection_params()

        if self.settings_dict.get('POOL_MIN_SIZE'):
            params['pool_min_size'] = int(self.settings_dict['POOL_MIN_SIZE'])
        if self.settings_dict.get('POOL_MAX_SIZE'):
            params['pool_max_size'] = int(self.settings_dict['POOL_MAX_SIZE'])
        elif params.get('pool_min_size'):
            params['pool_max_size'] = params['pool_min_size']
        return params

    def get_new_connection(self, conn_params):
        connection = Database.connect(**conn_params)
        # self.isolation_level must be set:
        # - after connecting to the database in order to obtain the database's
        #   default when no value is explicitly specified in options.
        # - before calling _set_autocommit() because if autocommit is on, that
        #   will set connection.isolation_level to ISOLATION_LEVEL_AUTOCOMMIT.
        options = self.settings_dict['OPTIONS']
        try:
            self.isolation_level = options['isolation_level']
        except KeyError:
            self.isolation_level = connection.isolation_level
        else:
            # Set the isolation level to the value from OPTIONS.
            if self.isolation_level != connection.isolation_level:
                connection.set_session(isolation_level=self.isolation_level)
        return connection
