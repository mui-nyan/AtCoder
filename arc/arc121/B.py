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
    red = 0
    green = 0
    blue = 0
    R = []
    G = []
    B = []
    for i in range(n*2):
        a,c = GET(int, str)
        if c == "R":
            red += 1
            R.append(a)
        elif c == "G":
            green += 1
            G.append(a)
        else:
            blue += 1
            B.append(a)
    
    if red%2==0 and green%2==0 and blue%2==0:
        # 全部同じ色ペアにできれば不満は0
        print(0)
        return
    
    ans = INF

    # 偶数こペア=Z , のこりふたつをX,Yとする
    if red%2==0:
        Z = R
        X = G
        Y = B
    elif green%2==0:
        Z = G
        X = R
        Y = B
    else:
        Z = B
        X = R
        Y = G
    
    X.sort()
    Y.sort()
    Z.sort()
    
    # Aパターン 偶数ペアは0点で確定してのこりでマッチング
    xi = 0
    yi = 0
    xn = len(X)
    yn = len(Y)

    while xi<xn and yi<yn:
        x = X[xi]
        y = Y[yi]
        c = abs(x - y)
        if ans > c:
            ans = c
        
        if x > y:
            yi += 1
        elif x < y:
            xi += 1
        else:
            xi += 1
            yi += 1
    
    # Bパターン 偶数ペアから2つをマッチする
    if len(Z) > 0:
        X = list(map(lambda x : (x, "X"), X))
        Y = list(map(lambda x : (x, "Y"), Y))
        XY = X+Y
        XY.sort()
        xi = 0
        xn = len(XY)
        zi = 0
        zn = len(Z)

        dp = {}
        dp["X"] = defaultdict(lambda:INF)
        dp["Y"] = defaultdict(lambda:INF)
        while xi<xn and zi<zn:
            x,col = XY[xi]
            z = Z[zi]
            c = abs(x - z)
            dp[col][zi] = min(dp[col][zi], c)
            
            if x > z:
                zi += 1
            elif x < z:
                xi += 1
            else:
                xi += 1
                zi += 1
        
        # log("dp", dp)
        
        Xcosts = [(cost,zi) for zi,cost in dp["X"].items()]
        Ycosts = [(cost,zi) for zi,cost in dp["Y"].items()]
        Xcosts.sort()
        Ycosts.sort()

        # log("Xcosts", Xcosts)
        # log("Ycosts", Ycosts)

        if Xcosts[0][1] != Ycosts[0][1]:
            ans = min(ans, Xcosts[0][0] + Ycosts[0][0])
        else:
            cos = Xcosts[0][0]
            coss = [
                Xcosts[1][0],
                Ycosts[1][0]
            ]
            log("coss", coss)
            cos += min(coss)
            ans = min(ans, cos)

    
    
    print(ans)





main()
