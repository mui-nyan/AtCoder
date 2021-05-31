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
    MOD = 10**9+7

    n, m = INTS()
    blacks = []
    for i in range(m):
        blacks.append(INTS())
    
    blacks.sort()
    blacks.append((INF,INF))

    # 到達可能なY座標の集合
    reachable = set([n])

    prev_x = None
    current_blacks = []
    for x,y in blacks:
        if x != prev_x:
            adds = set()
            removes = set()
            for _,y2 in current_blacks:
                # 到達可能の隣マスに黒があったら到達可能にする
                if y2 not in reachable and (y2-1 in reachable or y2+1 in reachable):
                    adds.add(y2)

                # 隣が到達可能でない到達可能マスに黒があったら行き止まり
                if y2 in reachable and (y2-1 not in reachable and y2+1 not in reachable):
                    removes.add(y2)
            
            for a in adds:
                reachable.add(a)
            for r in removes:
                reachable.remove(r)

            current_blacks = [(x,y)]
            prev_x = x
        else:
            current_blacks.append((x,y))
    
    print(len(reachable))

main()
