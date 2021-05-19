# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in veterinary_application/__init__.py
from veterinary_application import __version__ as version

setup(
	name='veterinary_application',
	version=version,
	description='Vetnerinary Services And Monitoring',
	author='Borealis Systems',
	author_email='info@bslkenya.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
