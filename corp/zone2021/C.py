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

    n = int(input())

    params = []

    for i in range(n):
        a,b,c,d,e = get_nums_l()
        params.append((a,b,c,d,e))
    
    left = 0
    right = 10**9 + 1

    while right - left > 1:
        x = (right + left) // 2
        conv = set()

        # 32通りに圧縮して重複排除
        for i in range(n):
            conv.add(tuple(int(params[i][p]>=x) for p in range(5)))
        
        conv = list(conv)


        # log(x, conv)

        while len(conv) < 3:
            conv.append((0,0,0,0,0))

        l = len(conv)

        ok = False
        for a in range(l):
            for b in range(a+1, l):
                for c in range(b+1, l):
                    for p in range(5):
                        if not conv[a][p] and not conv[b][p] and not conv[c][p]:
                            break
                    else:
                        ok = True
                        break
                else:
                    continue
                break
            else:
                continue
            break

        # log(x, conv, "OK" if ok else "NG")

        if ok:
            left = x
        else:
            right = x
    print(left)


main()
