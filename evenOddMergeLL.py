"""

Write a function that merges an LL into nodes with even-numbered data
followed by nodes with odd-numbered data.

"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

h = Node(8)
g = Node(7, h)
f = Node(6, g)
e = Node(5, f)
d = Node(4, e)
c = Node(3, d)
b = Node(2, c)
a = Node(1, b)

L = a

def iterateList(L):
    """Note: Does not alter 'L'."""
    array=[]
    while L:
        array.append(L.data)
        L = L.next
    return array

def merge(L):
    """
Function iterates through the list once and returns the even_head with
even data nodes followed by odd data nodes.
    """
    even_head = even = Node()
    odd_head = odd = Node()
    while L:
        if L.data % 2 == 0:
            even.next = L
            even = even.next
        if L.data % 2 != 0:
            odd.next = L
            odd = odd.next
        L = L.next
    else:
        odd.next = None
        even.next = odd_head.next
    return even_head.next

print(iterateList(merge(L)))
