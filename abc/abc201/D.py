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
    for i in range(h):
        grid.append(input())
    
    dp = [ [0] * w for _ in range(h) ]

    def get(x, y):
        parity = (x+y) % 2
        white = parity == 1
        # log(x,y,white)
        if white:
            return 1 if grid[y][x] == "+" else -1
        else:
            return 1 if grid[y][x] == "-" else -1
    
    
    for y in reversed(range(h)):
        for x in reversed(range(w)):
            if y == h-1 and x == w-1:
                continue
            parity = (x+y) % 2
            white = parity == 1
            
            vals = []
            if x < w-1:
                vals.append(dp[y][x+1] + get(x+1,y))
            if y < h-1:
                vals.append(dp[y+1][x] + get(x,y+1))

            # log(x,y,vals)
            if not white:
                dp[y][x] = max(vals)
            else:
                dp[y][x] = min(vals)
    
    v = dp[0][0]

    for d in dp:
        log(d)

    if v > 0:
        print("Takahashi")
    elif v < 0:
        print("Aoki")
    else:
        print("Draw")



main()
