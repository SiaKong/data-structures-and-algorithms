#O(|V| + |E|) with DFS

def topological_sort(graph):
    # Create a stack to hold the sorted elements
    stack = []
    # Create a set to keep track of visited nodes
    visited = set()
    
    def dfs(node):
        # Mark the current node as visited
        visited.add(node)
        # Visit all the unvisited neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        # Push the current node to the stack
        stack.append(node)
    
    # Visit all the nodes in the graph
    for node in graph:
        if node not in visited:
            dfs(node)
    
    return stack[::-1]

graph = {
    'A': ['D'],
    'B': ['D'],
    'C': [],
    'D': ['C'],
    'E': [],
    'F': ['B','A']
}


print(topological_sort(graph))

#returns ['F', 'E', 'B', 'A', 'D', 'C']
#but also can be ['F', 'E', 'A', 'B', 'D', 'C']