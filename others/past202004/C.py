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
grid = [ list(input()) for _ in range(n) ]

# 下から二段目から順に上にいく
for y in range(n-2, -1, -1):
    for x in range(0, 2*n-1):
        if grid[y][x] == ".":
            continue
        if "X" in grid[y+1][x-1:x+2]:
            grid[y][x] = "X"

for row in grid:
    print("".join(row))
