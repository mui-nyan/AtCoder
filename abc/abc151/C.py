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

n,m = get_nums_l()
qqq = list(map(lambda s: s.strip().split(), sys.stdin.readlines()))
qqq = list(map(lambda q: (int(q[0]), q[1]), qqq))
qqq.sort(key=lambda q: q[0])

prev = None
wa = 0
accepted = set()
ans_wa = 0
for q in qqq:
    no = q[0]
    ju = q[1]
    if no != prev:
        wa = 0
    if ju == "AC":
        if no not in accepted:
            accepted.add(no)
            ans_wa += wa
    if ju == "WA":
        wa += 1
    prev = no

print(len(accepted), ans_wa)