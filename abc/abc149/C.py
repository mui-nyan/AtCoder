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

sosuu = [None] * 200005

for i in range(2, len(sosuu)):
    if sosuu[i] is None:
        # log(i, "is prime.")
        sosuu[i] = True
        for j in range(i*2, len(sosuu), i):
            sosuu[j] = False

x = int(input())

while sosuu[x] != True:
    # log(x)
    x += 1

print(x)