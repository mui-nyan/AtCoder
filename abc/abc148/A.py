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

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

a = int(input())
b = int(input())

for i in range(1,4):
    if i not in (a,b):
        print(i)