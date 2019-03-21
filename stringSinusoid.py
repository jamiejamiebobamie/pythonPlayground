"""
Turn a string into a sinusoidal "snake" fashion. Example:

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
    print(result)
    return "".join(itertools.chain(*result))

print(stringSinusoid("string"))


#from Elements of Programming Interviews in Python, page 78:

def snake_string_pythonic(s):
    return s[1::4] + s[::2] + s[3::4]

print(snake_string_pythonic('string'))

#[['s', 'i'], ['t', 'n'], ['r', 'g']]
# sitnrg

# the book wants you to start on line 2:
#1  t   g
#2 s r n
#3    i
# Output: tgsrni

# my program starts on line 1:
#1  s  i
#2   t  n
#3    r  g

#mine doesn't work... mine's like descending fashion...
