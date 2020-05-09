import math
from functools import reduce
from collections import deque, defaultdict
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

n,*A = get_all_int()

D = defaultdict(int)

for a in A:
    D[a] += 1

if len(D.keys()) == n:
    print("Correct")
    exit()
else:
    x = -1
    y = -1

    for a in range(1, n+1):
        if D[a] == 0:
            x = a
        elif D[a] == 2:
            y = a

print(y, x)
