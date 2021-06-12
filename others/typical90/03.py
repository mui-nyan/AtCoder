import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    n = INT()
    edges = [[] for _ in range(n)]
    for i in range(n-1):
        a,b = INTS()
        a-=1
        b-=1
        edges[a].append(b)
        edges[b].append(a)
    
    def find_farthest_node(u):
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

    # 求めたいスコアは、木の直径 + 1 。
    # 適当な点から最も遠い点と、その点から最も遠い点の距離が木の直径になる
    m1, mu1 = find_farthest_node(0)
    m2, mu2 = find_farthest_node(mu1)
    print(m2+1)

main()
