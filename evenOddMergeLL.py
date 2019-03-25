"""

Write a function that merges two LL's, starting with the
nodes with even-numbered data followed by
the nodes with odd-numbered data.

"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# g = Node(5)
# f = Node(5, g)
# e = Node(4, f)
# d = Node(3, e)
# c = Node(2, d)
# b = Node(1, c)
# a = Node(0, b)

h = Node(7)
g = Node(5, h)
f = Node(5, g)
e = Node(3, f)
d = Node(3, e)
c = Node(2, d)
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
        even.next = odd_head
    return even_head

print(iterateList(merge(L)))




    # print("print"+str(iterateList(even)))


    # odd.next = None
    # new_head = head
    #
    #
    # while head.next:
    #     if head.data % 2 == 0:
    #         head = head.next
    #     else:
    #         odd.next = head
    #         odd = odd.next
    #         while odd.data % 2 != 0:
    #             odd = odd.next
    #     head.next = odd_head

    # print(iterateList(odd))

    # return new_head

# print(iterateList(L))
# print(iterateList(merge(L)))
