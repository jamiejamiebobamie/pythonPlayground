"""Implement a function that converts a spreadsheet column id to the corresponding integer,
with "A" corresponding to 1.
For example you should return 4 for "D", 27 for "AA", 702 for "ZZ", etc.
How would you test your code?
(From pg. 70 of Elements of Programming Interviews in Python)"""


def convert_Column_to_Int(column_id):
    integer = 0
    iter = 0
    alpha = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    # can a list comprehension build a dictionary?
    #e.g. "for character in alpha (alpha = list('abcdefgh...')), map the characer to its index+1"

    while abs(iter) < len(column_id):
        iter -= 1
        integer += 26**(abs(iter)-1) * alpha[column_id[iter]]
    return integer

print(convert_Column_to_Int("ZZZ"))

# I would test this function by writing another function
# that converts back to column_id's using modulus.
# time complexity: O(n). space complexity: O(n)? ...negligible?

#Book's answer:

def ss_decode_col_id(col):
    return reduce(lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0)
