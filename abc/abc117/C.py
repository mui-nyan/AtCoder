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

n,m = get_nums_l()
nums = get_nums_l()

nums.sort()
kaisa = [0] * (m-1)

for i in range(m-1):
    kaisa[i] = nums[i+1] - nums[i]

kaisa.sort(reverse=True)

print(sum(kaisa[n-1:]))