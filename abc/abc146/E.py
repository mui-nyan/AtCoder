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

n,k,*aaa = get_all_int()
# log(aaa)
ruiseki = [0] * (n+1)
for i,a in enumerate(aaa):
    ruiseki[i+1] = (ruiseki[i] + a - 1) % k

count = {}
ans = 0
for right in range(len(ruiseki)):
    x = ruiseki[right]
    # log(x, count.get(x, 0), count)
    count[x] = count.get(x, 0) + 1

    if right >= k:
        y = ruiseki[right-k]
        count[y] -= 1

    ans += count.get(x, 0) - 1

print(ans)
