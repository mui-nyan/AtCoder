import math
from functools import reduce
from collections import deque, defaultdict, Counter
import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def GET(*types):
    strs = input().split()
    return [ t(s) for s,t in zip(strs, types)]
def get_nums_l():  return [ int(s) for s in input().split(" ")]
def get_all_int(): return map(int, open(0).read().split())
def log(*args): print("DEBUG:", *args, file=sys.stderr)

def main():
    INF = 999999999999999999999999
    MOD = 10**9+7

    n = INT()
    P = []
    X = []
    Y = []
    for _ in range(n):
        x,y = INTS()
        P.append((x,y))
        X.append(x)
        Y.append(y)


    # if n < 2500:
    #     m = 0
    #     m2 = 0
    #     for a in range(n-1):
    #         for b in range(a+1, n):
    #             dis = max(abs(P[a][0]-P[b][0]), abs(P[a][1]-P[b][1]))
    #             if dis > m:
    #                 m2 = m
    #                 m = dis
    #             elif dis > m2:
    #                 m2 = dis
        
    #     print(m2)
    #     return
    
    X.sort()
    Y.sort()

    d = []
    d.append(abs(X[0] - X[-1]))
    d.append(abs(X[1] - X[-1]))
    d.append(abs(X[0] - X[-2]))
    d.append(abs(Y[0] - Y[-1]))
    d.append(abs(Y[1] - Y[-1]))
    d.append(abs(Y[0] - Y[-2]))

    d.sort()

    x0i = [ i for i,p in enumerate(P) if p[0]==X[0] ]
    y0i = [ i for i,p in enumerate(P) if p[1]==Y[0] ]
    x1i = [ i for i,p in enumerate(P) if p[0]==X[-1] ]
    y1i = [ i for i,p in enumerate(P) if p[1]==Y[-1] ]

    xxx = set([*x0i, *y0i, *x1i, *y1i])
    if len(xxx) == 2:
        print(d[-3])
    else:
        print(d[-2])

main()
