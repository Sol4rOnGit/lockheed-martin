from itertools import permutations, combinations, product
import itertools
#Used to save on nested loops

itertools.permutations
"""
Returns every possible ordering

permutations(range(3), 2) --> (0,1), (0,2), (1,0), (1,2), (2,0), (2,1)
"""
print(permutations(range(3), 2))

itertools.combinations
"""
Returns every subset of size r, no repeats where order doesn't matter.

combinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)
"""

print(combinations(range(4), 3))

itertools.product
"""
Replaces nested loops.
"""

list(product([1, 2], ['a', 'b'])) # -> [(1,'a'), (1,'b'), (2,'a'), (2,'b')]

#Equivalent to

for x in [1, 2]:
    for y in ["a", "b"]:
        print(x, y)

#Scales very well, can even do product(a, b, c, d)
