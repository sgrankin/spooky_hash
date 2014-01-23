#!/usr/bin/env python
from ez_setup import use_setuptools
use_setuptools()

import sys
from setuptools import setup, Extension

try:
    from Cython.Distutils import build_ext
    from Cython.Build import cythonize
except ImportError:
    print("Could not import Cython. Install `cython` and rerun.")
    sys.exit(1)

setup(
  name='spooky_hash',
  version='1.0',

  description='Python wrapper for SpookyHash V2',
  author='Sergey Grankin',
  url='https://github.com/sgrankin/spooky_hash',

  setup_requires=['nose>=1.0'],
  include_package_data=True,
  ext_modules=cythonize(
    [
      Extension(
        'spooky_hash',
        ['src/spooky_hash.pyx', 'src/SpookyV2.cpp'],
        language='c++'),
    ],
  ),
)
