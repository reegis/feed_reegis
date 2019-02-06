#! /usr/bin/env python

from setuptools import setup
import os

if not os.environ.get('READTHEDOCS') == 'True':
    requirements = [
        'oemof >= 0.2.1',
        'pandas >= 0.21.0, < 0.25',
        'demandlib',
        'tables',
        'matplotlib',
        'shapely',
        'windpowerlib',
        'pvlib < 0.7',
        'geopandas < 0.5',
        'requests',
        'numpy < 1.17',
        'workalendar',
        'owslib',
        'pyproj',
        'pytz',
        'python-dateutil',
        'networkx',
        'dill',
        'PyQt5',
        'cython',
        'xlrd',
        'Rtree']
else:
    requirements = ['oemof', 'cycler']


setup(name='reegis',
      version='0.0.1',
      author='Uwe Krien',
      author_email='uwe.krien@posteo.eu',
      description='Open geospatial data model',
      package_dir={'reegis': 'reegis'},
      install_requires=requirements)
