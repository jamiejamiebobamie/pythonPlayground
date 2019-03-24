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

    count = 0
    dummy_head = L
    n = length(L)

    while count < n-1:
        print(L.data)
        L = L.next
        count+=1
    if dummy_head.data == L.next.data:
        L.next.next, L.next = dummy_head.next, dummy_head
        n=n-1
    else:
        print(dummy_head.data, L.next.data)
        return 0

print(isPallindrome(L2))



    # if n % 2 == 0: #if the length of the list is even...
    #     while count < n/2+1:
    #         L = L.next
    #         count+=1
    # else: #if the length of the list is odd...
    #     while count < n//2 + 2:
    #         L = L.next
    #         count+=1

    # #if even
    # dummy_head=1 2 3 L=321
    # #if odd
    # dummy_head=1 2 3 L=21
    #trying to use two iterators and compare them as they traverse their part of the list...
    #going to try to reverse the list in place...


# print(isPallindrome(L2))
