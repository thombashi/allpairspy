# encoding: utf-8

import os.path
import sys

import setuptools


REQUIREMENT_DIR = "requirements"

needs_pytest = set(["pytest", "test", "ptr"]).intersection(sys.argv)
pytest_runner = ["pytest-runner"] if needs_pytest else []

with open(os.path.join(REQUIREMENT_DIR, "requirements.txt")) as f:
    install_requires = [line.strip() for line in f if line.strip()]

with open(os.path.join(REQUIREMENT_DIR, "test_requirements.txt")) as f:
    tests_requires = [line.strip() for line in f if line.strip()]

setuptools.setup(
    name="allpairspy",
    version="2.4.0",
    description="Pairwise test combinations generator",
    long_description="""Pairwise (aka 'all-pairs') test combinations generator written in
Python. Allows one to create a set of tests using 'pairwise combinations' method,
reducing a number of combinations of variables
into a lesser set that covers most situations.
""",
    author="Tsuyoshi Hombashi",
    author_email="tsuyoshi.hombashi@gmail.com",
    url="https://github.com/thombashi/allpairspy",
    install_requires=install_requires,
    tests_require=tests_requires,
    extras_require={
        "test": tests_requires,
    },
    setup_requires=pytest_runner,
    packages=setuptools.find_packages(exclude=["test*"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ])
