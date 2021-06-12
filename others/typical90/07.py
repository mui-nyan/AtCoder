from bisect import bisect_left
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    INF = 2**31-1
    n = INT()
    A = INTS() + [INF, -INF]
    A.sort()
    q = INT()
    for i in range(q):
        b = INT()
        x = bisect_left(A, b)
        fuman = min(
            abs(b - A[x]),
            abs(b - A[x-1])
        )
        print(fuman)

main()
