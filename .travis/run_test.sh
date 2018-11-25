#!/usr/bin/env bash

if [ "$TOXENV" != "cov" ] ; then
    tox
fi
