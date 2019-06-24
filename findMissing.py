# following along to this video: https://interviewing.io/recordings/Python-Airbnb-4


# write a fucntion that takes in two arrays
# and finds the one element that is missing from the second array

# a good question to ask is if the items are sorted and all unique?

def findMissing(A1, A2):
    # n is the number of elements in A1
    matches = set(A2) #O(n-1)

    for item in A1: # less than O(n)
        if not item in matches:
            return item

    return "wrong input"


A1 = [1,2,3,4,5,6,7,8,9,10]
A2 = [1,2,3,4,5,6,8,9,10]

print(findMissing(A1, A2)) # time complexity is less than O(2n)


def findMissingLowSpace(A1, A2):
    # O(2n) time, O(1ish) space though you can't be sure of size of int

    sum1 = sum2 = 0

    for item in A1:
        sum1 += item
    for item in A2:
        sum2 += item
    return sum1 - sum2


print(findMissingLowSpace(A1,A2))


#interview O(1) space solution:

def find_missing_xor(A1, A2):
    xor_sum = 0
    for num in A1:
        xor_sum ^= num
    for num in A2:
        xor_sum ^= num

    return xor_sum

print(find_missing_xor(A1, A2))
