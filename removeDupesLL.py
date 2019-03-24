# This is  problem from Elements of Programming Interviews in Python on pg. 91:
# Write a program that takes as input a singly linked list of integers in sorted order,
# and removes duplicates from it. The list should be sorted.

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
b = Node(0, c)
a = Node(0, b)

L = a

dummy_head = L

while L:
    print(L.data)
    L = L.next


def removeDupes(L):
    head = temp = L
    L = L.next
    bool = False
    while L:
        if temp.data != L.data:
            if bool == True:
                # temp.next = L
                head.next = L
                bool = False
            temp = L
            L = L.next
        else:
            bool = True
            print(bool, head.data)
            L = L.next
        return head



while removeDupes(dummy_head):
    print(dummy_head.data)
    dummy_head = dummy_head.next
