import math
from functools import reduce
from collections import deque
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

k,n = get_nums_l()
aaa = get_nums_l()
for i in range(n):
    aaa.append(aaa[i] + k)

ans = 99999999999999999999
for i in range(n):
    c = aaa[i+n-1] - aaa[i]
    ans = min(ans, c)

print(ans)