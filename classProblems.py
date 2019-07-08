A = [1,2,3,4,2,1,90,10,5,5,6,]
B = [96,4,3,76,37,12,34]
t = 4

A = sorted(A)
B = sorted(B)

i = 1
j = 1

test1 = A[0] + B[1]
test2 = A[1] + B[0]

while i < len(A) and j < len(B):
    
