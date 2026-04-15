import random # Import the random module to generate random numbers and choices
import math # Import the math module to use mathematical functions like calculating distance

# -----------------------------
# Problem Setup
# -----------------------------

GRID_SIZE = 25 # Define the size of the grid (25x25) for placing blocks

blocks = [ # Define a list of tuples representing the blocks to be placed
    ("ALU", 5, 5), # Block 0: ALU with width 5 and height 5
    ("Cache", 7, 4), # Block 1: Cache with width 7 and height 4
    ("Control", 4, 4), # Block 2: Control with width 4 and height 4
    ("Register", 6, 6), # Block 3: Register with width 6 and height 6
    ("Decoder", 5, 3), # Block 4: Decoder with width 5 and height 3
    ("Floating", 5, 5) # Block 5: Floating with width 5 and height 5
]

# connections (indices)
connections = [ # Define pairs of blocks that must be connected by wire
    (3, 0),  # Required wire from Register (index 3) to ALU (index 0)
    (2, 0),  # Required wire from Control (index 2) to ALU (index 0)
    (0, 1),  # Required wire from ALU (index 0) to Cache (index 1)
    (3, 5),  # Required wire from Register (index 3) to Floating (index 5)
    (1, 4),  # Required wire from Cache (index 1) to Decoder (index 4)
    (4, 5)   # Required wire from Decoder (index 4) to Floating (index 5)
]

ALPHA = 1000 # Penalty coefficient for overlapping blocks
BETA = 2 # Penalty coefficient for the total wiring length
GAMMA = 1 # Penalty coefficient for the total bounding area

POP_SIZE = 6 # Set the population size for the genetic algorithm to 6
GENERATIONS = 15 # Set the total number of generations to 15
MUTATION_RATE = 0.1 # Set the chance of mutation happening to 10%

# -----------------------------
# Helper Functions
# -----------------------------

def random_chromosome(): # Function to generate a random chromosome (layout configuration)
    return [(random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE)) for _ in range(6)] # Return a list of 6 random (x, y) coordinates within the grid

def get_rect(pos, block): # Function to calculate the bounding box of a specific block
    x, y = pos # Unpack the given x, y coordinates
    w, h = block[1], block[2] # Unpack the width and height of the block
    return (x, y, x + w, y + h) # Return a tuple containing (xmin, ymin, xmax, ymax)

# -----------------------------
# Overlap Calculation
# -----------------------------

def overlap_count(chrom): # Function to count the number of overlaps between blocks in a chromosome
    count = 0 # Initialize overlap counter to 0
    for i in range(6): # Loop over each block index from 0 to 5
        for j in range(i+1, 6): # Loop over subsequent block indices from i+1 to 5 to avoid redundant checks
            A = get_rect(chrom[i], blocks[i]) # Get the rectangle boundaries for block i
            B = get_rect(chrom[j], blocks[j]) # Get the rectangle boundaries for block j

            if not (A[2] <= B[0] or A[0] >= B[2] or # Check if rectangles do NOT overlap horizontally ...
                    A[1] >= B[3] or A[3] <= B[1]): # ... or vertically. If they don't meet these separation conditions, they overlap.
                count += 1 # Increment overlap counter
    return count # Return the total number of overlaps found

# -----------------------------
# Wiring Distance
# -----------------------------

def center(pos, block): # Function to find the center coordinate of a block
    x, y = pos # Extract the top-left x, y coordinates
    w, h = block[1], block[2] # Extract the width and height
    return (x + w/2, y + h/2) # Calculate and return the center (x, y)

def wiring_length(chrom): # Function to calculate the total length of all wired connections
    total = 0 # Initialize total wire length to 0
    for i, j in connections: # Iterate over each required connection pair
        c1 = center(chrom[i], blocks[i]) # Get center coordinates of the start block
        c2 = center(chrom[j], blocks[j]) # Get center coordinates of the end block
        dist = math.dist(c1, c2) # Calculate the Euclidean distance between the two centers
        total += dist # Add the distance to the total
    return total # Return the total computed wire length

# -----------------------------
# Bounding Area
# -----------------------------

def bounding_area(chrom): # Function to calculate the overall bounding footprint area of the entire layout
    xs = [] # Initialize a list to hold all x coordinates
    ys = [] # Initialize a list to hold all y coordinates

    for i in range(6): # Iterate through all 6 blocks
        x, y = chrom[i] # Get the top-left coordinate of block i
        w, h = blocks[i][1], blocks[i][2] # Get width and height of block i
        xs.extend([x, x + w]) # Add the left and right x-bounds to the list
        ys.extend([y, y + h]) # Add the top and bottom y-bounds to the list

    return (max(xs) - min(xs)) * (max(ys) - min(ys)) # Compute area by multiplying maximum span in x by maximum span in y

# -----------------------------
# Fitness Function
# -----------------------------

def fitness(chrom): # Function to evaluate the fitness of a chromosome
    overlaps = overlap_count(chrom) # Call helper to get number of overlaps
    wire = wiring_length(chrom) # Call helper to get total wire length
    area = bounding_area(chrom) # Call helper to get bounding area

    fit = -(ALPHA * overlaps + BETA * wire + GAMMA * area) # Compute the fitness as a negative penalty (we want to minimize overlaps, wire, area)
    return fit, overlaps, wire, area # Return the computed fitness along with the raw metrics

# -----------------------------
# Selection (Tournament)
# -----------------------------

def select(pop): # Function to select a parent from the population using tournament selection
    return max(random.sample(pop, 2), key=lambda x: fitness(x)[0]) # Pick 2 random chromosomes, return the one with higher fitness

# -----------------------------
# Crossover (Single Point)
# -----------------------------

def crossover(p1, p2): # Function to perform a single-point crossover between two parent chromosomes
    point = random.randint(1, 5) # Select a random crossover point index between 1 and 5
    child1 = p1[:point] + p2[point:] # Build child 1: left part from parent 1, right part from parent 2
    child2 = p2[:point] + p1[point:] # Build child 2: left part from parent 2, right part from parent 1
    return child1, child2 # Return the two new children

# -----------------------------
# Mutation
# -----------------------------

def mutate(chrom): # Function to perform random mutation on a chromosome
    if random.random() < MUTATION_RATE: # Check if a uniformly random float [0.0, 1.0) is less than the mutation rate
        i = random.randint(0, 5) # Randomly select one block to mutate
        chrom[i] = (random.randint(0, GRID_SIZE), # Change block i's x coordinate to a random new valid value
                    random.randint(0, GRID_SIZE)) # Change block i's y coordinate to a random new valid value
    return chrom # Return mutated (or unmodified) chromosome

# -----------------------------
# GA MAIN LOOP
# -----------------------------

def genetic_algorithm(): # The main function that runs the genetic algorithm
    population = [random_chromosome() for _ in range(POP_SIZE)] # Initialize the first generation with completely random chromosomes

    best = None # Keep track of the all-time best chromosome across all generations

    for gen in range(GENERATIONS): # Loop for the specified number of generations
        new_pop = [] # Initialize an empty list for the next generation's population

        # elitism (keep best 1)
        population.sort(key=lambda x: fitness(x)[0], reverse=True) # Sort current population descending by fitness
        new_pop.append(population[0]) # Add the very best chromosome straight into the new generation (Elitism)

        while len(new_pop) < POP_SIZE: # Loop until the new population reaches the target size
            p1 = select(population) # Select the first parent
            p2 = select(population) # Select the second parent

            c1, c2 = crossover(p1, p2) # Generate 2 children by crossing over parents

            new_pop.append(mutate(c1)) # Mutate first child and add it to the next generation
            if len(new_pop) < POP_SIZE: # Ensure we do not exceed POP_SIZE
                new_pop.append(mutate(c2)) # Mutate second child and add it if there's still room

        population = new_pop # Replace the old population with the new generation

        best = max(population, key=lambda x: fitness(x)[0]) # Evaluate the actual best chromosome in this new population

        print(f"Generation {gen+1}: Best Fitness = {fitness(best)[0]:.2f}") # Print progress of the best fitness so far

    return best # Return the best solution found after all generations

# -----------------------------
# RUN
# -----------------------------

best_solution = genetic_algorithm() # Execute the algorithm and capture the best result layout

fit, overlaps, wire, area = fitness(best_solution) # Re-calculate its stats for reporting

print("\nBest Layout:") # Print header
for i, pos in enumerate(best_solution): # Loop over each placed block
    print(blocks[i][0], pos) # Output block name and its final generated coordinate

print("\nFinal Results:") # Print header
print("Fitness:", fit) # Display best layout's calculated fitness score
print("Overlaps:", overlaps) # Display best layout's overlap count
print("Wiring Length:", wire) # Display best layout's total wiring distance
print("Bounding Area:", area) # Display best layout's computed bounding box area