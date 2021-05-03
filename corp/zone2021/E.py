import math
from functools import reduce
from collections import deque
from heapq import heappop, heappush
import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

def main():
    INF = 999999999999999999999999
    MOD = 10**9+7

    h,w = get_nums_l()

    A = []
    B = []
    for i in range(h):
        A.append(get_nums_l())
    for i in range(h-1):
        B.append(get_nums_l())
    
    edges = [ [] for _ in range(w*h*2) ]
    for y,a in enumerate(A):
        for x,cost in enumerate(a):
            edges[y*w + x].append((y*w + x + 1, cost))
            edges[y*w + x + 1].append((y*w + x, cost))
    for y,b in enumerate(B):
        for x, cost in enumerate(b):
            edges[y*w + x].append(((y+1)*w + x, cost))
            edges[y*w + x].append((y*w+x + (w*h), 1))
            edges[y*w+x + (w*h)].append((y*w+x, 0))
            if y > 0:
                edges[y*w+x + (w*h)].append(((y-1)*w+x + (w*h), 1))
    for x in range(w):
            y = h-1
            edges[y*w + x].append((y*w+x + (w*h), 1))
            edges[y*w+x + (w*h)].append((y*w+x, 0))
            edges[y*w+x + (w*h)].append(((y-1)*w+x + (w*h), 1))
        

    # log(edges)

    costs = [INF] * (w*h*2)

    que = []

    heappush(que, (0,0))

    while que:
        c,xy = heappop(que)

        x = xy % w
        y = xy // w

        # log(c,x,y)

        if c > costs[xy]:
            continue
        costs[xy] = c

        # if x == w-1 and y == h-1:
        #     break

        for nxy,nc in edges[y*w + x]:
            nx = nxy % w
            ny = nxy // w
            if costs[nxy] > c+nc:
                # log(" ", c, nx, ny)
                costs[nxy] = c + nc
                heappush(que, (c+nc, nxy))

    # log(costs)
    print(costs[h*w-1])





main()
