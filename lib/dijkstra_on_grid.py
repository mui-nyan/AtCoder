from heapq import heappush, heappop
def neighbors4(x, y):
    dxy = ( (0,1), (1,0), (0,-1), (-1,0) )
    for dx,dy in dxy:
        yield(x + dx, y + dy)

def dijkstra_on_grid(grid, sx, sy, gx=None, gy=None, INF=2**31-1):
    h = len(grid)
    w = len(grid[0])
    costs = [ [INF] * w for _ in range(h) ]

    hq = []
    hq.append((0, sx, sy))

    while hq:
        c,x,y = heappop(hq)
        # log(" ", c,x,y)
        if c >= costs[y][x]:
            continue
        costs[y][x] = c

        if gx is not None and x == gx and y == gy:
            return c

        for nx, ny in neighbors4(x, y):
            if nx >= w or ny >= h or nx<0 or ny<0:
                continue
            heappush(hq, (c + grid[ny][nx], nx, ny))

    return costs
