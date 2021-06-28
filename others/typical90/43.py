import sys
from collections import deque
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def get_next(x,y,d):
    ret = []
    if d != 2:
        ret.append((x, y-1, 0, d==0))
    if d != 3:
        ret.append((x+1, y, 1, d==1))
    if d != 0:
        ret.append((x, y+1, 2, d==2))
    if d != 1:
        ret.append((x-1, y, 3, d==3))
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
    # d = 上:0, 右:1, 下:2, 左:3
    costs = [ [ [INF] * (w) for _ in range(h) ] for _ in range(4) ]

    # 壁があるマスはコストを最低にしておくことで探索されないようにする (探索時の壁チェックを省略できる)
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "#":
                for d in range(4):
                    costs[d][y][x] = -INF

    # 直進は0, 曲がりは1で01-BFS
    que = deque()
    que.append((0,sx,sy,0))
    que.append((0,sx,sy,1))
    que.append((0,sx,sy,2))
    que.append((0,sx,sy,3))
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
