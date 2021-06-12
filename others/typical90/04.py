import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    h, w = INTS()
    grid = []
    for y in range(h):
        grid.append(INTS())
    
    hol_sum = [0] * h
    var_sum = [0] * w
    
    for y in range(h):
        for x in range(w):
            hol_sum[y] += grid[y][x]
            var_sum[x] += grid[y][x]
    
    ans = [[0] * w for _ in range(h)]

    for y in range(h):
        for x in range(w):
            ans[y][x] = hol_sum[y] + var_sum[x] - grid[y][x]
    
    for an in ans:
        print(*an)

main()
