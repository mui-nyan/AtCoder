from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def main():
    INF = 999999999999999999999999

    n, m = INTS()
    edges = [[] for _ in range(n)]
    for i in range(m):
        a,b,c,d = INTS()
        a -= 1
        b -= 1
        edges[a].append((b,c,d))
        edges[b].append((a,c,d))
    
    que = [(0,0)]
    times = [INF] * (n)

    while que:
        time, u = heappop(que)
        # log(time,u)

        if time >= times[u]:
            continue
        times[u] = time

        if u == n-1:
            print(time)
            return

        for v,c,d in edges[u]:
            x = time+c+(d//(time+1))
            w = max(0, isqrt(d)-time)
            x = min(x, time + c + w + (d//(time+w+1)))
            heappush(que, (x, v))

    print(-1)

main()
