from setuptools import setup

import os

# Put here required packages
packages = ['Django<=1.6', 'djangorestframework', 'markdown', 'django-filter']

if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
     packages.append('django-redis-cache')
     packages.append('hiredis')

setup(name='Django',
      version='0.0',
      description='A django-openshift quickstart',
      author='Fabio Alessandro Locati',
      author_email='fabio@locati.cc',
      url='http://fabiolocati.net',
      install_requires=packages,
)

