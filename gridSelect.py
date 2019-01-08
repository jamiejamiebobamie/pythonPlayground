#given a matrix with i rows and j columns put objects in their own unique row
#and column so that no two objects share i or j

import random

rows = [0,1,2,3,4]

for i, row in enumerate(rows):
    k = random.randint(i,len(rows)-1)
    rows[i], rows[k] = rows[k], rows[i]

print(rows)

columns = [0,1,2,3,4]

for i, column in enumerate(columns):
    k = random.randint(i,len(columns)-1)
    columns[i], columns[k] = columns[k], columns[i]

print(columns)

matrix = []

for i, row in enumerate(rows):
    matrix.append((rows[i],columns[i]))

print(matrix)


# square = [0,1,2,3,4]
#
# grid = []
#
# for i, block in enumerate(square):
#     k = random.randint(i,len(square)-1)
#     block[i], block[k] = block[k], block[i]
#     grid.append(list(block[i]))
#
# for i, block in enumerate(square):
#     k = random.randint(i,len(square)-1)
#     block[i], block[k] = block[k], block[i]
#     grid.append([block[i]])
#
# print(grid)
