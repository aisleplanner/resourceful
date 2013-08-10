from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
import os
import re


# v = open(os.path.join(os.path.dirname(__file__), 'resourceful', '__init__.py'))
# VERSION = re.compile(r".*__version__ = '(.*?)'", re.S).match(v.read()).group(1)
# v.close()
VERSION = "0.1"

readme = os.path.join(os.path.dirname(__file__), 'README.rst')

requires = [
    "WebOb >= 1.2.3",
    "which >= 1.1.0",
]


setup(name='resourceful',
      version=VERSION,
      description="Simple yet flexible resource management for Python webapps.",
      long_description=open(readme).read(),
      classifiers=[
      ],
      keywords='',
      author='Jon Rosebaugh',
      author_email='jon@inklesspen.com',
      url='',
      license='MIT',
      packages=find_packages('.', exclude=['examples*', 'test*']),
      include_package_data=True,
      tests_require = [],
      # test_suite = "nose.collector",
      zip_safe=True,
      install_requires=requires,
      entry_points = {
      'paste.filter_app_factory': [
          'resourceful = resourceful:make_resourceful',
          'publisher = resourceful:make_publisher',
          'injector = resourceful:make_injector',
      ],
      'resourceful.compilers': [
          'coffee = resourceful.compiler:COFFEE_COMPILER',
          'less = resourceful.compiler:LESS_COMPILER',
          'sass = resourceful.compiler:SASS_COMPILER',
      ],
      'resourceful.minifiers': [
          'cssmin = resourceful.compiler:CSSMIN_MINIFIER',
          'jsmin = resourceful.compiler:JSMIN_MINIFIER',
          'closure = resourceful.compiler:CLOSURE_MINIFIER',
      ]
      }
)
