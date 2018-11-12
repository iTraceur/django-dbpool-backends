# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from setuptools import find_packages

__version__ = '0.0.1'

setup(
    name='django-dbpool-backends',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/iTraceur/django-dbpool-backends',
    license='MIT License',
    author='iTraceur',
    author_email='iTraceur.cn@gmail.com',
    description='''A mysql / postgres database backend for Django which
                provides persistence connection pools implemented by DBUtils.
                ''',
    long_description='README.md',
    classifiers=[
        'Topic :: Database :: Libraries',
        'Development Status :: 3 - beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Programming Language :: Python',
    ],
    install_requires=[
        'Django>=1.8.2'
    ]
)
