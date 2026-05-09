# ==============================
# Alpha-Beta Pruning
# ==============================

import math

MAX = 1000
MIN = -1000

def alpha_beta(depth, node_index, maximizing_player,
               values, alpha, beta, height):

    # Leaf node reached
    if depth == height:
        return values[node_index]

    # Maximizing player
    if maximizing_player:

        best = MIN

        for i in range(2):

            val = alpha_beta(
                depth + 1,
                node_index * 2 + i,
                False,
                values,
                alpha,
                beta,
                height
            )

            best = max(best, val)
            alpha = max(alpha, best)

            # Beta pruning
            if beta <= alpha:
                break

        return best

    # Minimizing player
    else:

        best = MAX

        for i in range(2):

            val = alpha_beta(
                depth + 1,
                node_index * 2 + i,
                True,
                values,
                alpha,
                beta,
                height
            )

            best = min(best, val)
            beta = min(beta, best)

            # Alpha pruning
            if beta <= alpha:
                break

        return best


# Leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Height of tree
height = int(math.log2(len(values)))

result = alpha_beta(
    0,
    0,
    True,
    values,
    MIN,
    MAX,
    height
)

print("Optimal Value:", result)