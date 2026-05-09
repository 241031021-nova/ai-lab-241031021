# ==============================
# MiniMax Algorithm
# ==============================

import math

def minimax(depth, node_index, maximizing_player, values, height):

    # Leaf node reached
    if depth == height:
        return values[node_index]

    # Maximizing player
    if maximizing_player:
        return max(
            minimax(depth + 1, node_index * 2, False, values, height),
            minimax(depth + 1, node_index * 2 + 1, False, values, height)
        )

    # Minimizing player
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, values, height),
            minimax(depth + 1, node_index * 2 + 1, True, values, height)
        )


# Leaf node values
values = [3, 5, 2, 9, 12, 5, 23, 23]

# Height of tree
height = int(math.log2(len(values)))

result = minimax(0, 0, True, values, height)

print("Optimal Value:", result)