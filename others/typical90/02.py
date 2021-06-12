import math
from functools import reduce
from collections import deque, defaultdict, Counter
import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def valid(s):
    l = 0
    r = 0
    for c in s:
        if c == "(":
            l += 1
        else:
            r += 1
        if l < r:
            return False
    return l == r

def main():
    n = INT()

    def dfs(s):
        if len(s) == n:
            if valid(s):
                print(s)
            return

        for c in "()":
            dfs(s+c)
    
    dfs("(")

main()
