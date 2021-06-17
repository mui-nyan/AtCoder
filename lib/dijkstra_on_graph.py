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
