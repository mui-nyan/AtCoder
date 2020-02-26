import math
from functools import reduce
from collections import deque
import itertools
import sys
sys.setrecursionlimit(10**7)

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

n = int(input())
p = input()
q = input()

p_count = 1
q_count = 1

def kaijo(n):
    ret = 1
    for i in range(n):
        ret *= n
    return ret

for rrr in itertools.permutations(map(str,range(1,n+1))):
    s = " ".join(rrr)
    if s < p:
        p_count += 1
    if s < q:
        q_count += 1


print(abs(p_count - q_count))