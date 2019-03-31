A = [(0,0), (0,1), (0,3), (0,4),
(1,0), (1,1), (1,2), (1,3), (1,4),
(2,1), (2,2), (2,3),
(3,0), (3,1), (3,2), (3,3), (3,4),
(4,0), (4,1), (4,3), (4,4)]

def howMany(A):
    result = []
    def __test(vertex1, vertex2):
        #the test needs to check that the sides are equal and then check to make sure all of the square's vertices are in A, this second check isn't correct.
        if abs(vertex1[0] - vertex2[0]) == abs(vertex1[1] - vertex2[1]) and (vertex1[0] + abs(vertex1[0] - vertex2[0]), vertex1[1]) in A and (vertex2[0] + abs(vertex1[0] - vertex2[0]), vertex2[1]) in A:
            return (vertex1, vertex2) if vertex1[0] < vertex2[0] else (vertex2, vertex1)


    for i, vertex in enumerate(A):
        for j, point in enumerate(A):
            if vertex[0] != point[0] or vertex[1] != point[1]:
                test = __test(vertex,point)
                if test not in result:
                    result.append(test)

    print(result)
    return len(result)

print(howMany(A))
