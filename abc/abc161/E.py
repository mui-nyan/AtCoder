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

n,k,c = get_nums_l()
s = input()

ox = [ c=="o" for c in s ]
work = [False] * (n)
count = 0
prev = -99999999999999
for i,o in enumerate(ox):
    if o:
        if i-prev > c:
            work[i] = True
            prev = i
            count += 1
            if count == k:
                break

# log("ox", ox)
# log("work", work)

kouho = None
last_work = 9999999999999
ans = []
for i in range(n-1, -1, -1):
    if work[i]:
        if kouho == None:
            # log(i, "req")
            ans.append(i+1)
            last_work = i
        else:
            # log(i, "change")
            last_work = kouho
            kouho = None

    if not kouho and ox[i] and last_work-i>c:
        # log(i, "kouho")
        kouho = i

print("\n".join(map(str, sorted(ans))))
