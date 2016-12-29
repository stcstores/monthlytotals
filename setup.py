#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='montlytotals',
    version='1.0',
    description='Generates daily totals report',
    install_requires=['tabler', 'exchange_rates'],
    packages=find_packages())
