# Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].
#
# You need to return the number of important reverse pairs in the given array.
#
# Example1:
#
# Input: [1,3,2,3,1]
# Output: 2
# Example2:
#
# Input: [2,4,3,5,1]
# Output: 3
# Note:
#
# The length of the given array will not exceed 50,000.
# All the numbers in the input array are in the range of 32-bit integer.
#
# https://leetcode.com/problems/reverse-pairs/

A = [2,4,3,5,1]
B = [1,3,2,3,1]

#BRUTE FORCE
#O(n**2) time complexity
def findPairs(A):
    # cache = set()
    result = 0
    for i, item in enumerate(A):
        # i < j and nums[i] > 2*nums[j]
        j = 1
        while j < len(A):
            if i < j and A[i] > 2*A[j]:
                # print(i,j,A[i],A[j])
                result += 1
            j+=1
    return result

# print(findPairs(A))


# key insight is that the index 'i' must be lower than the other and MORE than twice the other's value.
# so large numbers that come early in the array == good.
# but 'large' is relative.

A = [2,4,3,5,1] #3

def buildTree(A):
    class binTreeNode:
        def __init__(self, index=None, value=None, left=None, right=None):
            self.index = index
            self.value = value
            self.left = left
            self.right = right

    #build binary tree #O(n) time
    for i, item in enumerate(A):
        if i == 0:
            root = binTreeNode(i, item)
        else:
            current = parent = root
            new_node = binTreeNode(i, item)
            while current:
                if current.value:
                    if new_node.value < current.value:
                        parent = current
                        current = current.left
                    elif new_node.value > current.value:
                        parent = current
                        current = current.right
                    else: #duplicate value
                        parent = current
                        current = current.left
            else:
                if new_node.value < parent.value:
                    parent.left = new_node
                    # print('left')
                elif new_node.value > parent.value:
                    parent.right = new_node
                    # print('right')
                else: #duplicate value
                    parent.left = new_node
                # print(parent.value, new_node.value)
    return root


def findResult(A):
    result = 0

    def traverseTree(root, j, value):
        # find items in the tree that are larger than the given value
        result = 0
        current = root
        while current:
            if current.value:
                print(value, current.value)
                if value <= current.value:
                    if j > current.index:
                        print(j, value, current.index, current.value)
                        result += 1
                    current = current.right
                else:
                    current = current.left
        return result

    for j, item in enumerate(reversed(A)): # O(2n)
        result += traverseTree(root, len(A)-j-1, item*2) # O(logn)
    return result

A = [2,4,3,5,1] # 3
B = [1,3,2,3,1] # 2

# not working...
root = buildTree(A)
print(findResult(A))
# time complexity == 3nlogn
# O(n) to build the binary tree
# O(n)
