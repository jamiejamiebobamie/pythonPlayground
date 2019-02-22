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

# board = ["O  ", "   ", "   "]
# board = ["XOX", " X ", "   "]
# board = ["XXX", "   ", "OOO"]
# board = ["XOX", "OXO", "XOX"]
# board = ["X O", "X O", "X  "]
board = ["XOX", "OOX", "OXX"]

 # "XOX"
 # "OOX"
 # "OXX"


def checkTTT(board):
    dictRow = {}
    dictCol = {}
    countX = 0
    countO = 0
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if column == "X":
                countX += 1
                if i in dictRow:
                    dictRow[i] += j
                else:
                    dictRow[i] = j
                if j in dictCol:
                    dictCol[j] += i
                else:
                    dictCol[j] = i
            if column == "O":
                countO += 1
                if i in dictRow:
                    dictRow[i] -= j
                else:
                    dictRow[i] = j
                if j in dictCol:
                    dictCol[j] -= i
                else:
                    dictCol[j] = i

    result = [0,0]
    for key in dictRow:
        print(key, dictRow[key])
        result[0]+=abs(dictRow[key])
    for key in dictCol:
        print(key, dictCol[key])
        result[1]+=abs(dictCol[key])

    return countX, countO, result
    return countO <= countX and countO+1 >= countX and result[0] <= 5 and result[1] <= 5

    # if O > X False, False if O is greater than X
    # if X > O+2 False, False if X has more than 1 more than O

    # attempting to create a dictionary that holds values of rows and columns based on the index (i,j)
    # this is based around the insight that the sum of all the indices of any winning row or column
    # equals 3 (0 + 1 + 2 = 3). This...

print(checkTTT(board))
