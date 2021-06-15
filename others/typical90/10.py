import math
from functools import reduce
from collections import deque, defaultdict, Counter
import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def GET(*types):
    strs = input().split()
    return [ t(s) for s,t in zip(strs, types)]
def get_nums_l():  return [ int(s) for s in input().split(" ")]
def get_all_int(): return map(int, open(0).read().split())
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

class CumulativeSum():
    def __init__(self, array, key=lambda a: a, operation=lambda a,b: a+b):
        n = len(array)
        self.array = [0] * (n+1)
        for i,a in enumerate(array):
            self.array[i+1] = operation(self.array[i],key(a))

    def get(self, l, r):
        """
        指定した区間の合計を計算します。
        区間は、元の配列に対する半開区間になります。
        [l:r)
        """
        return self.array[r] - self.array[l]

def main():
    

    n = INT()
    P = [ [0] * (n) for _ in range(2) ]

    for i in range(n):
        c,p = INTS()
        c -= 1
        P[c][i] = p

    ruiseki1 = CumulativeSum(P[0])
    ruiseki2 = CumulativeSum(P[1])

    q = INT()
    for i in range(q):
        l,r = INTS()
        l -= 1
        print(ruiseki1.get(l,r), ruiseki2.get(l,r))

main()
