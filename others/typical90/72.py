import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def neighbors4(x, y):
    dxy = ( (0,1), (1,0), (0,-1), (-1,0) )
    for dx,dy in dxy:
        yield(x + dx, y + dy)

def main():
    h,w = INTS()
    grid = []
    for i in range(h):
        grid.append(input())

    history=set()
    def dfs(x,y,gx,gy,n):
        history.add((x,y))
        kmax = 0
        for nx,ny in neighbors4(x,y):
            if nx<0 or nx>=w or ny<0 or ny>=h:
                continue
            if nx == gx and ny == gy:
                kmax = n+1
            elif grid[ny][nx] == "." and (nx,ny) not in history:
                k = dfs(nx,ny,gx,gy,n+1)
                if k > kmax:
                    kmax = k

        history.remove((x,y))
        # log(x,y,kmax)
        return kmax

    ans = -1
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "#":
                continue
            log("Start",x,y)
            k = dfs(x,y,x,y,0)
            if k > 2 and k > ans:
                ans = k

    print(ans)

main()
