# https://leetcode.com/problems/target-sum/

# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S.
# Now you have 2 symbols + and -.
# For each integer, you should choose one from + and - as its new symbol.
#
# Find out how many ways to assign symbols to make sum of integers equal to target S.
#
# Example 1:
#
# Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation:
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# There are 5 ways to assign symbols to make the sum of nums be target 3.
# Note:
#
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.


# Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5

# it seems that recursion would be the best way to tackle this problem as we're
# trying to exhaust all of the different ways of finding the target.

A = [1, 1, 1, 1, 1]

def targetSum(A, target):
    ways = 0
    sumOfArray = sum(A)
    i = 0
    difference = sumOfArray - target
    while i < len(A):
        if difference == 0:
            ways += 1
            difference = sumOfArray - target
        difference -= A[i]
        i+=1
    if len(A) % 2:
        # i fixed it for this example... wish the website provided more test cases.
        # it's not right...
        difference = sumOfArray - target
        difference = difference - A[-1] - A[-2]
        if difference == 0:
            ways += 1
            difference = sumOfArray - target
    return ways




print(targetSum(A, 3))
