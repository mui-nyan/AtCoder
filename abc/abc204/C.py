import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    n, m = INTS()
    edges = [[] for _ in range(n)]
    for i in range(m):
        a,b = INTS()
        a-=1
        b-=1
        edges[a].append(b)
    
    # log(edges)
    
    def dfs(u, reachable):
        # reachable = set()
        # log(u, reachable)
        if u in reachable:
            return reachable
        reachable.add(u)
        for v in edges[u]:
            dfs(v, reachable)
        return reachable

    ans = 0

    for start in range(n):
        reachable = dfs(start, set())
        # log("X", start, reachable)
        ans += len(reachable)

    print(ans)

main()
