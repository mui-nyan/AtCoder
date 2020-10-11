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

def neighbors2(x, y):
    yield(x + 1, y)
    yield(x, y + 1)

def main():
    INF = 999999999999999999999999
    MOD = 10**9+7

    h,w = get_nums_l()

    grid = []
    grid.append("#" * (w+2))
    for _ in range(h):
        grid.append("#" + input() + "#")
    grid.append("#" * (w+2))

    ans = 0

    for y in range(h+2):
        for x in range(w+2):
            if grid[y][x] == ".":
                for x2, y2 in neighbors2(x, y):
                    if grid[y2][x2] == ".":
                        ans += 1

    print(ans)


main()
