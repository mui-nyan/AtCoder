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
def log(*args): print("DEBUG:", *args, file=sys.stderr)

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

def main():
    INF = 999999999999999999999999
    MOD = 10**9+7

    n = INT()
    A = INTS()
    B = INTS()

    if sum(A) != sum(B):
        print(-1)
        return
    
    for i in range(n):
        A[i] += i
        B[i] += i

    idxs = defaultdict(list)
    for i,a in enumerate(A):
        idxs[a].append(i)
    
    if sorted(A) != sorted(B):
        print(-1)
        return

    # log(idxs)
    
    ans = 0
    count = defaultdict(int)
    bit = Bit(n)
    for i in range(n):
        b = B[i]
        c = count[b]
        count[b] += 1
        ai = idxs[b][c]
        bit.add(ai+1, 1)
        ans += i+1 - bit.sum(ai+1)
        # log(i, ai, bit.sum(ai+1))
    print(ans)

main()
