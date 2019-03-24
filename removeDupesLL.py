"""This is  problem from Elements of Programming Interviews in Python on pg. 91:
Write a program that takes as input a singly linked list of integers in sorted order,
and removes duplicates from it. The list should be sorted."""

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

# g = Node(5)
# f = Node(5, g)
# e = Node(4, f)
# d = Node(3, e)
# c = Node(2, d)
# b = Node(1, c)
# a = Node(0, b)

h = Node(6)
g = Node(5, h)
f = Node(5, g)
e = Node(3, f)
d = Node(3, e)
c = Node(2, d)
b = Node(1, c)
a = Node(0, b)

L = a

def iterateList(L):
    """Note: Does not alter 'L'."""
    array=[]
    while L:
        array.append(L.data)
        L = L.next
    return array

def removeDupes(L):
    """
    Uses two iterators to traverse the list.
    The 'temp' iterator stops when there is a duplicate
    and continues when a unique entry is reached.
    """
    head = temp = L
    bool = False
    while L:
        if temp.data != L.data:
            if bool == True:
                temp.next = L
                bool = False
            temp = L
        else:
            bool = True
        L = L.next
    return head


print(iterateList(L))
print(iterateList(removeDupes(L)))
