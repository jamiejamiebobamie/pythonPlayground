# Given a non-negative integer n, count all numbers with unique digits, x, where 0 <= x <= 10n.
#
# Example:
#
# Input: 2
# Output: 91
# Explanation: The answer should be the total numbers in the range of 0 <= x <= 100,
#              excluding 11,22,33,44,55,66,77,88,99

# https://leetcode.com/problems/count-numbers-with-unique-digits/

#Bruteforce:
def uniqueDigits(n):
    count = 0
    for _ in range(10**n):
        test = str(_)
        uniqueChars = set()
        unique = True
        for char in test:
            if char in uniqueChars:
                unique = False
                break
            uniqueChars.add(char)
        if unique:
            print(test)
            count+=1

    return count

print(uniqueDigits(3))

# O(n**2) time complexity (sort of)
# O(n) space complexity (sort of)

# I bet there's some trick having to do with the original duplicates that scales with n.
# 99, 102, 103, ..., 109-120,123,

# 9 is the first missing values
# next is 90?
# nope. 739
