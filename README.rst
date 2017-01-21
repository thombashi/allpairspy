.. image:: https://badge.fury.io/py/allpairspy.svg
    :target: https://badge.fury.io/py/allpairspy

.. image:: https://img.shields.io/pypi/pyversions/allpairspy.svg
   :target: https://pypi.python.org/pypi/allpairspy

.. image:: https://img.shields.io/travis/thombashi/allpairspy/master.svg?label=Linux
    :target: https://travis-ci.org/thombashi/allpairspy

.. image:: https://img.shields.io/appveyor/ci/thombashi/allpairspy/master.svg?label=Windows
    :target: https://ci.appveyor.com/project/thombashi/allpairspy

.. image:: https://coveralls.io/repos/github/thombashi/allpairspy/badge.svg?branch=master
    :target: https://coveralls.io/github/thombashi/allpairspy?branch=master


AllPairs test combinations generator 
------------------------------------------------

AllPairs is an open source test combinations generator written in 
Python, developed and maintained by MetaCommunications Engineering.
The generator allows one to create a set of tests using "pairwise 
combinations" method, reducing a number of combinations of variables
into a lesser set that covers most situations.

For more info on pairwise testing see http://www.pairwise.org.

The easiest way to get started is to check out usage examples in 
the "examples" directory and online at
https://apps.sourceforge.net/trac/allpairs/browser/examples/.


Features
--------

* Produces good enough dataset.

* Pythonic, iterator-style enumeration interface.

* Allows to filter out "invalid" combinations during search for the next combination.

* Allows to exclude "previously tested" pairs/combinations.

* Goes beyond pairs! If/when required can generate n-wise combinations.


Installation
------------

.. code::

    pip install allpairpy


Known issues
------------

* Not optimal - there are tools that can create smaller set covering
  all the pairs. However, they are missing some other important 
  features and/or do not integrate well with Python.

* Lousy written filtering function may lead to full permutation of  parameters.

* Version 2.0 has become slower (a side-effect of introducing ability to produce n-wise combinations).


Feedback
--------
  
Please submit patches, bug reports, and feature requests here:
http://apps.sourceforge.net/trac/allpairs/newticket

Other inquires can be directed to 
metacomm(at)users.sourceforge.net
