import random
import math

# -----------------------------
# Problem Setup
# -----------------------------

GRID_SIZE = 25

blocks = [
    ("ALU", 5, 5),
    ("Cache", 7, 4),
    ("Control", 4, 4),
    ("Register", 6, 6),
    ("Decoder", 5, 3),
    ("Floating", 5, 5)
]

# connections (indices)
connections = [
    (3, 0),  # Register → ALU
    (2, 0),  # Control → ALU
    (0, 1),  # ALU → Cache
    (3, 5),  # Register → Floating
    (1, 4),  # Cache → Decoder
    (4, 5)   # Decoder → Floating
]

ALPHA = 1000
BETA = 2
GAMMA = 1

POP_SIZE = 6
GENERATIONS = 15
MUTATION_RATE = 0.1

# -----------------------------
# Helper Functions
# -----------------------------

def random_chromosome():
    return [(random.randint(0, GRID_SIZE), random.randint(0, GRID_SIZE)) for _ in range(6)]

def get_rect(pos, block):
    x, y = pos
    w, h = block[1], block[2]
    return (x, y, x + w, y + h)

# -----------------------------
# Overlap Calculation
# -----------------------------

def overlap_count(chrom):
    count = 0
    for i in range(6):
        for j in range(i+1, 6):
            A = get_rect(chrom[i], blocks[i])
            B = get_rect(chrom[j], blocks[j])

            if not (A[2] <= B[0] or A[0] >= B[2] or
                    A[1] >= B[3] or A[3] <= B[1]):
                count += 1
    return count

# -----------------------------
# Wiring Distance
# -----------------------------

def center(pos, block):
    x, y = pos
    w, h = block[1], block[2]
    return (x + w/2, y + h/2)

def wiring_length(chrom):
    total = 0
    for i, j in connections:
        c1 = center(chrom[i], blocks[i])
        c2 = center(chrom[j], blocks[j])
        dist = math.dist(c1, c2)
        total += dist
    return total

# -----------------------------
# Bounding Area
# -----------------------------

def bounding_area(chrom):
    xs = []
    ys = []

    for i in range(6):
        x, y = chrom[i]
        w, h = blocks[i][1], blocks[i][2]
        xs.extend([x, x + w])
        ys.extend([y, y + h])

    return (max(xs) - min(xs)) * (max(ys) - min(ys))

# -----------------------------
# Fitness Function
# -----------------------------

def fitness(chrom):
    overlaps = overlap_count(chrom)
    wire = wiring_length(chrom)
    area = bounding_area(chrom)

    fit = -(ALPHA * overlaps + BETA * wire + GAMMA * area)
    return fit, overlaps, wire, area

# -----------------------------
# Selection (Tournament)
# -----------------------------

def select(pop):
    return max(random.sample(pop, 2), key=lambda x: fitness(x)[0])

# -----------------------------
# Crossover (Single Point)
# -----------------------------

def crossover(p1, p2):
    point = random.randint(1, 5)
    child1 = p1[:point] + p2[point:]
    child2 = p2[:point] + p1[point:]
    return child1, child2

# -----------------------------
# Mutation
# -----------------------------

def mutate(chrom):
    if random.random() < MUTATION_RATE:
        i = random.randint(0, 5)
        chrom[i] = (random.randint(0, GRID_SIZE),
                    random.randint(0, GRID_SIZE))
    return chrom

# -----------------------------
# GA MAIN LOOP
# -----------------------------

def genetic_algorithm():
    population = [random_chromosome() for _ in range(POP_SIZE)]

    best = None

    for gen in range(GENERATIONS):
        new_pop = []

        # elitism (keep best 1)
        population.sort(key=lambda x: fitness(x)[0], reverse=True)
        new_pop.append(population[0])

        while len(new_pop) < POP_SIZE:
            p1 = select(population)
            p2 = select(population)

            c1, c2 = crossover(p1, p2)

            new_pop.append(mutate(c1))
            if len(new_pop) < POP_SIZE:
                new_pop.append(mutate(c2))

        population = new_pop

        best = max(population, key=lambda x: fitness(x)[0])

        print(f"Generation {gen+1}: Best Fitness = {fitness(best)[0]:.2f}")

    return best

# -----------------------------
# RUN
# -----------------------------

best_solution = genetic_algorithm()

fit, overlaps, wire, area = fitness(best_solution)

print("\nBest Layout:")
for i, pos in enumerate(best_solution):
    print(blocks[i][0], pos)

print("\nFinal Results:")
print("Fitness:", fit)
print("Overlaps:", overlaps)
print("Wiring Length:", wire)
print("Bounding Area:", area)