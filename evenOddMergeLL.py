"""

Write a function that merges two LL's, starting with the
nodes with even-numbered data followed by
the nodes with odd-numbered data.

"""


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
c = Node(3, d)
b = Node(1, c)
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
    bool = False
    head = odd = odd_head = L


    while head.data % 2 != 0:

        odd = odd.next
        head = head.next

    print("print"+str(iterateList(odd)))


    odd.next = None
    new_head = head


    while head.next:
        if head.data % 2 == 0:
            head = head.next
        else:
            odd.next = head
            odd = odd.next
            while odd.data % 2 != 0:
                odd = odd.next
        head.next = odd_head

    # print(iterateList(odd))

    return new_head

print(iterateList(L))
print(iterateList(merge(L)))
