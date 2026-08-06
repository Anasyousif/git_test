from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, node):
        node.set_next(self.head)
        self.head = node
        # If the list was empty, the new node is also the tail
        if self.tail is None:
            self.tail = node

    def add_to_tail(self, node):
        # Case 1: List is empty
        if self.head is None:
            self.head = node
            self.tail = node
            return
        
        # Case 2: List has elements - use the tail pointer for O(1) insertion
        self.tail.set_next(node)
        self.tail = node

    # don't touch below this line

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(str(node.val))
        return " -> ".join(nodes)