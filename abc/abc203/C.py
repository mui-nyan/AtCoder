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

    n, k = INTS()
    friends = []
    for i in range(n):
        a,b = INTS()
        friends.append((a,b))
    friends.sort()
    friends = deque(friends)
    
    ans = k

    while friends:
        f = friends.popleft()
        if f[0] <= ans:
            ans += f[1]
        else:
            break
    
    print(ans)
    

main()
