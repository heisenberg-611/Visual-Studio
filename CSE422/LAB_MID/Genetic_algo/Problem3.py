import random

# ---------------------------
# STEP 1: Create Chromosome
# ---------------------------
def create_chromosome():
    return {
        "stop_loss": random.randint(1, 99),
        "take_profit": random.randint(1, 99),
        "trade_size": random.randint(1, 99)
    }


# ---------------------------
# STEP 2: Initialize Population
# ---------------------------
def initialize_population(size=4):
    return [create_chromosome() for _ in range(size)]


# ---------------------------
# STEP 3: Fitness Function
# ---------------------------
def calculate_fitness(chromosome, prices):
    capital = 1000

    sl = chromosome["stop_loss"] / 100
    tp = chromosome["take_profit"] / 100
    ts = chromosome["trade_size"] / 100

    for change in prices:
        trade_amount = capital * ts

        # Apply Stop-Loss
        if change < -sl * 100:
            profit = -trade_amount * sl

        # Apply Take-Profit
        elif change > tp * 100:
            profit = trade_amount * tp

        # Normal case
        else:
            profit = trade_amount * (change / 100)

        capital += profit

    return capital - 1000


# ---------------------------
# STEP 4: Select Parents
# ---------------------------
def select_parents(population):
    return random.sample(population, 2)


# ---------------------------
# STEP 5: Single Point Crossover
# ---------------------------
def crossover(p1, p2):
    def encode(c):
        return f"{int(c['stop_loss']):02}{int(c['take_profit']):02}{int(c['trade_size']):02}"

    def decode(s):
        return {
            "stop_loss": int(s[0:2]),
            "take_profit": int(s[2:4]),
            "trade_size": int(s[4:6])
        }

    s1 = encode(p1)
    s2 = encode(p2)

    point = random.randint(1, 5)

    child1 = s1[:point] + s2[point:]
    child2 = s2[:point] + s1[point:]

    return decode(child1), decode(child2)


# ---------------------------
# STEP 6: Mutation
# ---------------------------
def mutate(chromosome, rate=0.05):
    for key in chromosome:
        if random.random() < rate:
            chromosome[key] = random.randint(1, 99)
    return chromosome


# ---------------------------
# STEP 7: Next Generation
# ---------------------------
def next_generation(population, prices):
    # Sort by fitness (best first)
    population = sorted(population, key=lambda x: calculate_fitness(x, prices), reverse=True)

    # Keep best 2 (elitism)
    new_pop = population[:2]

    # Create rest using crossover + mutation
    while len(new_pop) < 4:
        p1, p2 = select_parents(population)
        c1, c2 = crossover(p1, p2)

        new_pop.append(mutate(c1))
        if len(new_pop) < 4:
            new_pop.append(mutate(c2))

    return new_pop


# ---------------------------
# STEP 8: Run GA
# ---------------------------
def run_ga():
    prices = [-1.2, 3.4, -0.8, 2.1, -2.5, 1.7, -0.3, 5.8, -1.1, 3.5]

    population = initialize_population()

    for _ in range(10):
        population = next_generation(population, prices)

    best = max(population, key=lambda x: calculate_fitness(x, prices))

    print("Best Strategy:", best)
    print("Final Profit:", calculate_fitness(best, prices))


# ---------------------------
# PART 2: Two Point Crossover
# ---------------------------
def two_point_crossover(p1, p2):
    s1 = f"{p1['stop_loss']:02}{p1['take_profit']:02}{p1['trade_size']:02}"
    s2 = f"{p2['stop_loss']:02}{p2['take_profit']:02}{p2['trade_size']:02}"

    pt1 = random.randint(1, 4)
    pt2 = random.randint(pt1 + 1, 5)

    child1 = s1[:pt1] + s2[pt1:pt2] + s1[pt2:]
    child2 = s2[:pt1] + s1[pt1:pt2] + s2[pt2:]

    return child1, child2


# ---------------------------
# MAIN RUN
# ---------------------------
if __name__ == "__main__":
    run_ga()

    # Part 2 Example
    p1 = create_chromosome()
    p2 = create_chromosome()

    print("\nParent 1:", p1)
    print("Parent 2:", p2)

    c1, c2 = two_point_crossover(p1, p2)
    print("Children after 2-point crossover:", c1, c2)