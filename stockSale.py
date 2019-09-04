"""

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

# def findMaxPrice(A):
#     """Iterate through the array twice once to find the min.
#     The second time to see if there is a value larger than that with a higher index.
#     If there is find the max and then subtract the min value from the max.
#     Otherwise return 0.
#     I believe this is O(n) time... well O(2n), but not O(n**2) as nothing is nested...
#
#     That's not going to work either as:
#     A = [7,2,5,3,6,4,1]
#     will result in a lowest value of 1 and nothing comes after 1 in the array...
#
#     A = [8,7,2,5,3,6,4,1]
#     """
#     indexMin = indexMax = 0
#     for i, item in enumerate(A):
#
#         testMin = A[indexMin]
#         testMax = A[indexMax]
#         # print(max(A[indexMax], item) - min(A[indexMin], item), testMax - testMin)
#         if max(A[indexMax], item) - min(A[indexMin], item) > testMax - testMin:
#             if A[indexMin] != testMin:
#                 indexMin = i
#             if A[indexMax] != testMax:
#                 indexMax = i
#         elif testMax - testMin <= 0:
#             indexMax = i+1
#
#         print(testMin,testMax)
#
#     return A[indexMax], A[indexMin], A[indexMax] - A[indexMin]
#
# A = [7,2,5,3,6,4,1]
# print(findMaxPrice(A))
#
# A = [7,6,4,3,1]
# print(findMaxPrice(A))



# we want to keep track of the min and max to get the maximum profit
# a max price must come after the index of the minimum price to be valid


"""

A = [7,6,4,3,1] == A[?] - A[?] = 0
A = [7,2,5,3,6,4,1] == A[4] - A[1] = 4
A = [8,7,2,5,3,6,4,1] == A[5] - A[2] = 4
A = [1,1,0,2,3,5] == A[5] - A[0?1] = 4

set the minIndex to be 0
set the maxIndex to be 1
set a boolean that stores if the min/max are valid
    (the min is less than the max and at an earlier index). set to false.

iterate through a range of numbers starting from 2 and ending at the length of the array
    (the range method is not inclusive at the upper bounds so this will work with array indices)

compare maxIndex, minIndex, A[i] element.
if the boolean is false, check for valid min/max.

    A = [7,2,5,3,6,4,1] == A[4] - A[1] = 4

    min = 7
    max = 2
    A[2] = 5

    if min > max:
        if A[i] > max:
            max, min = A[i], max
            bool = true

    if bool is never set to true then the array is sorted in descending order

"""

def findMaxPrice(A):
    """This method works for the given test inputs, but I am not sure if it works on all
    array configurations...
    """
    minIndex = 0
    maxIndex = 1
    valid = False

    for _ in range(2, len(A)):

        if A[minIndex] > A[maxIndex]:
            if A[_] > A[maxIndex]:
                maxIndex, minIndex = _, maxIndex
                valid = True

        if A[maxIndex] < A[_] and minIndex < _:
            maxIndex = _
        if A[minIndex] > A[_] and maxIndex > _:
            minIndex = _

        # print(_, A[minIndex], A[maxIndex], A[_])

    return (A[maxIndex] - A[minIndex]) if valid else 0


A = [7,2,5,3,6,4,1]
print(findMaxPrice(A))

A = [7,6,4,3,1]
print(findMaxPrice(A))

A = [7,1,5,3,6,4]
print(findMaxPrice(A))
