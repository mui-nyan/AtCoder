import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

def s(generator, splitter, mapper):
    return [ mapper(s) for s in generator().split(splitter) ]

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

MOD = 10**9 + 7

n,m = get_nums_l()

nums = get_nums_l()
numt = get_nums_l()


ncount = [0] * (10**5 + 10)

dp = [ [1]*m for _ in range(n) ]

dp[0][0] = 1

for i, s in enumerate(nums):
    for j, t in enumerate(numt):
        if(s == t):
            pass