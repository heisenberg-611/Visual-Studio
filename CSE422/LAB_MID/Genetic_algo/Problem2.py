def crossover(p1, p2): # Function to perform a two-point crossover operation
    # choose two points
    point1 = random.randint(1, 4) # Select the first crossover point randomly between index 1 and 4
    point2 = random.randint(point1 + 1, 5) # Select the second crossover point strictly after the first point, up to index 5

    # create children
    child1 = p1[:point1] + p2[point1:point2] + p1[point2:] # Build child1: p1 start, p2 middle section, p1 end
    child2 = p2[:point1] + p1[point1:point2] + p2[point2:] # Build child2: p2 start, p1 middle section, p2 end

    return child1, child2 # Return the two newly generated children
