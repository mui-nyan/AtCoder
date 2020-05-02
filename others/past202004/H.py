import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

def neighbors4(x, y):
  dxy = (0, 1, 0, -1, 0 )
  for i in range(4):
    yield(x + dxy[i], y + dxy[i+1])

def dijkstra(sx, sy):
    global n,m
    lens = [ [99999999999999]*m for _ in range(n) ]
    lens[sy][sx] = 0

    que = deque()
    que.append((sx, sy, 1))

    while que:
        x,y,score = que.popleft()

        for nx,ny in neighbors4(x,y):
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if lens[ny][nx] > score:
                lens[ny][nx] = score
                que.append((nx, ny, score+1))
    return lens

n,m = get_nums_l()
s_grid = list(map(lambda s: s.strip(), sys.stdin.readlines()))
n_grid = [ [-1]*m for _ in range(n) ]
s_pos = None
g_pos = None

for y in range(n):
    for x in range(m):
        if s_grid[y][x] == "S":
            n_grid[y][x] = 0
            s_pos = (y, x)
        elif s_grid[y][x] == "G":
            n_grid[y][x] = 0
            g_pos = (y, x)
        else:
            n_grid[y][x] = int(s_grid[y][x])

pos = [[] for _ in range(11)]
for y,row in enumerate(s_grid):
    for x,c in enumerate(row):
        if c == "S":
            pos[0].append([y, x])
        elif c == "G":
            pos[10].append([y, x])
        else:
            pos[int(c)].append([y, x])

dp = [None] * 11
for i,p in enumerate(pos):
    dp[i] = [9999999999999] * len(p)

dp[0][0] = 0

for now in range(10):
    for j1, p in enumerate(pos[now]):
        lens = dijkstra(p[1], p[0])
        for j2, q in enumerate(pos[now + 1]):
            dp[now+1][j2] = min(dp[now+1][j2], dp[now][j1] + lens[q[0]][q[1]])

# log(pos)
# log(dp)

print(dp[10][0] if dp[10][0] < 9999999999999 else -1)
