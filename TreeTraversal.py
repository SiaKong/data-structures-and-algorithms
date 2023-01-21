#O(n) for all

# A simple binary tree class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Pre-order traversal
def pre_order(root):
    if root:
        print(root.value)
        pre_order(root.left)
        pre_order(root.right)

# In-order traversal
def in_order(root):
    if root:
        in_order(root.left)
        print(root.value)
        in_order(root.right)

# Post-order traversal
def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.value)