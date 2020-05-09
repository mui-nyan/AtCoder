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

n = int(input())
C = [-1] + get_nums_l()
q = int(input())
S = [ input() for _ in range(q)]

# 全商品の在庫min
m_all = min(C[1:])
m_set = min([ c for c in C[1::2]])

# 全種類販売した回数
c_all = 0
c_set = 0

ans = 0

for s in S:
    A = list(map(int, s.split()))

    # log(A)
    # log(C)

    if A[0] == 1:
        # 単品
        x = A[1]
        a = A[2]
        if C[x] >= a + c_all + (c_set if x%2==1 else 0):
            C[x] -= a
            ans += a
            m_all = min(m_all, C[x])
            if x % 2 == 1:
                m_set = min(m_set, C[x])
    elif A[0] == 2:
        # セット
        a = A[1]
        if m_set >= a + c_set + c_all:
            c_set += a
            ans += a * ((n+1)//2)
    else:
        # 全部
        a = A[1]
        # log(m_all, m_set, c_all, c_set)
        if m_all >= a + c_all and m_set >= a + c_all + c_set:
            c_all += a
            ans += n * a
    
    # log(ans)

print(ans)
