""" DOUBLY LINKED LIST """
class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None





a = Node("one")
b = Node('two')
c = Node('three')

# Create links
a.next_node = b
b.prev_node = a

b.next_node = c
c.prev_node = b

print(a.next_node.next_node.value)
