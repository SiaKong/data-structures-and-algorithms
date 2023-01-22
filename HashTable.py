# Hash table implementation using linked list
# Lookup: O(1) if minimum collision, if not O(n)

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [None for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        new_node = Node(key, value)
        head = self.buckets[index]
        new_node.next = head
        self.buckets[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None