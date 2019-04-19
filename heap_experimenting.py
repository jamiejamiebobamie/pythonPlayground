

"""
Given an unsorted array, return the 2nd largest element.
"""

import heapq

A = [1001,22,3,45,56,666,75,8,90,100,11]

my_first_heap = heapq.heapify(A) #time complexity? O(n) or O(nlogn)
print(A) #checking to see if it worked... heapify is in place, apparently.
for i, item in enumerate(A):
    if 2*i+2 < len(A):
        print(A[i], A[2*i+1], A[2*i+2]) #testing heap property.
                                        #a heap is perfect binary tree with nodes
                                        #that are arranged according to
                                        #the heap property: a parent node is as
                                        #large or larger than the value of its
                                        #children.

                                        #a heap in python is represented as an array
                                        #where each item at index i has children
                                        #at indices 2*i+1 and 2*i+2.


#                         3
#             8                   75
#     22           11        666      1001
# 45     90    100    56

#returns the second largest element:
print(heapq.nlargest(2,A)[1]) #666


"""
'Given an unsorted array, return the 2nd largest element.'

import heapq

A = [1001,22,3,45,56,666,75,8,90,100,11]

heapq.heapify(A)
print(heapq.nlargest(2,A)[1])
"""


#python heapq module only provides functionality for a min heap, which is good
#when you're trying to find the LARGEST elements.

#if you want a max heap, you have to insert the negative of the values in the array

B = [1001,22,3,45,56,666,75,8,90,100,11]

#baby's first list comprehension...
B = [b*-1 for b in B]
print(B)
heapq.heapify(B)
print(B)
#i forgot there's also nsmallest:
print(heapq.nsmallest(2,A)[1])
#here's the second smallest item form the max heap:
print(-1*heapq.nlargest(2,B)[1])
#what is the time complexity between these two methods?
#it would seem like nlargest from B might be more performant.
