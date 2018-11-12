# -*- coding: utf-8 -*-

"""A connection pool of MySQL in Django based on DBUtils."""

from django_dbpool.DBUtils.PooledDB import PooledDB


class ConnectionWrapper(object):
    def __init__(self, connection):
        self._conn = connection

    def __getattr__(self, method):
        """ Proxy connection's attribute method """
        return getattr(self._conn, method)

    def close(self):
        """ Proxy the closing method of django db connection """
        self._conn.close()


class DBWrapper(object):
    def __init__(self, module):
        self._connection = None
        self._db = module
        self._pool = {}

    def __getattr__(self, item):
        return getattr(self._db, item)

    def connect(self, *args, **kwargs):
        """ Create pool and connection """
        db = kwargs.get('db')
        if db not in self._pool:
            pool_min_size = kwargs.pop('pool_min_size', None)
            pool_max_size = kwargs.pop('pool_max_size', None)
            self._pool[db] = PooledDB(self._db, mincached=pool_min_size, maxcached=pool_max_size, *args, **kwargs)
        self._connection = self._pool[db].connection()
        return ConnectionWrapper(self._connection)
