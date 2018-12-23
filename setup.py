#!/usr/bin/env python3

 # NOTES:
 #
 #   Use chrome to determin XPATH cause chrome uses a shorter format and firefox gives
 #   the whole path...
 #
__license__ = 'MIT'
__version__ = '3.0.1'
__date__ = '2018'
__author__ = 'Jarad Dingman'
__maintainer__ = 'Jarad Dingman'
__email__ = 'jayrad1996@gmail.com'
__status__ = 'Testing'

from setuptools import setup, find_packages
import boop

requires = [
    "scapy", "PyRIC", "netaddr"
]

setup(name='boop',
    version=__version__,
    description="My wireless tool",
    long_description="Use it or don't",
    url='',
    download_url="https://github.com/MisterBianco/boopsuite/archive/"+__version__+".tar.gz",
    author=__author__,
    author_email=__email__,
    maintainer=__maintainer__,
    maintainer_email=__email__,
    license=__license__,
    install_requires=requires,
    classifiers=['Development Status :: 5 - Production/Stable',
                'Intended Audience :: Developers',
                'Topic :: Security',
                'Topic :: Software Development',
                'Topic :: Software Development :: Libraries',
                'Topic :: Security',
                'Topic :: System :: Networking',
                'Topic :: Utilities',
                'Operating System :: POSIX :: Linux',
                'Programming Language :: Python :: 3.6',
                'Programming Language :: Python :: 3.7'],
    keywords='Linux Python wireless packet capture security hacking',
    packages=find_packages(),
    package_data={}
)
