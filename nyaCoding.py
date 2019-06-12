A = [3,4,3,0,2,2,3,0,0]
A = [4,2,0]
A = [4,4,3,3,1,0]

def solution(ranks):
    #O(2n) time complexity
    mySet = set() #O(n) space, n == number of unique elements in ranks
    underlings = 0
    for rank in ranks:
        mySet.add(rank)
    for rank in ranks:
        if rank+1 in mySet:
            underlings += 1
    return underlings

print(solution(A))
