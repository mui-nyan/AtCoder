import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)
import heapq

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

n,m = get_nums_l()
aaa = get_nums_l()
h = []

for a in aaa:
    heapq.heappush(h, -1 * a)

for _ in range(m):
    a = heapq.heappop(h)
    heapq.heappush(h, math.ceil(a/2))

print(-1 * sum(h))