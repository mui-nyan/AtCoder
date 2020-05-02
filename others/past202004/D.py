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

def two():
    for a in "abcdefghijklmnopqrstuvwxyz.":
        for b in "abcdefghijklmnopqrstuvwxyz.":
            yield a+b

def three():
    for a in "abcdefghijklmnopqrstuvwxyz.":
        for b in "abcdefghijklmnopqrstuvwxyz.":
            for c in "abcdefghijklmnopqrstuvwxyz.":
                yield a+b+c

def match(s, t):
    len_s = len(s)
    len_t = len(t)

    for left in range(len_s - len_t + 1):
        for i in range(len_t):
            # log(s[left+i], t[left+i])
            if t[i]!="." and s[left+i] != t[i]:
                break
        else:
            return True

s = input()
len_s = len(s)

ans = 0

# 1文字
for t in "abcdefghijklmnopqrstuvwxyz.":
    if t == ".":
        ans += 1
    elif t in s:
        ans += 1

# log("end one.", ans)

# 2文字
if len_s >= 2:
    for t in two():
        # log(t)
        if match(s, t):
            ans += 1

# log("end two.", ans)

# 3文字
if len_s >= 3:
    for t in three():
        if match(s, t):
            ans += 1

# log("end three.", ans)

print(ans)
