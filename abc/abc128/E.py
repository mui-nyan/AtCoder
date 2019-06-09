import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

def s(generator, splitter, mapper):
    return [ mapper(s) for s in generator().split(splitter) ]

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return map(int,input().split(" ") )

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return map(int, [ input() for _ in range(n)])


n,q = get_nums_l()
lines = sys.stdin.readlines()
d = deque()
event = []
for line in lines[:n]:
    s,t,x = map(int, line.split(" "))
    if t-x > 0:
        event.append((s-x, True, x))
        event.append((t-x, False, x))
event.sort(key=lambda e:e[1])
event.sort(key=lambda e:e[0])

next = 0
# PythonのsetはTreeSetではないのでmin(s)がO(n)らしい
s = set()
i_max = len(event)
for line in lines[n:]:
    di = int(line)
    while((next < i_max) and (event[next][0] <= di) ):
        e = event[next]
        if(e[1]):
            s.add(e[2])
        else:
            s.remove(e[2])
        next += 1
    
    if(s):
        print(min(s))
    else:
        print(-1)