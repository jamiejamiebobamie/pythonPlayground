"""

Test whether a link list in pallindromic.

"""

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

n = Node(0)
m = Node(1, n)
l = Node(2, m)
k = Node(3, l)
j = Node(2, k)
i = Node(1, j)
h = Node(0, i)

g = Node(5)
f = Node(5, g)
e = Node(3, f)
d = Node(3, e)
c = Node(3, d)
b = Node(1, c)
a = Node(1, b)

L1 = a #not pallindromic
L2 = h #pallindromic

def iterateList(L):
    array = []
    while L:
        array.append(L.data)
        L = L.next
    return array


def isPallindrome(L):
    #trying to not do the brute force method of putting all of the data in an array
    #and checking if that array is pallindromic...

    #i could also make the singly list a doubly linked list by adding a previous field to each node
    #which would make this much much easier...
    def length(L):
        """Get the length of the list."""
        count = 0
        while L:
            count+=1
            L = L.next
        return count

    bool = True
    count = 0
    dummy_head = L
    n = length(L)

    while bool and L:
        while count < n-1:
            dummy_head = dummy_head.next
            count+=1
        else:
            bool = dummy_head.data == L.data
            print(L,dummy_head, L == dummy_head, L.data, dummy_head.data, n, bool)
            count = 0
            n -= 2
            dummy_head = L.next
            L = L.next

isPallindrome(L2)
