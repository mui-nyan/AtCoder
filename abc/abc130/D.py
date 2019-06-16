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
nums = get_nums_l()

tail = 0
summ = 0
pattern = 0

for head in range(n):
    summ += nums[head]

    while summ >= k:
        pattern += head - tail
        summ -= nums[tail]
        tail += 1

nokori = n - tail
pattern += nokori*(nokori+1)//2

all_pattern = n*(n+1)//2

print(all_pattern - pattern)