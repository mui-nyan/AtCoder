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

    n = INT()
    A = INTS()

    m = max(A)
    s = 0

    ruisekiwa = [0] * (n+1)
    ruisekiMax = [0] * (n+1)
    for i,a in enumerate(A):
        ruisekiwa[i+1] = ruisekiwa[i] + A[i]
        ruisekiMax[i+1] = max(ruisekiMax[i], A[i])
    
    log(ruisekiwa)
    log(ruisekiMax)

    prev = 0
    for i in range(n):
        print(prev + ruisekiwa[i+1] + ruisekiMax[i+1] * (i+1))
        prev += ruisekiwa[i+1]
    

main()
