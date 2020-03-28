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

n,x,y = get_nums_l()

x,y = (min(x,y), max(x,y))

by_cost = [0] * (n+1)

for i in range(1, n):
    for j in range(i+1, n+1):
        c = j-i
        c = min(c, abs(i-x) + 1 + abs(j-y))
        by_cost[c] += 1

for i in range(1, n):
    print(by_cost[i])
