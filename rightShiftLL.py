"""

Write a program that takes as input a singly linked list
and a nonnegative integer k, and returns the list
cyclically shifted to the right by k.

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

def shiftList(L, k):

    """
    So the last k items get shifted to the front with the [-k] item in the
    list becoming the new head.

    Need to do this with one pass over the LL and O(1) storage.
    """


    head= iter = L

    def listLength(L):
        """
        Returns the length of the LL
        and sets the tail's next node to the current head.
        """
        temp = L
        L = L.next
        count = 1
        while L:
            count+=1
            L = L.next
            temp = temp.next
        temp.next = head
        return count, head

    #an attempt at running the function only once...
    funcReturn = listLength(L)
    n = funcReturn[0]
    head = funcReturn[1]

    count = 0
    # the count is less than the absolute value of the size linked list - the shift ('k') - 1
    while count < abs(n - k - 1):
        L = L.next
        count+=1
    #make the new head the [-k] item in the list
    head = L.next
    #set the element just before the [-k] the tail by setting its next field to 'None'
    L.next = None
    return head

print(iterateList(L))
print(iterateList(shiftList(L, 3)))
