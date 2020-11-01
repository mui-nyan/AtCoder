import math
from functools import reduce
from collections import deque
from bisect import bisect_left
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

    n,m = get_nums_l()
    H = get_nums_l()
    H.sort()
    W = get_nums_l()
    W.sort()

    # 左優先でペアを作る
    left = []
    for i in range(0,n-1,2):
        left.append(abs(H[i] - H[i+1]))

    # 右優先でペアを作る
    right = []
    for i in range(1,n-1,2):
        right.append(abs(H[i] - H[i+1]))

    ruisekiL = [0] * (len(left)+1)
    ruisekiR = [0] * (len(right)+1)
    for i in range(len(left)):
        ruisekiL[i+1] = (ruisekiL[i] + left[i])
    for i in range(len(right)):
        ruisekiR[-1 - i - 1] = ruisekiR[-1 - i] + right[-1 - i]
    
    # log(ruisekiL)
    # log(ruisekiR)

    ans = INF
    for w in W:
        i = bisect_left(H, w)
        j = i // 2
        # log(w, i)

        cost = ruisekiL[j] + ruisekiR[j] + abs(w - H[i - i%2])
        ans = min(ans, cost)
    
    print(ans)




main()
