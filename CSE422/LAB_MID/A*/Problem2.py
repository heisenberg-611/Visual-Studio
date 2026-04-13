from collections import deque

def check_admissibility():
    n, m = map(int, input().split())
    start, goal = map(int, input().split())

    h = {}
    for _ in range(n):
        x, y = map(int, input().split())
        h[x] = y

    graph = {i: []for i in range(1, n + 1)}
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[goal] = 0

    queue = deque([goal])
    while queue:
        node = queue.popleft()
        for nei in graph[node]:
            if dist[nei] == float('inf'):
                dist[nei] = dist[node]+1
                queue.append(nei)
    not_admissible = []
    for node in range(1, n + 1):
        if h[node] > dist[node]:
            not_admissible.append(node)

    if len(not_admissible) == 0:
        print(1)
    else:
        print(0)
        print("Not admissible nodes:", *not_admissible)
    
check_admissibility()