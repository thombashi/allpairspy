import metacomm.combinatorics.all_pairs2
all_pairs = metacomm.combinatorics.all_pairs2.all_pairs2


"""
Provided to make it easier to compare efficiency with other tools
as per http://pairwise.org/tools.asp

Current iutput is:

3^4: produces 9 rows
3^13: produces 17 rows
4^15 * 3^17 * 2^29: produces 37 rows
4^1 * 3^39 * 2^35: produces 27 rows
3^100: produces 29 rows
10^20: produces 219 rows
10^10: produces 172 rows

"""

def get_arrays( dimensions ):
    opts = []
   
    for d in dimensions:
        r = []
        for i in range(d[1]):
            r.append( range(d[0]) )
        opts += r
            
    return opts

def print_result( dimensions ):
    header_list = []
    for d in dimensions:
        header_list.append( "%i^%i" % d )
    header = " * ".join(header_list)
    
    pairwise = all_pairs( get_arrays( dimensions ) )
    n = len(list(pairwise))
    
    print "%s: produces %i rows" % (header, n)
 
        
print_result(( (3, 4), ))
print_result(( (3, 13), ))
print_result(( (4, 15), (3, 17), (2, 29) ))
print_result(( (4, 1), (3, 39), (2, 35) ))
print_result(( (3, 100), ))
print_result(( (10, 20), ))
print_result(( (10, 10), ))

#!/usr/bin/env python
