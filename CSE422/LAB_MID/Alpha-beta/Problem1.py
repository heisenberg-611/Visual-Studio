import math

def utility(gene, target, weights):
    score = 0
    n = max(len(gene), len(target))

    for i in range(n):
        g = ord(gene[i]) if i < len(gene) else 0
        t = ord(target[i]) if i < len(target) else 0
        w = weights[i] if i < len(weights) else 1

        score += w * abs(g - t)

    return -score


def minimax(gene, pool, target, weights, is_max, alpha, beta):
    if not pool:
        return utility(gene, target, weights), gene

    if is_max:
        best_score = -math.inf
        best_seq = ""

        for i in range(len(pool)):
            new_gene = gene + pool[i]
            new_pool = pool[:i] + pool[i+1:]

            score, seq = minimax(new_gene, new_pool, target, weights, False, alpha, beta)

            if score > best_score:
                best_score = score
                best_seq = seq

            alpha = max(alpha, best_score)
            if beta <= alpha:
                break

        return best_score, best_seq

    else:
        best_score = math.inf
        best_seq = ""

        for i in range(len(pool)):
            new_gene = gene + pool[i]
            new_pool = pool[:i] + pool[i+1:]

            score, seq = minimax(new_gene, new_pool, target, weights, True, alpha, beta)

            if score < best_score:
                best_score = score
                best_seq = seq

            beta = min(beta, best_score)
            if beta <= alpha:
                break

        return best_score, best_seq


# -------- INPUT --------
pool = input().split(",")
target = input().strip()
sid = list(map(int, input().split()))

# Take last n digits (n = len(target))
weights = sid[-len(target):]

score, sequence = minimax("", pool, target, weights, True, -math.inf, math.inf)

print("Best gene sequence generated:", sequence)
print("Utility score:", score)