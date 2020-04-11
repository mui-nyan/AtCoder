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

n = int(input())
edges = list(
    map(lambda s: 
        tuple(map(int,s.strip().split())), sys.stdin.readlines()
    )
)

children = [ [] for _ in range(n+1)]
for e in edges:
    children[e[0]].append(e[1])
    children[e[1]].append(e[0])

colors = [{} for _ in range(n+1)]

check = [False for _ in range(n+1)]

que = deque()
que.append((1, 0))

def solve(i, x):
    # log(i, x)
    check[i] = True

    color = 0
    for node in children[i]:
        if check[node]:
            continue

        color += 1
        if color == x:
            color += 1

        # log(i, node, color)
        colors[i][node] = color
        colors[node][i] = color
        que.append((node, color))

while que:
    e = que.popleft()
    solve(e[0], e[1])

maxColor = 0

for i in range(1, n+1):
    c = colors[i]
    maxColor = max(maxColor, max(c.values()))

print(maxColor)

for e in edges:
    print(colors[e[0]][e[1]])
