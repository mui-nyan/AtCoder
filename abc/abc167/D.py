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

n,k = get_nums_l()
A = [-1] + get_nums_l()

# log(A)

now = A[1]
count = 1
history = {1}

while now not in history:
    # log(now, count)
    count += 1
    history.add(now)
    now = A[now]

loop_start = now
init_len = 0
now = 1
while now != loop_start:
    now = A[now]
    init_len += 1

# log("init_len", init_len)
# log("count", count)

if k <= 2*n:
    now = 1
    for i in range(k):
        now = A[now]
else:
    l = (k - init_len) % (count-init_len)

    now = loop_start
    for i in range(l):
        now = A[now]

print(now)