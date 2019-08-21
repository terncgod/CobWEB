#!/usr/bin/env python

from setuptools import setup 

setup(
    name='cobweb',

    version='0.1.5',
    description='Email OSINT Tool',
    url='https://github.com/Cr7pt0nic',
    
    author = 'Crypto',
    author_email='Cr7pT0@protonmail.com',
    license='MIT',

    install_requires = ['colorama','requests','urllib3'],
    console =['cobweb.py'],
)
