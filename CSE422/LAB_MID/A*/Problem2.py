from collections import deque

def check_admissibility():
    n, m = map(int, input().split())
    start, goal = map(int, input().split())

    # Read heuristic values
    h = {}
    for _ in range(n):
        node, value = map(int, input().split())
        h[node] = value

    # Build graph
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # BFS from goal
    dist = {}
    for i in range(1, n + 1):
        dist[i] = -1   # -1 means not visited

    dist[goal] = 0
    queue = deque([goal])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

    # Check admissibility
    ok = True
    bad_nodes = []

    for i in range(1, n + 1):
        if h[i] > dist[i]:
            ok = False
            bad_nodes.append(i)

    # Output
    if ok:
        print(1)
    else:
        print(0)
        print(*bad_nodes)


check_admissibility()