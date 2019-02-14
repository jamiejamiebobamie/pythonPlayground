# https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/
#
# Given an array of integers. Find a peak element in it. An array element is peak if it is NOT smaller than its neighbors. For corner elements, we need to consider only one neighbor. For example, for input array {5, 10, 20, 15}, 20 is the only peak element. For input array {10, 20, 15, 2, 23, 90, 67}, there are two peak elements: 20 and 90. Note that we need to return any one peak element.
#
# Following corner cases give better idea about the problem.
# 1) If input array is sorted in strictly increasing order, the last element is always a peak element. For example, 50 is peak element in {10, 20, 30, 40, 50}.
# 2) If input array is sorted in strictly decreasing order, the first element is always a peak element. 100 is the peak element in {100, 80, 60, 50, 20}.
# 3) If all elements of input array are same, every element is a peak element.
#
# It is clear from above examples that there is always a peak element in input array in any input array.
#
# A simple solution is to do a linear scan of array and as soon as we find a peak element, we return it. The worst case time complexity of this method would be O(n).
#
# Can we find a peak element in worst time complexity better than O(n)?
# We can use Divide and Conquer to find a peak in O(Logn) time. The idea is Binary Search based, we compare middle element with its neighbors. If middle element is not smaller than any of its neighbors, then we return it. If the middle element is smaller than the its left neighbor, then there is always a peak in left half (Why? take few examples). If the middle element is smaller than the its right neighbor, then there is always a peak in right half (due to same reason as left half). Following are C and Java implementations of this approach.

from collections import deque as d

array = [10, 20, 15, 2, 23, 90, 67]

array = [100, 80, 60, 50, 20]

array = [0,0,0,0,0,0,0,0,0]

 #negative values???

def findPeak(array):

    peaks = []
    array.append(0)
    queue = d()
    queue.append(0)

    for item in array:
        if len(queue) < 3:
            queue.append(item)
        # print(queue, peaks)
        if len(queue) == 3:
            if queue[1] >= queue[0] and queue[1] >= queue[2]:
                peaks.append(queue[1])
            queue.popleft()

    return peaks

print(findPeak(array))
