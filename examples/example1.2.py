import metacomm.combinatorics.all_pairs2
all_pairs = metacomm.combinatorics.all_pairs2.all_pairs2

"""
Demo of the basic functionality - just getting pairwise/n-wise combinations
"""


# sample parameters are is taken from 
# http://www.stsc.hill.af.mil/consulting/sw_testing/improvement/cst.html


parameters = [ [ "Brand X", "Brand Y" ]
             , [ "98", "NT", "2000", "XP"]
             , [ "Internal", "Modem" ]
             , [ "Salaried", "Hourly", "Part-Time", "Contr." ]
             , [ 6, 10, 15, 30, 60 ]
             ]

triplewise = all_pairs( parameters, n=3 )

print "TRIPLEWISE:"
for i, v in enumerate(triplewise):
    print "%i:\t%s" % (i, str(v))
    
    