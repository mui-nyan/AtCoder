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
A = [-1] + get_nums_l()


ans = []

for i in range(1, n+1):
    x = i
    x = A[x]
    count = 1
    while x != i:
        x = A[x]
        count += 1
    
    ans.append(count)

print(" ".join(map(str,ans)))

