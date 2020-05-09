import math
from functools import reduce
from collections import deque
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def rangeI(it, l, r):
    for i, e in enumerate(it):
        if l <= i < r:
            yield e
        elif l >= r:
            break

def neighbors4(x, y):
  dxy = (0, 1, 0, -1, 0 )
  for i in range(4):
    yield(x + dxy[i], y + dxy[i+1])

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

INF = 999999999999999999999999
MOD = 10**9+7

h,w = get_nums_l()
grid = [ get_nums_l() for _ in range(h) ]

def dijkstra(sx,sy, gx,gy):
    costs = [ [INF] * w for _ in range(h) ]

    hq = []
    hq.append((0, sx, sy))

    while hq:
        c,x,y = heappop(hq)
        # log(" ", c,x,y)
        if c >= costs[y][x]:
            continue
        costs[y][x] = c

        for nx, ny in neighbors4(x, y):
            if nx >= w or ny >= h or nx<0 or ny<0:
                continue
            if gx is not None and nx == gx and ny == gy:
                return c + grid[ny][nx]
            heappush(hq, (c + grid[ny][nx], nx, ny))
    
    return costs

ans = INF
costs_a = dijkstra(0, h-1, None, None)
costs_b = dijkstra(w-1, h-1, None, None)
costs_c = dijkstra(w-1, 0, None, None)
for py in range(h):
    for px in range(w):
        # log(px, py)
        ap = costs_a[py][px]
        bp = costs_b[py][px]
        cp = costs_c[py][px]
        p2 = grid[py][px] * 2

        # log(bp, ap, cp)

        ans = min(ans, ap + bp + cp - p2)

print(ans)
