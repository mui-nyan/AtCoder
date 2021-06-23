import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    n = INT()
    edges = [ [] for _ in range(n)]

    for i in range(n-1):
        a,b = INTS()
        a-=1
        b-=1
        edges[a].append(b)
        edges[b].append(a)

    def dfs(init_ok):
        marks = []
        stack = []
        stack.append((0, init_ok, -1))
        while stack:
            u,ok,prev = stack.pop()
            if ok:
                marks.append(u)
            for v in edges[u]:
                if v != prev:
                    stack.append((v, not ok, u))
        return marks

    x = dfs(False)
    y = dfs(True)

    z = x if len(x) > len(y) else y

    if len(z) > n//2:
        z = z[:n//2]

    print(" ".join(map(lambda u:str(u+1), z)))

main()
