import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

def main():
    INF = 999999999999999999999999
    MOD = 10**9+7

    s = input()

    rev = False

    que = deque()

    for c in s:
        if c == "R":
            rev = not rev
        else:
            if rev:
                if not que or que[0] != c:
                    que.appendleft(c)
                else:
                    que.popleft()
            else:
                if not que or que[-1] != c:
                    que.append(c)
                else:
                    que.pop()

    t = "".join(que)
    if rev:
        t = t[::-1]
    print(t)

main()
