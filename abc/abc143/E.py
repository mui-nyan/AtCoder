import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def warshall_floyd(d):
    n = len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j]= min(d[i][j],d[i][k]+d[k][j])
    return d

def main():
    INF = 2**31-1

    n, m, l = INTS()

    # dist[i][j] = 街iから街jまでの距離(到達不可能はINF)
    dist = [ [INF] * n for _ in range(n) ]
    for i in range(n):
        dist[i][i] = 0

    for i in range(m):
        a,b,c = INTS()
        a -= 1
        b -= 1
        dist[a][b] = c
        dist[b][a] = c

    warshall_floyd(dist)

    # 補給無しで行ける範囲だけにコスト1の辺を貼る
    dist2 = [ [INF] * n for _ in range(n) ]
    for i in range(n):
        dist[i][i] = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if dist[i][j] <= l:
                dist2[i][j] = 1
            if dist[j][i] <= l:
                dist2[j][i] = 1
    warshall_floyd(dist2)
    
    for q in range(INT()):
        s,t = INTS()
        s -= 1
        t -= 1

        if dist2[s][t] != INF:
            print(dist2[s][t] - 1)
        else:
            print(-1)

main()
