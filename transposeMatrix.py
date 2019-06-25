# firebase problems

"""Write a function that takes in an input string
and returns True if all the characters
in the string are unique,
False if there is even a single repeated character."""

# solution:
def unique_chars_in_string(input_string):
    mySet = set()
    for char in input_string:
        if char in mySet:
            return False
        mySet.add(char)
    return True


"""Write a function that takes in an nXn matrix
and returns the transposed matrix, where the items in the original matrix's rows
are columns and vice versa."""

# solution:
def transpose_matrix(matrix):
    matrix_copy = []
    for i, row in enumerate(matrix):
        part = []
        for j, column in enumerate(row):
            part.append(matrix[j][i])
        matrix_copy.append(part)
    return matrix_copy


"""Given a singly linked list, write a method to perform In-place reversal."""

# solution:
class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None

    #method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    def addNodes(self, nodeArray):
        node = self.head
        while node:
            curr = node
            node = node.next
        for data in nodeArray:
            new_node = Node(data)
            curr.next = new_node
            curr = curr.next

    def traverseNodes(self):
        results = []
        node = self.head
        while node:
            results.append(node.data)
            node = node.next
        return results

    def reverse(self):
        curr = self.head.next # 1
        previous = self.head # 0
        temp = curr.next # 2
        self.head.next = None

        while previous and curr.next:
            curr.next = previous # 0
            previous = curr # 1
            curr = temp # 2
            temp = curr.next # 3
            self.head = curr
        else:
            curr.next = previous

class Node:
    #constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

newList = SinglyLinkedList()
newNode = Node(0)
newList.setHead(newNode)
print(newList.head.data)
newList.addNodes([1,2,3,4,5,6,7])
print(newList.traverseNodes())
newList.reverse()
print(newList.traverseNodes())
