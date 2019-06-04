"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000]."""

A = [3,8,9,3,1,2,3,2,4,5,6,-1,2,3,5,-4,7,10]

def findLowestInArray(A):
    entriesSeen = set()
    minimum = 1
    for item in A:
        if item == minimum:
            minimum += 1
            while minimum in entriesSeen:
                minimum += 1
        entriesSeen.add(item)
    return minimum

print(findLowestInArray(A))
