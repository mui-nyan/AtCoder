import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

def s(generator, splitter, mapper):
    return [ mapper(s) for s in generator().split(splitter) ]

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

n,k = get_nums_l()

edges = []

edges.append((1, 2))

right = min(k, n-2) 
for i in range(right):
    edges.append((2, i+3))

kumi = right + (right*(right-1)//2)

if(kumi < k):
    print(-1)
    exit()

over = kumi - k
count = 0
if over > 0:
    for i in range(right):
        for j in range(i+1, right):
            count += 1
            edges.append((i+3, j+3))
            if count >= over:
                break
        if count >= over:
            break

amari = n - (right+2)

for i in range(amari):
    for j in range(right+2):
        edges.append((j+1, i+right+3))

for i in range(amari-1):
    for j in range(i+1, amari):
        edges.append((i+right+3, j+right+3))

print(len(edges))
for e in edges:
    print(" ".join(map(str,(e))))