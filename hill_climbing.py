# ==============================
# Hill Climbing
# ==============================

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

def hill_climbing(graph, start):
    current = start

    while True:
        neighbors = graph[current]

        if not neighbors:
            return current

        next_node = min(neighbors, key=lambda x: heuristic[x])

        if heuristic[next_node] >= heuristic[current]:
            return current

        current = next_node

print("Hill Climbing Result:", hill_climbing(graph, 'A'))