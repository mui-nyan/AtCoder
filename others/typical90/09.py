from math import atan2, pi
from bisect import bisect_left
import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def theta(p):
    """点pの偏角を求めます。"""
    return atan2(p[1], p[0]) / pi * 180

def main():
    INF = 2**31-1

    n = INT()
    P = []
    for i in range(n):
        P.append(INTS())

    ans = -INF
    P2 = [0] * n
    for j in range(n):
        pj_x = P[j][0]
        pj_y = P[j][1]
        # 原点がPjになるように移動する
        for i in range(n):
            P2[i] = [P[i][0]-pj_x, P[i][1]-pj_y]

        # 各pの偏角を求めてソートする
        T = []
        for i in range(n):
            if i == j:
                continue
            p = P2[i]
            T.append(theta(p))
        T.sort()

        # log(T)

        for i in range(n):
            if i == j:
                continue

            ti = theta(P2[i])
            # 偏角がti+180°に近い点を探す
            # 0度と360の連続を考慮するので+180と-180を両方探す

            indexes = []
            x = bisect_left(T, ti)
            if x < n-1:
                indexes.append(x)
            if x > 0:
                indexes.append(x-1)
            x = bisect_left(T, ti-180)
            if x < n-1:
                indexes.append(x)
            if x > 0:
                indexes.append(x-1)

            for x in indexes:
                tk = T[x]
                d = min(abs(tk - ti), 360-abs(tk-ti))
                if d > ans:
                    ans = d

    print(ans)

main()
