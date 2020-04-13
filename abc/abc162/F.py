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

n = int(input())
A = get_nums_l()

# スキップできる回数
p = 1 if n%2==0 else 2
# log(p)

# dp[i][j][k] i==1なら次取れる スキップ回数をj回残してk個目まで見たときの最大和
dp = [ [ [0]*(n+1) for _ in range(p+1) ] for _ in range(2) ]

dp[0][0][0] = -999999999999999999
dp[0][1][0] = -999999999999999999
dp[1][0][0] = -999999999999999999
if p == 2:
    dp[0][2][0] = -999999999999999999
    dp[1][1][0] = -999999999999999999

# log(dp)

for k in range(n):
    dp[0][0][k+1] = dp[1][0][k] + A[k]
    dp[0][1][k+1] = dp[1][1][k] + A[k]
    dp[1][0][k+1] = max(dp[1][1][k], dp[0][0][k])
    dp[1][1][k+1] = dp[0][1][k]

    if p == 2:
        dp[0][2][k+1] = dp[1][2][k] + A[k]
        dp[1][2][k+1] = dp[0][2][k]
        #dp[1][0][k+1] = max(dp[1][0][k+1], dp[1][1][k])
        dp[1][1][k+1] = max(dp[1][1][k+1], dp[1][2][k])

# for a in dp:
#     for b in a:
#         log(b)


ans = [dp[0][0][n], dp[0][1][n], dp[1][0][n], dp[1][1][n]]
if p == 2:
    # ans.append(dp[0][2][n])
    ans.append(dp[1][2][n])
print(max(ans))

