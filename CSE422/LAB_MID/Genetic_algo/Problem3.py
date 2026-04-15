import random # Import the random module to generate random integers and selections

# ---------------------------
# STEP 1: Create Chromosome
# ---------------------------
def create_chromosome(): # Function to generate a new random individual
    return { # Return a dictionary representing the chromosome configuration
        "stop_loss": random.randint(1, 99), # Generate a random integer from 1 to 99 for stop_loss percentage
        "take_profit": random.randint(1, 99), # Generate a random integer from 1 to 99 for take_profit percentage
        "trade_size": random.randint(1, 99) # Generate a random integer from 1 to 99 for trade_size percentage
    }


# ---------------------------
# STEP 2: Initialize Population
# ---------------------------
def initialize_population(size=4): # Function to generate an initial set of chromosomes
    return [create_chromosome() for _ in range(size)] # Return a list of 'size' randomly created chromosomes


# ---------------------------
# STEP 3: Fitness Function
# ---------------------------
def calculate_fitness(chromosome, prices): # Evaluate how well a strategy (chromosome) performs
    capital = 1000 # Set the starting capital baseline to $1000

    sl = chromosome["stop_loss"] / 100 # Convert the integer stop-loss to a float ratio
    tp = chromosome["take_profit"] / 100 # Convert the integer take-profit to a float ratio
    ts = chromosome["trade_size"] / 100 # Convert the integer trade-size to a float ratio

    for change in prices: # Loop chronologically through each simulated price change event
        trade_amount = capital * ts # Evaluate the capital risked on this specific trade

        # Apply Stop-Loss
        if change < -sl * 100: # Check if the price drop exceeds the allocated stop-loss limit
            profit = -trade_amount * sl # Take the calculated max loss explicitly due to closing early

        # Apply Take-Profit
        elif change > tp * 100: # Check if the price surge exceeds the take-profit mark limit
            profit = trade_amount * tp # Secure the allocated exact profit due to closing trade early

        # Normal case
        else: # Normal holding period (no limits hit)
            profit = trade_amount * (change / 100) # Gain or lose exactly parallel to market price change proportion

        capital += profit # Adjust the current working capital with this trade's profit or loss

    return capital - 1000 # Return the net profit generated compared to the starting baseline


# ---------------------------
# STEP 4: Select Parents
# ---------------------------
def select_parents(population): # Function to blindly select two parents
    return random.sample(population, 2) # Pick two distinct chromosomes at random from the population


# ---------------------------
# STEP 5: Single Point Crossover
# ---------------------------
def crossover(p1, p2): # Perform a single block single-point crossover utilizing encoding representation
    def encode(c): # Helper inner function to encode dictionary states to a 6-digit continuous string
        return f"{int(c['stop_loss']):02}{int(c['take_profit']):02}{int(c['trade_size']):02}" # Format integers cleanly into padded strings 

    def decode(s): # Helper inner function to decode a 6-digit string back into a workable config dictionary
        return { # Construct and return equivalent dictionary mapping
            "stop_loss": int(s[0:2]), # First 2 characters define stop loss
            "take_profit": int(s[2:4]), # Middle 2 characters define take profit
            "trade_size": int(s[4:6]) # Final 2 characters dictate trade size
        }

    s1 = encode(p1) # Serialize first parent
    s2 = encode(p2) # Serialize second parent

    point = random.randint(1, 5) # Generate random crossover splitting point index inside the string

    child1 = s1[:point] + s2[point:] # Form child 1 using part from parent1 and rest from parent2
    child2 = s2[:point] + s1[point:] # Form child 2 using part from parent2 and rest from parent1

    return decode(child1), decode(child2) # Return the properly deserialized new children dictionaries


# ---------------------------
# STEP 6: Mutation
# ---------------------------
def mutate(chromosome, rate=0.05): # Function to randomly jump state fields (approx 5% per gene)
    for key in chromosome: # Iterate over the config keys
        if random.random() < rate: # By random chance, execute mutation block
            chromosome[key] = random.randint(1, 99) # Reassign entire parameter completely within bounds
    return chromosome # Return modified state


# ---------------------------
# STEP 7: Next Generation
# ---------------------------
def next_generation(population, prices): # Advance iteration clock and rebreed population pool
    # Sort by fitness (best first)
    population = sorted(population, key=lambda x: calculate_fitness(x, prices), reverse=True) # Process all scores and sort in descending order of utility

    # Keep best 2 (elitism)
    new_pop = population[:2] # Pass the top 2 outright to the next cycle directly

    # Create rest using crossover + mutation
    while len(new_pop) < 4: # Supplement population until maximum pool size is met
        p1, p2 = select_parents(population) # Grab a set of parents unconditionally
        c1, c2 = crossover(p1, p2) # Apply reproduction rules 

        new_pop.append(mutate(c1)) # Register a mutated variant of child 1
        if len(new_pop) < 4: # Sanity bound check
            new_pop.append(mutate(c2)) # Register mutated variant of child 2

    return new_pop # Provide output replacement cluster


# ---------------------------
# STEP 8: Run GA
# ---------------------------
def run_ga(): # Main control execution loop mapping
    prices = [-1.2, 3.4, -0.8, 2.1, -2.5, 1.7, -0.3, 5.8, -1.1, 3.5] # Defined static market history data list

    population = initialize_population() # Produce raw first attempt pool

    for _ in range(10): # Advance simulation 10 steps sequentially
        population = next_generation(population, prices) # Trigger life cycle replacement routines

    best = max(population, key=lambda x: calculate_fitness(x, prices)) # Check entire mature remaining pool for all-time peak candidate

    print("Best Strategy:", best) # Print optimal layout representation parameters
    print("Final Profit:", calculate_fitness(best, prices)) # Produce raw numeric proof of strategy efficacy


# ---------------------------
# PART 2: Two Point Crossover
# ---------------------------
def two_point_crossover(p1, p2): # Similar reproduction routine demonstrating alternative two section mixing string manipulation 
    s1 = f"{p1['stop_loss']:02}{p1['take_profit']:02}{p1['trade_size']:02}" # Pre-encode parent 1 identically to part 1
    s2 = f"{p2['stop_loss']:02}{p2['take_profit']:02}{p2['trade_size']:02}" # Pre-encode parent 2 identically identically

    pt1 = random.randint(1, 4) # Select initial cut point offset inside range limits
    pt2 = random.randint(pt1 + 1, 5) # Select secondary cut point reliably posterior to first selection

    child1 = s1[:pt1] + s2[pt1:pt2] + s1[pt2:] # Child 1 string creation from mixed sectors correctly ordered
    child2 = s2[:pt1] + s1[pt1:pt2] + s2[pt2:] # Child 2 string mirror operation alternative section pulls 

    return child1, child2 # Hand back encoded string format data blocks for future conversion/usage


# ---------------------------
# MAIN RUN
# ---------------------------
if __name__ == "__main__": # Evaluate root level initiation instruction check
    run_ga() # Fire procedure 1

    # Part 2 Example
    p1 = create_chromosome() # Scaffold mock demo parent object 1
    p2 = create_chromosome() # Scaffold mock demo parent object 2

    print("\nParent 1:", p1) # Display diagnostic payload input 1
    print("Parent 2:", p2) # Display diagnostic payload input 2

    c1, c2 = two_point_crossover(p1, p2) # Fire functional test
    print("Children after 2-point crossover:", c1, c2) # Verify payload results print properly