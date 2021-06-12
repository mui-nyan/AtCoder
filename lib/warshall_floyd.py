def warshall_floyd(d):
    """
    全点対最短経路長を O(N^3) で求めます。
    d: 辺のコストを表す行列
        d[i][j] = 頂点iから頂点jを直接結ぶ辺のコスト。
        直接繋がっていない場合はINF。自身への辺は0。

    return すべての経路長を埋めたd。d自体も破壊的に変更します。
    """
    n = len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j]= min(d[i][j],d[i][k]+d[k][j])
    return d
