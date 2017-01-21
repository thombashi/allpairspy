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


Usage
------------

.. code:: python
    
    from allpairspy import AllPairs

    parameters = [
        ["Brand X", "Brand Y"],
        ["98", "NT", "2000", "XP"],
        ["Internal", "Modem"],
        ["Salaried", "Hourly", "Part-Time", "Contr."],
        [6, 10, 15, 30, 60]
    ]

    print("PAIRWISE:")
    for i, parameter in enumerate(AllPairs(parameters)):
        print("{:2d}: {}".format(i, parameter))

.. code:: 

     0: ['Brand X', '98', 'Internal', 'Salaried', 6]
     1: ['Brand Y', 'NT', 'Modem', 'Hourly', 6]
     2: ['Brand Y', '2000', 'Internal', 'Part-Time', 10]
     3: ['Brand X', 'XP', 'Modem', 'Contr.', 10]
     4: ['Brand X', '2000', 'Modem', 'Part-Time', 15]
     5: ['Brand Y', 'XP', 'Internal', 'Hourly', 15]
     6: ['Brand Y', '98', 'Modem', 'Salaried', 30]
     7: ['Brand X', 'NT', 'Internal', 'Contr.', 30]
     8: ['Brand X', '98', 'Internal', 'Hourly', 60]
     9: ['Brand Y', '2000', 'Modem', 'Contr.', 60]
    10: ['Brand Y', 'NT', 'Modem', 'Salaried', 60]
    11: ['Brand Y', 'XP', 'Modem', 'Part-Time', 60]
    12: ['Brand Y', '2000', 'Modem', 'Hourly', 30]
    13: ['Brand Y', '98', 'Modem', 'Contr.', 15]
    14: ['Brand Y', 'XP', 'Modem', 'Salaried', 15]
    15: ['Brand Y', 'NT', 'Modem', 'Part-Time', 15]
    16: ['Brand Y', 'XP', 'Modem', 'Part-Time', 30]
    17: ['Brand Y', '98', 'Modem', 'Part-Time', 6]
    18: ['Brand Y', '2000', 'Modem', 'Salaried', 6]
    19: ['Brand Y', '98', 'Modem', 'Salaried', 10]
    20: ['Brand Y', 'XP', 'Modem', 'Contr.', 6]
    21: ['Brand Y', 'NT', 'Modem', 'Hourly', 10]


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
