import math
from functools import reduce
from collections import deque, defaultdict
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
Q = [ s.split() for s in map(lambda s: s.strip(), sys.stdin.readlines()) ]

data = deque()

for q in Q:
    if q[0] == "1":
        data.append([q[1], int(q[2])])

    elif q[0] == "2":
        d = int(q[1])
        deleted = 0
        p = None

        d_char = defaultdict(int)

        while data and deleted + data[0][1] <= d:
            p = data.popleft()
            deleted += p[1]
            d_char[p[0]] += p[1]

        if data:
            p = data.popleft()
            dd = (d - deleted)
            data.appendleft([p[0], p[1] - dd])
            d_char[p[0]] += dd
        
        print(sum(map(lambda x: x**2, d_char.values())))

    # log(data)
