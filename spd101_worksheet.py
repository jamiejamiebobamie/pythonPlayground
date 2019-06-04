

A = [2,3,4,5,2,232,323,232,323,23,232,32,32,3,4,4,3,3,2,2,21,1]
B = [2,3,6,1,4,5,6,3,2,1]

def sortLists(A,B):
    if len(A) > len(B):
    #   set A to be the smaller one. sort the arrays.
        A, B = sorted(B), sorted(A)
    else:
        A, B = sorted(A), sorted(B)

    C = []

    i = j = 0

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i+=1
        else:
            C.append(B[j])
            j+=1
    else:
        if i < len(A):
            C.extend(A[i:])
        else:
            C.extend(B[j:])

    return C


# print(sortLists(A,B))


A = "Hello324234wdksfsksalsfl ffkkfkdf   ututjtjfjfjfjdkmsadid"
B = "hihihihihihihihi3243434343442Hello  uttjdkkmsadid"


def findSubstrings(A, B):
    lookup= set()

    j = i = 0

    while j < len(B):
        test = ""
        while i + j < len(B):
            test += B[i+j]
            if test not in lookup:
                lookup.add(test)
            i+=1
        j+=1
        i = 0

    i = j = 0

    results = set()

    while j < len(A):
        test = ""
        while i + j < len(A):
            test += A[i+j]
            if test in lookup:
                results.add(test)
            i+=1
        j+=1
        i = 0

    print(len(lookup))
    return results

# print(findSubstrings(A, B))


A = [1,2,3,3,4,4,5,53,33,43,2423,432,423,432,432,432,432,4,234,324,325,523,233243,-1,-3,1,-1,-21,-212,-121,-21,-21,-212,-1,-21212,-12,-32,-32,-32,-32,-3,-23,-23,-23,-23,-2,-2,-32,-32,-3,-2]


def findLargestThreeNumbers(A):
    first =  second = third = float('-inf')
    for item in A:
        if item > first:
            first = item
        elif item > second:
            second = item
        elif item > third:
            third = item
    return first*second*third, (first, second, third)

print(findLargestThreeNumbers(A))
