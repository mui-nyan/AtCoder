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

    tmp = input().split()
    n = int(tmp[0])
    S = tmp[1]

    A = [0]*(n+1)
    G = [0]*(n+1)
    C = [0]*(n+1)
    T = [0]*(n+1)

    for i,c in enumerate(S):
        A[i+1] = A[i] + (1 if c=="A" else 0)
        G[i+1] = G[i] + (1 if c=="G" else 0)
        C[i+1] = C[i] + (1 if c=="C" else 0)
        T[i+1] = T[i] + (1 if c=="T" else 0)
    
    # log(A,G,C,T)

    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            a = A[j+1] - A[i]
            g = G[j+1] - G[i]
            c = C[j+1] - C[i]
            t = T[j+1] - T[i]

            if a==t and g==c:
                ans += 1
    
    print(ans)



main()
