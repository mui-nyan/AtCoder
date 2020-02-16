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

n = int(input())
sss = []
for _ in range(n):
    sss.append(input())

m = {}
for s in sss:
    if s in m:
        m[s] += 1
    else:
        m[s] = 1

items = m.items()
items = list(sorted(items, key=lambda i:i[0]))
items = list(sorted(items, key=lambda i: i[1], reverse=True))

max_ = items[0][1]
i = 0
while i<len(items) and items[i][1] == max_:
    print(items[i][0])
    i+=1
