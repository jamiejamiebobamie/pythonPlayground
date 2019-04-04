"""
Elements of Programmign Interviews in Python
pg 210

Design an algorithm that takes three sorted arrays and returns one entry from
each such that the minimum interval containing these three entries is as small
as possible.

For example:
Input: [5,10,15], [3,6,9,12,15], [8,16,24]
Output: [15,15,16]

( Interval: 1 =  abs(15-16) )


"""

import collections

A1 = [5,10,15]
A2 = [3,6,9,12,15]
A3 = [8,16,24]

def findThree(A1,A2,A3):
    i = j = k = 0

    result = collections.namedtuple('result',('A1','A2','A3','difference'))

    result.A1 = A1[0]
    result.A2 = A2[0]
    result.A3 = A3[0]
    result.difference = max(abs(result.A1-result.A3), max(abs(result.A1-result.A2),abs(result.A2-result.A3)))

    while i < len(A1) or j < len(A2) or k < len(A3):
        if i < len(A1):
            if result.difference > max(abs(A1[i]-result.A3), max(abs(A1[i]-result.A2),abs(result.A2-result.A3))):
                result.difference = max(abs(A1[i]-result.A3), max(abs(A1[i]-result.A2),abs(result.A2-result.A3)))
                result.A1 = A1[i]
            print("A1",A1[i])
            i+=1
        if j < len(A2):
            if result.difference > max(abs(result.A1-result.A3), max(abs(result.A1-A2[j]),abs(A2[j]-result.A3))):
                result.difference = max(abs(result.A1-result.A3), max(abs(result.A1-A2[j]),abs(A2[j]-result.A3)))
                result.A2 = A2[j]
            print("A2",A2[j])
            j+=1
        if k < len(A3):
            if result.difference > max(abs(result.A1-A3[k]), max(abs(result.A1-result.A2),abs(result.A2-A3[k]))):
                result.difference = max(abs(result.A1-A3[k]), max(abs(result.A1-result.A2),abs(result.A2-A3[k])))
                result.A3 = A3[k]
            print("A3",A3[k])
            k+=1
    return result.A1, result.A2, result.A3, result.difference

print(findThree(A1,A2,A3))
