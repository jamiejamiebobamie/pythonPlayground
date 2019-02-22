# A Tic-Tac-Toe board is given as a string array board.
# Return True if and only if it is possible to reach this board position during
# the course of a valid tic-tac-toe game.

# The board is a 3 x 3 array, and consists of characters " ", "X", and "O".
# The " " character represents an empty square.

# Here are the rules of Tic-Tac-Toe:

# Players take turns placing characters into empty squares (" ").
# The first player always places "X" characters,
# while the second player always places "O" characters.
# "X" and "O" characters are always placed into empty squares, never filled ones.
# The game ends when there are 3 of the same (non-empty) character
# filling any row, column, or diagonal.

# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# Example 1:
# Input: board = ["O  ", "   ", "   "]
# Output: false
# Explanation: The first player always plays "X".
#
# Example 2:
# Input: board = ["XOX", " X ", "   "]
# Output: false
# Explanation: Players take turns making moves.
#
# Example 3:
# Input: board = ["XXX", "   ", "OOO"]
# Output: false
#
# Example 4:
# Input: board = ["XOX", "O O", "XOX"]
# Output: true
# Note:
#
# board is a length-3 array of strings, where each string board[i] has length 3.
# Each board[i][j] is a character in the set {" ", "X", "O"}.

board = ["O  ", "   ", "   "]
board = ["XOX", " X ", "   "]
board = ["XXX", "   ", "OOO"]
board = ["XOX", "O O", "XOX"]

def checkTTT(board):
    dictX = {}
    dictO = {}
    countX = 0
    countO = 0
    for i, place in enumerate(board):
        for j, plaze in enumerate(place):
            if plaze == "X":
                if i in dictX:
                    dictX[i] += j
                else:
                    dictX[i] = j
                if j in dictX:
                    dictX[j] += i
                else:
                    dictX[j] = i
                countX += 1
            if plaze == "O":
                if i in dictO:
                    dictO[i] += j
                else:
                    dictO[i] = j
                if j in dictO:
                    dictO[j] += i
                else:
                    dictO[j] = i
                countO += 1
    return countX, countO, dictO.keys(), dictO.values()
    # return countO <= countX and countO+2 >= countX

    #if O > X False
    #if X == O False
    #if X > O+2 False




print(checkTTT(board))
