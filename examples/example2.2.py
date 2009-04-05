import functools

import metacomm.combinatorics.all_pairs2
all_pairs = metacomm.combinatorics.all_pairs2.all_pairs2


"""
Another demo of filtering capabilities.
Demonstrates how to use named parameters
"""

# sample parameters are is taken from 
# http://www.stsc.hill.af.mil/consulting/sw_testing/improvement/cst.html


parameters = [ ( "brand"
               , [ "Brand X", "Brand Y" ] )
             , ( "os"
               , [ "98", "NT", "2000", "XP"] )
             , ( "network"
               , [ "Internal", "Modem" ] )
             , ( "employee"
               , [ "Salaried", "Hourly", "Part-Time", "Contr." ] )
             , ( "increment"
               , [ 6, 10, 15, 30, 60 ] )
             ]

                 
def is_valid_combination( values, names ):

    dictionary = dict( zip( names, values ) )

    """
    Should return True if combination is valid and False otherwise.
    
    Dictionary that is passed here can be incomplete.
    To prevent search for unnecessary items filtering function
    is executed with found subset of data to validate it.
    """

    rules = [ lambda d: "98" == d["os"] and "Brand Y" == d["brand"] # Brand Y does not support Windows 98
            , lambda d: "XP" == d["os"] and "Brand X" == d["brand"] # Brand X does not work with XP
            , lambda d: "Contr." == d["employee"] and d["increment"] < 30 # Contractors are billed in 30 min increments
            ]
    
    for rule in rules:
        try:
            if rule(dictionary):
                return False
        except KeyError: pass
    
    return True
          
             
pairwise = all_pairs(
      [ x[1] for x in parameters ]
    , filter_func = lambda values: is_valid_combination( values, [ x[0] for x in parameters ] )
    )

for i, v in enumerate(pairwise):
    print "%i:\t%s" % (i, str(v))





        