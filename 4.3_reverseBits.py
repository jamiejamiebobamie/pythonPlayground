"""

Write a program that takes a 64 bit word and reverse the bits.

"""


# BruteForce
def reverseBits(x):
    hey = list(str(x)) #O(n)
    result = [] #O(1)
    for h in hey: #O(n)
        bit = int(h) #O(1)
        bit ^= 1 #O(1)
        bit = str(bit) #O(1)
        result.append(bit) #O(1)
    return int("".join(reversed(result))) #O(nlogn)


test = 11011011011
print(reverseBits(test))

#book's solution page 28:
def reverse_bits(x):
    #book's solution is to use a precomputed lookup table with keys that are 16
    #digits long and values that are the inverse of the keys (also 16 digits long)
    #if the input is 64 bit words there are 4 lookups into the table starting with
    #the LSB 16 digits and working your way up to build the word.
    #the book uses bitwise operator '|' ('or') to join the word parts as if concantenating
    #a string.
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    #...
    return
