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

s = input()
n = len(s)
ans = 0

dp1 = [999999999999999999] * (n+1)
dp2 = [999999999999999999] * (n+1)

# dp1[i] = 上からi桁目までピッタリ払った最小コスト
# dp2[i] = 上からi桁目を1多く払った最小コスト

dp1[0] = 0
dp2[0] = 1

for i,c in enumerate(s):
    a = int(c)

    dp1[i+1] = min(dp1[i]+a, dp2[i]+a+1)
    dp2[i+1] = min(dp1[i]+a+1, dp2[i]+(10-a-1), dp2[i]+a+2)

print(min(dp1[n], dp2[n]+1))
