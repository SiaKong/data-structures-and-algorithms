#O(|V| + |E|) where V is the set of vertices and E is the set of edges

def dfs(graph, root):
    stack = []
    visited = []

    stack.append(root)

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex)
            visited.append(vertex)
            for neighbor in graph[vertex]:
                stack.append(neighbor)

# Example usage
graph = {
    'A': ['B', 'G'],
    'B': ['C','D', 'E'],
    'C': [],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': ['H'],
    'H': ['I'],
    'I': []
}

dfs(graph, 'A')