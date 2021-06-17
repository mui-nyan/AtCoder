import sys
sys.setrecursionlimit(10**7)
from heapq import heappush, heappop
def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    INF = 2**31-1

    n, m = INTS()
    edges = [ [] for _ in range(n) ]
    for i in range(m):
        a,b,c = INTS()
        a-=1
        b-=1
        edges[a].append((b,c))
        edges[b].append((a,c))
    
    def dijkstra(start):
        costs = [INF] * n

        hq = []
        hq.append((0, start))

        while hq:
            cost, u = heappop(hq)

            if cost >= costs[u]:
                continue
            costs[u] = cost

            for v, c in edges[u]:
                heappush(hq, (cost + c, v))

        return costs
    
    costs_from_0 = dijkstra(0)
    costs_from_n_minus_1 = dijkstra(n-1)

    for k in range(0,n):
        print(costs_from_0[k] + costs_from_n_minus_1[k])

main()
