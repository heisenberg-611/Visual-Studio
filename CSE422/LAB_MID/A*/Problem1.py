import heapq # Import the heapq module to use the priority queue for the A* search algorithm

direction = [ # Define a list containing the possible movement directions for the agent
    (-1, 0, 'U'), # Move Up: decrement row by 1, column unchanged, abbreviation 'U'
    (1, 0, 'D'),  # Move Down: increment row by 1, column unchanged, abbreviation 'D'
    (0, -1, 'L'), # Move Left: row unchanged, decrement column by 1, abbreviation 'L'
    (0, 1, 'R')   # Move Right: row unchanged, increment column by 1, abbreviation 'R'
]

def manhattan(x1, x2, y1, y2): # Define a function to calculate a heuristic distance
    return abs(x1-x2) + abs(y1-y2) # Return the sum of absolute differences between the given parameters

def astar(n, m, start, goal, maze): # Define the A* search algorithm function
    visited = set() # Create an empty set to keep track of visited cells in the maze
    pq =[] # Initialize an empty list that will be used as the priority queue
    sx, sy = start # Unpack the starting cell coordinates into sx and sy
    gx, gy = goal # Unpack the goal cell coordinates into gx and gy

    h = manhattan(sx, sy, gx, gy) # Calculate the initial heuristic (h-score) from start to goal
    heapq.heappush(pq, (h, 0, sx, sy, "")) # Push the starting node into the priority queue (f-score, g-score, x, y, path)

    while pq: # Start a loop that will run as long as there are nodes to explore in the priority queue
        f, g, x, y, path = heapq.heappop(pq) # Pop the node with the lowest f-score from the priority queue

        if(x, y) in visited: # Check if the current cell has already been visited
            continue # If it has been visited before, skip to the next iteration of the loop

        visited.add((x, y)) # Add the current cell to the visited set to mark it as explored

        if(x,y) == (gx,gy): # Check if the current cell is the goal cell
            return g, path # If it is the goal, return the total cost (g) and the movement path
        
        for dx, dy, move in direction: # Iterate through all possible movement directions
            nx, ny = x + dx, y + dy # Calculate the coordinates of the adjacent cell

            if 0 <= nx < n and 0 <= ny < m: # Check if the newly calculated coordinates are within the maze boundaries
                if maze[nx][ny] == '0' and (nx, ny) not in visited: # Check if the cell is traversable ('0' means path) and not yet visited

                    new_g = g+1 # Calculate the new g-score (cost from start node so far plus 1 for this step)
                    new_h = manhattan(nx, ny, gx, gy) # Calculate the new heuristic h-score from this new node to the goal
                    new_f = new_g + new_h # Calculate the f-score by adding g-score and h-score

                    heapq.heappush(pq,(new_f, new_g, nx, ny, path+move)) # Push the new state into the priority queue
    return -1, "" # If the loop finishes to completion without reaching the goal, return -1 (failure) and an empty path

n, m = map(int, input().split()) # Read the number of rows (n) and columns (m) from the user input
sx, sy = map(int, input().split()) # Read the starting coordinates (sx, sy) from the user input
gx, gy = map(int, input().split()) # Read the goal coordinates (gx, gy) from the user input

maze = [input().strip() for _ in range(n)] # Read 'n' lines of strings to represent the maze grid and store them in a list

cost, path = astar(n, m, (sx, sy), (gx, gy), maze) # Call the A* search function with the given inputs and get cost & path

if cost == -1: # Check if the astar function failed to find a valid path
    print(-1) # Print -1 to signify failure
    print("No path found") # Print a readable text indicating no path was found
else: # If a valid path is found
    print("Total step: ", cost) # Print the total number of steps (cost) taken to reach the goal
    print("->".join(path)) # Print the path found by joining the move characters with "->"