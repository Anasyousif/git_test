class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        # Check if the stack is empty first
        if not self.items:
            return None
        # Return the last item (the top) without removing it
        return self.items[-1]

    def pop(self):
        # Check if the stack is empty first
        if not self.items:
            return None
        # .pop() without arguments removes and returns the last item
        return self.items.pop()