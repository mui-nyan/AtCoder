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

x, y, a, b, c = get_nums_l()
ppp = get_nums_l()
qqq = get_nums_l()
rrr = get_nums_l()

ppp.sort(reverse=True)
qqq.sort(reverse=True)
rrr.sort(reverse=True)

xxx = ppp[:x] + qqq[:y]
xxx.sort()

ans = 0
for i in range(x+y):
    x = xxx[i]
    if i < len(rrr):
        x = max(x, rrr[i])
    ans += x

print(ans)
