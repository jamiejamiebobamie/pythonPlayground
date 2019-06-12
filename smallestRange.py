# You have k lists of sorted integers in ascending order.
# Find the smallest range that includes at least one number from each of the k lists.
#
# We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.
#
# Example 1:
#
# Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# Output: [20,24]
# Explanation:
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
# Note:
#
# The given list may contain duplicates, so ascending order means >= here.
# 1 <= k <= 3500
# -105 <= value of elements <= 105.
# For Java users, please note that the input type has been changed to List<List<Integer>>.
# And after you reset the code template, you'll see this point.

# https://leetcode.com/problems/smallest-range/

A=[[4,10,15,24,26],
   [0,9,12,20],
   [5,18,22,30]]

def smallRange(A):
    smallest_range = [float('inf'),float("-inf")]
    dict = {}
    num_of_k_sorted_arrays = len(A)
    for i in range(len(A)):
        dict[i] = [0,-1, len(A[i])] # create front and back indexes for each list and get list length
        smallest_range[0] = min(A[i][0],smallest_range[0]) # find low of max range
        smallest_range[1] = max(A[i][-1],smallest_range[1]) # find high of max range

    # iterate through each interior array
    # update the smallest_range array with a new_value from one of the interior arrays
    # if the new value makes the range smaller (smallest_range[1]-smallest_range[0])
    # before updating check to ensure that the each interior has a value within the new range
    for i, a in enumerate(A):
        while dict[i][2] > 0:
            if smallest_range[1] - a[dict[i][0]] < smallest_range[1] - smallest_range[0]:
                test = a[dict[i][0]]
                number_to_pass = 0
                for a in A:
                    for num in a:
                        if num > test:
                            number_to_pass += 1
                if number_to_pass == num_of_k_sorted_arrays:
                    smallest_range[0] = test
            if dict[i][0] < dict[i][2] - 1:
                dict[i][0] += 1

            if a[dict[i][1]] - smallest_range[0] < smallest_range[1] - smallest_range[0]:
                test = a[dict[i][1]]
                number_to_pass = 0
                for a in A:
                    for num in a:
                        if num > test:
                            number_to_pass += 1
                if number_to_pass == num_of_k_sorted_arrays:
                    smallest_range[1] = test
            if dict[i][0] - 1 > 0:
                dict[i][1] -= 1

            dict[i][2] -= 1

    print(smallest_range)



smallRange(A)
