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

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def rangeI(it, l, r):
    for i, e in enumerate(it):
        if l <= i < r:
            yield e
        elif l >= r:
            break

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

INF = 999999999999999999999999
MOD = 10**9+7

s = input()
n = len(s)

ans = n
for x in range(1, 2**n):
    times = []
    for i in range(n):
        if x & 2**i != 0:
            times.append(i)

    # log(x, times)

    check = [False] * (n)

    for time in times:
        for i,c in enumerate(s):
            if c == "o":
                check[(time+i) % n] = True
    
    ok = True
    for b in check:
        if not b:
            ok = False
            break
    if ok:
        ans = min(ans, len(times))

print(ans)