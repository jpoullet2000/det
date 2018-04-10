# coding: utf-8

import sys
import os
from setuptools import setup, find_packages

NAME = "det"

here = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, here)
from det import __version__ as version

with open(os.path.join(here, 'README.rst')) as readme_file:
    readme = readme_file.read()

requirements_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'requirements.txt')
test_requirements_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test-requirements.txt')

with open(requirements_path) as requirements_file:
    requirements = requirements_file.readlines()

with open(test_requirements_path) as test_requirements_file:
    test_requirements = test_requirements_file.readlines()

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

setup(
    name=NAME,
    version=version,
    description="Data engineering toolkit API",
    author_email="jeanbaptistepoullet@statrgy.com",
    url="",
    keywords=["Swagger", "Data engineering toolkit API"],
    install_requires=requirements,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['det=det.__main__:main']},
    long_description="""\
    Data engineering toolkit API
    """
)

