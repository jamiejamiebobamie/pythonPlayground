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


#build____
n= 3
array = []
for i in range(n):
    array.append(list(" "*n))
print(array)

dict = {}

for i, row in enumerate(array):
    for j, column in enumerate(row):
        print(i,j,3*i+j*2)
        dict[3*i+j*2] = " "

DL = list(dict.keys())
print(DL)

#build____


#choose____
value = True

iter = 0
for key in DL:
    rando = rand.randint(iter,len(DL)-1)
    # print(rando)
    DL[rando], DL[iter] = DL[iter], DL[rando]
    iter += 1
print(DL)
#choose____

#play___
for i, keys in enumerate(dict):
    if value:
        dict[DL[i]] = "X"
    else:
        dict[DL[i]] = "O"
    value = not value
    iter += 1
#play___

print(dict)


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

# [0, 2, 3, 4, 5, 6, 7, 8, 10]
# [7, 5, 2, 6, 8, 4, 0, 10, 3]
# {0: 'X', 2: 'X', 3: 'X', 4: 'O', 5: 'O', 6: 'O', 7: 'X', 8: 'X', 10: 'O'}
