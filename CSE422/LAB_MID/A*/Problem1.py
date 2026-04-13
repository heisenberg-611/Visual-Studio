import heapq

direction = [
    (-1, 0, 'U'),
    (1, 0, 'D'),
    (0, -1, 'L'),
    (0, 1, 'R')
]

def manhattan(x1, x2, y1, y2):
    return abs(x1-x2) + abs(y1-y2)

def astar(n, m, start, goal, maze):
    visited = set()
    pq =[]
    sx, sy = start
    gx, gy = goal

    h = manhattan(sx, sy, gx, gy)
    heapq.heappush(pq, (h, 0, sx, sy, ""))

    while pq:
        f, g, x, y, path = heapq.heappop(pq)

        if(x, y) in visited:
            continue

        visited.add((x, y))

        if(x,y) == (gx,gy):
            return g, path
        
        for dx, dy, move in direction:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == '0' and (nx, ny) not in visited:

                    new_g = g+1
                    new_h = manhattan(nx, ny, gx, gy)
                    new_f = new_g + new_h

                    heapq.heappush(pq,(new_f, new_g, nx, ny, path+move))
    return -1, ""

n, m = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())

maze = [input().strip() for _ in range(n)]

cost, path = astar(n, m, (sx, sy), (gx, gy), maze)

if cost == -1:
    print(-1)
    print("No path found")
else:
    print("Total step: ", cost)
    print("->".join(path))