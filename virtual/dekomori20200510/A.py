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
s = input()

def solve(m):
    # dp[i][j] = 前半i文字目,後半j文字目までを考慮した場合の、そこまでの最小コスト
    dp = [ [INF] * (n-m+1) for _ in range(m+1)]
    dp[0][0] = 0
    for i in range(m+1):
        for j in range(n-m+1):
            if i<m:
                dp[i+1][j]   = min(dp[i+1][j], dp[i][j] + 1)
            if j<n-m:
                dp[i][j+1]   = min(dp[i][j+1], dp[i][j] + 1)
            if i<m and j<n-m:
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + (0 if s[i]==s[m+j] else 2))
    
    # for row in dp:
    #     log("", row)
    return dp[m][n-m]

ans = n

for m in range(1, n):
    # log("m:", m)
    ans = min(ans, solve(m))

print(ans)
