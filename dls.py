def dls(graph, node, goal, depth, path=None):
    if path is None:
        path = [node]

    if node == goal:
        return path

    if depth <= 0:
        return None

    for neighbor in graph[node]:
        if neighbor not in path:
            result = dls(graph, neighbor, goal, depth - 1, path + [neighbor])

            if result:
                return result

    return None


# Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print(dls(graph, 'A', 'F', 2))