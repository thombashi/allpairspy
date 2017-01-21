# encoding: utf-8


from distutils.core import setup

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
    packages=['metacomm', 'metacomm.combinatorics'],
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
