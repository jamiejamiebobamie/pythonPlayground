"""Say you have an array for which the ith element is the price of a given stock on day i.

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

def findMaxPrice(A):
    """Iterate through the array twice once to find the min.
    The second time to see if there is a value larger than that with a higher index.
    If there is find the max and then subtract the min value from the max.
    Otherwise return 0.
    I believe this is O(n) time... well O(2n), but not O(n**2) as nothing is nested...

    That's not going to work either as:
    A = [7,2,5,3,6,4,1]
    will result in a lowest value of 1 and nothing comes after 1 in the array...

    A = [8,7,2,5,3,6,4,1]
    """
    indexMin = indexMax = 0
    for i, item in enumerate(A):

        testMin = A[indexMin]
        testMax = A[indexMax]
        # print(max(A[indexMax], item) - min(A[indexMin], item), testMax - testMin)
        if max(A[indexMax], item) - min(A[indexMin], item) > testMax - testMin:
            if A[indexMin] != testMin:
                indexMin = i
            if A[indexMax] != testMax:
                indexMax = i
        elif testMax - testMin <= 0:
            indexMax = i+1

        print(testMin,testMax)

    return A[indexMax], A[indexMin], A[indexMax] - A[indexMin]

A = [7,2,5,3,6,4,1]
print(findMaxPrice(A))

A = [7,6,4,3,1]
print(findMaxPrice(A))
