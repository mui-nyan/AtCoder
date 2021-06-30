import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

from heapq import heappush, heappop

def dijkstra_on_graph(edges, start, INF=2**31-1):
    """
    単一始点最短経路問題を解きます。
    edges[i] = ノードiから辿れる頂点とそのコストを束にしたタプルのリスト
    """
    n = len(edges)
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

def main():
    INF = 2**31-1

    n, m = INTS()
    edges = [ [] for _ in range(n+1+m) ]

    # T[i] = 研究者iの高橋数。高橋くんは研究者1で、高橋数0。
    T = [-1] * (n+1)
    T[1] = 0

    for i in range(m):
        k = INT()
        R = INTS()

        for r in R:
            edges[r].append((i+n+1, 1))
            edges[i+n+1].append((r, 1))

    costs = dijkstra_on_graph(edges, 1)

    for i in range(n):
        c = costs[i+1]
        c = -1 if c == INF else c//2
        print(c)

main()
