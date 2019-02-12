# https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/


# array.sort() = sorts in place RUNTIME: nlog(n)
# sorted() = makes a new array and requires a new variable

arr = [7, 7,7, 6, 4, 7, 10, 2, 2, 2, 1, 2, 1, 0, 0, 0, 4, 3, 20, 15]
k = 2

#array has no duplicates
def returnK(array, s_or_l, k):
    array.sort() #what's the runtime for this method
    if s_or_l == "s":
        return arr[k-1]
    elif s_or_l == "l":
        return arr[-k]

# print(returnK(arr, "s", k))




#array has duplicates
def return_K(array, s_or_l, k):

    n = None
    dict = {}
    # ar = []

    array.sort()

    # somehow convert dict into new_list

    for num in array:
        # if i == 0:
        #     n = num
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1
    ar = list(dict.keys()) #what's the runtime on this?
        # if i > 0:
        #     if num != n:
        #         ar.append(dict[num])
    print(ar)
    if s_or_l == "s":
        return ar[k-1]
    elif s_or_l == "l":
        return ar[-k]


print(return_K(arr, "s", k))
