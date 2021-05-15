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

    s = input()

    o = s.count("o")
    x = s.count("x")
    q = s.count("?")

    os = []
    xs = []
    qs = []
    for i,c in enumerate(s):
        if c == "o":
            os.append(str(i))
        if c == "x":
            xs.append(str(i))
        if c == "?":
            qs.append(str(i))


    ans = 0
    for p in range(10000):
        sp = str(p).zfill(4)


        ok = True

        for c in sp:
            if not (c in os or c in qs):
                ok = False
        
        for c in os:
            if c not in sp:
                ok = False
        
        if ok:
            ans += 1
    

    print(ans)


main()
