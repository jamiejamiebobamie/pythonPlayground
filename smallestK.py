# https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/

arr = [7, 10, 4, 3, 20, 15]
k = 3

def returnK(array, s_or_l, k):
    array.sort()
    if s_or_l == "s":
        return arr[k-1]
    elif s_or_l == "l":
        return arr[-k]

print(returnK(arr, "l", k))
