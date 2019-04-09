import collections

def countIslands(numberOfRows, numberOfColumns, matrix):
    result = []

    count = 0

    k = m = 0
    while k < numberOfRows:
    #
    #     while matrix[k][m] != 1 and k < numberOfRows:
    #         m=0
    #         while matrix[k][m] != 1 and m < numberOfColumns:
    #             print(k,m)
    #             m+=1
    #         else:
    #             count+=1
    #     else:
    #         count+=1
    #         k+=1
    #
    # return count

#_____

        while matrix[k][m] == 1 and k < numberOfRows:
            k+=1
        else:
            while matrix[k][m] == 1 and m < numberOfColumns:
                m+=1
            else:
                count+=1
                k -= 1
                m = 0

        return count



matrix = [  [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 1, 1] ]

print(countIslands(5,5, matrix))
