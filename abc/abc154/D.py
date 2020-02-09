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

n,k,*ppp = get_all_int()

sum_ = sum(ppp[:k])
maxs = sum_
maxt = 0

tail = 0
while tail+k < len(ppp):
    sum_ -= ppp[tail]
    sum_ += ppp[tail+k]
    tail += 1
    if sum_ > maxs:
        maxs = sum_
        maxt = tail

ans = 0
for p in ppp[maxt:maxt+k]:
    ans += (p+1)/2

print(ans)