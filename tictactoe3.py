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
import random as rand

class TicTacToe:
    def __init__(self, n=3):
        self.n = n

        self.rows = {}
        self.cols = {}
        self.diags = {}

        self.board = self.buildBoard(n) # an array of i-j board indices
        self.order = self.randomOrder(self.board)

    def buildBoard(self, n):
        """Returns an array of (i,j) index keys to be randomized.
        Builds rows, cols, and diags dictionaries."""
        boardDict = []
        diagCount = 0

        for i in range(n):
            self.rows[i] = None
            self.cols[i] = None
            for j in range(n):
                if (i == j) or (i + j == n-1):
                    if diagCount < 2: #only need one of each
                        self.diags[i,j] = None
                        diagCount += 1
                boardDict.append((i,j))
        return boardDict

    def randomOrder(self, array):
        """Takes a dictionary of index-keys and mixes up their order.
        Returns an array of i-j index-keys. This is the order the tiles will be played.
        X will play even tiles starting at 0 and O will play odd starting at 1."""

        iter = 0
        order = array
        for key in array:
            rando = rand.randint(iter,len(order)-1)
            order[rando], order[iter] = order[iter], order[rando]
            iter += 1
        return order

    def play(self):
        value = 0 #O
        player = {0: 'O', 1: 'X'}
        moveCount = 0
        iter = 0
        turn = ""
        while moveCount < self.n**2:
            value = not value #X starts
            turn = player[value]
            key = self.order[iter]

            # keep track of count and homogenity
            # at each i/j index key in the given row/column/diagonal dictionary.
            # doesn't need to be a node. can be a tuple or array.

            iter +=1
            moveCount += 1
            print(turn, key)
        else:
            return "Tie"

new = TicTacToe(5)
print(new.play())
