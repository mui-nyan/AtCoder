from itertools import permutations
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    INF = 2**31-1

    n = INT()
    time = []
    for i in range(n):
        time.append(INTS())

    m = INT()
    bad = [ [False] * (n) for _ in range(n) ]
    for i in range(m):
        x,y = INTS()
        x-=1
        y-=1
        bad[x][y] = True
        bad[y][x] = True

    ans = INF
    for P in permutations(range(n)):
        ok = True
        for i in range(n-1):
            a = P[i]
            b = P[i+1]
            if bad[a][b]:
                ok = False
                break
        if ok:
            t = 0
            for i,p in enumerate(P):
                t += time[p][i]
            if t < ans:
                ans = t

    print(ans if ans!=INF else "-1")

main()
