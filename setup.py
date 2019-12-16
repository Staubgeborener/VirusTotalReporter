#!/usr/bin/env python
# encoding: utf-8

import os
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name='VirusTotalReporter',
    version='0.5',
    packages=find_packages(),
    install_requires=required,
    url='https://github.com/Staubgeborener/VirusTotalReporter',
    license='MIT',
    author='Eric Schröder',
    description='checks files/content of folders with VirusTotal Database and create html report',
    long_description=readme,
    long_description_content_type = "text/markdown"
)
