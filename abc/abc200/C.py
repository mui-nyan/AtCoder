import math
from functools import reduce
from collections import deque,defaultdict
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

    n,*A = get_all_int()

    ans = 0
    mod200 = defaultdict(int)
    for a in A:
        x = a%200
        ans += mod200[x]
        mod200[x] += 1

    print(ans)

main()
