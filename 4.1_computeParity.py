"""

Compute the parity of a very large word of 64bits.
The parity of word is 1 if the number of one's in the word is odd. Otherwise it is 0.
problem 4.1 in Elements of Programming Interviews
"""

# 1110 == 14
#
# 10 == 2
#
# 1 == 1
#
# 111 == 7
#
# all have a parity of 1
#
# how do we do this without iterating through the entire word? O(n)

#brute force: time complexity is O(n)
#my solution:
def computeParity(word):
    count=0
    for bit in str(word):
        if bit == '1':
            count+=1
    return 1 if count % 2 else 0


#page 25's solution. time complexity O(k)
def parity1(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1 # removes the lowest set bit
    return result


#page 26's solution. time complexity O(logn)
def parity2(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1

word1 = 111
#my function and the book's functions are giving me oppposite results:
print(computeParity(word1)) #   1
print(parity1(word1))       #   0
print(parity2(word1))       #   0
                            #   :(
                            
# the parity is 1 if the number of 1's is odd...
