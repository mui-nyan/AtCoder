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

class cumulative_sum():
    def __init__(self, array, key=lambda a: a):
        n = len(array)
        self.array = [0] * (n+1)
        for i,a in enumerate(array):
            self.array[i+1] = self.array[i] + key(a)

    def get(self, l, r):
        """指定した区間(半開区間)の合計を計算します。"""
        return self.array[r] - self.array[l]

def main():
    tmp = input().split()
    n = int(tmp[0])
    S = tmp[1]

    A = cumulative_sum(S, key=lambda c: 1 if c=="A" else 0)
    G = cumulative_sum(S, key=lambda c: 1 if c=="G" else 0)
    C = cumulative_sum(S, key=lambda c: 1 if c=="C" else 0)
    T = cumulative_sum(S, key=lambda c: 1 if c=="T" else 0)

    ans = 0
    for i in range(n):
        for j in range(i+1, n+1):
            a = A.get(i, j)
            g = G.get(i, j)
            c = C.get(i, j)
            t = T.get(i, j)

            if a==t and g==c:
                ans += 1
    
    print(ans)

main()
