# given an array, rotate the array to the right k steps where k is a nonegative int.


A = [1,2,3,4,5,6,7]

def rotate(A,k):
    #time complexity is O(2n)-ish
    shift = k % len(A)
    return A[-shift:]+A[:-shift] # slicing == O(n) + concatenation == O(n)


print(rotate(A,3))
