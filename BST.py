class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    #O(h): where h is the height of the tree
    #O(log n): for a well-balanced tree
    def insert(self, val, node=None):
        if not node:
            node = self.root
        if not node:
            self.root = Node(val)
            return
        if val < node.val:
            if not node.left:
                node.left = Node(val)
            else:
                self.insert(val, node.left)
        else:
            if not node.right:
                node.right = Node(val)
            else:
                self.insert(val, node.right)

    #O(h): where h is the height of the tree
    #O(log n): for a well-balanced tree
    def search(self, val, node=None):
        if not node:
            node = self.root
        if not node:
            return False
        if val == node.val:
            return True
        elif val < node.val:
            return self.search(val, node.left)
        else:
            return self.search(val, node.right)
            
    #O(h): where h is the height of the tree
    def delete(self, data):
        current = self.root
        parent = None
        is_left = None

        # Find the node to be deleted and its parent
        while current is not None and current.data != data:
            parent = current
            if data < current.data:
                is_left = True
                current = current.left
            else:
                is_left = False
                current = current.right

        # Node not found
        if current is None:
            return False

        # Case 1: Node has no children
        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
            elif is_left:
                parent.left = None
            else:
                parent.right = None

        # Case 2: Node has one child
        elif current.left is None or current.right is None:
            if current.left is not None:
                child = current.left
            else:
                child = current.right
            if parent is None:
                self.root = child
            elif is_left:
                parent.left = child
            else:
                parent.right = child

        # Case 3: Node has two children
        else:
            # Find the in-order successor of the node
            # (i.e. the leftmost child in the right subtree)
            successor = current.right
            while successor.left is not None:
                successor = successor.left

            # Replace the node's data with that of its in-order successor
            current.data = successor.data

            # Recursively delete the in-order successor
            self.delete(successor.data)

        return True
