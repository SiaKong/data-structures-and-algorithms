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
    def delete(self, val, node=None):
        if not node:
            node = self.root
        if not node:
            return None
        if val < node.val:
            node.left = self.delete(val, node.left)
        elif val > node.val:
            node.right = self.delete(val, node.right)
        else:
            if not node.left and not node.right:
                return None
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                min_val = self.find_min(node.right)
                node.val = min_val
                node.right = self.delete(min_val, node.right)
        return node