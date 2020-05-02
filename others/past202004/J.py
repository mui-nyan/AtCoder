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

s = input()

last_open = None
while True:
    for i,c in enumerate(s):
        if c == "(":
            last_open = i
        if c == ")":
            s = s[:last_open] + s[last_open+1:i] + s[i-1:last_open:-1] + s[i+1:]
            break
    # log(s)
    if last_open is None:
        print(s)
        exit()
    last_open = None
