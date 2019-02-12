# https://leetcode.com/problems/minimum-path-sum/
#
# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right
# which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example:
#
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

# array =  [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]

# def minSum(array):
#     positionRow = 0
#     positionCol = 0
#     sum = array[0][0]
#     print(sum)
#     while positionRow < len(array)-1 and positionCol < len(array[0])-1:
#         if array[positionRow+1][positionCol] < array[positionRow][positionCol+1]:
#             positionRow += 1
#             sum += array[positionRow][positionCol]
#             print(sum, array[positionRow][positionCol])
#         elif array[positionRow+1][positionCol] > array[positionRow][positionCol+1]:
#             positionCol += 1
#             sum += array[positionRow][positionCol]
#             print(sum, array[positionRow][positionCol])
#     sum += array[len(array)-1][len(array)-1]
#     return sum
#
#     #wrong^^^^^^^^^^ adds 1 + 1 + 4 (skips 2) + 1,
#
#takes the wrong path as it's not the lowest sum and incorrectly adds sums by omission
#
# print(minSum(array))

# array =  [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
#
# def allPaths(array):
#     #makes a dictionary of key:array index, value:array value at index
#     dict = {}
#     dict[0,0] = array[0][0]
#     for rowI in range(len(array)):
#         for colI in range(len(array[0])):
#             if rowI+1 < len(array) and colI+1 < len(array[0]):
#                 dict[rowI+1,colI] = array[rowI+1][colI]
#                 dict[rowI,colI+1] = array[rowI][colI+1]
#             elif rowI+1 < len(array):
#                 dict[rowI+1,colI] = array[rowI+1][colI]
#             elif colI+1 < len(array[0]):
#                 dict[rowI,colI+1] = array[rowI][colI+1]
#     return dict
#
#
# allValues = list(allPaths(array).values())
# allKeys = list(allPaths(array).keys())
# print(allKeys[0])
# print(allValues[0])


#
# sums = []
# moves = 0
# sums.append(dictValues[moves])
# while moves < len(array)+1:
#     if min(dictValues)
#
#     moves+=1

array =  [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

class Node:
     def __init__(self, downNode=None, rightNode=None):
         self.index = None
         self.value = None
         self.down = downNode
         self.right = rightNode

root = Node()

current = root

moves = 0
rowI = 0
colI = 0
# while moves < len(array)+2:
for rowI in range(len(array)):
    for colI in range(len(array[0])):
    if rowI+1 < len(array) and colI+1 < len(array[0]):
        current.down = array[rowI][colI+1]
        current.right = array[rowI+1][colI]
    elif rowI+1 < len(array):
        current.right = array[rowI+1][colI]
    elif colI+1 < len(array[0]):
        current.down = array[rowI][colI+1]
    rowI += 1
    colI += 1
    current = Node()
    # moves += 1

# Someday pretty baby.


# I have other things to do... it's intelligent to make a tree of nodes
# with each node being a place in the array and with the node's children
# being the right and down moves at each place.
# Once the tree is built, you traverse the nodes from root to leaf,
# each leaf being the same node of value array[len(array)-1][len(array)-1].

# The best path to take is determined as you traverse the nodes and sum their values.

# Is it possible to build the tree and traverse it at the same time?
