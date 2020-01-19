# encoding: utf-8

import io
import os.path
import sys

import setuptools


MODULE_NAME = "allpairspy"
REPOSITORY_URL = "https://github.com/thombashi/{:s}".format(MODULE_NAME)
REQUIREMENT_DIR = "requirements"

pkg_info = {}


def need_pytest():
    return set(["pytest", "test", "ptr"]).intersection(sys.argv)


def get_release_command_class():
    try:
        from releasecmd import ReleaseCommand
    except ImportError:
        return {}

    return {"release": ReleaseCommand}


with open(os.path.join(MODULE_NAME, "__version__.py")) as f:
    exec(f.read(), pkg_info)

with io.open("README.rst", encoding="utf8") as fp:
    long_description = fp.read()

with open(os.path.join(REQUIREMENT_DIR, "requirements.txt")) as f:
    install_requires = [line.strip() for line in f if line.strip()]

with open(os.path.join(REQUIREMENT_DIR, "test_requirements.txt")) as f:
    tests_requires = [line.strip() for line in f if line.strip()]

PYTEST_RUNNER_REQUIRES = ["pytest-runner"] if need_pytest() else []

setuptools.setup(
    name=MODULE_NAME,
    version=pkg_info["__version__"],
    url=REPOSITORY_URL,

    author=pkg_info["__author__"],
    author_email=pkg_info["__author_email__"],
    description="Pairwise test combinations generator",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    license=pkg_info["__license__"],
    maintainer=pkg_info["__maintainer__"],
    maintainer_email=pkg_info["__maintainer_email__"],
    packages=setuptools.find_packages(exclude=["test*"]),
    project_urls={
        "Source": REPOSITORY_URL,
        "Tracker": "{:s}/issues".format(REPOSITORY_URL),
    },

    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires=install_requires,
    setup_requires=PYTEST_RUNNER_REQUIRES,
    tests_require=tests_requires,
    extras_require={
        "release": ["releasecmd>=0.0.18,<0.1.0"],
        "test": tests_requires,
    },

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
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
    cmdclass=get_release_command_class())
