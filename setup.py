#!/usr/bin/env python3

"""Installation script for songbook.

$ python setup.py install
"""
from patacrep import __version__

from setuptools import setup

import sys
import os
import site


SETUP = {"name": 'patacrep',
        "version": __version__,
        "description": 'Songbook compilation chain',
        "author": 'The Songbook team',
        "author_email": 'crep@team-on-fire.com',
        "url": 'https://github.com/patacrep/patacrep',
        "packages": ['patacrep', 'patacrep.content', 'patacrep.latex'],
        "license": "GPLv2 or any later version",
        "scripts": ['songbook'],
        "requires": [
            "argparse", "codecs", "distutils", "fnmatch", "glob", "json",
            "locale", "logging", "os", "re", "subprocess", "sys",
            "textwrap", "unidecode", "jinja2", "chardet"
            ],
        "install_requires": [
            "argparse", "unidecode", "jinja2", "chardet", "ply"
            ],
        "package_data": {'patacrep': [  'data/latex/*',
                                        'data/templates/*',
                                        'data/examples/*.sb',
                                        'data/examples/*/*.sg',
                                        'data/examples/*/*.ly',
                                        'data/examples/*/*.jpg',
                                        'data/examples/*/*.png',
                                        'data/examples/*/*.png',
                                        'data/examples/*/*/header']},
        "classifiers": [
            "Environment :: Console",
            "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
            "Natural Language :: English",
            "Operating System :: POSIX :: Linux",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: MacOS :: MacOS X",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Topic :: Utilities",
            ],
        "platforms": ["GNU/Linux", "Windows", "MacOsX"]
}

if sys.platform.startswith('win32'):
    from shutil import copy
    copy("songbook", "songbook.py")
    SETUP["scripts"] = ['songbook.py']

setup(**SETUP)