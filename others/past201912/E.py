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

n,q = get_nums_l()
S = [ input() for _ in range(q)]

follows = [ [False] * (n+1) for _ in range(n+1)]

for s in S:
    A = list(map(int, s.split()))

    if A[0] == 1:
        # フォローする
        follows[A[1]][A[2]] = True
    elif A[0] == 2:
        # フォロバ
        for i in range(1, n+1):
            if follows[i][A[1]]:
                follows[A[1]][i] = True
    else:
        # フォロイーのフォロイーを全部フォロー
        followees = []
        for i in range(1, n+1):
            if follows[A[1]][i]:
                followees.append(i)
        
        for followee in followees:
            for i in range(1, n+1):
                if follows[followee][i]:
                    follows[A[1]][i] = True

for i in range(1, n+1):
    follows[i][i] = False

for i in range(1, n+1):
    print("".join(map(lambda b: "Y" if b else "N", rangeI(follows[i], 1,n+1))))
