#!/usr/bin/env python
from distutils.core import setup
from rpy.version import version

setup(
    name='RaspberryPy',
    version=version,
    description='A Pythonic environment for learning Python on the RaspberryPi'\
        ' device.',
    long_description=open('README').read(),
    author='Nicholas Tollervey',
    author_email='ntoll@ntoll.org',
    url='http://packages.python.org/RaspberryPy/',
    packages=['rpy'],
    scripts=['bin/rpy'],
    license='MIT',
)
