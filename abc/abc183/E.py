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

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

def main():
    INF = 999999999999999999999999
    MOD = 10**9+7

    h,w = get_nums_l()

    grid = []
    for y in range(h):
        grid.append(input())
    
    # dp[y][x] = マス(x,y)に到達する場合の数
    dp = [[0] * w for _ in range(h)]
    dp[0][0] = 1

    v_ruiseki = [0] * w
    naname_ruiseki = [0] * (w+h-1)
    for y in range(h):
        h_ruiseki = 0
        for x in range(w):
            if grid[y][x] == "#":
                h_ruiseki = 0
                v_ruiseki[x] = 0
                naname_ruiseki[y-x+1] = 0
                continue
            
            if y==0 and x==0:
                here = 1
            else:
                here = h_ruiseki + v_ruiseki[x] + naname_ruiseki[y-x+1]
                here = here%MOD
            dp[y][x] = here

            h_ruiseki =  (h_ruiseki + here) % MOD
            v_ruiseki[x] = (v_ruiseki[x] + here) % MOD
            naname_ruiseki[y - x + 1] = (naname_ruiseki[y - x + 1] + here) % MOD

    
    print(dp[-1][-1] % MOD)


main()
