import math
from functools import reduce
from collections import deque, Counter
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

    S = input()

    if len(S) == 1:
        print("Yes" if S=="8" else "No")
        exit()
    
    if len(S) == 2:
        S = "".join(list(sorted(S)))
        print("Yes" if S in ("16", "24", "23", "48", "56", "46", "27", "88", "69") else "No")
        exit()

    C = Counter(S)
    # log(C)

    for eight in range(104, 1001, 8):
        eight_s = str(eight)
        if "0" in eight_s:
            continue
        C2 = Counter(eight_s)

        ng = False
        for k,v in C2.items():
            if C[k] >= v:
                pass
            else:
                ng = True
        if not ng:
            print("Yes")
            exit()
    print("No")

main()
