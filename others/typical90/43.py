import sys
from collections import deque
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def get_next(x,y,d):
    ret = []
    ret.append((x, y-1, 0, d==0))
    ret.append((x+1, y, 1, d==1))
    ret.append((x, y+1, 0, d==0))
    ret.append((x-1, y, 1, d==1))
    return ret

def main():
    INF = 2**31-1

    h,w = INTS()
    sy,sx = INTS()
    gy,gx = INTS()
    sy-=1
    sx-=1
    gx-=1
    gy-=1

    grid = []
    for y in range(h):
        grid.append(input())

    # costs[d][y][x] = マス(x,y)に向き(d)で到達するときの最低コスト
    # d = 上下:0, 左右:1。後戻りする経路は考える必要がないので、2状態で足りる
    costs = [ [ [INF] * (w) for _ in range(h) ] for _ in range(2) ]

    # 壁があるマスはコストを最低にしておくことで探索されないようにする (探索時の壁チェックを省略できる)
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "#":
                for d in range(2):
                    costs[d][y][x] = -INF

    # 直進は0, 曲がりは1で01-BFS
    que = deque()
    que.append((0,sx,sy,0))
    que.append((0,sx,sy,1))
    while que:
        c,x,y,d = que.popleft()

        if c >= costs[d][y][x]:
            continue

        costs[d][y][x] = c
        # log(x,y,d)

        if x == gx and y == gy:
            print(c)
            return

        for nx, ny, nd, straight in get_next(x, y, d):
            if (nx<0 or nx>=w or ny<0 or ny>=h) or (c >= costs[nd][ny][nx]):
                continue

            if straight:
                # 直進はコスト変化なしで先頭に追加
                que.appendleft((c,nx,ny,nd))
            else:
                # 曲がりはコスト+1で末尾に追加
                que.append((c+1,nx,ny,nd))

main()
