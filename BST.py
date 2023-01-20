class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node, node=None):
        if not node:
            node = self.root
        if not node:
            self.root = new_node
            return
        if new_node.val < node.val:
            if not node.left:
                node.left = new_node
            else:
                self.insert(new_node, node.left)
        else:
            if not node.right:
                node.right = new_node
            else:
                self.insert(new_node, node.right)

    def search(self, search_node, node=None):
        if not node:
            node = self.root
        if not node:
            return False
        if search_node.val == node.val:
            return True
        elif search_node.val < node.val:
            return self.search(search_node, node.left)
        else:
            return self.search(search_node, node.right)