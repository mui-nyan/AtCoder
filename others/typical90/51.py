from collections import defaultdict
from bisect import bisect_right
import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args): print("DEBUG:", *args, file=sys.stderr)

def main():
    n,k,p = INTS()
    A = INTS()

    if n == 1:
        print(1 if A[0] <= p else 0)
        return
    
    L = A[:n//2]
    R = A[n//2:]

    # log(L)
    # log(R)

    n_l = len(L)
    n_r = len(R)

    X = defaultdict(list)

    for bits in range(2**n_l):
        cost = 0
        picked = 0
        for i in range(n_l):
            if bits >> i & 1 != 0:
                picked += 1
                cost += L[i]
        X[picked].append(cost)
    
    for x in X.values():
        x.sort()

    # log(X)

    ans = 0
    for bits in range(2**n_r):
        cost = 0
        picked = 0
        for i in range(n_r):
            if bits >> i & 1 != 0:
                picked += 1
                cost += R[i]
        if picked > k or cost > p:
            continue
        # log(bits, bisect_right(X[k - picked], p-cost))
        ans += bisect_right(X[k - picked], p-cost)
    
    print(ans)

main()
