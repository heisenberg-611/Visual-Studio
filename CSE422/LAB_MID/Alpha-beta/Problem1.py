import math # Import the math module to use mathematical constants like infinity

def utility(gene, target, weights): # Function to calculate the utility score of a given gene sequence
    score = 0 # Initialize the final score to 0
    n = max(len(gene), len(target)) # Find the maximum length between the generated gene and the target gene

    for i in range(n): # Loop through each character position up to the maximum length
        g = ord(gene[i]) if i < len(gene) else 0 # Get ASCII value of gene char or 0 if index is out of bounds
        t = ord(target[i]) if i < len(target) else 0 # Get ASCII value of target char or 0 if index is out of bounds
        w = weights[i] if i < len(weights) else 1 # Get the weight for this position or 1 if index is out of bounds

        score += w * abs(g - t) # Calculate difference, multiply by weight and add to the total score

    return -score # Return the negative score (because the problem likely requires maximizing negative penalty)


def minimax(gene, pool, target, weights, is_max, alpha, beta): # Recursive Minimax algorithm with alpha-beta pruning
    if not pool: # Base case: if the character pool is empty, the terminal state is reached
        return utility(gene, target, weights), gene # Return the computed utility and the sequence itself

    if is_max: # If it is the maximizing player's turn
        best_score = -math.inf # Initialize the best score as negative infinity
        best_seq = "" # Initialize the best sequence as empty string

        for i in range(len(pool)): # Loop through each available character in the pool
            new_gene = gene + pool[i] # Create a new gene by appending the chosen character
            new_pool = pool[:i] + pool[i+1:] # Create a new pool by removing the chosen character

            score, seq = minimax(new_gene, new_pool, target, weights, False, alpha, beta) # Recursively call minimax for the minimizing player

            if score > best_score: # Update best score and sequence if the current score is greater
                best_score = score # Set new best score for the maximizer
                best_seq = seq # Update the best sequence

            alpha = max(alpha, best_score) # Update the alpha value
            if beta <= alpha: # Alpha-beta pruning condition
                break # Prune the search tree if beta is less than or equal to alpha

        return best_score, best_seq # Return the highest score and the resulting sequence

    else: # If it is the minimizing player's turn
        best_score = math.inf # Initialize the best score as positive infinity
        best_seq = "" # Initialize the best sequence as empty string

        for i in range(len(pool)): # Loop through each available character in the pool
            new_gene = gene + pool[i] # Create a new gene by appending the chosen character
            new_pool = pool[:i] + pool[i+1:] # Delete the chosen character from the pool

            score, seq = minimax(new_gene, new_pool, target, weights, True, alpha, beta) # Recursively call minimax for the maximizing player

            if score < best_score: # Update best score and sequence if the current score is smaller
                best_score = score # Set new best score for the minimizer
                best_seq = seq # Update the best sequence

            beta = min(beta, best_score) # Update the beta value
            if beta <= alpha: # Alpha-beta pruning condition
                break # Prune the search tree if beta is less than or equal to alpha

        return best_score, best_seq # Return the lowest score and the resulting sequence


# -------- INPUT --------
pool = input().split(",") # Read the input, split by comma to create the character pool
target = input().strip() # Read the target sequence and strip any trailing whitespaces
sid = list(map(int, input().split())) # Read the student ID digits, convert each to an integer, and store in a list

# Take last n digits (n = len(target))
weights = sid[-len(target):] # Extract the last N digits from the student ID to use as weights, where N is target length

score, sequence = minimax("", pool, target, weights, True, -math.inf, math.inf) # Call initially with empty string, max player turn, alpha=-inf, beta=inf

print("Best gene sequence generated:", sequence) # Output the sequence that resulted in the best score
print("Utility score:", score) # Output the best utility score found