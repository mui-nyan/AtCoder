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

n,a = get_nums_l()
xxx = get_nums_l()

valMax = 2505

# dp[i][j][k] = i番目まで処理して、選択した個数がjで、合計がkのとき、平均aにできるパターン数
dp = [ [ [0]*valMax for __ in range(n+1) ] for _ in range(n+1) ]

for j in range(n+1):
    for k in range(valMax):
        dp[n][j][k] = 1 if j !=0 and k == j*a else 0

for i in range(n-1, -1, -1):
    for j in range(i+1):
        for k in range(valMax):
            no_pic = dp[i+1][j][k]
            pic = dp[i+1][j+1][k + xxx[i]] if k+xxx[i] < valMax else 0
            dp[i][j][k] = no_pic + pic
            # if no_pic+pic > 0:
                # log((i,j,k), no_pic, pic, no_pic+pic)

print(dp[0][0][0])