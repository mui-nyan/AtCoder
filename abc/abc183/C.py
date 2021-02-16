import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

from itertools import permutations

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

    n,k = get_nums_l()

    T = []
    for i in range(n):
        t = get_nums_l()
        T.append(t)
    
    ans = 0

    nodes = list(range(1, n))
    for route in permutations(nodes, n-1):
        cost = 0
        now = 0
        for i in range(n-1):
            next = route[i]
            cost += T[now][next]
            now = next
        cost += T[now][0]
        # log("cost", cost)

        if cost == k:
            ans += 1

    print(ans)

main()
