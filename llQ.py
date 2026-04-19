from node import Node


class LLQueue:
    def remove_from_head(self):
        if self.head is None:
            return None

    # 2. Assign the head to be removed to a variable
        removed_node = self.head

    # 3. Set the list's head to the next node in the list
        self.head = self.head.next

    # 4. If the list became empty, set the list's tail to None
        if self.head is None:
            self.tail = None

    # 5. Set the (now removed) head's next to None
        removed_node.next = None

    # 6. Return the removed head
        return removed_node

    # don't touch below this line

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def __init__(self):
        self.tail = None
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
        return " <- ".join(nodes)
