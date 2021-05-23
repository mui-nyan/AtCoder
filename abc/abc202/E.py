from bisect import bisect_left
import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

def eulerTour(children, root=0):
    """オイラーツアーにより入時刻,出時刻,根からの距離を求めます。"""
    n = len(children)
    dist = [0] * (n)
    in_time = [0] * (n)
    out_time = [0] * (n)
    t = 0
    def dfs(u):
        nonlocal t
        in_time[u] = t
        for c in children[u]:
            t += 1
            dist[c] = dist[u] + 1
            dfs(c)
        t += 1
        out_time[u] = t
    dfs(root)

    return dist, in_time, out_time

def main():
    n = int(input())
    parent = [-1, -1] + get_nums_l()

    children = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        children[parent[i]].append(i)

    dist, in_time, out_time = eulerTour(children, 1)

    # from_dist[d] = 根からの距離がdである頂点の入時刻のリスト
    from_dist = [[] for _ in range(n+1)]
    for u,d in enumerate(dist):
        if u == 0:
            continue
        from_dist[d].append(in_time[u])
    for fd in from_dist:
        fd.sort()
    # log(from_dist)

    def solve(u,d):
        # 根からの距離がdで、かつuの子孫である頂点の個数を求める
        candidate = from_dist[d]

        u_in = in_time[u]
        u_out = out_time[u]

        # vがuの子孫である条件は、u_in < v_in < u_in

        return bisect_left(candidate, u_out) - bisect_left(candidate, u_in)

    q = int(input())

    for i in range(q):
        u,d = get_nums_l()
        print(solve(u,d))

main()
