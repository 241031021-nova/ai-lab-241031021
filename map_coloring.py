# ==============================
# Map Coloring Problem
# ==============================

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

colors = ['Red', 'Green', 'Blue']

def is_valid(node, color, coloring):
    for neighbor in graph[node]:
        if neighbor in coloring and coloring[neighbor] == color:
            return False
    return True

def map_coloring(coloring={}, nodes=list(graph.keys())):
    if not nodes:
        return coloring

    node = nodes[0]

    for color in colors:
        if is_valid(node, color, coloring):
            coloring[node] = color

            result = map_coloring(coloring, nodes[1:])

            if result:
                return result

            del coloring[node]

    return None

print("Map Coloring:", map_coloring())