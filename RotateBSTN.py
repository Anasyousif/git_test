class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def rotate_left(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return
        
        y = pivot_parent.right
        pivot_parent.right = y.left
        
        if y.left != self.nil:
            y.left.parent = pivot_parent
            
        y.parent = pivot_parent.parent

        if pivot_parent.parent is None:
            self.root = y
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = y
        else:
            # Added this missing case
            pivot_parent.parent.right = y
            
        y.left = pivot_parent
        pivot_parent.parent = y

    def rotate_right(self, pivot_parent):
        # 1. Changed check to .left (since we need a left child to rotate right)
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
            
        # 2. x is the pivot (the left child)
        x = pivot_parent.left
        
        # 3. Move x's right child to pivot_parent's left
        pivot_parent.left = x.right
        
        if x.right != self.nil:
            x.right.parent = pivot_parent
            
        x.parent = pivot_parent.parent

        # 4. Update the parent of the sub-tree
        if pivot_parent.parent is None:
            self.root = x
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = x
        else:
            pivot_parent.parent.left = x

        # 5. Put pivot_parent to the right of x
        x.right = pivot_parent
        pivot_parent.parent = x

        # don't touch below this line

    def insert(self, val):
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                # duplicate, just ignore
                return

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node
