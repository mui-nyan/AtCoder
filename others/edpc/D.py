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

n,w = get_nums_l()
ppp = list(map(lambda s: tuple(map(int,s.strip().split())), sys.stdin.readlines()))

# dp[i] = 重さiで得られる最大の価値
dp = [0] * (w+1)

for p in ppp:
    we = p[0]
    va = p[1]
    for i in reversed(range(len(dp))):
        if i+we > w:
            continue
        ne = i+we
        dp[ne] = max(dp[ne], dp[i]+va)

# log(dp)

print(max(dp))