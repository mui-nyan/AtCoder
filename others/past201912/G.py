import math
from functools import reduce
from collections import deque
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

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

INF = 999999999999999999999999
MOD = 10**9+7

n = int(input())
scores = [ list(map(int, input().split())) for _ in range(n-1) ]

def dfs(P):
    if len(P) == n:
        solve(P)
    else:
        for i in range(3):
            dfs(P + [i])

ans = -INF

def solve(P):
    global ans

    G = [ [] for _ in range(3)]
    for i,p in enumerate(P):
        G[p].append(i)
    
    score = 0

    for H in G:
        len_h = len(H)
        for i in range(len_h - 1):
            for j in range(i+1, len_h):
                # log(i, j)
                a = H[i]
                b = H[j]
                a,b = (min(a,b), max(a,b))
                b -= (a+1)
                score += scores[a][b]

    ans = max(ans, score)

dfs([])

print(ans)
