# Given a gold mine of n*m dimensions.
# Each field in this mine contains a positive integer which is the amount of gold in tons.
# Initially the miner is at first column but can be at any row.
# He can move only (right->,right up /,right down\) that is from a given cell,
# the miner can move to the cell diagonally up towards the right or right or diagonally down towards the right.
# Find out maximum amount of gold he can collect.
#
# Examples:
#
# Input : mat[][] = {{1, 3, 3},
#                    {2, 1, 4},
#                   {0, 6, 4}};
# Output : 12
# {(1,0)->(2,1)->(2,2)}
#
# Input: mat[][] = { {1, 3, 1, 5},
#                    {2, 2, 4, 1},
#                    {5, 0, 2, 3},
#                    {0, 6, 1, 2}};
# Output : 16
# (2,0) -> (1,1) -> (1,2) -> (0,3) OR
# (2,0) -> (3,1) -> (2,2) -> (2,3)
#
# Input : mat[][] = {{10, 33, 13, 15},
#                   {22, 21, 04, 1},
#                   {5, 0, 2, 3},
#                   {0, 6, 14, 2}};
# Output : 83


# array = [[1, 3, 3],[2, 1, 4],[0, 6, 4]]

array =           [[10, 33, 13, 15],
                  [22, 21, 4, 1],
                  [5, 0, 2, 3],
                  [0, 6, 14, 2]]

def getMoney(array):

    choices = []
    for column in range(len(array[0])): #the miner moves from the rightmost column (index 0) to the leftmost column (index len(array))
        block = []
        for row in range(len(array)):
            block.append((array[row][column],row))
        # if abs((block[len(block)-1])[1] - block[len(block)-2][1]) < 3:
            choices.append(max(block))
            print(choices)
            if column > 1:
                while (abs(choices[-1][1] - choices[-2][1])) > 3:
                    choices.pop()
                    block.pop(row*column)
                    choices.append(max(block))

    return choices

getMoney(array)
# print(getMoney(array))
# Input : mat[][] = {{1, 3, 3},
#                    {2, 1, 4},
#                   {0, 6, 4}};


#WORK IN PROGRESS... FUNCTION GIVES MAX MONEY MOVES, BUT DOESN'T TAKE INTO ACCOUNT THE INDEX MOVEMENT RULES.
#PRONE TO ERROR THE LARGER THE ARRAY BECOMES.
