def conv_edges_to_tree_with_root(edges, root):
    """隣接リストを根付き木に変換します。"""
    n = len(edges)
    children = [ [] for _ in range(n) ]
    def dfs(u, prev):
        for v in edges[u]:
            if v != prev:
                children[u].append(v)
                dfs(v, u)
    dfs(root, -1)
    return children
