from node import Node


class LinkedList:
    def add_to_tail(self, node):
        if  self.head is None:
            self.head = node
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.set_next(node)
            
            

    # don't touch below this line

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)
