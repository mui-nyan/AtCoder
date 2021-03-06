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

n,m,x = get_nums_l()

books = [ get_nums_l() for _ in range(n)]

ans = INF

for bits in range(2 ** n):
    skills = [0] * (m)
    cost = 0
    for i in range(n):
        if 2**i & bits != 0:
            cost += books[i][0]
            for j in range(m):
                skills[j] += books[i][j+1]
    if min(skills) >= x:
        ans = min(ans, cost)

print(-1 if ans==INF else ans)
