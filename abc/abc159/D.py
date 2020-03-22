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
aaa = get_nums_l()

counts = [0] * (n+1)
patterns = [0] * (n+1)

for a in aaa:
    counts[a] += 1

for i in range(n+1):
    m = counts[i]
    patterns[i] = m * (m-1) // 2

all_patterns = sum(patterns)

for a in aaa:
    ans = all_patterns - patterns[a]
    ans += (counts[a]-1) * (counts[a]-2) // 2
    print(ans)
