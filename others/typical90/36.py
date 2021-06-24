import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def find(pred, iter):
    return next(filter(pred, iter), None)

def main():
    INF = 2**31-1

    n, q = INTS()

    P = []
    for i in range(n):
        # 45°回転して考える
        x,y = INTS()
        x,y = x-y, x+y
        P.append((x,y))
    
    xmin = INF
    xmax = -INF
    ymin = INF
    ymax = -INF

    for x,y in P:
        xmin = min(xmin, x)
        xmax = max(xmax, x)
        ymin = min(ymin, y)
        ymax = max(ymax, y)

    selected = []
    selected.append(find(lambda p: p[0] == xmin, P))
    selected.append(find(lambda p: p[0] == xmax, P))
    selected.append(find(lambda p: p[1] == ymin, P))
    selected.append(find(lambda p: p[1] == ymax, P))

    for _ in range(q):
        i = INT()
        i -= 1
        x,y = P[i]

        ans = 0
        for x2,y2 in selected:
            # 回転前のマンハッタン距離 = 回転後のチェビシェフ距離
            dist = max(abs(x-x2), abs(y-y2))
            if dist > ans:
                ans = dist
        print(ans)

main()
