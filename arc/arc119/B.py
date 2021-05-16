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
    s = input()
    t = input()

    s,t = (max(s,t), min(s,t))
    # log(s,t)

    s_zeros = s.count("0")
    t_zeros = t.count("0")

    if s_zeros != t_zeros:
        print("-1")
        return
    
    if s == t:
        print("0")
        return
    
    s_zero_i = [ i for i,c in enumerate(s) if c=="0" ]
    t_zero_i = [ i for i,c in enumerate(t) if c=="0" ]

    ans = 0
    for i in range(len(s_zero_i)):
        if s_zero_i[i] != t_zero_i[i]:
            ans += 1
    
    print(ans)


main()
