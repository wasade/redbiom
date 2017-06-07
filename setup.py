#!/usr/bin/env python

# ----------------------------------------------------------------------------
# Copyright (c) 2016--, redbiom development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop

# based on http://stackoverflow.com/a/36902139

def _post():
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        _post()


class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)
        _post()


# pypi does not render markdown.
# https://stackoverflow.com/a/26737672/19741
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()


# adapted from q2cli's setup.py

setup(
    name='redbiom',
    version='2017.6.3',
    license='BSD-3-Clause',
    author='Daniel McDonald',
    author_email='wasade@gmail.com',
    url='https://github.com/biocore/redbiom',
    packages=find_packages(),
    long_description=long_description,
    include_package_data=True,
    install_requires=['click >= 6.7', 'biom-format >= 2.1.5', 'requests',
                      'h5py', 'pandas', 'nltk', 'joblib',
                      'scikit-bio >= 0.4.2'],
    entry_points='''
        [console_scripts]
        redbiom=redbiom.commands:cli
    ''',
    cmdclass={'install': PostInstallCommand,
              'develop': PostDevelopCommand}
)
