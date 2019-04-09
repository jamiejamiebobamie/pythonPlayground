import collections

def countIslands(numberOfRows, numberOfColumns, matrix):

    rows = {}
    count = 0

    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            if column == 1:
                if i in rows:
                    rows[i].append(j)
                else:
                    rows[i] = [j]
    print rows

    # islands = []
    # island = []
    for _ in range(numberOfRows):
        k = 0
        if _ in rows:
            count+=1
            i = 1
            curr = rows[_].pop()
            while curr-i in rows[_+k]:
                print(_,rows[_+k],curr-i)
                i+=1
            else:
                k+=1
    return count


    #         while rows[_]:
    #             while len(island)<2 or island[i]
    #             i+=1
    #             island.append(rows[_].pop())
    #             else:
    #                 islands.append(island)
    #                 island = []
    #                 i = 0
    #             break



    # k = m = 0
    # while result:
    #     count+=1
    #     current = result.pop()
    #     while current[0] + k


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

        # while matrix[k][m] == 1 and k < numberOfRows:
        #     k+=1
        # else:
        #     while matrix[k][m] == 1 and m < numberOfColumns:
        #         m+=1
        #     else:
        #         count+=1
        #         k -= 1
        #         m = 0
        #
        # return count



matrix = [  [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0] ]

print(countIslands(5,5, matrix))
