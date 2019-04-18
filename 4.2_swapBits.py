"""

given an array that contains a 64 bit integer representing a word
with the integer at index 0 representing the LSB and the integer at index 63
representing the MSB

implement a function that takes a 64 bit integer and swaps the bits at indices
i an j

"""

#brute force: time complexity O(n) space complexity: O(n)
#my approach:
def swapBits(x, i, j):
    result = []
    string_int = str(x)
    if string_int[i] != string_int[j]:
        for index, bit in enumerate(string_int):
            if index == i:
                result.append(string_int[j])
                continue
            elif index == j:
                result.append(string_int[i])
                continue
            else:
                result.append(bit)
    return "".join(result)

#solution page 27
# time complexity: O(1)
def swap_bits(x, i, j):
    #Extract the i-th and j-th bits, and see if they differ.
    if (x >> i) & 1 != (x >> j) & 1:
        #i-th and j-th bits differ. we will swap them by flipping their values.
        #Select the bits to flip with bit_mask since x^1 = 0 when x = 1 and 1
        #when x = 0, we can perform the flip XOR.
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x

test = 10001
print(swapBits(test, 2,4))

#the book's solutions aren't giving me the same/right answers.
print(swap_bits(test,2,4))
print((test >> 4))
