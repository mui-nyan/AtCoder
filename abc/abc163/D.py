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

MOD = 10**9+7
n,k = get_all_int()

ans = 0

for m in range(k, n+2):
    # m個選ぶ最小値
    a = (m-1) * m // 2

    # m個選ぶ最大値
    b = (n+(n-m+1)) * m // 2
    
    ans += b-a+1

print(ans % MOD)
