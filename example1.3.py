import metacomm.combinatorics.all_pairs2
all_pairs = metacomm.combinatorics.all_pairs2.all_pairs2

"""
Demo of the basic functionality - just getting pairwise combinations
and skipping previously tested pairs.
"""


# sample parameters are is taken from 
# http://www.stsc.hill.af.mil/consulting/sw_testing/improvement/cst.html


parameters = [ [ "Brand X", "Brand Y" ]
             , [ "98", "NT", "2000", "XP"]
             , [ "Internal", "Modem" ]
             , [ "Salaried", "Hourly", "Part-Time", "Contr." ]
             , [ 6, 10, 15, 30, 60 ]
             ]

             
tested = [ [ "Brand X", "98", "Modem", "Hourly", 10 ]
         , [ "Brand X", "98", "Modem", "Hourly", 15 ]
         , [ "Brand Y", "NT", "Internal", "Part-Time", 10 ]
         ]
             
pairwise = all_pairs( parameters, previously_tested=tested )

print "PAIRWISE:"
for i, v in enumerate(pairwise):
    print "%i:\t%s" % (i, str(v))


    