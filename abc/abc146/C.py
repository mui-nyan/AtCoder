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

a,b,x = get_nums_l()

def d(n):
    ans = 0
    while n > 0:
        ans += 1
        n = n//10
    return ans

left = 0
right = 10**9 + 1

while left + 1 < right:
    center = (left+right)//2
    if a * center + b*d(center) <= x:
        left = center
    else:
        right = center

print(left)
