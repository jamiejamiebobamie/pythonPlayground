"""
Turn a string into it's sinusoidal "snake" case. Example:

Input: "GEEKSFORGEEKS"

G       S       G       S
  E   K   F   R   E   K
    E       O       E

Output: "GSGSEKFREKEOE"

"""

import itertools

def stringSinusoid(s):
    result = [[],[],[]]
    iter = 0
    for i, c in enumerate(s):
        result[i%3].append(c)
    print((result)
    return "".join(itertools.chain(*result))

print(stringSinusoid("string"))
