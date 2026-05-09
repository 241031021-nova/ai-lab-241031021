def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()

    node = path[-1]

    if node == goal:
        return path

    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            new_path = dfs(graph, start, goal, path + [neighbor], visited)
            if new_path:
                return new_path
    return None