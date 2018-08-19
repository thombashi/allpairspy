#!/usr/bin/env bash

pyver=$(python -c "from __future__ import print_function; import sys; print('{}{}'.format(*sys.version_info[0:2]))")

tox

if [ "$TRAVIS_OS_NAME" = "linux" ] && [ "$pyver" = "36" ]; then
    python setup.py test --addopts "-v --cov allpairspy --cov-report term-missing"
fi
