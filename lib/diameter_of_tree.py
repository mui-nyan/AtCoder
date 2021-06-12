def diameter_of_tree(edges):
    """
    木の直径を求めて返します。
    edges: 隣接リスト。 edges[i] = 頂点iから直接繋がっている頂点のリスト。
    """
    def find_farthest_node(u):
        """
        ある頂点から最も遠い点とその距離を返します。
        return: (距離, 最遠の頂点)
        """
        def dfs(u, dist, prev):
            m = dist
            mu = u
            for v in edges[u]:
                # 逆流を防ぐ
                if v != prev:
                    m2,mu2 = dfs(v, dist+1, u)
                    if m2 > m:
                        m = m2
                        mu = mu2
            return m,mu

        return dfs(u, 0, set())

    # 適当な点から最も遠い点と、その点から最も遠い点の距離が木の直径になる
    m1, mu1 = find_farthest_node(0)
    m2, mu2 = find_farthest_node(mu1)
    return m2

