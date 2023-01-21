def bfs(graph, node):
    queue = []
    visited = []

    visited.append(node)
    queue.append(node)
    
    while queue:
        vertex = queue.pop(0)
        print(vertex, end = " ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': ['I', 'J'],
    'G': [],
    'H': [],
    'I': [],
    'J': []
}

bfs(graph, 'A')