""" Determine if Singly Linked Lit contains a 'cycle' - meaning a nextnode points back to a previous node in the sequence """

class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None


def cycle_check(node):
    marker1 = node
    marker2 = node

    while marker2 != None and marker2.nextnode != None:
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        print(marker1.value)
        print(marker2.value)

        if marker2 == marker1 :
            return True

    return False




#CYCLE NODE
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a #CYCLE HERE


#NON-CYCLE NODE
x = Node('one')
y = Node('two')
z = Node('three')

x.nextnode = y
y.nextnode = z
z.nextnode = None


print(cycle_check(c))
print(cycle_check(x))
