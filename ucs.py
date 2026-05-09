# ==============================
# UCS (Uniform Cost Search)
# ==============================

import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [],
    'F': []
}

def ucs(graph, start, goal):
    pq = [(0, start, [])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node not in visited:
            visited.add(node)
            path = path + [node]

            if node == goal:
                return path, cost

            for neighbor, c in graph[node]:
                heapq.heappush(pq, (cost + c, neighbor, path))

    return None

print("UCS:", ucs(graph, 'A', 'F'))