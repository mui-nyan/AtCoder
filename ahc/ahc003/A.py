from functools import reduce
import sys

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

from heapq import heappush, heappop

def neighbors4(x, y):
  dxy = (0, 1, 0, -1, 0 )
  for i in range(4):
    yield(x + dxy[i], y + dxy[i+1])

def toChar(x,y,nx,ny):
    if nx > x:
        return "R"
    elif nx < x:
        return "L"
    elif ny > y:
        return "D"
    else:
        return "U"

def toDxDy(c):
    if c=="R":
        return (1,0)
    if c=="L":
        return (-1,0)
    if c=="D":
        return (0,1)
    if c=="U":
        return (0,-1)

def main():
    INF = 999999999999999999999999
    MOD = 10**9+7

    costx = [ [4000] * 29 for _ in range(30) ]
    costy = [ [4000] * 30 for _ in range(29) ]
    updatesx = [ [0] * 29 for _ in range(30) ]
    updatesy = [ [0] * 30 for _ in range(29) ]

    def dijkstra(sx,sy, gx,gy):
        dist = [ [INF] * 30 for _ in range(30) ]
        hq = []
        hq.append((0, 0, sx, sy))
        while hq:

            _,c,x,y = heappop(hq)
            # log(" ", c,x,y)
            if c >= dist[y][x]:
                continue
            dist[y][x] = c

            if x == gx and y == gy:
                # 最短経路発見
                break

            for nx, ny in neighbors4(x, y):
                if nx >= 30 or ny >= 30 or nx<0 or ny<0:
                    continue
                if x != nx:
                    # 横移動
                    nc = c + costx[ny][min(x,nx)]
                else:
                    # 縦移動
                    nc = c + costy[min(y, ny)][nx]
                heappush(hq, (nc+(abs(gx-nx)+abs(gy-ny))*1000, nc, nx, ny))
        
        # この経路の予測距離
        estimated_dist = c

        # 最短経路の復元
        c = dist[gy][gx]
        x,y = gx,gy
        route = []
        while x != sx or y != sy:
            for nx, ny in neighbors4(x, y):
                if nx >= 30 or ny >= 30 or nx<0 or ny<0:
                    continue
                if x != nx:
                    # 横移動
                    d = costx[ny][min(x,nx)]
                else:
                    # 縦移動
                    d = costy[min(y,ny)][nx]
                if c-d == dist[ny][nx]:
                    # 戻り経路なのでnxnyとxyを逆に与える
                    route.append(toChar(nx,ny,x,y))
                    c = c-d
                    x,y = nx, ny

        return route[::-1], estimated_dist

    def update(sx, sy, route, diff_per_len):
        x,y = sx,sy
        for r in route:
            dx,dy = toDxDy(r)
            cx = min(x,x+dx)
            cy = min(y,y+dy)
            if dx != 0:
                # 横
                # up = updatesx[cy][cx]
                # costx[cy][cx] = min(9000, max(1000, costx[cy][cx]+int(diff_per_len * 1.5 * (0.9 ** (up)))))
                costx[cy][cx] = min(9000, max(1000, costx[cy][cx]+int(diff_per_len * 1.5 * (0.998 ** (k)))))
                # updatesx[cy][cx] += 1
                # log(ch, up, int(ch * (2 ** (-up))))
                # costx[cy][cx] = min(9000, max(1000, costx[cy][cx] + diff_per_len))
            else:
                # 縦
                # up = updatesy[cy][cx]
                # costy[cy][cx] = min(9000, max(1000, costy[cy][cx] + int(diff_per_len * 1.5 * (0.9 ** (up)))))
                costy[cy][cx] = min(9000, max(1000, costy[cy][cx] + int(diff_per_len * 1.5 * (0.998 ** (k)))))
                # updatesy[cy][cx] += 1
                # log(ch, up, int(ch * (2 ** (-up))))
                # costy[cy][cx] = min(9000, max(1000, costy[cy][cx] + diff_per_len))

            x,y = x+dx, y+dy

    # クエリ1000個
    for k in range(1000):
        sy, sx, gy, gx = get_nums_l()

        route, estimated_dist = dijkstra(sx, sy, gx, gy)
        print(*route, sep="", flush=True)

        real_dist = int(input())
        diff = real_dist - estimated_dist
        diff_per_len = diff // len(route)
        update(sx, sy, route, diff_per_len)

main()
