def crossover(p1, p2):
    # choose two points
    point1 = random.randint(1, 4)
    point2 = random.randint(point1 + 1, 5)

    # create children
    child1 = p1[:point1] + p2[point1:point2] + p1[point2:]
    child2 = p2[:point1] + p1[point1:point2] + p2[point2:]

    return child1, child2
