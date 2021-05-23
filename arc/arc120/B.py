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

def main():
    INF = 999999999999999999999999
    MOD = 998244353

    h,w = INTS()
    grid = []
    for i in range(h):
        grid.append(input())
    
    fazys = 0
    for y in range(h+w-1):
        # log("---")
        ok = True
        fazy = False
        color = None
        for x in range(w):
            if y-x < 0 or y-x >= h:
                continue
            c = grid[y-x][x]
            if c == ".":
                fazy = True
            elif color != None:
                if color != c:
                    ok = False
                    break
            elif c != ".":
                color = c
        
        if ok:
            if fazy and color==None:
                fazys += 1
        else:
            print(0)
            return
    
    print(pow(2, fazys, MOD))

main()
