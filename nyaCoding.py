# A = [3,4,3,0,2,2,3,0,0]
# A = [4,2,0]
# A = [4,4,3,3,1,0]
#
# def solution(ranks):
#     #O(2n) time complexity
#     mySet = set() #O(n) space, n == number of unique elements in ranks
#     underlings = 0
#     for rank in ranks:
#         mySet.add(rank)
#     for rank in ranks:
#         if rank+1 in mySet:
#             underlings += 1
#     return underlings
#
# print(solution(A))


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    result = []
    if N % 2:
        for _ in range(N//2):
            if _ == 0:
                result.append(-1)
                result.append(-2)
                result.append(3)
            else:
                value = _ + 3
                result.append(value)
                result.append(value*-1)
    else:
        for _ in range(N/2):
            value = _ + 1
            result.append(value)
            result.append(value*-1)
    return result
