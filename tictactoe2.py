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
# print(array)

unhash = {}

for i, row in enumerate(array):
    for j, column in enumerate(row):
        # print(i,j,3*i+j*2)
        # dict[3*i+j*2] = " "
        unhash[3*i+j*2] = [i, j, " "]
# print(len(unhash))

#build____


#choose____


iter = 0
keys = list(unhash.keys())
print(keys)
for key in keys:
    rando = rand.randint(iter,len(keys)-1)
    # print(rando)
    keys[rando], keys[iter] = keys[iter], keys[rando]
    iter += 1
    print(keys)
print(keys)
#choose____

#play___
value = True
for key in keys:
    # print(unhash[key])
    if value:
        unhash[key][2] = "X"
    else:
        unhash[key][2] = "O"
    value = not value
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


"""
board   boardNode     keep track of adjacent repeats linkedlist?



     X X O X X O
     X O X X O X
     O X O O X O
     X X O X X O
     X O X X O X
     O X O O X O

     (0,5)(1,4)(2,3)(3,2)(4,1)(5,0)
     diagonal indices are a pallindrome or 'stepwise' ascending


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
    at each bin have a linked list of index, X/O,
    and a boolean: 'hetero' (mixed)
    True if it contains both X and O
    Do not append to list if True.

update move count each turn.

diagonals??

2 bins for diagonals



"""

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
