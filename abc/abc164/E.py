from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10**7)
from time import sleep

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(ss) for ss in input().split(" ")]

def rangeI(it, l, r):
    for i, e in enumerate(it):
        if l <= i < r:
            yield e
        elif l >= r:
            break

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

cdef int n,m,s,co,coin,city,max_coin,u,v,a,b
cdef long long time

n,m,s = get_nums_l()

# 銀貨所持枚数の上限。確実に最短経路を通過できる枚数
max_coin = 50*(n-1)
s = min(s, max_coin)

lines = list(map(lambda line: line.strip(), sys.stdin.readlines()))

# rails[i] = 都市iを始点とする路線情報(行き先, 運賃, 時間)
rails  = [ [] for _ in range(n + 1) ]
for line in rangeI(lines, 0, m):
    u,v,a,b = map(int, line.split())
    rails[u].append([v, a, b])
    rails[v].append([u, a, b])

cities = [None] + [ list(map(int, line.split())) for line in rangeI(lines, m, m+n) ]

# log("rails:", rails)
# log("cities:", cities)

# t = 目的地
# for t in range(2, n+1):
    # log("t:", t)

# table[i][j] = 現在頂点i, 銀貨j枚持っている場合の最小時間
table = [ [999999999999999999] * (max_coin + 1) for _ in range(n+1)]
hq = []
# 初期状態 時間0, 都市1, 銀貨s枚
heappush(hq, (0, 1, s))

check = {i for i in range(2, n+1) }

while hq:
    # sleep(0.1)
    time, city, coin,  = heappop(hq)

    # if city == t:
    #     print(time)
    #     break

    if table[city][coin] <= time:
        continue

    # for co in range(coin+1):
    #     if table[city][co] > time:
    #         table[city][co] = time

    table[city][coin] = time

    if city in check:
        check.remove(city)
        if len(check) == 0:
            break


    # log(city, coin, time)

    # ここで両替した場合 銀貨と時間を増やす
    # log("-", city, min(max_coin, coin+cities[city][0]), time + cities[city][1])
    heappush(hq, (time + cities[city][1], city, min(max_coin, coin+cities[city][0])))

    # 進める都市に進む
    for v, a, b in rails[city]:
        if coin < a:
            # 銀貨が足りないと移動できない
            continue
        # log("-", v, coin-a, time + b)
        heappush(hq, (time+b, v, coin-a))

for t in range(2, n+1):
    print(min(table[t]))
