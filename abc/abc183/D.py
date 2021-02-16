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

    n,w = get_nums_l()
    S = []
    T = []
    P = []
    for i in range(n):
        s,t,p = get_nums_l()
        S.append(s)
        T.append(t)
        P.append(p)
    
    imos = [0] * 200001

    for s,t,p in zip(S,T,P):
        imos[s] += p
        imos[t] -= p

    now = 0
    for i,p in enumerate(imos):
        now += p
        if now > w:
            print("No")
            return
    
    print("Yes")


main()
