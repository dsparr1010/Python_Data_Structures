""" SINGLY LINKED LIST """

class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None

# class SinglyLinkedList(object):
#     def __init__(self, node):

a = Node('ATL')
b = Node('LAX')
c = Node('ORD')

a.nextnode = b
b.nextnode = c

print(a.value)
print(a.nextnode.value)