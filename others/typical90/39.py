import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

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

def main():
    n = INT()

    edges = [ [] for _ in range(n) ]
    for i in range(n-1):
        a,b = INTS()
        a-=1
        b-=1
        edges[a].append(b)
        edges[b].append(a)

    children = conv_edges_to_tree_with_root(edges, 0)
    
    memo = [0] * (n)
    def dfs(u):
        """"頂点u以下の部分木に含まれる頂点数を返しつつ、メモに記録します。"""
        ret = 1
        for v in children[u]:
            ret += dfs(v)
        memo[u] = ret
        return ret
    dfs(0)

    # ある辺の「答えへの貢献度」は、 x = その辺の下側の部分木に含まれる頂点数 としたときの x * (n-x) 。

    ans = 0
    for u in range(1,n):
        ans += memo[u] * (n-memo[u])

    print(ans)

main()
