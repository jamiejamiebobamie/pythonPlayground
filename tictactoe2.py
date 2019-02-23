# Design a Tic-tac-toe game that is played between two players on a n x n grid.
#
# You may assume the following rules:
#
# A move is guaranteed to be valid and is placed on an empty block.
# Once a winning condition is reached, no more moves is allowed.
# A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
# Example:
# Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.
#
# TicTacToe toe = new TicTacToe(3);
#
# toe.move(0, 0, 1); -> Returns 0 (no one wins)
# |X| | |
# | | | | // Player 1 makes a move at (0, 0).
# | | | |
#
# toe.move(0, 2, 2); -> Returns 0 (no one wins)
# |X| |O|
# | | | | // Player 2 makes a move at (0, 2).
# | | | |
#
# toe.move(2, 2, 1); -> Returns 0 (no one wins)
# |X| |O|
# | | | | // Player 1 makes a move at (2, 2).
# | | |X|
#
# toe.move(1, 1, 2); -> Returns 0 (no one wins)
# |X| |O|
# | |O| | // Player 2 makes a move at (1, 1).
# | | |X|
#
# toe.move(2, 0, 1); -> Returns 0 (no one wins)
# |X| |O|
# | |O| | // Player 1 makes a move at (2, 0).
# |X| |X|
#
# toe.move(1, 0, 2); -> Returns 0 (no one wins)
# |X| |O|
# |O|O| | // Player 2 makes a move at (1, 0).
# |X| |X|
#
# toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
# |X| |O|
# |O|O| | // Player 1 makes a move at (2, 1).
# |X|X|X|
# Follow up:
# Could you do better than O(n2) per move() operation?
#
# Hint:
#
# Could you trade extra space such that move() operation can be done in O(1)?
# You need two arrays: int rows[n], int cols[n], plus two variables: diagonal, anti_diagonal.

import random as rand

# def tictac(n):
#     array = list('1'*n)
#     turn = 0 #X = 1, O = 0
#     turns = 0
#     while turns < n:
#         array[turns], array[rand.randint(0,n-turns)] = turn^turn, array[rand.randint(0,n-turns)]
#         turn = 1
#         turns += 1
#     return array
#
# print(tictac(8))

#learn numpy...

#
# #build____
# n= 3
# array = []
# for i in range(n):
#     array.append(list(" "*n))
# # print(array)
#
# unhash = {}
#
# for i, row in enumerate(array):
#     for j, column in enumerate(row):
#         # print(i,j,3*i+j*2)
#         # dict[3*i+j*2] = " "
#         unhash[3*i+j*2] = [i, j, " "]
# # print(len(unhash))
#
# #build____
#
#
# #choose____
#
#
# iter = 0
# keys = list(unhash.keys())
# print(keys)
# for key in keys:
#     rando = rand.randint(iter,len(keys)-1)
#     # print(rando)
#     keys[rando], keys[iter] = keys[iter], keys[rando]
#     iter += 1
#     print(keys)
# print(keys)
# #choose____
#
# #play___
# value = True
# for key in keys:
#     # print(unhash[key])
#     if value:
#         unhash[key][2] = "X"
#     else:
#         unhash[key][2] = "O"
#     value = not value
    # iter += 1
#play___


# 0 2 4
# 3 5 7
# 6 8 10

# X X O
# X O X
# O X O

# _ X O
# _ O X
# O X _


#ended at 4 after 6 moves:

# [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# (0, 0, 0)
# (0, 1, 2)
# (0, 2, 4)
# (1, 0, 3)
# (1, 1, 5) #hash function: 3*i+j*2
# (1, 2, 7)
# (2, 0, 6)
# (2, 1, 8)
# (2, 2, 10)



# d[0] = (0, 0)
# d[2] = (0, 1)
# d[4] = (0, 2)
# d[3] = (1, 0)
# d[5] = (1, 1)
# d[7] = (1, 2)
# d[6] = (2, 0)
# d[8] = (2, 1)
# d[10] = (2, 2)

# print(unhash)

# [0, 2, 3, 4, 5, 6, 7, 8, 10]
# [7, 5, 2, 6, 8, 4, 0, 10, 3]
# {0: 'X', 2: 'X', 3: 'X', 4: 'O', 5: 'O', 6: 'O', 7: 'X', 8: 'X', 10: 'O'}


# fisher-yates shuffle
# [0, 2, 3, 4, 5, 6, 7, 8, 10]
# [3, 2, 0, 4, 5, 6, 7, 8, 10]
# [3, 0, 2, 4, 5, 6, 7, 8, 10]
# [3, 0, 2, 4, 5, 6, 7, 8, 10]
# [3, 0, 2, 4, 5, 6, 7, 8, 10]
# [3, 0, 2, 4, 8, 6, 7, 5, 10]
# [3, 0, 2, 4, 8, 6, 7, 5, 10]
# [3, 0, 2, 4, 8, 6, 5, 7, 10]
# [3, 0, 2, 4, 8, 6, 5, 10, 7]
# [3, 0, 2, 4, 8, 6, 5, 10, 7]
# [3, 0, 2, 4, 8, 6, 5, 10, 7]

"""
must span 'n' to win.

(i,j)
rows have repeat j's
    (a row's key would be j)
columns have repeat i's
    (a column's key would be i)

no one cheats in this game so we don't need to keep track of if the move is valid
    only if there's a winner or if all spaces have been filled.

the key insight is that we don't need to worry about rows and columns the moment
    they contain both an X and O, because it can't be a winner.

make bins out of all rows and columns.
    at each bin have a linked list of nodes with the properties:
        value: index of space in multidimensional array,
        player: X/O,
        next: next node in linked list,

    #ALL NODES HAVE THESE PROPERTIES, BUT THEY'RE
    ONLY CHANGED ON THE FIRST NODE OF THE LIST:
        homogenous: True #True if this list contains only X or O elements,
        count: # of nodes in list

    Do not append to list if 'homogenous' is False.


diagonals??

     X X O X X O
     X O X X O X
     O X O O X O
     X X O X X O
     X O X X O X
     O X O O X O

     (0,5)(1,4)(2,3)(3,2)(4,1)(5,0)

     X X O
     X O X
     O X O

     (0,2)(1,1)(2,0) = 6

     O X X
     X O X
     O X O

     (0,0)(1,1)(2,2) = 6

          O X O X
          X O X X
          O X O O
          X O O O

     (0,0)(1,1)(2,2)(3,3) = 12
     (0,3)(1,2)(2,1)(3,0) = 12

            O X
            X O

    (0,0)(1,1)
    (0,1)(1,0)

     diagonal indices are a pallindrome or 'stepwise' ascending

     diagDict keys: 'pal' and 'step'


'   value = 0 #O
    player = {0: O, 1: X}
    spacesCount = 0
    dictRow, dictCol, dictDiag = {}, {}, {}

    while spacesCount < n**2:

        value = not value #X starts

        if key in dictRow:
            if dictRow[key].homogenous:
                    dictRow[key].addNode(i,j,player[value])
                    dictRow[key].count += 1
                if dictRow[key].count == n:
                    return dictRow[key].player
                if player[value] != dictRow[key].peek(): #peek(), in at the first node and return it's player attribute
                    dictRow[key].homogenous = False
        else:
            dictRow[key].addNode(i,j,player[value])
            dictRow[key].count += 1

        if key in dictRow:
            if dictCol[key].homogenous:
                    dictCol[key].addNode(i,j,player[value])
                    dictCol[key].count += 1
                if dictCol[key].count == n:
                    return dictCol[key].player
                if player[value] != dictCol[key].peek(): #peek(), in at the first node and return it's player attribute
                    dictCol[key].homogenous = False
        else:
            dictCol[key].addNode(i,j,player[value])
            dictCol[key].count += 1

        #look at the indices and add them to the appropriate diagonal bin:
        if i == j:
            if len(dictDiag) != 0:
                if dictDiag['step'].homogenous:
                    dictDiag['step'].addNode(i,j,player[value])
                    dictDiag[key].count += 1
                    if dictDiag['step'].count == n:
                        return dictDiag['step'].player
                    if player[value] != dictDiag['step'].peek():
                        dictDiag['step'].homogenous = False
                else:
                    dictDiag['step'].addNode(i,j,player[value])
                    dictDiag[key].count += 1

        if i + j == n-1:
            if len(dictDiag) != 0:
                if dictDiag['pal'].homogenous:
                    dictDiag['pal'].addNode(i,j,player[value])
                    dictDiag[key].count += 1
                    if dictDiag['pal'].count == n:
                        return dictDiag['pal'].player
                    if player[value] != dictDiag['pal'].peek():
                        dictDiag['pal'].homogenous = False
                else:
                    dictDiag['pal'].addNode(i,j,player[value])
                    dictDiag[key].count += 1

        spaceCount += 1 #update move count each turn.

    else:
        return "Tie"
'

"""
class TicTacToe:
    def __init__(self, n=None):
        self.board = self.buildBoard(n)
        self.order = self.randomOrder(self.board)
        self.play = True
        self.count = 0 # keep track of the overall tiles or unneccessary?

    def buildBoard(self, n):
        """Returns a dictionary of (i,j) index keys with 'None' values."""
        boardDict = {}
        for i in range(n):
            for j in range(n):
                boardDict[i,j] = None
        return boardDict

    def randomOrder(self, dictionary):
        """takes a dictionary of index-keys and mixes their order up
        returning and array of index-keys"""
        iter = 0
        order = list(dictionary.keys())# these methods probably add to the time complexity...
        for key in order:
            rando = rand.randint(iter,len(order)-1)
            order[rando], order[iter] = order[iter], order[rando]
            iter += 1
        return order

        def play(self):
            pass

        class LinkedList:
            def __init__(self):
                self.head = self.tail = None # the chonological tiles played. is this necessary?
                                             # TicTacToe.order = the chonological order of the tiles played.

                class LL_Node:
                    def __init__(self, value=None, player=None):
                        """new idea: the first tile in either a row or column or diagonal
                        becomes the head of the list you add to the node by setting
                        the row, column, or diag attributes to the next node in the row,
                        column, or diagonal, keeping the count (of each...)
                        before you add a node you check a node's type(?)
                        and if it conflicts with the current type of the node you set the
                        row, column, or diagonal to "Nope" to say 'don't add more nodes...'
                        The tile becomes a 'blocker' for that row, column, or diagonal.
                        """

                        self.row = None # does this become a graph if you have multiple pointers / next nodes?
                        self.column = None # how do I keep track of their respective heads?
                        self.diag = None # 

                        self.value = value # (i,j)
                        self.player = player # X or O

                        self.next = None # the chonological order of the tiles played / chosen
                        self.homogenous = True
                        self.count = 0 # n-1 to end game

                # def addNode(i,j,player,): # must account for a node not being present.


# new = TicTacToe(13)
# for order in new.order:
#     print(order, new.board[order])

#
# #choose____
# def makeTurnPositionsArray(board)
#
# iter = 0
# keys = list(unhash.keys())
# print(keys)
# for key in keys:
#     rando = rand.randint(iter,len(keys)-1)
#     # print(rando)
#     keys[rando], keys[iter] = keys[iter], keys[rando]
#     iter += 1
#     print(keys)
# print(keys)
# #choose____
#
# #play___
# value = True
# for key in keys:
#     # print(unhash[key])
#     if value:
#         unhash[key][2] = "X"
#     else:
#         unhash[key][2] = "O"
#     value = not value
#
#
# value = 0 #O
# player = {0: O, 1: X}
# spacesCount = 0
# dictRow, dictCol, dictDiag = {}, {}, {}
#
#     while spacesCount < n**2:
#
#         value = not value #X starts
#
#         key =
#
#         if key in dictRow:
#             if dictRow[key].homogenous:
#                     dictRow[key].addNode(i,j,player[value])
#                     dictRow[key].count += 1
#                 if dictRow[key].count == n:
#                     return dictRow[key].player
#                 if player[value] != dictRow[key].peek(): #peek(), in at the first node and return it's player attribute
#                     dictRow[key].homogenous = False
#         else:
#             dictRow[key].addNode(i,j,player[value])
#             dictRow[key].count += 1
#
#         if key in dictRow:
#             if dictCol[key].homogenous:
#                     dictCol[key].addNode(i,j,player[value])
#                     dictCol[key].count += 1
#                 if dictCol[key].count == n:
#                     return dictCol[key].player
#                 if player[value] != dictCol[key].peek(): #peek(), in at the first node and return it's player attribute
#                     dictCol[key].homogenous = False
#         else:
#             dictCol[key].addNode(i,j,player[value])
#             dictCol[key].count += 1
#
#         #look at the indices and add them to the appropriate diagonal bin:
#         if i == j:
#             if len(dictDiag) != 0:
#                 if dictDiag['step'].homogenous:
#                     dictDiag['step'].addNode(i,j,player[value])
#                     dictDiag[key].count += 1
#                     if dictDiag['step'].count == n:
#                         return dictDiag['step'].player
#                     if player[value] != dictDiag['step'].peek():
#                         dictDiag['step'].homogenous = False
#                 else:
#                     dictDiag['step'].addNode(i,j,player[value])
#                     dictDiag[key].count += 1
#
#         if i + j == n-1:
#             if len(dictDiag) != 0:
#                 if dictDiag['pal'].homogenous:
#                     dictDiag['pal'].addNode(i,j,player[value])
#                     dictDiag[key].count += 1
#                     if dictDiag['pal'].count == n:
#                         return dictDiag['pal'].player
#                     if player[value] != dictDiag['pal'].peek():
#                         dictDiag['pal'].homogenous = False
#                 else:
#                     dictDiag['pal'].addNode(i,j,player[value])
#                     dictDiag[key].count += 1
#
#         spaceCount += 1 #update move count each turn.
#
#     else:
#         return "Tie"
