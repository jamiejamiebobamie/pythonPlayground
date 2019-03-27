"""

Form a Linked List from the Leaves of a Binary Tree

pg129

Given a binary tree, compute a linked list from th eleaves of the binary tree.
The leaves should appear in left-to-right order.

"""

class LLNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class NodeBT:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left=left
        self.right=right


def traverseLL(head):
    array = []
    while head:
        array.append(head.data)
        head = head.next
    return array










j = NodeBT("j")
i = NodeBT("i")
h = NodeBT("h")
g = NodeBT("g",i,j)
f = NodeBT("f",None,h)
e = NodeBT("e",None,g)
d = NodeBT("d")
c = NodeBT("c",f)
b = NodeBT("b",e)
a = NodeBT("a",c,d)
root = NodeBT("root",a,b)

def traverseTree(root):
    iter = LLNode()
    dummy_head = LLNode(None,iter)
    def __helper(node):
        if node.left:
            __helper(node.left)
            # traverseTree(root.left)

        if node.right:
            __helper(node.right)
            # traverseTree(root.right)

        if node.left==None and node.right==None:
            new = LLNode(node.data)
            # print(new.data)
            # iter.next = new
            # iter = iter.next
        # return dummy_head
        # return new = LLNode(node.data)

    return __helper(root)

traverseTree(root) #having difficulty creating the LL inside the function.


#Book's solution:

def create_list_of_leaves(tree):
    if not tree:
        return []
    if not tree.left and not tree.right:
        return [tree]
    return create_list_of_leaves(tree.left) + create_list_of_leaves(tree.right)

#   so simple...

for c in create_list_of_leaves(root):
    print(c.data)
