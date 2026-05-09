# ==============================
# Greedy Best First Search
# ==============================

import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

heuristic = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 6,
    'E': 3,
    'F': 0
}

def greedy_bfs(graph, start, goal):
    pq = [(heuristic[start], [start])]
    visited = set()

    while pq:
        h, path = heapq.heappop(pq)
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                heapq.heappush(
                    pq,
                    (heuristic[neighbor], path + [neighbor])
                )

    return None

print("Greedy BFS:", greedy_bfs(graph, 'A', 'F'))