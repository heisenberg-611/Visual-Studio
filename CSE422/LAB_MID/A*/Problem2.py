from collections import deque # Import deque from collections module to use it as an efficient queue for BFS

def check_admissibility(): # Define a function to evaluate if a given heuristic is admissible
    n, m = map(int, input().split()) # Read integers n (number of nodes) and m (number of edges)
    start, goal = map(int, input().split()) # Read integers representing the starting node and the goal node

    # Read heuristic values
    h = {} # Initialize an empty dictionary to store the heuristic value for each node
    for _ in range(n): # Loop n times to read the heuristic for every node
        node, value = map(int, input().split()) # Read the node number and its corresponding heuristic value
        h[node] = value # Map the specific node to its heuristic value in the dictionary

    # Build graph
    graph = {} # Initialize an empty dictionary to represent the graph via an adjacency list
    for i in range(1, n + 1): # Loop over each node from 1 to n (inclusive)
        graph[i] = [] # Initialize each node's adjacent list as empty

    for _ in range(m): # Loop m times to read all the graph edges
        u, v = map(int, input().split()) # Read the nodes u and v that are connected by an edge
        graph[u].append(v) # Add node v to the adjacency list of node u (undirected edge)
        graph[v].append(u) # Add node u to the adjacency list of node v (undirected edge)

    # BFS from goal
    dist = {} # Initialize a dictionary to store shortest path distances from the goal to all other nodes
    for i in range(1, n + 1): # Loop from node 1 to node n
        dist[i] = -1   # Initialize all distances to -1, which means 'not yet visited'

    dist[goal] = 0 # The shortest path distance from the goal to itself is 0
    queue = deque([goal]) # Initialize the BFS queue containing the goal node as the starting point

    while queue: # Run the loop as long as there are nodes to process in the BFS queue
        node = queue.popleft() # Remove and get the first node from the queue's left side
        for neighbor in graph[node]: # Loop through each neighbor connected to the current node
            if dist[neighbor] == -1: # If the neighbor hasn't been visited before (distance is -1)
                dist[neighbor] = dist[node] + 1 # Set the neighbor's shortest path distance from goal (dist[node] + 1 step)
                queue.append(neighbor) # Push the newly visited neighbor node into the back of the queue

    # Check admissibility
    ok = True # Flag variable assumed True, representing that the heuristic is admissible
    bad_nodes = [] # List to store any nodes that violate the admissibility property

    for i in range(1, n + 1): # Check the admissibility condition for each node in the graph
        if h[i] > dist[i]: # The condition h(n) <= h*(n). If heuristic h(n) is greater than the actual true cost dist[i]...
            ok = False # Set the flag to False because the heuristic is inadmissible
            bad_nodes.append(i) # Append the violating node to the 'bad_nodes' list

    # Output
    if ok: # After checking all nodes, check if the admissible flag is still True
        print(1) # Print 1 if the heuristic is admissible for all nodes
    else: # If ok is False, the heuristic is inadmissible
        print(0) # Print 0 representing inadmissibility
        print(*bad_nodes) # Print all the nodes which violated admissibility separated by spaces


check_admissibility() # Execute the entry point function