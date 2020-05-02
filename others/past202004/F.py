import math
from functools import reduce
from collections import deque
import heapq
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
tasks = [ tuple(map(int, s.split())) for s in map(lambda s: s.strip(), sys.stdin.readlines()) ]
tasks.sort()

# log(tasks)

que = []

day = 1
i = 0
ans = [0]
for day in range(1, n+1):
    while i < n and tasks[i][0] == day:
        heapq.heappush(que, -1 * tasks[i][1]) 
        i += 1
    ans.append(ans[-1] + (-1 * heapq.heappop(que)))

for i in range(1, n+1):
    print(ans[i])
