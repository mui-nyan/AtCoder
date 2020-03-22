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
len_s = len(s)
kaibun = s == s[::-1]
left = s[:(len_s-1)//2] == s[:(len_s-1)//2][::-1]
right = s[(len(s)+3)//2-1:] == s[(len(s)+3)//2-1:][::-1]
log(kaibun, left, right)
print("Yes" if kaibun and left and right else "No")