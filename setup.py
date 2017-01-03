#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='montlytotals',
    version='1.1',
    description='Generates daily totals report',
    install_requires=['tabler', 'exchange_rates', ],
    package_data={'templates': 'monthlytotals/report_template.html'},
    include_package_data=True,
    packages=find_packages())
