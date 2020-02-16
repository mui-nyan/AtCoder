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

n,  = get_nums_l()
abc = [ [int(t) for t in s.split()] for s in sys.stdin.readlines() ]

dp_a = [0] * (n)
dp_b = [0] * (n)
dp_c = [0] * (n)

dp_a[0] = abc[0][0]
dp_b[0] = abc[0][1]
dp_c[0] = abc[0][2]

for i in range(1,n):
    dp_a[i] = max(dp_b[i-1], dp_c[i-1]) + abc[i][0]
    dp_b[i] = max(dp_a[i-1], dp_c[i-1]) + abc[i][1]
    dp_c[i] = max(dp_a[i-1], dp_b[i-1]) + abc[i][2]

print(max(dp_a[n-1], dp_b[n-1], dp_c[n-1]))