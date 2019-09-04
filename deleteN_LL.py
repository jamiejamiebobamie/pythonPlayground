# delete the n node of from the end of a linked list (N == 1 == tail node)
# the problem is there is no pointer to the tail node, only the head of the LL.
# do it in O(n) time.


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None # just for adding nodes, not for solving the problem
        self.length = 0

    def addNode(self, data):
        new_node = LinkedListNode(data)
        node = previous = self.head
        while node:
            previous = node
            node = node.next
        else:
            self.length += 1
            if previous:
                previous.next = new_node
                self.tail = new_node
                new_node.last = previous
            else:
                self.head = self.tail = new_node

    def deleteNode(self):
        """Acts like a queue. Removes the front item by reassinging the head."""
        if self.length > 0:
            self.head = self.head.next
            self.length -= 1
        else:
            return None

    def getListData(self):
        data = []
        node = self.head
        while node:
            data.append(node.data)
            node = node.next
        return data

class LinkedListNode():
    def __init__(self, data, next=None, last=None):
        self.data = data
        self.next = next
        self.last = last

def delete_N_NodeOfLL(LL, n):
    """This method creates a new LinkedList called "sublist" that is of length n or less.
    It runs in O(m) time (m, being the length of the LL), but requires O(n) storage.
    Since we only need a pointer to a single node to be deleted. It's not optimal, considering the storage requirements.
    """
    if n <= 0:
        return
    sublist = LinkedList()
    node = LL.head
    while node:
        if sublist.length < n:
            sublist.addNode(node)
        else:
            sublist.addNode(node)
            sublist.deleteNode()
        node = node.next
    if sublist.length == n:
        node_to_delete = sublist.head.data
        if node_to_delete.last: # the node to delete is not the head
            node_to_delete.last.next = node_to_delete.next
        if node_to_delete.next: # if the node to delete is not the tail
            node_to_delete.next.last = node_to_delete.last
        if node_to_delete == LL.head:
            LL.head = node_to_delete.next


newLinkedList = LinkedList()

newLinkedList.addNode(1)
newLinkedList.addNode(2)
newLinkedList.addNode(3)
newLinkedList.addNode(4)
newLinkedList.addNode(5)
print(newLinkedList.getListData())
delete_N_NodeOfLL(newLinkedList,3)
print(newLinkedList.getListData())
