#! /usr/bin/env python

from setuptools import setup

setup(name='reegis',
      version='0.0.1',
      author='Uwe Krien',
      author_email='uwe.krien@posteo.eu',
      description='Open geospatial data model',
      package_dir={'reegis': 'reegis'},
      install_requires=['oemof >= 0.1.0',
                        'pandas >= 0.21.0',
                        'demandlib',
                        'tables',
                        'matplotlib',
                        'shapely',
                        'windpowerlib',
                        'pvlib==v0.6.1-beta',
                        'geopandas',
                        'requests',
                        'numpy >= 0.16',
                        'geoplot',
                        'workalendar',
                        'owslib',
                        'pyproj',
                        'pytz',
                        'python-dateutil',
		        'networkx',
			'dill', 'PyQt5']
      )
