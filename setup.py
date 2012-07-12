#!/usr/bin/python
from setuptools import setup, find_packages
import os
import sys

def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    f = open(path)
    return f.read()

install_requires = []
pyversion = sys.version_info[:2]
if pyversion < (2, 7) or (3, 0) <= pyversion <= (3, 1):
    install_requires.append('argparse')

setup(
    name='propernoun',
    version='0.0.1',
    packages=find_packages(),

    author='Tommi Virtanen',
    author_email='tommi.virtanen@inktank.com',
    description='Update PowerDNS from DHCP leases & libvirt virtual machines',
    long_description=read('README.rst'),
    license='MIT',
    keywords='libvirt virtualization dns dhcp',
    url="https://github.com/ceph/propernoun",

    install_requires=[
        'setuptools',
        'lxml',
        'pyparsing >=1.5.2',
        'inotifyx >=0.2.0',
        'sqlalchemy >=0.7.8',
        'ipaddr',
        ] + install_requires,

    tests_require=[
        'pytest >=2.1.3',
        'mock >=0.8.0',
        ],

    entry_points={

        'console_scripts': [
            'propernoun = propernoun.cli:main',
            ],

        },
    )
