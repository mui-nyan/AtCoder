import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

def main():
    INF = 999999999999999999999999
    MOD = 10**9+7

    n = int(input())
    edge = [[]for i in range(n+1)]
    weight = [[]for i in range(n+1)]
    for i in range(n-1):
        u,v,w = get_nums_l()
        edge[u].append(v)
        edge[v].append(u)
        weight[u].append(w)
        weight[v].append(w)

    dist = [-1]*(n+1)
    root = 1
    dist[root] = 0
    que = deque([root])

    while que:
        now = que.popleft()
        for i in range(len(edge[now])):
            nex = edge[now][i]
            if dist[nex] == -1:
                dist[nex] = dist[now]^weight[now][i]
                que.append(nex)

    ans = 0
    for k in range(60):
        # count[x] = dist[i]のkビット目がxであるようなiの個数
        count = [0, 0]
        for i in range(1, n+1):
            count[ (dist[i] >> k) & 1 ] += 1
        ans += 2**k * (count[0] * count[1])
        ans %= MOD
    print(ans)
main()
