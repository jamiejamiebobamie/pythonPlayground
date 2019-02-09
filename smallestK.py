# https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/


# array.sort() = sorts in place RUNTIME: nlog(n)
# sorted() = makes a new array and requires a new variable

arr = [7, 7,7, 6, 4, 7, 10, 4, 3, 20, 15]
k = 2

#array has no duplicates
def returnK(array, s_or_l, k):
    array.sort() #what's the runtime for this method
    if s_or_l == "s":
        return arr[k-1]
    elif s_or_l == "l":
        return arr[-k]

print(returnK(arr, "s", k))




#array has duplicates
def return_K(array, s_or_l, k):
    n = None
    dict = {}
    ar = []
    array.sort()
    for i, num in enumerate(array):
        if i == 0:
            n = num
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1
        if i > 0:
            if num != n:
                ar.append(dict[num])
    if s_or_l == "s":
        return arr[k-1]
    elif s_or_l == "l":
        return arr[-k]


print(return_K(arr, "s", k))
