"""
https://leetcode.com/problems/maximum-subarray/
53. Maximum Subarray
Easy

5137

199

Favorite

Share
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle."""


def maxSubArray(nums):
    def __helper(i,sumNum):
        if i+1 < len(nums):
            return max(__helper(i+1,sumNum+nums[i]), __helper(i+1,sumNum))
        else:
            return sumNum
    if len(nums) > 1:
        return max(__helper(0,nums[0]), __helper(0,0))
    else:
        return nums[0]


arr = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(arr))




#
# def longest(array):
#     maxSum = 0
#     theMaxest = float('-inf')
#     for num in array:
#         if num > 0:
#             maxSum+=num
#         elif theMaxest < maxSum+num:
#             maxSum+=num
#             theMaxest = maxSum
#         else:
#             theMaxest = maxSum
#             maxSum = 0
#
#     return theMaxest
