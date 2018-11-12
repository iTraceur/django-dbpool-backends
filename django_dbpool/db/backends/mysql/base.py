# -*- coding: utf-8 -*-
"""
MySQL database backend for Django.

Requires mysqlclient: https://pypi.org/project/mysqlclient/
"""
from django.core.exceptions import ImproperlyConfigured
from django.db.backends.mysql.base import DatabaseWrapper as MysqlDatabaseWrapper
from django.utils import six
from django.utils.safestring import SafeBytes, SafeText

try:
    import MySQLdb as Database
    from ..pool import DBWrapper
except ImportError as err:
    raise ImproperlyConfigured(
        'Error loading MySQLdb module.\n'
        'Did you install mysqlclient?'
    ) from err

Database = DBWrapper(Database)


class DatabaseWrapper(MysqlDatabaseWrapper):
    Database = Database

    def get_connection_params(self):
        params = super().get_connection_params()
        pool_config = self.settings_dict.get('POOL')
        if pool_config.get('min_size'):
            params['pool_min_size'] = int(pool_config['min_size'])
        if pool_config.get('max_size'):
            params['pool_max_size'] = int(pool_config['max_size'])
        return params

    def get_new_connection(self, conn_params):
        conn = Database.connect(**conn_params)
        conn.encoders[SafeText] = conn.encoders[six.text_type]
        conn.encoders[SafeBytes] = conn.encoders[bytes]
        return conn
