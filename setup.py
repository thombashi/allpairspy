
from distutils.core import setup

setup(
      name = 'AllPairs'
    , version = '2.0.1'
    , description = 'Pairwise test combinations generator'
    , long_description = '''Pairwise (aka "all-pairs") test combinations generator written in
Python. Allows one to create a set of tests using "pairwise 
combinations" method, reducing a number of combinations of variables
into a lesser set that covers most situations.
'''
    , author = 'MetaCommunications Engineering'
    , author_email = 'metacomm@users.sourceforge.net'
    , url='http://apps.sourceforge.net/trac/allpairs/'
    , packages = [ 'metacomm', 'metacomm.combinatorics' ]
    , classifiers =
        [
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'Intended Audience :: Science/Research',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.3',
          'Programming Language :: Python :: 2.4',
          'Programming Language :: Python :: 2.5',
          'Topic :: Software Development :: Testing',
          'Topic :: Utilities',
        ]
    )
