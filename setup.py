# encoding: utf-8

import os.path
import sys

from distutils.core import setup
import setuptools


REQUIREMENT_DIR = "requirements"

needs_pytest = set(["pytest", "test", "ptr"]).intersection(sys.argv)
pytest_runner = ["pytest-runner"] if needs_pytest else []


with open(os.path.join(REQUIREMENT_DIR, "requirements.txt")) as f:
    install_requires = [line.strip() for line in f if line.strip()]

with open(os.path.join(REQUIREMENT_DIR, "test_requirements.txt")) as f:
    tests_require = [line.strip() for line in f if line.strip()]

setup(
    name='allpairspy',
    version='2.0.1',
    description='Pairwise test combinations generator',
    long_description='''Pairwise (aka "all-pairs") test combinations generator written in
Python. Allows one to create a set of tests using "pairwise 
combinations" method, reducing a number of combinations of variables
into a lesser set that covers most situations.
''',
    author="Tsuyoshi Hombashi",
    author_email="gogogo.vm@gmail.com",
    url='https://github.com/thombashi/allpairspy',
    install_requires=install_requires,
    tests_require=tests_require,
    setup_requires=pytest_runner,
    packages=setuptools.find_packages(exclude=["test*"]),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
    ]
)
