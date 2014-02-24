#!/usr/bin/env python
from ez_setup import use_setuptools
use_setuptools()

import sys
from setuptools import setup, Extension

try:
    from Cython.Build import cythonize
    extensions = cythonize([
        Extension(
            'spooky_hash',
            ['src/spooky_hash.pyx', 'src/SpookyV2.cpp'],
            language='c++'),
    ])
except ImportError:
    extensions = [
        Extension(
            'spooky_hash',
            ['src/spooky_hash.cpp', 'src/SpookyV2.cpp'],
            language='c++'),
    ]

long_description = open('README.md').read()
try:
    import pypandoc
    long_description = pypandoc.convert(long_description, 'rst', format='md')
except:
    pass

setup(
    name='spooky_hash',
    version='1.0.1',

    description='Python wrapper for SpookyHash V2',
    author='Sergey Grankin',
    url='https://github.com/sgrankin/spooky_hash',
    long_description = long_description,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Cython',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development',
    ],

    setup_requires=[
        'nose>=1.0',
        'setuptools_git >= 0.3',
    ],
    include_package_data=True,
    ext_modules=extensions,
)
