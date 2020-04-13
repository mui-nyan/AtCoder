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

n = int(input())
s = input()

ruisekiR = [0] * (n+1)
ruisekiG = [0] * (n+1)
ruisekiB = [0] * (n+1)

for i,c in enumerate(s):
    ruisekiR[i+1] = ruisekiR[i] + ( 1 if c == "R" else 0)
    ruisekiG[i+1] = ruisekiG[i] + ( 1 if c == "G" else 0)
    ruisekiB[i+1] = ruisekiB[i] + ( 1 if c == "B" else 0)

# log(ruisekiR)
# log(ruisekiG)
# log(ruisekiB)

ans = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        if s[i] == s[j]:
            continue
        c = "R"
        if "R" in (s[i], s[j]):
            c = "G"
            if "G" in (s[i], s[j]):
                c = "B"

        # log(s[i], s[j], c)

        if c == "R":
            ans += (ruisekiR[n] - ruisekiR[j])
        if c == "G":
            ans += (ruisekiG[n] - ruisekiG[j])
        if c == "B":
            ans += (ruisekiB[n] - ruisekiB[j])

        if j+(j-i)<n and s[j+(j-i)] == c:
            ans -= 1

print(ans)
