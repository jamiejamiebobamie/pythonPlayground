# def myPoorlyNamedFunction(matrix):

    #this is obviously incorrect, i computed the minimum for each row:
    # minimum = float("inf")
    # for index, i in enumerate(matrix):
    #     for j in i:
    #         minimum = min(j, minimum)
    #
    #     matrix[index].append(minimum)

    #i realized my error here and thought I might get some brownie points if I tried to subtract the minimum from each interior array item
    # for _ in range(0,len(matrix)-2):
    #     for j, columns in enumerate()
    #    -matrix[_][j]-=matrix[_][-1]
    #
    # return matrix

# print(myPoorlyNamedFunction(matrix))



A = [[1,2,3],   #      A = [[1,2,3],
     [1,2,3],   #           [2,4,6],
     [1,2,3]]   #           [3,6,9]]

def computeColumn(matrix):
    i = j = 0
    while i < len(matrix):
        if i != 0 and j < len(matrix[0]):
            matrix[i][j] += matrix[i-1][j]
        j += 1
        if j == len(matrix[0]):
            j = 0
            i += 1
    return matrix

print(computeColumn(A))
